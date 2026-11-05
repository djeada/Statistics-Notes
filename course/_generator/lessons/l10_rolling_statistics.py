"""Lesson 10 - Rolling statistics (rolling mean/SD/min/max/percentile, window choice, rolling z-score, edge effects)."""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import Book, Dash, md, write_csv  # noqa: E402

SLUG = "10-rolling-statistics"
TITLE = "Rolling statistics"
MODULE = "Understanding time series"
DATASET = "180 days of average payment-processing time (ms) with a volatile period and three spike days"
N = 180
W, PCTL, ZTHR = 14, 0.9, 3
SPIKES = (40, 105, 150)  # +30 ms each: the same size, very different meaning in calm and in volatile weeks
VOL = (80, 130)  # days with 14 ms noise instead of 5 ms; the mean does not change


def make_data() -> pd.DataFrame:
    rng = np.random.default_rng(1023)
    t = np.arange(N)
    sd = np.where((t >= VOL[0]) & (t < VOL[1]), 14.0, 5.0)
    x = 120 + 0.05 * t + rng.normal(0, 1, N) * sd
    for d in SPIKES:
        x[d] += 30
    return pd.DataFrame({"date": pd.date_range("2026-02-02", periods=N, freq="D"), "payment_ms": x.round(1)})


def fill(text: str, **kw) -> str:
    for k, v in kw.items():
        text = text.replace(f"@{k}@", str(v))
    return text


def prior_z(x: pd.Series, w: int) -> pd.Series:
    m, s = x.shift(1).rolling(w).mean(), x.shift(1).rolling(w).std()
    return (x - m) / s


