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

**Worked example.** Calibration errors $e = (-9,-4,-2,0,1,3,4,6,9,14)$, $n=10$, mean 2.2, SD 6.60, point forecast 200,
90% interval. *Normal:* $z=1.645$, half-width $=10.8$, interval $[189.2, 210.8]$. *Empirical* (linear-interpolation percentiles,
as Excel's `PERCENTILE`): $Q_{5\%}=-6.75$, $Q_{95\%}=11.75$, interval $[193.2, 211.8]$. The empirical interval leans to the
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
