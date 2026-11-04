"""Lesson 25 - Prediction intervals and forecast uncertainty (seasonal-naive errors at 1-4 week horizons, coverage check)."""
import math
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import norm

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import INPUT_FILL, Book, Dash, md, write_csv  # noqa: E402
from _orders_story import orders_series  # noqa: E402

SLUG = "25-prediction-intervals-and-forecast-uncertainty"
TITLE = "Prediction intervals and forecast uncertainty"
MODULE = "Forecasting and model evaluation"
DATASET = "350 days of shop orders (2025-01-06 .. 2025-12-20); calibration on the first 224 days, coverage check on the last 126"

N, TC = 350, 224
KS = [1, 2, 3, 4]               # forecast horizon in weeks (lag of the seasonal naive forecast)
C1, C2 = 0.80, 0.95
NH = 112                        # days of history shown in the fan chart
NB = 11                         # 28-day volatility blocks starting at t = 29


def make_data() -> pd.DataFrame:
    # random-walk level (uncertainty grows with horizon) + weekday pattern + AR(1) noise; volatility x1.6 from day 241 (autumn season)
    return orders_series("2025-01-06", N, 2506, base=150, lin=0.12, ar=0.25, sd=6, rw_sd=3.5, weekday_scale=1.0,
                         sd_mult_from=240, sd_mult=1.6, spikes=[(60, 40), (130, -35), (255, 55), (290, 50)])


def add_col(b, name, fn, expected, fmt="0.000", first_row=2):
    """Like Book.add_column but writes the formula in EVERY row (so changing a yellow input still works) and checks only non-NaN rows."""
    L = b.add_column(name, fn, expected=None, fmt=fmt, first_row=first_row)
    for r in range(first_row, b.n + 2):
        v = expected[r - 2]
        if not np.isnan(v):
            b.checks.append((f"Data!{L}{r}", f"{name} row {r}", float(v)))
    return L


def fill(text, **kw):
    for k, v in kw.items():
        text = text.replace(f"@@{k}@@", str(v))
    assert "@@" not in text
    return text


# worked example numbers --------------------------------------------------------------
_E = np.array([-9, -4, -2, 0, 1, 3, 4, 6, 9, 14.0])
_F = 200.0
_z90 = norm.ppf(0.95)
EX = dict(
    N=len(_E), MEAN=f"{_E.mean():.1f}", SD=f"{_E.std(ddof=1):.2f}", Z=f"{_z90:.3f}", HW=f"{_z90 * _E.std(ddof=1):.1f}",
    NLO=f"{_F - _z90 * _E.std(ddof=1):.1f}", NHI=f"{_F + _z90 * _E.std(ddof=1):.1f}",
    QLO=f"{np.percentile(_E, 5):.2f}", QHI=f"{np.percentile(_E, 95):.2f}",
    ELO=f"{_F + np.percentile(_E, 5):.1f}", EHI=f"{_F + np.percentile(_E, 95):.1f}")


