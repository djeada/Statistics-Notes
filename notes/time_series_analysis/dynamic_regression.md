# Dynamic Regression

Dynamic regression combines explanatory variables with time-series structure. It is useful when the target depends on external predictors but ordinary regression leaves autocorrelated residuals.

## Regression with Dynamic Errors

A basic model is

$$
y_t = \beta_0 + \beta_1 x_{1,t} + \cdots + \beta_k x_{k,t} + n_t,
$$

where the error process $n_t$ follows an ARMA or ARIMA model. The regression coefficients describe the conditional mean after accounting for serial dependence in the errors.

If $n_t$ follows ARMA$(p,q)$, then

$$
\phi(B)n_t = \theta(B)\varepsilon_t.
$$

This is often called **regression with ARIMA errors** or **dynamic regression**.

## Why Ordinary Least Squares Can Be Inadequate

When residuals are autocorrelated, ordinary least squares coefficient estimates can still be unbiased under appropriate exogeneity assumptions, but standard errors and uncertainty calculations are generally wrong if the serial correlation is ignored. Forecasts also waste information contained in the residual dynamics.

## Lagged Predictors and Distributed Lags

Effects are not always instantaneous. A distributed-lag model includes current and past predictor values:

$$
y_t = \beta_0 + \beta_0^{(x)}x_t + \beta_1^{(x)}x_{t-1}+\cdots+\beta_r^{(x)}x_{t-r}+n_t.
$$

Use lagged predictors when the domain suggests delayed responses. Avoid adding many lags mechanically because adjacent lags are often highly correlated.

## Future Predictor Availability

Dynamic regression introduces an important forecasting requirement: future predictor values must be known or forecast separately.

Examples of predictors known in advance include calendar variables, scheduled prices, and planned promotions. Weather or macroeconomic variables may require their own forecasts. Evaluating a model with realized future predictors when those values would not have been known at the forecast origin creates leakage and overstates performance.

## ARIMAX Terminology

The label **ARIMAX** is used inconsistently. It can mean ARIMA with exogenous regressors, but software packages differ in parameterization. Always inspect the exact model equation rather than relying on the name alone.

## Causality Caution

A useful predictor is not automatically causal. Regression coefficients in observational time series can reflect confounding, feedback, common trends, or omitted variables. Temporal ordering helps forecasting but does not by itself identify interventions.

## Workflow

1. Plot target and predictors and align their timestamps.
2. Decide which predictors would actually be available at forecast time.
3. Transform non-stationary variables when required by the modeling objective.
4. Fit the regression mean structure.
5. Inspect residual ACF/PACF.
6. Add ARMA/ARIMA error structure when residual dependence remains.
7. Diagnose residuals again.
8. Backtest the complete procedure, including how future predictors are obtained.

See [regression with ARMA errors](regression_with_arma_errors.md) for a shorter treatment and `scripts/time_series_analysis/dynamic_regression.py` for a worked simulation.
