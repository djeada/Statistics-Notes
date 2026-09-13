# Forecast Evaluation and Backtesting

## Worked calculation: three errors and one scale

Suppose the actual values are $(10,12,9)$ and forecasts are $(9,11,10)$. The errors $y-\hat y$ are $(1,1,-1)$, so

$$
\operatorname{MAE}=\frac{1+1+1}{3}=1,
\qquad
\operatorname{RMSE}=\sqrt{\frac{1+1+1}{3}}=1.
$$

If the in-sample naive scale is $2$, then

$$
\operatorname{MASE}=\frac{1}{2}=0.5.
$$

The scale must be calculated using only the training portion at each origin. Reusing a scale computed from the full series is a small but real form of leakage. A rolling-origin evaluation repeats this calculation after each training window so that every forecast is made with past information only.

![Rolling-origin forecasts and forecast errors](../../assets/time_series/student/15_forecast_backtesting.png)

Forecast evaluation asks a different question from in-sample fit: **How well would this procedure have predicted observations that were genuinely in the future at the time of fitting?**

## Preserve Temporal Order

Randomly shuffling observations breaks the information structure of a forecasting problem. A valid evaluation design keeps training observations earlier than validation or test observations. Use validation data for model or hyperparameter selection and reserve the final test period for the last comparison.

## Rolling-Origin Evaluation

A single holdout can be noisy. Rolling-origin evaluation repeats the forecasting experiment at several historical origins. An **expanding window** keeps all available history; a **rolling window** discards older observations and is useful when the process may change.

For horizon $h$, the forecast error at origin $t$ is

$$
e_{t,h}=y_{t+h}-\hat y_{t+h\mid t}.
$$

Report accuracy by horizon when the decision problem distinguishes short- and long-horizon forecasts.

## Baselines First

Useful baselines include naive, seasonal-naive, drift, and historical-mean forecasts. A complicated model that cannot outperform a sensible baseline has not demonstrated forecasting value.

## Point Forecast Metrics

For errors $e_i=y_i-\hat y_i$:

$$
\operatorname{MAE}=\frac{1}{n}\sum |e_i|,
\qquad
\operatorname{RMSE}=\sqrt{\frac{1}{n}\sum e_i^2}.
$$

Mean Absolute Scaled Error compares absolute forecast error with a naive in-sample scale:

$$
\operatorname{MASE}=
\frac{\frac{1}{n}\sum |e_i|}
{\frac{1}{T-m}\sum_{t=m+1}^{T}|y_t-y_{t-m}|}.
$$

MAPE can be useful when values are strictly positive and not near zero, but it is unstable near zero and undefined at zero.

## Prediction Intervals

Evaluate interval forecasts with coverage, width, and calibration by horizon. For probabilistic forecasts, quantile or pinball loss evaluates predicted quantiles directly.

## Leakage

Common sources include full-data normalization, future-aware imputation, rolling features that include the target time, selecting hyperparameters on the final test period, using future exogenous values that would not be known at the forecast origin, and shuffled cross-validation.

Every feature should answer: **Would this value have been available at the forecast origin?**

Information criteria such as AIC/AICc/BIC are useful for in-sample candidate selection, but they are not substitutes for out-of-sample forecast evaluation.

See [`forecast_backtesting.py`](../../scripts/time_series/forecast_backtesting.py) and the companion [forecast-backtesting notebook](../../notebooks/time_series/forecast_backtesting.ipynb).
