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

## Worked solutions

1. The conditional mean is $\hat X_T(h)=\phi^hX_T$. One step: $0.8(5)=4$. Five steps: $0.8^5(5)=0.32768(5)=1.6384$.
2. $X_{T+2}=\phi^2X_T+\phi\varepsilon_{T+1}+\varepsilon_{T+2}$, so $\operatorname{Var}=\sigma^2(1+\phi^2)=1+0.64=1.64$, greater than the one-step variance $1$ because the error now contains the first future shock (propagated through $\phi$) in addition to the second: uncertainty accumulates with horizon.
3. Errors $(10-9,12-11,9-10)=(1,1,-1)$. MAE $=(1+1+1)/3=1$. RMSE $=\sqrt{(1+1+1)/3}=1$. MASE $=\mathrm{MAE}/2=0.5$.
4. Model answer:
   ```python
   for T in range(100, n-H):
       train = y[:T+1]
       naive = np.repeat(train[-1], H)
       snaive = np.array([train[T+1+h-12] for h in range(H)])  # period 12
       ar = AutoReg(train, lags=1).fit().forecast(H)
       # store errors by horizon h = 1..H
   ```
   Compute MAE by horizon across origins. Typically AR is best at short horizons for a stationary series, seasonal-naive for strongly seasonal series, and all converge to the unconditional behaviour at long horizons.
5. Model answer: at origin $t$ the model sees observations $1,\dots,t$ and predicts $t+1,t+2,t+3$; the next origin $t+1$ adds observation $t+1$:
   ```
   origin t   : [1 ... t] | t+1 t+2 t+3
   origin t+1 : [1 ... t+1] | t+2 t+3 t+4
   ```
   Only data to the left of the bar are available.
