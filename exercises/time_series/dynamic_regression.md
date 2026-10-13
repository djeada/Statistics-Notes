# Dynamic Regression

Read [dynamic regression](../../notes/time_series/dynamic_regression.md) and [regression with ARMA errors](../../notes/time_series/regression_with_arma_errors.md).

1. For $y_t=2+1.5x_t+n_t$, calculate $y_t$ when $x_t=4$ and $n_t=0.3$.
2. For $y_t=2+x_t+0.5x_{t-1}+n_t$, calculate the regression mean when $x_t=4$ and $x_{t-1}=2$.
3. Simulate AR(1) errors with coefficient $0.75$. Fit ordinary least squares and inspect residual autocorrelation. Explain what the dynamic error model adds.
4. List three predictors known in advance at the forecast origin and three predictors that usually require their own forecasts.
5. Explain why a statistically useful predictor is not automatically a causal intervention.
6. Compare a model with current $x_t$ only to one with $x_t$ and $x_{t-1}$. Use rolling-origin evaluation and state how future $x$ values are obtained.
7. Explain why the label ARIMAX is not enough to identify the exact likelihood or error equation used by software.

## Checks

- The value in question 1 is $2+1.5(4)+0.3=8.3$.
- The regression mean in question 2 is $2+4+1=7$.
- The complete forecasting procedure includes the predictor-forecast step whenever future predictors are unavailable.

## Applied practice

8. Run [dynamic_multivariate_visualizations.py](../../scripts/time_series/dynamic_multivariate_visualizations.py). Explain which figure demonstrates future-predictor leakage.
9. Simulate a distributed-lag response with weights $(1,0.6,0.25)$. Estimate the lag pattern and discuss collinearity between adjacent predictors.
10. Compare OLS, heteroskedasticity-and-autocorrelation robust standard errors, and a regression-with-ARMA-errors model. Which changes coefficients and which changes uncertainty?
11. Create a predictor known in advance, a predictor observed with a release delay, and a predictor requiring a forecast. Use different treatment for each.
12. Add a structural break to the regression slope. Examine residuals and coefficient stability over expanding windows.
13. Explain how a causal intervention design would need stronger assumptions than a predictive regression.

## Reflection

Document the target equation, lag convention, predictor availability, error model, and complete backtesting procedure. Treat ARIMAX as a software label that must be translated into an equation.

## Extension tasks

14. Derive the long-run multiplier for a stable distributed-lag model with coefficients $(1,0.5,0.25)$.
15. Add a predictor with a release delay and compare an oracle backtest with a real-time backtest.
16. Simulate feedback from $y_t$ into $x_{t+1}$. Explain why a regression coefficient may not have a causal interpretation.
17. Compare dynamic regression errors before and after adding an AR(1) term. Use residual ACF and temporal MAE.
18. Fit a model with a known calendar variable and a forecasted weather variable. Include predictor uncertainty in the interval discussion.
19. Explain how omitted common trend can produce a spurious dynamic regression.

## Worked solutions

Numerical results below come from seeded runs (`numpy.random.default_rng`) in Python with statsmodels; your seed may give slightly different digits.

**1.** $y_t=2+1.5x_t+n_t=2+1.5(4)+0.3=2+6+0.3=8.3$.

**2.** The regression mean is $2+x_t+0.5x_{t-1}=2+4+0.5(2)=2+4+1=7$. Adding the error $n_t$ gives the observation.

**3.** Simulate, fit OLS, then fit regression with AR(1) errors:

```python
import numpy as np, statsmodels.api as sm
from statsmodels.tsa.statespace.sarimax import SARIMAX

rng = np.random.default_rng(0)
n = 300
x = rng.normal(size=n)
e = rng.normal(size=n)
u = np.zeros(n)
for t in range(1, n):
    u[t] = 0.75 * u[t - 1] + e[t]
y = 2 + 1.5 * x + u

X = sm.add_constant(x)
ols = sm.OLS(y, X).fit()
r = ols.resid
print(ols.params, ols.bse, np.corrcoef(r[1:], r[:-1])[0, 1])
dyn = SARIMAX(y, exog=X, order=(1, 0, 0), trend="n").fit(disp=False)
print(dyn.params, dyn.bse)
```

OLS gives slope $1.444$ (s.e. $0.076$) and residual lag-1 autocorrelation $0.69$ (Durbin-Watson $0.62$), so the independent-error assumption fails. The regression with AR(1) errors gives slope $1.477$ (s.e. $0.051$), $\hat\phi=0.69$, and residual lag-1 autocorrelation $-0.02$. The dynamic error model whitens the residuals, gives valid and more efficient inference, and lets forecasts use the current error $\hat n_t$ (Question 17).

**4.** Known in advance: calendar variables (day of week, holiday flag), a planned price or promotion schedule, a scheduled policy date. Usually need their own forecast: temperature, competitor price, macroeconomic indicators (or any quantity measured only after the forecast origin).

**5.** A predictor can be useful because it is correlated with the response through a confounder, a common trend, or reverse causation. A prediction uses the observed joint behaviour; an intervention changes $x$ and needs the stronger claim that nothing else moves with it.

