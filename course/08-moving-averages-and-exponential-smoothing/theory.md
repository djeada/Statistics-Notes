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
  $1/7 = 0.143$ and for $\alpha = 0.3$ it is 0.176, i.e. the noise SD shrinks to 0.378 (SMA) and 0.420 (EWMA 0.3) of its raw
  value; the matching $\alpha = 0.25$ gives 0.378, the same as the SMA.
- **Start-up:** $s_1 = x_1$ inherits that day's noise, which decays like $(1-\alpha)^t$. Skip the first few days or start
  from the mean of a baseline.

### Worked example (first days of `data.csv`)

Tickets on the first five days are 192, 218, 213, 185, 198. EWMA with $\alpha=0.3$: $s_1 = x_1$, then $s_2 = 0.3x_2 + 0.7s_1$, and so on:
$s$ = 192.00, 199.80, 203.76, 198.13, 198.09. The trailing 3-day SMA for 2026-02-05 (days 2-4) is 205.33.

## Choosing alpha (or the window)

- **For forecasting:** a one-step forecast of tomorrow is today's $s_t$. Pick $\alpha$ that minimises
  $\sqrt{\tfrac1{n-1}\sum (x_{t+1}-s_t)^2}$. In `data.csv` the best of the grid is $\alpha = 0.2$, and the curve is flat
  around it, so the choice is not critical.
- **For monitoring:** decide how many days of delay you can accept for a real change and how many false alerts you can
  tolerate; large $\alpha$ (short window) detects faster and alerts falsely more often.
- **For reporting:** use a window equal to the natural cycle (a week, a month).

In `data.csv` with an alert level of 215 tickets: the raw series alerts 14 times before the release; the first alert after the release comes, counted in days
from the release, after 1 (trailing SMA7), 0 (centred MA), 1 (EWMA 0.3), 4 (EWMA 0.1) and 9 (SMA 21). Noise SD
before the release: raw 15.8, SMA7 5.4, EWMA 0.3 6.2, EWMA 0.1 2.8.

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
