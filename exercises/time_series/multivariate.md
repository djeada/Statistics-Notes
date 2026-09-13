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
