# Time-Series Exercises

These practice sets use the worked examples in [notes/time_series/](../../notes/time_series/). Keep the time order visible in every calculation: when a question asks for a forecast, state what was known at the forecast origin.

Run the numerical demonstrations that support the notes with:

    python scripts/time_series/time_series_student_visualizations.py

The script writes figures to [assets/time_series/student/](../../assets/time_series/student/) and prints checkpoints that can be used to verify hand calculations.

## Sequence

1. [Foundations](foundations.md) — sequences, recursions, moments, stochastic processes, and random walks.
2. [Dependence and identification](dependence_and_identification.md) — autocovariance, ACF/PACF, AR/MA models, stationarity, and invertibility.
3. [ARIMA and seasonality](arima_and_seasonality.md) — backshift notation, differencing, decomposition, and seasonal models.
4. [Modeling and diagnostics](modeling_and_diagnostics.md) — estimation, information criteria, residual checks, and randomness.
5. [Forecasting and evaluation](forecasting_and_evaluation.md) — baselines, intervals, rolling origins, and leakage.
6. [Dynamic regression](dynamic_regression.md) — lagged predictors, dynamic errors, and future information.
7. [Multivariate models](multivariate.md) — VAR, Granger predictability, cointegration, and VECM.
8. [State space](state_space.md) — filtering, smoothing, missing values, and Kalman updates.
9. [Frequency and volatility](frequency_and_volatility.md) — spectra, aliasing, returns, and conditional variance.

The first five sets build the univariate foundation. The final four apply the same ideas to external predictors, systems of series, latent states, and changing variance.

## How to use the figures

Each topic has a companion program in [scripts/time_series/README.md](../../scripts/time_series/README.md). Run the relevant program before answering the applied questions, then change one parameter and describe which part of the figure changes.

| Practice set | Companion program |
|---|---|
| Foundations | [foundations_visualizations.py](../../scripts/time_series/foundations_visualizations.py) |
| Dependence and identification | [dependence_visualizations.py](../../scripts/time_series/dependence_visualizations.py) |
| ARIMA and seasonality | [arima_seasonality_visualizations.py](../../scripts/time_series/arima_seasonality_visualizations.py) |
| Modeling and diagnostics | [diagnostics_visualizations.py](../../scripts/time_series/diagnostics_visualizations.py) |
| Forecasting and evaluation | [forecasting_evaluation_visualizations.py](../../scripts/time_series/forecasting_evaluation_visualizations.py) |
| Dynamic and multivariate models | [dynamic_multivariate_visualizations.py](../../scripts/time_series/dynamic_multivariate_visualizations.py) |
| State space | [state_space_frequency_visualizations.py](../../scripts/time_series/state_space_frequency_visualizations.py) |
| Frequency and volatility | [state_space_frequency_visualizations.py](../../scripts/time_series/state_space_frequency_visualizations.py), [financial_time_series_visualizations.py](../../scripts/time_series/financial_time_series_visualizations.py) |

For a complete submission, include the equation used to generate a simulation, the numerical calculation, the figure, and an interpretation that states the assumptions and information available at the forecast origin.
