# Forecast Evaluation and Backtesting

A backtest recreates forecasting decisions at historical dates. At each date, hide the later observations, run the procedure using the information then available, and score the resulting predictions when their target observations become available. This evaluates a forecasting process rather than how closely a fitted curve follows the data used to estimate it.

The procedure includes preprocessing, parameter estimation, model selection, predictor forecasts, and any update rule. If one of those steps uses later information, a chronological split of the final target rows does not rescue the experiment.

Specify the target, origins, horizons, available predictors, and scoring rule before comparing methods. Use the same evaluation cases for every candidate and include a baseline that represents the simplest plausible structure. Then examine errors by horizon and through time: an overall average can hide a failure at the horizon or regime that matters for the decision.

## Worked calculation: three errors and one scale

Suppose the actual values are $(10,12,9)$ and forecasts are $(9,11,10)$. Using the convention $e=y-\hat y$, the errors are $(1,1,-1)$, so

$$
\mathrm{MAE}=\frac{1+1+1}{3}=1,
\qquad
\mathrm{RMSE}=\sqrt{\frac{1+1+1}{3}}=1.
$$

If the in-sample naive scale is 2, then

$$
\mathrm{MASE}=\frac{1}{2}=0.5.
$$

The scale must be calculated using only the training portion available at each forecast origin. Here the fixed scale is 2 for all three errors. If the training window and its scale change between origins, calculate each scaled error with its corresponding training scale before aggregating. A scale computed from future test values would leak information. A rolling-origin evaluation repeats this calculation through time so that every forecast is produced using past information only.

