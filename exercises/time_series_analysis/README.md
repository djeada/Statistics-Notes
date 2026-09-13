# Time Series Analysis Exercises

These exercises follow the dependency order in `notes/time_series_analysis/README.md`. Use plots and calculations where appropriate, and state assumptions explicitly.

## Foundations

1. Let $\varepsilon_t$ be independent with mean 0 and variance 4. Compute its autocovariance function and explain why it is white noise.
2. Give an example of a process that is uncorrelated across time but not independent. Explain why weak white noise does not imply independence.
3. For $X_t=X_{t-1}+\varepsilon_t$, derive $\operatorname{Var}(X_t)$ when $X_0$ is fixed. Explain why the process is not weakly stationary.
4. Simulate 500 observations from an AR(1) process with $\phi=0.7$. Compare the sample ACF with the theoretical pattern $\rho(h)=\phi^{|h|}$.

## ARMA and Diagnostics

5. For an AR(2) model, write the stationarity condition in terms of roots of the AR polynomial and check a parameter pair of your choice.
6. Explain why past innovations in an MA(q) model cannot be treated as ordinary observed regressors.
7. Fit two candidate ARMA models to the same stationary series. Compare AIC/AICc/BIC and residual ACF. Explain why the smallest information criterion alone is not sufficient.
8. A fitted model has a Ljung-Box p-value of 0.002 at lag 12. What does this suggest, and what would you inspect next?

## Forecast Evaluation

9. Implement a naive forecast, seasonal-naive forecast, and one statistical model on the same series. Evaluate all three with expanding-window backtesting.
10. Compute MAE, RMSE, and MASE for the same forecasts. Describe a situation in which their rankings could differ.
11. Construct an example where MAPE is misleading because actual values are close to zero.
12. Identify three forms of leakage that can occur when constructing rolling features or exogenous predictors.

## Dynamic and Multivariate Models

13. Simulate a regression with AR(1) errors. Compare OLS residual autocorrelation with a regression model that includes dynamic errors.
14. Explain the difference between a predictor that Granger-causes a target and a predictor that has a causal intervention effect.
15. Simulate two independent random walks and regress one on the other. Repeat several times and observe how often apparently impressive fits occur.
16. Simulate two cointegrated $I(1)$ series. Verify that each level series appears non-stationary while an appropriate linear combination is stationary.
17. Fit a VAR to stationary multivariate data and compute an impulse response. State the assumptions needed before interpreting the response structurally.

## State Space and Frequency Domain

18. Implement the scalar local-level Kalman filter. Vary measurement variance while keeping process variance fixed and explain how the Kalman gain changes.
19. Explain the difference between filtering and smoothing. Which is valid for a real-time estimate at time $t$?
20. Simulate a sinusoid with period 12 plus noise. Use a periodogram to recover the dominant period.
21. Explain aliasing with an example in which a high-frequency signal is sampled too slowly.
22. Add a strong trend to a periodic signal and compare the periodogram before and after detrending.

## Short Solution Checks

- Exercise 1: $\gamma(0)=4$ and $\gamma(h)=0$ for nonzero lags.
- Exercise 3: with innovation variance $\sigma^2$, the random-walk variance grows linearly as $t\sigma^2$ when $X_0$ is fixed.
- Exercise 8: the residuals retain serial structure at the tested lags; revisit order, transformations, seasonality, or omitted dynamics.
- Exercise 11: percentage errors can explode or become undefined near zero; use an appropriate scale-free alternative such as MASE when suitable.
- Exercise 14: Granger causality is predictive precedence conditional on the included information set, not proof of structural causality.
- Exercise 19: filtering uses information through time $t$; smoothing can use observations after $t$ and is retrospective.
