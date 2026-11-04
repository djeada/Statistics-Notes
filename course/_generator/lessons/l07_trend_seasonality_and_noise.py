"""Lesson 07 - Trend, seasonality and noise (additive decomposition with weekday seasonality)."""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import Book, Dash, md, write_csv  # noqa: E402

SLUG = "07-trend-seasonality-and-noise"
TITLE = "Trend, seasonality and noise"
MODULE = "Understanding time series"
DATASET = "147 days (21 full weeks) of daily orders of an online shop"
DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
WEEKDAY_EFFECT = np.array([35, 30, 20, 10, -5, -45, -45], dtype=float)  # sums to 0
SALE_DAY = 100  # index of the flash-sale day (hidden in the task)


def make_data() -> pd.DataFrame:
    rng = np.random.default_rng(707)
    n = 147
    t = np.arange(n)
    dates = pd.date_range("2026-01-05", periods=n, freq="D")  # 2026-01-05 is a Monday
    noise = rng.normal(0, 14, n)
    orders = 420 + 0.9 * t + WEEKDAY_EFFECT[t % 7] + noise
    orders[SALE_DAY] += 140  # flash sale
    return pd.DataFrame({"date": dates, "orders": orders.round(0).astype(int)})


def decompose(df: pd.DataFrame) -> pd.DataFrame:
    """Independent pandas implementation of the classical additive decomposition (period 7)."""
    s = df["orders"].astype(float)
    wd = df["date"].dt.weekday
    out = pd.DataFrame({"date": df["date"], "orders": s, "wd": wd})
    out["trend"] = s.rolling(7, center=True).mean()
    out["detr"] = s - out["trend"]
    avg = out.groupby("wd")["detr"].mean()
    idx = avg - avg.mean()
    out["seasonal"] = wd.map(idx)
    out["resid"] = s - out["trend"] - out["seasonal"]
    out["adj"] = s - out["seasonal"]
    return out, avg, idx


def fill(text: str, **kw) -> str:
    for k, v in kw.items():
        text = text.replace(f"@{k}@", str(v))
    return text


