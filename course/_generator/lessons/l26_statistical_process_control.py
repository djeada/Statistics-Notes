"""Lesson 26 - Statistical process control (Shewhart I-MR and X-bar/R charts, Western Electric rules, contaminated baseline)."""
import math
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import INPUT_FILL, Book, Dash, md, write_csv  # noqa: E402

SLUG = "26-statistical-process-control"
TITLE = "Statistical process control"
MODULE = "Statistical monitoring and decision-making"
DATASET = "400 incubator-chamber temperature readings, 5 minutes apart (target 37.0 C)"

N = 400
D2, A2, D4_X, D4_MR = 1.128, 0.577, 2.114, 3.267
BASE_B, BASE_A, MON, SEARCH, NSG = (1, 60), (1, 100), 100, 200, 12


def make_data() -> pd.DataFrame:
    rng = np.random.default_rng(2609)
    x = 37.0 + rng.normal(0, 0.30, N)
    t = np.arange(1, N + 1)
    x[60:72] += 0.9                      # obs 61-72: door left open / loading (assignable cause inside the first 100)
    x[149] += 1.4                        # obs 150: sensor glitch
    x[189] -= 1.3                        # obs 190: sensor glitch
    x += np.where(t > 230, (t - 230) * 0.0035, 0.0)   # slow drift after obs 230 (+0.6 C by the end = 2 sigma)
    return pd.DataFrame({"timestamp": pd.date_range("2026-02-10 08:00", periods=N, freq="5min"), "temp_c": np.round(x, 2)})


def add_col(b, name, fn, expected, fmt="0.000", first_row=2):
    """Like Book.add_column but writes the formula in EVERY row (so yellow inputs keep working) and checks only non-NaN rows."""
    L = b.add_column(name, fn, expected=None, fmt=fmt, first_row=first_row)
    for r in range(first_row, b.n + 2):
        v = expected[r - 2]
        if not np.isnan(v):
            b.checks.append((f"Data!{L}{r}", f"{name} row {r}", float(v)))
    return L


def we_rules(z):
    n = len(z)
    r = np.zeros((4, n))
    for i in range(n):
        r[0, i] = abs(z[i]) > 3
        if i >= 2:
            w = z[i - 2:i + 1]
            r[1, i] = (w > 2).sum() >= 2 or (w < -2).sum() >= 2
        if i >= 4:
            w = z[i - 4:i + 1]
            r[2, i] = (w > 1).sum() >= 4 or (w < -1).sum() >= 4
        if i >= 7:
            w = z[i - 7:i + 1]
            r[3, i] = (w > 0).all() or (w < 0).all()
    return r


def fill(text, **kw):
    for k, v in kw.items():
        text = text.replace(f"@@{k}@@", str(v))
    assert "@@" not in text
    return text


# worked example numbers -------------------------------------------------------------
_X = np.array([37.1, 36.8, 37.0, 37.3, 36.9, 37.2, 37.0, 36.7, 37.1, 37.4])
_Xc = _X.copy()
_Xc[5:8] += 1.0
_mr = lambda a: np.abs(np.diff(a)).mean()
EX = dict(
    MEAN=f"{_X.mean():.2f}", MRBAR=f"{_mr(_X):.3f}", SIG=f"{_mr(_X) / D2:.3f}", SD=f"{_X.std(ddof=1):.3f}",
    UCL=f"{_X.mean() + 3 * _mr(_X) / D2:.2f}", LCL=f"{_X.mean() - 3 * _mr(_X) / D2:.2f}",
    CMEAN=f"{_Xc.mean():.2f}", CSD=f"{_Xc.std(ddof=1):.3f}", CMRBAR=f"{_mr(_Xc):.3f}", CSIG=f"{_mr(_Xc) / D2:.3f}",
    RSD=f"{_Xc.std(ddof=1) / _X.std(ddof=1):.1f}", RMR=f"{_mr(_Xc) / _mr(_X):.2f}x".replace('x', ''), CUCL_SD=f"{_Xc.mean() + 3 * _Xc.std(ddof=1):.2f}", CUCL_MR=f"{_Xc.mean() + 3 * _mr(_Xc) / D2:.2f}")


