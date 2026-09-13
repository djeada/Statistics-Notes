# Dynamic Regression

## Worked calculation: an external predictor and a lag

Suppose

$$
y_t=2+1.5x_t+n_t.
$$

For $x_t=4$ and $n_t=0.3$, the observed value is

$$
y_t=2+1.5(4)+0.3=8.3.
$$

If the response takes time to react, use a distributed lag such as

$$
y_t=2+1.0x_t+0.5x_{t-1}+n_t.
$$

When $x_t=4$ and $x_{t-1}=2$, the regression mean is $2+4+1=7$. For forecasting, that calculation is valid only if both predictor values would be available at the forecast origin. A realized future temperature, exchange rate, or policy variable may need its own forecast.

![Dynamic regression with serially correlated errors](../../assets/time_series/student/16_dynamic_regression.png)

Dynamic regression combines explanatory variables with time-series structure. It is useful when the target depends on external predictors but ordinary regression leaves autocorrelated residuals.

A basic model is

$$
y_t=\beta_0+\beta_1x_{1,t}+\cdots+\beta_kx_{k,t}+n_t,
$$

where the error process $n_t$ follows an ARMA or ARIMA model. If $n_t$ follows ARMA$(p,q)$,

$$
\phi(B)n_t=\theta(B)\varepsilon_t.
$$

Ignoring residual autocorrelation can invalidate ordinary standard-error calculations and waste forecastable structure even when coefficient estimates remain unbiased under suitable exogeneity assumptions.

## Lagged Predictors

A distributed-lag model may include current and past predictor values:

$$
y_t=\beta_0+\beta_0^{(x)}x_t+\beta_1^{(x)}x_{t-1}+\cdots+\beta_r^{(x)}x_{t-r}+n_t.
$$

Use lags when the domain suggests delayed responses; avoid mechanically adding many correlated lags.

## Future Predictor Availability

Future predictor values must be known or forecast separately. Calendar variables or scheduled promotions may be known in advance; weather and macroeconomic predictors usually are not. Evaluating with realized future predictors when they would not have been available creates leakage.

The label **ARIMAX** is used inconsistently across software. Inspect the exact model equation rather than relying on the name.

A useful predictor is not automatically causal. Temporal ordering helps forecasting but does not by itself identify interventions.

A practical workflow is: align timestamps, define what will be known at forecast time, fit the regression mean structure, inspect residual ACF/PACF, add dynamic error structure when justified, diagnose again, and backtest the complete procedure.

See [regression with ARMA errors](regression_with_arma_errors.md), [`dynamic_regression.py`](../../scripts/time_series/dynamic_regression.py), and the companion [notebook](../../notebooks/time_series/dynamic_regression.ipynb).

## Student guide: separate the mean, the errors, and the information set

Dynamic regression is easiest to understand as three linked questions:

1. What variables explain the conditional mean of $y_t$?
2. What serial structure remains in the regression error?
3. Which predictor values will actually be available when a forecast is issued?

Treating these as one question leads to common errors. A strong contemporaneous regression relationship does not guarantee white residuals, and a predictor that is useful with realized future values may be unusable in a real forecast.

### A complete model equation

A regression with ARMA errors can be written

$$
y_t=\beta^\top x_t+n_t,
$$

with

$$
\phi(B)n_t=\theta(B)\varepsilon_t.
$$

For example, with one predictor and AR(1) errors:

$$
y_t=\beta_0+\beta_1x_t+n_t,
\qquad
n_t=\phi n_{t-1}+\varepsilon_t.
$$

If $\beta_0=2$, $\beta_1=1.5$, $x_t=4$, and $n_t=0.3$, then

$$
E(y_t\mid x_t,\text{past errors})=2+1.5(4)=8,
\qquad
y_t=8.3.
$$

The regression mean and the realized observation are different objects. The dynamic error model explains why nearby observations can depart from the mean in a related way.

### Why OLS residual checks matter

Suppose ordinary least squares produces residuals with lag-1 autocorrelation $0.75$. Even if the slope estimate is unbiased under strict exogeneity, the usual independent-error standard error is not the correct measure of uncertainty. The residual process contains information that can improve forecasts.

Use three residual views:

- residuals against time, for trend, breaks, and changing variance;
- residual ACF/PACF, for remaining serial dependence;
- squared residuals, for conditional variance dependence.

An error model is useful only if it improves the complete forecast experiment. A dynamic error term that reduces AIC but fails on future-like origins is not automatically preferable.

