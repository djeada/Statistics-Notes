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

The first seven days (Mon 2026-01-05 to Sun 2026-01-11) have orders 453, 414, 467, 423, 409, 381, 383. Their mean, 418.57, is the trend estimate for
the middle day 2026-01-08 (observed 423), so that day's detrended value is +4.43. Averaging the detrended Saturdays over all
21 weeks gives -47.4; the seven weekday means average -0.09, so after centring the Saturday index is
-47.3 (Sunday -40.6, Monday +33.2). A Saturday is therefore expected to be about -47.3 orders away from the trend.
Fitting a line to the seasonally adjusted series gives a slope of 0.92 orders per day.

## How much is trend, how much is season?

Using the variances of the components (Wang, Smith & Hyndman),

$$
F_T = 1 - \frac{\operatorname{Var}(R)}{\operatorname{Var}(T + R)}, \qquad
F_S = 1 - \frac{\operatorname{Var}(R)}{\operatorname{Var}(S + R)}
$$

are close to 1 when the component dominates the noise and close to 0 when it is invisible. Here $F_T$ = 0.83 and
$F_S$ = 0.77 with residual SD 17.0 orders. Report the residual SD in the units of the data; it is the yardstick for
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
