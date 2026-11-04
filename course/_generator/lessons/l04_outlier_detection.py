"""Lesson 04 - Outlier detection."""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import GRAFANA_DS, PALETTE, Book, Dash, md, write_csv  # noqa: E402

SLUG = "04-outlier-detection"
TITLE = "Outlier detection"
MODULE = "Understanding data beyond averages"
DATASET = "300 purchase-order lines (category, quantity, unit price, amount) with decimal slips and genuine bulk orders"
ZTHR, IQRK, MZTHR, PRATIO = 3.0, 1.5, 3.5, 5.0
CATS = ["stationery", "lab_supplies", "it_hardware"]


def make_data() -> pd.DataFrame:
    rng = np.random.default_rng(404)
    n = 300
    cat = rng.choice(CATS, size=n, p=[0.4, 0.4, 0.2])
    mu = {"stationery": 4.0, "lab_supplies": 25.0, "it_hardware": 180.0}
    sg = {"stationery": 0.30, "lab_supplies": 0.35, "it_hardware": 0.35}
    qr = {"stationery": (5, 60), "lab_supplies": (2, 25), "it_hardware": (1, 6)}
    price = np.array([rng.lognormal(np.log(mu[c]), sg[c]) for c in cat]).round(2)
    qty = np.array([rng.integers(qr[c][0], qr[c][1], endpoint=True) for c in cat])
    idx = rng.permutation(n)
    up, down, bulk = idx[:8], idx[8:11], idx[11:18]
    price[up] = (price[up] * 100).round(2)  # decimal slip: 12.50 typed as 1250.00
    hw = np.where(cat == "it_hardware")[0]
    down = np.array([i for i in hw if i not in set(up) | set(bulk)])[:3]
    price[down] = (price[down] / 100).round(2)  # decimal slip the other way
    for i in bulk:  # genuine bulk orders: normal price, 12-20x normal quantity
        qty[i] = int(qty[i] * rng.choice([12, 15, 20]))
    amount = (qty * price).round(2)
    day = np.sort(rng.integers(0, 60, n))
    date = pd.Timestamp("2026-02-02") + pd.to_timedelta(day, unit="D")
    return pd.DataFrame({"line_id": np.arange(1, n + 1), "date": date, "category": cat, "quantity": qty,
                         "unit_price_eur": price, "amount_eur": amount})


def xy_two_frames(d: Dash, title: str, frames: list[tuple[str, pd.DataFrame]], x: str, y: str, description: str,
                  colors: list[str], w: int = 12, h: int = 9) -> None:
    """XY chart whose series come from separate frames (no NaN padding needed): one target per series."""
    targets = []
    series = []
    overrides = []
    for i, (name, f) in enumerate(frames):
        ref = "ABCDEFGH"[i]
        targets.append({"refId": ref, "datasource": GRAFANA_DS, "scenarioId": "csv_content",
                        "csvContent": f[[x, y]].rename(columns={y: name}).to_csv(index=False, float_format="%.6g")})
        series.append({"x": x, "y": name, "frame": i, "name": name, "color": {"fixed": colors[i]}})
        overrides.append({"matcher": {"id": "byName", "options": name}, "properties": [
            {"id": "color", "value": {"mode": "fixed", "fixedColor": colors[i]}}]})
    d._add({"type": "xychart", "title": title, "description": description, "datasource": GRAFANA_DS,
            "targets": targets,
            "fieldConfig": {"defaults": {"custom": {"show": "points", "pointSize": {"fixed": 7}}}, "overrides": overrides},
            "options": {"mapping": "manual", "series": series, "legend": {"displayMode": "list", "placement": "bottom"}}}, w, h)


