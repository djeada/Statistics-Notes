# State Space

Read [state-space models](../../notes/time_series/state_space_models.md).

1. In the local-level model, use $a_{t|t-1}=10$, $P_{t|t-1}=1.25$, $y_t=12$, and $R=1$ to calculate the innovation, innovation variance, Kalman gain, updated level, and updated variance.
2. Repeat question 1 with $R=4$. Which direction does the Kalman gain move and why?
3. Explain the difference between filtering, smoothing, and forecasting. Which one is valid for a real-time estimate at time $t$?
4. Remove one observation from a simulated series. Show how the state prediction proceeds without a measurement update.
5. Simulate a local-level process and compare raw-observation RMSE with filtered-state RMSE.
6. Explain how the innovation sequence contributes to a Gaussian state-space likelihood.
7. Give one example where a state-space model is preferable to a simple regression with time as a predictor.

## Checks

- The innovation is 2, its variance is 2.25, and the gain is $1.25/2.25=0.5556$.
- The updated level is approximately $11.1112$ and the updated variance is approximately $0.5555$.
- Increasing measurement variance makes the filter trust the prior state more, so the gain decreases.