6. (i) Normalization: standardizing with the full-sample mean and standard deviation. (ii) Imputation: filling gaps by interpolation, using future values, or by the full-sample mean. (iii) Rolling features: centered rolling windows that include $y_{t+1},\dots$, or features not shifted by one step. (iv) Exogenous variables: using the realized value of a predictor at time $t+h$ that would not be known at the origin, or using revised data that was not yet released.
7. Example: demand actuals $(0,2,5)$ and forecasts $(1,2,4)$. The percentage error at $0$ is undefined ($1/0$); with actuals of $0.01$ and a forecast of $1$, the error is $9900\%$, dominating the mean. MAPE also penalizes over-forecasts more than under-forecasts. Use MASE, MAE, or scaled errors.
8. Coverage $=\#\text{inside}/20$; e.g. 18 inside gives $0.90$, 19 gives $0.95$. With 20 intervals the binomial standard deviation is $\sqrt{20(0.95)(0.05)}\approx0.97$ intervals, so $17$ to $20$ inside is consistent with nominal 95%. Coverage alone is not enough because infinitely wide intervals achieve 100%; report width (or the interval/Winkler score) alongside.
9. The seasonal-naive forecast reproduces the seasonal pattern from the prior cycle, while a non-seasonal AR(p) with small $p$ reverts to the mean and cannot represent a period-12 shape. Where seasonality is strong, the benchmark captures most of the variance.
10. Model answer: expanding window uses all history (lower variance); rolling window uses the most recent $w$ observations (adapts after a break). After a break, the rolling window's error falls once $w$ observations from the new regime are available, while the expanding window is biased by the old regime for a long time. Before the break, the expanding window usually wins.
11. MAE: robust and interpretable, suited to a linear-cost decision (inventory units). RMSE: when large errors are costly (quadratic loss, e.g. power-grid reserves). Mean error (bias): when systematic over/under forecasting matters (budgeting). MASE: to compare across series with different scales. Report each by horizon $h=1,\dots,H$.
12. Model answer: coverage $=\frac1m\sum\mathbf 1\{l_i\le y_i\le u_i\}$ and mean width $=\frac1m\sum(u_i-l_i)$ per level. Expected: coverage near $0.80,0.95,0.99$; widths ratios about $1.28:1.96:2.58$ under Gaussian errors. Under-coverage suggests underestimated variance or breaks.
13. At origin $t$, a trailing mean $\frac1k\sum_{j=0}^{k-1}y_{t-j}$ uses only past data. A centered mean $\frac1k\sum_{j=-m}^{m}y_{t+j}$ uses $y_{t+1},\dots,y_{t+m}$, which are unknown, so it leaks the future. Example with $y=(1,2,3,10,4)$ at $t=3$ ($k=3$): trailing $=(1+2+3)/3=2$; centered $=(2+3+10)/3=5$. The centered feature has the information that a spike happens next.
14. Model answer: forecast the predictor $\hat z_{T+h}$ (for example by its own AR model), feed it into the target model, and combine variances: $\operatorname{Var}\approx\sigma_y^2+\beta^2\sigma_z^2(h)$. Compare MAE and interval coverage to the oracle that uses realized $z_{T+h}$: the oracle is more accurate but unavailable, and gives an optimistic evaluation.
15. Model answer: plot $e_t$ against time and against phase (month), and the rolling MAE. Large misses at break dates, in high-volatility segments, or in specific seasonal phases point to, respectively, a structural change, heteroskedasticity, and a seasonal misspecification. A quantitative check is the ACF of $|e_t|$ and mean $|e|$ by month.
16. $X_{T+h}-\hat X_T(h)=\sum_{j=0}^{h-1}\phi^j\varepsilon_{T+h-j}$, so $\operatorname{Var}=\sigma^2\sum_{j=0}^{h-1}\phi^{2j}=\sigma^2\dfrac{1-\phi^{2h}}{1-\phi^2}$. For $\phi=0.5$, $\sigma^2=4$, $h=3$: $4(1+0.25+0.0625)=4(1.3125)=5.25$ (equivalently $4(1-0.015625)/0.75=5.25$).
17. Example: forecasts from a model that is accurate on average (small MAE) but uses a constant error variance estimated in a calm period, so intervals are too narrow in volatile regimes and coverage falls below nominal (e.g. 70% for a 95% interval). The tradeoff: point accuracy and calibration are separate properties, so assess both, for instance with the interval score $(u-l)+\frac2\alpha(l-y)_++\frac2\alpha(y-u)_+$.
18. After a mean shift of size $\Delta$ at the midpoint, the expanding window's estimated mean remains between the two regimes (bias up to $\Delta/2$ and falling slowly), while a rolling window of size $w$ re-centres after $w$ observations. Evaluate by MAE after the break: rolling wins by about the bias, but it has higher variance before the break.
19. For quarterly data with seasonal period $m=4$: $\text{scale}=\frac1{T-4}\sum_{t=5}^{T}|y_t-y_{t-4}|$ computed on the training data only, and $\mathrm{MASE}=\mathrm{MAE}_{\text{test}}/\text{scale}$. The scale is the in-sample error of the seasonal-naive benchmark and puts the error in comparable units; it is not an estimate of test error.
20. Model answer:

    | Step | Leak if done on full data | Safe version |
    |---|---|---|
    | Log transform | Not leaky (pointwise), but Box-Cox $\lambda$ fit on all data is | Fit $\lambda$ on the training window |
    | Imputation | Interpolating with future points | Forward-fill or model-based using past only |
    | Lagged features | Lag $0$ or centered lag | Use lags $\ge h$ available at the origin |
    | Hyperparameter tuning | Choosing on test period | Tune on validation only, time-ordered folds |
21. Model answer: report MAE (and bias) in a table by horizon $h=1,\dots,12$ and by regime (e.g. pre-break, post-break; calm, volatile). A single overall number hides that errors grow with $h$ and are worse in the volatile regime.

## Submission check

State the decision loss, baseline, origin geometry, information set, metrics, interval score, and final test rule.