def build(out: Path) -> Book:
    df = make_data()
    write_csv(out, df)
    n = len(df)
    amt = df["amount_eur"].to_numpy()
    sd = lambda v: float(np.std(v, ddof=1))
    q = lambda v, p: float(np.percentile(v, p))

    b = Book(df, "Lesson 04 - Outlier detection",
             "Solved workbook. Yellow cells are assumptions you can change; everything else is a live formula.")
    loc = b.local
    cat_c, qty_c, up_c = b.col("category"), b.col("quantity"), b.col("unit_price_eur")
    AMT = b.rng("amount_eur")

    b.section("0. Decision thresholds (edit and watch the counts change)")
    zthr = b.row("z-score threshold", ZTHR, None, "0.0", "|z| > threshold is flagged", is_input=True)
    iqrk = b.row("Tukey fence multiplier k", IQRK, None, "0.0", "fences Q1 - k IQR, Q3 + k IQR (1.5 inner, 3 outer)", is_input=True)
    mzthr = b.row("Modified z threshold", MZTHR, None, "0.0", "Iglewicz-Hoaglin recommendation", is_input=True)
    pratio = b.row("Price-ratio limit for 'price error'", PRATIO, None, "0.0",
                   "unit price more than 5x or less than 1/5 of the category median", is_input=True)

    # ----------------------------------------------------- context: unit price vs category median
    b.section("1. Context: is the unit price plausible for the category?")
    cat_med = {}
    for c in CATS:
        b.add_column(f"up_{c}", lambda r, c=c: f'=IF(Data!{cat_c}{r}="{c}",Data!{up_c}{r},"")')
        cat_med[c] = b.row(f"Median unit price, {c} (EUR)", f"=MEDIAN({b.rng('up_' + c)})",
                           float(np.median(df.loc[df.category == c, "unit_price_eur"])), "0.00")
    med_of = {c: float(np.median(df.loc[df.category == c, "unit_price_eur"])) for c in CATS}
    ratio = (df["unit_price_eur"] / df["category"].map(med_of)).to_numpy()
    is_err = ((ratio > PRATIO) | (ratio < 1 / PRATIO)).astype(int)
    abs_ref = lambda cell: "Analysis!$B$" + cell.split("$")[-1]
    b.add_column("price_ratio", lambda r: (f'=Data!{up_c}{r}/IF(Data!{cat_c}{r}="stationery",{abs_ref(cat_med["stationery"])},'
                                           f'IF(Data!{cat_c}{r}="lab_supplies",{abs_ref(cat_med["lab_supplies"])},{abs_ref(cat_med["it_hardware"])}))'),
                 expected=ratio, fmt="0.00")
    PR = b.col("price_ratio")
    b.add_column("price_error", lambda r: f"=IF(OR(Data!{PR}{r}>{abs_ref(pratio)},Data!{PR}{r}<1/{abs_ref(pratio)}),1,0)",
                 expected=is_err, fmt="0")
    ERR = b.rng("price_error")
    b.row("Lines whose unit price is implausible (price errors)", f"=SUM({ERR})", int(is_err.sum()), "0")
    b.row("... of which price too high (decimal slip up)", f"=COUNTIF({b.rng('price_ratio')},\">\"&{loc(pratio)})",
          int((ratio > PRATIO).sum()), "0")
    b.row("... of which price too low (decimal slip down)", f"=COUNTIF({b.rng('price_ratio')},\"<\"&1/{loc(pratio)})",
          int((ratio < 1 / PRATIO).sum()), "0")

    # ----------------------------------------------------- generic detection block
    flags = {}

    def block(tag: str, col: str, v: np.ndarray, title: str, fmt: str):
        b.section(title)
        R = b.rng(col)
        L = b.col(col)
        mean = b.row("Mean", f"=AVERAGE({R})", v.mean(), fmt)
        s = b.row("Standard deviation (STDEV.S)", f"=STDEV({R})", sd(v), fmt)
        med = b.row("Median", f"=MEDIAN({R})", float(np.median(v)), fmt)
        b.add_column(f"absdev_{tag}", lambda r: f"=ABS(Data!{L}{r}-{abs_ref(med)})", expected=np.abs(v - np.median(v)), fmt=fmt)
        mad = b.row("MAD", f"=MEDIAN({b.rng('absdev_' + tag)})", float(np.median(np.abs(v - np.median(v)))), fmt)
        q1 = b.row("Q1", f"=QUARTILE({R},1)", q(v, 25), fmt)
        q3 = b.row("Q3", f"=QUARTILE({R},3)", q(v, 75), fmt)
        iqr = b.row("IQR", f"={loc(q3)}-{loc(q1)}", q(v, 75) - q(v, 25), fmt)
        m_, s_, md_, mad_ = v.mean(), sd(v), float(np.median(v)), float(np.median(np.abs(v - np.median(v))))
        q1_, q3_ = q(v, 25), q(v, 75)
        iq = q3_ - q1_
        zhi = b.row("z-score upper limit (mean + threshold x SD)", f"={loc(mean)}+{loc(zthr)}*{loc(s)}", m_ + ZTHR * s_, fmt)
        zlo = b.row("z-score lower limit", f"={loc(mean)}-{loc(zthr)}*{loc(s)}", m_ - ZTHR * s_, fmt)
        fhi = b.row("Inner fence, upper (Q3 + k IQR)", f"={loc(q3)}+{loc(iqrk)}*{loc(iqr)}", q3_ + IQRK * iq, fmt)
        flo = b.row("Inner fence, lower (Q1 - k IQR)", f"={loc(q1)}-{loc(iqrk)}*{loc(iqr)}", q1_ - IQRK * iq, fmt)
        mzhi = b.row("Modified-z upper limit (median + thr x MAD / 0.6745)", f"={loc(med)}+{loc(mzthr)}*{loc(mad)}/0.6745",
                     md_ + MZTHR * mad_ / 0.6745, fmt)
        mzlo = b.row("Modified-z lower limit", f"={loc(med)}-{loc(mzthr)}*{loc(mad)}/0.6745", md_ - MZTHR * mad_ / 0.6745, fmt)
        z = (v - m_) / s_
        mz = 0.6745 * (v - md_) / mad_
        b.add_column(f"z_{tag}", lambda r: f"=(Data!{L}{r}-{abs_ref(mean)})/{abs_ref(s)}", expected=z, fmt="0.00")
        b.add_column(f"mz_{tag}", lambda r: f"=0.6745*(Data!{L}{r}-{abs_ref(med)})/{abs_ref(mad)}", expected=mz, fmt="0.00")
        fz = (np.abs(z) > ZTHR).astype(int)
        fi = ((v < q1_ - IQRK * iq) | (v > q3_ + IQRK * iq)).astype(int)
        fm = (np.abs(mz) > MZTHR).astype(int)
        Z, M = b.col(f"z_{tag}"), b.col(f"mz_{tag}")
        b.add_column(f"flag_z_{tag}", lambda r: f"=IF(ABS(Data!{Z}{r})>{abs_ref(zthr)},1,0)", expected=fz, fmt="0")
        b.add_column(f"flag_iqr_{tag}", lambda r: f"=IF(OR(Data!{L}{r}<{abs_ref(flo)},Data!{L}{r}>{abs_ref(fhi)}),1,0)",
                     expected=fi, fmt="0")
        b.add_column(f"flag_mz_{tag}", lambda r: f"=IF(ABS(Data!{M}{r})>{abs_ref(mzthr)},1,0)", expected=fm, fmt="0")
        nz = b.row("Flagged by z-score", f"=SUM({b.rng('flag_z_' + tag)})", int(fz.sum()), "0")
        ni = b.row("Flagged by Tukey inner fences", f"=SUM({b.rng('flag_iqr_' + tag)})", int(fi.sum()), "0")
        nm = b.row("Flagged by modified z", f"=SUM({b.rng('flag_mz_' + tag)})", int(fm.sum()), "0")
        flags[tag] = dict(z=z, mz=mz, fz=fz, fi=fi, fm=fm, mean=m_, sd=s_, med=md_, mad=mad_, q1=q1_, q3=q3_, iqr=iq,
                          zhi=m_ + ZTHR * s_, fhi=q3_ + IQRK * iq, flo=q1_ - IQRK * iq, mzhi=md_ + MZTHR * mad_ / 0.6745,
                          cells=dict(nz=nz, ni=ni, nm=nm, mean=mean, sd=s, med=med, mad=mad, q1=q1, q3=q3, iqr=iqr, zhi=zhi, fhi=fhi,
                                     mzhi=mzhi, zlo=zlo, flo=flo, mzlo=mzlo))
        return flags[tag]

    cb = b.col("amount_eur")
    A = block("amt", "amount_eur", amt, "2. Detection on the raw amount (EUR)", "#,##0.00")
    # outer fences + extra rows
    ofhi = A["q3"] + 3 * A["iqr"]
    nout = int(((amt > ofhi) | (amt < A["q1"] - 3 * A["iqr"])).sum())
    outer = b.row("Flagged by Tukey OUTER fences (k = 3)",
                  f"=COUNTIF({AMT},\">\"&({loc(A['cells']['q3'])}+3*{loc(A['cells']['iqr'])}))+COUNTIF({AMT},\"<\"&({loc(A['cells']['q1'])}-3*{loc(A['cells']['iqr'])}))",
                  nout, "0")
    fz, fi, fm = A["fz"], A["fi"], A["fm"]
    b.section("3. Masking and agreement between the rules (raw amount)")
    FZ, FI, FM = b.rng("flag_z_amt"), b.rng("flag_iqr_amt"), b.rng("flag_mz_amt")
    both = b.row("Flagged by z AND modified z", f"=COUNTIFS({FZ},1,{FM},1)", int(((fz == 1) & (fm == 1)).sum()), "0")
    onlym = b.row("Flagged by modified z but MISSED by z (masked)", f"=COUNTIFS({FZ},0,{FM},1)", int(((fz == 0) & (fm == 1)).sum()), "0")
    onlyz = b.row("Flagged by z only", f"=COUNTIFS({FZ},1,{FM},0)", int(((fz == 1) & (fm == 0)).sum()), "0")
    sd_ratio = b.row("SD / robust SD (1.4826 MAD) of the amount",
                     f"={loc(A['cells']['sd'])}/(1.4826*{loc(A['cells']['mad'])})", A["sd"] / (1.4826 * A["mad"]), "0.0",
                     "how far the SD is inflated by the outliers themselves")

    # ln_amount must exist as a Data column first
    b.add_column("ln_amount", lambda r: f"=LN(Data!{cb}{r})", expected=np.log(amt), fmt="0.000")
    LN = block("ln", "ln_amount", np.log(amt), "4. Detection on ln(amount)", "0.000")

    # ----------------------------------------------------- confusion table
    b.section("5. Which rule finds the price errors? (price error = unit price implausible for its category)")
    rows, exp = [], {}
    methods = [("z-score, raw", "flag_z_amt", A["fz"]), ("Tukey 1.5 IQR, raw", "flag_iqr_amt", A["fi"]),
               ("Modified z, raw", "flag_mz_amt", A["fm"]), ("z-score, ln", "flag_z_ln", LN["fz"]),
               ("Tukey 1.5 IQR, ln", "flag_iqr_ln", LN["fi"]), ("Modified z, ln", "flag_mz_ln", LN["fm"])]
    conf = {}
    for i, (name, col, f) in enumerate(methods):
        Fr = b.rng(col)
        rows.append([name, f"=SUM({Fr})", f"=COUNTIFS({Fr},1,{ERR},1)", f"=COUNTIFS({Fr},1,{ERR},0)", f"=COUNTIFS({Fr},0,{ERR},1)"])
        caught, fa, missed = int(((f == 1) & (is_err == 1)).sum()), int(((f == 1) & (is_err == 0)).sum()), int(((f == 0) & (is_err == 1)).sum())
        exp.update({(i, 1): int(f.sum()), (i, 2): caught, (i, 3): fa, (i, 4): missed})
        conf[name] = (int(f.sum()), caught, fa, missed)
    c0, c1 = b.table(["Rule", "Flagged", "Price errors caught", "Legit lines flagged", "Price errors missed"], rows, expect=exp)
    b.bar_chart_from_table("Price errors caught / missed and false alarms by rule", 1, [3, 4, 5], c0, c1, anchor="H4",
                           x_title="rule", y_title="lines")

    b.section("6. What deleting does to the numbers")
    cA = A["cells"]
    tot = b.row("Total spend, all lines (EUR)", f"=SUM({AMT})", amt.sum(), "#,##0")
    t_ok = b.row("Total spend without the price errors (EUR)", f"=SUMIFS({AMT},{ERR},0)", float(amt[is_err == 0].sum()), "#,##0")
    t_mz = b.row("Total spend without every line flagged by modified z (EUR)", f"=SUMIFS({AMT},{FM},0)", float(amt[fm == 0].sum()), "#,##0")
    lost = b.row("Legitimate spend deleted by the modified-z rule (EUR)", f"=SUMIFS({AMT},{FM},1,{ERR},0)",
                 float(amt[(fm == 1) & (is_err == 0)].sum()), "#,##0", "genuine bulk orders")
    legit_n = b.row("Legitimate lines deleted by the modified-z rule", f"=COUNTIFS({FM},1,{ERR},0)", int(((fm == 1) & (is_err == 0)).sum()), "0")
    m_ok = b.row("Mean amount without the price errors (EUR)", f"=AVERAGEIFS({AMT},{ERR},0)", float(amt[is_err == 0].mean()), "0.00")
    m_mz = b.row("Mean amount without modified-z flagged lines (EUR)", f"=AVERAGEIFS({AMT},{FM},0)", float(amt[fm == 0].mean()), "0.00")
    b.row("Mean amount, all lines (EUR)", f"={loc(cA['mean'])}", A["mean"], "0.00")
    ok_amt = amt[is_err == 0]

    n_err = int(is_err.sum())
    n_hi = int((ratio > PRATIO).sum())
    big4 = float(np.sort(amt)[::-1][0])
    b.answers([
        ("Mean, SD, median, MAD, Q1, Q3, IQR of the amount", f"={cA['sd']}",
         f"Mean {A['mean']:.0f}, SD {A['sd']:.0f}, median {A['med']:.0f}, MAD {A['mad']:.0f}, Q1 {A['q1']:.0f}, Q3 {A['q3']:.0f}, IQR {A['iqr']:.0f} EUR. "
         f"The SD is {A['sd'] / (1.4826 * A['mad']):.0f}x the robust SD: the outliers inflate the very yardstick used to detect them."),
        ("z-score rule (|z| > 3): count, limit, largest amount", f"={cA['nz']}",
         f"{int(fz.sum())} lines exceed |z| > 3 (upper limit {A['zhi']:.0f} EUR, largest amount {big4:.0f} EUR)."),
        ("Tukey fences: limits and counts for k = 1.5 and k = 3", f"={cA['ni']}",
         f"Upper inner fence {A['fhi']:.0f} EUR flags {int(fi.sum())} lines; outer fences (k = 3, {ofhi:.0f} EUR) flag {nout}. "
         "Most of the extra flags are legitimate high-value hardware or bulk lines: the amount is right-skewed, so fences on the raw scale over-flag."),
        ("Modified z (> 3.5): count and limit", f"={cA['nm']}",
         f"{int(fm.sum())} lines (limit {A['mzhi']:.0f} EUR). The MAD barely notices the extremes, so the limit is far tighter than the z-score limit."),
        ("Masking: lines flagged by modified z but missed by z", f"={onlym}",
         f"{int(((fz == 0) & (fm == 1)).sum())} lines are missed by the z-score. Once a few huge values inflate the SD, only still-larger values exceed 3 SD: masking."),
        ("The three rules on ln(amount)", f"={LN['cells']['nz']}",
         f"z-score {int(LN['fz'].sum())}, Tukey {int(LN['fi'].sum())}, modified z {int(LN['fm'].sum())} (vs {int(fz.sum())}, {int(fi.sum())}, {int(fm.sum())} on the raw scale). "
         "On the log scale the rules agree much better because the amounts are close to lognormal."),
        ("Category median unit price, price ratio, count of price errors and how many of the modified-z flags are errors", f"={cA['nm']}",
         f"{n_err} lines have an implausible price ({n_hi} too high, {n_err - n_hi} too low). Of the {int(fm.sum())} lines flagged by modified z, "
         f"{int(((fm == 1) & (is_err == 1)).sum())} are price errors and {int(((fm == 1) & (is_err == 0)).sum())} are genuine large orders at a normal unit price."),
        ("Table: errors caught, false alarms, errors missed per rule", f"=Analysis!C{c0 + 2}",
         "; ".join(f"{k}: caught {v[1]}/{n_err}, false alarms {v[2]}" for k, v in conf.items()) + ". No amount-only rule separates errors from big orders; the unit price does."),
        ("Total and mean spend after deleting everything flagged by modified z versus only the price errors", f"={lost}",
         f"Deleting every modified-z flag removes {float(amt[(fm == 1) & (is_err == 0)].sum()):,.0f} EUR of legitimate spend ({int(((fm == 1) & (is_err == 0)).sum())} genuine bulk orders) "
         f"and gives total {amt[fm == 0].sum():,.0f}; deleting only the price errors gives {amt[is_err == 0].sum():,.0f}. Mean amount {amt[is_err == 0].mean():.0f} vs {amt[fm == 0].mean():.0f} EUR."),
        ("Interpretation: judge or delete?", "see text",
         "A statistical flag says 'unusual', not 'wrong'. Here the decision comes from context (unit price vs category), and the right action differs: "
         "correct the decimal slips (a fix, not a deletion), keep the bulk orders, and document the rule. Limitations: the price-ratio rule itself is a "
         "threshold, categories with few lines have noisy medians, and an error that keeps a plausible price (wrong quantity) would be invisible to every rule used here."),
    ])

    # ------------------------------------------------------------------- grafana
    d = Dash("stats-04-outlier-detection", "04 · Outlier detection",
             "Three outlier rules on purchase-order amounts: masking, false alarms on skewed data, and the context (unit price) "
             "that separates errors from genuine bulk orders (values computed from data.csv).", df.rename(columns={"date": "time"}), "time")
    d.stat("Lines flagged on the raw amount (of 300)",
           {"z-score |z|>3": int(fz.sum()), "Tukey 1.5 IQR": int(fi.sum()), "modified z > 3.5": int(fm.sum()),
            "true price errors": n_err, "z-score missed errors": conf["z-score, raw"][3]},
           "Compare each rule with the number of lines whose unit price is really implausible.", decimals=0,
           thresholds=[(None, "blue")])
    t = pd.DataFrame({"time": df["date"] + pd.to_timedelta(np.arange(n) % 24, unit="h"),
                      "legit_lines": np.where(is_err == 0, amt, np.nan), "price_errors": np.where(is_err == 1, amt, np.nan),
                      "z limit (mean+3SD)": A["zhi"], "Tukey upper fence": A["fhi"], "modified-z limit": A["mzhi"]})
    d.timeseries("Order-line amount with the three upper limits (log axis, EUR)", t,
                 "Red dots are lines with an implausible unit price. The Tukey and modified-z limits almost coincide. The z-score limit sits above half of them (masking); "
                 "the other two limits catch them but also flag genuine large orders.",
                 points=["legit_lines", "price_errors"], dashed=["z limit (mean+3SD)", "Tukey upper fence", "modified-z limit"],
                 colors={"legit_lines": "#4E79A7", "price_errors": "#E15759", "z limit (mean+3SD)": "#F28E2B",
                         "Tukey upper fence": "#59A14F", "modified-z limit": "#B07AA1"}, unit="short")
    d.panels[-1]["fieldConfig"]["defaults"]["custom"]["scaleDistribution"] = {"type": "log", "log": 10}
    cm = pd.DataFrame([[k, v[2], v[1], v[3]] for k, v in conf.items()],
                      columns=["rule", "legit lines flagged (false alarms)", "price errors caught", "price errors missed"])
    d.bars("Rule performance against the price-error ground truth", cm,
           f"There are {n_err} price errors. Raw-scale rules over-flag legitimate lines; log-scale rules do better; none is perfect.")
    lx = np.log10(df["quantity"].to_numpy())
    ly = np.log10(ratio)
    mm = is_err == 1
    xy_two_frames(d, "Context: quantity vs unit price relative to category median (log10 axes)",
                  [("legit lines", pd.DataFrame({"log10_quantity": lx[~mm], "log10_price_ratio": ly[~mm]})),
                   ("price errors", pd.DataFrame({"log10_quantity": lx[mm], "log10_price_ratio": ly[mm]}))],
                  "log10_quantity", "log10_price_ratio",
                  "Genuine bulk orders sit far to the right on the 0 line (normal price, big quantity); price errors sit at +2 or -2 (price off by 100x).",
                  ["#4E79A7", "#E15759"])
    cnt, edges = np.histogram(np.log10(amt), bins=np.arange(0, 6, 0.5))
    d.bars("Histogram of log10(amount)", pd.DataFrame({"log10_amount_bin": [f"{a:.1f}-{a + 0.5:.1f}" for a in edges[:-1]], "lines": cnt}),
           "On the log scale the main body is roughly bell-shaped and the errors are separate bumps in the right tail.")
    d.save(out)

    md(out / "theory.md", fill(THEORY, theory_values(A, fz, fi, fm)))
    md(out / "task.md", TASK.replace("<<n_err>>", "").replace("<<zthr>>", str(ZTHR)))
    return b


