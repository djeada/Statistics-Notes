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

Runnable examples for [`notes/time_series`](../../notes/time_series/README.md).

The directory progresses from white noise, random walks, stationarity, ACF and AR models through smoothing/ARIMA, then to forecast backtesting, dynamic regression, VAR/cointegration, state-space filtering, and frequency-domain analysis. For evaluation, prefer the temporal backtesting examples over shuffled cross-validation.