def build(out: Path) -> Book:
    df = make_data()
    write_csv(out, df)
    n = len(df)
    x = df["payment_ms"]
    rm, rs = x.rolling(W).mean(), x.rolling(W).std()
    rmin, rmax, rq = x.rolling(W).min(), x.rolling(W).max(), x.rolling(W).quantile(PCTL)
    sd7, sd28 = x.rolling(7).std(), x.rolling(28).std()
    z14, z28 = prior_z(x, 14), prior_z(x, 28)
    zg = (x - x.mean()) / x.std()
    zi = (x - rm) / rs
    nflag = lambda z: int((z.abs() > ZTHR).sum())
    last = n + 1

    # ------------------------------------------------------------------ workbook
    b = Book(df, "Lesson 10 - Rolling statistics",
             "Yellow cells are assumptions: window length, percentile and z-score threshold.")
    b.section("0. Settings")
    w = b.row("Window length w (days)", W, None, "0", "rolling statistics use the last w days including today", is_input=True)
    pc = b.row("Rolling percentile", PCTL, None, "0.00", is_input=True)
    zt = b.row("Alert threshold |z|", ZTHR, None, "0.0", is_input=True)

    def roll(fn):
        return lambda r: f'=IF(ROW()-1<{w},"",{fn}(OFFSET(B{r},-({w}-1),0,{w},1)))'

    specs = [("roll_mean", roll("AVERAGE"), rm), ("roll_sd", roll("STDEV"), rs), ("roll_min", roll("MIN"), rmin),
             ("roll_max", roll("MAX"), rmax),
             ("roll_pctl", lambda r: f'=IF(ROW()-1<{w},"",PERCENTILE(OFFSET(B{r},-({w}-1),0,{w},1),{pc}))', rq)]
    for nm, fn, ex in specs:
        L = b.add_column(nm, fn, expected=ex, fmt="0.00")
        col = list(b._cols).index(nm) + 1
        for r in range(2, n + 2):  # formula in every row so changing w keeps working
            if b.data.cell(row=r, column=col).value is None:
                b.data.cell(row=r, column=col, value=fn(r)).number_format = "0.00"
    # C roll_mean D roll_sd E roll_min F roll_max G roll_pctl
    b.add_column("sd_7", lambda r: f"=STDEV(B{r - 6}:B{r})", expected=sd7, fmt="0.00")
    b.add_column("sd_28", lambda r: f"=STDEV(B{r - 27}:B{r})", expected=sd28, fmt="0.00")
    b.add_column("z_prior14", lambda r: f"=(B{r}-AVERAGE(B{r - 14}:B{r - 1}))/STDEV(B{r - 14}:B{r - 1})", expected=z14, fmt="0.00")
    b.add_column("z_prior28", lambda r: f"=(B{r}-AVERAGE(B{r - 28}:B{r - 1}))/STDEV(B{r - 28}:B{r - 1})", expected=z28, fmt="0.00")
    b.add_column("z_global", lambda r: f"=(B{r}-AVERAGE($B$2:$B${last}))/STDEV($B$2:$B${last})", expected=zg, fmt="0.00")
    b.add_column("z_incl_w", lambda r: f'=IF(ISNUMBER(D{r}),(B{r}-C{r})/D{r},"")', expected=zi, fmt="0.00")
    # H sd_7 I sd_28 J z_prior14 K z_prior28 L z_global M z_incl_w
    rng_ = lambda L: f"Data!${L}$2:${L}${last}"
    DT = rng_("A")

    b.section("1. Rolling statistics on the last day")
    b.row("Rolling mean (ms)", f"=Data!C{last}", rm.iloc[-1], "0.00")
    b.row("Rolling standard deviation (ms)", f"=Data!D{last}", rs.iloc[-1], "0.00")
    b.row("Rolling minimum (ms)", f"=Data!E{last}", rmin.iloc[-1], "0.00")
    b.row("Rolling maximum (ms)", f"=Data!F{last}", rmax.iloc[-1], "0.00")
    b.row("Rolling percentile (ms)", f"=Data!G{last}", rq.iloc[-1], "0.00", "PERCENTILE, linear interpolation")

    b.section("2. Edge effect")
    b.row("Days with a rolling value", f"=COUNT({rng_('C')})", int(rm.notna().sum()), "0")
    b.row("Days lost at the start", f"=ROWS({rng_('C')})-COUNT({rng_('C')})", int(rm.isna().sum()), "0", "w - 1")
    b.row("First date with a rolling value", f"=INDEX({DT},{b.local(w)})", None, "yyyy-mm-dd")

    b.section("3. Window length and volatility: largest and smallest rolling SD")
    t_first = b.next_row + 1
    rows, exp = [], {}
    for i, (lab, L, s) in enumerate([("7 days", "H", sd7), ("w days (setting)", "D", rs), ("28 days", "I", sd28)]):
        rr = rng_(L)
        rows.append([lab, f"=MAX({rr})", f"=MIN({rr})", f"=B{t_first + i}/C{t_first + i}", f"=INDEX({DT},MATCH(MAX({rr}),{rr},0))"])
        exp.update({(i, 1): s.max(), (i, 2): s.min(), (i, 3): s.max() / s.min()})
    v0, v1 = b.table(["Window", "Largest rolling SD", "Smallest rolling SD", "Ratio", "Date of the largest"], rows,
                     fmt={1: "0.00", 2: "0.00", 3: "0.0", 4: "yyyy-mm-dd"}, expect=exp)
    b.bar_chart_from_table("Largest vs smallest rolling SD by window", 1, [2, 3], v0, v1, anchor="H4", y_title="ms")

    b.section("4. Rolling z-score alerts")
    zz = {}
    for lab, L, z in [("z against the previous 14 days", "J", z14), ("z against the previous 28 days", "K", z28),
                      ("z against the whole series (global)", "L", zg), ("z with today inside its own w-day window", "M", zi)]:
        rr = rng_(L)
        zz[L] = b.row(f"Days with |z| > threshold, {lab}", f'=COUNTIF({rr},">"&{b.local(zt)})+COUNTIF({rr},"<"&-{b.local(zt)})',
                      nflag(z), "0")
    b.row("Largest possible z when today is inside its own window: (w-1)/SQRT(w)", f"=({b.local(w)}-1)/SQRT({b.local(w)})",
          (W - 1) / np.sqrt(W), "0.00", "Samuelson's bound: no point can exceed it")

    b.section("5. The three days with the largest previous-14-day z-score")
    top = z14.nlargest(3)
    s0 = b.next_row + 1
    rows, exp = [], {}
    for k, (i, v) in enumerate(top.items()):
        rr = rng_("J")
        pos = f"MATCH(B{s0 + k},{rr},0)"
        rows.append([k + 1, f"=LARGE({rr},{k + 1})", f"=INDEX({DT},{pos})", f"=INDEX({rng_('B')},{pos})",
                     f"=INDEX({rng_('K')},{pos})", f"=INDEX({rng_('L')},{pos})", f"=INDEX({rng_('M')},{pos})"])
        exp.update({(k, 1): v, (k, 3): x.iloc[i], (k, 4): z28.iloc[i], (k, 5): zg.iloc[i], (k, 6): zi.iloc[i]})
    k0, k1 = b.table(["Rank", "z (previous 14 d)", "Date", "payment_ms", "z (previous 28 d)", "z (global)", "z (inside window)"], rows,
                     fmt={1: "0.00", 2: "yyyy-mm-dd", 3: "0.0", 4: "0.00", 5: "0.00", 6: "0.00"}, expect=exp)
    b.line_chart("Payment time, rolling mean and rolling maximum", "date", ["payment_ms", "roll_mean", "roll_max"], anchor="H22",
                 y_title="ms")
    b.line_chart("Rolling standard deviation (7, w and 28 days)", "date", ["sd_7", "roll_sd", "sd_28"], anchor="H40", y_title="ms")

    ratio14 = float(rs.max() / rs.min())
    vol_date = df["date"][int(rs.idxmax())]
    in_vol = lambda z: [i for i in z.index[z.abs() > ZTHR] if VOL[0] <= i < VOL[1]]
    gv = len(in_vol(zg))
    vol_dates = ", ".join(f"{df['date'][i]:%m-%d}" for i in in_vol(zg))
    flagged = lambda z: [f"{df['date'][i]:%m-%d}" for i in z.index[z.abs() > ZTHR]]
    b.answers([
        ("Rolling mean, SD, minimum, maximum and 90th percentile on the last day (w = 14)", f"=Data!C{last}",
         f"Mean {rm.iloc[-1]:.1f}, SD {rs.iloc[-1]:.1f}, min {rmin.iloc[-1]:.1f}, max {rmax.iloc[-1]:.1f}, P90 {rq.iloc[-1]:.1f} ms "
         f"(window = the last 14 days including the last one)."),
        ("How many days have no rolling value, and why?", f"=ROWS({rng_('C')})-COUNT({rng_('C')})",
         f"{W - 1} days: a trailing window of {W} needs {W} observations, so the first value appears on {df['date'][W - 1]:%Y-%m-%d}."),
        ("When is the rolling SD (w = 14) at its maximum and minimum?", f"=Analysis!B{v0 + 1}",
         f"Largest {rs.max():.1f} ms on {vol_date:%Y-%m-%d}, smallest {rs.min():.1f} ms: a {ratio14:.1f}-fold change in spread while the rolling mean "
         f"stays between {rm.min():.0f} and {rm.max():.0f}. The volatility changed, the level did not."),
        ("Compare windows of 7, 14 and 28 days (ratio largest/smallest SD)", f"=Analysis!D{v0}",
         f"Ratios 7 d: {sd7.max() / sd7.min():.1f}, 14 d: {ratio14:.1f}, 28 d: {sd28.max() / sd28.min():.1f}. Short windows react fast but are "
         f"noisy (their SD swings between {sd7.min():.1f} and {sd7.max():.1f}); long windows are steady but late and blurred."),
        ("Number of days with |z| > 3 against the whole series, the previous 14 days and the previous 28 days", f"={zz['L']}",
         f"Global: {nflag(zg)} days ({', '.join(flagged(zg))}); previous 14 d: {nflag(z14)} ({', '.join(flagged(z14))}); previous 28 d: "
         f"{nflag(z28)} ({', '.join(flagged(z28))}). The global rule flags {gv} day(s) of the volatile period ({vol_dates}) that are "
         f"ordinary there; the rolling rules flag the calm-period spikes and the first volatile day, when the window still holds calm data."),
        ("The three days with the largest previous-14-day z-score", f"=Analysis!B{k0}",
         "Days " + ", ".join(f"{df['date'][i]:%Y-%m-%d} (z = {v:.1f})" for i, v in top.items()) +
         f". The same +30 ms on {df['date'][SPIKES[1]]:%Y-%m-%d} (inside the volatile period) scores only z = {z14.iloc[SPIKES[1]]:.1f}."),
        ("z with the day inside its own window vs the previous window", f"=Analysis!G{k0}",
         f"With today in its own 14-day window the largest possible z is 13/sqrt(14) = {(W - 1) / np.sqrt(W):.2f}; the first spike scores "
         f"{zi.iloc[SPIKES[0]]:.2f} instead of {z14.iloc[SPIKES[0]]:.2f}. Compare against a window that excludes the candidate."),
        ("Interpretation: choice of window, edge effects, and what the flags mean", "see note",
         "A window is a bet about how fast the process changes: shorter = faster, noisier, and it forgets the spike quickly; "
         "longer = steadier, but it blends two regimes after a change. The first w-1 days and the days right after a change are the "
         "weakest. With 180 daily tests, a 3-sigma rule yields about one false alarm per 370 days by chance for normal data, more for "
         "heavy-tailed data, and a flag only says 'unusual versus the recent past', not 'broken'."),
    ])

    # ------------------------------------------------------------------- grafana
    d = Dash("stats-10-rolling", "10 · Rolling statistics",
             "Rolling mean, spread, envelope and z-score alerts on daily payment-processing time.",
             df.rename(columns={"date": "time"}), "time")
    d.stat("Alert counts (|z| > 3) and volatility", {"global z": nflag(zg), "rolling z, 14 d": nflag(z14), "rolling z, 28 d": nflag(z28),
                                                  "max / min rolling SD (14 d)": ratio14, "max possible z (w=14)": (W - 1) / np.sqrt(W)},
           "The same 180 days judged against the whole series or against the recent past.", decimals=1)
    pm, ps = x.shift(1).rolling(14).mean(), x.shift(1).rolling(14).std()
    up, lo = pm + ZTHR * ps, pm - ZTHR * ps
    flag = x.where(z14.abs() > ZTHR)
    flagg = x.where(zg.abs() > ZTHR)
    a = pd.DataFrame({"time": df["date"], "payment_ms": x, "upper band (previous 14 d, +3 SD)": up, "lower band": lo,
                      "rolling z flag": flag})
    d.timeseries("Payment time with rolling 3-SD band", a,
                 "The band is built from the previous 14 days only. It is narrow in calm weeks and wide in the volatile weeks.",
                 points=["rolling z flag"], dashed=["upper band (previous 14 d, +3 SD)", "lower band"], unit="ms", w=24, h=10,
                 colors={"payment_ms": "#9AA5B1", "upper band (previous 14 d, +3 SD)": "#4E79A7", "lower band": "#4E79A7", "rolling z flag": "#E15759"})
    g = pd.DataFrame({"time": df["date"], "payment_ms": x, "global flag": flagg, "global mean + 3 SD": x.mean() + 3 * x.std(),
                      "global mean - 3 SD": x.mean() - 3 * x.std()})
    d.timeseries("The same data judged by one global rule", g, "One fixed limit flags ordinary days of the volatile weeks and ignores that calm weeks have a much smaller normal range.",
                 points=["global flag"], dashed=["global mean + 3 SD", "global mean - 3 SD"], unit="ms",
                 colors={"payment_ms": "#9AA5B1", "global flag": "#F28E2B", "global mean + 3 SD": "#F28E2B", "global mean - 3 SD": "#F28E2B"})
    s = pd.DataFrame({"time": df["date"], "7 days": sd7, "14 days": rs, "28 days": sd28})
    d.timeseries("Rolling standard deviation by window length", s, "Short window: fast and jumpy. Long window: smooth and late.",
                 unit="ms", colors={"7 days": "#E15759", "14 days": "#4E79A7", "28 days": "#59A14F"})
    env = pd.DataFrame({"time": df["date"], "rolling max": rmax, "rolling P90": rq, "rolling mean": rm, "rolling min": rmin})
    d.timeseries("Rolling envelope (14 days): max, P90, mean, min", env, "Maximum and minimum are extreme-value statistics: very sensitive to a single day.",
                 unit="ms", colors={"rolling max": "#E15759", "rolling P90": "#F28E2B", "rolling mean": "#4E79A7", "rolling min": "#76B7B2"}, w=24, h=8)
    tb = pd.DataFrame({"date": [f"{df['date'][i]:%Y-%m-%d}" for i in top.index], "payment_ms": x[top.index].to_numpy(),
                       "z previous 14 d": z14[top.index].round(2).to_numpy(), "z previous 28 d": z28[top.index].round(2).to_numpy(),
                       "z global": zg[top.index].round(2).to_numpy(), "z inside window": zi[top.index].round(2).to_numpy()})
    d.table("Top three days by rolling z-score", tb, "Same data, different yardsticks.", w=24, h=5)
    d.save(out)

    # ------------------------------------------------------------------ markdown
    i0 = SPIKES[0]
    win = x.iloc[i0 - 14:i0]
    ex = dict(d0=f"{df['date'][i0]:%Y-%m-%d}", x0=f"{x.iloc[i0]:.1f}", m14=f"{win.mean():.2f}", s14=f"{win.std():.2f}",
              z0=f"{z14.iloc[i0]:.2f}", zi0=f"{zi.iloc[i0]:.2f}", mx=f"{(W - 1) / np.sqrt(W):.2f}", r7=f"{sd7.max() / sd7.min():.1f}",
              r28=f"{sd28.max() / sd28.min():.1f}", r14=f"{ratio14:.1f}", nz14=nflag(z14), nzg=nflag(zg), nz28=nflag(z28),
              dv=f"{df['date'][SPIKES[1]]:%Y-%m-%d}", zv=f"{z14.iloc[SPIKES[1]]:.1f}", zgv=f"{zg.iloc[SPIKES[1]]:.1f}",
              vs=f"{df['date'][VOL[0]]:%Y-%m-%d}", d80=f"{df['date'][VOL[0]]:%Y-%m-%d}", ve=f"{df['date'][VOL[1] - 1]:%Y-%m-%d}")
    md(out / "theory.md", fill(THEORY, **ex))
    md(out / "task.md", fill(TASK, first=df["date"].iloc[0].strftime("%Y-%m-%d"), last=df["date"].iloc[-1].strftime("%Y-%m-%d")))
    return b