def build(out: Path) -> Book:
    df = make_data()
    write_csv(out, df)
    x = df["temp_c"].to_numpy(float)
    t = np.arange(1, N + 1)
    mr = np.concatenate([[np.nan], np.abs(np.diff(x))])

    def base(a, e):
        seg = x[a - 1:e]
        m = seg.mean()
        sd = seg.std(ddof=1)
        mrb = np.abs(np.diff(seg)).mean()
        return dict(n=len(seg), mean=m, sd=sd, mrbar=mrb, sig=mrb / D2)
    BA, BB = base(*BASE_A), base(*BASE_B)
    sets = {"A-SD": (BA["mean"], BA["sd"]), "A-MR": (BA["mean"], BA["sig"]), "B-SD": (BB["mean"], BB["sd"]), "B-MR": (BB["mean"], BB["sig"])}
    CL, SG = BB["mean"], BB["sig"]
    z = (x - CL) / SG
    R = we_rules(z)
    anyr = (R.sum(axis=0) > 0).astype(float)
    sig_first = lambda flag: int(t[(flag == 1) & (t > SEARCH)][0]) if ((flag == 1) & (t > SEARCH)).any() else 0
    first_set = {}
    cnt_set = {}
    for k, (m_, s_) in sets.items():
        beyond = (x > m_ + 3 * s_) | (x < m_ - 3 * s_)
        first_set[k] = sig_first(beyond.astype(float))
        cnt_set[k] = int((beyond & (t > MON)).sum())
    first_rule = [sig_first(R[k]) for k in range(4)] + [sig_first(anyr)]
    # X-bar / R chart
    xs = x.reshape(-1, 5)
    xb, rg = xs.mean(axis=1), xs.max(axis=1) - xs.min(axis=1)
    xbb, rbar = xb[:NSG].mean(), rg[:NSG].mean()
    ucl_x, lcl_x, ucl_r = xbb + A2 * rbar, xbb - A2 * rbar, D4_X * rbar
    flag_x = ((xb > ucl_x) | (xb < lcl_x)).astype(float)
    sg_idx = np.arange(1, 81)
    sel_x = (flag_x == 1) & (sg_idx * 5 > SEARCH)
    first_x = int(sg_idx[sel_x][0]) if sel_x.any() else 0
    ucl_mr = D4_MR * BB["mrbar"]

    # ------------------------------------------------------------------ workbook
    b = Book(df, "Lesson 26 - Statistical process control",
             "Phase I: limits from a baseline. Phase II: monitor later readings against them. Yellow cells = assumptions you can change.")
    add_col(b, "t", lambda r: "=ROW()-1", t.astype(float), "0")
    tcol = b.col("t")
    X = b.rng("temp_c")
    T = b.rng("t")

    b.section("1. Inputs")
    sB, eB = b.row("Baseline B: first observation", BASE_B[0], None, "0", is_input=True), b.row("Baseline B: last observation", BASE_B[1], None, "0", is_input=True)
    sA, eA = b.row("Baseline A: first observation", BASE_A[0], None, "0", is_input=True), b.row("Baseline A: last observation", BASE_A[1], None, "0", is_input=True)
    mon = b.row("Monitoring starts after observation", MON, None, "0", "signals are counted after this point", is_input=True)
    srch = b.row("Search for a sustained change from observation", SEARCH, None, "0", "skips the early isolated glitches", is_input=True)
    nsg = b.row("Baseline subgroups for the X-bar chart (of 5 readings)", NSG, None, "0", "12 subgroups = readings 1-60", is_input=True)
    d2 = b.row("d2 for moving ranges of 2", D2, None, "0.000", "sigma = MR-bar / d2")

    add_col(b, "mr", lambda r: f"=ABS(Data!B{r}-Data!B{r - 1})", mr, "0.00", first_row=3)
    MRr = b.rng("mr")

    b.section("2. Baseline statistics")
    rows, exp = [], {}
    base_row = b.next_row + 1
    for i, (nm, (s_, e_), BS) in enumerate([("A: first 100 readings", (sA, eA), BA), ("B: first 60 readings", (sB, eB), BB)]):
        n_ = f'COUNTIFS({T},">="&{s_},{T},"<="&{e_})'
        mean_ = f'AVERAGEIFS({X},{T},">="&{s_},{T},"<="&{e_})'
        rows.append([nm, f"={n_}", f"={mean_}",
                     f'=SQRT((SUMPRODUCT(({T}>={s_})*({T}<={e_})*{X}^2)-B{base_row + i}*C{base_row + i}^2)/(B{base_row + i}-1))',
                     f'=AVERAGEIFS({MRr},{T},">"&{s_},{T},"<="&{e_})', f"=E{base_row + i}/{d2}"])
        exp.update({(i, 1): BS["n"], (i, 2): BS["mean"], (i, 3): BS["sd"], (i, 4): BS["mrbar"], (i, 5): BS["sig"]})
    p0, p1 = b.table(["Baseline", "n", "Mean (C)", "Sample SD (C)", "MR-bar (C)", "sigma = MR-bar / d2 (C)"], rows,
                     fmt={1: "0", 2: "0.000", 3: "0.000", 4: "0.000", 5: "0.000"}, expect=exp)

    b.section("3. Three-sigma limits, four ways (centre = baseline mean; sigma from the SD or from MR-bar)")
    rows, exp = [], {}
    base_row = b.next_row + 1
    spec = [("A-SD", p0, "D"), ("A-MR", p0, "F"), ("B-SD", p0 + 1, "D"), ("B-MR", p0 + 1, "F")]
    for i, (nm, pr, scol) in enumerate(spec):
        m_, s_ = sets[nm]
        rows.append([nm, f"=C{pr}", f"={scol}{pr}", f"=B{base_row + i}+3*C{base_row + i}", f"=B{base_row + i}-3*C{base_row + i}",
                     f"=3*C{base_row + i}",
                     f'=COUNTIFS({X},">"&D{base_row + i},{T},">"&{mon})+COUNTIFS({X},"<"&E{base_row + i},{T},">"&{mon})'])
        exp.update({(i, 1): m_, (i, 2): s_, (i, 3): m_ + 3 * s_, (i, 4): m_ - 3 * s_, (i, 5): 3 * s_, (i, 6): cnt_set[nm]})
    l0, l1 = b.table(["Limits", "Centre line", "sigma", "UCL", "LCL", "Half-width (3 sigma)", "Readings outside after the monitoring start"],
                     rows, fmt={1: "0.000", 2: "0.000", 3: "0.00", 4: "0.00", 5: "0.00", 6: "0"}, expect=exp)
    CLb, SGb = f"Analysis!$B${l0 + 3}", f"Analysis!$C${l0 + 3}"
    UCLb, LCLb = f"Analysis!$D${l0 + 3}", f"Analysis!$E${l0 + 3}"
    UCLa, LCLa = f"Analysis!$D${l0}", f"Analysis!$E${l0}"

    # helper columns that use the limits ---------------------------------------------
    add_col(b, "CL_B", lambda r: f"={CLb}", np.full(N, CL), "0.000")
    add_col(b, "UCL_B", lambda r: f"={UCLb}", np.full(N, CL + 3 * SG), "0.000")
    add_col(b, "LCL_B", lambda r: f"={LCLb}", np.full(N, CL - 3 * SG), "0.000")
    add_col(b, "UCL_A_sd", lambda r: f"={UCLa}", np.full(N, sets["A-SD"][0] + 3 * sets["A-SD"][1]), "0.000")
    add_col(b, "z_B", lambda r: f"=(Data!B{r}-{CLb})/{SGb}", z, "0.000")
    zc = b.col("z_B")
    zr = lambda lo, r: f"Data!{zc}{r - lo}:{zc}{r}"
    nan_fill = lambda arr, lo: np.where(np.arange(N) >= lo, arr, np.nan)
    add_col(b, "rule1", lambda r: f"=IF(ABS(Data!{zc}{r})>3,1,0)", R[0], "0")
    add_col(b, "rule2", lambda r: f'=IF(OR(COUNTIF({zr(2, r)},">2")>=2,COUNTIF({zr(2, r)},"<-2")>=2),1,0)', nan_fill(R[1], 2), "0", first_row=4)
    add_col(b, "rule3", lambda r: f'=IF(OR(COUNTIF({zr(4, r)},">1")>=4,COUNTIF({zr(4, r)},"<-1")>=4),1,0)', nan_fill(R[2], 4), "0", first_row=6)
    add_col(b, "rule4", lambda r: f'=IF(OR(COUNTIF({zr(7, r)},">0")=8,COUNTIF({zr(7, r)},"<0")=8),1,0)', nan_fill(R[3], 7), "0", first_row=9)
    rc = [b.col(f"rule{k}") for k in (1, 2, 3, 4)]
    add_col(b, "any_rule", lambda r: "=IF(" + "+".join(f"Data!{c}{r}" for c in rc) + ">0,1,0)", anyr, "0")
    ac = b.col("any_rule")
    # first-signal helper columns (blank when there is no signal)
    for nm, colL, flag in [("t_rule1", rc[0], R[0]), ("t_rule2", rc[1], R[1]), ("t_rule3", rc[2], R[2]), ("t_rule4", rc[3], R[3]), ("t_any", ac, anyr)]:
        add_col(b, nm, lambda r, colL=colL: f'=IF(AND(Data!{colL}{r}=1,Data!{tcol}{r}>{srch}),Data!{tcol}{r},"")',
                np.where((flag == 1) & (t > SEARCH), t, np.nan), "0", first_row=2)
    for nm, (m_, s_), UL, LL in [("t_A_sd", sets["A-SD"], l0, l0), ("t_A_mr", sets["A-MR"], l0 + 1, l0 + 1),
                                 ("t_B_sd", sets["B-SD"], l0 + 2, l0 + 2), ("t_B_mr", sets["B-MR"], l0 + 3, l0 + 3)]:
        beyond = ((x > m_ + 3 * s_) | (x < m_ - 3 * s_)) & (t > SEARCH)
        add_col(b, nm, lambda r, UL=UL: (f'=IF(AND(Data!{tcol}{r}>{srch},OR(Data!B{r}>Analysis!$D${UL},Data!B{r}<Analysis!$E${UL})),Data!{tcol}{r},"")'),
                np.where(beyond, t, np.nan), "0")
    colr = lambda nm: b.rng(nm)

    b.section("4. First signal after the search start (0 = never)")
    rows, exp = [], {}
    items = [("Chart A, limits from sample SD", "t_A_sd", first_set["A-SD"]), ("Chart A, limits from MR-bar", "t_A_mr", first_set["A-MR"]),
             ("Chart B, limits from sample SD", "t_B_sd", first_set["B-SD"]), ("Chart B, limits from MR-bar (rule 1)", "t_B_mr", first_set["B-MR"])]
    for i, (lab, nm, v) in enumerate(items):
        rows.append([lab, f"=IF(COUNT({colr(nm)})=0,0,MIN({colr(nm)}))"])
        exp[(i, 1)] = v
    s0, s1 = b.table(["3-sigma limits (rule 1 only)", "First signal at observation"], rows, fmt={1: "0"}, expect=exp)

    b.section("5. Western Electric rules on chart B (centre and sigma from baseline B, MR-based)")
    rows, exp = [], {}
    names = ["Rule 1: one point beyond 3 sigma", "Rule 2: 2 of 3 beyond 2 sigma (same side)", "Rule 3: 4 of 5 beyond 1 sigma (same side)",
             "Rule 4: 8 in a row on one side of the centre", "Any rule"]
    cols = [(rc[0], R[0], "t_rule1"), (rc[1], R[1], "t_rule2"), (rc[2], R[2], "t_rule3"), (rc[3], R[3], "t_rule4"), (ac, anyr, "t_any")]
    for i, (nm, (cL, flag, tn)) in enumerate(zip(names, cols)):
        rr_ = f"Data!${cL}$2:${cL}${N + 1}"
        rows.append([nm, f'=COUNTIFS({rr_},1,{T},"<="&{eB})', f'=COUNTIFS({rr_},1,{T},">"&{eB},{T},"<="&{eA})',
                     f'=COUNTIFS({rr_},1,{T},">"&{mon})', f"=IF(COUNT({colr(tn)})=0,0,MIN({colr(tn)}))"])
        exp.update({(i, 1): int(((flag == 1) & (t <= BASE_B[1])).sum()), (i, 2): int(((flag == 1) & (t > BASE_B[1]) & (t <= BASE_A[1])).sum()),
                    (i, 3): int(((flag == 1) & (t > MON)).sum()), (i, 4): first_rule[i]})
    w0, w1 = b.table(["Rule", "Flags inside baseline B", "Flags in the rest of baseline A (obs 61-100)", "Flags after the monitoring start",
                      "First flag after the search start"], rows, fmt={j: "0" for j in range(1, 5)}, expect=exp)

    b.section("6. Moving-range chart and false-alarm arithmetic")
    umr = b.row("MR chart UCL = 3.267 * MR-bar (baseline B)", f"=3.267*Analysis!$E${p0 + 1}", ucl_mr, "0.000")
    b.row("Moving ranges above the MR-chart UCL after the monitoring start", f'=COUNTIFS({MRr},">"&{umr},{T},">"&{mon})',
          int(((mr > ucl_mr) & (t > MON)).sum()), "0", "a single glitch creates two big moving ranges (in and out)")
    p3 = 2 * (1 - 0.5 * (1 + math.erf(3 / math.sqrt(2))))
    pr = b.row("P(|z| > 3) for normal data", "=2*(1-NORMSDIST(3))", p3, "0.00000")
    b.row("Average run length (points) between false alarms of rule 1", f"=1/{b.local(pr)}", 1 / p3, "0.0")
    b.row("Expected false alarms of rule 1 in 400 in-control points", f"=400*{b.local(pr)}", 400 * p3, "0.00")

    # X-bar / R chart ----------------------------------------------------------------
    sg_rows = np.arange(6, N + 2, 5)            # Excel rows of the last reading of each subgroup
    sg_arr = np.full(N, np.nan)
    sg_arr[sg_rows - 2] = sg_idx
    xb_arr = np.full(N, np.nan)
    xb_arr[sg_rows - 2] = xb
    r_arr = np.full(N, np.nan)
    r_arr[sg_rows - 2] = rg

    # add_col writes every row; subgroup columns must exist only on every 5th row, so write them by hand
    def sg_col(name, fn, arr, fmt):
        L = b.add_column(name, lambda r: "", expected=None, fmt=fmt, first_row=2)
        for r in range(2, N + 2):
            cell = b.data.cell(row=r, column=b.data.max_column)
            cell.value = fn(r) if (r - 1) % 5 == 0 else None
            if cell.value is not None and not np.isnan(arr[r - 2]):
                b.checks.append((f"Data!{L}{r}", f"{name} row {r}", float(arr[r - 2])))
        return L
    sg_col("subgroup", lambda r: f"=INT((Data!{tcol}{r}-1)/5)+1", sg_arr, "0")
    sgc = b.col("subgroup")
    sg_col("xbar", lambda r: f"=AVERAGE(Data!B{r - 4}:B{r})", xb_arr, "0.000")
    sg_col("range", lambda r: f"=MAX(Data!B{r - 4}:B{r})-MIN(Data!B{r - 4}:B{r})", r_arr, "0.00")
    xbc, rgc = b.col("xbar"), b.col("range")
    SGr = f"Data!${sgc}$2:${sgc}${N + 1}"

    b.section("7. X-bar / R chart (subgroups of 5 consecutive readings; limits from the first 12 subgroups)")
    xbb_c = b.row("X-double-bar (baseline subgroups)", f'=AVERAGEIFS(Data!${xbc}$2:${xbc}${N + 1},{SGr},"<="&{nsg})', xbb, "0.000")
    rb_c = b.row("R-bar (baseline subgroups)", f'=AVERAGEIFS(Data!${rgc}$2:${rgc}${N + 1},{SGr},"<="&{nsg})', rbar, "0.000")
    ux = b.row("X-bar chart UCL = X-double-bar + A2 * R-bar   (A2 = 0.577 for n = 5)", f"={b.local(xbb_c)}+0.577*{b.local(rb_c)}", ucl_x, "0.000")
    lx = b.row("X-bar chart LCL", f"={b.local(xbb_c)}-0.577*{b.local(rb_c)}", lcl_x, "0.000")
    b.row("R chart UCL = D4 * R-bar   (D4 = 2.114)", f"=2.114*{b.local(rb_c)}", ucl_r, "0.000")
    flag_arr = np.full(N, np.nan)
    flag_arr[sg_rows - 2] = flag_x
    first_arr = np.full(N, np.nan)
    first_arr[sg_rows - 2] = np.where((flag_x == 1) & (sg_idx * 5 > SEARCH), sg_idx, np.nan)
    sg_col("xbar_flag", lambda r: f"=IF(OR(Data!{xbc}{r}>{ux},Data!{xbc}{r}<{lx}),1,0)", flag_arr, "0")
    fl = b.col("xbar_flag")
    sg_col("sg_first", lambda r: f'=IF(AND(Data!{fl}{r}=1,5*Data!{sgc}{r}>{srch}),Data!{sgc}{r},"")', first_arr, "0")
    sfc = b.col("sg_first")
    nfx = b.row("X-bar points outside the limits after the baseline subgroups", f'=COUNTIFS(Data!${fl}$2:${fl}${N + 1},1,{SGr},">"&{nsg})',
                int(((flag_x == 1) & (sg_idx > NSG)).sum()), "0")
    fsg = b.row("First X-bar signal after the search start: subgroup number (0 = never)", f"=IF(COUNT(Data!${sfc}$2:${sfc}${N + 1})=0,0,MIN(Data!${sfc}$2:${sfc}${N + 1}))",
                first_x, "0")
    fx_obs = b.row("... = reading number (last reading of that subgroup)", f"=5*{b.local(fsg)}", 5 * first_x, "0")

    b.line_chart("Individuals chart: readings, baseline-B limits and the (wider) baseline-A SD limit", "timestamp",
                 ["temp_c", "CL_B", "UCL_B", "LCL_B", "UCL_A_sd"], anchor="J4", y_title="C")

    ex_pts = int(((anyr == 1) & (t > BASE_B[1]) & (t <= BASE_A[1])).sum())
    exc_t = t[(anyr == 1) & (t > BASE_B[1]) & (t <= BASE_A[1])]
    exc_lo, exc_hi = int(exc_t.min()), int(exc_t.max())
    assert abs(5 * first_x - first_rule[0]) <= 10 and min(first_rule[2], first_rule[3]) < 5 * first_x - 15 and first_set["A-SD"] == 0
    b.answers([
        ("Mean, sample SD, MR-bar and sigma = MR-bar/1.128 for baseline A (first 100) and baseline B (first 60)", f"=Analysis!D{p0}",
         f"A: mean {BA['mean']:.3f}, SD {BA['sd']:.3f}, sigma(MR) {BA['sig']:.3f}. B: mean {BB['mean']:.3f}, SD {BB['sd']:.3f}, sigma(MR) {BB['sig']:.3f}. "
         f"The 100-reading baseline has a {BA['mean'] - BB['mean']:+.2f} C higher mean and its SD is {BA['sd'] / BB['sd']:.2f}x the clean one, "
         "because it contains an unusual stretch."),
        ("Three-sigma limits for the four combinations (A/B x SD/MR)", f"=Analysis!D{l0 + 3}",
         "UCL/LCL: " + "; ".join(f"{k}: {m_ + 3 * s_:.2f}/{m_ - 3 * s_:.2f}" for k, (m_, s_) in sets.items()) +
         ". The SD-based limits of the contaminated baseline are the widest; MR-bar is less affected because it only sees the two jumps into and out of the excursion."),
        ("Readings outside the limits after observation 100, for each of the four limit sets", f"=Analysis!G{l0}",
         ", ".join(f"{k}: {cnt_set[k]}" for k in sets) + ". Chart A with the sample SD flags almost nothing, including the two glitches: "
         "a contaminated baseline makes the chart blind."),
        ("First signal after observation 200 for each limit set", f"=Analysis!B{s0}",
         ", ".join(f"{k}: " + (f"obs {first_set[k]}" if first_set[k] else "never") for k in sets) +
         f". The first 3-sigma signal of the clean chart (obs {first_set['B-MR']}) is a noise point that happens to land high; the drifting mean itself never leaves the 3-sigma band."),
        ("Western Electric rules 1-4 on chart B: flags per rule and the first flag after observation 200", f"=Analysis!E{w0 + 3}",
         "First flags: " + ", ".join(f"rule {k + 1}: obs {first_rule[k]}" for k in range(4)) +
         f"; any rule: obs {first_rule[4]}. The run rules (3 and 4) react to a small sustained shift {first_rule[0] - min(first_rule[2], first_rule[3])} readings "
         "before the 3-sigma rule does."),
        ("How many flags does chart B raise inside obs 61-100 (the part of baseline A that is not in B)? What do they have in common?", f"=Analysis!C{w0 + 4}",
         f"{ex_pts} flags in obs 61-100, all of them between obs {exc_lo} and {exc_hi}: a temporary excursion of about +0.9 C (door open / loading) sitting inside the 'baseline'. "
         "Phase I needs exactly this step: find assignable causes, remove them, recompute."),
        ("X-bar / R chart with subgroups of 5: limits, first signal after reading 200", f"={fsg}",
         f"X-bar limits {lcl_x:.2f} to {ucl_x:.2f} (X-double-bar {xbb:.2f}, R-bar {rbar:.2f}); first signal after reading 200 at subgroup {first_x} "
         f"(reading {5 * first_x}), {int(((flag_x == 1) & (sg_idx > NSG)).sum())} signals after the baseline subgroups, the first of them in the excursion. Averaging 5 readings narrows "
         f"the limits by sqrt(5), yet this slow drift (0.6 C by the end) is only picked up at about the same time as the first 3-sigma signal of the individuals chart "
         f"(obs {first_set['B-MR']}); the run rules (first flag at obs {min(first_rule[2], first_rule[3])}) were earlier than both."),
        ("False-alarm arithmetic: P(|z|>3), average run length, expected false alarms per 400 readings", f"={pr}",
         f"P = {p3:.5f}, ARL = {1 / p3:.0f} readings, so about {400 * p3:.1f} rule-1 false alarm per 400 normal in-control readings. Adding rules 2-4 "
         "multiplies the false-alarm rate (simulated: about 1.8% of in-control points get some flag)."),
        ("Is the process 'out of control' because of a shift or a drift? What would you do on the first signal?", "see text",
         "A drift (mean moving gradually after ~obs 230) rather than a step: run rules and the X-bar chart see it long before a single reading crosses 3 sigma. "
         "On a signal: look for an assignable cause (door, heater, sensor), do not simply widen the limits. Limits assume independent, roughly normal readings; "
         "autocorrelated sensor data make charts raise far more false alarms."),
    ])

    # ------------------------------------------------------------------- grafana
    d = Dash("stats-26-spc", "26 · Statistical process control",
             "Shewhart individuals and X-bar charts for the chamber temperature: limits from a baseline, run rules, and what a contaminated baseline does.",
             df.rename(columns={"timestamp": "time"}), "time")
    d.stat("Phase I limits from the clean baseline B (C)", {"centre line": CL, "sigma (MR-bar/1.128)": SG, "UCL (3 sigma)": CL + 3 * SG,
                                                          "LCL (3 sigma)": CL - 3 * SG},
           "First 60 readings. sigma estimated from the average moving range.", unit="celsius", decimals=2)
    ic = pd.DataFrame({"time": df["timestamp"], "temp_c": x, "CL": CL, "UCL (baseline B)": CL + 3 * SG, "LCL (baseline B)": CL - 3 * SG,
                       "UCL (baseline A, sample SD)": sets["A-SD"][0] + 3 * sets["A-SD"][1],
                       "rule signal": np.where(anyr == 1, x, np.nan)})
    d.timeseries("Individuals chart", ic,
                 "Red dots: any Western Electric rule 1-4 (baseline B). The orange line is what the contaminated baseline's SD would have allowed.",
                 points=["rule signal"], dashed=["UCL (baseline B)", "LCL (baseline B)", "UCL (baseline A, sample SD)"],
                 colors={"temp_c": "#4E79A7", "CL": "#59A14F", "UCL (baseline B)": "#E15759", "LCL (baseline B)": "#E15759",
                         "UCL (baseline A, sample SD)": "#F28E2B", "rule signal": "#E15759"}, w=24, h=10)
    d.timeseries("Moving-range chart", pd.DataFrame({"time": df["timestamp"], "moving range": mr, "UCL (3.267 MR-bar)": ucl_mr, "MR-bar": BB["mrbar"]}),
                 "Each glitch appears as two large moving ranges. The drift is invisible here (MR measures short-term noise only).",
                 dashed=["UCL (3.267 MR-bar)"], colors={"moving range": "#4E79A7", "UCL (3.267 MR-bar)": "#E15759", "MR-bar": "#59A14F"}, w=12, h=8)
    xt = df["timestamp"].iloc[::5].reset_index(drop=True)
    d.timeseries("X-bar chart (subgroups of 5)", pd.DataFrame({"time": xt, "subgroup mean": xb, "X-double-bar": xbb, "UCL": ucl_x, "LCL": lcl_x,
                                                                "signal": np.where(flag_x == 1, xb, np.nan)}),
                 "The 5-reading average is less noisy, but the drift is slow: the means only cross the upper limit near the end. The first red dots are the excursion in the baseline.",
                 points=["signal"], dashed=["UCL", "LCL"],
                 colors={"subgroup mean": "#4E79A7", "X-double-bar": "#59A14F", "UCL": "#E15759", "LCL": "#E15759", "signal": "#E15759"}, w=12, h=8)
    d.bars("3-sigma half-width by baseline and sigma estimate (C)", pd.DataFrame(
        {"limits": ["A, sample SD", "A, MR-bar", "B, sample SD", "B, MR-bar"], "half-width": [3 * sets[k][1] for k in sets]}),
        "A contaminated baseline inflates the sample SD most.", unit="celsius", w=12, h=8)
    fr = [first_rule[0], first_rule[1], first_rule[2], first_rule[3]]
    d.bars("First signal after reading 200 (reading number; no bar = never)", pd.DataFrame(
        {"detector": ["Rule 1", "Rule 2", "Rule 3", "Rule 4", "A, 3 sigma SD", "X-bar"],
         "reading": [float(v) if v else np.nan for v in fr + [first_set["A-SD"], 5 * first_x]]}),
        "Rule 1 = 3 sigma, rule 2 = 2 of 3 beyond 2 sigma, rule 3 = 4 of 5 beyond 1 sigma, rule 4 = 8 in a row; X-bar = subgroup chart; A = contaminated baseline. Rules 3 and 4 detect the small drift first; X-bar and rule 1 need a larger shift; the contaminated chart never signals.", w=12, h=8)
    d.save(out)

    md(out / "theory.md", fill(THEORY, **EX))
    md(out / "task.md", TASK)
    return b


