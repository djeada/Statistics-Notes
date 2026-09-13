# Time-Series Figure Catalog

The time-series notes use deterministic synthetic figures so the calculations can be reproduced without downloading a data source.

## Existing unit figures

The original unit figures remain directly under this directory. They cover introductory series, ACF/PACF, differencing, decomposition, smoothing, turning points, and volatility.

## Student-pack figures

The expanded chapter companions write eight figures per topic:

| Directory | Topics |
|---|---|
| [foundations/](foundations/) | series, recursions, components, moments, sampling, stationarity |
| [dependence/](dependence/) | autocovariance, ACF/PACF, AR/MA persistence, backshift, invertibility |
| [arima_seasonality/](arima_seasonality/) | differencing, decomposition, ARIMA forecasts, seasonal naive, order selection |
| [diagnostics/](diagnostics/) | detrending, residual checks, variance, breaks, temporal splits |
| [forecasting/](forecasting/) | baselines, rolling origins, metrics, intervals, leakage |
| [dynamic_multivariate/](dynamic_multivariate/) | dynamic regression, VAR, Granger predictability, VECM, impulses |
| [state_space_frequency/](state_space_frequency/) | Kalman filtering, missing data, spectra, aliasing, coherence |
| [financial/](financial/) | returns, ARCH/GARCH, leverage, persistence, tails |

Generate them from the repository root with the topic programs in [scripts/time_series/](../../scripts/time_series/README.md). Each script uses a fixed random seed and prints the numerical checkpoints used in the corresponding notes.
