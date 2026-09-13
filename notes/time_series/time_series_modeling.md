# Time Series Modeling

Time series modeling combines model specification, parameter estimation, model selection, and diagnostics. The aim is not simply to minimize in-sample error, but to find a parsimonious model whose residuals behave approximately like white noise and whose forecasts generalize to future observations.

### Model Fitting

For autoregressive models, ordinary or conditional least squares can often be used because the lagged observations are observed. For MA and ARMA models, the innovations are unobserved, so estimation is typically performed with maximum likelihood or related numerical methods.

### Worked Example: Fitting an AR(2) Model

Consider the AR(2) model

$$
Y_t = \beta_0 + \beta_1 Y_{t-1} + \beta_2 Y_{t-2} + \varepsilon_t.
$$

To keep the example identifiable, use a short synthetic series that does not make the lag columns perfectly collinear:

| $t$ | $Y_t$ |
|---:|---:|
| 1 | 1.0 |
| 2 | 2.0 |
| 3 | 1.5 |
| 4 | 3.0 |
| 5 | 2.5 |
| 6 | 4.0 |

Using observations $t=3,\dots,6$ gives

$$
\mathbf y =
\begin{bmatrix}
1.5\\
3.0\\
2.5\\
4.0
\end{bmatrix},
\qquad
\mathbf X =
\begin{bmatrix}
1 & 2.0 & 1.0\\
1 & 1.5 & 2.0\\
1 & 3.0 & 1.5\\
1 & 2.5 & 3.0
\end{bmatrix}.
$$

The least-squares estimator is

$$
\hat{\boldsymbol\beta}
=
(\mathbf X^\top\mathbf X)^{-1}\mathbf X^\top\mathbf y,
$$

provided $\mathbf X$ has full column rank. For this dataset,

$$
\mathbf X^\top\mathbf X
=
\begin{bmatrix}
4 & 9 & 7.5\\
9 & 21.5 & 17\\
7.5 & 17 & 16.25
\end{bmatrix},
$$

and

$$
\mathbf X^\top\mathbf y
=
\begin{bmatrix}
11\\
25\\
23.25
\end{bmatrix}.
$$

Solving the normal equations gives approximately

$$
\hat\beta_0 = 0.328,\qquad
\hat\beta_1 = 0.080,\qquad
\hat\beta_2 = 1.195.
$$

so the fitted conditional-mean equation is approximately

$$
\hat Y_t = 0.328 + 0.080Y_{t-1} + 1.195Y_{t-2}.
$$

This small example is only meant to demonstrate the mechanics of regression-style estimation for an AR model. In real time-series work, the next steps matter as much as the coefficient calculation: check stationarity assumptions, inspect residual autocorrelation, compare plausible model orders, and evaluate forecasts out of sample.

### Why the Previous Toy Dataset Was Problematic

If the observations increase by a constant amount, adjacent lag columns can become linearly dependent once an intercept is included. In that case $\mathbf X^\top\mathbf X$ is singular, so the inverse in the ordinary least-squares formula does not exist and the coefficients are not uniquely identified. Always check that the design matrix has full column rank before presenting an inverse-based calculation.

### Fitting MA and ARMA Models

An MA(2) model has the form

$$
Y_t = \mu + \varepsilon_t + \theta_1\varepsilon_{t-1}+\theta_2\varepsilon_{t-2}.
$$

Unlike the AR case, the lagged innovations are not observed. Treating them as if they were ordinary regressors is therefore not valid. Practical estimation generally uses maximum likelihood, innovations algorithms, or state-space methods implemented by statistical software. Methods such as Hannan-Rissanen can also provide useful starting estimates for ARMA models.

### Comparison of Common Models