def build(out: Path) -> Book:
    df = make_data()
    write_csv(out, df)
    n = len(df)
    D, avg, idx = decompose(df)
    ok = D["trend"].notna().to_numpy()
    tt = np.arange(n, dtype=float)
    slope_raw, icpt_raw = np.polyfit(tt, D["orders"], 1)
    slope_adj, icpt_adj = np.polyfit(tt, D["adj"], 1)
    res = D["resid"][ok]
    res_sd = float(res.std(ddof=1))
    tpr = (D["orders"] - D["seasonal"])[ok]
    ft = 1 - res.var(ddof=1) / tpr.var(ddof=1)
    fs = 1 - res.var(ddof=1) / D["detr"][ok].var(ddof=1)
    weekend = float((idx[5] + idx[6]) / 2 - idx[:5].mean())
    big = D["resid"].abs()
    big_i = int(big.idxmax())
    n3 = int((big > 3 * res_sd).sum())
    next_pred = icpt_adj + slope_adj * n + idx[0]  # day n is a Monday

    # ------------------------------------------------------------------ workbook
    b = Book(df, "Lesson 07 - Trend, seasonality and noise",
             "Classical additive decomposition: orders = trend + weekday effect + residual.")
    O, A = b.rng("orders"), "Data!$A$2:$A$%d" % (n + 1)
    b.add_column("day_no", lambda r: f"=A{r}-$A$2", expected=np.arange(n), fmt="0")
    b.add_column("weekday", lambda r: f"=WEEKDAY(A{r},2)", expected=D["wd"] + 1, fmt="0")
    b.add_column("trend_cma7", lambda r: f"=AVERAGE(B{r - 3}:B{r + 3})" if 5 <= r <= n - 2 else "",
                 expected=D["trend"], fmt="0.0")
    b.add_column("detrended", lambda r: f'=IF(ISNUMBER(E{r}),B{r}-E{r},"")', expected=D["detr"], fmt="0.0")
    W, DET = b.rng("weekday"), b.rng("detrended")

    b.section("1. Linear trend of the raw series")
    s_raw = b.row("Slope of orders vs day (orders per day)", f"=SLOPE({O},{b.rng('day_no')})", slope_raw, "0.000")
    i_raw = b.row("Intercept", f"=INTERCEPT({O},{b.rng('day_no')})", icpt_raw, "0.0")

    b.section("2. Weekday seasonal indices (mean of detrended values, centred to sum to 0)")
    r0 = b.next_row  # header row of the table
    f, l = r0 + 1, r0 + 7
    rows, exp = [], {}
    for k in range(7):
        r = f + k
        rows.append([DAYS[k], f"=AVERAGEIF({W},{k + 1},{DET})", f"=B{r}-AVERAGE($B${f}:$B${l})",
                     f"=COUNTIF({W},{k + 1})"])
        exp.update({(k, 1): avg[k], (k, 2): idx[k], (k, 3): n // 7})
    t0, t1 = b.table(["Weekday", "Mean detrended", "Seasonal index", "Days"], rows,
                     fmt={1: "0.0", 2: "0.0", 3: "0"}, expect=exp)
    assert (t0, t1) == (f, l)
    b.row("Sum of the seven indices", f"=SUM(C{f}:C{l})", 0.0, "0.000", "Zero by construction")
    wk = b.row("Weekend dip (Sat/Sun mean minus Mon-Fri mean)", f"=AVERAGE(C{f + 5}:C{f + 6})-AVERAGE(C{f}:C{f + 4})",
               weekend, "0.0", "orders")
    b.bar_chart_from_table("Weekday seasonal index (orders)", 1, [3], f, l, anchor="H4", y_title="orders")

    seas_ref = f"Analysis!$C${f}:$C${l}"
    b.add_column("seasonal", lambda r: f"=INDEX({seas_ref},D{r})", expected=D["seasonal"], fmt="0.0")
    b.add_column("seasonally_adj", lambda r: f"=B{r}-G{r}", expected=D["adj"], fmt="0.0")
    b.add_column("residual", lambda r: f'=IF(ISNUMBER(E{r}),B{r}-E{r}-G{r},"")', expected=D["resid"], fmt="0.0")
    b.add_column("abs_residual", lambda r: f'=IF(ISNUMBER(I{r}),ABS(I{r}),"")', expected=big, fmt="0.0")
    b.add_column("trend_plus_resid", lambda r: f'=IF(ISNUMBER(E{r}),B{r}-G{r},"")',
                 expected=np.where(ok, D["orders"] - D["seasonal"], np.nan), fmt="0.0")
    RES, ABSR = b.rng("residual"), b.rng("abs_residual")

    b.section("3. Trend of the seasonally adjusted series")
    s_adj = b.row("Slope (orders per day)", f"=SLOPE({b.rng('seasonally_adj')},{b.rng('day_no')})", slope_adj, "0.000",
                  "Compare with the raw slope above")
    i_adj = b.row("Intercept", f"=INTERCEPT({b.rng('seasonally_adj')},{b.rng('day_no')})", icpt_adj, "0.0")
    b.row("Rows lost at the edges by a centred 7-day average", f"=COUNTBLANK({b.rng('trend_cma7')})", int((~ok).sum()), "0")

    b.section("4. Noise")
    sd = b.row("Residual standard deviation (orders)", f"=STDEV({RES})", res_sd, "0.00")
    b.row("Largest absolute residual", f"=MAX({ABSR})", float(big.max()), "0.0")
    b.row("Date of the largest residual", f"=INDEX({A},MATCH(MAX({ABSR}),{ABSR},0))", None, "yyyy-mm-dd")
    n3c = b.row("Days with |residual| > 3 SD", f'=COUNTIF({ABSR},">"&3*{b.local(sd)})', n3, "0")
    ft_c = b.row("Trend strength  1 - Var(resid)/Var(trend+resid)",
                 f"=1-VAR({RES})/VAR({b.rng('trend_plus_resid')})", ft, "0.000")
    fs_c = b.row("Seasonal strength  1 - Var(resid)/Var(seasonal+resid)", f"=1-VAR({RES})/VAR({DET})", fs, "0.000")

    b.section("5. Forecast for the next day (a Monday): trend + weekday effect")
    nxt = b.row("Next day number", n, None, "0")
    fc = b.row("Forecast orders", f"={b.local(i_adj)}+{b.local(s_adj)}*{b.local(nxt)}+C{f}", next_pred, "0.0",
               "intercept + slope x day + Monday index")

    b.line_chart("Orders and 7-day centred average", "date", ["orders", "trend_cma7", "seasonally_adj"],
                 anchor="H22", y_title="orders")

    b.answers([
        ("Slope of the raw series (orders/day)", f"={s_raw}",
         f"{slope_raw:.3f} orders per day: the shop gains about {slope_raw * 7:.1f} orders per week."),
        ("Centred 7-day average: rows lost at the edges", f"=COUNTBLANK({b.rng('trend_cma7')})",
         "3 rows at each end have no full window, so the trend estimate is missing exactly where a forecast needs it."),
        ("Weekday seasonal indices; weekend dip", f"={wk}",
         f"Highest: {DAYS[int(idx.idxmax())]} ({idx.max():+.1f}); lowest: {DAYS[int(idx.idxmin())]} ({idx.min():+.1f}). "
         f"Weekends run {abs(weekend):.0f} orders below weekdays."),
        ("Slope and intercept of the seasonally adjusted series", f"={s_adj}",
         f"Slope {slope_adj:.3f}/day vs raw {slope_raw:.3f}/day: close, because 21 whole weeks contain each weekday equally "
         f"often; the adjusted line is far less scattered, so the slope is better determined."),
        ("Residual SD and the day with the largest residual", f"={sd}",
         f"SD = {res_sd:.1f} orders. Largest residual {D['resid'][big_i]:+.0f} on {D['date'][big_i]:%Y-%m-%d} "
         f"({int((big > 3 * res_sd).sum())} day(s) beyond 3 SD): a one-off event no trend or weekday effect explains."),
        ("Trend strength and seasonal strength", f"={ft_c}",
         f"Trend strength {ft:.2f}, seasonal strength {fs:.2f}: both components explain most of the variation; noise is small."),
        ("Forecast for the next Monday", f"={fc}",
         f"{next_pred:.0f} orders (trend {icpt_adj + slope_adj * n:.0f} plus Monday effect {idx[0]:+.0f}); a point forecast with no interval."),
        ("Do the seven indices sum to zero? Why centre them?", f"=SUM(Analysis!C{f}:C{l})",
         "Yes. Without centring the seasonal term would also shift the overall level and compete with the trend intercept."),
        ("Limits of this decomposition", "see note",
         "Additive effects assume the weekend dip stays the same size as the level grows; a single sale day is left in the "
         "residual but also leaks a little into the Wednesday index and the trend average; edge days have no trend."),
    ])

    # ------------------------------------------------------------------- grafana
    d = Dash("stats-07-trend-seasonality", "07 · Trend, seasonality and noise",
             "Additive decomposition of daily orders: 7-day centred trend, weekday effect and residuals.",
             D.rename(columns={"date": "time"}), "time")
    d.stat("Decomposition summary", {"trend orders/day": slope_adj, "weekend dip": weekend, "residual SD": res_sd,
                                     "trend strength": ft, "seasonal strength": fs, "sale-day residual": D["resid"][big_i]},
           "Computed from data.csv; see theory.md for the definitions.", decimals=2)
    raw = D[["date", "orders", "trend"]].rename(columns={"date": "time", "trend": "trend (centred 7-day mean)"})
    d.timeseries("Orders and centred 7-day mean", raw, "The 7-day window contains every weekday once, so the weekly cycle cancels.",
                 colors={"orders": "#9AA5B1", "trend (centred 7-day mean)": "#4E79A7"})
    fit = pd.DataFrame({"time": D["date"], "seasonally adjusted": D["adj"], "linear trend": icpt_adj + slope_adj * tt})
    d.timeseries("Seasonally adjusted orders and fitted trend", fit,
                 "Orders minus the weekday index; the weekly sawtooth is gone, the line remains.", dashed=["linear trend"],
                 colors={"seasonally adjusted": "#59A14F", "linear trend": "#E15759"})
    d.bars("Weekday seasonal index (orders)", pd.DataFrame({"weekday": DAYS, "index": idx.to_numpy().round(1)}),
           "Mean detrended orders per weekday, centred to sum to zero.", w=8)
    rs = pd.DataFrame({"time": D["date"], "residual": D["resid"], "+3 SD": 3 * res_sd, "-3 SD": -3 * res_sd,
                       "beyond 3 SD": D["resid"].where(D["resid"].abs() > 3 * res_sd)})
    d.timeseries("Residuals (noise) with 3 SD limits", rs, "What is left after trend and weekday effect; the flagged dot is the flash sale.",
                 points=["beyond 3 SD"], dashed=["+3 SD", "-3 SD"],
                 colors={"residual": "#76B7B2", "+3 SD": "#E15759", "-3 SD": "#E15759", "beyond 3 SD": "#E15759"}, w=16)
    d.save(out)

    # ------------------------------------------------------------------ markdown
    first7 = df["orders"].iloc[:7].tolist()
    ex = dict(o=", ".join(map(str, first7)), cma=f"{np.mean(first7):.2f}", d4=df["date"].iloc[3].strftime("%Y-%m-%d"),
              ob=first7[3], dt=f"{first7[3] - np.mean(first7):+.2f}", sat=f"{idx[5]:+.1f}", sun=f"{idx[6]:+.1f}",
              mon=f"{idx[0]:+.1f}", sl=f"{slope_adj:.2f}", ftv=f"{ft:.2f}", fsv=f"{fs:.2f}", nm=f"{res_sd:.1f}",
              satavg=f"{avg[5]:.1f}", avgm=f"{avg.mean():.2f}", nused=n // 7)
    md(out / "theory.md", fill(THEORY, **ex))
    md(out / "task.md", fill(TASK, first=df["date"].iloc[0].strftime("%Y-%m-%d"), last=df["date"].iloc[-1].strftime("%Y-%m-%d")))
    return b


THEORY = r"""
# Theory: trend, seasonality and noise

## Why decompose a series

A daily count jumps around, and every jump invites a story: "Saturday was bad", "growth is slowing", "the campaign
worked". Most of those stories are wrong because three different things are mixed in one line: a slow **trend**, a
regular **seasonal** pattern (here: the day of the week) and unpredictable **noise**. Decomposition separates them, so
that you compare like with like (Saturday with Saturdays), measure growth without the weekly sawtooth, and recognise a
genuinely unusual day only after the predictable part has been removed.

## The additive model

$$
y_t = T_t + S_{t \bmod m} + R_t, \qquad \sum_{k=1}^{m} S_k = 0
$$

- $T_t$, the **trend**: slowly changing level (here a roughly linear growth in orders per day).
- $S_k$, the **seasonal index** of position $k$ in a cycle of length $m$ (weekday: $m = 7$). It repeats exactly and is
  centred to sum to zero, so it redistributes orders within a cycle without changing the level.
- $R_t$, the **residual** (noise): everything left over. It should look patternless; if not, the model is incomplete.

"Additive" means the seasonal swing has the same size in orders whatever the level. If the swing grows with the level
(sales doubling doubles the weekend dip), use a multiplicative model $y_t = T_t \cdot S_k \cdot R_t$, or take logarithms
first (see [lesson 09](../09-differencing-and-growth-rates/theory.md)).

## Classical decomposition, step by step

1. **Estimate the trend with a centred moving average whose length equals the period.** For $m = 7$ (odd):
   $\hat T_t = \frac{1}{7}\sum_{j=-3}^{3} y_{t+j}$. Because the window contains every weekday exactly once, the seasonal
   effects (which sum to zero) cancel and what remains is the level. For an even period (e.g. $m = 12$) use a 2 x 12 average.
2. **Detrend:** $y_t - \hat T_t$ contains seasonality and noise only.
3. **Seasonal index** of weekday $k$: the mean of the detrended values on that weekday, then subtract the mean of the
   seven means so the indices sum to zero.
4. **Residual:** $\hat R_t = y_t - \hat T_t - \hat S_{k(t)}$. The **seasonally adjusted** series is $y_t - \hat S_{k(t)}$.

### Worked example (from `data.csv`)

The first seven days (Mon 2026-01-05 to Sun 2026-01-11) have orders @o@. Their mean, @cma@, is the trend estimate for
the middle day @d4@ (observed @ob@), so that day's detrended value is @dt@. Averaging the detrended Saturdays over all
@nused@ weeks gives @satavg@; the seven weekday means average @avgm@, so after centring the Saturday index is
@sat@ (Sunday @sun@, Monday @mon@). A Saturday is therefore expected to be about @sat@ orders away from the trend.
Fitting a line to the seasonally adjusted series gives a slope of @sl@ orders per day.

## How much is trend, how much is season?

Using the variances of the components (Wang, Smith & Hyndman),

$$
F_T = 1 - \frac{\operatorname{Var}(R)}{\operatorname{Var}(T + R)}, \qquad
F_S = 1 - \frac{\operatorname{Var}(R)}{\operatorname{Var}(S + R)}
$$

are close to 1 when the component dominates the noise and close to 0 when it is invisible. Here $F_T$ = @ftv@ and
$F_S$ = @fsv@ with residual SD @nm@ orders. Report the residual SD in the units of the data; it is the yardstick for
"is this day unusual?" (a residual beyond about 3 SD deserves an explanation).

## Assumptions

- The seasonal pattern is **fixed**: the same $S_k$ every week. If it evolves, use methods that let it drift
  ([lesson 23](../23-exponential-smoothing-models/theory.md)).
- The period is **known** (7 days here; 24 hours, 12 months elsewhere).
- Trend is smooth relative to the window; a sudden step is smeared across the window length.
- Additive structure (see above).

## Pitfalls

1. **Edge loss.** A centred average of length 7 has no value for the first and last 3 days. The newest data - the part
   you care about for decisions - has no trend estimate. Fit a regression line instead, or accept a one-sided average.
2. **Outliers leak.** A flash-sale day inflates its own weekday's index and the average of the six neighbouring days.
   Check the residuals, and re-estimate without such days when the cause is known.
3. **Incomplete cycles.** If the series contains 20.5 weeks, some weekdays appear once more than others and the trend and
   indices are biased. Use whole cycles.
4. **Seasonally adjusted is not "true".** It depends on the estimated indices; a different model gives a different adjusted series.
5. **Reading the trend slope from the raw data** works only when each weekday occurs equally often.
6. **Residual is a model output.** Whatever you leave out of the model (promotions, holidays) ends up there.

## Where this leads

Differencing removes trend and seasonality algebraically instead
([lesson 09](../09-differencing-and-growth-rates/theory.md)); smoothers estimate the trend with fewer assumptions
([lesson 08](../08-moving-averages-and-exponential-smoothing/theory.md)); regression with trend and weekday dummies
turns this decomposition into a forecast ([lesson 22](../22-trend-and-seasonal-regression-forecasting/theory.md));
seasonal-naive benchmarks use the same period ([lesson 21](../21-naive-and-seasonal-naive-forecasts/theory.md)).
Background: [seasonality and trends](../../notes/time_series/seasonality_and_trends.md),
[stationarity](../../notes/time_series/stationarity.md).
"""

TASK = r"""
# Task: trend, seasonality and noise

## Scenario

You analyse daily orders for an online shop. Management reads the daily number every morning and keeps asking
"is it growing?", "why are weekends so bad?" and "was last month's campaign day special?". You have been given 21 weeks
of data and must separate what is *structure* (growth and weekly rhythm) from what is *noise*, so that the team stops
reacting to ordinary Saturdays and spots days that are really unusual.

## Data

`data.csv` - 147 consecutive days from @first@ (a Monday) to @last@; one row = one day.

| column | meaning |
|---|---|
| `date` | calendar day |
| `orders` | number of completed orders that day (count) |

## Questions

Work in a spreadsheet (import `data.csv`), then compare with `solution.xlsx`.

1. Fit a straight line to `orders` against the day number (0, 1, 2, ...). What is the slope in orders per day, and per week?
2. Compute a **centred 7-day moving average** as the trend estimate. How many rows have no value, and why?
3. Subtract the trend from the orders. Average the result for each weekday (Mon = 1 ... Sun = 7) and centre the seven
   values so they sum to zero. Which weekday is best, which is worst, and how large is the weekend dip?
4. Subtract the seasonal index from the orders to get the **seasonally adjusted** series and fit a line to it. Compare slope
   and intercept with question 1.
5. Compute the **residual** (orders - trend - seasonal index). What is its standard deviation? Which day has the largest
   absolute residual, and how many days are further than 3 SD from zero?
6. Compute the trend strength and the seasonal strength (formulas in the theory file). Which component is more
   important here?
7. Forecast the orders of the day after the last one (a Monday) as `intercept + slope x day number + Monday index`.
8. Check that the seven seasonal indices sum to zero, and explain why they are centred.
9. *Interpretation:* name two ways in which this decomposition could mislead the team (think about the edges of the series,
   one-off events and the assumption of a fixed weekly pattern).

## Grafana

Import `grafana/dashboard.json` (see `../grafana/README.md`; no data-source setup is needed).

- On "Orders and centred 7-day mean", where does the smooth line start and stop, and why?
- On "Seasonally adjusted orders and fitted trend", what disappeared compared with the raw series, and what stayed?
- On "Residuals", what does the flagged point tell you, and do the other residuals look patternless?

## Deliverable

A note (6-8 lines) for the head of e-commerce with named parts: **Growth** (orders per day, with the seasonally adjusted
slope), **Weekly pattern** (the indices and what to do about them), **Unusual days** (date, size in orders, how you know it
is unusual) and **Caveat** (one limitation of the method).
"""
