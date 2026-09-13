# Dynamic Regression

## Worked calculation: an external predictor and a lag

Suppose

$$
y_t=2+1.5x_t+n_t.
$$

For $x_t=4$ and $n_t=0.3$, the observed value is

$$
y_t=2+1.5(4)+0.3=8.3.
$$

If the response takes time to react, use a distributed lag such as

$$
y_t=2+1.0x_t+0.5x_{t-1}+n_t.
$$

When $x_t=4$ and $x_{t-1}=2$, the regression mean is $2+4+1=7$. For forecasting, that calculation is valid only if both predictor values would be available at the forecast origin. A realized future temperature, exchange rate, or policy variable may need its own forecast.

![Dynamic regression with serially correlated errors](../../assets/time_series/student/16_dynamic_regression.png)

Dynamic regression combines explanatory variables with time-series structure. It is useful when the target depends on external predictors but ordinary regression leaves autocorrelated residuals.

A basic model is

$$
y_t=\beta_0+\beta_1x_{1,t}+\cdots+\beta_kx_{k,t}+n_t,
$$

where the error process $n_t$ follows an ARMA or ARIMA model. If $n_t$ follows ARMA$(p,q)$,

$$
\phi(B)n_t=\theta(B)\varepsilon_t.
$$

Ignoring residual autocorrelation can invalidate ordinary standard-error calculations and waste forecastable structure even when coefficient estimates remain unbiased under suitable exogeneity assumptions.

## Lagged Predictors

A distributed-lag model may include current and past predictor values:

$$
y_t=\beta_0+\beta_0^{(x)}x_t+\beta_1^{(x)}x_{t-1}+\cdots+\beta_r^{(x)}x_{t-r}+n_t.
$$

Use lags when the domain suggests delayed responses; avoid mechanically adding many correlated lags.

## Future Predictor Availability

Future predictor values must be known or forecast separately. Calendar variables or scheduled promotions may be known in advance; weather and macroeconomic predictors usually are not. Evaluating with realized future predictors when they would not have been available creates leakage.

The label **ARIMAX** is used inconsistently across software. Inspect the exact model equation rather than relying on the name.

A useful predictor is not automatically causal. Temporal ordering helps forecasting but does not by itself identify interventions.

A practical workflow is: align timestamps, define what will be known at forecast time, fit the regression mean structure, inspect residual ACF/PACF, add dynamic error structure when justified, diagnose again, and backtest the complete procedure.

See [regression with ARMA errors](regression_with_arma_errors.md), [`dynamic_regression.py`](../../scripts/time_series/dynamic_regression.py), and the companion [notebook](../../notebooks/time_series/dynamic_regression.ipynb).
