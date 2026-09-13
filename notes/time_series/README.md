# Time Series

Time-series methods extend the core statistics curriculum to observations indexed by time, where serial dependence, trend, seasonality, and changing variance make independent-sample methods inadequate.

## Prerequisites

Before starting this unit, be comfortable with:

- **[Joint Distributions & Covariance](../joint_distributions_and_covariance/README.md)** — covariance, correlation, and dependence;
- **[Regression](../regression/README.md)** — fitted models, residuals, and regression inference;
- **[Resampling & Model Assessment](../resampling_and_model_assessment/README.md)** — out-of-sample evaluation and leakage;
- basic algebra of sequences and difference equations.

## 1. Mathematical and Data Foundations

1. **[Series](series.md)** — sequences, series, convergence, and manipulations used in linear-process representations.
2. **[Difference Equations](difference_equations.md)** — recursive equations behind dynamic models.
3. **[Time Series](time_series.md)** — what makes time-indexed data different from ordinary cross-sectional data.
4. **[Statistical Moments and Time Series](statistical_moments_and_time_series.md)** — means, variances, covariance, and higher moments in the time-indexed setting.

## 2. Dependence and Stationarity

1. **[Stationarity](stationarity.md)** — the stability conditions that make many classical models interpretable.
2. **[Random Walk](random_walk.md)** — the canonical nonstationary process and a bridge to unit-root ideas.
3. **[Seasonality and Trends](seasonality_and_trends.md)** — deterministic and stochastic structure that must be handled before model identification.
4. **[Autocovariance Function](autocovariance_function.md)** — dependence measured across lags.
5. **[Autocorrelation Function](autocorrelation_function.md)** — normalized lag dependence plus PACF ideas used for model identification.
6. **[Randomness Tests](randomness_tests.md)** — quick checks for residual randomness and remaining dependence.

## 3. Classical Linear Models

1. **[Autoregressive Models](autoregressive_models.md)** — AR models and persistence through lagged observations.
2. **[Moving Average Models](moving_average_models.md)** — MA models driven by present and past innovations.
3. **[Backward Shift Operator](backward_shift_operator.md)** — compact polynomial notation for ARMA/ARIMA models.
4. **[Invertibility](invertibility.md)** — when innovations can be represented stably from observed values.
5. **[Yule-Walker Equations](yule_walker_equations.md)** — moment equations connecting AR coefficients and autocovariances.
6. **[ARIMA Models](arima_models.md)** — differencing plus ARMA structure for nonstationary series.

## 4. Fitting, Diagnostics, and Forecasting

**[Time-Series Modeling](time_series_modeling.md)** organizes model identification, estimation, information criteria, residual checks, and model comparison. A practical workflow is:

1. plot and understand the series;
2. identify trend, seasonality, structural breaks, and variance changes;
3. assess stationarity and transform/difference when justified;
4. use ACF/PACF and domain knowledge to propose candidate models;
5. estimate model parameters with a method appropriate to the model;
6. diagnose residual dependence and distributional problems;
7. compare plausible models without choosing solely by in-sample fit;
8. evaluate forecasts on future observations using temporal validation.

Then continue to **[Forecasting](forecasting.md)** for forecast construction, uncertainty, exponential-smoothing methods, and forecast evaluation.

## 5. Extensions

- **[Regression with ARMA Errors](regression_with_arma_errors.md)** combines regression structure with serially correlated errors.
- **[Financial Time-Series Models](financial_time_series_models.md)** introduces volatility-focused models used for financial returns.

Future extensions naturally include multivariate time series, cointegration, state-space models, Kalman filtering, and causal/predictive lead-lag methods.

## Terminology

Keep three uses of “moving average” distinct:

- a **rolling mean / moving-average smoother** is a descriptive smoothing operation;
- an **MA(q) model** is a stochastic model driven by current and lagged innovations;
- **exponential smoothing** is a forecasting family with recursively updated state estimates.

## Model Assessment

Randomly shuffled train/test splits are usually inappropriate for forecasting because they can leak future information into model development. Preserve temporal order with holdout-from-the-end, expanding-window, or rolling-origin evaluation. See **[Validation and Model Selection](../resampling_and_model_assessment/validation_and_model_selection.md)** for the general assessment principles.