def build(out: Path) -> Book:
    df = make_data()
    write_csv(out, df)
    y = df["orders"].to_numpy(float)
    t = np.arange(1, N + 1)
    e = {k: np.where(t > 7 * k, y - np.concatenate([np.full(7 * k, np.nan), y[:N - 7 * k]]), np.nan) for k in KS}
    ecal = {k: np.where(t <= TC, e[k], np.nan) for k in KS}
    aev = {k: np.where(t > TC, np.abs(e[k]), np.nan) for k in KS}
    sd = {k: float(np.nanstd(ecal[k], ddof=1)) for k in KS}
    ncal = {k: int(np.sum(~np.isnan(ecal[k]))) for k in KS}
    z = {c: float(norm.ppf((1 + c) / 2)) for c in (C1, C2)}
    qlo = {(k, c): float(np.nanpercentile(ecal[k], 100 * (1 - c) / 2)) for k in KS for c in (C1, C2)}
    qhi = {(k, c): float(np.nanpercentile(ecal[k], 100 * (1 + c) / 2)) for k in KS for c in (C1, C2)}
    hit = {}
    for k in KS:
        for c in (C1, C2):
            ok = ~np.isnan(e[k])
            hit[("n", c, k)] = np.where(ok, (np.abs(e[k]) <= z[c] * sd[k]).astype(float), np.nan)
            hit[("e", c, k)] = np.where(ok, ((e[k] >= qlo[(k, c)]) & (e[k] <= qhi[(k, c)])).astype(float), np.nan)
    cal_m, ev_m = t <= TC, t > TC
    cov = lambda key, m: float(np.nanmean(hit[key][m]))
    n_ev = int(np.sum(~np.isnan(aev[1])))

    # ------------------------------------------------------------------ workbook
    b = Book(df, "Lesson 25 - Prediction intervals and forecast uncertainty",
             "Seasonal-naive errors e_k(t) = y[t] - y[t-7k] stand in for forecast errors at horizons of k weeks. Calibrate on t <= Tcal, test coverage after.")
    b.add_column("t", lambda r: "=ROW()-1", t, "0")
    tc = b.col("t")

    b.section("1. Inputs (yellow = edit me)")
    tcal = b.row("Calibration ends at day t =", TC, None, "0", "error quantiles/SD use t <= Tcal; coverage is tested on t > Tcal", is_input=True)
    cc1 = b.row("Confidence level 1", C1, None, "0.00", is_input=True)
    cc2 = b.row("Confidence level 2", C2, None, "0.00", is_input=True)
    z1 = b.row("z for level 1 = NORMSINV((1+c)/2)", f"=NORMSINV((1+{cc1})/2)", z[C1], "0.0000")
    z2 = b.row("z for level 2", f"=NORMSINV((1+{cc2})/2)", z[C2], "0.0000")
    TL = tcal

    # error columns
    for k in KS:
        b.add_column(f"e{k}", lambda r, k=k: f"=Data!B{r}-Data!B{r - 7 * k}", e[k], "0.0", first_row=7 * k + 2)
    for k in KS:
        add_col(b, f"ecal{k}", lambda r, k=k: f'=IF(Data!{tc}{r}<={TL},Data!{b.col(f"e{k}")}{r},"")', ecal[k], "0.0", first_row=7 * k + 2)
    for k in KS:
        add_col(b, f"aeval{k}", lambda r, k=k: f'=IF(Data!{tc}{r}>{TL},ABS(Data!{b.col(f"e{k}")}{r}),"")', aev[k], "0.0", first_row=7 * k + 2)
    rg = lambda nm, lo=2: f"Data!${b.col(nm)}${lo}:${b.col(nm)}${N + 1}"
    rk = lambda nm, k: rg(nm, 7 * k + 2)

    b.section("2. Forecast error by horizon (calibration period)")
    rows, exp = [], {}
    base_row = b.next_row + 1
    for i, k in enumerate(KS):
        rows.append([k, f"=COUNT({rk(f'ecal{k}', k)})", f"=AVERAGE({rk(f'ecal{k}', k)})", f"=STDEV({rk(f'ecal{k}', k)})",
                     f"=$D${base_row}*SQRT(A{base_row + i})", f"=D{base_row + i}/$D${base_row}"])
        exp.update({(i, 1): ncal[k], (i, 2): np.nanmean(ecal[k]), (i, 3): sd[k], (i, 4): sd[1] * math.sqrt(k), (i, 5): sd[k] / sd[1]})
    a0, a1 = b.table(["Horizon k (weeks)", "n (calibration)", "Mean error (bias)", "SD of error", "SD(1)*sqrt(k) random-walk rule", "SD(k) / SD(1)"],
                     rows, fmt={1: "0", 2: "0.00", 3: "0.00", 4: "0.00", 5: "0.00"}, expect=exp)
    b.line_chart_from_table("Error SD grows with the horizon", 1, [4, 5], a0, a1, anchor="J4", x_title="horizon (weeks)", y_title="orders")
    sdc = lambda k: f"Analysis!$D${a0 + KS.index(k)}"

    b.section("3. Interval half-widths / quantile offsets (error = actual - forecast; interval = forecast + offsets)")
    rows, exp = [], {}
    base_row = b.next_row + 1
    for i, k in enumerate(KS):
        rg_ = rk(f"ecal{k}", k)
        rows.append([k, f"={z1}*{sdc(k)}", f"=PERCENTILE({rg_},(1-{cc1})/2)", f"=PERCENTILE({rg_},(1+{cc1})/2)",
                     f"={z2}*{sdc(k)}", f"=PERCENTILE({rg_},(1-{cc2})/2)", f"=PERCENTILE({rg_},(1+{cc2})/2)"])
        exp.update({(i, 1): z[C1] * sd[k], (i, 2): qlo[(k, C1)], (i, 3): qhi[(k, C1)], (i, 4): z[C2] * sd[k], (i, 5): qlo[(k, C2)],
                    (i, 6): qhi[(k, C2)]})
    i0, i1 = b.table(["k", "Normal +/- (level 1)", "Empirical lower (level 1)", "Empirical upper (level 1)", "Normal +/- (level 2)",
                      "Empirical lower (level 2)", "Empirical upper (level 2)"], rows, fmt={j: "0.0" for j in range(1, 7)}, expect=exp)
    cell = lambda col, k: f"Analysis!${col}${i0 + KS.index(k)}"

    # hit columns ------------------------------------------------------------------------
    for k in KS:
        ek = b.col(f"e{k}")
        for lvl, (cnorm, clo, chi) in {C1: ("B", "C", "D"), C2: ("E", "F", "G")}.items():
            pct = int(round(lvl * 100))
            b.add_column(f"hitN{pct}_k{k}", lambda r, k=k, ek=ek, cnorm=cnorm: f"=IF(ABS(Data!{ek}{r})<={cell(cnorm, k)},1,0)",
                         hit[("n", lvl, k)], "0", first_row=7 * k + 2)
            b.add_column(f"hitE{pct}_k{k}", lambda r, k=k, ek=ek, clo=clo, chi=chi: f"=IF(AND(Data!{ek}{r}>={cell(clo, k)},Data!{ek}{r}<={cell(chi, k)}),1,0)",
                         hit[("e", lvl, k)], "0", first_row=7 * k + 2)

    def cov_table(title_sfx, crit, mask):
        rows, exp = [], {}
        base = b.next_row + 1
        for i, k in enumerate(KS):
            row = [k]
            for j, (m, lvl) in enumerate([("N", C1), ("E", C1), ("N", C2), ("E", C2)]):
                nm = f"hit{m}{int(round(lvl * 100))}_k{k}"
                row.append(f'=AVERAGEIFS({rk(nm, k)},{rk("t", k)},"{crit}"&{TL})')
                exp[(i, 1 + j)] = cov(("n" if m == "N" else "e", lvl, k), mask)
            rows.append(row)
        rows.append(["all four horizons"] + [f"=AVERAGE({chr(66 + j)}{base}:{chr(66 + j)}{base + 3})" for j in range(4)])
        for j, (m, lvl) in enumerate([("n", C1), ("e", C1), ("n", C2), ("e", C2)]):
            exp[(4, 1 + j)] = float(np.mean([cov((m, lvl, k), mask) for k in KS]))
        return b.table(["Horizon k (weeks)", "Normal, level 1", "Empirical, level 1", "Normal, level 2", "Empirical, level 2"], rows,
                       fmt={j: "0.0%" for j in range(1, 5)}, expect=exp)

    b.section("4. Coverage INSIDE the calibration period (should be close to the nominal levels by construction)")
    c0, c1 = cov_table("cal", "<=", cal_m)
    b.section("5. Coverage AFTER the calibration period (the honest test)")
    d0, d1 = cov_table("eval", ">", ev_m)
    b.bar_chart_from_table("Out-of-sample coverage of the level-2 intervals", 1, [4, 5], d0, d0 + 3, anchor="J24", y_title="share of actuals inside")
    ncov = b.row("Evaluation days per horizon (k = 1)", f"=COUNT({rk('aeval1', 1)})", n_ev, "0")
    se95 = b.row("Binomial SE of a coverage estimate at level 2", f"=SQRT({cc2}*(1-{cc2})/{b.local(ncov)})", math.sqrt(C2 * (1 - C2) / n_ev), "0.000",
                 "ignores that neighbouring errors are correlated, so it is too optimistic")
    zsc = b.row("z-score of the observed level-2 normal coverage at k = 1", f"=(D{d0}-{cc2})/{b.local(se95)}", (cov(("n", C2, 1), ev_m) - C2) / math.sqrt(C2 * (1 - C2) / n_ev), "0.0")

    b.section("6. Why it fails: errors after the calibration period are bigger")
    rows, exp = [], {}
    base = b.next_row + 1
    for i, k in enumerate(KS):
        ar = rk(f"aeval{k}", k)
        rows.append([k, f"={sdc(k)}", f"=SQRT(SUMSQ({ar})/COUNT({ar}))", f"=C{base + i}/B{base + i}",
                     f"=PERCENTILE({ar},{cc2})/B{base + i}", f"=PERCENTILE({ar},{cc1})/B{base + i}"])
        rms = float(np.sqrt(np.nanmean(aev[k] ** 2)))
        exp.update({(i, 1): sd[k], (i, 2): rms, (i, 3): rms / sd[k], (i, 4): float(np.nanpercentile(aev[k], 95)) / sd[k],
                    (i, 5): float(np.nanpercentile(aev[k], 80)) / sd[k]})
    v0, v1 = b.table(["k", "SD in calibration", "RMS error after Tcal", "Ratio", "z needed for 95% (plain 95th pct of |e| / SD)",
                      "z needed for 80%"], rows, fmt={1: "0.0", 2: "0.0", 3: "0.00", 4: "0.00", 5: "0.00"}, expect=exp)
    rows, exp = [], {}
    e1 = rg("e1", 9)
    blocks = []
    for j in range(NB):
        lo = 29 + 28 * j
        r0, r1_ = lo + 1, lo + 28
        s_ = float(np.std(e[1][lo - 1:lo + 27], ddof=1))
        blocks.append((df["date"].iloc[lo - 1], s_))
        rows.append([f"=Data!A{r0}", lo, f"=STDEV(Data!{b.col('e1')}{r0}:{b.col('e1')}{r1_})"])
        exp[(j, 2)] = s_
    k0, k1 = b.table(["Block start", "t", "SD of 1-week error in the 28-day block"], rows, fmt={0: "yyyy-mm-dd", 2: "0.0"}, expect=exp)
    b.line_chart_from_table("Volatility of the 1-week error by 28-day block", 1, [3], k0, k1, anchor="J44", y_title="SD (orders)")

    b.section("7. Operational fan: 28-day forecast after the last observation (seasonal naive, intervals use SD from ALL errors)")
    rows, exp = [], {}
    sd_all = {k: float(np.nanstd(e[k], ddof=1)) for k in KS}
    fan = []
    for h in range(1, 29):
        k = math.ceil(h / 7)
        src = N + 1 + h - 7 * k     # Excel row of the source day
        fval = y[src - 2]
        fan.append((df["date"].iloc[-1] + pd.Timedelta(days=h), k, fval, fval - z[C2] * sd_all[k], fval + z[C2] * sd_all[k],
                    fval - z[C1] * sd_all[k], fval + z[C1] * sd_all[k]))
        rr_ = b.next_row + h
        sdform = f"STDEV({rk(f'e{k}', k)})"
        rows.append([h, k, f"=Data!$A${N + 1}+A{rr_}", f"=Data!B{src}", f"=D{rr_}-{z2}*{sdform}", f"=D{rr_}+{z2}*{sdform}",
                     f"=D{rr_}-{z1}*{sdform}", f"=D{rr_}+{z1}*{sdform}"])
        exp.update({(h - 1, 3): fval, (h - 1, 4): fan[-1][3], (h - 1, 5): fan[-1][4], (h - 1, 6): fan[-1][5], (h - 1, 7): fan[-1][6]})
    f0, f1 = b.table(["h (days)", "k", "date", "Forecast", "Lower (level 2)", "Upper (level 2)", "Lower (level 1)", "Upper (level 1)"], rows,
                     fmt={2: "yyyy-mm-dd", 3: "0", 4: "0", 5: "0", 6: "0", 7: "0"}, expect=exp)
    wid1 = fan[0][4] - fan[0][3]
    wid28 = fan[27][4] - fan[27][3]
    b.row("Level-2 interval width at h = 1", f"=(F{f0}-E{f0})", wid1, "0.0")
    b.row("... at h = 28", f"=(F{f1}-E{f1})", wid28, "0.0")

    covN95 = [cov(("n", C2, k), ev_m) for k in KS]
    covE95 = [cov(("e", C2, k), ev_m) for k in KS]
    covN80 = [cov(("n", C1, k), ev_m) for k in KS]
    covE80 = [cov(("e", C1, k), ev_m) for k in KS]
    rms = {k: float(np.sqrt(np.nanmean(aev[k] ** 2))) for k in KS}
    b.answers([
        ("Compute the 1..4-week errors y[t] - y[t-7k] and the SD of each in the calibration period (t <= 224)", f"=Analysis!D{a0}",
         "SD: " + ", ".join(f"k={k}: {sd[k]:.1f}" for k in KS) + f". The error grows with the horizon: SD(4)/SD(1) = {sd[4] / sd[1]:.2f}, because "
         "the level wanders (a random-walk component), so a longer look-back accumulates more level change."),
        ("Does the sqrt(k) random-walk rule describe the growth?", f"=Analysis!F{a1}",
         f"Rule gives {sd[1] * 2:.1f} at k=4, data {sd[4]:.1f}: the rule overstates it, because part of the error is day-level noise that does not accumulate."),
        ("Level-2 (95%) normal interval half-width for k = 1..4", f"=Analysis!E{i0}",
         ", ".join(f"k={k}: +/-{z[C2] * sd[k]:.1f}" for k in KS) + ". These widths are only valid if the errors are roughly normal and the volatility stays at its calibration level."),
        ("Empirical 2.5% and 97.5% quantile offsets for each k; compare with the normal ones", f"=Analysis!F{i0}",
         ", ".join(f"k={k}: [{qlo[(k, C2)]:.1f}, {qhi[(k, C2)]:+.1f}]" for k in KS) +
         ". The empirical interval is not symmetric around 0: it contains the average bias (growth) and the skew of promotion days."),
        ("Coverage of the 80% and 95% intervals inside the calibration period", f"=Analysis!D{c0 + 4}",
         f"Normal 95%: {np.mean([cov(('n', C2, k), cal_m) for k in KS]):.1%}, empirical 95%: {np.mean([cov(('e', C2, k), cal_m) for k in KS]):.1%}; "
         f"80% levels {np.mean([cov(('n', C1, k), cal_m) for k in KS]):.1%} / {np.mean([cov(('e', C1, k), cal_m) for k in KS]):.1%}. "
         "Close to nominal, as it must be: the intervals were built from exactly these errors."),
        ("Coverage after the calibration period (t > 224), by horizon", f"=Analysis!D{d0 + 4}",
         f"Nominal 95%: normal {np.mean(covN95):.1%}, empirical {np.mean(covE95):.1%}; nominal 80%: normal {np.mean(covN80):.1%}, "
         f"empirical {np.mean(covE80):.1%} (k=1: {covN95[0]:.1%} and {covN80[0]:.1%}). Both methods under-cover, so the 'forecast ranges' "
         "promised more certainty than the data delivered."),
        ("Why: compare the error size after Tcal with the calibration SD, and the 28-day block volatility", f"=Analysis!D{v0}",
         "RMS error after Tcal / calibration SD: " + ", ".join(f"k={k}: {rms[k] / sd[k]:.2f}" for k in KS) +
         f". To reach 95% coverage a multiplier of about {np.nanpercentile(aev[1], 95) / sd[1]:.1f} (not 1.96) would have been needed at k=1. "
         "The block table shows the volatility step in autumn, which no calibration on the earlier months could know."),
        ("Operational fan: interval width at h = 1 and h = 28", f"=Analysis!F{f1}-Analysis!E{f1}",
         f"Level-2 width {wid1:.0f} orders at h=1 and {wid28:.0f} at h=28 (x{wid28 / wid1:.2f}); it widens in weekly steps because the seasonal naive uses "
         "the same lag for 7 consecutive horizons. Given the evaluation result the widths are probably still too narrow."),
        ("What would you change before publishing 95% ranges to the operations team?", "see text",
         "Recalibrate on a recent window (or inflate by the observed ratio), report coverage from a rolling backtest instead of the calibration "
         "sample, consider a log scale so that spread grows with the level, and say explicitly that the range ignores model risk and unforeseen promotions."),
    ])

    # ------------------------------------------------------------------- grafana
    d = Dash("stats-25-prediction-intervals", "25 · Prediction intervals and forecast uncertainty",
             "Residual-based and empirical-quantile intervals for the seasonal naive forecast, their widening with the horizon and a "
             "coverage check on days the intervals were not fitted on.",
             pd.DataFrame({"time": list(df["date"].iloc[-NH:]) + [x[0] for x in fan]}), "time")
    d.stat("Out-of-sample coverage, mean of 4 horizons (nominal 80% / 95%)",
           {"normal 80%": float(np.mean(covN80)), "empirical 80%": float(np.mean(covE80)), "normal 95%": float(np.mean(covN95)),
            "empirical 95%": float(np.mean(covE95))},
           "Share of days after t = 224 whose actual fell inside the interval. Compare with 0.80 and 0.95.", unit="percentunit", decimals=1,
           thresholds=[(None, "red"), (0.78, "orange"), (0.93, "green")])
    ts = pd.DataFrame({"time": list(df["date"].iloc[-NH:]) + [x[0] for x in fan]})
    ts["orders"] = list(y[-NH:]) + [np.nan] * 28
    ts["forecast"] = [np.nan] * (NH - 1) + [y[-1]] + [x[2] for x in fan]
    ts["95% lower"] = [np.nan] * NH + [x[3] for x in fan]
    ts["95% upper"] = [np.nan] * NH + [x[4] for x in fan]
    ts["80% lower"] = [np.nan] * NH + [x[5] for x in fan]
    ts["80% upper"] = [np.nan] * NH + [x[6] for x in fan]
    d.timeseries("Orders (last 16 weeks) and the 28-day forecast fan", ts,
                 "The ranges widen in weekly steps and are centred on the seasonal naive forecast (the last week repeated).",
                 dashed=["95% lower", "95% upper", "80% lower", "80% upper"],
                 colors={"orders": "#9AA5B1", "forecast": "#4E79A7", "95% lower": "#E15759", "95% upper": "#E15759",
                         "80% lower": "#F28E2B", "80% upper": "#F28E2B"}, w=24, h=9)
    d.bars("Error SD by horizon (calibration period)", pd.DataFrame({"horizon": [f"{k} wk" for k in KS], "SD of error": [sd[k] for k in KS],
                                                                  "sqrt(k) rule": [sd[1] * math.sqrt(k) for k in KS]}),
           "The error grows with the horizon, slower than the random-walk rule.", w=8, h=8)
    d.bars("95% coverage by horizon", pd.DataFrame({"horizon": [f"{k} wk" for k in KS],
                                                    "normal, calibration": [cov(("n", C2, k), cal_m) for k in KS],
                                                    "normal, after Tcal": covN95, "empirical, after Tcal": covE95, "nominal": [C2] * 4}),
           "Inside the calibration period the intervals look perfect; afterwards they miss by 10-15 points.", unit="percentunit", w=8, h=8)
    bd = pd.DataFrame({"block start": [f"{x[0]:%b %d}" for x in blocks], "SD of 1-week error": [x[1] for x in blocks]})
    d.bars("Volatility of the 1-week error (28-day blocks)", bd, "The jump in the September blocks is the regime change the intervals did not know about.", w=8, h=8)
    d.save(out)

    md(out / "theory.md", fill(THEORY, **EX))
    md(out / "task.md", TASK)
    return b