**6.** Fit both models on an expanding window, forecast one (or $h$) steps ahead from each origin, and compare MAE or RMSE across origins. At each origin $x_{t+1}$ must be known in advance, forecast using only data up to the origin, or explicitly labelled as an oracle (realized) value. Report oracle and real-time results separately.

**7.** "ARIMAX" is used both for $\phi(B)y_t=\beta^\top x_t+\theta(B)\varepsilon_t$ (the exogenous term is filtered by the AR polynomial) and for $y_t=\beta^\top x_t+n_t$ with $\phi(B)n_t=\theta(B)\varepsilon_t$ (regression with ARMA errors). The two give different $\beta$ interpretations, differencing handling, intercept meaning, and likelihoods. Write the equation and check the software documentation.

**8.** `future_predictor_availability()` ("Realized future predictors can leak into evaluation").

**9.** Distributed lag with a persistent predictor:

```python
rng = np.random.default_rng(1)
n = 400
z = np.zeros(n + 2)
for t in range(1, n + 2):
    z[t] = 0.95 * z[t - 1] + rng.normal()
x0, x1, x2 = z[2:], z[1:-1], z[:-2]          # x_t, x_{t-1}, x_{t-2}
y = 1.0 * x0 + 0.6 * x1 + 0.25 * x2 + rng.normal(scale=0.5, size=n)
fit = sm.OLS(y, sm.add_constant(np.column_stack([x0, x1, x2]))).fit()
print(fit.params, fit.bse)
```

Estimates are $(1.048,\,0.609,\,0.185)$ with s.e. about $0.03$ against the true $(1,\,0.6,\,0.25)$. Adjacent predictors have correlation $0.91$ and variance inflation factors $5.7$, $9.2$, $5.7$, so individual weights are less precise than their sum ($1.84$ against $1.85$). With even higher persistence, report cumulative effects or use a parsimonious lag shape (polynomial or geometric) instead of free weights.

**10.** OLS and HAC share the same coefficients ($1.444$ in Question 3's data) and differ only in the standard error ($0.076$ OLS, $0.060$ HAC with 8 lags). The regression with ARMA errors changes both the coefficient ($1.477$) and the standard error ($0.051$), and also changes forecasts because it models $n_t$.

**11.** Known in advance: use directly. Release-delayed: use the latest *released* value (lag it by the delay) in training and backtests. Needs a forecast: use $\hat x_{t+h|t}$ in forecasting, and propagate its error into the interval (Question 18).

**12.** With the slope $1$ before $t=100$ and $2$ afterwards, the expanding-window slope estimates after 50, 100, 150, and 200 observations are $1.08$, $1.07$, $1.36$, $1.52$. The estimate drifts upward after the break and never reaches $2$, so recursive coefficients, CUSUM, or a break dummy reveal instability that one global fit hides.

**13.** A causal claim needs at least no unmeasured confounding of $x$ and $y$, no feedback from $y$ to future $x$ (or a model for it), a well-defined intervention, and stability of the relationship when $x$ is set rather than observed. A predictive regression needs none of these.

**14.** For $y_t=\sum_{j=0}^{2}\beta_jx_{t-j}$, a permanent unit step in $x$ adds $\beta_0$ in the first period, $\beta_0+\beta_1$ in the second, and $\beta_0+\beta_1+\beta_2$ from then on. The long-run multiplier is $1+0.5+0.25=1.75$. With an AR part, $\phi(B)y_t=\beta(B)x_t$, it is $\beta(1)/\phi(1)$.

**15.** Oracle backtest: plug in the realized predictor value at each origin. Real-time backtest: use only the released vintage (the value $d$ periods old when the delay is $d$). The oracle error is usually smaller; the gap is the cost of the delay.

**16.** If $y_t$ feeds $x_{t+1}$, then $x_t$ is correlated with past errors, so the coefficient mixes the effect of $x$ on $y$ with the effect of earlier $y$ on $x$. Regression still predicts, but the slope does not describe the effect of setting $x$.

**17.** Rolling one-step forecasts on the last 100 of 400 observations (AR(1) errors, $\phi=0.75$): MAE $1.336$ for OLS and $0.813$ for regression with AR(1) errors. The residual ACF of the second model is near zero at lag 1; the first still shows $\hat\rho(1)\approx0.7$.

**18.** The forecast error of $y$ includes $\beta(x_{t+h}-\hat x_{t+h})$, so $\mathrm{Var}(\text{error})\approx\sigma_n^2(h)+\beta^2\mathrm{Var}(x\text{ error})$. Intervals computed with the future predictor treated as known are too narrow.

**19.** Two series $y_t=a+bt+\varepsilon_t$ and $x_t=c+dt+\eta_t$ with unrelated noise give a highly significant slope in $y\sim x$ because both move with time. Add $t$, use differences, or model the trend explicitly; the apparent relationship should disappear if the series are otherwise independent.

## Submission check

Include the model equation, predictor timing table, residual diagnostics, baseline, and a forecast comparison that uses only information available at each origin.
