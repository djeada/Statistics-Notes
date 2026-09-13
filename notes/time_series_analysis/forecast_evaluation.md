# Forecast Evaluation and Backtesting

Forecast evaluation asks a different question from in-sample model fit: **How well would this procedure have predicted observations that were genuinely in the future at the time of fitting?**

## Preserve Temporal Order

Randomly shuffling observations breaks the information structure of a forecasting problem. A valid evaluation design keeps training observations earlier than validation or test observations.

A simple split is:

```text
training ---------------- validation -------- test
past                                      future
```

Use the validation period for model or hyperparameter selection. Reserve the test period for the final comparison.

## Rolling-Origin Evaluation

A single holdout can be noisy. Rolling-origin evaluation repeats the forecasting experiment at several historical origins.

For one-step-ahead evaluation:

```text
train [1 ........ t]       -> forecast t+1
train [1 ........ t+1]     -> forecast t+2
train [1 ........ t+2]     -> forecast t+3
```

An **expanding window** keeps all available history. A **rolling window** discards older observations and is useful when the process may change over time.

For horizon $h$, the forecast error at origin $t$ is

$$
e_{t,h} = y_{t+h} - \hat y_{t+h\mid t}.
$$

Accuracy should often be reported separately by horizon because one-step and twelve-step forecasting are different tasks.

## Baselines First

A forecasting method should beat simple benchmarks appropriate to the data. Common baselines are:

- **Naive:** $\hat y_{t+h\mid t}=y_t$.
- **Seasonal naive:** use the most recent observation from the same season.
- **Drift:** extrapolate the average change from the first to the latest observation.
- **Historical mean:** useful for stable level-only series.

A complicated model that cannot outperform a sensible baseline has not demonstrated forecasting value.

## Point Forecast Metrics

For errors $e_i=y_i-\hat y_i$:

**Mean Absolute Error**

$$
\operatorname{MAE}=\frac{1}{n}\sum_{i=1}^n |e_i|.
$$

**Root Mean Squared Error**

$$
\operatorname{RMSE}=\sqrt{\frac{1}{n}\sum_{i=1}^n e_i^2}.
$$

RMSE penalizes large misses more strongly than MAE.

**Mean Absolute Scaled Error** compares absolute forecast error with a naive in-sample scale:

$$
\operatorname{MASE}=
\frac{\frac{1}{n}\sum |e_i|}
{\frac{1}{T-m}\sum_{t=m+1}^{T}|y_t-y_{t-m}|},
$$

where $m=1$ for non-seasonal data or the seasonal period for seasonal data. MASE is scale-free and remains defined when actual values are zero.

MAPE can be useful when values are strictly positive and not close to zero, but it becomes unstable near zero and is undefined at zero. Do not use it automatically.

## Prediction Intervals

A forecasting system should communicate uncertainty, not only point predictions. For a nominal $(1-\alpha)$ interval, evaluate:

- **Coverage:** fraction of outcomes inside the interval.
- **Width:** narrower intervals are better only when coverage remains appropriate.
- **Calibration by horizon:** uncertainty should usually increase as the horizon grows.

For probabilistic forecasts, quantile or pinball loss evaluates predicted quantiles directly.

## Leakage

Common sources of time-series leakage include:

- computing normalization parameters using the full dataset;
- imputing past missing values with future observations;
- creating rolling features that accidentally include the target time;
- selecting hyperparameters using the final test period;
- using future exogenous variables that would not actually be known when the forecast is made;
- randomly shuffling observations before cross-validation.

Every feature should answer: **Would this value have been available at the forecast origin?**

## Comparing Models

Compare models on the same origins and horizons. Report both the average error and enough detail to see instability across time. A model can have a good overall MAE while failing badly during regime changes.

Information criteria such as AIC/AICc/BIC are useful for in-sample candidate selection, but they are not substitutes for out-of-sample forecast evaluation.

## Reproducible Workflow

1. Define forecast horizon and decision target.
2. Choose a realistic baseline.
3. Define expanding- or rolling-window origins.
4. Fit every candidate using only information available at each origin.
5. Record point and interval forecasts.
6. Summarize metrics by model and horizon.
7. Inspect error behavior over time, not only averages.
8. Use a final untouched test period for the last comparison.

See `scripts/time_series_analysis/forecast_backtesting.py` for a minimal expanding-window example.
