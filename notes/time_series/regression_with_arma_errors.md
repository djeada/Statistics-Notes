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
