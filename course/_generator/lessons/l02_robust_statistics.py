"""Lesson 02 - Robust statistics."""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import Book, Dash, md, write_csv  # noqa: E402

SLUG = "02-robust-statistics"
TITLE = "Robust statistics"
MODULE = "Understanding data beyond averages"
DATASET = "288 temperature readings (10 min apart) from two sensors in a cold room; sensor A has driver error codes"
TRIM = 0.10  # TRIMMEAN proportion (total, both tails)
WINS = 0.05  # winsorise at P5 / P95
KS = [14, 29, 58, 100, 150]  # number of corrupted readings in the breakdown table
MAD_K = 1.4826


def make_data() -> pd.DataFrame:
    rng = np.random.default_rng(202)
    n = 288
    t = pd.date_range("2026-01-12 00:00:00", periods=n, freq="10min")
    h = np.arange(n) * 10 / 60
    base = 21.5 + 0.9 * np.sin(2 * np.pi * (h - 9) / 24)  # slow daily cycle of the room
    a = (base + rng.normal(0, 0.25, n)).round(2)
    b = (base + rng.normal(0, 0.25, n)).round(2)
    bad = rng.choice(np.arange(5, n - 5), 10, replace=False)
    a[bad[:9]] = 85.0  # DS18B20 power-on-reset value
    a[bad[9]] = -127.0  # DS18B20 "sensor disconnected" value
    return pd.DataFrame({"timestamp": t, "temp_a_c": a, "temp_b_c": b})


def trimmed(v, prop=TRIM):
    k = int(len(v) * prop / 2)  # Excel TRIMMEAN: floor(n*prop/2) values removed from each end
    s = np.sort(v)
    return float(s[k:len(v) - k].mean())


def winsor(v, p=WINS):
    lo, hi = np.percentile(v, 100 * p), np.percentile(v, 100 * (1 - p))
    return np.clip(v, lo, hi)


def mad(v):
    return float(np.median(np.abs(v - np.median(v))))


def iqr(v):
    return float(np.percentile(v, 75) - np.percentile(v, 25))


def corrupt(v, k):
    w = v.copy()
    w[:k] = 85.0
    return w


