# Regression with ARMA Errors

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
