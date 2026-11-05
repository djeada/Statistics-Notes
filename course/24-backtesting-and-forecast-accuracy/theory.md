# Theory: backtesting and forecast accuracy

## Why this matters

A forecast model is only as good as the evidence that it works on data it has not seen. In-sample fit measures how well you
described the past; it says nothing about how wrong you will be next week. **Backtesting** replays history as if you were
forecasting in real time, so that the accuracy you measure is the accuracy you would have had. The two ways this goes wrong
are *leakage* (the evaluation secretly uses the future) and *luck* (one lucky holdout period picks the wrong model).

## Forecast origin, horizon, error

- The **origin** $T$ is the last observation available when the forecast is made; the **horizon** $h$ says how far ahead:
  $\hat y_{T+h\mid T}$ uses only $y_1,\dots,y_T$ (and anything known in advance, such as the calendar).
- The **forecast error** is $e_{T+h} = y_{T+h} - \hat y_{T+h\mid T}$ (actual minus forecast). Positive = under-forecast.

## Rolling-origin (time-series cross-validation)

Choose a first origin $T_0$ with enough history, forecast the next $H$ days, then move the origin forward and repeat:

1. **Expanding window**: the training set at origin $T$ is $y_1..y_T$ (it grows).
2. **Sliding window**: only the last $W$ observations are used (constant size); better when the process drifts.

Never shuffle: random K-fold splits train on the future and test on the past. With $K$ origins every $s$ days and horizon
$H$ you obtain $K\cdot H$ errors, but they are **not independent**: forecasts from the same origin share the same level error,
and adjacent origins overlap in time. The effective sample size is closer to the number of origins than to $K\cdot H$.

## Accuracy measures

For $n$ errors $e_i$ with actuals $a_i$ and forecasts $f_i$:

$$
\text{MAE}=\tfrac1n\sum|e_i|,\quad
\text{RMSE}=\sqrt{\tfrac1n\sum e_i^2},\quad
\text{MAPE}=\tfrac1n\sum\frac{|e_i|}{|a_i|},\quad
\text{sMAPE}=\tfrac1n\sum\frac{2|e_i|}{|a_i|+|f_i|},
$$
$$
\text{MASE}=\frac{\text{MAE}}{\frac{1}{T_0-m}\sum_{t=m+1}^{T_0}|y_t-y_{t-m}|},\qquad
\text{bias}=\tfrac1n\sum e_i .
$$

- **MAE** is in the unit of the data and robust to rare large misses; **RMSE** punishes large errors (use it when a big miss is
  disproportionately costly, e.g. stock-outs). RMSE $\ge$ MAE always; a large gap means a few large errors.
- **MAPE** is scale-free but explodes when actuals are near zero and penalises over-forecasts more than under-forecasts;
  **sMAPE** softens that but is still unstable near zero (and is not symmetric either). Never use them on series that touch zero.
- **MASE** divides by the in-sample error of the seasonal naive method ($m=7$ here). It is unit-free, defined at zero, and
  below 1 means "better than the naive benchmark would have been on the training data".
- **Bias** tells you whether errors lean in one direction (plan for it), the others tell you how large they are.

**Worked example** with actuals $(102,98,110,95)$, forecasts $(100,104,105,99)$ and an in-sample scale of 6.0: errors
$(2,-6,5,-4)$, MAE $=4.25$, RMSE $=4.50$, MAPE $=4.21\%$, sMAPE $=4.17\%$, MASE $=0.71$, bias $=-0.75$. The
RMSE is larger than the MAE because of the $-6$ and $+5$ errors; the negative bias says the model slightly over-forecasts.

## Leakage: when the test is not a test

Leakage means information from the future influences the forecast or its tuning. Typical forms:

1. **Centred smoothers** (centred moving average, a spline fitted to the whole series) used as a "forecast", or a forecast
   *calibrated* so that it matches the realised total of the period it is supposed to predict.
2. **Fitting on everything**, then scoring the last weeks (the coefficients have already seen them). Includes seasonal factors,
   scalers and outlier thresholds computed on the whole series.
3. **Tuning on the test set**: trying many models or parameters and reporting the best holdout score; the winner's score is
   optimistic by selection. Keep a final untouched block, or nest the tuning inside the backtest.
4. **Features that are not known at the origin** (next week's promo calendar is fine, next week's weather actuals are not).

## A single holdout is one draw

The error of a forecast method in one 4-week window depends heavily on what happened in that window (a promotion, a holiday, a
quiet month). Rank methods on a single holdout and the winner may be the one that suits *that* month. A rolling-origin
evaluation gives a distribution of scores (min, max, how often each method wins), which is what you need to judge
whether a difference between two methods is larger than the week-to-week scatter.

## Assumptions and pitfalls

1. Future errors resemble backtest errors: no structural change. Check the most recent origins separately.
2. The horizon of the backtest must be the horizon of the decision (a 1-day-ahead score says little about 4 weeks ahead).
3. Report several metrics: the ranking can change between MAE and RMSE.
4. Aggregating over origins hides the worst cases; look at the largest per-origin error.
5. Comparing against a naive benchmark ([lesson 21](../21-naive-and-seasonal-naive-forecasts/theory.md)) is mandatory; a score without
   a benchmark has no meaning.

## Related notes

- [Trend and seasonal regression forecasting](../22-trend-and-seasonal-regression-forecasting/theory.md)
- [Exponential smoothing models](../23-exponential-smoothing-models/theory.md)
- [Prediction intervals and forecast uncertainty](../25-prediction-intervals-and-forecast-uncertainty/theory.md)
- [Sampling distributions](../16-sampling-distributions-and-the-clt/theory.md)
- Repo note: [forecast evaluation](../../notes/time_series/forecast_evaluation.md)