THEORY = r"""
# Theory: rolling statistics

## Why one number per series is not enough

The mean and standard deviation of a whole series assume that the process behaves the same way throughout. Real systems
do not: the baseline drifts, the spread changes after a deployment, a busy season starts. A **rolling statistic** applies an
ordinary statistic to a window that slides along time, so it shows how the local level, spread or extremes evolve - and
gives a local yardstick for "is today unusual?". Judging today against the whole history would call every ordinary day of a
turbulent period an anomaly and ignore the size of a spike in a calm one.

## Definitions

For a window of $w$ observations ending at day $t$ (a **trailing** window, usable in real time):

$$
\bar{x}_t = \frac1w \sum_{j=0}^{w-1} x_{t-j}, \qquad
s_t = \sqrt{\frac{1}{w-1}\sum_{j=0}^{w-1}\bigl(x_{t-j}-\bar x_t\bigr)^2}, \qquad
\min_t,\ \max_t,\ Q_{p,t}.
$$

All of them are the lesson-01/02/03 statistics computed on a sliding subset. In the workbook the sample SD (`STDEV`) and the
inclusive percentile (`PERCENTILE`) are used. A *centred* window needs future data and is only for looking back; an
*expanding* window (from the start to $t$) never forgets.

## Rolling z-score

To judge a new value, compare it with the **previous** window, which excludes it:

$$
z_t = \frac{x_t - \bar{x}_{t-1}^{(w)}}{s_{t-1}^{(w)}}, \qquad \text{alert if } |z_t| > c \ (\text{often } c = 3).
$$

Why exclude today? If $x_t$ is inside its own window, it inflates the SD and pulls the mean, and a point can never exceed
$z = (w-1)/\sqrt{w}$ (Samuelson's bound): @mx@ for $w = 14$, so a 3.5-sigma alert is impossible by construction.

### Worked example (from `data.csv`)

On @d0@ the payment time is @x0@ ms. The previous 14 days have mean @m14@ and SD @s14@, so
$z = (@x0@ - @m14@)/@s14@ = @z0@$. With the day inside its own window the z-score is only @zi0@.
The same extra +30 ms on @dv@, during the volatile period (@vs@ to @ve@, noise SD roughly 14 ms instead of 5 ms), scores only
$z = @zv@$ against its own 14-day window; against the *global* mean and SD it would look like $z = @zgv@$.
Counting days with $|z|>3$: the global rule flags @nzg@ days, the previous-14-day rule @nz14@, the previous-28-day rule @nz28@.

## Choosing the window

| window | effect |
|---|---|
| short (7 d) | follows changes quickly; noisy (rolling SD ratio largest/smallest @r7@ here); a single spike dominates min/max |
| medium (14 d) | compromise (ratio @r14@) |
| long (28 d) | smooth and stable (ratio @r28@); slow to notice a change and straddles two regimes for weeks |

Practical rules: use a multiple of the seasonal period (7, 14, 28 days) so the cycle cancels
([lesson 07](../07-trend-seasonality-and-noise/theory.md)); make the window long enough for the statistic (an SD from 7 points is
very imprecise, a P99 from 14 points is meaningless - see [lesson 03](../03-percentiles-and-extreme-values/theory.md)); and make it short
enough that the process is roughly stable inside it. Rolling mean with a window is the SMA of
[lesson 08](../08-moving-averages-and-exponential-smoothing/theory.md); the EWMA variant replaces the hard window with decaying weights.

## Edge effects

- The first $w-1$ days have no value (or a value from a partial window if you allow `min_periods < w`; then the first
  results are much less reliable and should be marked).
- After a regime change the window contains old and new data for $w$ days, so the rolling SD is a blend and the z-scores of
  the first volatile days are inflated (the first volatile day, @d80@, is flagged by the rolling rule for exactly this reason).
- The latest value is the one that matters for monitoring and also the one with the most one-sided information.
- Missing days shift a row-count window; use a time-based window if the data are unevenly spaced
  ([lesson 06](../06-time-aggregation-and-sampling-frequency/theory.md)).

## Assumptions and pitfalls

1. **Rolling max/min are extreme-value statistics:** they depend on one point and jump when it enters or leaves the window.
2. **Autocorrelation:** consecutive rolling values share $w-1$ observations. Do not treat them as independent samples or
   test them as if they were.
3. **Multiple testing:** with daily checks, a $3\sigma$ rule gives about one false alert per year even for perfect normal data;
   real latency data are heavy-tailed, so expect more ([lesson 29](../29-false-alarms-and-detection-performance/theory.md)).
4. **Contamination:** an anomaly stays in the next windows and raises the SD, which hides the following anomaly. Robust variants
   use median and MAD ([lesson 02](../02-robust-statistics/theory.md)).
5. **Trend inside the window** makes the rolling SD too large; detrend or use a shorter window
   ([lesson 09](../09-differencing-and-growth-rates/theory.md)).
6. **A flag is a statement about the recent past,** not about correctness: a slow drift is never flagged because the window drifts with it.

## Where this leads

Rolling windows are the machinery behind anomaly detectors ([lesson 28](../28-time-series-anomaly-detection/theory.md)) and control
charts ([lesson 26](../26-statistical-process-control/theory.md)); window choice reappears as the training window in backtests
([lesson 24](../24-backtesting-and-forecast-accuracy/theory.md)). Background:
[stationarity](../../notes/time_series/stationarity.md), [statistical moments](../../notes/time_series/statistical_moments_and_time_series.md).
"""

