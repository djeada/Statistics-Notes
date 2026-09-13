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

## Applied practice

8. Run [state_space_frequency_visualizations.py](../../scripts/time_series/state_space_frequency_visualizations.py) and identify the difference between filtering and smoothing in the plotted data.
9. Repeat the scalar update for $(P,R)=(1.25,0.1)$, $(1.25,1)$, and $(1.25,4)$. Plot the gain against $R$.
10. Introduce a block of missing observations. Compare filtered variance before, during, and after the gap.
11. Estimate $Q$ and $R$ on simulated local-level data by a grid search. Plot the innovation sum of squares over the grid.
12. Compare a local-level model with a regression on time when the latent level changes randomly. Explain which uncertainty each model represents.
13. Calculate standardized innovations and inspect their ACF and squared ACF.
14. Explain why a smoothed historical state cannot be used as a real-time feature without recreating the full-sample future information.

## Reflection

State the transition equation, measurement equation, disturbance assumptions, initialization, missing-data rule, and forecast target for your state-space model.

## Extension tasks

15. Derive the local-level update from minimizing a variance-weighted quadratic loss.
16. Compare filtered and smoothed estimates around an abrupt level change.
17. Calculate the innovation log-likelihood contribution for $v_t=2$ and $F_t=2.25$.
18. Simulate two processes with the same observations but different $(Q,R)$ ratios. Compare gains and filtered paths.
19. Explain how a local trend state differs from a regression on time.
20. Create a missing block at the beginning, middle, and end of a series. Compare uncertainty behavior.

## Submission check

Include the state and measurement equations, one hand update, a gain or variance figure, missing-data behavior, and a real-time versus retrospective interpretation.