def build(out: Path) -> Book:
    df = make_data()
    write_csv(out, df)
    a, bb = df["temp_a_c"].to_numpy(), df["temp_b_c"].to_numpy()
    n = len(df)
    sd = lambda v: float(np.std(v, ddof=1))

    b = Book(df, "Lesson 02 - Robust statistics",
             "Solved workbook. Yellow cells are assumptions you can change; everything else is a live formula.")
    A, B = b.rng("temp_a_c"), b.rng("temp_b_c")
    ca, cb = b.col("temp_a_c"), b.col("temp_b_c")
    loc = b.local

    b.section("1. Classical estimates")
    meanA = b.row("Sensor A: mean (C)", f"=AVERAGE({A})", a.mean(), "0.000")
    meanB = b.row("Sensor B: mean (C)", f"=AVERAGE({B})", bb.mean(), "0.000")
    sdA = b.row("Sensor A: standard deviation (C)", f"=STDEV({A})", sd(a), "0.000")
    sdB = b.row("Sensor B: standard deviation (C)", f"=STDEV({B})", sd(bb), "0.000")

    b.section("2. Robust centre")
    trim = b.row("TRIMMEAN proportion (total, both tails)", TRIM, None, "0%", "10 % -> 5 % cut from each end", is_input=True)
    wins = b.row("Winsorising level (each tail)", WINS, None, "0%", "values are clipped to P5 / P95", is_input=True)
    medA = b.row("Sensor A: median (C)", f"=MEDIAN({A})", float(np.median(a)), "0.000")
    medB = b.row("Sensor B: median (C)", f"=MEDIAN({B})", float(np.median(bb)), "0.000")
    trA = b.row("Sensor A: trimmed mean", f"=TRIMMEAN({A},{loc(trim)})", trimmed(a), "0.000")
    trB = b.row("Sensor B: trimmed mean", f"=TRIMMEAN({B},{loc(trim)})", trimmed(bb), "0.000")
    loA = b.row("Sensor A: lower winsor bound (C)", f"=PERCENTILE({A},{loc(wins)})", float(np.percentile(a, 5)), "0.000")
    hiA = b.row("Sensor A: upper winsor bound (C)", f"=PERCENTILE({A},1-{loc(wins)})", float(np.percentile(a, 95)), "0.000")
    loB = b.row("Sensor B: lower winsor bound (C)", f"=PERCENTILE({B},{loc(wins)})", float(np.percentile(bb, 5)), "0.000")
    hiB = b.row("Sensor B: upper winsor bound (C)", f"=PERCENTILE({B},1-{loc(wins)})", float(np.percentile(bb, 95)), "0.000")
    wa, wb = winsor(a), winsor(bb)
    b.add_column("winsor_a", lambda r: f"=MIN(MAX(Data!{ca}{r},Analysis!$B${loA.split('$')[-1]}),Analysis!$B${hiA.split('$')[-1]})",
                 expected=wa)
    b.add_column("winsor_b", lambda r: f"=MIN(MAX(Data!{cb}{r},Analysis!$B${loB.split('$')[-1]}),Analysis!$B${hiB.split('$')[-1]})",
                 expected=wb)
    wA = b.row("Sensor A: winsorised mean", f"=AVERAGE({b.rng('winsor_a')})", float(wa.mean()), "0.000")
    wB = b.row("Sensor B: winsorised mean", f"=AVERAGE({b.rng('winsor_b')})", float(wb.mean()), "0.000")

    b.section("3. Robust spread")
    iqrA = b.row("Sensor A: IQR (C)", f"=QUARTILE({A},3)-QUARTILE({A},1)", iqr(a), "0.000")
    iqrB = b.row("Sensor B: IQR (C)", f"=QUARTILE({B},3)-QUARTILE({B},1)", iqr(bb), "0.000")
    b.row("Sensor A: IQR / 1.349 (normal-consistent SD)", f"={loc(iqrA)}/1.349", iqr(a) / 1.349, "0.000")
    b.row("Sensor B: IQR / 1.349 (normal-consistent SD)", f"={loc(iqrB)}/1.349", iqr(bb) / 1.349, "0.000")
    b.add_column("absdev_a", lambda r: f"=ABS(Data!{ca}{r}-Analysis!$B${medA.split('$')[-1]})", expected=np.abs(a - np.median(a)))
    b.add_column("absdev_b", lambda r: f"=ABS(Data!{cb}{r}-Analysis!$B${medB.split('$')[-1]})", expected=np.abs(bb - np.median(bb)))
    madA = b.row("Sensor A: MAD (median absolute deviation)", f"=MEDIAN({b.rng('absdev_a')})", mad(a), "0.000")
    madB = b.row("Sensor B: MAD", f"=MEDIAN({b.rng('absdev_b')})", mad(bb), "0.000")
    sA = b.row("Sensor A: 1.4826 x MAD (normal-consistent SD)", f"={MAD_K}*{loc(madA)}", MAD_K * mad(a), "0.000")
    sB = b.row("Sensor B: 1.4826 x MAD (normal-consistent SD)", f"={MAD_K}*{loc(madB)}", MAD_K * mad(bb), "0.000")

    b.section("4. Finding and removing the damage in sensor A")
    thr = b.row("Threshold: robust SDs from the median", 10, None, "0", "Edit me", is_input=True)
    cut = 10 * MAD_K * mad(a)
    far = np.abs(a - np.median(a)) > cut
    nfar = b.row("Readings further than the threshold", f"=COUNTIF({b.rng('absdev_a')},\">\"&{loc(thr)}*{loc(sA)})",
                 int(far.sum()), "0")
    b.row("... of which exactly 85.0 or -127.0 (driver error codes)", f"=COUNTIF({A},85)+COUNTIF({A},-127)",
          int(((a == 85) | (a == -127)).sum()), "0")
    cleanA = b.row("Sensor A: mean without those readings",
                   f"=AVERAGEIF({b.rng('absdev_a')},\"<=\"&{loc(thr)}*{loc(sA)},{A})", float(a[~far].mean()), "0.000")
    b.row("Sensor A: mean without them minus sensor B mean (C)", f"={loc(cleanA)}-{loc(meanB)}", float(a[~far].mean() - bb.mean()),
          "0.000", "calibration difference between the sensors")
    b.row("Classical 3-sigma upper limit for A (mean + 3 SD)", f"={loc(meanA)}+3*{loc(sdA)}", a.mean() + 3 * sd(a), "0.0")
    b.row("Classical 3-sigma lower limit for A (mean - 3 SD)", f"={loc(meanA)}-3*{loc(sdA)}", a.mean() - 3 * sd(a), "0.0")
    upA = b.row("Robust upper limit for A (median + 3 x 1.4826 MAD)", f"={loc(medA)}+3*{loc(sA)}",
                float(np.median(a) + 3 * MAD_K * mad(a)), "0.0")
    b.row("Robust lower limit for A (median - 3 x 1.4826 MAD)", f"={loc(medA)}-3*{loc(sA)}",
          float(np.median(a) - 3 * MAD_K * mad(a)), "0.0")

    b.section("5. Influence of ONE extra reading added to the clean sensor B")
    xs = [22, 30, 85, 500, 5000]
    rows, exp = [], {}
    r0 = b.next_row + 1
    for i, xv in enumerate(xs):
        r = r0 + i
        rows.append([xv, f"=(SUM({B})+A{r})/(COUNT({B})+1)", f"=MEDIAN({B},A{r})", f"=B{r}-{loc(meanB)}", f"=C{r}-{loc(medB)}"])
        m_new, md_new = (bb.sum() + xv) / (n + 1), float(np.median(np.append(bb, xv)))
        exp.update({(i, 1): m_new, (i, 2): md_new, (i, 3): m_new - bb.mean(), (i, 4): md_new - np.median(bb)})
    i0, i1 = b.table(["Extra reading X (C)", "Mean", "Median", "Mean shift", "Median shift"], rows,
                     fmt={1: "0.000", 2: "0.000", 3: "0.000", 4: "0.0000"}, expect=exp)
    infl = {xv: (exp[(i, 3)], exp[(i, 4)]) for i, xv in enumerate(xs)}

    b.section("6. Breakdown: overwrite the first k readings of sensor B with 85.0")
    for k in KS:
        b.add_column(f"b_bad{k}", lambda r, k=k: f"=IF(ROW()-1<={k},85,Data!{cb}{r})", expected=corrupt(bb, k), fmt="0.00")
    rows, exp = [], {}
    r0 = b.next_row + 1
    for i, k in enumerate(KS):
        rg = b.rng(f"b_bad{k}")
        cbad = corrupt(bb, k)
        r = r0 + i
        lo_, hi_ = np.percentile(cbad, 5), np.percentile(cbad, 95)
        lo_c, hi_c = f"E{r}", f"F{r}"
        rows.append([k, f"=A{r}/COUNT({rg})", f"=AVERAGE({rg})", f"=TRIMMEAN({rg},{loc(trim)})",
                     f"=PERCENTILE({rg},{loc(wins)})", f"=PERCENTILE({rg},1-{loc(wins)})",
                     f"=SUMPRODUCT(({rg}<{lo_c})*{lo_c}+({rg}>{hi_c})*{hi_c}+({rg}>={lo_c})*({rg}<={hi_c})*{rg})/COUNT({rg})",
                     f"=MEDIAN({rg})"])
        exp.update({(i, 1): k / n, (i, 2): cbad.mean(), (i, 3): trimmed(cbad), (i, 4): lo_, (i, 5): hi_,
                    (i, 6): float(winsor(cbad).mean()), (i, 7): float(np.median(cbad))})
    j0, j1 = b.table(["k corrupted", "share", "Mean", "Trimmed mean", "P5", "P95", "Winsorised mean", "Median"], rows,
                     fmt={1: "0.0%", 2: "0.00", 3: "0.00", 4: "0.00", 5: "0.00", 6: "0.00", 7: "0.00"}, expect=exp)
    breakdown = {k: (exp[(i, 2)], exp[(i, 3)], exp[(i, 6)], exp[(i, 7)]) for i, k in enumerate(KS)}
    b.line_chart("Sensor A vs sensor B (C)", "timestamp", ["temp_a_c", "temp_b_c"], anchor="H4", y_title="C")
    b.bar_chart_from_table("Estimates of the centre when k readings are corrupted (C)", 1, [3, 4, 7, 8], j0, j1, anchor="H24",
                           x_title="k corrupted readings", y_title="C")

    b.answers([
        ("Mean and SD of both sensors", f"={meanA}",
         f"A: mean {a.mean():.2f}, SD {sd(a):.2f}. B: mean {bb.mean():.2f}, SD {sd(bb):.2f}. The two sensors watch the same room, yet the SD of A "
         f"is {sd(a) / sd(bb):.0f}x larger and its mean {a.mean() - bb.mean():.2f} C higher."),
        ("Median, 10 % trimmed mean and 5 % winsorised mean of both", f"={medA}",
         f"Sensor A: median {np.median(a):.2f}, trimmed {trimmed(a):.2f}, winsorised {wa.mean():.2f}. Sensor B: {np.median(bb):.2f}, {trimmed(bb):.2f}, "
         f"{wb.mean():.2f}. The robust centres of A agree with B within {max(abs(np.median(a) - np.median(bb)), abs(trimmed(a) - trimmed(bb)), abs(wa.mean() - wb.mean())):.2f} C."),
        ("IQR, IQR/1.349, MAD, 1.4826 MAD versus SD", f"={sA}",
         f"A: IQR {iqr(a):.2f}, 1.4826 MAD {MAD_K * mad(a):.2f} against SD {sd(a):.2f}. B: IQR {iqr(bb):.2f}, 1.4826 MAD {MAD_K * mad(bb):.2f}, SD {sd(bb):.2f}. "
         "Robust scales of A match those of B; only the SD is wrecked."),
        ("Readings further than 10 robust SDs from the median; values; mean without them", f"={nfar}",
         f"{int(far.sum())} readings (9 x 85.0 and 1 x -127.0 - the DS18B20 power-on-reset and disconnected codes). Without them the mean of A is "
         f"{a[~far].mean():.2f}, {a[~far].mean() - bb.mean():+.2f} C from B (a small calibration difference)."),
        ("Add one reading X (22, 30, 85, 500, 5000) to sensor B: new mean and median", f"={meanB}",
         f"X = 5000 moves the mean by {infl[5000][0]:.1f} C but the median by {infl[5000][1]:.4f} C; X = 85 moves them by {infl[85][0]:.2f} and "
         f"{infl[85][1]:.4f}. The mean's influence grows without bound with X; the median's is bounded."),
        ("Overwrite k = 14, 29, 58, 100, 150 readings of B by 85: which estimator breaks where?", f"=Analysis!H{j0 + 2}",
         f"k = 29 (10 %): mean {breakdown[29][0]:.1f}, trimmed {breakdown[29][1]:.2f}, winsorised {breakdown[29][2]:.2f}, median {breakdown[29][3]:.2f}. "
         f"k = 58 (20 %): trimmed {breakdown[58][1]:.1f}, winsorised {breakdown[58][2]:.1f}, median {breakdown[58][3]:.2f}. "
         f"k = 150 (52 %): even the median is {breakdown[150][3]:.1f}. Breakdown points: mean 0 %, 10 % trimmed mean 5 % per tail (10 % total), 5 % winsorised mean 5 %, median 50 %."),
        ("3-sigma limits of A computed classically and robustly", f"={upA}",
         f"Classical: {a.mean() - 3 * sd(a):.0f} to {a.mean() + 3 * sd(a):.0f} C - a 35 C reading would pass. Robust: "
         f"{np.median(a) - 3 * MAD_K * mad(a):.1f} to {np.median(a) + 3 * MAD_K * mad(a):.1f} C - catches every bad reading and none of the ordinary ones."),
        ("Interpretation and limitations", "see text",
         "Robust estimates are right here because the damage is a handful of impossible driver codes. They are not a substitute for looking at the data: "
         "if 10 % of readings were genuine heat events, the median would hide them. Robust estimators also pay a price on clean data (the median has about "
         "64 % of the mean's efficiency for normal data), and a MAD of zero (many ties) makes the robust SD collapse."),
    ])

    # ------------------------------------------------------------------- grafana
    d = Dash("stats-02-robust-statistics", "02 · Robust statistics",
             "Ten driver error codes in sensor A: classical vs robust centre and spread, and where each estimator breaks down "
             "(values computed from data.csv).", df.rename(columns={"timestamp": "time"}), "time")
    d.stat("Sensor A: classical vs robust (C)",
           {"mean": a.mean(), "median": np.median(a), "trimmed mean": trimmed(a), "SD": sd(a),
            "1.4826 x MAD": MAD_K * mad(a), "sensor B median": np.median(bb)},
           "Sensor B is clean and sits in the same room, so it shows what A should read.", decimals=2,
           thresholds=[(None, "blue")])
    raw = pd.DataFrame({"time": df["timestamp"], "temp_b_c": bb, "temp_a_c": a})
    d.timeseries("Raw readings, sensor A vs sensor B", raw,
                 "The spikes (85.0) and the single -127.0 are the DS18B20 error codes; on this scale every real reading is a flat line.",
                 unit="celsius", colors={"temp_a_c": "#E15759", "temp_b_c": "#4E79A7"})
    zoom = pd.DataFrame({"time": df["timestamp"], "temp_b_c": bb, "temp_a_c_zoom": np.where((a > 15) & (a < 30), a, np.nan),
                         "A mean": a.mean(), "A median": np.median(a)})
    d.timeseries("Same data, readings between 15 and 30 C only", zoom,
                 "Without the bad codes the sensors agree (slow daily cycle of about 1.8 C). The mean of A sits above nearly all real readings; its median in the middle.",
                 dashed=["A mean", "A median"], unit="celsius",
                 colors={"temp_a_c_zoom": "#E15759", "temp_b_c": "#4E79A7", "A mean": "#F28E2B", "A median": "#59A14F"})
    sp = pd.DataFrame({"scale": ["SD", "IQR / 1.349", "1.4826 x MAD"],
                       "sensor_A": [sd(a), iqr(a) / 1.349, MAD_K * mad(a)],
                       "sensor_B": [sd(bb), iqr(bb) / 1.349, MAD_K * mad(bb)]}).round(3)
    d.bars("Three estimates of the spread (C)", sp, "Only the classical SD is destroyed by ten bad readings.", unit="celsius")
    ks = np.arange(0, 151, 3)
    curves = []
    for k in ks:
        cb_ = corrupt(bb, k)
        curves.append([100 * k / n, cb_.mean(), trimmed(cb_), float(winsor(cb_).mean()), float(np.median(cb_))])
    cdf = pd.DataFrame(curves, columns=["percent_corrupted", "mean", "trimmed_mean_10", "winsorised_5", "median"]).round(3)
    d.xy("Breakdown curves: B with k% of readings overwritten by 85", cdf, "percent_corrupted",
         ["mean", "trimmed_mean_10", "winsorised_5", "median"],
         "The mean moves immediately, the trimmed and winsorised means resist until their trimming level is exceeded, the median "
         "until about 50 %.", lines=["mean", "trimmed_mean_10", "winsorised_5", "median"])
    d.save(out)

    md(out / "theory.md", fill(THEORY, theory_values()))
    md(out / "task.md", TASK)
    return b


