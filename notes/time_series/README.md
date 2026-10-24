# Time Series

Time-series analysis studies observations whose order carries information. A high value followed by another high value suggests a different mechanism from the same values alternating above and below a mean. Trends and seasonal patterns change expected values across dates; serial dependence connects deviations across dates; variance dynamics change the scale of uncertainty. A useful model distinguishes those features instead of treating every visible pattern as one kind of correlation.

The mathematical foundations below explain how recursions and weighted shock histories create temporal behavior. The linear-model chapters turn that behavior into AR, MA, ARIMA, and seasonal equations. Estimation and diagnostics then ask whether those equations describe the observed series adequately. Forecasting adds a dated information boundary and tests what the complete procedure predicts beyond its training record.

## The main modeling distinctions

**Levels and changes** answer different questions. A random-walk level accumulates shocks permanently, while its first difference recovers the new increment. Differencing can therefore make the dynamic equation stationary without making the original level stationary. Returning to level forecasts requires reversing the transformation and propagating the resulting uncertainty.

**Observed lags and latent shocks** distinguish AR and MA mechanisms. An AR coefficient feeds an earlier observed value back into the recursion. An MA coefficient carries a particular innovation forward for a finite number of dates. Both can create serial dependence, but their estimation and covariance patterns differ because only the observed lags are directly present in the dataset.

**A regression component and an innovation** are not the same object. External predictors can explain part of the response while leaving a correlated regression error. A dynamic error equation then predicts part of that error, leaving a new innovation. Diagnostics and forecasts need to use the appropriate sequence.

**Historical reconstruction and forecasting** use different information. A centered smoother or a smoothed latent state can use later observations to estimate an earlier quantity. A forecast issued at that earlier date cannot. Chronological evaluation must reproduce the entire information restriction, including transformations, predictor availability, estimation, and model selection.

## Notation and conventions

| Symbol or term | Meaning in these notes | What to check |
|---|---|---|
| $X_t$ and $x_t$ | A random variable and its observed realization at time $t$. | A single observed path does not show every feature of the process distribution. |
| $\varepsilon_t$, $\epsilon_t$, $Z_t$, or $w_t$ | Shocks or innovations, according to the equation in the chapter. | Weak white noise, independent noise, and conditional-mean innovations impose different assumptions. |
| $\mu$ and $c$ | Process mean and model intercept. | For an AR model they are generally different quantities. |
| $B$, $\Delta$, and $\nabla$ | Backshift and differencing operators. | $BX_t=X_{t-1}$; $\Delta X_t=\nabla X_t=X_t-X_{t-1}$. |
| $\gamma(h)$ and $\rho(h)$ | Population autocovariance and autocorrelation at lag $h$. | Hats or sample coefficients denote estimates; state their denominator convention. |
| $\mathcal F_t$ and $\hat X_{t+h\mid t}$ | Information available at origin $t$, and a forecast $h$ steps ahead from that origin. | Predictors, transformations, and parameter estimates must respect the same information boundary. |
| AR and MA roots | Zeros of a lag polynomial in a variable such as $z$. | Stable causal AR and invertible MA polynomials have zeros outside the unit circle; time-recursion roots use the reciprocal convention. |

The usual MA convention here is $\theta(B)=1+\theta_1B+\cdots+\theta_qB^q$, but a few examples explicitly use minus-signed coefficients. Compare expanded equations before comparing coefficient values across chapters or software. The formula tables are references to the assumptions explained in the text, rather than formulas that apply to every series without qualification.

## Prerequisites

Before starting this unit, be comfortable with:

