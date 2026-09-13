# Forecasting and Evaluation

Read [forecasting](../../notes/time_series/forecasting.md) and [forecast evaluation](../../notes/time_series/forecast_evaluation.md).

1. For $X_t=0.8X_{t-1}+\varepsilon_t$, $X_T=5$, and innovation variance 1, calculate the one-step and five-step conditional-mean forecasts.
2. Calculate the two-step forecast variance. Explain why it is larger than the one-step variance.
3. Actual values are $(10,12,9)$ and forecasts are $(9,11,10)$. Calculate MAE, RMSE, and MASE when the training naive scale is 2.
4. Implement naive, seasonal-naive, and AR forecasts. Use expanding-window origins and compare errors by horizon.
5. Draw a rolling-origin diagram for a three-step-ahead forecast. Mark which observations are available at each origin.
6. Give four examples of time-series leakage involving normalization, imputation, rolling features, or exogenous variables.
7. Construct a case where MAPE is undefined or misleading because actual values are zero or close to zero.
8. For nominal 95% intervals, calculate empirical coverage from 20 forecast intervals. Explain why coverage alone is not enough without interval width.

## Checks

- The one-step forecast is 4 and the five-step forecast is $0.8^5(5)=1.6384$.
- The two-step forecast variance is $1+0.8^2=1.64$.
- MAE and RMSE are both 1; MASE is $0.5$.
- The final test period must remain untouched while model choices are made.