THEORY = r"""
# Theory: prediction intervals and forecast uncertainty

## Why a point forecast is not enough

"Next week we will get 1,310 orders" invites a decision (how many packers to book) that depends on *how wrong* the number can
be. A **prediction interval** is a range that should contain the future observation with a stated probability, say 95%. It is not
a confidence interval for a parameter (lesson 17 / [bootstrapping](../17-bootstrapping-and-confidence-intervals/theory.md)):
it must cover the **new observation**, so it includes the noise of that single future day *and* the uncertainty about the level
and trend. The failure this lesson prevents is the interval that looks reasonable on the data it was fitted to and then misses
far more often than promised.

## Residual-based (normal) intervals

If forecast errors $e_h = y_{T+h}-\hat y_{T+h\mid T}$ are roughly normal with mean 0 and standard deviation $\sigma_h$:

$$
\hat y_{T+h\mid T} \pm z_{(1+c)/2}\,\sigma_h,\qquad z_{0.975}=1.960,\; z_{0.90}=1.282 .
$$

The key is $\sigma_h$ at **each horizon**, estimated from *out-of-sample* errors of the same method at the same horizon. The
standard deviation of the one-step *in-sample residuals* understates it: it ignores that the level and parameters change
between the origin and the target. Errors typically grow with the horizon. If the level behaves like a random walk and the
daily noise is independent, then $\operatorname{Var}(e_h) = 2\sigma_\varepsilon^2 + h\,\sigma_w^2$: a constant part plus a part
linear in $h$. For the seasonal naive method, whose error at horizon $h$ is $y_t - y_{t-7k}$ with $k=\lceil h/7\rceil$, the
interval widens in weekly *steps*; the "random-walk rule" $\sigma_k=\sigma_1\sqrt{k}$ is an upper estimate because the
$2\sigma_\varepsilon^2$ part does not accumulate.

## Empirical-quantile intervals

Skip the normal assumption: take the errors $e^{(1)},\dots,e^{(m)}$ of the calibration set and use their quantiles,

$$
\bigl[\hat y + Q_{(1-c)/2}(e),\;\; \hat y + Q_{(1+c)/2}(e)\bigr].
$$

The offsets can be asymmetric and include any average bias, which is what you want when promotions skew the errors to one side.
The price is data: the 2.5% tail of 200 errors is five points. Use at least a few hundred errors for a 95% interval or accept
that its ends are noisy.

**Worked example.** Calibration errors $e = (-9,-4,-2,0,1,3,4,6,9,14)$, $n=@@N@@$, mean @@MEAN@@, SD @@SD@@, point forecast 200,
90% interval. *Normal:* $z=@@Z@@$, half-width $=@@HW@@$, interval $[@@NLO@@, @@NHI@@]$. *Empirical* (linear-interpolation percentiles,
as Excel's `PERCENTILE`): $Q_{5\%}=@@QLO@@$, $Q_{95\%}=@@QHI@@$, interval $[@@ELO@@, @@EHI@@]$. The empirical interval leans to the
right because the error sample has a long right tail (+14); the normal one is symmetric and puts the same weight on both sides.

## Checking coverage

An interval with nominal level $c$ is **calibrated** if the observed share of actuals inside it is close to $c$. Compute coverage
(a) on the calibration data (will look perfect: the intervals were built from those errors) and (b) on **later** data, by horizon.
Sampling noise matters: with $n$ evaluation points the binomial standard error of the coverage is $\sqrt{c(1-c)/n}$ (about
2 points for $n=126$ at 95%), and since neighbouring errors are correlated the true uncertainty is larger. A shortfall
of 10-15 points is not noise. Also report the **width**: an interval that covers 99% by being enormous is useless; a good one is
both calibrated and as narrow as possible.

## What makes intervals too narrow in practice

1. **Regime change / changing volatility**: the calibration period was calmer than the future (here the volatility rises in autumn).
2. **Ignored model and parameter uncertainty**: the formula assumes the model structure is right.
3. **Autocorrelated errors**: errors at consecutive horizons are positively correlated, so they do not average out; a weekly total
   cannot be bounded by adding daily intervals.
4. **Non-normal errors**: promotions, outages and holidays create fat, skewed tails.
5. **Level-dependent spread**: if the noise grows with the level, use a log transform or a percentage error.
6. **In-sample residuals**: the SD of fitted residuals understates out-of-sample error (lessons 22-24).

## Practical recipe

Backtest ([lesson 24](../24-backtesting-and-forecast-accuracy/theory.md)) the method over many origins, keep the errors **by
horizon**, form the interval from the most recent window of errors, check coverage on origins not used for the calibration, and
widen the interval (or lengthen the window) until the coverage on held-out origins matches the promise. Publish the coverage you
measured next to the interval.

## Related notes

- [Naive and seasonal naive forecasts](../21-naive-and-seasonal-naive-forecasts/theory.md)
- [Trend and seasonal regression forecasting](../22-trend-and-seasonal-regression-forecasting/theory.md) and [exponential smoothing](../23-exponential-smoothing-models/theory.md)
- [Residual analysis and diagnostics](../15-residual-analysis-and-model-diagnostics/theory.md)
- [Statistical process control](../26-statistical-process-control/theory.md): the same idea of a noise band, used for monitoring
- Repo note: [forecast evaluation](../../notes/time_series/forecast_evaluation.md)
"""