def fill(text: str, vals: dict) -> str:
    for k, v in vals.items():
        text = text.replace(f"<<{k}>>", str(v))
    return text


def theory_values(A, fz, fi, fm) -> dict:
    ex = np.array([10, 11, 11, 12, 12, 13, 13, 14, 15, 90.0])
    m, s = ex.mean(), np.std(ex, ddof=1)
    med = np.median(ex)
    mad = np.median(np.abs(ex - med))
    q1, q3 = np.percentile(ex, [25, 75])
    big = np.array([10, 11, 11, 12, 12, 13, 13, 14, 15, 90, 95, 100, 105.0])
    mb, sb = big.mean(), np.std(big, ddof=1)
    return {
        "ex_mean": f"{m:.1f}", "ex_zmax": f"{9 / np.sqrt(10):.2f}", "mk_zmax": f"{12 / np.sqrt(13):.2f}", "ex_sd": f"{s:.2f}", "ex_z": f"{(90 - m) / s:.2f}", "ex_med": f"{med:.1f}", "ex_mad": f"{mad:.1f}",
        "ex_mz": f"{0.6745 * (90 - med) / mad:.1f}", "ex_q1": f"{q1:.2f}", "ex_q3": f"{q3:.2f}", "ex_iqr": f"{q3 - q1:.2f}",
        "ex_fence": f"{q3 + 1.5 * (q3 - q1):.2f}", 
        "mk_mean": f"{mb:.1f}", "mk_sd": f"{sb:.1f}", "mk_z": f"{(90 - mb) / sb:.2f}", "mk_zlimit": f"{mb + 3 * sb:.0f}",
        "mk_n": 4, "mk_med": f"{np.median(big):.1f}", "mk_mad": f"{np.median(np.abs(big - np.median(big))):.1f}",
        "mk_mz": f"{0.6745 * (90 - np.median(big)) / np.median(np.abs(big - np.median(big))):.1f}",
        "p_normal": f"{2 * 0.00135 * 100:.2f}", "exp_false": f"{300 * 0.0027:.1f}",
    }


