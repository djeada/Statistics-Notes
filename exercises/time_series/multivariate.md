# Multivariate Models

Read [multivariate time series](../../notes/time_series/multivariate_time_series.md).

1. Write the two-equation VAR(1) for $y_t=(x_t,z_t)^\top$ with coefficient matrix $\begin{pmatrix}0.5&0.2\\-0.1&0.4\end{pmatrix}$ and intercept zero.
2. For $x_t=10$, $y_t=1.4x_t+u_t$, and $u_t=0.5$, calculate $y_t$ and the spread.
3. Explain why a regression of one independent random walk on another can have a high in-sample $R^2$.
4. Simulate two cointegrated series. Check that each level is non-stationary while the spread is more stable.
5. Explain what a Granger-predictability test conditions on and why it is not a structural causal intervention test.
6. Fit a VAR to stationary differences and inspect stability and residual cross-correlation.
7. Explain the role of $\alpha$ and $\beta$ in $\Pi=\alpha\beta^\top$ for a VECM.
8. Compute or plot an impulse response and state the assumptions needed before interpreting it as a response to a structural shock.

## Checks

- The value in question 2 is $1.4(10)+0.5=14.5$.
- A stable spread supports a cointegration story; it does not by itself identify a causal mechanism.
- Orthogonalized impulse responses can depend on variable ordering.

## Applied practice

9. Run [dynamic_multivariate_visualizations.py](../../scripts/time_series/dynamic_multivariate_visualizations.py). Identify the feedback, predictive, long-run, and shock-propagation figures.
10. Simulate a stable VAR(1). Check the eigenvalues of its coefficient matrix and compare simulated persistence with the largest eigenvalue.
11. Compare VAR lag orders using AIC and BIC. Inspect residual cross-correlation before choosing the smaller or larger order.
12. Simulate independent random walks and repeat the levels regression many times. Record how often the $R^2$ exceeds a chosen threshold.
13. Simulate cointegrated levels, estimate their spread, and compare a differenced VAR with a VECM conceptually.
14. Test Granger predictability in both directions. Explain why rejection in one direction does not prove an intervention effect.
15. Plot an impulse response under two variable orderings and describe what changes.

## Reflection

Write down the integration, deterministic-term, lag-order, stability, identification, and forecast-validation assumptions before interpreting a multivariate result.

## Extension tasks

16. Calculate the eigenvalues of a supplied VAR(1) coefficient matrix and determine whether the system is stable.
17. Simulate two unrelated random walks 100 times and summarize the distribution of levels-regression $R^2$.
18. Estimate a cointegrating vector in a two-series example and plot the spread.
19. Compare a VAR in levels, a VAR in differences, and a VECM in terms of the relationships each preserves.
20. Change the ordering used for orthogonalized impulse responses and identify the responses that change.
21. Explain why a Granger test can be unstable when the lag order or deterministic terms are misspecified.

## Submission check

Report the system dimensions, transformations, lag order, stability evidence, identification assumptions, and joint forecast-validation design.
