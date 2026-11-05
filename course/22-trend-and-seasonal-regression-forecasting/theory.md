# Theory: trend and seasonal regression forecasting

## Why regression, and what it prevents

A moving average or a naive forecast ([lesson 21](../21-naive-and-seasonal-naive-forecasts/theory.md)) reuses past values
and cannot say *how much* of the pattern is growth, *how much* is Saturday, and *how much* is December. A regression on
**time** and **calendar dummies** separates them into coefficients you can read, test and extrapolate. The danger it creates
is the opposite one: a model that fits history well (high $R^2$) and then forecasts badly because it extrapolates a trend
that has changed. This lesson shows how to build the model correctly and how to judge it on data it has not seen.

## The model

For observation $t = 1,\dots,n$ with weekday $w(t) \in \{\text{Mon},\dots,\text{Sun}\}$ and month $m(t)$:

$$
y_t = \beta_0 + \beta_1 t + \sum_{j=2}^{7} \gamma_j\,\mathbb{1}[w(t)=j] + \sum_{k=2}^{12} \delta_k\,\mathbb{1}[m(t)=k] + \varepsilon_t .
$$

- $\beta_1$ is the **trend**: expected change in orders per day, per day.
- $\gamma_j$ is the weekday $j$ level **relative to Monday** (the omitted *base* category); $\delta_k$ is month $k$ relative to
  January. One category must be omitted: with all 7 weekday dummies plus the intercept the columns add up to the constant
  column and the least-squares problem has no unique solution (the *dummy-variable trap*).
- The effects are **additive**: Saturday is always the same number of orders below Monday. If seasonality grows with the level
  (a multiplicative pattern) regress $\log y_t$ instead.

Coefficients minimise $\sum_t (y_t - \hat y_t)^2$ over the **training** rows only. In a spreadsheet:
`=INDEX(LINEST(y, X, TRUE, TRUE), 1, c)` where `X` is a block of contiguous columns. **LINEST returns the coefficients in
reverse order** (last predictor first, intercept last), so predictor $j$ of $m$ sits in column $m+1-j$.

## Forecasting

The $h$-step forecast just evaluates the fitted equation at future values of the *known* regressors:
$\hat y_{n+h} = \hat\beta_0 + \hat\beta_1 (n+h) + \hat\gamma_{w(n+h)} + \hat\delta_{m(n+h)}$. Calendar regressors are known in
advance, so no recursion or forecasting of inputs is needed. That is the main practical advantage over methods that need
future values of drivers (lesson 13).

## Worked example (10 days, 2 weekend days)

Orders $y = (112,118,121,119,126,104,101,129,135,136)$ for $t=1..10$, day 1 is a Monday; $W_t=1$ on Saturday/Sunday ($t=6,7$).

- Trend only, $y = a + bt$: $a = 110.13$, $b = 1.812$, $R^2 = 0.21$. The weekend dip hides the trend.
- Trend + weekend dummy: $\hat y_t = 111.80 + 2.419\,t - 25.02\,W_t$, $R^2 = 0.967$, residual SE $= 2.46$.
- Forecasts: $t=11$ (Thursday): $111.80 + 2.419\cdot 11 = 138.41$; $t=13$ (Saturday): $111.80 + 2.419\cdot 13 - 25.02 = 118.22$.

Adding one dummy raised $R^2$ from 0.21 to 0.97 and also *corrected the trend* from 1.81 to 2.42 orders/day: a seasonal pattern
left out of the model biases the trend estimate whenever the sample does not contain whole cycles.

## In-sample fit is not forecast accuracy

Split chronologically: fit on the first part, evaluate on the last 28 days. $R^2$ and the residual standard error describe
the *training* rows; the **holdout RMSE** $\sqrt{\tfrac1H\sum (y_{n+h}-\hat y_{n+h})^2}$ describes forecasting. Always compare
against the cheapest competitor. Here that is the seasonal naive forecast $\hat y_{n+h} = y_{n+h-7\lceil h/7\rceil}$: more
terms in the regression are only worth their complexity if they beat it **out of sample**. Report the **bias** (mean error) as
well as RMSE: a trend model that over-forecasts every day has a systematic, fixable problem; one with the same RMSE and no
bias has a noise problem.

## Assumptions

1. The relationship between time and the mean is the one you wrote down (linear trend, fixed calendar effects).
2. Errors have zero mean and roughly constant variance. With daily data they are usually **autocorrelated**, so the
   standard errors LINEST reports are too small; point forecasts stay fine but intervals need care (lesson 25).
3. The structure of the future resembles the past: that is an assumption about the world, not something the fit can test.

## Pitfalls

1. **Extrapolating a trend that stalls.** A linear term has no memory of recent growth; its error grows with the horizon.
   Shorten the fitting window, add curvature, or use smoothing that adapts ([lesson 23](../23-exponential-smoothing-models/theory.md)).
2. **Dummy trap / wrong base.** Omit exactly one category per factor; interpret coefficients relative to it.
3. **Month dummies from one year.** Each month effect is then a single observation of that month and cannot be separated
   from that year's events; two or more years are the minimum, or use a smooth Fourier term.
4. **Holidays and one-off events.** Black Friday does not belong to "November"; give it its own indicator or remove it from
   the fit, otherwise it distorts the neighbouring coefficients.
5. **Judging by $R^2$.** Adding regressors never lowers training $R^2$; it can raise holdout error.
6. **Leakage.** Fitting the dummies on all data and then "forecasting" the last weeks is not a forecast.

## Related notes

- [Trend, seasonality and noise](../07-trend-seasonality-and-noise/theory.md)
- [Linear regression](../12-linear-and-nonlinear-regression/theory.md) and [multiple regression](../13-multiple-regression-and-confounding/theory.md)
- [Residual diagnostics](../15-residual-analysis-and-model-diagnostics/theory.md)
- [Backtesting and forecast accuracy](../24-backtesting-and-forecast-accuracy/theory.md) and [prediction intervals](../25-prediction-intervals-and-forecast-uncertainty/theory.md)
- Repo notes: [seasonality and trends](../../notes/time_series/seasonality_and_trends.md), [forecast evaluation](../../notes/time_series/forecast_evaluation.md)