def fill(text: str, vals: dict) -> str:
    for k, v in vals.items():
        text = text.replace(f"<<{k}>>", str(v))
    return text


def theory_values() -> dict:
    ex = np.array([21.4, 21.6, 21.5, 21.7, 85.0, 21.3, 21.5, 21.6, 21.4])
    m = np.median(ex)
    return {
        "n": len(ex), "mean": f"{ex.mean():.2f}", "sd": f"{np.std(ex, ddof=1):.2f}", "med": f"{m:.1f}",
        "mad": f"{mad(ex):.1f}", "smad": f"{MAD_K * mad(ex):.2f}", "mean_wo": f"{ex[ex < 80].mean():.2f}",
        "sd_wo": f"{np.std(ex[ex < 80], ddof=1):.2f}", "tr": f"{trimmed(ex, 0.25):.2f}",
        "devs": ", ".join(f"{v:.1f}" for v in np.sort(np.abs(ex - m))),
        "wins_hi": f"{np.percentile(ex, 90):.2f}", "wins_mean": f"{winsor(ex, 0.10).mean():.2f}",
        "wins_lo": f"{np.percentile(ex, 10):.2f}",
        "dmean": f"{ex.mean() - ex[ex < 80].mean():.1f}", "dsd": f"{np.std(ex, ddof=1) / np.std(ex[ex < 80], ddof=1):.0f}",
        "dmed": f"{abs(m - np.median(ex[ex < 80])):.2f}",
    }