THEORY = r"""
# Theory: outlier detection

## Why "find the outliers" is a decision, not a calculation

An outlier is an observation that looks inconsistent with the rest *under some model of the data*. Every detection rule encodes such a model
(a bell curve, a quartile range, a robust spread), and every rule can be wrong in two ways: **false alarms** (unusual but legitimate points)
and **misses** (errors that the rule's own yardstick hides). Outlier detection prevents two failures at once: silently averaging garbage into a
KPI, and silently deleting the most informative observations (the viral order, the real incident). The statistics only nominate candidates; the
decision to correct, keep or delete needs context.

## Three standard rules

Let $\bar x$ and $s$ be the mean and sample SD, $\tilde x$ the median, $\text{MAD}=\operatorname{median}|x_i-\tilde x|$, and $Q_1,Q_3$ the quartiles with
$\text{IQR}=Q_3-Q_1$ (linear-interpolation quartiles, as `QUARTILE` computes).

1. **z-score:** flag $|z_i|>c$ with $z_i=(x_i-\bar x)/s$ and $c=3$. For *normal* data a fraction $2\cdot0.00135 = <<p_normal>>\,\%$ of points exceed 3 by chance,
   so about <<exp_false>> false alarms are expected among 300 clean points.
2. **Tukey fences:** flag $x_i<Q_1-k\,\text{IQR}$ or $x_i>Q_3+k\,\text{IQR}$, with $k=1.5$ ("outside") or $k=3$ ("far out"). Quartiles are robust and no normality
   is assumed, but the fences are symmetric around the box, so they over-flag in skewed data.
3. **Modified z-score (Iglewicz-Hoaglin):** $M_i = 0.6745\,(x_i-\tilde x)/\text{MAD}$, flag $|M_i|>3.5$. It is the z-score with median and MAD replacing
   mean and SD (lesson [robust statistics](../02-robust-statistics/theory.md)); the constant 0.6745 makes MAD comparable to $\sigma$ for normal data.

## Worked example: one outlier

Ten values $10,11,11,12,12,13,13,14,15,90$. Mean $<<ex_mean>>$, SD $<<ex_sd>>$, so $z(90)=<<ex_z>>$ - **below 3, not flagged**, although 90 is plainly wrong.
This is not bad luck: in a sample of size $n$ no observation can have $|z|>(n-1)/\sqrt n$, which is <<ex_zmax>> for $n=10$, so a 3-SD rule cannot flag anything in a sample of ten.
The robust rules have no such limit: median <<ex_med>>, MAD <<ex_mad>>, $M(90)=<<ex_mz>>$; quartiles <<ex_q1>> and <<ex_q3>> give IQR <<ex_iqr>> and an upper fence of <<ex_fence>>, so 90 is far outside.

## Masking

Now append three more, similar errors: $\dots,15,90,95,100,105$. The mean jumps to <<mk_mean>> and the SD to <<mk_sd>>, so $z(90)=<<mk_z>>$ and the 3-SD limit is <<mk_zlimit>>:
**nothing is flagged**, although 4 of 13 values are wild (here the cap $(n-1)/\sqrt n$ is <<mk_zmax>>, but the real cause is the inflated SD). The outliers inflated the mean and SD they were being measured with: this is *masking*. The median (<<mk_med>>) and MAD (<<mk_mad>>)
barely move, so $M(90)=<<mk_mz>>$ still flags all four. Masking is why a z-score is acceptable as a quick check on a clean variable with at most one or two suspects,
but not as a general-purpose detector. The opposite problem, *swamping* (a good point flagged because bad points shifted the centre), arises with the same mechanism.

## Skewed data and transformation

For right-skewed amounts (prices, durations) any symmetric rule on the raw scale flags legitimate high values and never flags low ones. Apply the rule to
$\ln x$ (or another normalising transform), then interpret the flags on the original scale. The log turns "10 times the typical value" into a fixed distance
on the axis regardless of the level.

## From flags to decisions

A flagged point belongs to one of four cases, and the rule cannot tell which:

| cause | example | action |
|---|---|---|
| recording / unit error | price typed 100x too large | correct if the true value is recoverable, otherwise mark missing |
| different population | wholesale order inside a retail data set | keep, analyse separately (segment) |
| genuine extreme of the same process | rare large but legitimate order | keep; use robust summaries or a heavy-tail model |
| signal | the first sign of a fault or an incident | investigate; this is what you are monitoring for |

Good practice: ask *why*, using other columns (here: unit price against the category median); document every rule and threshold; report results with and without
the points; never delete silently. Deleting everything the rule flags changes the estimand: here it would understate total spend by the value of the legitimate large orders.

## Assumptions and pitfalls

1. **Thresholds are conventions.** 3 SD, 1.5 IQR and 3.5 are defaults, not laws; the expected number of false alarms grows with $n$ (0.27 % of 10 000 points is 27 points).
2. **Multiple testing.** Scanning many series or many windows with a 3 sigma rule will produce false alarms every day; see [false alarms and detection performance](../29-false-alarms-and-detection-performance/theory.md).
3. **Univariate rules miss contextual outliers.** An amount can be unremarkable overall yet impossible for its category or time of day; condition on context or build a
   residual first ([residual analysis](../15-residual-analysis-and-model-diagnostics/theory.md)).
4. **Time series.** In a series with trend or seasonality a point is unusual relative to its expected value, not to the global mean ([time-series anomaly detection](../28-time-series-anomaly-detection/theory.md)).
5. **Swamping the tails.** If the data are genuinely [heavy-tailed](../01-distribution-shapes-and-heavy-tails/theory.md), a large share of "outliers" are ordinary.
6. **A MAD of 0** (many repeated values) makes the modified z undefined; use the IQR or a floor.

## Related notes

- [Robust statistics](../02-robust-statistics/theory.md)
- [Percentiles and extreme values](../03-percentiles-and-extreme-values/theory.md)
- [Normal curve and z-score](../../notes/random_variables_and_distributions/normal_curve_and_z_score.md)
"""

