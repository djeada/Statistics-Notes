# ARIMA and Seasonality

Read [the backshift operator](../../notes/time_series/backward_shift_operator.md), [ARIMA models](../../notes/time_series/arima_models.md), and [seasonality and trends](../../notes/time_series/seasonality_and_trends.md).

1. For $y=(120,123,126,130)$, calculate the first differences. Which level information is removed?
2. For monthly observations with $y_{t-12}=92$ and $y_t=100$, calculate the seasonal difference. Write the operator form.
3. Expand $(1-B)^2y_t$ and evaluate it for $(y_{t-2},y_{t-1},y_t)=(13,12,15)$.
4. A quarterly additive seasonal pattern is $(-3,1,4,-2)$. Check its normalization and calculate the deterministic value at $t=5$ when the level is $50+2t$.
5. Explain when an additive decomposition is more appropriate than a multiplicative decomposition. Use a plot or a small simulated example.
6. A differenced series has an ACF that still decays slowly. Give three possible explanations and a next diagnostic for each.
7. Write the full model equation for ARIMA$(1,1,1)$ and SARIMA$(0,1,1)(0,1,1)_{12}$ using the backshift operator.
8. Explain why differencing twice can make a series harder to model even when it reduces the apparent trend.

## Checks

- First differences are $(3,3,4)$.
- The seasonal difference is $100-92=8$, written $(1-B^{12})y_t$.
- $(1-B)^2y_t=y_t-2y_{t-1}+y_{t-2}=4$ for the supplied values.
- The seasonal indices sum to zero, and the deterministic value at $t=5$ is $60-3=57$.

## Applied practice

9. Run [arima_seasonality_visualizations.py](../../scripts/time_series/arima_seasonality_visualizations.py) and explain which figures show under-differencing and over-differencing.
10. Simulate additive and multiplicative seasonality with the same period. Decide whether a log transform is justified from the changing amplitude.
11. Fit a seasonal-naive benchmark before fitting a SARIMA candidate. Report errors at horizons 1, 3, 6, and 12.
12. Use a period-12 series to compute both $(1-B)y_t$ and $(1-B^{12})y_t$. Explain which feature each operation targets.
13. Show algebraically that $(1-B)(1-B^{12})y_t$ contains four terms. Verify the result numerically for a short vector.
14. Compare candidate orders using AIC and residual ACF. Explain why models fit to different transformed responses should not be compared blindly.
15. Integrate a sequence of forecasted changes back to levels. Include an interval and explain how uncertainty accumulates.

## Reflection

Write a short model card: target scale, ordinary difference order, seasonal period and difference order, candidate orders, baseline, residual result, and forecast-evaluation design.

## Extension tasks

16. Show that a random walk needs one ordinary difference but a seasonal random walk needs $(1-B^s)$.
17. Generate a series with a deterministic trend and compare detrending with first differencing.
18. Add an outlier before estimating seasonal indices. Explain how it changes the average seasonal effect.
19. Compare additive decomposition, multiplicative decomposition, and log-additive decomposition on a growing seasonal series.
20. Use a validation period to choose between a seasonal-naive forecast and a SARIMA candidate. Leave a final test period untouched.
21. Explain how the inverse transformation changes the interpretation of a forecast interval.

## Worked solutions

1. $\Delta y=(123-120,\,126-123,\,130-126)=(3,3,4)$. Differencing removes the level (any additive constant) and turns a linear trend into a constant; one observation is lost.
2. $\nabla_{12}y_t=y_t-y_{t-12}=100-92=8$, written $(1-B^{12})y_t$.
3. $(1-B)^2=1-2B+B^2$, so $(1-B)^2y_t=y_t-2y_{t-1}+y_{t-2}=15-2(12)+13=4$. It equals the change in the first difference: $(15-12)-(12-13)=3+1=4$.
4. The indices sum to $-3+1+4-2=0$, so they are normalized. At $t=5$ (second year, quarter 1) the seasonal value is $-3$ and the level is $50+2(5)=60$, giving $57$ (assuming $t=1$ is the first quarter).
5. Additive decomposition fits when the seasonal swing has a constant size regardless of the level; multiplicative when the amplitude scales with the level. Check: plot $y_t$ against its yearly range or compare peak-to-trough size in early and late years. Simulated example: `y = 100 + 0.5*t + 10*np.sin(2*np.pi*t/12)` (additive) versus `y = (100 + 0.5*t)*(1 + 0.1*np.sin(2*np.pi*t/12))` (multiplicative; the swing doubles as the level doubles).
6. (i) Remaining unit root or trend: unit-root test (ADF/KPSS) on the differenced series, or a second difference check; (ii) a strong seasonal component: seasonal ACF spikes at multiples of $s$, so fit seasonal differencing or dummies; (iii) a structural break or level shift: rolling mean plots and break tests. A near-unit AR root (long memory) is a fourth possibility, assessed by comparing AR fits and forecasts.
7. ARIMA$(1,1,1)$: $(1-\phi B)(1-B)y_t=c+(1+\theta B)\varepsilon_t$. SARIMA$(0,1,1)(0,1,1)_{12}$: $(1-B)(1-B^{12})y_t=(1+\theta B)(1+\Theta B^{12})\varepsilon_t$.
8. Each difference amplifies high-frequency noise: for white noise, $\operatorname{Var}(\Delta\varepsilon_t)=2\sigma^2$, and for second differences $\operatorname{Var}=6\sigma^2$. It also adds a unit MA root (an over-differenced, noninvertible component), induces a negative lag-1 autocorrelation ($-2/3$ after two differences of white noise), and loses observations. Prefer the smallest difference order that makes the series look stationary.
9. Model answer: in the script's figures, a slowly decaying ACF/trend remaining after one difference indicates under-differencing; a strongly negative ACF at lag 1 near $-0.5$ (and inflated variance) after differencing a stationary series indicates over-differencing.
10. Model answer: in the multiplicative series the seasonal swing grows with the level; after `np.log` the swings are roughly constant, which justifies the log. For the additive series the log is not needed and may create an artificial pattern. Check by plotting seasonal range versus yearly mean, or by comparing the residual spread before and after the transform.
11. Model answer:
    For each origin $t$, forecast $\hat y_{t+h}=y_{t+h-12}$ for $h\in\{1,3,6,12\}$ and report MAE by horizon for both the seasonal-naive and SARIMA candidate. If the SARIMA model cannot beat seasonal-naive at these horizons, its complexity is not justified.
