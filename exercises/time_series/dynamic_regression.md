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
