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

## Submission check

Include one table of candidates, one residual figure, one forecast-error figure, and a paragraph distinguishing in-sample fit from future performance.