TASK = r"""
# Task: rolling statistics

## Scenario

You run reliability for a payments platform. The dashboard shows the daily average **payment-processing time** with one
fixed alert line (mean + 3 SD of everything so far). On-call engineers say it "cries wolf" during some weeks and stays
silent when a single day clearly looked wrong. You are asked to replace it with a rolling view and to explain, with data,
which window length and which rule you would use.

## Data

`data.csv` - 180 consecutive days from @first@ to @last@; one row = one day.

| column | meaning |
|---|---|
| `date` | calendar day |
| `payment_ms` | average payment-processing time of that day (milliseconds) |

## Questions

Work in a spreadsheet (import `data.csv`), then compare with `solution.xlsx`.

1. With a window of 14 days (including the current day), compute the rolling **mean, SD, minimum, maximum and 90th percentile**.
   Report the values on the last day.
2. How many days at the start have no rolling value, and on which date does the first one appear?
3. On which date is the rolling SD largest, and what is the ratio of its largest to its smallest value? Does the rolling mean change by
   a comparable factor?
4. Repeat the rolling SD for windows of 7 and 28 days. Compare the ratio largest/smallest and the dates of the maximum.
5. Compute the **global z-score** $(x-\bar x)/s$ and two **rolling z-scores** against the *previous* 14 and 28 days. How many days have
   $|z|>3$ in each case, and which days are they?
6. List the three days with the largest previous-14-day z-score and their z-scores under the other two rules. What happens to
   a spike of the same size inside and outside the volatile weeks?
7. Compute a z-score where the day is *inside* its own 14-day window. What is the largest value it can ever reach, and what does the
   first spike score?
8. *Interpretation:* which window and rule would you deploy, what do the first 13 days and the start of the volatile period tell you
   about the weak points of a rolling alert, and what does a flag actually mean?

## Grafana

Import `grafana/dashboard.json` (see `../grafana/README.md`; no data-source setup is needed).

- On "Payment time with rolling 3-SD band", how does the width of the band change over the period and why?
- Compare the flags there with the global flags in "The same data judged by one global rule". Which days differ?
- On "Rolling standard deviation by window length", which line reacts first when the spread jumps, and which is the smoothest?

## Deliverable

A short note (6-8 lines) for the on-call team with named parts: **Rule** (window, statistic, threshold), **Evidence** (flag
counts and example days for the old and the new rule), **Weak points** (edge effects, regime changes) and **Next step** (one
thing you would try, for example a median/MAD version).
"""
