# Regression with ARMA Errors

A regression can explain the response's relationship with observed predictors while leaving persistent departures around that relationship. **Regression with ARMA errors** models those departures as a time series. Its two equations distinguish the predictor contribution from the dynamic error; the final innovation is the new shock left after both are accounted for.

For example, temperature may explain the baseline demand level, while yesterday's positive regression error helps predict another positive departure today. The complete forecast uses both pieces. Treating the whole regression error as unpredictable would discard the second piece.

The serial error has separate implications for inference and prediction. Correlation changes the covariance of the estimated regression coefficients, making ordinary independent-error standard errors unreliable in general. It also creates forecastable structure in the error process. A robust covariance adjustment can address the first issue without addressing the second; an explicit dynamic error model can represent both under its assumptions.

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

The predictor component is 7 and the observation is 7.4, leaving a regression error of 0.4. That error is not necessarily the new innovation. If the previous regression error was 0.5, the AR(1) predicts $0.7(0.5)=0.35$ of today's departure, leaving a new innovation of only 0.05. Forecasting and residual diagnostics must distinguish these two error sequences.

![A regression mean with autocorrelated errors](https://raw.githubusercontent.com/djeada/Statistics-Notes/main/assets/time_series/student/16_dynamic_regression.png)

The figure separates the regression mean from the serial error around it. The covariates explain the systematic mean structure, while the ARMA component describes dependence that remains after conditioning on those predictors.

## Model equation and the two error sequences

In many applications, the response $y_t$ depends on observed covariates and still has autocorrelated residual variation. A **regression with ARMA errors** writes

$$
y_t=x_t^\top\beta+n_t,
$$

where the error process follows an ARMA model such as

$$
n_t=\phi_1n_{t-1}+\cdots+\phi_pn_{t-p}
+\varepsilon_t-\theta_1\varepsilon_{t-1}-\cdots-\theta_q\varepsilon_{t-q}.
$$

Here $\varepsilon_t$ is white noise. The signs on the MA coefficients are a convention; some texts and software use plus signs instead, so compare full model equations rather than parameter labels alone.

## Why This Matters

With serially correlated errors, repeated observations can contain overlapping information about the same regression relationship. Even under exogeneity sufficient for consistent slope estimation, the covariance formula based on independent errors generally misstates precision. Ignoring the dependence can therefore alter confidence intervals and tests without necessarily producing an obviously poor fitted line.

At a one-step origin, forecast the regression component from the available future predictors and forecast the error from its past. Their sum is the response forecast. In the AR(1)-error example, a current residual departure feeds forward with powers of 0.7. Replacing an error model with a robust standard error does not supply that recursion, because coefficient uncertainty and predictable residual dynamics are different quantities.

## Practical Workflow

A practical workflow is:

1. align the response and predictors and specify the regression mean;
2. inspect residual ACF/PACF and plots after fitting a simple mean model;
3. choose a parsimonious ARMA structure for the remaining serial dependence;
4. estimate the regression coefficients and error process together, commonly by maximum likelihood or generalized least squares methods;
5. check that the final standardized innovation residuals no longer contain systematic autocorrelation;
6. evaluate forecasts using only predictors and observations available at each forecast origin.

This structure combines explanatory regression with a time-series model for the unexplained dynamics.

## Decomposing departures and fitting their covariance

Write

$$
y_t=x_t^\top\beta+n_t,
\qquad
\phi(B)n_t=\theta(B)\varepsilon_t.
$$

The regression component $x_t^\top\beta$ describes the predictor relationship. The regression error $n_t$ can still be forecast from its own history, so the full conditional mean also includes $E(n_t\mid\mathcal F_{t-1})$ when the required predictors are available. The innovation $\varepsilon_t$ is the new shock after that dynamic prediction. Keeping those roles separate helps avoid using lagged error structure to compensate for a missing predictor or trend.

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

GLS reweights and combines rows so that the transformed error covariance is proportional to the identity when the specified $\Sigma$ is correct. For AR(1) errors, subtracting $\rho$ times the previous equation gives $y_t-\rho y_{t-1}$ on the left and the same transformation of **every** predictor on the right. An intercept becomes $\beta_0(1-\rho)$ rather than remaining unchanged. Transforming the response alone would fit a different model.

![Regression with dynamic errors](https://raw.githubusercontent.com/djeada/Statistics-Notes/main/assets/time_series/dynamic_multivariate/01_dynamic_regression_errors.png)

After fitting, the regression errors can still show persistent runs because the ARMA equation is designed to explain them. The estimated innovations should have much less linear serial dependence. Inspecting only the raw regression errors could wrongly reject a successful combined model; inspecting only the fitted mean could wrongly accept one whose final innovations remain structured.

### Workflow

1. Align the response and predictors on the correct timestamps.
2. Fit a simple, interpretable mean model.
3. Inspect residual ACF/PACF and squared residuals.
4. Choose a parsimonious error structure.
5. Estimate the combined model.
6. Check standardized residuals and parameter stability.
7. Backtest predictions using only information available at each forecast origin.

See [dynamic regression](https://github.com/djeada/Statistics-Notes/blob/main/notes/time_series/dynamic_regression.md) for predictor availability, lagged effects, and forecast scenarios for future covariates.

### What the forecast conditions on

A forecast using $x_{t+1}$ assumes that value is known or supplied as a scenario. If the future predictor is forecast separately, ordinary model intervals may be conditional on that supplied path and omit its uncertainty. Report that condition explicitly. When several predictors and the response feed back on one another, a joint model may be more appropriate than treating one predictor path as externally determined.

## Formula reference

| Component / case | General formula | Notes / special case |
|---|---|---|
| Regression with dynamic errors | $y_t=x_t^\top\beta+n_t$ | The regression component describes predictor effects; forecasting also uses the predictable part of $n_t$. |
| ARMA($p,q$) errors | $\phi(B)n_t=\theta(B)\varepsilon_t$ | $\varepsilon_t$ is white noise; MA sign convention can vary. |
| Combined model | $\phi(B)(y_t-x_t^\top\beta)=\theta(B)\varepsilon_t$ | Compact regression-with-ARMA-errors form. |
| AR(1) errors | $n_t=\rho n_{t-1}+\varepsilon_t$ | Stationary when $\lvert\rho\rvert<1$. |
| AR(1) quasi-difference | $y_t-\rho y_{t-1}=\beta_0(1-\rho)+\beta^\top(x_t-\rho x_{t-1})+\varepsilon_t$ | Basis of GLS-style transformations for AR(1) errors. |
| GLS estimator | $\hat\beta=(X^\top\Sigma^{-1}X)^{-1}X^\top\Sigma^{-1}y$ | Uses the error covariance matrix $\Sigma$. |
| Error covariance, stationary AR(1) | $\mathrm{Cov}(n_t,n_{t-h})=\sigma_n^2\rho^{\lvert h\rvert}$ | $\sigma_n^2=\sigma_\varepsilon^2/(1-\rho^2)$. |
| One-step forecast | $\hat y_{t+1\mid t}=x_{t+1}^\top\hat\beta+\hat n_{t+1\mid t}$ | Requires the future predictor vector $x_{t+1}$. |
| Regression with ARIMA errors | $\phi(B)(1-B)^d n_t=\theta(B)\varepsilon_t$ | Allows nonstationary error structure before differencing. |
| Dynamic-regression difference form | $\phi(B)(1-B)^d(y_t-x_t^\top\beta)=\theta(B)\varepsilon_t$ | Common ARIMAX/regression-with-ARIMA-errors representation. |
