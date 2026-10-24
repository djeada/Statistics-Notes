# Time Series Modeling

Fitting a time-series model means more than finding coefficients for an equation. The procedure chooses a target, decides how trend and seasonality enter, handles missing observations, estimates dynamic parameters, and produces forecasts from a defined information set. Any of those decisions can affect the result as much as changing an AR or MA order.

A useful modeling exercise makes each decision checkable. We should be able to say what was fitted, which observations supplied each predictor, how a forecast was constructed, and what the residuals reveal about the assumptions.

Model assessment has three distinct parts. Training fit measures how well the fitted equation describes the data used to estimate it. Diagnostics examine whether that equation has left systematic structure unexplained. Chronological evaluation measures how the complete procedure predicts later observations. Good performance in one part does not guarantee good performance in the others, which is why a coefficient table or information criterion alone cannot settle the specification.

## Worked calculation: fit, complexity, and diagnostics

Suppose two likelihood-based candidates have the following summaries:

| Model | log-likelihood | number of parameters |
|---|---:|---:|
| A | $-100$ | 3 |
| B | $-96$ | 6 |

Using

$$
\mathrm{AIC}=-2\ell+2k,
$$

their AIC values are

$$
\mathrm{AIC}_A=200+6=206,
\qquad
\mathrm{AIC}_B=192+12=204.
$$

Model B has the lower AIC in this in-sample comparison, but that result does not establish that its assumptions are adequate or its forecasts are better. If B leaves a residual lag-12 spike while A has approximately white-noise residuals, A may be the more useful forecasting model. Compare candidates on the same observations, inspect residuals, and use temporal backtesting before treating a small information-criterion difference as meaningful.