12. $(1-B)y_t$ removes a slowly changing level/trend (and kills the stochastic trend), while $(1-B^{12})y_t$ removes a repeating period-12 pattern and the seasonal level. For a series with both, apply both: $(1-B)(1-B^{12})y_t$.
    ```python
    d1 = np.diff(y); d12 = y[12:] - y[:-12]; d112 = np.diff(d12)
    ```
13. $(1-B)(1-B^{12})=1-B-B^{12}+B^{13}$, so $(1-B)(1-B^{12})y_t=y_t-y_{t-1}-y_{t-12}+y_{t-13}$: four terms. Numerically, for $y=(1,3,2,5,4,7,6,9,8,11,10,13,12,15)$ ($n=14$, $t=14$): $15-12-3+1=1$, and via the two-step route $\nabla_{12}y_{14}-\nabla_{12}y_{13}=(15-3)-(12-1)=1$, matching. Sample loss: $13$ observations.
14. AIC values are computed from the likelihood of the response, so they are only comparable when every candidate models the same response on the same sample. A log-transformed model has a likelihood of $\log y$; its AIC must be adjusted by the Jacobian ($+2\sum\log y_t$) to compare with a level model, and differencing orders change the effective sample, so AIC comparisons across $d$ are invalid. Use out-of-sample error on the original scale for such cases.
15. If $\hat\Delta_{T+h}$ are forecast changes, then $\hat y_{T+h}=y_T+\sum_{j=1}^h\hat\Delta_{T+j}$. Error variances add up: for a random walk, $\operatorname{Var}=h\sigma^2$, so a 95% interval is $\hat y_{T+h}\pm1.96\sigma\sqrt h$, widening with the square root of the horizon. With $y_T=130$, $\hat\Delta=3.5$, $\sigma=1$: $\hat y_{T+3}=140.5$, interval $140.5\pm3.4$ (ignoring the correlation of $\Delta$ forecasts).
16. Random walk: $y_t=y_{t-1}+\varepsilon_t$, so $(1-B)y_t=\varepsilon_t$ is white noise and one ordinary difference suffices. Seasonal random walk: $y_t=y_{t-s}+\varepsilon_t$, so $(1-B^s)y_t=\varepsilon_t$; the ordinary difference gives $y_t-y_{t-1}=\varepsilon_t+\varepsilon_{t-1}$-type terms only if $s=1$, and for $s>1$ it leaves a strong lag-$s$ dependence ($\varepsilon_{t}-\varepsilon_{t-1}$ is not the innovation of a seasonal random walk) behind.
17. For $y_t=a+bt+\varepsilon_t$: detrending gives residual $\varepsilon_t$ (white, correct). First differencing gives $b+\varepsilon_t-\varepsilon_{t-1}$, an MA(1) with $\theta=-1$ (noninvertible, variance doubled, lag-1 ACF $-0.5$). Detrending is right for a deterministic trend; differencing is right for a stochastic trend.
18. An outlier of size $A$ in a season-$k$ observation shifts the estimated seasonal index of that season by about $A/m$ ($m$ years), and the normalization subtracts $A/(sm)$ from the others. Seasonal indices computed with the mean are sensitive; use the median or robust (STL) decomposition.
19. Model answer: additive decomposition leaves a growing seasonal pattern in the remainder; multiplicative decomposition removes it but cannot handle zero/negative values; log-additive gives the same structure as multiplicative with additive residuals and is the easiest for ARIMA. Choose by remainder stability (constant spread).
20. Model answer: split into train / validation / test in time order. Fit both on train, compare MAE (by horizon) on validation, choose, then refit on train+validation and evaluate once on the untouched test period.
21. If the interval is built on the log scale, $[\exp(l),\exp(u)]$ is asymmetric, covers the median (not the mean) of $y$, and widens with the level. The point forecast $\exp(\hat\mu)$ estimates the median; the mean needs the correction $\exp(\hat\mu+\sigma^2/2)$.

## Submission check

Report the exact operators, sample loss from differencing, seasonal period, model-selection evidence, and whether the residuals resemble white noise.