THEORY = r"""
# Theory: statistical process control

## Why control charts

A process (a furnace, an incubator, an API) wanders around its target because of many small causes: this is **common-cause
variation**. Occasionally something specific happens (a door is left open, a sensor fails, a heater degrades): an **assignable
(special) cause**. Reacting to common-cause noise (tampering) makes the process worse; ignoring a special cause lets it run.
A **Shewhart control chart** draws the centre line and limits that ordinary noise should (almost) never cross, and so turns
"is this reading odd?" into a rule you can apply consistently. It is a hypothesis test run repeatedly: each new point tests
"the process still behaves like the baseline".

## Phase I and Phase II

- **Phase I** (baseline): take a period when the process is believed to be stable, examine it, remove points with a known
  assignable cause, and estimate the centre $\bar x$ and the spread $\hat\sigma$.
- **Phase II** (monitoring): hold those limits fixed and test every new point. Limits are **not** recomputed from the data being
  monitored, otherwise a slow drift drags the limits with it.

## Individuals (I-MR) chart

For one reading per time step, limits are $\bar x \pm 3\hat\sigma$ with $\hat\sigma$ estimated from the **average moving range**

$$
\overline{MR} = \frac{1}{m-1}\sum_{i=2}^{m}|x_i-x_{i-1}|,\qquad \hat\sigma=\frac{\overline{MR}}{d_2},\quad d_2=1.128 .
$$

Why not simply use the sample SD of the baseline? The moving range measures only *short-term* point-to-point variation, so a
shift or excursion in the baseline touches just one or two ranges, while it inflates the sample SD of the whole baseline. A
contaminated baseline then produces limits that are too wide, and the chart cannot see the problem it was built to find.
The MR chart (UCL $=3.267\,\overline{MR}$) watches the spread itself.

**Worked example.** Ten readings $(37.1, 36.8, 37.0, 37.3, 36.9, 37.2, 37.0, 36.7, 37.1, 37.4)$: mean @@MEAN@@, $\overline{MR}=@@MRBAR@@$,
$\hat\sigma=@@SIG@@$ (sample SD $@@SD@@$), limits $@@LCL@@ \ldots @@UCL@@$. Now let three readings (6-8) be $+1.0$ too high, as in an excursion:
mean @@CMEAN@@, sample SD $@@CSD@@$ but $\overline{MR}=@@CMRBAR@@$, $\hat\sigma=@@CSIG@@$. The SD grows by a factor @@RSD@@ but the MR-based sigma only by a factor @@RMR@@. The upper limit moves from @@UCL@@ to @@CUCL_SD@@ (SD) or
@@CUCL_MR@@ (MR-bar). With only ten points both estimates are hit hard; with a 60-100 reading baseline and a short
excursion the moving-range estimate is much less affected. Better still, remove the excursion rather than average it in.

## X-bar and R chart

With rational subgroups of size $n$ (here $n=5$ consecutive readings) plot the subgroup mean $\bar x_j$ and range $R_j$. Limits
$\bar{\bar x} \pm A_2\bar R$ and $D_4\bar R$ (for $n=5$: $A_2=0.577$, $D_4=2.114$). Averaging cuts noise by $\sqrt n$, so the chart
detects smaller sustained shifts, at the price of reacting only once a whole subgroup is complete. Choose subgroups so that
variation *within* a subgroup is common-cause only.

## Detection rules (Western Electric)

With $z=(x-\bar x)/\hat\sigma$ the zone rules flag: **1** a point beyond $\pm3$; **2** two of three consecutive points beyond $\pm2$ on the same
side; **3** four of five beyond $\pm1$ on the same side; **4** eight in a row on one side of the centre. Rule 1 finds large, sudden
changes; rules 2-4 find smaller sustained ones, which is how a drift is caught early. The price is false alarms. For independent
normal data a rule-1 flag has probability $2(1-\Phi(3))=0.0027$ per point (an average of about 370 points between false alarms).
A simulation of 2 million in-control points gave per-point flag rates of about 0.27% (rule 1), 0.30% (rule 2), 0.53% (rule 3),
0.77% (rule 4) and 1.8% for "any rule", roughly one false alarm per 55 points. More sensitivity always costs specificity
(lesson 29).

## Assumptions

1. Observations are independent. Sensor data are often autocorrelated; positive autocorrelation shrinks the moving ranges (limits too
   narrow, too many alarms) and creates long runs on one side of the centre.
2. Roughly normal, or at least symmetric, short-term variation; for skewed data transform or use percentile-based limits.
3. A baseline that really represents the stable process, with enough points (rule of thumb: 20-25 subgroups or 50-100 individual readings).
4. Fixed limits in Phase II; recalibrate only after a documented change.

## Pitfalls

1. **Contaminated baseline** (above): wide limits, missed signals.
2. **Using the sample SD of the monitoring data** for limits: the shift inflates the SD and hides itself.
3. **Chart limits vs specification limits**: control limits say what the process *does*, specs say what the customer *wants*; they are unrelated.
4. **Acting on every flag**: a 1-in-55 false alarm rate with rules 1-4 means alarms are expected in long series.
5. **Ignoring run structure**: a drift never crosses 3 sigma for a long time, but eight points above the centre line is already unusual.
6. **Rational subgroups**: grouping readings across a shift change or two machines turns special-cause variation into "within-subgroup noise".

## Related notes

- [Percentiles and extreme values](../03-percentiles-and-extreme-values/theory.md) and [outlier detection](../04-outlier-detection/theory.md)
- [Robust statistics](../02-robust-statistics/theory.md): MR-bar is a robust spread estimate in the same spirit
- [Rolling statistics](../10-rolling-statistics/theory.md)
- [Change-point detection](../27-change-point-detection/theory.md), [anomaly detection](../28-time-series-anomaly-detection/theory.md), [false alarms](../29-false-alarms-and-detection-performance/theory.md)
- Repo notes: [stationarity](../../notes/time_series/stationarity.md), [randomness tests](../../notes/time_series/randomness_tests.md)
"""

