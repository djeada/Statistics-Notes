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
$z = (w-1)/\sqrt{w}$ (Samuelson's bound): 3.47 for $w = 14$, so a 3.5-sigma alert is impossible by construction.

### Worked example (from `data.csv`)

On 2026-03-14 the payment time is 157.9 ms. The previous 14 days have mean 122.60 and SD 4.07, so
$z = (157.9 - 122.60)/4.07 = 8.67$. With the day inside its own window the z-score is only 3.19.
The same extra +30 ms on 2026-05-18, during the volatile period (2026-04-23 to 2026-06-11, noise SD roughly 14 ms instead of 5 ms), scores only
$z = 2.0$ against its own 14-day window; against the *global* mean and SD it would look like $z = 3.5$.
Counting days with $|z|>3$: the global rule flags 5 days, the previous-14-day rule 3, the previous-28-day rule 5.

## Choosing the window

| window | effect |
|---|---|
| short (7 d) | follows changes quickly; noisy (rolling SD ratio largest/smallest 15.0 here); a single spike dominates min/max |
| medium (14 d) | compromise (ratio 7.7) |
| long (28 d) | smooth and stable (ratio 5.1); slow to notice a change and straddles two regimes for weeks |

Practical rules: use a multiple of the seasonal period (7, 14, 28 days) so the cycle cancels
([lesson 07](../07-trend-seasonality-and-noise/theory.md)); make the window long enough for the statistic (an SD from 7 points is
very imprecise, a P99 from 14 points is meaningless - see [lesson 03](../03-percentiles-and-extreme-values/theory.md)); and make it short
enough that the process is roughly stable inside it. Rolling mean with a window is the SMA of
[lesson 08](../08-moving-averages-and-exponential-smoothing/theory.md); the EWMA variant replaces the hard window with decaying weights.

## Edge effects

- The first $w-1$ days have no value (or a value from a partial window if you allow `min_periods < w`; then the first
  results are much less reliable and should be marked).
- After a regime change the window contains old and new data for $w$ days, so the rolling SD is a blend and the z-scores of
  the first volatile days are inflated (the first volatile day, 2026-04-23, is flagged by the rolling rule for exactly this reason).
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
