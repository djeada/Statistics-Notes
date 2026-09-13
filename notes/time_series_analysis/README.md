# Time Series Analysis

This section is organized as a dependency-first learning path. The goal is to move from mathematical prerequisites and stochastic-process foundations to model identification, estimation, diagnostics, forecasting, and extensions.

## 1. Prerequisites

- **[series.md](series.md)** reviews sequences, geometric series, convergence, and mean-square convergence used in infinite AR/MA representations.
- **[difference_equations.md](difference_equations.md)** introduces difference equations used to describe dynamic systems.
- **[statistical_moments_and_time_series.md](statistical_moments_and_time_series.md)** connects means, variances, covariance, and higher moments to time-indexed data.

## 2. Foundations

- **[time_series.md](time_series.md)** introduces time-series data, dependence, trend, seasonality, exploratory plots, and the basic modeling workflow.
- **[stationarity.md](stationarity.md)** defines strict and weak stationarity and covers common stationarity and unit-root checks such as ADF and KPSS.
- **[random_walk.md](random_walk.md)** gives a central example of a non-stationary process and motivates differencing.
- **[seasonality_and_trends.md](seasonality_and_trends.md)** covers trend, seasonality, decomposition, smoothing, and detrending.
- **[autocovariance_function.md](autocovariance_function.md)** introduces lagged covariance as the basic second-order dependence measure.
- **[autocorrelation_function.md](autocorrelation_function.md)** develops ACF and PACF as normalized and conditional summaries of serial dependence.
- **[randomness_tests.md](randomness_tests.md)** collects quick checks for residual randomness, independence, and trend, including Ljung-Box-type diagnostics.

## 3. Classical Linear Models

Read these after the foundations above so that stationarity, dependence, and diagnostics are already familiar.

- **[autoregressive_models.md](autoregressive_models.md)** develops AR models and their ACF/PACF behavior.
- **[moving_average_models.md](moving_average_models.md)** develops stochastic MA(q) models. Do not confuse an MA(q) model with a rolling/moving-average smoother.
- **[backward_shift_operator.md](backward_shift_operator.md)** introduces lag/backshift notation for compact model representations.
- **[invertibility.md](invertibility.md)** explains invertibility and why an MA representation should have a unique stable AR representation.
- **[yule_walker_equations.md](yule_walker_equations.md)** derives parameter relationships for AR models from their autocovariances.
- **[arima_models.md](arima_models.md)** combines AR, differencing, MA, and seasonal structure into ARMA/ARIMA/SARIMA models.

## 4. Identification, Estimation, and Diagnostics

- **[time_series_modeling.md](time_series_modeling.md)** discusses model fitting, parameter estimation, model comparison, and residual diagnostics.

A useful workflow is:

1. Plot and understand the raw series.
2. Handle trend, seasonality, changing variance, missing values, and structural breaks.
3. Assess stationarity and difference/transform when appropriate.
4. Use ACF/PACF and domain knowledge to propose candidate models.
5. Estimate parameters and compare parsimonious candidates with criteria such as AIC/BIC.
6. Diagnose residuals; they should behave approximately like white noise.
7. Only then evaluate forecasts on data not used to fit the model.

## 5. Forecasting

- **[forecasting.md](forecasting.md)** covers forecast construction, baselines, exponential smoothing, forecast errors, and practical prediction workflows.

When evaluating forecasting methods, preserve temporal order. Prefer holdout periods, expanding-window evaluation, or rolling-origin evaluation instead of randomly shuffled train/test splits.

## 6. Extensions

- **[regression_with_arma_errors.md](regression_with_arma_errors.md)** combines regression with autocorrelated errors.
- **[financial_time_series_models.md](financial_time_series_models.md)** introduces volatility models such as ARCH/GARCH.

Future extensions that would fit naturally here include multivariate time series (VAR/cointegration), dynamic regression, and state-space/Kalman-filter models.

## Terminology Note

These notes use similar-sounding terms for different objects:

- A **rolling mean / moving-average smoother** averages observed values to smooth a series.
- An **MA(q) model** is a stochastic model in which the current value depends on current and past innovations.
- **Exponential smoothing** is a forecasting family based on recursively weighted levels/trends/seasonality.

Keeping these concepts separate avoids one of the most common sources of confusion in introductory time-series material.