### Distributed lags

An external effect may be delayed:

$$
y_t=\beta_0+\beta_0^{(x)}x_t+\beta_1^{(x)}x_{t-1}
\cdots+\beta_r^{(x)}x_{t-r}+n_t.
$$

For the numerical example

$$
y_t=2+1.0x_t+0.5x_{t-1}+n_t,
$$

with $x_t=4$, $x_{t-1}=2$, and $n_t=0.3$, the regression mean is

$$
2+1(4)+0.5(2)=7,
$$

and the observation is $7.3$.

The sum of lag coefficients, $1.5$ in this example, describes the total long-run effect only under additional stability and interpretation assumptions. Adjacent predictors are often correlated, so adding many lags can make individual coefficients unstable. Use domain timing, regularization, polynomial distributed lags, or a transfer-function representation when a long lag response is plausible.

### Exogenous predictors and future availability

Create an explicit availability table before fitting:

| predictor | value at $t$ known? | value at $t+1$ known? | treatment |
|---|---|---|---|
| day-of-week | yes | yes | include directly |
| scheduled promotion | yes if schedule is fixed | usually yes | include with a documented schedule |
| weather | observed through $t$ | no | forecast weather or omit |
| policy rate | depends on release timing | often no | use a real-time vintage or forecast |

If a dynamic regression is evaluated with the realized future weather, the result answers a different question: performance conditional on perfect weather information. That may be useful for diagnosis, but it is not the same as an operational forecast.

When $x_{t+h}$ must be forecast, uncertainty from the predictor forecast should flow into the uncertainty for $y_{t+h}$. Plugging in a single future predictor path usually understates total forecast uncertainty.

### Transformations and alignment

Before fitting:

1. align timestamps and sampling frequency;
2. inspect release delays and revisions;
3. decide whether levels, differences, growth rates, or log values match the scientific question;
4. check whether transformations preserve the timing of information;
5. document missing-value treatment.

A one-period shift can change the model from forecasting with past information to using a future observation. Use a small table of timestamps to verify the lag convention.

### Estimation choices

For a mean equation with serially correlated errors, common approaches include:

- maximum likelihood for regression with ARIMA errors;
- generalized least squares when a covariance model is specified;
- regression followed by a model for residuals;
- state-space estimation when missing values, latent effects, or time-varying coefficients matter.

The two-step residual approach is useful for teaching and initialization but does not always give the same estimates or uncertainty as joint maximum likelihood. Inspect the software's treatment of intercepts, differencing, missing observations, and exogenous variables.

### Interpretation and causality

The coefficient $\beta_j$ describes a conditional association within the specified model. It is not automatically a causal effect. Confounding, reverse feedback, common trends, omitted variables, measurement timing, and interventions can all invalidate a causal interpretation.

Granger predictability asks whether past values of a predictor improve conditional prediction. It does not establish that changing the predictor would change the target. A useful forecast variable can be a proxy for an unobserved process.

### A complete workflow

1. Define the forecast target and forecast origin.
2. Draw the target and each predictor on the same time axis.
3. Decide which future predictor values are known, scheduled, or forecast.
4. Choose transformations and lags from timing and subject-matter reasoning.
5. Fit the mean equation.
6. Inspect residual ACF, PACF, variance, and breaks.
7. Add dynamic error structure only where it addresses a diagnosed problem.
8. Recheck residuals and parameter stability.
9. Backtest the entire predictor-plus-target procedure.
10. Report coefficient interpretation separately from forecasting performance.

### Visual companions

Run [dynamic_multivariate_visualizations.py](../../scripts/time_series/dynamic_multivariate_visualizations.py) to generate the figures below:

![Dynamic regression errors](../../assets/time_series/dynamic_multivariate/01_dynamic_regression_errors.png)

![Distributed lag](../../assets/time_series/dynamic_multivariate/02_distributed_lag.png)

![Future predictor availability](../../assets/time_series/dynamic_multivariate/03_future_predictor_availability.png)

![VAR feedback](../../assets/time_series/dynamic_multivariate/04_var_feedback.png)

![Granger predictability](../../assets/time_series/dynamic_multivariate/05_granger_predictability.png)

![Cointegrating spread](../../assets/time_series/dynamic_multivariate/06_cointegrating_spread.png)

![VECM adjustment](../../assets/time_series/dynamic_multivariate/07_vecm_adjustment.png)

![Impulse response](../../assets/time_series/dynamic_multivariate/08_impulse_response.png)
