# Modeling and Diagnostics

Read [time-series modeling](../../notes/time_series/time_series_modeling.md), [randomness tests](../../notes/time_series/randomness_tests.md), and the ACF/PACF note.

1. Fit an AR(1) by least squares to a simulated stationary series. Compare the fitted coefficient with the value used to generate the data.
2. Given log-likelihood $-100$ and $k=3$, calculate AIC. Repeat for log-likelihood $-96$ and $k=6$. Which candidate is preferred by AIC?
3. Explain why a lower AIC does not excuse a residual ACF with a large lag-12 spike.
4. For $y_t=0.4+0.6y_{t-1}-0.2y_{t-2}+\varepsilon_t$, $y_{t-1}=3$, $y_{t-2}=2$, and $\varepsilon_t=0.5$, calculate the observation and conditional mean.
5. Fit a candidate model, calculate residuals, and inspect their mean, variance, ACF, and squared ACF. What different failures can each diagnostic reveal?
6. A Ljung-Box p-value at lag 10 is 0.002. State the null hypothesis, the evidence, and two model changes worth investigating.
7. Explain why MA innovations cannot be inserted as if they were observed regressors in an ordinary regression.
8. Compare two candidate models using AIC, residual diagnostics, and expanding-window forecast error. Write a short model-selection justification that names all three sources of evidence.

## Checks

- The two AIC values are 206 and 204.
- The conditional mean in question 4 is $0.4+0.6(3)-0.2(2)=1.8$, and the realized value is $2.3$ after adding the shock.
- The Ljung-Box result suggests remaining serial dependence at one or more tested lags; it does not identify the correct replacement model by itself.

## Applied practice

9. Run [diagnostics_visualizations.py](../../scripts/time_series/diagnostics_visualizations.py). For each figure, identify the model assumption it challenges.
10. Simulate residuals with a mean shift, variance shift, nonlinear dependence, and heavy tails. Which diagnostic reveals each feature most clearly?
11. Calculate $Q(10)$ from a supplied residual ACF and explain the role of the effective sample size.
12. Fit a model before and after a suspected structural break. Compare parameter estimates, residuals, and temporal backtests.
13. Build a candidate table with transformation, parameter count, AIC, residual lag-1 ACF, Ljung-Box p-value, MAE, and interval coverage.
14. Explain why selecting the candidate with the smallest in-sample SSE can favor an overfit model.
15. Use a time-respecting train/validation/test split and document which choices are made in each segment.

## Reflection

State what would make you reject a fitted model even if its information criterion is lowest. Include at least one residual reason and one forecasting reason.

## Extension tasks

16. Compute AICc for $n=40$, $k=5$, and AIC $=120$.
17. Simulate a residual series with a break in variance and compare raw, squared, and rolling-window plots.
18. Calculate the Ljung-Box statistic through lag 3 for supplied ACF values $(0.2,0.1,0.05)$ and $n=100$.
19. Compare a Gaussian likelihood with a heavy-tailed innovation assumption when the residual histogram has extreme observations.
20. Explain why a model with white residuals can still have poor forecast performance after a structural break.
21. Write a reproducible model-selection log that records every decision made before the final test period.

## Worked solutions

1. Model answer:
   ```python
   rng = np.random.default_rng(1)
   phi = 0.6; n = 300
   x = np.zeros(n)
   for t in range(1, n):
       x[t] = phi*x[t-1] + rng.normal()
   phi_hat = (x[1:]*x[:-1]).sum()/(x[:-1]**2).sum()
   ```
   $\hat\phi=\sum x_tx_{t-1}/\sum x_{t-1}^2$ is close to $0.6$, with standard error about $\sqrt{(1-\phi^2)/n}=0.046$; a difference of one or two standard errors is normal.
