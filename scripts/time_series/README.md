# Time Series Scripts

## Student worked figures

Run the master visualization script from the repository root:

    python scripts/time_series/time_series_student_visualizations.py

It prints the numerical checkpoints used in the notes and writes the new figures to [assets/time_series/student/](../../assets/time_series/student/). Existing figures in [assets/time_series/](../../assets/time_series/) are retained and reused by the notes.

| Topic | Existing example | Worked-figure script |
|---|---|---|
| Foundations | [white_noise.py](white_noise.py), [random_walk.py](random_walk.py) | [time_series_student_visualizations.py](time_series_student_visualizations.py) |
| Dependence and ARMA | [autocorrelation_function.py](autocorrelation_function.py), [autoregressive_model.py](autoregressive_model.py), [moving_average.py](moving_average.py) | [time_series_student_visualizations.py](time_series_student_visualizations.py) |
| ARIMA and seasonality | [arima_inflation.py](arima_inflation.py), [sarima_mock.py](sarima_mock.py) | [time_series_student_visualizations.py](time_series_student_visualizations.py) |
| Forecasting | [forecast_backtesting.py](forecast_backtesting.py), [exponential_smoothing_temp.py](exponential_smoothing_temp.py) | [time_series_student_visualizations.py](time_series_student_visualizations.py) |
| Dynamic and multivariate models | [dynamic_regression.py](dynamic_regression.py), [var_and_cointegration.py](var_and_cointegration.py) | [time_series_student_visualizations.py](time_series_student_visualizations.py) |
| State space and frequency | [kalman_filter.py](kalman_filter.py), [frequency_domain.py](frequency_domain.py) | [time_series_student_visualizations.py](time_series_student_visualizations.py) |
| Financial volatility | [sma_ema_stocks.py](sma_ema_stocks.py) | [time_series_student_visualizations.py](time_series_student_visualizations.py) |

The scripts that fit statistical models need the dependencies listed in the repository requirements. The worked-figure script intentionally keeps its calculations explicit and only requires NumPy and Matplotlib.

## Topic visualization programs

The expanded student chapters use one script per topic. Each program computes the numerical examples printed in its terminal output and writes eight figures to a topic directory.

| Visualization script | Main lesson | Figure output |
|---|---|---|
| [foundations_visualizations.py](foundations_visualizations.py) | series, recursions, components, moments, sampling, and stationarity | [assets/time_series/foundations/](../../assets/time_series/foundations/) |
| [dependence_visualizations.py](dependence_visualizations.py) | covariance, ACF/PACF, AR/MA persistence, backshift, invertibility, and randomness | [assets/time_series/dependence/](../../assets/time_series/dependence/) |
| [arima_seasonality_visualizations.py](arima_seasonality_visualizations.py) | differencing, decomposition, ARIMA forecasts, seasonal naive, and order selection | [assets/time_series/arima_seasonality/](../../assets/time_series/arima_seasonality/) |
| [diagnostics_visualizations.py](diagnostics_visualizations.py) | detrending, residual checks, variance, breaks, and temporal splits | [assets/time_series/diagnostics/](../../assets/time_series/diagnostics/) |
| [forecasting_evaluation_visualizations.py](forecasting_evaluation_visualizations.py) | baselines, rolling origins, intervals, metrics, leakage, and horizon error | [assets/time_series/forecasting/](../../assets/time_series/forecasting/) |
| [dynamic_multivariate_visualizations.py](dynamic_multivariate_visualizations.py) | dynamic regression, VAR feedback, Granger predictability, VECM, and impulses | [assets/time_series/dynamic_multivariate/](../../assets/time_series/dynamic_multivariate/) |
| [state_space_frequency_visualizations.py](state_space_frequency_visualizations.py) | Kalman filtering, missing data, spectra, leakage, aliasing, and coherence | [assets/time_series/state_space_frequency/](../../assets/time_series/state_space_frequency/) |
| [financial_time_series_visualizations.py](financial_time_series_visualizations.py) | returns, ARCH/GARCH, leverage, persistence, and heavy tails | [assets/time_series/financial/](../../assets/time_series/financial/) |

Run any script from the repository root, for example:

    python scripts/time_series/forecasting_evaluation_visualizations.py

The scripts use deterministic random seeds. They are teaching simulations rather than fitted analyses of a real data source, so changing the seed or sample length is a useful exercise.

Runnable examples for [`notes/time_series`](../../notes/time_series/README.md).

The directory progresses from white noise, random walks, stationarity, ACF and AR models through smoothing/ARIMA, then to forecast backtesting, dynamic regression, VAR/cointegration, state-space filtering, and frequency-domain analysis. For evaluation, prefer the temporal backtesting examples over shuffled cross-validation.
