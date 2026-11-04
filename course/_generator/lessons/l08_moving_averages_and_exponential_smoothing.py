"""Lesson 08 - Moving averages and exponential smoothing (lag vs smoothness)."""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import Book, Dash, md, write_csv  # noqa: E402

SLUG = "08-moving-averages-and-exponential-smoothing"
TITLE = "Moving averages and exponential smoothing"
MODULE = "Understanding time series"
DATASET = "140 days of support tickets with a level shift after a product release"
N = 140
SHIFT = 84  # row index of the release (a Monday); hidden level shift of +28 tickets/day
W, A_FAST, A_SLOW, THR = 7, 0.3, 0.1, 215
GRID = [0.05, 0.1, 0.2, 0.3, 0.5, 0.7, 0.9]
START = 21  # first row index at which every smoother (incl. 21-day SMA) is defined


def make_data() -> pd.DataFrame:
    rng = np.random.default_rng(808)
    t = np.arange(N)
    wk = np.array([8, 6, 3, 0, -2, -8, -7], dtype=float)
    wk -= wk.mean()
    level = np.where(t >= SHIFT, 228.0, 200.0)
    x = level + wk[t % 7] + rng.normal(0, 16, N)
    return pd.DataFrame({"date": pd.date_range("2026-02-02", periods=N, freq="D"), "tickets": x.round(0).astype(int)})


def ewma(x, a):
    out = [float(x[0])]
    for v in x[1:]:
        out.append(a * float(v) + (1 - a) * out[-1])
    return np.array(out)


def fill(text: str, **kw) -> str:
    for k, v in kw.items():
        text = text.replace(f"@{k}@", str(v))
    return text