![Conditional mean and residual diagnostics for an AR model](https://raw.githubusercontent.com/djeada/Statistics-Notes/main/assets/time_series/student/13_modeling_residual_diagnostics.png)

The figure shows the two parts of model assessment together: the fitted conditional mean should capture the systematic structure, and the residuals should no longer contain obvious predictable dependence.

## What a fitted model must explain

Time-series modeling combines specification, parameter estimation, model selection, diagnostics, and forecast evaluation. The aim is not simply to minimize in-sample error, but to find a parsimonious model whose assumptions are reasonable, whose residuals contain little unexplained structure, and whose forecasts generalize to future observations.

## Model Fitting

Choose the estimator to match what the model treats as observed. AR lag columns can be built directly from the data, making conditional least squares straightforward. An MA or ARMA equation contains unobserved past shocks; the candidate parameters determine how those shocks are reconstructed. Likelihood, innovations recursions, and equivalent state-space formulations account for that dependence rather than treating a reconstructed shock column as fixed data.

Record how the estimator handles the record's beginning, missing values, deterministic terms, and innovation variance. Conditional fitting can treat some initial observations or shocks as given; exact likelihood models their joint contribution under specified assumptions. These choices can change short-sample estimates and criterion values. Reproducing the model equation without reproducing the estimation convention may therefore fail to reproduce the reported result.

## Worked Example: Fitting an AR(2) Model

Consider

$$
Y_t=\beta_0+\beta_1Y_{t-1}+\beta_2Y_{t-2}+\varepsilon_t.
$$

Use the short synthetic series

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
\mathbf y=
\begin{bmatrix}
1.5\\
3.0\\
2.5\\
4.0
\end{bmatrix},
\qquad
\mathbf X=
\begin{bmatrix}
1&2.0&1.0\\
1&1.5&2.0\\
1&3.0&1.5\\
1&2.5&3.0
\end{bmatrix}.
$$

If $\mathbf X$ has full column rank, the least-squares estimator is

$$
\hat{\boldsymbol\beta}
=(\mathbf X^\top\mathbf X)^{-1}\mathbf X^\top\mathbf y.
$$

For this dataset,

$$
\mathbf X^\top\mathbf X
=
\begin{bmatrix}
4&9&7.5\\
9&21.5&17\\
7.5&17&16.25
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
\hat\beta_0=0.328,
\qquad
\hat\beta_1=0.080,
\qquad
\hat\beta_2=1.195.
$$

Thus the fitted conditional mean is

$$
\hat Y_t=0.328+0.080Y_{t-1}+1.195Y_{t-2}.
$$

The coefficient sum is $\hat\beta_1+\hat\beta_2\approx1.275>1$, and both zeros of $1-0.080z-1.195z^2$ have modulus below 1. The corresponding time-recursion roots lie outside the unit circle, so this fit violates causal stability.

Four usable rows estimate three mean coefficients, leaving just one residual degree of freedom. The data constrain this equation weakly, even though the normal equations have a solution. The example should therefore be read as a calculation of the estimator, not as evidence that AR(2) is suitable. Check root stability first, then compare simpler candidates and later forecasts before assigning meaning to the fitted lag effects.

## Why the Design Matrix Needs Variation

If observations increase by a constant amount (for example $1,2,3,\ldots$), adjacent lag columns can become linearly dependent once an intercept is included. Then $\mathbf X^\top\mathbf X$ is singular, the inverse in the ordinary least-squares expression does not exist, and the coefficients are not uniquely identified.

An invertible-looking matrix formula is not a guarantee that the data identify the coefficients well. Exact linear dependence makes the solution nonunique; near dependence makes it sensitive to small data changes. Numerically, solve the least-squares problem with an appropriate factorization rather than explicitly forming the normal-equation inverse. Substantively, ask whether the sample contains enough variation and history to distinguish the proposed lag effects.

## Fitting MA and ARMA Models

An MA(2) model is

$$
Y_t=\mu+\varepsilon_t+\theta_1\varepsilon_{t-1}+\theta_2\varepsilon_{t-2}.
$$

The lagged innovations are latent. Treating them as ordinary observed regressors is therefore not valid. Practical estimation commonly uses maximum likelihood, innovations algorithms, or state-space methods. Procedures such as Hannan-Rissanen can also provide useful starting estimates for ARMA likelihood optimization.

## Comparison of Common Models

| Model | Main idea | Typical use | Important assumptions / cautions |
|---|---|---|---|
| **AR($p$)** | Current value depends on past values | Short-memory stationary dependence | Check stationarity and root location after any required transformation |
| **MA($q$)** | Current value depends on current and past innovations | Short-lived shock effects | Innovations are latent; invertibility matters for identification |
| **ARMA($p,q$)** | Combines AR and MA terms | Stationary linear series | Use parsimonious order selection and residual diagnostics |
| **ARIMA($p,d,q$)** | ARMA structure after differencing | Integrated or stochastic-trend series | Use the smallest justified differencing order |
| **SARIMA** | ARIMA plus seasonal AR, MA, and differencing terms | Regular seasonal structure | Seasonal period and seasonal differencing must match the data mechanism |
| **SES / Holt / Holt-Winters / ETS** | Recursive level, trend, and seasonal states | Forecasting evolving level/trend/seasonality | Different structures imply different error and state dynamics |
| **VAR** | Several variables depend on their joint lags | Multivariate linear dynamics | Lag order, stability, and cointegration matter; predictability is not automatically causal |
| **ARCH/GARCH** | Conditional variance evolves over time | Volatility clustering | Usually modeled after specifying an adequate conditional mean |

The table is a model map, not a ranking. The appropriate class depends on what is being forecast, which structures are present, and which assumptions remain plausible after diagnostics.

## A Practical Identification and Validation Workflow

1. **Explore the series.** Plot the data and identify trend, seasonality, missingness, outliers, structural breaks, and changing variance.
2. **Assess stationarity.** Use plots, ACF behavior, and tests such as ADF/KPSS as supporting evidence.
3. **Transform when needed.** Apply variance stabilization, detrending, ordinary differencing, or seasonal differencing only when justified.
4. **Propose candidate orders.** Use ACF/PACF patterns and domain knowledge as heuristics rather than mechanical rules.
5. **Estimate parameters.** Use a method appropriate to the model class.
6. **Compare parsimonious candidates.** Use AIC, AICc, or BIC only among models fitted to comparable data and likelihoods.
7. **Diagnose residuals.** Check residual time plots, ACF/PACF, squared residuals, and relevant tests such as Ljung-Box.
8. **Evaluate forecasts temporally.** Preserve chronology with holdouts or rolling/expanding origins.

![Temporal validation split](https://raw.githubusercontent.com/djeada/Statistics-Notes/main/assets/time_series/diagnostics/08_temporal_validation_split.png)

The figure emphasizes the final step: model selection is incomplete until the complete procedure is tested on observations from later periods without information leakage.

## ARMA Identification and Estimation Checklist

For a stationary series, a common ARMA workflow is:

1. propose a small set of $p$ and $q$ values from ACF/PACF behavior and domain knowledge;
2. decide whether a mean or intercept term is appropriate;
3. estimate AR and MA coefficients with a suitable numerical method;
4. estimate the innovation variance;
5. compare candidates using diagnostics and information criteria;
6. verify that residuals no longer contain material serial dependence.

For pure AR models, Yule-Walker or Burg estimators can be useful. Innovations algorithms target MA structure, while Hannan-Rissanen can provide starting values before likelihood optimization.

## Order Selection with AICc

The **corrected Akaike Information Criterion (AICc)** adjusts AIC for finite samples. One common form is

$$
\mathrm{AICc}
=\mathrm{AIC}
+\frac{2k(k+1)}{n-k-1},
$$

where $k$ is the number of estimated parameters counted in the likelihood and $n$ is the effective sample size. This expression requires $n>k+1$; when the denominator is zero or negative, it cannot be used as an ordinary finite-sample correction.

Lower values indicate a better fit-complexity tradeoff within a comparable candidate set. Parameter-count and effective-sample conventions vary across implementations, so check the software documentation when reproducing exact values.

## Parameter Redundancy

An ARMA equation can contain the same factor on both sides. For example, $(1-0.5B)X_t=(1-0.5B)\varepsilon_t$ reduces to white noise in the appropriate causal representation. Reporting an AR term and an MA term would then give a needlessly complicated description of the same process. Nearly shared fitted factors can similarly make separate coefficients weakly identified, even when no exact cancellation occurs.

Prefer reduced representations without common factors. If estimated roots nearly cancel, treat the apparent complexity with caution rather than interpreting each coefficient as a separate dynamic mechanism.

## Model Selection Is Not Only About Fit

Adding parameters generally gives the training fit more freedom, but it also makes estimates more sensitive to the sample and can absorb patterns that will not recur. Prefer a candidate whose complexity is supported by enough data and a clear remaining feature. A useful improvement should survive residual checks and evaluation at the actual forecast horizons, rather than appearing only as a smaller training error.

## Connections to Other Notes

- See **[stationarity.md](https://github.com/djeada/Statistics-Notes/blob/main/notes/time_series/stationarity.md)** before interpreting AR/MA/ARIMA models.
- See **[autocorrelation_function.md](https://github.com/djeada/Statistics-Notes/blob/main/notes/time_series/autocorrelation_function.md)** for ACF/PACF-based identification.
- See **[autoregressive_models.md](https://github.com/djeada/Statistics-Notes/blob/main/notes/time_series/autoregressive_models.md)** and **[moving_average_models.md](https://github.com/djeada/Statistics-Notes/blob/main/notes/time_series/moving_average_models.md)** for model-specific properties.
- See **[arima_models.md](https://github.com/djeada/Statistics-Notes/blob/main/notes/time_series/arima_models.md)** for differencing and seasonal ARIMA models.
- See **[randomness_tests.md](https://github.com/djeada/Statistics-Notes/blob/main/notes/time_series/randomness_tests.md)** for residual checks.
- See **[forecasting.md](https://github.com/djeada/Statistics-Notes/blob/main/notes/time_series/forecasting.md)** for forecast construction and uncertainty.

## Making estimation and model assessment reproducible

A time-series model is a set of assumptions about the conditional mean, temporal dependence, new shocks, variance behavior, and information available for prediction. Record these assumptions explicitly before comparing software summaries.

A table of coefficients alone does not tell a reader which observations were used, how missing values were handled, which transformations were applied, or whether the residuals are adequate.

### Start with the target and the index

Record:

- the response variable and its units;
- the timestamp and sampling interval;
- whether timestamps are regular;
- the forecast horizon;
- the difference between observation time and release time;
- the deployment decision the forecast supports.

For example, a monthly sales forecast issued on the last day of March may use completed March sales, while a forecast issued on March 10 may have only partial March information. The timestamp is therefore part of the model's information set, not just a plotting label.

### Explore before fitting

Inspect the level series, relevant transformations, first and seasonal differences, rolling mean and variance, missingness and outliers, ACF/PACF, known calendar effects, and possible structural breaks.

![Detrending](https://raw.githubusercontent.com/djeada/Statistics-Notes/main/assets/time_series/diagnostics/01_detrending.png)

The detrending figure shows why preprocessing should follow the mechanism. Removing a deterministic trend can reveal stationary residual structure, while differencing answers a different question by modeling changes rather than deviations around a fitted trend.

An ACF that decays slowly may reflect a unit root, deterministic trend, seasonal pattern, or structural break. It is evidence to investigate, not a diagnosis by itself.

### Estimation mechanics

For AR($p$), lagged observations are observed:

$$
y_t=c+\phi_1y_{t-1}+\cdots+\phi_py_{t-p}+\varepsilon_t.
$$

For MA($q$), lagged innovations are not observed:

$$
y_t=\mu+\varepsilon_t+\theta_1\varepsilon_{t-1}+\cdots+\theta_q\varepsilon_{t-q}.
$$

The innovations must be inferred recursively or through an equivalent state-space representation. Treating them as known regressors changes the estimation problem.

For a Gaussian state-space or innovations representation, log-likelihood contributions often have the form

$$
-\frac12\left[\log(2\pi)+\log(F_t)+\frac{v_t^2}{F_t}\right].
$$

The likelihood contribution uses both the innovation $v_t$ and its predicted variance $F_t$. A model cannot improve the criterion simply by making residuals look small if it assigns incompatible uncertainty to them. Different initialization, observation samples, or response transformations can also change the likelihood basis. Compare information criteria only after ensuring that their underlying likelihoods are meaningfully comparable.

### Numerical order selection

Suppose one model has $\ell=-100$ and $k=3$:

$$
\mathrm{AIC}=-2(-100)+2(3)=206.
$$

A larger model has $\ell=-96$ and $k=6$:

$$
\mathrm{AIC}=-2(-96)+2(6)=204.
$$

The extra three parameters cost 6 AIC units, while the log-likelihood improvement lowers the fit term by 8. The net improvement is therefore 2 units. This explains the preference arithmetically without treating it as proof of forecasting superiority. If candidate models use different response transformations or observation rows, the reported numbers may not represent this same fit-versus-penalty comparison.

$$
\mathrm{BIC}=-2\ell+k\log n.
$$

Use AICc when the effective sample is not large relative to the parameter count, and compare only models fitted to comparable observations and likelihood definitions.

### Residuals as a model check

Let

$$
\hat\varepsilon_t=y_t-\hat y_{t\mid t-1}
$$

be one-step residuals. They compare the observation with its fitted one-step prediction. Their mean checks systematic offset; their time pattern checks changing regimes; their ACF checks remaining linear dependence; their squared values check variation in error magnitude. These are different questions. In a variance model, examine standardized innovations rather than demanding that raw errors have a constant conditional scale.

For residual autocorrelation,

$$
\hat\rho(h)
=\frac{\sum_{t=h+1}^{T}
(\hat\varepsilon_t-\bar\varepsilon)
(\hat\varepsilon_{t-h}-\bar\varepsilon)}
{\sum_{t=1}^{T}(\hat\varepsilon_t-\bar\varepsilon)^2}.
$$

![Residual ACF](https://raw.githubusercontent.com/djeada/Statistics-Notes/main/assets/time_series/diagnostics/02_residual_acf.png)

A short-lag residual pattern can indicate incomplete dynamic adjustment; a repeated seasonal pattern can indicate an omitted seasonal component or calendar effect. A break can create a broad pattern that adding AR lags would only imitate. Use the shape to propose a specific explanation, fit that explanation, and check whether it resolves the pattern. A residual spike is evidence about a failure, not an instruction to add that lag mechanically.

The Ljung-Box statistic through lag $m$ is

$$
Q(m)=T(T+2)\sum_{h=1}^{m}\frac{\hat\rho(h)^2}{T-h}.
$$

![Ljung-Box shape](https://raw.githubusercontent.com/djeada/Statistics-Notes/main/assets/time_series/diagnostics/06_ljung_box_shape.png)

The figure reinforces that the test aggregates evidence across several lags. A small p-value says the residuals retain linear dependence at one or more tested lags; it does not prescribe the replacement model.

### Residual variance and distribution

A residual ACF near zero does not establish independent, homoskedastic residuals. Inspect squared residuals and their dependence as well.

![Residual variance](https://raw.githubusercontent.com/djeada/Statistics-Notes/main/assets/time_series/diagnostics/03_residual_variance.png)

Changing residual spread indicates that the conditional variance may need separate modeling.

![Residual nonlinearity](https://raw.githubusercontent.com/djeada/Statistics-Notes/main/assets/time_series/diagnostics/04_residual_nonlinearity.png)

A residual plot can also reveal nonlinear patterns that a linear mean model cannot capture even when ordinary autocorrelation is small.

![Residual distribution](https://raw.githubusercontent.com/djeada/Statistics-Notes/main/assets/time_series/diagnostics/05_residual_distribution.png)

Heavy tails or skewness can make Gaussian prediction intervals poorly calibrated even when the conditional mean is adequate. The relevant distributional assumption should match the forecast objective, especially when tail probabilities matter.

### Structural breaks

A single stable parameter set can average over multiple regimes. After a break, residuals may show a level shift, a change in persistence, a variance jump, or a change in seasonal amplitude.

![Structural break](https://raw.githubusercontent.com/djeada/Statistics-Notes/main/assets/time_series/diagnostics/07_structural_break.png)

The break figure shows why an isolated global fit can be misleading: parameters that describe the pre-break period may no longer represent the post-break process.

Choose a response that represents what changed. A known one-time level shift can enter as an intervention variable. An ongoing change in dynamics may favor a shorter estimation window, separate regimes, or time-varying states. Resetting a model discards information and changes the forecasting procedure, so evaluate that reset rule chronologically. Deleting unusual observations without a substantive explanation can hide precisely the events that drive future forecast errors.

### A model comparison table

Keep an auditable record:

| candidate | transformation | parameters | AIC | residual ACF | backtest MAE | notes |
|---|---|---:|---:|---|---:|---|
| naive | none | 0 | — | — |  | baseline |
| AR(1) | none | 2 |  |  |  |  |
| ARIMA | first difference |  |  |  |  |  |
| seasonal model | seasonal difference |  |  |  |  |  |

The chosen model should be the simplest candidate that captures the important structure and performs acceptably on chronologically held-out data. A lower in-sample criterion paired with structured residuals calls for further diagnosis; it does not settle the selection decision.

## Formula reference

| Topic / model | General formula | Use / special case |
|---|---|---|
| AR($p$) | $Y_t=c+\sum_{i=1}^{p}\phi_iY_{t-i}+\varepsilon_t$ | Lagged observations are observed regressors. |
| MA($q$) | $Y_t=\mu+\varepsilon_t+\sum_{j=1}^{q}\theta_j\varepsilon_{t-j}$ | Lagged innovations are latent. |
| ARMA($p,q$) | $\phi(B)(Y_t-\mu)=\theta(B)\varepsilon_t$ | Stationary short-memory linear model. |
| ARIMA($p,d,q$) | $\phi(B)(1-B)^dY_t=c+\theta(B)\varepsilon_t$ | Adds ordinary differencing. |
| SARIMA | $\Phi(B^s)\phi(B)(1-B^s)^D(1-B)^dY_t=\Theta(B^s)\theta(B)\varepsilon_t$ | Adds seasonal dynamics and differencing. |
| OLS for AR design | $\hat\beta=(X^\top X)^{-1}X^\top y$ | Requires full column rank; numerical solvers are preferred to explicit inversion. |
| Gaussian innovation log-likelihood | $\ell_t=-\tfrac12[\log(2\pi)+\log F_t+v_t^2/F_t]$ | State-space/innovations form; sum over $t$. |
| Residual | $\hat\varepsilon_t=y_t-\hat y_{t\mid t-1}$ | One-step unexplained component. |
| Residual ACF | $\hat\rho(h)=\frac{\sum_{t=h+1}^{T}(\hat\varepsilon_t-\bar\varepsilon)(\hat\varepsilon_{t-h}-\bar\varepsilon)}{\sum_{t=1}^{T}(\hat\varepsilon_t-\bar\varepsilon)^2}$ | Checks remaining linear dependence. |
| Ljung-Box | $Q(m)=T(T+2)\sum_{h=1}^{m}\hat\rho(h)^2/(T-h)$ | Joint residual-autocorrelation diagnostic. |
| AIC | $\mathrm{AIC}=-2\ell+2k$ | Lower is preferred within comparable likelihood fits. |
| AICc | $\mathrm{AICc}=\mathrm{AIC}+2k(k+1)/(n-k-1)$ | Small-sample correction to AIC. |
| BIC | $\mathrm{BIC}=-2\ell+k\log n$ | Penalizes complexity more strongly as $n$ grows. |
| AR stationarity/causality | $\phi(z)=0\Rightarrow\lvert z\rvert>1$ | Standard backshift-root condition. |
| MA invertibility | $\theta(z)=0\Rightarrow\lvert z\rvert>1$ | Selects the stable innovation representation. |
| Forecast error | $e_{t,h}=y_{t+h}-\hat y_{t+h\mid t}$ | Evaluate on chronological future-like origins. |
| MAE / RMSE | $\mathrm{MAE}=n^{-1}\sum\lvert e_i\rvert$, $\mathrm{RMSE}=\sqrt{n^{-1}\sum e_i^2}$ | Complement likelihood criteria with out-of-sample loss. |
