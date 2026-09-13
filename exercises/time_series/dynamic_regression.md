# Dynamic Regression

Read [dynamic regression](../../notes/time_series/dynamic_regression.md) and [regression with ARMA errors](../../notes/time_series/regression_with_arma_errors.md).

1. For $y_t=2+1.5x_t+n_t$, calculate $y_t$ when $x_t=4$ and $n_t=0.3$.
2. For $y_t=2+x_t+0.5x_{t-1}+n_t$, calculate the regression mean when $x_t=4$ and $x_{t-1}=2$.
3. Simulate AR(1) errors with coefficient $0.75$. Fit ordinary least squares and inspect residual autocorrelation. Explain what the dynamic error model adds.
4. List three predictors known in advance at the forecast origin and three predictors that usually require their own forecasts.
5. Explain why a statistically useful predictor is not automatically a causal intervention.
6. Compare a model with current $x_t$ only to one with $x_t$ and $x_{t-1}$. Use rolling-origin evaluation and state how future $x$ values are obtained.
7. Explain why the label ARIMAX is not enough to identify the exact likelihood or error equation used by software.

## Checks

- The value in question 1 is $2+1.5(4)+0.3=8.3$.
- The regression mean in question 2 is $2+4+1=7$.
- The complete forecasting procedure includes the predictor-forecast step whenever future predictors are unavailable.

## Applied practice

8. Run [dynamic_multivariate_visualizations.py](../../scripts/time_series/dynamic_multivariate_visualizations.py). Explain which figure demonstrates future-predictor leakage.
9. Simulate a distributed-lag response with weights $(1,0.6,0.25)$. Estimate the lag pattern and discuss collinearity between adjacent predictors.
10. Compare OLS, heteroskedasticity-and-autocorrelation robust standard errors, and a regression-with-ARMA-errors model. Which changes coefficients and which changes uncertainty?
11. Create a predictor known in advance, a predictor observed with a release delay, and a predictor requiring a forecast. Use different treatment for each.
12. Add a structural break to the regression slope. Examine residuals and coefficient stability over expanding windows.
13. Explain how a causal intervention design would need stronger assumptions than a predictive regression.

## Reflection

Document the target equation, lag convention, predictor availability, error model, and complete backtesting procedure. Treat ARIMAX as a software label that must be translated into an equation.

## Extension tasks

14. Derive the long-run multiplier for a stable distributed-lag model with coefficients $(1,0.5,0.25)$.
15. Add a predictor with a release delay and compare an oracle backtest with a real-time backtest.
16. Simulate feedback from $y_t$ into $x_{t+1}$. Explain why a regression coefficient may not have a causal interpretation.
17. Compare dynamic regression errors before and after adding an AR(1) term. Use residual ACF and temporal MAE.
18. Fit a model with a known calendar variable and a forecasted weather variable. Include predictor uncertainty in the interval discussion.
19. Explain how omitted common trend can produce a spurious dynamic regression.

## Submission check

Include the model equation, predictor timing table, residual diagnostics, baseline, and a forecast comparison that uses only information available at each origin.
