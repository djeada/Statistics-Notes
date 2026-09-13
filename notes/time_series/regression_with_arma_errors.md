# Regression with ARMA Errors

Regression with ARMA errors separates two kinds of structure that often appear together in time series. The regression explains how observed predictors shift the conditional mean, while the ARMA component models serial dependence that remains in the unexplained part.

This distinction matters for both inference and forecasting. Autocorrelated errors change the uncertainty around regression coefficients and can contain additional predictive information, so a good model must handle the mean relationship and the temporal error process as parts of one coherent specification.

## Worked calculation: a regression mean plus serial error

Consider

$$
y_t=1+2x_t+n_t,
\qquad
n_t=0.7n_{t-1}+\varepsilon_t.
$$

If $x_t=3$ and the current error happens to be $n_t=0.4$, then

$$
y_t=1+2(3)+0.4=7.4.
$$

The regression mean is $1+2(3)=7$, but the error is serially dependent. Under suitable exogeneity, ordinary least squares can still estimate the mean coefficients consistently, but the usual independent-error standard errors and forecast formulas are no longer appropriate. Modeling the ARMA error captures the predictable part of $n_t$ and produces uncertainty estimates that reflect the temporal dependence.

![A regression mean with autocorrelated errors](../../assets/time_series/student/16_dynamic_regression.png)

The figure separates the regression mean from the serial error around it. The covariates explain the systematic mean structure, while the ARMA component describes dependence that remains after conditioning on those predictors.

In many applications, the response $Y_t$ depends on observed covariates and still has autocorrelated residual variation. A **regression with ARMA errors** writes

$$
Y_t=\beta^TX_t+R_t,
$$

where the error process follows an ARMA model such as

$$
R_t=\phi_1R_{t-1}+\cdots+\phi_pR_{t-p}
+Z_t-\theta_1Z_{t-1}-\cdots-\theta_qZ_{t-q}.
$$

Here $Z_t$ is white noise. The signs on the MA coefficients are a convention; some texts and software use plus signs instead, so compare full model equations rather than parameter labels alone.

### Why This Matters

Serially correlated errors affect both inference and forecasting. Even when the regression coefficients remain consistently estimable under appropriate exogeneity assumptions, the ordinary independent-error covariance formula is generally wrong. Ignoring residual dependence can therefore produce misleading standard errors, confidence intervals, and tests.

A fitted error process also improves dynamic forecasts because part of the current residual may be predictable from previous residuals. This is different from merely adjusting standard errors after fitting the mean model.

### Practical Workflow

A practical workflow is:

1. align the response and predictors and specify the regression mean;
2. inspect residual ACF/PACF and plots after fitting a simple mean model;
3. choose a parsimonious ARMA structure for the remaining serial dependence;
4. estimate the regression coefficients and error process together, commonly by maximum likelihood or generalized least squares methods;
5. check that the final standardized residuals no longer contain systematic autocorrelation;
6. evaluate forecasts using only predictors and observations available at each forecast origin.

This structure combines explanatory regression with a time-series model for the unexplained dynamics.

## Student guide: estimate the mean and the error process together

Write

$$
y_t=x_t^\top\beta+n_t,
\qquad
\phi(B)n_t=\theta(B)\varepsilon_t.
$$

The regression part describes how the conditional mean changes with the predictors. The ARMA part describes serial dependence left after that mean has been specified. Keeping those roles separate helps avoid using lagged error structure to compensate for a missing predictor or trend.

### Numerical example

Suppose

$$
y_t=1+2x_t+n_t,
\qquad
n_t=0.7n_{t-1}+\varepsilon_t.
$$

For $x_t=3$ and $n_t=0.4$,

$$
y_t=1+2(3)+0.4=7.4.
$$

The regression mean is 7. If $n_{t-1}=0.5$, the predictable AR contribution to the current error is

$$
0.7(0.5)=0.35,
$$

so the innovation is

$$
\varepsilon_t=0.4-0.35=0.05.
$$

This decomposition shows how the observed value can depart from the regression mean in a way that is partly predictable from earlier errors and partly new information.

### Why ordinary least squares can mislead

Under suitable exogeneity, OLS can estimate $\beta$ consistently even when the errors are autocorrelated. Its usual independent-error variance estimator, however, is generally invalid, and OLS is no longer efficient among linear unbiased estimators when the covariance structure is known.

A heteroskedasticity-and-autocorrelation robust covariance estimator can improve inference about $\beta$ without specifying a full dynamic error model. It does not, by itself, model the serial errors or provide the same recursive forecasts. Choose between these approaches according to the inferential or forecasting objective.

### GLS intuition

If the error covariance matrix $\Sigma$ were known, generalized least squares would estimate

$$
\hat\beta_{\mathrm{GLS}}
=(X^\top\Sigma^{-1}X)^{-1}X^\top\Sigma^{-1}y.
$$

The transformation accounts for the fact that observations with correlated errors contain overlapping information. In practice, $\Sigma$ is unknown and must be estimated from the ARMA parameters, often jointly or iteratively. Misspecifying the error model can therefore affect both coefficient uncertainty and forecasts.

![Regression with dynamic errors](../../assets/time_series/dynamic_multivariate/01_dynamic_regression_errors.png)

The figure illustrates this joint view: the regression component follows the predictor-driven mean, while the dynamic error model accounts for systematic departures around it.

### Workflow

1. Align the response and predictors on the correct timestamps.
2. Fit a simple, interpretable mean model.
3. Inspect residual ACF/PACF and squared residuals.
4. Choose a parsimonious error structure.
5. Estimate the combined model.
6. Check standardized residuals and parameter stability.
7. Backtest predictions using only information available at each forecast origin.

See [dynamic regression](dynamic_regression.md) for predictor availability, lagged effects, and forecast scenarios for future covariates.