def build(out: Path) -> Book:
    df = make_data()
    write_csv(out, df)
    x = df["tickets"].astype(float)
    release = df["date"].iloc[SHIFT]
    S = {"raw": x.to_numpy(), "sma_w": x.rolling(W).mean().to_numpy(), "sma21": x.rolling(21).mean().to_numpy(),
         "cma7": x.rolling(7, center=True).mean().to_numpy(), "ewma_fast": ewma(x, A_FAST), "ewma_slow": ewma(x, A_SLOW)}
    flags = {k: np.nan_to_num(v > THR, nan=0).astype(int) * 1 for k, v in S.items()}
    for k in ("sma_w", "sma21", "cma7"):  # NaN > thr is False already; make explicit
        flags[k] = np.where(np.isnan(S[k]), 0, S[k] > THR).astype(int)
    delay = {k: int(np.argmax(f[SHIFT:])) if f[SHIFT:].any() else np.nan for k, f in flags.items()}
    false_alarms = {k: int(f[:SHIFT].sum()) for k, f in flags.items()}
    noise = {k: float(np.std(v[START:SHIFT], ddof=1)) for k, v in S.items()}
    grid = {a: ewma(x, a) for a in GRID}
    rmse = {a: float(np.sqrt(np.mean((x.to_numpy()[1:] - g[:-1]) ** 2))) for a, g in grid.items()}
    best_a = min(rmse, key=rmse.get)

    # ------------------------------------------------------------------ workbook
    b = Book(df, "Lesson 08 - Moving averages and exponential smoothing",
             "Yellow cells are assumptions: change the window, the alphas, the alert threshold or the release date.")
    b.section("0. Settings")
    w = b.row("SMA window w (days)", W, None, "0", "trailing average of the last w days", is_input=True)
    af = b.row("alpha, fast EWMA", A_FAST, None, "0.00", is_input=True)
    asl = b.row("alpha, slow EWMA", A_SLOW, None, "0.00", is_input=True)
    thr = b.row("Alert threshold (tickets/day)", THR, None, "0", "a smoothed value above this raises an alert", is_input=True)
    rel = b.row("Release date", release.to_pydatetime(), None, "yyyy-mm-dd", "known from the release calendar", is_input=True)
    n = b.n
    B_ = f"Data!$B$2:$B${n + 1}"

    wl = w

    def sma_formula(r):
        return f'=IF(ROW()-1<{wl},"",AVERAGE(OFFSET(B{r},-({wl}-1),0,{wl},1)))'

    b.add_column("sma_w", sma_formula, expected=S["sma_w"], fmt="0.0")
    for r in range(2, n + 2):  # make the column robust when w is changed: formula in every row
        if b.data.cell(row=r, column=3).value is None:
            b.data.cell(row=r, column=3, value=sma_formula(r)).number_format = "0.0"
    b.add_column("sma21", lambda r: f"=AVERAGE(B{r - 20}:B{r})", expected=S["sma21"], fmt="0.0")
    b.add_column("cma7", lambda r: f"=AVERAGE(B{r - 3}:B{r + 3})", expected=S["cma7"], fmt="0.0")
    # column letters: A date, B tickets, C sma_w, D sma21, E cma7, F ewma_fast, G ewma_slow
    b.add_column("ewma_fast", lambda r: f"=B{r}" if r == 2 else f"={af}*B{r}+(1-{af})*F{r - 1}",
                 expected=S["ewma_fast"], fmt="0.0")
    b.add_column("ewma_slow", lambda r: f"=B{r}" if r == 2 else f"={asl}*B{r}+(1-{asl})*G{r - 1}",
                 expected=S["ewma_slow"], fmt="0.0")
    thr_l = thr
    names = ["raw", "sma_w", "sma21", "cma7", "ewma_fast", "ewma_slow"]
    cols = {"raw": "B", "sma_w": "C", "sma21": "D", "cma7": "E", "ewma_fast": "F", "ewma_slow": "G"}
    for k in names:
        L = cols[k]
        if k == "raw":
            fn = lambda r, L=L: f"=IF({L}{r}>{thr_l},1,0)"
        else:
            fn = lambda r, L=L: f"=IF(ISNUMBER({L}{r}),IF({L}{r}>{thr_l},1,0),0)"
        b.add_column(f"alert_{k}", fn, expected=flags[k], fmt="0")
    flagcol = {k: b.col(f"alert_{k}") for k in names}
    # alpha grid for one-step forecasts
    gcol = {}
    for a in GRID:
        nm = f"ewma_a{int(a * 100):02d}"
        L = b.add_column(nm, lambda r, a=a: None, expected=None, fmt="0.0")
        gcol[a] = L
        for r in range(2, n + 2):
            b.data.cell(row=r, column=b.data.max_column, value=(f"=B{r}" if r == 2 else f"={a}*B{r}+(1-{a})*{L}{r - 1}")
                        ).number_format = "0.0"
        for r in range(2, n + 2):
            b.checks.append((f"Data!{L}{r}", f"{nm} row {r}", float(grid[a][r - 2])))

    b.section("1. Smoothness: noise left in each series before the release")
    rel_idx = b.row("Release row index (days after the first date)", f"={rel}-Data!$A$2", SHIFT, "0")
    ri = b.local(rel_idx)
    rows, exp = [], {}
    labels = {"raw": "raw tickets", "sma_w": "SMA(w) trailing", "sma21": "SMA 21 trailing", "cma7": "centred MA 7",
              "ewma_fast": "EWMA fast", "ewma_slow": "EWMA slow"}
    r_tab = b.next_row
    for i, k in enumerate(names):
        L, FL = cols[k], flagcol[k]
        seg = f"OFFSET(Data!${L}$2,{START},0,{ri}-{START},1)"
        rows.append([labels[k], f"=STDEV({seg})",
                     f"=SUM(OFFSET(Data!${FL}$2,0,0,{ri},1))",
                     f"=MATCH(1,OFFSET(Data!${FL}$2,{ri},0,{n}-{ri},1),0)-1",
                     f"=INDEX(Data!$A$2:$A${n + 1},{ri}+D{r_tab + 1 + i}+1)"])
        exp[(i, 1)] = noise[k]
        exp[(i, 2)] = false_alarms[k]
        exp[(i, 3)] = delay[k]
    t0, t1 = b.table(["Series", "Noise SD before release", "Alerts before release", "Days until alert after release",
                      "Alert date"], rows, fmt={1: "0.00", 2: "0", 3: "0", 4: "yyyy-mm-dd"}, expect=exp)
    assert t0 == r_tab + 1
    b.bar_chart_from_table("Noise SD before release (tickets/day)", 1, [2], t0, t1, anchor="H4", y_title="tickets/day")
    b.bar_chart_from_table("Days until the alert after the release", 1, [4], t0, t1, anchor="H22", y_title="days")

    b.section("2. Last values and equivalence of window and alpha")
    last = n + 1
    b.row("SMA(w) on the last day", f"=Data!C{last}", S["sma_w"][-1], "0.0")
    b.row("EWMA fast on the last day", f"=Data!F{last}", S["ewma_fast"][-1], "0.0")
    b.row("EWMA slow on the last day", f"=Data!G{last}", S["ewma_slow"][-1], "0.0")
    b.row("Average age of data in SMA(w) (days)", f"=({wl}-1)/2", (W - 1) / 2, "0.0", "(w-1)/2")
    b.row("Average age of data in fast EWMA (days)", f"=(1-{af})/{af}", (1 - A_FAST) / A_FAST, "0.00", "(1-alpha)/alpha")
    b.row("alpha giving the same average age as SMA(w)", f"=2/({wl}+1)", 2 / (W + 1), "0.000", "alpha = 2/(w+1)")
    b.row("Noise variance factor of SMA(w), independent noise", f"=1/{wl}", 1 / W, "0.000", "1/w")
    b.row("Noise variance factor of fast EWMA", f"={af}/(2-{af})", A_FAST / (2 - A_FAST), "0.000", "alpha/(2-alpha)")

    b.section("3. Choosing alpha: one-step-ahead forecast error over the whole series")
    rows, exp = [], {}
    g0 = b.next_row + 1
    for i, a in enumerate(GRID):
        L = gcol[a]
        rows.append([a, f"=SQRT(SUMXMY2(Data!$B$3:$B${n + 1},Data!${L}$2:${L}${n}) / ({n}-1))"])
        exp[(i, 1)] = rmse[a]
    g_first, g_last = b.table(["alpha", "RMSE of one-step forecast"], rows, fmt={0: "0.00", 1: "0.00"}, expect=exp)
    best = b.row("alpha with the smallest RMSE", f"=INDEX(A{g_first}:A{g_last},MATCH(MIN(B{g_first}:B{g_last}),B{g_first}:B{g_last},0))",
                 best_a, "0.00")
    b.bar_chart_from_table("One-step forecast RMSE by alpha", 1, [2], g_first, g_last, anchor="H40", y_title="tickets")
    b.line_chart("Tickets and smoothers", "date", ["tickets", "sma_w", "cma7", "ewma_fast", "ewma_slow"], anchor="P4",
                 y_title="tickets/day")

    tab = lambda k: t0 + names.index(k)
    b.answers([
        ("SMA(7): value on the last day, rows lost, average age of the data", f"=Data!C{last}",
         f"{S['sma_w'][-1]:.1f} tickets; the first {W - 1} rows have no value and the average observation in the window is "
         f"{(W - 1) / 2:.0f} days old."),
        ("Centred 7-day MA vs trailing 7-day MA around the release", f"=Analysis!D{tab('cma7')}",
         f"First alert {delay['cma7']} day(s) after the release for the centred MA vs {delay['sma_w']} for the trailing SMA; the centred "
         f"average already contains post-release days, so it shows {false_alarms['cma7']} alert(s) *before* the release - it uses the future "
         f"and cannot run in real time."),
        ("EWMA values (alpha 0.3 and 0.1) on the last day; alpha equal in average age to SMA(7)", f"=Data!F{last}",
         f"{S['ewma_fast'][-1]:.1f} and {S['ewma_slow'][-1]:.1f}; alpha = 2/(7+1) = {2 / 8:.2f} matches the average age of SMA(7)."),
        ("Noise SD before the release for every series", f"=Analysis!B{tab('raw')}",
         f"Raw {noise['raw']:.1f}; SMA7 {noise['sma_w']:.1f}; SMA21 {noise['sma21']:.1f}; EWMA 0.3 {noise['ewma_fast']:.1f}; EWMA 0.1 "
         f"{noise['ewma_slow']:.1f}. SMA7 does better than EWMA 0.3 partly because its window is exactly one weekly cycle and cancels the weekday pattern."),
        (f"Alerts before and delay after the release at threshold {THR}", f"=Analysis!C{tab('raw')}",
         f"Raw data: {false_alarms['raw']} false alerts before the release. Delays (days): SMA7 {delay['sma_w']}, SMA21 {delay['sma21']}, "
         f"EWMA 0.3 {delay['ewma_fast']}, EWMA 0.1 {delay['ewma_slow']}; false alerts before release: "
         f"{false_alarms['sma_w']}, {false_alarms['sma21']}, {false_alarms['ewma_fast']}, {false_alarms['ewma_slow']}."),
        ("alpha that minimises the one-step RMSE", f"={best}",
         f"alpha = {best_a} (RMSE {rmse[best_a]:.2f}); the alpha grid curve is shallow near the minimum. Minimum forecast error "
         f"and fast detection are different goals."),
        ("What happens to delay and noise if the window grows to 21?", f"=Analysis!D{tab('sma21')}",
         f"SMA21 noise falls to {noise['sma21']:.1f} but the alert comes {delay['sma21']} days after the release instead of {delay['sma_w']}."),
        ("Interpretation: trade-off, real-time use, startup", "see note",
         "Smoother means later: noise variance and lag move in opposite directions for every smoother in this lesson. A centred "
         "average cannot be computed on today's data. EWMA starts from the first observation, so its first days are biased."),
    ])

    # ------------------------------------------------------------------- grafana
    d = Dash("stats-08-smoothing", "08 · Moving averages and exponential smoothing",
             "Smoother = later: detection delay, noise left and weights on the past for SMA and EWMA.",
             df.rename(columns={"date": "time"}), "time")
    d.stat("Days from release to alert (threshold %d)" % THR,
           {"SMA 7": delay["sma_w"], "SMA 21": delay["sma21"], "centred MA 7": delay["cma7"],
            "EWMA 0.3": delay["ewma_fast"], "EWMA 0.1": delay["ewma_slow"], "raw: false alerts before": false_alarms["raw"]},
           "Smoothers need days to react after the release; raw data alerts at once but also fires before the release.",
           decimals=0, thresholds=[(None, "green"), (5, "orange"), (9, "red")])
    ts = pd.DataFrame({"time": df["date"], "raw tickets": x, "SMA 7": S["sma_w"], "EWMA 0.3": S["ewma_fast"],
                       "EWMA 0.1": S["ewma_slow"], "alert threshold": THR})
    d.timeseries("Tickets per day and three smoothers", ts, "The step is around the release date; every smoother follows it later "
                 "than the raw series, EWMA 0.1 the latest.", dashed=["alert threshold"], h=10, w=24,
                 colors={"raw tickets": "#B8C0CC", "SMA 7": "#4E79A7", "EWMA 0.3": "#F28E2B", "EWMA 0.1": "#59A14F",
                         "alert threshold": "#E15759"})
    cmp_ = pd.DataFrame({"time": df["date"], "SMA 7 (trailing)": S["sma_w"], "centred MA 7": S["cma7"]})
    d.timeseries("Trailing vs centred 7-day average", cmp_, "The centred average is shifted 3 days earlier because it uses future data.",
                 colors={"SMA 7 (trailing)": "#4E79A7", "centred MA 7": "#B07AA1"}, w=12)
    sm = pd.DataFrame({"series": ["raw", "SMA 7", "SMA 21", "centred 7", "EWMA 0.3", "EWMA 0.1"],
                       "noise SD before release": [round(noise[k], 2) for k in names],
                       "days to alert": [delay[k] for k in names]})
    d.bars("Noise left vs days to alert", sm, "Lower noise comes with a longer delay.", w=12)
    ages = np.arange(0, 15)
    wt = pd.DataFrame({"age (days)": [f"age {a}" for a in ages], "SMA 7": np.where(ages < 7, 1 / 7, 0).round(3),
                       "EWMA 0.3": (0.3 * 0.7 ** ages).round(3), "EWMA 0.1": (0.1 * 0.9 ** ages).round(3)})
    d.bars("Weights on past observations", wt, "How much each past day contributes today: a rectangle vs geometric tails.", w=12)
    rm = pd.DataFrame({"alpha": [f"alpha {a:.2f}" for a in GRID],
                       "RMSE above the best alpha (%)": [round(100 * (rmse[a] / rmse[best_a] - 1), 1) for a in GRID]})
    d.bars("One-step forecast error by alpha", rm, "How much worse than the best alpha (%, RMSE of tomorrow's forecast = today's EWMA). "
           "The optimum is flat, and the best alpha for forecasting is not the best for alerting.", w=12)
    d.save(out)

    # ------------------------------------------------------------------ markdown
    xs = df["tickets"].iloc[:5].tolist()
    e = [float(xs[0])]
    for v in xs[1:]:
        e.append(0.3 * v + 0.7 * e[-1])
    ex = dict(x=", ".join(map(str, xs)), e=", ".join(f"{v:.2f}" for v in e), s3=f"{np.mean(xs[1:4]):.2f}",
              s3d=df["date"].iloc[3].strftime("%Y-%m-%d"), sd=f"{delay['sma_w']}", cd=f"{delay['cma7']}", ed=f"{delay['ewma_fast']}",
              sl=f"{delay['ewma_slow']}", nr=f"{noise['raw']:.1f}", ns=f"{noise['sma_w']:.1f}", ne=f"{noise['ewma_fast']:.1f}",
              nsl=f"{noise['ewma_slow']:.1f}", ba=best_a, sd7=f"{np.sqrt(1 / 7):.3f}", se=f"{np.sqrt(0.3 / 1.7):.3f}",
              ea=f"{0.3 / 1.7:.3f}", se25=f"{np.sqrt(0.25 / 1.75):.3f}", rs=f"{noise['sma21']:.1f}", d21=delay["sma21"],
              fa=false_alarms["raw"])
    md(out / "theory.md", fill(THEORY, thr=THR, **ex))
    md(out / "task.md", fill(TASK, thr=THR, first=df["date"].iloc[0].strftime("%Y-%m-%d"),
                             last=df["date"].iloc[-1].strftime("%Y-%m-%d"), rel=release.strftime("%Y-%m-%d")))
    return b


