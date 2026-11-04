# Theory: change-point detection

## The problem a single threshold cannot solve

A sensor that drifts from 70.0 C to 70.7 C will almost never produce a point outside the usual +/-3 sigma limits when the
noise is 0.8 C - yet the process has changed, and a month later the change may be expensive. Shewhart-style rules look at
**one reading at a time** and need a large jump. A **change-point** method looks at the *accumulated* evidence of many small
deviations, trading a little delay for much more sensitivity. Two complementary tools are used here: an **online** detector
(CUSUM: "has something changed *yet*?") and an **offline** estimator (the best split: "*when* did it change?").

## Model

Readings $x_1,\dots,x_n$ are independent with mean $\mu_0$ before an unknown change time $\tau$ and $\mu_1=\mu_0+\delta\sigma$
after it, with constant standard deviation $\sigma$. Estimate $\mu_0,\sigma$ from a phase-I stretch known to be in control and
standardise: $z_t=(x_t-\mu_0)/\sigma$.

## CUSUM

Two one-sided sums accumulate the part of each deviation that exceeds the **reference value** $k$ (the allowance):

$$C_t^{+}=\max\bigl(0,\;C_{t-1}^{+}+z_t-k\bigr),\qquad C_t^{-}=\max\bigl(0,\;C_{t-1}^{-}-z_t-k\bigr),\qquad C_0^{\pm}=0.$$

An alarm is raised the first time $C_t^{\pm}>h$, the **decision threshold**. Interpretation:

- $k$ is usually set to **half the shift you want to catch**: $k=\delta/2$ (so $k=0.5$ targets a 1-sigma shift). Deviations smaller
  than $k$ push the sum back to zero, so ordinary noise cannot accumulate.
- $h$ controls how much accumulated evidence you demand; $h=4$ or $5$ with $k=0.5$ is the textbook default.
- The point where $C^{+}$ last equalled 0 before the alarm is a natural estimate of the change start.

Worked example ($k=0.5$): standardised readings $0.2,\;0.9,\;1.1,\;0.6,\;1.4$ give
$C^{+}=\max(0,0.2-0.5)=0,\;0.4,\;1.0,\;1.1,\;2.0$. No single reading exceeds 1.5 sigma, but the sum reaches 2.0 after five
readings; with $h=2$ that is an alarm, with $h=5$ it would still be silent.

## Best split (offline estimate of $\tau$)

For every candidate split $j$ fit one mean to $x_1..x_j$ and another to $x_{j+1}..x_n$ and compute the total
sum of squared errors

$$\mathrm{SSE}(j)=\sum_{t\le j}(x_t-\bar x_{1:j})^2+\sum_{t>j}(x_t-\bar x_{j+1:n})^2 .$$

The estimate is $\hat\tau=\arg\min_j \mathrm{SSE}(j)$; under Gaussian noise this is the maximum-likelihood change point.
Worked example: $x=\{1,2,1,4,5,4\}$. A single mean (2.833) gives $\mathrm{SSE}=14.83$; splitting after $j=3$ gives means 1.333
and 4.333 and $\mathrm{SSE}=0.667+0.667=1.33$ - a 91 % reduction. The SSE-versus-$j$ curve is V-shaped, and its depth tells you
how convincing the change is. Always keep a few points at each end (here 10) since a split near the edge fits one mean to a handful of
values.

In this lesson's data the minimum is at reading 138 and the CUSUM alarm comes at reading 153.

## Delay versus false alarms

Two numbers summarise a CUSUM chart. **ARL0** is the average number of readings between false alarms when nothing has changed;
**ARL1** is the average number of readings until an alarm after a real shift. Raising $h$ raises both. For one-sided CUSUM,
Siegmund's approximation with $b=h+1.166$ and $\Delta=\delta-k$ is

$$\mathrm{ARL}_1\approx\frac{e^{-2\Delta b}+2\Delta b-1}{2\Delta^2},\qquad
\mathrm{ARL}_0\approx\frac{e^{2kb}-2kb-1}{2k^2}\quad(\Delta=-k).$$

For $k=0.5,\,h=5$ this gives $\mathrm{ARL}_0\approx 938$ one-sided (about 465 for the two-sided chart) and $\mathrm{ARL}_1\approx 10$ readings for
a 1-sigma shift. $\mathrm{ARL}_0$ grows like $e^{2kh}$ while delay grows only linearly in $h$ - so a moderate increase
of $h$ buys a lot of false-alarm protection for a few extra readings of delay.

## Assumptions and pitfalls

1. **Phase I must be clean.** If mu0 or sigma0 are estimated from data that already contain the shift, the chart is calibrated
   to the wrong target. Use a robust estimate ([lesson 2](../02-robust-statistics/theory.md)) when outliers are possible.
2. **Autocorrelation breaks the ARL numbers.** Smooth sensors have correlated errors; effective sample size is smaller and false alarms are
   more frequent than the table says ([lesson 14](../14-spurious-correlation-and-autocorrelation/theory.md)).
3. **The best split always finds something.** Even pure noise has a minimum SSE; judge the reduction in SSE, the size of the shift
   in sigma units, and whether the split is stable when you drop 10 % of the data.
4. **One change point only.** Several changes need binary segmentation or a penalised criterion; a single split between two
   shifts is a compromise.
5. **Alarm is not diagnosis.** CUSUM says the mean moved; it does not say whether the sensor drifted or the process did.
6. **Reset rules matter.** After an alarm you must decide whether to reset the sums; otherwise the chart stays "in alarm".

## Related notes

- [Statistical process control](../26-statistical-process-control/theory.md) - the Shewhart chart this lesson improves on
- [Anomaly detection](../28-time-series-anomaly-detection/theory.md) and
  [false alarms and detection performance](../29-false-alarms-and-detection-performance/theory.md)
- [Rolling statistics](../10-rolling-statistics/theory.md) and [trend and seasonality](../07-trend-seasonality-and-noise/theory.md)
- Repo notes: [stationarity](../../notes/time_series/stationarity.md), [random walk](../../notes/time_series/random_walk.md)