TASK = r"""
# Task: prediction intervals and forecast uncertainty

## Scenario

Operations plans packing capacity from Hearthside's order forecast, which is simply "the same weekday last week" (the seasonal
naive rule). They now ask for a **range**: *"give us a number we can staff for with 95% confidence, one to four weeks ahead."*
You will build the ranges from the method's own past errors and then test whether a nominal 80% / 95% range really contains
that share of future days.

## Data

`data.csv` - 350 consecutive days, 2025-01-06 (Monday) to 2025-12-20, one row per day.

| column | meaning |
|---|---|
| `date` | calendar day |
| `orders` | orders placed that day |

The forecast for day t made k weeks earlier is `orders[t - 7k]` (k = 1, 2, 3, 4), so its error is `e_k(t) = orders[t] - orders[t - 7k]`.
**Calibration period: t <= 224** (first 32 weeks). **Evaluation: t > 224** (the last 126 days). Put 224 and the two confidence
levels (80%, 95%) in input cells.

## Questions

Work in a spreadsheet (import `data.csv`), then compare with `solution.xlsx`.

1. Build the four error columns e_1..e_4. Compute the mean and SD of each over the calibration period. How does the SD change with k?
2. Compare SD(k) with the random-walk rule SD(1) * sqrt(k). Which is larger at k = 4, and why?
3. Build normal intervals (forecast +/- z * SD(k)) for 80% and 95%. Report the 95% half-widths for k = 1..4.
4. Build empirical intervals from the 10%/90% and 2.5%/97.5% percentiles of the calibration errors (`PERCENTILE`). How do they differ from the normal ones?
5. For each horizon, compute the share of calibration-period days whose error lies inside each of the four intervals (normal/empirical x 80%/95%).
6. Repeat on the evaluation days (t > 224). Which intervals under-cover, by how much, and is the shortfall larger than the binomial standard error?
7. Compute the RMS error after t = 224 relative to the calibration SD, and the SD of the 1-week error in consecutive 28-day blocks. What happened?
8. Produce the 28-day forecast after the last observation with 80% and 95% bounds (use the SD of all errors at each k). How much wider is the interval at h = 28 than at h = 1?
9. *Explain in 3-4 sentences* what you would change before sending 95% ranges to operations.

## Grafana

Import `grafana/dashboard.json` (see `../grafana/README.md`; no data-source setup is needed).

- In "Orders (last 16 weeks) and the 28-day forecast fan", where does the band step wider, and does it look wide enough compared with the recent day-to-day swings?
- In "95% coverage by horizon", compare the calibration and evaluation bars. Which intervals are closest to the nominal level?
- In "Volatility of the 1-week error (28-day blocks)", in which blocks does the volatility change?

## Deliverable

A short note (6-8 lines): *what range do you give operations, how often will it fail, and why?* Include the coverage table (calibration vs
evaluation), the fan chart, and one sentence on how you would keep the intervals honest as new data arrive.
"""
