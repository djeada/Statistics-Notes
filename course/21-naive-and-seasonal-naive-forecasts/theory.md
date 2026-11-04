# Theory: naive and seasonal naive forecasts

## Why benchmarks come first

A forecast error of "24 loaves" means nothing until you know what a trivial method would have achieved. Forecasting projects fail quietly when a clever model is
*worse than copying last week* and nobody checked. A **benchmark** is a method so simple that it costs nothing and needs no estimation; a model earns its
complexity only by beating it on data it has not seen. The four classical benchmarks, for history $y_1,\dots,y_T$ and horizon $h = 1,2,\dots$:

| method | forecast $\hat y_{T+h}$ | when it is hard to beat |
|---|---|---|
| **mean** | $\frac1T\sum_{t=1}^T y_t$ | stationary noise around a constant level |
| **naive** | $y_T$ | random-walk-like series (prices, levels that drift) |
| **seasonal naive** | $y_{T+h-m(k+1)},\ k=\lfloor (h-1)/m\rfloor$ | strong, stable seasonality (period $m$: 7 for daily data with a weekly cycle) |
| **drift** | $y_T + h\,\dfrac{y_T - y_1}{T-1}$ | steady trend without seasonality |

The seasonal naive rule says: "tomorrow looks like the same weekday in the last observed week". For horizons up to $m$ it uses the previous season; for $h = m+1,\dots,2m$ it
reuses the **same last observed** season again - it never uses forecasts as inputs.

## The holdout

Evaluate on data the method did not see: split the series at time $T$ into **training** ($1..T$) and **holdout/test** ($T+1..T+H$), choose methods using only the training
part, and compute errors on the holdout. Never shuffle a time series before splitting and never tune on the holdout (that is leakage: the number then measures nothing).
A single holdout is one experiment; [lesson 24](../24-backtesting-and-forecast-accuracy/theory.md) repeats it over several origins.

## Accuracy measures

With errors $e_t = y_t - \hat y_t$ on the $H$ holdout points:

$$
\text{MAE} = \frac1H\sum |e_t|,\qquad
\text{RMSE} = \sqrt{\frac1H\sum e_t^2},\qquad
\text{MAPE} = \frac1H\sum \frac{|e_t|}{|y_t|},\qquad
\text{MASE} = \frac{\text{MAE}}{\frac1{T-m}\sum_{t=m+1}^T |y_t - y_{t-m}|}.
$$

- MAE is in the units of the data and treats all errors alike; RMSE punishes large errors and is always $\ge$ MAE; the gap shows how concentrated the errors are.
- MAPE is unit-free but explodes when actual values are near zero, and penalizes over-forecasts less than under-forecasts relative to the same absolute error.
- MASE scales by the in-sample error of the (seasonal) naive method: below 1 means better than that benchmark did in the past; comparable across series.
- The **mean error** $\frac1H\sum e_t$ measures bias: a method with large mean error is systematically high or low.
- **Skill** relative to a benchmark: $1 - \text{MAE}_{model}/\text{MAE}_{benchmark}$.

## Worked example (computed)

Period $m = 3$. History $y_1..y_6 = 10, 14, 6, 12, 16, 8$; the next three actual values are $13, 18, 9$.

| method | forecasts | MAE | RMSE | MAPE |
|---|---|---|---|---|
| mean | 11, 11, 11 | 3.67 | 4.36 | 25.5 % |
| naive | 8, 8, 8 | 5.33 | 6.48 | 35.0 % |
| seasonal naive | 12, 16, 8 | 1.33 | 1.41 | 10.0 % |

The in-sample seasonal naive error is $(|12-10| + |16-14| + |8-6|)/3 = 2$, so the MASE of the seasonal naive forecast is $1.33/2 = 0.67$ and that of naive $5.33/2 = 2.67$.
Naive is worst because the last value (8) is the low point of the cycle; the mean ignores the cycle.

## Assumptions and when it fails

1. **Seasonal naive copies the base season, noise included.** One holiday, outage or promotion in the last season is repeated at every horizon - robustify by using the median or average of several past seasons, or by cleaning
   the anomaly first ([lesson 4](../04-outlier-detection/theory.md)).
2. **It cannot extrapolate a trend** (growing series are forecast too low); drift or a trend model is needed ([lesson 22](../22-trend-and-seasonal-regression-forecasting/theory.md)).
3. **Naive after a seasonal peak** inherits the peak: the last value of a weekly series is a poor level estimate.
4. **Choose $m$ from the data** ([lesson 7](../07-trend-seasonality-and-noise/theory.md)); a wrong period makes seasonal naive worse than the mean.

## Pitfalls in evaluation

1. Comparing models on different holdouts or horizons.
2. Reporting only RMSE or only MAPE; show at least MAE and RMSE and check bias.
3. Using a holdout that covers only a quiet period; include at least one full season, preferably several.
4. Letting the holdout influence the choice of model (leakage), then calling the result "out-of-sample".
5. Declaring success when the model beats the *mean* but not seasonal naive.

## Connections

- Seasonality and noise: [lesson 7](../07-trend-seasonality-and-noise/theory.md); smoothing methods that generalize these benchmarks: [lesson 8](../08-moving-averages-and-exponential-smoothing/theory.md) and [lesson 23](../23-exponential-smoothing-models/theory.md).
- Regression forecasts with trend and seasonal terms: [lesson 22](../22-trend-and-seasonal-regression-forecasting/theory.md); proper evaluation by rolling origin: [lesson 24](../24-backtesting-and-forecast-accuracy/theory.md); intervals: [lesson 25](../25-prediction-intervals-and-forecast-uncertainty/theory.md).
- Repo notes: [forecasting](../../notes/time_series/forecasting.md), [forecast evaluation](../../notes/time_series/forecast_evaluation.md),
  [seasonality and trends](../../notes/time_series/seasonality_and_trends.md), [metrics](../../notes/resampling_and_model_assessment/metrics.md).
