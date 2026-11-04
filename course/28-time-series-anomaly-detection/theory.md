# Theory: time-series anomaly detection

## The failure this prevents

A temperature that is 8 C lower than usual is an emergency on a Wednesday and perfectly normal on a Sunday. A detector
that compares each reading with one global mean and spread cannot tell the two apart: it floods the on-call engineer with
weekend alarms until the alerts are muted - and then misses the real spike. Anomaly detection for time series is therefore
mostly about **building the right expectation first** (trend, seasonality) and only then asking how surprising the data are.

## Types of anomaly

- **Point anomaly**: a single reading far from its expected value (sensor dropout, transient spike).
- **Level shift**: the series jumps and stays (fouling, recalibration, a new setpoint). Several consecutive points are anomalous.
- **Contextual anomaly**: a value that is ordinary overall but wrong *for its context* (25 C on a Sunday when Sundays are 41 C).
- **Variance change**: the noise itself becomes larger or smaller (see [rolling statistics](../10-rolling-statistics/theory.md)).

## Expected value: a seasonal baseline

Write $x_t=\text{baseline}_t+e_t$. With a weekly cycle one simple, robust baseline is the **median of the same weekday in the
previous $m$ weeks**:

$$\hat b_t=\operatorname{median}\bigl(x_{t-7},x_{t-14},\dots,x_{t-7m}\bigr),\qquad e_t=x_t-\hat b_t .$$

Using only past values makes the detector *online* (it never peeks at the future), and the median means one earlier spike
does not corrupt the baseline. Here $m=4$, so the first 28 days produce no baseline. The residual $e_t$ is noisier than the
raw noise because $\hat b_t$ is itself an estimate: with four values the median has a standard deviation of roughly 0.6 times that of one
observation, which inflates the residual standard deviation by about 15-20 %. This is why the *scale* must be estimated from the residuals, not from the raw readings.

## Robust residual score

Scale the residual by a robust estimate of its usual size. With $\mathrm{MAD}=\operatorname{median}|e-\operatorname{median}(e)|$ and, since
residuals are already centred near 0, the median absolute residual over the last $w$ days:

$$\hat\sigma_t = 1.4826\cdot\operatorname{median}\bigl(|e_{t-w}|,\dots,|e_{t-1}|\bigr),\qquad z_t=\frac{e_t}{\hat\sigma_t}.$$

The constant $1.4826=1/\Phi^{-1}(0.75)$ makes $\hat\sigma$ consistent with the standard deviation for Gaussian noise
(equivalently the "modified z-score" of Iglewicz and Hoaglin multiplies by $0.6745$). Flag the day when $|z_t|>T$.
Median and MAD resist the very anomalies we are trying to find; a mean and standard deviation would be inflated by them
([lesson 2](../02-robust-statistics/theory.md), [lesson 4](../04-outlier-detection/theory.md)).

## Worked example

Previous four Mondays: 52.4, 53.1, 52.8, 51.9. The median is $(52.4+52.8)/2=52.6$. Today's reading is 59.4, so
$e=6.8$. The last 7 absolute residuals are 0.4, 1.1, 0.7, 1.6, 0.2, 0.9, 1.3 with median 0.9, so $\hat\sigma=1.4826\cdot0.9=1.33$ and
$z=6.8/1.33=5.1$. With $T=3.5$ this is an alarm. Under pure Gaussian noise $P(|Z|>3.5)=4.65\times10^{-4}$, i.e. about 0.17 false
alarms per year of daily data - but real residuals have heavier tails, so expect more.

## Choosing T and the adaptation time

Raising $T$ lowers false alarms and misses small anomalies; the trade-off is quantified in
[lesson 29](../29-false-alarms-and-detection-performance/theory.md). Two things limit how long a **level shift** is
flagged. The baseline (median of four weeks) is half-absorbed after two weeks and fully absorbed after three. Faster still,
the shifted residuals enter the rolling window that estimates the scale, which inflates $\hat\sigma$ and shrinks $z$ - in this
lesson's data the shift is flagged for only about a week. Re-learning is useful after a legitimate setpoint change and dangerous
when a real, permanent fault is accepted as normal.
Pair a point detector with a change-point detector such as CUSUM ([lesson 27](../27-change-point-detection/theory.md)) or a
fixed reference level.

## Assumptions and pitfalls

1. **The season is stable.** Holidays, daylight-saving shifts and product launches change the cycle; flags cluster around them.
2. **Warm-up costs history.** The first $7m$ + $w/2$ days cannot be scored; anomalies there are invisible.
3. **Contaminated baselines and scales.** If two of the four earlier same weekdays were anomalous the median is wrong; a long run of
   anomalies also inflates the rolling scale. A longer window, or excluding already-flagged days from the scale, helps.
4. **Heavy tails and autocorrelation** make the Gaussian false-alarm rate optimistic ([lesson 14](../14-spurious-correlation-and-autocorrelation/theory.md)).
5. **Trend.** A drifting series has a lagging baseline; detrend or use a regression baseline
   ([lesson 7](../07-trend-seasonality-and-noise/theory.md), [lesson 22](../22-trend-and-seasonal-regression-forecasting/theory.md)).
6. **Multiple testing.** Scoring 365 days with $T=3$ is 365 chances to alarm; the daily error rate is not the yearly one.

## Related notes

- [Seasonal naive forecasts](../21-naive-and-seasonal-naive-forecasts/theory.md) - the baseline above is a seasonal naive forecast with a median
- [Statistical process control](../26-statistical-process-control/theory.md)
- Repo notes: [seasonality and trends](../../notes/time_series/seasonality_and_trends.md)