- **[Joint Distributions & Covariance](https://github.com/djeada/Statistics-Notes/tree/main/notes/joint_distributions_and_covariance)** — covariance, correlation, and dependence;
- **[Regression](https://github.com/djeada/Statistics-Notes/tree/main/notes/regression)** — fitted models, residuals, and regression inference;
- **[Resampling & Model Assessment](https://github.com/djeada/Statistics-Notes/tree/main/notes/resampling_and_model_assessment)** — out-of-sample evaluation and leakage;
- basic algebra of sequences and difference equations.

## 1. Mathematical and Stochastic Foundations

1. **[Series](https://github.com/djeada/Statistics-Notes/blob/main/notes/time_series/series.md)** — sequences, series, convergence, and manipulations used in linear-process representations.
2. **[Difference Equations](https://github.com/djeada/Statistics-Notes/blob/main/notes/time_series/difference_equations.md)** — recursive equations behind dynamic models.
3. **[Time Series](https://github.com/djeada/Statistics-Notes/blob/main/notes/time_series/time_series.md)** — what makes time-indexed data different from ordinary cross-sectional data.
4. **[Statistical Moments and Time Series](https://github.com/djeada/Statistics-Notes/blob/main/notes/time_series/statistical_moments_and_time_series.md)** — means, variances, covariance, and higher moments in the time-indexed setting.
5. **[Stochastic Processes and White Noise](https://github.com/djeada/Statistics-Notes/blob/main/notes/time_series/stochastic_processes_and_white_noise.md)** — sample paths, innovations, weak white noise, and the probabilistic foundation for ARMA-type models.

## 2. Dependence and Stationarity

1. **[Stationarity](https://github.com/djeada/Statistics-Notes/blob/main/notes/time_series/stationarity.md)** — stability conditions that make many classical models interpretable.
2. **[Random Walk](https://github.com/djeada/Statistics-Notes/blob/main/notes/time_series/random_walk.md)** — the canonical nonstationary process and a bridge to unit-root ideas.
3. **[Seasonality and Trends](https://github.com/djeada/Statistics-Notes/blob/main/notes/time_series/seasonality_and_trends.md)** — deterministic and stochastic structure that must be handled before model identification.
4. **[Autocovariance Function](https://github.com/djeada/Statistics-Notes/blob/main/notes/time_series/autocovariance_function.md)** — dependence measured across lags.
5. **[Autocorrelation Function](https://github.com/djeada/Statistics-Notes/blob/main/notes/time_series/autocorrelation_function.md)** — normalized lag dependence plus PACF ideas used for model identification.
6. **[Randomness Tests](https://github.com/djeada/Statistics-Notes/blob/main/notes/time_series/randomness_tests.md)** — quick checks for residual randomness and remaining dependence.

## 3. Classical Linear Models

1. **[Autoregressive Models](https://github.com/djeada/Statistics-Notes/blob/main/notes/time_series/autoregressive_models.md)** — AR models and persistence through lagged observations.
2. **[Moving Average Models](https://github.com/djeada/Statistics-Notes/blob/main/notes/time_series/moving_average_models.md)** — MA models driven by present and past innovations.
3. **[Backward Shift Operator](https://github.com/djeada/Statistics-Notes/blob/main/notes/time_series/backward_shift_operator.md)** — compact polynomial notation for ARMA/ARIMA models.
4. **[Invertibility](https://github.com/djeada/Statistics-Notes/blob/main/notes/time_series/invertibility.md)** — when innovations can be represented stably from observed values.
5. **[Yule-Walker Equations](https://github.com/djeada/Statistics-Notes/blob/main/notes/time_series/yule_walker_equations.md)** — moment equations connecting AR coefficients and autocovariances.
6. **[ARIMA Models](https://github.com/djeada/Statistics-Notes/blob/main/notes/time_series/arima_models.md)** — differencing plus ARMA structure for nonstationary series.

## 4. Fitting and Diagnostics

**[Time-Series Modeling](https://github.com/djeada/Statistics-Notes/blob/main/notes/time_series/time_series_modeling.md)** organizes identification, estimation, information criteria, residual checks, and model comparison. A disciplined workflow is: understand the series, handle structural features, assess stationarity, propose parsimonious candidates, estimate with a method appropriate to the model, diagnose residuals, and compare candidates without choosing solely by in-sample fit.

Use the same workflow for every model class:

1. define the forecast target, time origin, and horizon;
2. inspect the series for missing values, outliers, trend, seasonality, breaks, and changing variance;
3. transform or difference only when the model and question require it;
4. fit a small set of plausible candidates;
5. check residual dependence and variance;
6. evaluate the complete forecasting procedure at historical forecast origins, using only information available at each date.

## 5. Forecasting and Evaluation

1. **[Forecasting](https://github.com/djeada/Statistics-Notes/blob/main/notes/time_series/forecasting.md)** — forecast construction, uncertainty, exponential smoothing, and forecast intervals.
2. **[Forecast Evaluation and Backtesting](https://github.com/djeada/Statistics-Notes/blob/main/notes/time_series/forecast_evaluation.md)** — temporal train/validation/test design, rolling-origin evaluation, baselines, MAE/RMSE/MASE, interval calibration, and leakage.

Randomly shuffled train/test splits are usually inappropriate for forecasting because they can leak future information into model development. Preserve temporal order with holdout-from-the-end, expanding-window, or rolling-origin evaluation.

## 6. Extensions

1. **[Dynamic Regression](https://github.com/djeada/Statistics-Notes/blob/main/notes/time_series/dynamic_regression.md)** — external predictors with ARMA/ARIMA error structure and future-regressor availability.
2. **[Regression with ARMA Errors](https://github.com/djeada/Statistics-Notes/blob/main/notes/time_series/regression_with_arma_errors.md)** — a shorter focused treatment of serially correlated regression errors.
3. **[Multivariate Time Series](https://github.com/djeada/Statistics-Notes/blob/main/notes/time_series/multivariate_time_series.md)** — VAR, Granger predictability, cointegration, and VECM.
4. **[State-Space Models and the Kalman Filter](https://github.com/djeada/Statistics-Notes/blob/main/notes/time_series/state_space_models.md)** — latent-state models, filtering, smoothing, missing observations, and likelihood.
5. **[Frequency-Domain Analysis](https://github.com/djeada/Statistics-Notes/blob/main/notes/time_series/frequency_domain_analysis.md)** — periodograms, spectra, aliasing, leakage, and coherence.
6. **[Financial Time-Series Models](https://github.com/djeada/Statistics-Notes/blob/main/notes/time_series/financial_time_series_models.md)** — volatility-focused models for financial returns.

## Practice

The [time-series exercise path](https://github.com/djeada/Statistics-Notes/tree/main/exercises/time_series) follows the sections above:

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

- [scripts/time_series/](https://github.com/djeada/Statistics-Notes/tree/main/scripts/time_series) contains runnable examples from white noise through forecast backtesting, VAR/VECM, Kalman filtering, and periodograms.
- [notebooks/time_series/](https://github.com/djeada/Statistics-Notes/tree/main/notebooks/time_series) contains interactive notebooks for foundations, backtesting, dynamic regression, and advanced state-space/frequency-domain ideas.
- The visualization scripts in [scripts/time_series/](https://github.com/djeada/Statistics-Notes/tree/main/scripts/time_series) write deterministic teaching figures to [assets/time_series/](https://raw.githubusercontent.com/djeada/Statistics-Notes/main/assets/time_series) when the scientific Python dependencies are installed.

The expanded chapters use these topic companions:

| Chapter family | Script | Figures |
|---|---|---|
| foundations and stationarity | [foundations_visualizations.py](https://github.com/djeada/Statistics-Notes/blob/main/scripts/time_series/foundations_visualizations.py) | [foundations](https://raw.githubusercontent.com/djeada/Statistics-Notes/main/assets/time_series/foundations) |
| dependence and diagnostics | [dependence_visualizations.py](https://github.com/djeada/Statistics-Notes/blob/main/scripts/time_series/dependence_visualizations.py), [diagnostics_visualizations.py](https://github.com/djeada/Statistics-Notes/blob/main/scripts/time_series/diagnostics_visualizations.py) | [dependence](https://raw.githubusercontent.com/djeada/Statistics-Notes/main/assets/time_series/dependence), [diagnostics](https://raw.githubusercontent.com/djeada/Statistics-Notes/main/assets/time_series/diagnostics) |
| ARIMA and seasonality | [arima_seasonality_visualizations.py](https://github.com/djeada/Statistics-Notes/blob/main/scripts/time_series/arima_seasonality_visualizations.py) | [arima_seasonality](https://raw.githubusercontent.com/djeada/Statistics-Notes/main/assets/time_series/arima_seasonality) |
| forecasting and evaluation | [forecasting_evaluation_visualizations.py](https://github.com/djeada/Statistics-Notes/blob/main/scripts/time_series/forecasting_evaluation_visualizations.py) | [forecasting](https://raw.githubusercontent.com/djeada/Statistics-Notes/main/assets/time_series/forecasting) |
| dynamic and multivariate models | [dynamic_multivariate_visualizations.py](https://github.com/djeada/Statistics-Notes/blob/main/scripts/time_series/dynamic_multivariate_visualizations.py) | [dynamic_multivariate](https://raw.githubusercontent.com/djeada/Statistics-Notes/main/assets/time_series/dynamic_multivariate) |
| state space and frequency | [state_space_frequency_visualizations.py](https://github.com/djeada/Statistics-Notes/blob/main/scripts/time_series/state_space_frequency_visualizations.py) | [state_space_frequency](https://raw.githubusercontent.com/djeada/Statistics-Notes/main/assets/time_series/state_space_frequency) |
| financial models | [financial_time_series_visualizations.py](https://github.com/djeada/Statistics-Notes/blob/main/scripts/time_series/financial_time_series_visualizations.py) | [financial](https://raw.githubusercontent.com/djeada/Statistics-Notes/main/assets/time_series/financial) |

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

## Formula reference

| Topic | General formula | Notes / common special case |
|---|---|---|
| Mean | $\mu_t=E[X_t]$ | Weak stationarity requires $\mu_t=\mu$ for all $t$. |
| Autocovariance | $\gamma(t,s)=\mathrm{Cov}(X_t,X_s)$ | For a weakly stationary process, $\gamma(t,s)=\gamma(t-s)$. |
| Autocorrelation | $\rho(h)=\gamma(h)/\gamma(0)$ | $\rho(0)=1$ and $\rho(-h)=\rho(h)$. |
| Backshift | $B^kX_t=X_{t-k}$ | $\nabla X_t=(1-B)X_t$ and $\nabla_sX_t=(1-B^s)X_t$. |
| AR($p$) | $X_t=c+\sum_{i=1}^{p}\phi_iX_{t-i}+\varepsilon_t$ | AR(1): $X_t=c+\phi X_{t-1}+\varepsilon_t$. |
| MA($q$) | $X_t=\mu+\varepsilon_t+\sum_{j=1}^{q}\theta_j\varepsilon_{t-j}$ | MA(1): $X_t=\mu+\varepsilon_t+\theta\varepsilon_{t-1}$. |
| ARMA($p,q$) | $\phi(B)(X_t-\mu)=\theta(B)\varepsilon_t$ | AR and MA are obtained by setting $q=0$ or $p=0$. |
| ARIMA($p,d,q$) | $\phi(B)(1-B)^dX_t=c+\theta(B)\varepsilon_t$ | Random walk: ARIMA$(0,1,0)$; ARMA: ARIMA$(p,0,q)$. |
| SARIMA | $\Phi(B^s)\phi(B)(1-B^s)^D(1-B)^dX_t=\Theta(B^s)\theta(B)\varepsilon_t$ | Seasonal period is $s$; setting $P=D=Q=0$ gives non-seasonal ARIMA. |
| Forecast error | $e_{t+h\mid t}=X_{t+h}-\hat X_{t+h\mid t}$ | MSE $=n^{-1}\sum e_t^2$; RMSE $=\sqrt{\mathrm{MSE}}$. |
| State space | $\alpha_t=T_t\alpha_{t-1}+R_t\eta_t$, $\;X_t=Z_t\alpha_t+\varepsilon_t$ | Kalman filtering recursively updates the latent state. |