| Model | Main idea | Typical use | Important assumptions / cautions |
|---|---|---|---|
| **AR($p$)** | Current value depends on past values | Short-memory stationary dependence | Usually modeled as stationary after any required transformation/differencing |
| **MA($q$)** | Current value depends on current/past innovations | Short-lived shock effects | Innovations are unobserved; invertibility is important for identification |
| **ARMA($p,q$)** | Combines AR and MA terms | Stationary linear series | Requires parsimonious order selection and residual diagnostics |
| **ARIMA($p,d,q$)** | ARMA after differencing | Integrated/non-stationary series | Avoid unnecessary differencing; diagnose the differenced model |
| **SARIMA** | ARIMA plus seasonal AR/MA/differencing | Regular seasonal structure | Seasonal period and seasonal differencing must be chosen carefully |
| **SES / Holt / Holt-Winters / ETS** | Recursive level/trend/seasonal smoothing | Forecasting level, trend, and seasonal patterns | Different ETS structures imply different error/trend/seasonal behavior |
| **VAR** | Several series depend on their joint lags | Multivariate linear dynamics | Stationarity/cointegration and lag-order choices matter; predictive precedence is not automatically causal |
| **ARCH/GARCH** | Conditional variance evolves over time | Volatility clustering | Models the variance dynamics, often after specifying a conditional mean model |

### A Practical Identification and Validation Workflow

1. **Explore the series.** Plot the data and identify trend, seasonality, outliers, missing values, structural breaks, and changing variance.
2. **Assess stationarity.** Use plots, ACF behavior, and tests such as ADF/KPSS as supporting evidence rather than relying on a single test.
3. **Transform when needed.** Apply variance-stabilizing transformations, detrending, ordinary differencing, or seasonal differencing when justified.
4. **Propose candidate orders.** Use ACF/PACF patterns together with domain knowledge; do not treat cutoff heuristics as infallible rules.
5. **Estimate parameters.** Use an estimation method appropriate to the model class.
6. **Compare parsimonious candidates.** AIC, AICc, and BIC are useful for comparing likelihood-based models fit to the same response data.
7. **Diagnose residuals.** Inspect residual plots and residual ACF/PACF and use tests such as Ljung-Box. Remaining serial dependence indicates model inadequacy.
8. **Evaluate forecasts temporally.** Preserve time order with a holdout period, expanding-window evaluation, or rolling-origin evaluation. Randomly shuffled cross-validation is generally inappropriate for forecasting because it leaks future information into model training.

### ARMA Identification and Estimation Checklist

For a stationary series, a common ARMA workflow is:

1. Choose candidate orders $p$ and $q$ using ACF/PACF patterns and domain knowledge.
2. Decide whether a mean/intercept term is appropriate and center the series when useful.
3. Estimate AR/MA coefficients with an appropriate numerical method.
4. Estimate the innovation variance $\sigma^2$.
5. Compare candidate models using diagnostics and information criteria.
6. Check that residuals do not retain material serial dependence.

For pure AR models, Yule-Walker or Burg estimates can be useful. Innovations algorithms are useful for MA structure, while Hannan-Rissanen can provide starting estimates for ARMA models before likelihood optimization.

### Order Selection with AICc

The **Akaike Information Criterion with correction (AICc)** adjusts AIC for finite samples. One common form is

$$
\operatorname{AICc}
=
\operatorname{AIC}
+
\frac{2k(k+1)}{n-k-1},
$$

where $k$ is the number of estimated parameters used in the likelihood and $n$ is the effective sample size. Lower values indicate a better tradeoff between fit and complexity among models fitted to comparable data. Parameter-count conventions vary by implementation, so the software documentation should be checked when reproducing exact AICc values.

### Parameter Redundancy

An over-parameterized ARMA model can sometimes represent a simpler process if its AR and MA polynomials share common factors. Such cancellations make parameters redundant and can cause identification problems. Prefer reduced representations without common AR/MA factors.

### Model Selection Is Not Only About Fit

A more complex model can always reduce some in-sample error, but that does not guarantee better forecasting. Prefer the simplest model that captures the important dependence structure, passes residual diagnostics reasonably well, and performs competitively on future or pseudo-future observations.

### Connections to Other Notes

- See **[stationarity.md](stationarity.md)** before interpreting AR/MA/ARIMA models.
- See **[autocorrelation_function.md](autocorrelation_function.md)** for ACF/PACF-based identification.
- See **[autoregressive_models.md](autoregressive_models.md)** and **[moving_average_models.md](moving_average_models.md)** for model-specific properties.
- See **[arima_models.md](arima_models.md)** for differencing and seasonal ARIMA models.
- See **[randomness_tests.md](randomness_tests.md)** for residual checks.
- See **[forecasting.md](forecasting.md)** for forecast construction and evaluation metrics.