TASK = r"""
# Task: outlier detection

## Scenario

The procurement team of a research institute exports its purchase-order lines for February and March. Finance wants to publish the average
amount per line and the total spend, but the monthly audit has found "some crazy numbers". You are asked to flag suspicious lines, decide which
are errors that must be corrected and which are legitimate, and say how much the published figures change depending on your decision.

## Data

`data.csv` - 300 purchase-order lines, one row per line.

| column | meaning |
|---|---|
| `line_id` | running number |
| `date` | date the order was placed |
| `category` | `stationery`, `lab_supplies` or `it_hardware` |
| `quantity` | units ordered |
| `unit_price_eur` | price per unit in EUR |
| `amount_eur` | line total in EUR (`quantity` x `unit_price_eur`) |

## Questions

Work in a spreadsheet (import `data.csv`), then compare with `solution.xlsx`. Use `STDEV` (sample), `QUARTILE` (inclusive) and thresholds z = <<zthr>>, Tukey k = 1.5 (inner) and 3 (outer), modified z = 3.5.

1. Compute mean, SD, median, MAD, Q1, Q3 and IQR of `amount_eur`.
2. Flag lines with $|z|>3$. How many are there, and what is the upper limit in EUR?
3. Compute the Tukey fences for k = 1.5 and k = 3. How many lines does each flag?
4. Compute the modified z for every line. How many have $|M|>3.5$ and what is the equivalent upper limit in EUR?
5. How many lines are flagged by the modified z but *not* by the z-score? Why can that happen? (Compare the SD with 1.4826 x MAD.)
6. Repeat the three rules on $\ln(\text{amount})$. How do the counts change and why?
7. Compute the median unit price per category and the ratio of each line's unit price to its category median. Call a line a *price error* if the ratio is above 5 or below 1/5. How many price errors are there? Of the lines flagged by the modified z on the raw amount, how many are price errors and how many are not?
8. Build a table with, for each of the six rules (three rules, raw and log scale): lines flagged, price errors caught, legitimate lines flagged, price errors missed.
9. Compute the total spend and the mean amount (a) over all lines, (b) without the price errors, (c) without every line flagged by the modified z. How much legitimate spend would (c) delete?
10. *Explain in three sentences* what you would do with each kind of flagged line, and one situation in which none of these rules would find a wrong value.

## Grafana

Import `grafana/dashboard.json` (no data-source setup is needed).

- In "Order-line amount with the three upper limits", which dashed limit lies above many of the red dots? Which limit is below many blue dots?
- In "Context: quantity vs unit price", where do the red dots sit compared with the large blue ones?
- In "Rule performance", which rule gives the best trade-off between caught errors and false alarms?

## Deliverable

A short note (6-10 lines) titled *Which lines do we correct, keep or investigate?* with three named parts: **Method** (rules and thresholds used),
**Findings** (counts, what the errors look like, what the large legitimate lines look like) and **Impact** (how total and mean spend change under each choice).
Include one chart and state one limitation.
"""