![Rolling-origin forecasts and forecast errors](https://raw.githubusercontent.com/djeada/Statistics-Notes/main/assets/time_series/student/15_forecast_backtesting.png)

The figure makes the evaluation design explicit: the forecast origin moves forward, the model is refit or updated using the information available at that date, and the later observation is used only to score the forecast.

## The evaluation question

Forecast evaluation asks a different question from in-sample fit: **How well would this forecasting procedure have predicted observations that were genuinely in the future when each forecast was issued?**

## Preserve Temporal Order

Randomly shuffling observations destroys the information structure of a forecasting problem. A valid evaluation keeps training observations earlier than validation or test observations. Validation periods can be used for model or hyperparameter selection, while the final test period should remain untouched until the procedure has been selected.

![Temporal leakage](https://raw.githubusercontent.com/djeada/Statistics-Notes/main/assets/time_series/forecasting/07_temporal_leakage.png)

The figure contrasts a valid chronological split with a leaked evaluation. The issue is not only where the target rows are split: preprocessing, feature construction, imputation, and predictor forecasts must also respect the same information boundary.

## Rolling-Origin Evaluation

A single holdout records performance over one part of history, which may be unusually easy, volatile, or structurally different. Rolling origins repeat the forecast experiment at several dates. An expanding training window retains all earlier observations; a fixed rolling window deliberately discards older ones. Choose the rule according to how the deployed procedure will update, and apply it consistently when comparing candidates.

For horizon $h$, define the forecast error at origin $t$ as

$$
e_{t,h}=y_{t+h}-\hat y_{t+h\mid t}.
$$

![Rolling origins](https://raw.githubusercontent.com/djeada/Statistics-Notes/main/assets/time_series/forecasting/02_rolling_origins.png)

The rolling-origin figure shows how the training window, origin, and forecast horizon move together. Accuracy should be reported by horizon whenever short- and long-horizon decisions have different importance.

## Baselines First

A baseline is a forecast with a clear persistence assumption. Naive repeats the latest level, seasonal-naive repeats the latest corresponding season, drift extends the historical average change, and the historical mean assumes a stable level without useful short-run dynamics. A sophisticated method should be compared with the relevant baseline on the same origins; comparing it with an unsuitable benchmark can exaggerate its value.

![Forecast baselines](https://raw.githubusercontent.com/djeada/Statistics-Notes/main/assets/time_series/forecasting/01_baseline_forecasts.png)

The baseline figure shows that different simple rules encode different assumptions: persistence, repeating seasonality, linear drift, or reversion to a stable historical mean. Choose the baseline that reflects the simplest plausible structure in the problem.

## Point Forecast Metrics

For errors $e_i=y_i-\hat y_i$,

$$
\mathrm{MAE}=\frac{1}{n}\sum_{i=1}^{n}|e_i|,
\qquad
\mathrm{RMSE}=\sqrt{\frac{1}{n}\sum_{i=1}^{n}e_i^2}.
$$

Mean Absolute Scaled Error compares the absolute forecast error with an in-sample naive scale. For seasonal period $m$,

$$
\mathrm{MASE}=
\frac{\frac{1}{n}\sum_{i=1}^{n}|e_i|}
{\frac{1}{T-m}\sum_{t=m+1}^{T}|y_t-y_{t-m}|}.
$$

MAPE can be useful when percentage error has a meaningful interpretation and values are strictly positive and comfortably away from zero. It is undefined at zero and unstable near zero. MASE has a denominator limitation too: if the training series has no changes at the chosen naive or seasonal-naive lag, its scale is zero and the usual ratio is undefined.

![Point metrics](https://raw.githubusercontent.com/djeada/Statistics-Notes/main/assets/time_series/forecasting/03_point_metrics.png)

The point-metrics figure illustrates that MAE and RMSE can rank the same errors differently because RMSE gives more weight to large misses. Metric choice should reflect the loss that matters in deployment rather than habit.

## Prediction Intervals

A nominal 90% prediction interval should contain the target about 90% of the time over an appropriate collection of comparable cases. Too many misses suggest undercoverage, but very wide intervals can achieve high coverage while communicating little. Report coverage and width together, and inspect whether failures concentrate at long horizons or during volatile periods. Finite-sample coverage will vary, so do not expect exact equality with the nominal percentage.

![Interval coverage](https://raw.githubusercontent.com/djeada/Statistics-Notes/main/assets/time_series/forecasting/04_interval_coverage.png)

The figure shows why nominal coverage alone is not enough: intervals can achieve high coverage simply by being too wide. A useful interval is both appropriately calibrated and reasonably narrow.

For probabilistic forecasts, quantile or pinball loss evaluates predicted quantiles directly and can be aggregated across several quantile levels.

## Leakage

Common leakage sources include full-data normalization, future-aware imputation, centered rolling features, selecting hyperparameters on the final test period, using future exogenous values that would not have been known at the forecast origin, and shuffled cross-validation.

Every feature should answer the same question: **Would this value have been available when the forecast was issued?**

Information criteria such as AIC, AICc, and BIC can help select candidates in sample, but they are not substitutes for out-of-sample forecast evaluation.

See the companion [forecast-backtesting notebook](https://github.com/djeada/Statistics-Notes/blob/main/notebooks/time_series/forecast_backtesting.ipynb) for an additional worked environment.

## Reconstructing and scoring the historical forecasting experiment

Forecast evaluation is an experiment repeated at historical dates. The central object is not only a fitted model; it is the entire **forecasting procedure**:

1. how the data are transformed;
2. how features are constructed;
3. how parameters are estimated;
4. how future predictors are obtained;
5. how the forecast is produced;
6. how the error or interval score is recorded.

If any step uses information from after the forecast origin, the evaluation is optimistic even if the final model equation itself looks valid.

### Information sets and forecast origins

Let $\mathcal F_t$ denote the information available immediately after observing $y_t$. Under squared-error loss, the optimal one-step conditional-mean forecast is

$$
\hat y_{t+1\mid t}=E(y_{t+1}\mid\mathcal F_t),
$$

and a two-step forecast is

$$
\hat y_{t+2|t}=E(y_{t+2}\mid\mathcal F_t).
$$

The notation emphasizes the information boundary. A forecast made at time $t$ cannot use $y_{t+1}$ to tune a transformation, estimate a scaling constant, choose a lag order, or fill a missing value.

For fixed horizon $h$,

$$
e_{t,h}=y_{t+h}-\hat y_{t+h\mid t}.
$$

State the sign convention because directional bias changes sign if error is defined as forecast minus actual. MAE and RMSE are unaffected by that reversal, but mean error and calibration plots are not.

### A concrete expanding-window calculation

Suppose the observed series is

| time | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| $y_t$ | 10 | 12 | 11 | 14 | 13 | 16 | 15 |

Use the naive rule $\hat y_{t+1\mid t}=y_t$ and evaluate one-step forecasts at origins $t=3,4,5,6$:

| origin $t$ | training values | forecast | actual | error |
|---:|---|---:|---:|---:|
| 3 | 10, 12, 11 | 11 | 14 | 3 |
| 4 | 10, 12, 11, 14 | 14 | 13 | -1 |
| 5 | 10, 12, 11, 14, 13 | 13 | 16 | 3 |
| 6 | 10, 12, 11, 14, 13, 16 | 16 | 15 | -1 |

At each origin the naive forecast uses only the latest observation then available. The resulting errors $(3,-1,3,-1)$ separate direction from size: the method underpredicts by 3 twice and overpredicts by 1 twice. Absolute and squared scores summarize magnitude, while the mean error reveals that the signs do not balance. The calculations below use all four forecasts rather than only a favorable subset.

$$
\mathrm{MAE}=\frac{3+1+3+1}{4}=2,
$$

and

$$
\mathrm{RMSE}
=\sqrt{\frac{3^2+(-1)^2+3^2+(-1)^2}{4}}
=\sqrt5
\approx2.236.
$$

The mean error is

$$
\mathrm{ME}=\frac{3-1+3-1}{4}=1,
$$

so the forecasts underpredict on average in this short evaluation. A single absolute-error score would hide that directional bias.

An expanding window uses every observation that has become available. A rolling window instead retains the most recent $w$ observations and can adapt more quickly after a structural change.

### Baselines are part of the scientific question

The most useful baseline depends on the structure of the series.

For a persistent non-seasonal level, the naive forecast is

$$
\hat y_{t+h\mid t}=y_t.
$$

For seasonal period $s$, a seasonal-naive forecast reuses the most recent observed value from the same season:

$$
\hat y_{t+h\mid t}=y_{t+h-s\lceil h/s\rceil}.
$$

A common drift forecast extrapolates the average historical change:

$$
\hat y_{t+h\mid t}
=y_t+h\frac{y_t-y_1}{t-1}.
$$

For a stable series without meaningful persistence, a historical-mean forecast is

$$
\hat y_{t+h\mid t}=\frac{1}{t}\sum_{j=1}^{t}y_j.
$$

The baseline is not a disposable preliminary. If an advanced procedure cannot improve on it using the same origins and horizons, the extra complexity has not shown forecasting value.

### Point metrics and what they reward

For $n$ evaluation cases,

$$
\mathrm{MAE}=\frac{1}{n}\sum_{i=1}^{n}|e_i|,
\qquad
\mathrm{RMSE}=\sqrt{\frac{1}{n}\sum_{i=1}^{n}e_i^2}.
$$

MAE gives each additional unit of error the same marginal weight. RMSE squares first, so a few large misses can dominate the result. In this example, both scores use the same errors; differing values reflect the loss function rather than a change in forecasts. Choose the score to match the cost of misses, and report the target units so that its scale can be interpreted.

Mean error,

$$
\mathrm{ME}=\frac{1}{n}\sum_{i=1}^{n}e_i,
$$

measures directional bias but can be close to zero when positive and negative errors cancel. Report it alongside an absolute metric when systematic over- or under-prediction matters.

For seasonal period $m$, define the training scale

$$
Q_m=\frac{1}{T-m}\sum_{t=m+1}^{T}|y_t-y_{t-m}|,
$$

then

$$
\mathrm{MASE}=\frac{\frac{1}{n}\sum_i|e_i|}{Q_m}.
$$

The MASE denominator is an average absolute naive or seasonal-naive change computed from training data. It supplies a scale for the error, not a direct measurement of the baseline's later performance. A MASE below 1 therefore means the forecast's average absolute error is below that training scale; to claim it outperforms the baseline out of sample, also score the baseline on the same evaluation cases. Recompute the scale within each training window when that is part of the intended experiment.

MAPE is

$$
\mathrm{MAPE}=\frac{100}{n}\sum_i\left|\frac{e_i}{y_i}\right|.
$$

It is undefined when $y_i=0$ and can become arbitrarily large when $y_i$ is near zero. Percentage metrics should therefore be chosen only when their denominator is meaningful for the application.

### Interval forecasts

For interval forecast $(L_i,U_i)$ with nominal coverage $1-\alpha$, empirical coverage is

$$
\widehat{\mathrm{Coverage}}
=\frac{1}{n}\sum_{i=1}^{n}\mathbf 1\{L_i\le y_i\le U_i\}.
$$

Coverage does not describe where or how badly an interval misses. Two procedures can have the same coverage while one makes small misses and the other misses catastrophically during high-demand periods. Examine average width, tail-specific misses, horizon, and regime as well as the headline proportion. Quantile loss or an interval score can combine aspects of calibration and informativeness without rewarding arbitrary widening of every interval.

For a Gaussian stationary AR(1) with coefficient $\phi$ and innovation variance $\sigma^2$, the $h$-step forecast-error variance is

$$
\sigma_h^2
=\sigma^2\sum_{j=0}^{h-1}\phi^{2j}
=\sigma^2\frac{1-\phi^{2h}}{1-\phi^2}.
$$

When $|\phi|<1$, this approaches the unconditional variance $\sigma^2/(1-\phi^2)$ as the horizon grows.

### Leakage audit

Ask the same question of every operation: **Could this value have been computed at the forecast origin?**

| Operation | Unsafe version | Safe version |
|---|---|---|
| scaling | fit mean and standard deviation on all rows | fit them inside each training window |
| imputation | interpolate using observations after the gap | use past-only rules or an explicit forecasting model |
| rolling feature | centered rolling mean | trailing rolling mean ending at $t$ |
| feature selection | choose lags using the final test period | choose using training/validation origins |
| external predictor | use realized $x_{t+h}$ | forecast $x_{t+h}$ or use a value known in advance |
| seasonal normalization | estimate seasonal indices from the full sample | estimate them from data available at each origin |

Check one historical origin from raw inputs to the final score. Was the scaler fitted only on its training rows? Did imputation consult later values? Were predictor revisions published after the origin? Did the forecasting routine use a filtered state or a retrospectively smoothed state? This concrete reconstruction is often more informative than merely confirming that a train/test boundary appears in the code.

### Comparing models fairly

Evaluate all candidates on identical forecast origins, horizons, and target observations, and score them on the same reporting scale. Models may use different internal transformations, provided those transformations are fitted within each training window and forecasts are returned to the common evaluation scale. The following table is a template to fill with measured backtest results; blank cells are not zeros:

| model | MAE $h=1$ | MAE $h=3$ | RMSE $h=1$ | mean error |
|---|---:|---:|---:|---:|
| seasonal naive |  |  |  |  |
| ARIMA |  |  |  |  |
| dynamic regression |  |  |  |  |

![Error by horizon](https://raw.githubusercontent.com/djeada/Statistics-Notes/main/assets/time_series/forecasting/05_error_by_horizon.png)

The horizon plot shows why one average score can hide important differences. A model can be best at one-step prediction and lose that advantage at longer horizons.

Model classes also differ in how they adapt as new observations arrive. Exponential smoothing, for example, updates a latent level recursively rather than refitting a large parameter set at each step.

![Exponential smoothing](https://raw.githubusercontent.com/djeada/Statistics-Notes/main/assets/time_series/forecasting/06_exponential_smoothing.png)

This figure is useful in evaluation because the update rule itself is part of the forecasting procedure. A fair backtest must reproduce that update chronologically rather than estimate the smoothed state using future observations.

Plot errors over calendar time as well as by horizon.

![Forecast errors over time](https://raw.githubusercontent.com/djeada/Statistics-Notes/main/assets/time_series/forecasting/08_forecast_errors_over_time.png)

Errors from adjacent origins can refer to overlapping future periods, especially when the horizon exceeds one step. They are therefore often dependent. A sharp regime-specific failure can also be diluted by many easy periods in the aggregate score. Plot the dated errors, retain failed forecasts rather than silently dropping difficult cases, and account for dependence when quantifying uncertainty in model comparisons.

### Reproducible evaluation recipe

1. State the response, sampling interval, horizon, and decision loss.
2. Reserve a final test period before tuning.
3. Choose at least one domain-appropriate baseline.
4. Specify expanding or rolling origins.
5. At each origin, fit preprocessing and the model using past data only.
6. Produce point and interval forecasts.
7. Record errors, interval scores, fit failures, and the available sample.
8. Summarize by horizon and inspect errors over time.
9. Refit the selected procedure on all allowed historical data.
10. Record how the live forecast will obtain future predictors and update itself.

## Formula reference

| Metric / benchmark | General formula | Interpretation / special case |
|---|---|---|
| Forecast error | $e_{t,h}=y_{t+h}-\hat y_{t+h\mid t}$ | State the sign convention explicitly. |
| Mean error | $\mathrm{ME}=n^{-1}\sum_i e_i$ | Directional bias; positive under this convention means underforecasting on average. |
| MAE | $\mathrm{MAE}=n^{-1}\sum_i\lvert e_i\rvert$ | Linear penalty on absolute error. |
| MSE | $\mathrm{MSE}=n^{-1}\sum_i e_i^2$ | Squared-error loss. |
| RMSE | $\mathrm{RMSE}=\sqrt{n^{-1}\sum_i e_i^2}$ | Gives larger misses more weight than MAE. |
| MAPE | $\mathrm{MAPE}=100n^{-1}\sum_i\lvert e_i/y_i\rvert$ | Undefined at zero and unstable near zero. |
| sMAPE | $\mathrm{sMAPE}=100n^{-1}\sum_i\frac{2\lvert y_i-\hat y_i\rvert}{\lvert y_i\rvert+\lvert\hat y_i\rvert}$ | One common symmetric-percentage convention; software definitions can differ. |
| MASE scale | $Q_m=(T-m)^{-1}\sum_{t=m+1}^{T}\lvert y_t-y_{t-m}\rvert$ | Use $m=1$ for nonseasonal naive scaling or seasonal period $m$. |
| MASE | $\mathrm{MASE}=[n^{-1}\sum_i\lvert e_i\rvert]/Q_m$ | Values below 1 beat the corresponding in-sample naive scale. |
| RMSSE | $\mathrm{RMSSE}=\sqrt{[n^{-1}\sum_i e_i^2]/[(T-m)^{-1}\sum_{t=m+1}^{T}(y_t-y_{t-m})^2]}$ | Squared-error scaled analogue of MASE. |
| Naive forecast | $\hat y_{t+h\mid t}=y_t$ | Random-walk benchmark. |
| Seasonal naive | $\hat y_{t+h\mid t}=y_{t+h-s\lceil h/s\rceil}$ | Repeats the most recent observation from the same season. |
| Drift forecast | $\hat y_{t+h\mid t}=y_t+h(y_t-y_1)/(t-1)$ | Linear extrapolation of average historical change. |
| Empirical interval coverage | $n^{-1}\sum_i I(L_i\le y_i\le U_i)$ | Compare with nominal coverage $1-\alpha$. |
| Average interval width | $n^{-1}\sum_i(U_i-L_i)$ | Sharpness measure; narrower is better only when calibration is adequate. |
| Interval score | $(U-L)+\frac{2}{\alpha}(L-y)I(y<L)+\frac{2}{\alpha}(y-U)I(y>U)$ | Proper score balancing width and misses for a central $(1-\alpha)$ interval. |
| Pinball loss | $L_\tau(y,q)=(\tau-I(y<q))(y-q)$ | Proper loss for a forecast quantile $q$ at level $\tau$. |