THEORY = r"""
# Theory: moving averages and exponential smoothing

## Why smooth, and what it costs

A noisy daily number hides its own level: yesterday's 231 tickets could be a real jump or an ordinary bad day. Averaging
neighbouring values cancels noise, so the level becomes visible. But an average of *past* values describes where the
level **was**, not where it is. Every smoother therefore buys smoothness with **lag**, and there is no setting that gives
both. Choosing a window (or alpha) is choosing a point on that trade-off for a purpose: alerting, reporting or forecasting.

## Simple moving average (SMA)

The trailing SMA of window $w$ gives equal weight $1/w$ to the last $w$ observations:

$$
\mathrm{SMA}_t = \frac{1}{w}\sum_{j=0}^{w-1} x_{t-j}.
$$

- The first $w-1$ days have no value (no full window).
- The *average age* of the data inside is $(w-1)/2$ days: after a step change the SMA needs about that long to reach the
  middle of the step, and $w$ days to finish it.
- The **centred** MA $\frac{1}{w}\sum_{j=-(w-1)/2}^{(w-1)/2} x_{t+j}$ has no lag but uses *future* values: it is a tool
  for describing history, never for a live alert.
- If $w$ equals the seasonal period (7 for weekly data) the seasonal pattern cancels exactly
  ([lesson 07](../07-trend-seasonality-and-noise/theory.md)); other widths leave a ripple.

## Exponentially weighted moving average (EWMA)

$$
s_t = \alpha x_t + (1-\alpha)\,s_{t-1}, \qquad s_1 = x_1, \qquad 0<\alpha\le 1.
$$

Unrolling the recursion shows the weights: $s_t = \sum_{j\ge 0}\alpha(1-\alpha)^j x_{t-j}$ (plus a weight on the starting
value). Recent days count most, old days never drop out abruptly, and only one number has to be stored.

- **Average age** of the data: $(1-\alpha)/\alpha$ days.
- **Matching an SMA:** equal average age gives $\alpha = 2/(w+1)$ (for $w=7$: $\alpha = 0.25$).
- **Noise reduction** for independent noise, as a variance factor: SMA $1/w$, EWMA $\alpha/(2-\alpha)$. For $w=7$ that is
  $1/7 = 0.143$ and for $\alpha = 0.3$ it is @ea@, i.e. the noise SD shrinks to @sd7@ (SMA) and @se@ (EWMA 0.3) of its raw
  value; the matching $\alpha = 0.25$ gives @se25@, the same as the SMA.
- **Start-up:** $s_1 = x_1$ inherits that day's noise, which decays like $(1-\alpha)^t$. Skip the first few days or start
  from the mean of a baseline.

### Worked example (first days of `data.csv`)

Tickets on the first five days are @x@. EWMA with $\alpha=0.3$: $s_1 = x_1$, then $s_2 = 0.3x_2 + 0.7s_1$, and so on:
$s$ = @e@. The trailing 3-day SMA for @s3d@ (days 2-4) is @s3@.

## Choosing alpha (or the window)

- **For forecasting:** a one-step forecast of tomorrow is today's $s_t$. Pick $\alpha$ that minimises
  $\sqrt{\tfrac1{n-1}\sum (x_{t+1}-s_t)^2}$. In `data.csv` the best of the grid is $\alpha = @ba@$, and the curve is flat
  around it, so the choice is not critical.
- **For monitoring:** decide how many days of delay you can accept for a real change and how many false alerts you can
  tolerate; large $\alpha$ (short window) detects faster and alerts falsely more often.
- **For reporting:** use a window equal to the natural cycle (a week, a month).

In `data.csv` with an alert level of @thr@ tickets: the raw series alerts @fa@ times before the release; the first alert after the release comes, counted in days
from the release, after @sd@ (trailing SMA7), @cd@ (centred MA), @ed@ (EWMA 0.3), @sl@ (EWMA 0.1) and @d21@ (SMA 21). Noise SD
before the release: raw @nr@, SMA7 @ns@, EWMA 0.3 @ne@, EWMA 0.1 @nsl@.

## Assumptions and pitfalls

1. **A smoother estimates a local level**; with a trend a trailing average lags the line by its average age, and with a
   step it blurs the edge. Do not read the date of a change off a smoothed curve; read it off the raw data or use a
   change-point method ([lesson 27](../27-change-point-detection/theory.md)).
2. **Centred averages leak the future.** Back-testing a rule on a centred MA overstates what was possible in real time.
3. **Window not matching the cycle** leaves a periodic ripple: EWMA 0.3 still shows part of the weekly pattern.
4. **Outliers** enter an SMA with weight $1/w$ for $w$ days, and an EWMA with weight $\alpha$ and a long tail.
   Consider a rolling median ([lesson 10](../10-rolling-statistics/theory.md)).
5. **Missing days or uneven spacing** break both definitions; resample first
   ([lesson 06](../06-time-aggregation-and-sampling-frequency/theory.md)).
6. **A smoothed series is autocorrelated by construction**; correlations and tests computed on it are misleading.

## Where this leads

Rolling windows beyond the mean are in [lesson 10](../10-rolling-statistics/theory.md). EWMA is the engine of simple
exponential smoothing and of EWMA control charts ([lesson 23](../23-exponential-smoothing-models/theory.md),
[lesson 26](../26-statistical-process-control/theory.md)). Background:
[time series](../../notes/time_series/time_series.md), [moving average models](../../notes/time_series/moving_average_models.md)
(different object: MA *processes* model noise, they do not smooth data).
"""

