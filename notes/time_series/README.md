# Time Series

Time-series methods extend the core statistics curriculum to observations indexed by time, where serial dependence, trend, seasonality, and changing variance make independent-sample methods inadequate.

## Prerequisites

Before starting this unit, be comfortable with:

- **[Joint Distributions & Covariance](../joint_distributions_and_covariance/README.md)** — covariance, correlation, and dependence;
- **[Regression](../regression/README.md)** — fitted models, residuals, and regression inference;
- **[Resampling & Model Assessment](../resampling_and_model_assessment/README.md)** — out-of-sample evaluation and leakage;
- basic algebra of sequences and difference equations.

## 1. Mathematical and Stochastic Foundations

1. **[Series](series.md)** — sequences, series, convergence, and manipulations used in linear-process representations.
2. **[Difference Equations](difference_equations.md)** — recursive equations behind dynamic models.
3. **[Time Series](time_series.md)** — what makes time-indexed data different from ordinary cross-sectional data.
4. **[Statistical Moments and Time Series](statistical_moments_and_time_series.md)** — means, variances, covariance, and higher moments in the time-indexed setting.
5. **[Stochastic Processes and White Noise](stochastic_processes_and_white_noise.md)** — sample paths, innovations, weak white noise, and the probabilistic foundation for ARMA-type models.

## 2. Dependence and Stationarity

1. **[Stationarity](stationarity.md)** — stability conditions that make many classical models interpretable.
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

## 4. Fitting and Diagnostics

**[Time-Series Modeling](time_series_modeling.md)** organizes identification, estimation, information criteria, residual checks, and model comparison. A disciplined workflow is: understand the series, handle structural features, assess stationarity, propose parsimonious candidates, estimate with a method appropriate to the model, diagnose residuals, and compare candidates without choosing solely by in-sample fit.

Use the same workflow for every model class:

1. define the forecast target, time origin, and horizon;
2. inspect the series for missing values, outliers, trend, seasonality, breaks, and changing variance;
3. transform or difference only when the model and question require it;
4. fit a small set of plausible candidates;
5. check residual dependence and variance;
6. evaluate the complete forecasting procedure on future-like origins.

## 5. Forecasting and Evaluation

1. **[Forecasting](forecasting.md)** — forecast construction, uncertainty, exponential smoothing, and forecast intervals.
2. **[Forecast Evaluation and Backtesting](forecast_evaluation.md)** — temporal train/validation/test design, rolling-origin evaluation, baselines, MAE/RMSE/MASE, interval calibration, and leakage.

Randomly shuffled train/test splits are usually inappropriate for forecasting because they can leak future information into model development. Preserve temporal order with holdout-from-the-end, expanding-window, or rolling-origin evaluation.

## 6. Extensions

1. **[Dynamic Regression](dynamic_regression.md)** — external predictors with ARMA/ARIMA error structure and future-regressor availability.
2. **[Regression with ARMA Errors](regression_with_arma_errors.md)** — a shorter focused treatment of serially correlated regression errors.
3. **[Multivariate Time Series](multivariate_time_series.md)** — VAR, Granger predictability, cointegration, and VECM.
4. **[State-Space Models and the Kalman Filter](state_space_models.md)** — latent-state models, filtering, smoothing, missing observations, and likelihood.
5. **[Frequency-Domain Analysis](frequency_domain_analysis.md)** — periodograms, spectra, aliasing, leakage, and coherence.
6. **[Financial Time-Series Models](financial_time_series_models.md)** — volatility-focused models for financial returns.

## Practice

The [time-series exercise path](../../exercises/time_series/README.md) follows the sections above:

1. foundations and stationarity;
2. ACF/PACF and ARMA identification;
3. ARIMA and seasonality;
4. forecasting and temporal evaluation;
5. dynamic regression;
6. multivariate models;
7. state-space models;
8. frequency-domain analysis and volatility.

Each set links back to the relevant notes and to a small implementation where one is available. The exercises are designed to be solved with simulated data first, so the information available at the forecast origin is explicit.

## Companion Implementations

- [scripts/time_series/](../../scripts/time_series/) contains runnable examples from white noise through forecast backtesting, VAR/VECM, Kalman filtering, and periodograms.
- [notebooks/time_series/](../../notebooks/time_series/) contains interactive notebooks for foundations, backtesting, dynamic regression, and advanced state-space/frequency-domain ideas.
- The visualization scripts in [scripts/time_series/](../../scripts/time_series/) write deterministic teaching figures to [assets/time_series/](../../assets/time_series/) when the scientific Python dependencies are installed.

The expanded chapters use these topic companions:

| Chapter family | Script | Figures |
|---|---|---|
| foundations and stationarity | [foundations_visualizations.py](../../scripts/time_series/foundations_visualizations.py) | [foundations](../../assets/time_series/foundations/) |
| dependence and diagnostics | [dependence_visualizations.py](../../scripts/time_series/dependence_visualizations.py), [diagnostics_visualizations.py](../../scripts/time_series/diagnostics_visualizations.py) | [dependence](../../assets/time_series/dependence/), [diagnostics](../../assets/time_series/diagnostics/) |
| ARIMA and seasonality | [arima_seasonality_visualizations.py](../../scripts/time_series/arima_seasonality_visualizations.py) | [arima_seasonality](../../assets/time_series/arima_seasonality/) |
| forecasting and evaluation | [forecasting_evaluation_visualizations.py](../../scripts/time_series/forecasting_evaluation_visualizations.py) | [forecasting](../../assets/time_series/forecasting/) |
| dynamic and multivariate models | [dynamic_multivariate_visualizations.py](../../scripts/time_series/dynamic_multivariate_visualizations.py) | [dynamic_multivariate](../../assets/time_series/dynamic_multivariate/) |
| state space and frequency | [state_space_frequency_visualizations.py](../../scripts/time_series/state_space_frequency_visualizations.py) | [state_space_frequency](../../assets/time_series/state_space_frequency/) |
| financial models | [financial_time_series_visualizations.py](../../scripts/time_series/financial_time_series_visualizations.py) | [financial](../../assets/time_series/financial/) |

## Model Selection Map

| Data feature or question | Useful starting point | Check before interpreting |
|---|---|---|
| Stable mean with short-memory dependence | AR, MA, or ARMA | stationarity, invertibility, residual ACF |
| Trend or unit-root behavior | differencing, ARIMA, or state space | whether differencing removed the useful long-run signal |
| Regular seasonal pattern | seasonal naive, ETS, or SARIMA | seasonal period, seasonal leakage, horizon |
| External predictors | dynamic regression | availability of future predictors and residual dependence |
| Several interacting series | VAR or VECM | stationarity, cointegration, lag count, stability |
| Latent level, missing observations, or changing signal | state-space model | filtering versus smoothing and innovation diagnostics |
| Cycles whose periods matter | spectral analysis | sampling rate, aliasing, leakage, detrending |
| Changing conditional variance | ARCH/GARCH family | heavy tails, leverage effects, and risk horizon |

## Terminology

Keep three uses of “moving average” distinct:

- a **rolling mean / moving-average smoother** is a descriptive smoothing operation;
- an **MA(q) model** is a stochastic model driven by current and lagged innovations;
- **exponential smoothing** is a forecasting family with recursively updated state estimates.
