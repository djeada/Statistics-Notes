# Dynamic Regression

Suppose electricity demand depends on temperature, but errors from a temperature-only regression stay positive for several days in a row. The predictor explains one source of movement; the residual runs suggest another. **Dynamic regression** represents both the predictor relationship and the remaining time-series dependence instead of asking either component to explain everything.

It can also allow delayed predictor effects. An advertising change today may affect several later periods, while yesterday's unexplained deviation can still help predict today's. Lagged predictors describe the first mechanism; a serial error model describes the second.

A forecast additionally needs a source for future predictor values. Tomorrow's weekday is known now; tomorrow's weather is not. A statistically useful relationship can therefore be easy to estimate retrospectively but difficult to use operationally. Define when each predictor becomes available, whether it is revised, and how its future path will be obtained before interpreting the model's forecasting accuracy.

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

When $x_t=4$ and $x_{t-1}=2$, the regression mean is

$$
2+4+1=7.
$$

For forecasting, that calculation is valid only if the required predictor values would be available at the forecast origin. A realized future temperature, exchange rate, or policy variable may itself need to be forecast.

![Dynamic regression with serially correlated errors](https://raw.githubusercontent.com/djeada/Statistics-Notes/main/assets/time_series/student/16_dynamic_regression.png)

The figure separates two sources of structure: the regression mean follows an external predictor, while serial dependence remains in the errors around that mean. Dynamic regression models both pieces rather than forcing the predictor to explain all temporal dependence.

## Regression component, serial error, and innovation

Dynamic regression combines explanatory variables with time-series structure. It is useful when the target depends on external predictors but an ordinary regression leaves autocorrelated errors. The fitted innovation residuals from the complete model, rather than the regression errors alone, are the quantities checked for remaining linear dependence.

A basic model is

$$
y_t=\beta_0+\beta_1x_{1,t}+\cdots+\beta_kx_{k,t}+n_t,
$$

where the error process $n_t$ follows an ARMA or ARIMA model. If $n_t$ follows ARMA($p,q$),

$$
\phi(B)n_t=\theta(B)\varepsilon_t.
$$

With exogenous predictors and suitable regularity conditions, serial correlation need not prevent consistent estimation of the regression coefficients by OLS. It does invalidate the usual independent-error covariance formula in general, and it leaves the predictable part of the serial error unused in forecasts. These conclusions require the exogeneity assumptions to be stated; autocorrelation does not excuse an endogenous predictor.

![Dynamic regression errors](https://raw.githubusercontent.com/djeada/Statistics-Notes/main/assets/time_series/dynamic_multivariate/01_dynamic_regression_errors.png)

Consecutive positive regression errors mean that the predictor component is repeatedly below the observed series. An AR error can carry part of that departure into the next prediction. The final innovation is the difference after both the predictor contribution and the forecastable error contribution have been used. Check that innovation sequence for remaining correlation; the regression error itself is correlated by construction.

## Lagged Predictors

A distributed-lag model may include current and past predictor values:

$$
y_t=\beta_0+\beta_0^{(x)}x_t+\beta_1^{(x)}x_{t-1}+\cdots+\beta_r^{(x)}x_{t-r}+n_t.
$$

Choose predictor lags from a plausible response timetable and from the forecasting information set. Several adjacent lags of a persistent predictor often move together, so their separate coefficients can be difficult to estimate. A large positive coefficient at one lag and a large negative coefficient at the next may reflect this instability rather than a meaningful reversal. Examine the combined response and consider parsimonious lag restrictions or regularization when many delays are plausible.

![Distributed lag](https://raw.githubusercontent.com/djeada/Statistics-Notes/main/assets/time_series/dynamic_multivariate/02_distributed_lag.png)

The figure illustrates how one change in $x_t$ can influence the response across several later periods. The lag coefficients describe the shape and duration of that response.

## Future Predictor Availability

Future predictor values must be known or forecast separately. Calendar variables and scheduled promotions may be available in advance; future weather and macroeconomic quantities usually are not. Evaluating a model with realized future predictors that would not have been available creates information leakage.

![Future predictor availability](https://raw.githubusercontent.com/djeada/Statistics-Notes/main/assets/time_series/dynamic_multivariate/03_future_predictor_availability.png)

The visual distinguishes predictors that are known at the forecast origin from those that must themselves be forecast. This distinction determines whether a reported forecast is operationally reproducible.

The name **ARIMAX** does not uniquely specify where the predictor enters. A regression whose residual follows ARIMA and an ARMAX equation with predictors inside an autoregressive response equation can give different coefficient interpretations and forecast recursions. Write the expanded equation, including differencing and intercepts. Then check the software's parameterization against that equation rather than assuming the label supplies the model.

A useful predictor is not automatically causal. Temporal ordering can support forecasting, but it does not by itself identify the effect of an intervention.

A practical workflow is to align timestamps, define what will be known at forecast time, fit the regression mean, inspect residual dependence, add dynamic error structure when justified, diagnose the combined model, and backtest the complete procedure.

See [regression with ARMA errors](https://github.com/djeada/Statistics-Notes/blob/main/notes/time_series/regression_with_arma_errors.md) and the companion [notebook](https://github.com/djeada/Statistics-Notes/blob/main/notebooks/time_series/dynamic_regression.ipynb).

## Predictor effects, serial errors, and usable future information

Dynamic regression is easiest to understand as three linked questions:

1. What variables explain the conditional mean of $y_t$?
2. What serial structure remains in the regression error?
3. Which predictor values will actually be available when a forecast is issued?

Treating these as one question leads to common mistakes. A strong contemporaneous regression relationship does not guarantee white residuals, and a predictor that is useful when its future values are known may be unusable in a real forecast.

### A complete model equation

A regression with ARMA errors can be written

$$
y_t=\beta^\top x_t+n_t,
$$

with

$$
\phi(B)n_t=\theta(B)\varepsilon_t.
$$

For example, with one predictor and AR(1) errors,

$$
y_t=\beta_0+\beta_1x_t+n_t,
\qquad
n_t=\phi n_{t-1}+\varepsilon_t.
$$

If $\beta_0=2$, $\beta_1=1.5$, $x_t=4$, and $n_t=0.3$, then the regression mean is

$$
2+1.5(4)=8,
$$

and the realized observation is

$$
y_t=8.3.
$$

The value 8 is the predictor contribution; adding the serial error 0.3 gives the observation 8.3. Before observing it, the forecast may already include a predicted part of that 0.3 from earlier errors. The coefficient 1.5 therefore describes the regression component, while the complete one-step mean combines that component with the dynamic error forecast. This separation matters when interpreting fitted values and residual plots.

### Why OLS residual checks matter

A residual lag-1 correlation of 0.75 says that nearby regression errors have substantial linear association. Under suitable exogeneity, OLS can still estimate the predictor slope consistently, but the independent-error standard-error formula ignores that association. For forecasting, the pattern also suggests information left unused by the mean-only prediction. These are two consequences of the same residual structure: one concerns coefficient uncertainty, the other the forecast equation.

Use three complementary residual views:

- residuals over time, for trend, breaks, and changing variance;
- residual ACF/PACF, for remaining serial dependence;
- squared residuals, for conditional variance dependence.

An error model is useful only if it improves the complete forecast experiment. A dynamic error term that lowers AIC but fails at historical forecast origins is not automatically preferable.

### Distributed lags

An external effect may be delayed:

$$
y_t=\beta_0+\beta_0^{(x)}x_t+\beta_1^{(x)}x_{t-1}+\cdots+\beta_r^{(x)}x_{t-r}+n_t.
$$

For

$$
y_t=2+1.0x_t+0.5x_{t-1}+n_t,
$$

with $x_t=4$, $x_{t-1}=2$, and $n_t=0.3$, the regression mean is

$$
2+1(4)+0.5(2)=7,
$$

and the observation is $7.3$.

The coefficient sum, $1.5$ here, has a specific path interpretation in this finite distributed-lag equation. A permanent one-unit increase in $x$ raises the regression component by 1.5 once both included predictor lags reflect the increase. A one-period pulse instead produces effects of 1.0 and 0.5 in successive periods, also summing to 1.5. Neither interpretation alone establishes a causal effect. When many correlated lags are plausible, domain timing, regularization, polynomial distributed lags, or transfer-function models can provide more stable descriptions.

### Exogenous predictors and future availability

Create an explicit availability table before fitting:

| predictor | value at $t$ known? | value at $t+1$ known? | treatment |
|---|---|---|---|
| day-of-week | yes | yes | include directly |
| scheduled promotion | yes if schedule is fixed | usually yes | include with a documented schedule |
| weather | observed through $t$ | no | forecast weather or omit |
| policy rate | depends on release timing | often no | use a real-time vintage or forecast |

If a dynamic regression is evaluated with realized future weather, the result measures performance conditional on perfect future weather information. That can be useful for diagnosis, but it is not the same as an operational forecast.

If the predictor must itself be forecast, the response forecast is uncertain both because of future response shocks and because of the unknown predictor path. A plug-in calculation conditions on one assumed path and usually omits the second source. One way to represent it is to generate plausible future predictor paths, produce response forecasts conditional on each path, and combine the resulting distributions under explicitly stated assumptions.

### Transformations and alignment

Before fitting:

1. align timestamps and sampling frequencies;
2. inspect release delays and revisions;
3. decide whether levels, differences, growth rates, or logs match the scientific question;
4. verify that transformations preserve the intended information timing;
5. document missing-value treatment.

Verify timing with a few explicit rows. For a forecast issued after date $t$, list the target $y_{t+h}$ and the actual publication dates of every predictor value used. A predictor labeled with month $t$ may have been published in month $t+1$, and revised historical data may differ from the vintage available at the origin. Row labels alone do not establish availability.

### Estimation choices

For a mean equation with serially correlated errors, common approaches include maximum likelihood for regression with ARIMA errors, generalized least squares under a specified covariance model, two-step regression followed by residual modeling, and state-space estimation when missing values or time-varying latent effects matter.

A two-step approach first estimates a regression while treating the errors one way, then models residuals that depend on those estimates. Joint estimation can revise the regression coefficients as it learns the error covariance, so the resulting parameters and uncertainty need not agree. Two-step fitting remains useful for exploration and initialization, but report it as that procedure rather than as an automatic substitute for joint likelihood or GLS.

### Interpretation and causality

A coefficient describes how the modeled regression component changes when a predictor changes with the other included terms held fixed. It becomes a causal intervention effect only with additional identification assumptions. Common trends, feedback, omitted drivers, and measurement timing can all create a useful forecast association without supporting that intervention interpretation. Specify the predictive or causal objective before giving the coefficient a substantive meaning.

Granger predictability asks whether past values of one series improve prediction of another after conditioning on the included information. It is a predictive concept, not a guarantee that intervening on the predictor would change the target.

![Granger predictability](https://raw.githubusercontent.com/djeada/Statistics-Notes/main/assets/time_series/dynamic_multivariate/05_granger_predictability.png)

The figure illustrates the predictive question: does adding the past of one series improve forecasts beyond the target's own history and other included variables?

When several variables respond to one another, a joint multivariate model can make that feedback explicit. A single-equation forecast must still justify how the predictor path is obtained and how its relationship with the error process is handled.

![VAR feedback](https://raw.githubusercontent.com/djeada/Statistics-Notes/main/assets/time_series/dynamic_multivariate/04_var_feedback.png)

The VAR figure shows reciprocal lagged dependence, where each series can respond to the history of the others. This is different from treating one predictor as externally determined.

Related multivariate models also handle shared stochastic trends and dynamic responses to system-wide shocks.

![Cointegrating spread](https://raw.githubusercontent.com/djeada/Statistics-Notes/main/assets/time_series/dynamic_multivariate/06_cointegrating_spread.png)

A cointegrating spread can remain stable even when the component series are individually non-stationary.

![VECM adjustment](https://raw.githubusercontent.com/djeada/Statistics-Notes/main/assets/time_series/dynamic_multivariate/07_vecm_adjustment.png)

The VECM figure shows how deviations from a long-run equilibrium can feed into subsequent changes.

![Impulse response](https://raw.githubusercontent.com/djeada/Statistics-Notes/main/assets/time_series/dynamic_multivariate/08_impulse_response.png)

An impulse-response plot traces the model-implied effect of a specified system shock over future periods. Its interpretation depends on the multivariate identification assumptions, not only on temporal ordering.

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

## Formula reference

| Component / case | General formula | Notes / special case |
|---|---|---|
| Static regression mean | $y_t=\beta_0+\beta^\top x_t+n_t$ | $n_t$ may still be serially dependent. |
| ARMA errors | $\phi(B)n_t=\theta(B)\varepsilon_t$ | Gives regression with ARMA errors. |
| ARIMA errors | $\phi(B)(1-B)^dn_t=\theta(B)\varepsilon_t$ | Allows an integrated error process before differencing. |
| Combined dynamic regression | $\phi(B)(1-B)^d[y_t-\beta_0-\beta^\top x_t]=\theta(B)\varepsilon_t$ | One common ARIMAX/regression-with-ARIMA-errors form. |
| Distributed lag | $y_t=\beta_0+\sum_{j=0}^{r}\beta_j^{(x)}x_{t-j}+n_t$ | Captures delayed predictor effects. |
| Cumulative lag effect | $\sum_{j=0}^{r}\beta_j^{(x)}$ | Interpretable as a total response only under an appropriate sustained-change scenario. |
| Transfer-function form | $y_t=\beta_0+\frac{\omega(B)}{\delta(B)}B^b x_t+n_t$ | Generalizes finite distributed lags with delay $b$. |
| One-step forecast | $\hat y_{t+1\mid t}=\hat\beta_0+\hat\beta^\top x_{t+1}+\hat n_{t+1\mid t}$ | Requires $x_{t+1}$ to be known or separately forecast. |
| $h$-step forecast | $\hat y_{t+h\mid t}=\hat\beta_0+\hat\beta^\top x_{t+h}+\hat n_{t+h\mid t}$ | Predictor-path uncertainty should be included when future $x$ is forecast. |
| Intervention pulse | $P_t=I(t=T_0)$ | Models a one-period event. |
| Intervention step | $S_t=I(t\ge T_0)$ | Models a persistent level shift. |
| AR(1) dynamic error | $n_t=\phi n_{t-1}+\varepsilon_t$ | Stationary when $\lvert\phi\rvert<1$. |