THEORY = r"""
# Theory: robust statistics

## Why a few points can ruin an average

Sensors glitch, logs contain sentinel values (`-1`, `9999`, `85.0`), a data-entry slip adds a zero. If your estimate changes a lot
when a handful of observations change, it is not safe to run unattended: a dashboard, a control chart or a forecasting pipeline fed with it
will fail silently. **Robust statistics** are estimators whose value stays close to the "right" answer when a small share of the data is
arbitrarily wrong or comes from a different process. The price is a little less precision on perfectly clean, normal data.

## How we measure robustness

Two ideas capture most of what you need.

- **Breakdown point**: the smallest fraction of observations that can be replaced by arbitrary values to make the estimator
  arbitrarily bad. The sample mean and the standard deviation have breakdown point 0 (one bad value is enough), the median and the MAD have 50 %
  (the maximum possible), the IQR 25 %, a trimmed mean with $\alpha$ trimmed from each tail has $\alpha$.
- **Influence**: how much one extra observation at value $x$ moves the estimate. For the mean it is $(x-\bar x)/(n+1)$ - unbounded in $x$.
  For the median it is bounded: once $x$ is beyond the centre, it only changes which of the middle order statistics is selected.

## The estimators

**Centre.**

- *Median*: the middle order statistic (average of the two middle ones for even $n$).
- *Trimmed mean*: sort, drop the lowest and highest $\alpha n$ values, average the rest. Excel/Sheets `TRIMMEAN(range, p)` takes $p$ as the **total**
  proportion removed (both tails) and removes $\lfloor np/2\rfloor$ from each end.
- *Winsorised mean*: instead of dropping the extremes, clip them to the $\alpha$ and $1-\alpha$ percentiles, then average. It keeps the sample size
  (and the weight of the tail observations, but capped).

**Scale.**

- *IQR* $= Q_3 - Q_1$. For normal data $\text{IQR}\approx1.349\,\sigma$, so $\text{IQR}/1.349$ estimates $\sigma$.
- *MAD* $=\operatorname{median}_i\,|x_i-\operatorname{median}(x)|$. For normal data $\text{MAD}\approx0.6745\,\sigma$, so
  $\hat\sigma = 1.4826\cdot\text{MAD}$ (since $1.4826 = 1/\Phi^{-1}(0.75)$).

The factors 1.349 and 1.4826 make the estimators agree with $\sigma$ *for normal data*; for skewed data the scaled MAD or IQR is a robust measure of
spread, not an estimate of the SD.

## Worked example

Nine readings of a room temperature: $21.4,\ 21.6,\ 21.5,\ 21.7,\ 85.0,\ 21.3,\ 21.5,\ 21.6,\ 21.4$ (the 85.0 is a sensor reset code).

- mean $=<<mean>>$, SD $=<<sd>>$ - both useless.
- median $=<<med>>$. Absolute deviations from it, sorted: <<devs>>; their median is MAD $=<<mad>>$, so $1.4826\cdot\text{MAD}=<<smad>>$.
- Without the 85.0 the mean is <<mean_wo>> and the SD <<sd_wo>>; the median-based answers were already close to these.
- A 25 % trimmed mean drops the two smallest and two largest values: <<tr>>.
- Winsorising at P10/P90 (bounds <<wins_lo>> and <<wins_hi>> with linear-interpolation percentiles, as `PERCENTILE` computes) gives a mean of <<wins_mean>>.

One bad value out of nine moved the mean by <<dmean>> C and multiplied the SD by about <<dsd>>; the median moved by <<dmed>> C.

## Choosing an estimator

| situation | centre | scale |
|---|---|---|
| clean, symmetric, light tails | mean | SD |
| a few suspected gross errors | median or 5-10 % trimmed mean | 1.4826 MAD or IQR/1.349 |
| heavy tails that are real (not errors) | median plus the mean (they answer different questions) | MAD, quantile ranges |
| need to use all points but cap influence | winsorised mean | winsorised SD |

For normal data the median has asymptotic efficiency $2/\pi\approx 64\,\%$ relative to the mean (its sampling variance is 1.57 times larger); a 10 % trimmed mean
loses only a few percent. That is the insurance premium for robustness.

## Assumptions and pitfalls

1. **Robust is not "ignore the data".** A median does not tell you that 3 % of your readings are `85.0`. Always count and look at the points
   that robust and classical estimates disagree about (see [outlier detection](../04-outlier-detection/theory.md)).
2. **Breakdown is a limit.** If a third of the readings are corrupted a 10 % trimmed mean fails; if more than half are, nothing can save the median.
3. **Genuine heavy tails are not contamination.** Robust centres of a [heavy-tailed](../01-distribution-shapes-and-heavy-tails/theory.md) variable estimate the typical
   value, not the total; the mean is still the right target for totals.
4. **Ties break the MAD.** If more than half of the values are identical (counts, rounded data) then MAD $=0$ and any observation
   is "infinitely" far; use IQR or add a small floor.
5. **Different tools, different conventions.** `TRIMMEAN` takes a total proportion; `PERCENTILE` interpolates linearly; `STDEV` is the sample SD ($n-1$).
6. **Robust standard errors are a different topic.** The median's sampling error is not $s/\sqrt n$; use the bootstrap ([lesson 17](../17-bootstrapping-and-confidence-intervals/theory.md)).

## Related notes

- [Percentiles and extreme values](../03-percentiles-and-extreme-values/theory.md)
- [Outlier detection](../04-outlier-detection/theory.md)
- [Descriptive statistics](../../notes/foundations/descriptive_statistics.md)
"""