TASK = r"""
# Task: moving averages and exponential smoothing

## Scenario

You lead customer support analytics. Product shipped a pricing-page release on **@rel@** and asked you to set up an
alert that fires when daily ticket volume rises above **@thr@ tickets** *on a smoothed basis*: the raw daily number is too
noisy to alert on. You must choose a smoother and show the trade-off to the on-call manager: how quickly does each
option fire after a real change, and how often does it fire when nothing happened?

## Data

`data.csv` - 140 consecutive days from @first@ (a Monday) to @last@; one row = one day.

| column | meaning |
|---|---|
| `date` | calendar day |
| `tickets` | new support tickets opened that day (count) |

## Questions

Work in a spreadsheet (import `data.csv`), then compare with `solution.xlsx`.

1. Compute a **trailing 7-day SMA**. What is its value on the last day, how many rows are empty, and how old (on average,
   in days) is the data inside the window?
2. Compute a **centred 7-day MA** as well. On which rows is it defined, and how does its timing compare with the trailing
   SMA around the release date?
3. Compute **EWMA** with alpha = 0.3 (fast) and alpha = 0.1 (slow), starting from the first observation. What are the last
   values, and which alpha has the same average age as a 7-day SMA?
4. For each series (raw, SMA 7, SMA 21, centred MA 7, EWMA fast, EWMA slow) compute the **standard deviation over days 22 to the
   release** (before the release). How much noise does each one remove? Which smoother removes more than its alpha/window
   suggests, and why?
5. Create alert flags (smoothed value > @thr@). For each series count the alerts **before** the release and find how many days after
   it the first alert occurs.
6. Compute a one-step forecast RMSE (forecast for day t+1 = EWMA at day t) for alpha = 0.05, 0.1, 0.2, 0.3, 0.5, 0.7, 0.9.
   Which alpha is best?
7. Change the window input to 21. What happens to noise and delay?
8. *Interpretation:* which smoother would you deploy for the alert, and why can the centred MA not be used?

## Grafana

Import `grafana/dashboard.json` (see `../grafana/README.md`; no data-source setup is needed).

- In "Tickets per day and three smoothers", where do the curves cross the threshold relative to each other? Which one is last?
- In "Weights on past observations", why does the EWMA 0.1 bar series reach so far back, and what does that mean for its delay?
- In "Noise left vs days to alert", is there any series that is both quick and smooth?

## Deliverable

A note (6-8 lines) for the on-call manager with named parts: **Recommendation** (smoother and parameter), **Evidence** (delay
and false alerts of at least three options), **Trade-off** (what you give up) and **Caveat** (one limitation, e.g. a single
release, weekday pattern, start-up).
"""
