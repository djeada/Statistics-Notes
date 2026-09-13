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

## Applied practice

9. Run [forecasting_evaluation_visualizations.py](../../scripts/time_series/forecasting_evaluation_visualizations.py). Explain why the seasonal-naive benchmark can be stronger than a non-seasonal AR model.
10. Implement expanding-window and rolling-window evaluation. Compare them after introducing a simulated structural break.
11. Report MAE, RMSE, mean error, and MASE by horizon. Give a decision context in which each metric would be preferred.
12. Evaluate 80%, 95%, and 99% intervals. Report coverage and width separately.
13. Create a feature that uses a centered rolling mean and a trailing rolling mean. Demonstrate the difference at one forecast origin.
14. Forecast an external predictor separately, then propagate its uncertainty into the target forecast. Compare with using the realized future predictor as an oracle.
15. Plot errors over time and investigate whether large misses cluster around breaks, high variance, or seasonal phases.

## Reflection

Write the exact sequence executed at each forecast origin. A reader should be able to tell whether preprocessing, feature construction, tuning, model fitting, and interval construction used only past information.

## Extension tasks

16. Derive the $h$-step forecast variance for an AR(1) and calculate it for $\phi=0.5$, $\sigma^2=4$, and $h=3$.
17. Construct a forecast that has low MAE but poor interval coverage. Explain the tradeoff.
18. Compare expanding and rolling windows after changing the data-generating mean halfway through the sample.
19. Calculate MASE with a seasonal scale for a quarterly series and explain why the scale is not the test error.
20. Build a leakage audit table for a pipeline with log transformation, imputation, lagged features, and hyperparameter tuning.
21. Report a forecast by horizon and by regime instead of one overall metric.

## Submission check

State the decision loss, baseline, origin geometry, information set, metrics, interval score, and final test rule.