TASK = r"""
# Task: statistical process control

## Scenario

A cell-culture lab runs an incubator whose chamber temperature must stay near **37.0 C**. A sensor logs one reading every
5 minutes. The first 100 readings were taken right after a service visit and are believed to represent normal operation. The
lab manager wants a **control chart** that raises an alarm when the chamber stops behaving normally, and asks whether
control limits drawn from the first 100 readings are good enough. Your job: build the limits, decide which signals are real, and find out when
the process really changed.

## Data

`data.csv` - 400 readings, 2026-02-10 08:00 to 2026-02-11 17:15, one row per 5-minute reading.

| column | meaning |
|---|---|
| `timestamp` | time of the reading |
| `temp_c` | chamber temperature in degrees Celsius |

Number the readings 1..400. Two candidate baselines: **A = readings 1-100** (the lab's choice) and **B = readings 1-60**. Put the
baseline limits, the monitoring start (100) and the search start (200) in input cells.

## Questions

Work in a spreadsheet (import `data.csv`), then compare with `solution.xlsx`.

1. For baselines A and B compute the mean, the sample SD, the average moving range MR-bar (mean of |x[t] - x[t-1]| inside the baseline) and sigma = MR-bar / 1.128.
2. Build 3-sigma limits (mean +/- 3 sigma) for the four combinations: A or B, sigma from the sample SD or from MR-bar.
3. For each of the four limit sets, count the readings after reading 100 that lie outside the limits.
4. For each limit set, find the first reading after reading 200 that is outside the limits (0 if none).
5. Using baseline B (MR-based sigma), compute z = (x - mean) / sigma and Western Electric rules 1-4. Count flags per rule and find the first flag after reading 200 for each rule.
6. How many flags does chart B raise among readings 61-100? What do they have in common? What does it say about baseline A?
7. Group readings in subgroups of 5. Build an X-bar / R chart with limits from the first 12 subgroups (A2 = 0.577, D4 = 2.114). How many subgroup means leave the limits after the baseline, and at which subgroup does X-bar first signal after reading 200?
8. For normal in-control data, what is P(|z| > 3), the average run length between rule-1 false alarms, and how many false alarms do you expect among 400 readings?
9. *Explain in 3-4 sentences* whether the problem you found is a sudden shift or something else, what you would do on the first alarm, and which assumption of the chart you worry about most.

## Grafana

Import `grafana/dashboard.json` (see `../grafana/README.md`; no data-source setup is needed).

- In "Individuals chart", which red dots are isolated and which form a pattern? Compare the orange line with the red limit.
- In "X-bar chart", which red dots belong to the baseline excursion and when does the drift first push the means out? Compare with the individuals chart.
- In "First signal after reading 200", rank the detectors. Which one never or almost never fires?

## Deliverable

A short note (6-8 lines) for the lab manager: *is the incubator in control, when did it stop being so, and which chart would you
install?* Include the individuals chart with limits and one table comparing the detectors. State one risk of acting on every alarm.
"""