2. $\mathrm{AIC}=2k-2\ln L$. First: $2(3)-2(-100)=6+200=206$. Second: $2(6)-2(-96)=12+192=204$. The second has lower AIC, so AIC prefers it (the likelihood gain of 4 exceeds the penalty difference of 3).
3. AIC measures one-step likelihood fit overall. A significant lag-12 residual spike means a systematic seasonal dependence is unmodeled, so forecasts are suboptimal and standard errors and intervals are wrong. A lower AIC among inadequate candidates only ranks bad models. Add seasonal terms and re-check.
4. Conditional mean: $0.4+0.6(3)-0.2(2)=0.4+1.8-0.4=1.8$. Realized $y_t=1.8+0.5=2.3$.
5. Mean: bias (non-zero mean means a missing constant or trend). Variance over time: heteroskedasticity or a break. ACF: remaining linear dependence (wrong orders, missing seasonality). Squared ACF: conditional heteroskedasticity (ARCH). Add the Q-Q plot for non-normality and outliers.
6. $H_0$: the residual autocorrelations at lags $1,\dots,10$ are all zero (white noise, after adjusting degrees of freedom by the number of fitted ARMA parameters). A p-value of $0.002$ is strong evidence against $H_0$, so some serial dependence remains. Investigate: adding AR/MA or seasonal terms, and modeling a missing trend, outlier, or regime shift.
7. MA innovations $\varepsilon_{t-j}$ are unobserved and depend on the parameters themselves: $\varepsilon_t=X_t-\mu-\theta\varepsilon_{t-1}$. They must be reconstructed recursively from the data given $\theta$, so the model is nonlinear in the parameters and OLS does not apply; estimation uses conditional/exact maximum likelihood or the Kalman filter.
8. Model answer: build a table with in-sample AIC (same response, same sample), residual Ljung-Box p-value and ACF, and expanding-window MAE by horizon. Select model B if it has lower AIC, white residuals, and lower or equal out-of-sample error; if criteria disagree prefer the simpler model with adequate residuals and better forecasts, since forecasting is the stated purpose.
9. Model answer: residual time plot challenges zero mean and constant variance; residual ACF challenges independence/whiteness; Q-Q plot challenges normality; squared ACF challenges constant conditional variance; Ljung-Box plot challenges joint whiteness across lags.
10. Model answer: mean shift: residual time plot or mean/t-test by segment; variance shift: rolling variance or squared residuals; nonlinear dependence: ACF of squares or absolute values; heavy tails: Q-Q plot and kurtosis, Jarque-Bera.
11. $Q(m)=n(n+2)\sum_{k=1}^m\hat\rho_k^2/(n-k)$ is compared with $\chi^2_{m-p-q}$. Example: $n=100$, $\hat\rho_{1,2,3}=0.2,0.1,0.05$ gives $5.42$ (see question 18). The weights $1/(n-k)$ reflect the number of products available at each lag (effective sample size $n-k$), and with short series the correction matters; degrees of freedom are reduced by the number of fitted ARMA parameters.
12. Model answer: fit the same specification on the two segments; a break is supported if coefficients change by more than their standard errors, residual variance changes, or a Chow-type comparison rejects, and the model fit on the post-break segment gives lower rolling-origin error. A single full-sample model averages two regimes and typically leaves autocorrelated residuals.
13. Model answer: a table with one row per candidate and the columns listed, with the log response noted (AIC comparable only across candidates with the same response). Rank by out-of-sample MAE first, then use AIC and residual checks to confirm adequacy; coverage near the nominal value is required.
14. SSE always declines (weakly) when parameters are added, since a larger model nests the smaller one. A model with many parameters fits noise, which does not repeat in future data, so selecting by minimal SSE favors overfit. Penalized criteria (AIC, BIC) or out-of-sample SSE correct this.
15. Model answer: train (earliest block): estimate parameters, transformations and scalers. Validation (next block): choose orders, features, and hyperparameters. Test (latest block): evaluated once, after all choices are frozen. No shuffling, and preprocessing statistics come only from the training data.
16. $\mathrm{AICc}=\mathrm{AIC}+\dfrac{2k(k+1)}{n-k-1}=120+\dfrac{2(5)(6)}{34}=120+1.765=121.76$.
17. Model answer: simulate `e[:300] ~ N(0,1)`, `e[300:] ~ N(0,3^2)`. The raw plot shows larger swings after the break, the squared series shows a level jump, and a rolling variance (window 30) steps from about 1 to 9. All three are consistent; the squared and rolling plots locate the break most clearly.
18. $Q(3)=100(102)\left[\dfrac{0.2^2}{99}+\dfrac{0.1^2}{98}+\dfrac{0.05^2}{97}\right]=10200(0.000404+0.000102+0.0000258)=5.42$. With 3 degrees of freedom (no fitted ARMA parameters), the 5% critical value is $7.81$ and $p\approx0.14$, so there is no evidence against white noise at these three lags.
19. Gaussian ML overweights extreme observations: the squared residuals dominate the likelihood, which can inflate $\hat\sigma^2$ and distort parameters. A Student-$t$ innovation likelihood downweights large residuals, gives wider tails (better interval calibration), and its fitted degrees of freedom summarize tail heaviness. Compare by AIC (same response) and tail coverage.
20. Residual whiteness only describes the in-sample past. After a structural break the parameters change, so the model, though white in the training period, produces biased forecasts and miscalibrated intervals. Whiteness is a necessary, not sufficient, condition; test with a time-respecting backtest that spans the break.
21. Model answer: a log with data version/date, series definition and transformations, split dates, candidates with seeds, selection criteria and the rule for choosing, every rejected specification, and the date the test period was first opened.

## Submission check

Include one table of candidates, one residual figure, one forecast-error figure, and a paragraph distinguishing in-sample fit from future performance.
