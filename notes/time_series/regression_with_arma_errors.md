# Regression with ARMA Errors

## Worked calculation: a regression mean plus serial error

Consider

$$
y_t=1+2x_t+n_t,
\qquad
n_t=0.7n_{t-1}+\varepsilon_t.
$$

If $x_t=3$ and the current error happens to be $n_t=0.4$, then the observed value is

$$
y_t=1+2(3)+0.4=7.4.
$$

The regression mean is $1+2(3)=7$, but the error is not independent from the previous error. Ordinary least squares may estimate the mean slope reasonably under exogeneity, yet its usual standard errors assume a dependence structure that is not present here. Modeling the ARMA error uses the predictable part of $n_t$ and produces more appropriate forecasts and uncertainty estimates.

![A regression mean with autocorrelated errors](../../assets/time_series/student/16_dynamic_regression.png)

In many applications, we want to explain a response series $Y_t$ using covariates while still accounting for autocorrelation. A standard approach is **regression with ARMA errors**:

$$
Y_t = \beta^T X_t + R_t
$$

where the residual process $R_t$ follows an ARMA model:

$$
R_t = \phi_1 R_{t-1} + \cdots + \phi_p R_{t-p} + Z_t - \theta_1 Z_{t-1} - \cdots - \theta_q Z_{t-q}
$$

with $Z_t$ as white noise.

### Why This Matters

- Ordinary least squares assumes independent errors.  
- Autocorrelated residuals lead to **biased standard errors** and misleading inference.  
- Modeling the residuals as ARMA provides more reliable uncertainty estimates.  

### Practical Workflow

1. **Fit a regression model** for the deterministic part ($\beta^T X_t$).
2. **Inspect residuals** using ACF/PACF to identify ARMA structure.
3. **Fit the combined model** with ARMA errors using MLE or GLS.
4. **Validate residuals** to confirm they resemble white noise.

This approach blends explanatory modeling (regression) with time series dependence (ARMA), which is common in econometrics and forecasting.

## Student guide: estimate the mean and the error process together

Let

$$
y_t=x_t^\top\beta+n_t,
\qquad
\phi(B)n_t=\theta(B)\varepsilon_t.
$$

The regression part answers how the target changes with the predictors, conditional on the error process. The ARMA part explains serial structure left after the mean has been modeled.

### Numerical example

Suppose

$$
y_t=1+2x_t+n_t,
\qquad
n_t=0.7n_{t-1}+\varepsilon_t.
$$

For $x_t=3$ and $n_t=0.4$, the observation is

$$
y_t=1+2(3)+0.4=7.4.
$$

The regression mean is 7. If the previous error was $n_{t-1}=0.5$, the predictable part of the current error is $0.35$ and the innovation is $0.05$.

### Why ordinary least squares can mislead

Under suitable exogeneity, OLS can estimate $\beta$ consistently even when the errors are autocorrelated. The usual independent-error variance estimator, however, is generally wrong. Serial dependence also means that a model of the error can improve forecasts.

A heteroskedasticity-and-autocorrelation robust covariance estimate may improve inference about $\beta$, but it does not by itself produce dynamic forecasts or model the serial error process. Regression with ARMA errors addresses a different objective.

### GLS intuition

If the error covariance matrix $\Sigma$ were known, generalized least squares would use

$$
\hat\beta_{\mathrm{GLS}}
=(X^\top\Sigma^{-1}X)^{-1}X^\top\Sigma^{-1}y.
$$

The weights account for the fact that observations carry overlapping information. In practice, $\Sigma$ is estimated jointly or iteratively, so misspecification of the ARMA error matters.

### Workflow

1. Align response and predictors.
2. Fit a simple mean model.
3. Inspect residual ACF/PACF and squared residuals.
4. Choose a parsimonious error structure.
5. Estimate the combined model.
6. Check standardized residuals.
7. Backtest predictions using only information available at each origin.

See [dynamic regression](dynamic_regression.md) for predictor availability and lagged effects.

![Regression with dynamic errors](../../assets/time_series/dynamic_multivariate/01_dynamic_regression_errors.png)