TASK = r"""
# Task: robust statistics

## Scenario

A cold room storing vaccines has two independent digital thermometers, **A** and **B**, logging every 10 minutes for two days. Quality
assurance wants one number for the room's temperature and one for its variability, to set alarm limits. The first report from sensor A
says the temperature is "about 23 C with a standard deviation of 14 C" - nobody believes this, since the compressor holds the room near
21-22 C. You must decide which statistics to trust and how much the answer depends on a few readings.

## Data

`data.csv` - 288 rows (12 Jan 2026 00:00 to 13 Jan 2026 23:50), one row per 10-minute reading.

| column | meaning |
|---|---|
| `timestamp` | time of the reading |
| `temp_a_c` | sensor A, degrees Celsius |
| `temp_b_c` | sensor B, degrees Celsius (same room) |

## Questions

Work in a spreadsheet (import `data.csv`), then compare with `solution.xlsx`. `STDEV` is the sample SD; `TRIMMEAN(range, 0.1)` removes 10 % in total.

1. Compute mean and SD of both sensors. Do they agree?
2. Compute the median, the 10 % trimmed mean and the 5 % winsorised mean (clip to P5/P95, then average) of both sensors.
3. Compute IQR, IQR/1.349, MAD and 1.4826 x MAD of both sensors and compare with the SD.
4. How many readings of A are further than 10 robust SDs (1.4826 x MAD) from the median? What values do they have? What is the mean of A without them, and how far is it from B's mean?
5. Add *one* extra reading X to sensor B for X = 22, 30, 85, 500, 5000. How do the mean and the median change?
6. Overwrite the first k readings of B with 85.0 for k = 14, 29, 58, 100, 150. For each k compute mean, trimmed mean, winsorised mean and median. At what share of corrupted data does each estimator break?
7. Compute 3-sigma alarm limits for sensor A (a) as mean $\pm$ 3 SD and (b) as median $\pm$ 3 x 1.4826 MAD. Which pair would flag a reading of 35 C?
8. *Explain in three sentences* when a robust estimate would be the wrong choice and one weakness of robust estimators on clean data.

## Grafana

Import `grafana/dashboard.json` (no data-source setup is needed).

- In "Raw readings, sensor A vs sensor B", where do the mean and median of A sit relative to the bulk of the data?
- In "Three estimates of the spread", which estimates of A and B agree and which do not?
- In "Breakdown curves", read off the share of corrupted readings at which each line leaves the horizontal.

## Deliverable

A short note (6-10 lines) titled *Which numbers go on the QA report?* with three named parts: **What was wrong** (the evidence in
sensor A), **Recommended estimates** (centre and spread, with values) and **Limits** (when these estimates stop being reliable).
Include one chart.
"""
