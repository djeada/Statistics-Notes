# Multivariate Models

Read [multivariate time series](../../notes/time_series/multivariate_time_series.md).

1. Write the two-equation VAR(1) for $y_t=(x_t,z_t)^\top$ with coefficient matrix $\begin{pmatrix}0.5&0.2\\-0.1&0.4\end{pmatrix}$ and intercept zero.
2. For $x_t=10$, $y_t=1.4x_t+u_t$, and $u_t=0.5$, calculate $y_t$ and the spread.
3. Explain why a regression of one independent random walk on another can have a high in-sample $R^2$.
4. Simulate two cointegrated series. Check that each level is non-stationary while the spread is more stable.
5. Explain what a Granger-predictability test conditions on and why it is not a structural causal intervention test.
6. Fit a VAR to stationary differences and inspect stability and residual cross-correlation.
7. Explain the role of $\alpha$ and $\beta$ in $\Pi=\alpha\beta^\top$ for a VECM.
8. Compute or plot an impulse response and state the assumptions needed before interpreting it as a response to a structural shock.

## Checks

- The value in question 2 is $1.4(10)+0.5=14.5$.
- A stable spread supports a cointegration story; it does not by itself identify a causal mechanism.
- Orthogonalized impulse responses can depend on variable ordering.

## Applied practice

9. Run [dynamic_multivariate_visualizations.py](../../scripts/time_series/dynamic_multivariate_visualizations.py). Identify the feedback, predictive, long-run, and shock-propagation figures.
10. Simulate a stable VAR(1). Check the eigenvalues of its coefficient matrix and compare simulated persistence with the largest eigenvalue.
11. Compare VAR lag orders using AIC and BIC. Inspect residual cross-correlation before choosing the smaller or larger order.
12. Simulate independent random walks and repeat the levels regression many times. Record how often the $R^2$ exceeds a chosen threshold.
13. Simulate cointegrated levels, estimate their spread, and compare a differenced VAR with a VECM conceptually.
14. Test Granger predictability in both directions. Explain why rejection in one direction does not prove an intervention effect.
15. Plot an impulse response under two variable orderings and describe what changes.

## Reflection

Write down the integration, deterministic-term, lag-order, stability, identification, and forecast-validation assumptions before interpreting a multivariate result.

## Extension tasks

16. Calculate the eigenvalues of a supplied VAR(1) coefficient matrix and determine whether the system is stable.
17. Simulate two unrelated random walks 100 times and summarize the distribution of levels-regression $R^2$.
18. Estimate a cointegrating vector in a two-series example and plot the spread.
19. Compare a VAR in levels, a VAR in differences, and a VECM in terms of the relationships each preserves.
20. Change the ordering used for orthogonalized impulse responses and identify the responses that change.
21. Explain why a Granger test can be unstable when the lag order or deterministic terms are misspecified.

## Worked solutions

Simulation numbers come from seeded Python runs (`numpy.random.default_rng`, statsmodels); other seeds change the digits, not the conclusions.

**1.** With $y_t=(x_t,z_t)^\top$ and $y_t=Ay_{t-1}+\varepsilon_t$:

$$
x_t=0.5x_{t-1}+0.2z_{t-1}+\varepsilon_{1t},\qquad
z_t=-0.1x_{t-1}+0.4z_{t-1}+\varepsilon_{2t}.
$$

**2.** $y_t=1.4(10)+0.5=14.5$. The spread (the cointegrating combination) is $y_t-1.4x_t=u_t=0.5$.

**3.** Two independent random walks each have a stochastic trend, so over any sample they drift and the sample correlation between the levels is not near zero. The regression $t$-statistic does not converge to a standard distribution and the residuals are strongly autocorrelated (low Durbin-Watson). In 1000 simulations with $n=200$ the mean $R^2$ was $0.24$, the median $0.16$, and $R^2>0.5$ occurred in $16.5\%$ of runs, versus essentially $0$ for independent stationary series.

**4.**

```python
import numpy as np, statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller, coint

rng = np.random.default_rng(1)
n = 500
w = np.cumsum(rng.normal(size=n))                 # shared stochastic trend
x = w + rng.normal(scale=0.5, size=n)
y = 1.4 * w + rng.normal(scale=0.5, size=n)
print(adfuller(x)[1], adfuller(y)[1])             # levels: cannot reject unit root
fit = sm.OLS(y, sm.add_constant(x)).fit()
spread = y - fit.params[1] * x - fit.params[0]
print(fit.params, adfuller(spread)[1], coint(y, x)[1])
```

The ADF $p$-values for the levels are $0.45$ and $0.43$ (unit root not rejected), the estimated cointegrating slope is $1.397$ (true $1.4$), and the spread has ADF $p\approx0.000$. (The ADF test on an estimated spread should use Engle-Granger critical values, as `coint` does.)

**5.** $x$ Granger-causes $y$ if past $x$ improves the prediction of $y$ given the past of $y$ (and other included variables). It is a statement about predictive content within a given information set and lag order; omitted variables, a common driver, or timing differences can create it without any intervention effect.

**6.** Difference each integrated series, choose the lag order by information criteria and residual diagnostics, then check that all eigenvalues of the companion matrix have modulus below $1$ and that the residual cross-correlation matrices have no remaining structure. If the levels are cointegrated, the differenced VAR omits the error-correction term.

**7.** $\Delta y_t=\Pi y_{t-1}+\sum_i\Gamma_i\Delta y_{t-i}+\varepsilon_t$ with $\Pi=\alpha\beta^\top$ of rank $r$. The columns of $\beta$ are the cointegrating vectors (long-run equilibrium relations, so $\beta^\top y_t$ is stationary); $\alpha$ holds the adjustment speeds with which each variable corrects deviations from those relations. Only $\alpha\beta^\top$ is identified without normalization.

**8.** The impulse response of $y_{t+k}$ to a one-unit shock in $\varepsilon_{jt}$ is $A^ke_j$ for a VAR(1). It is a response to a *structural* shock only if the shocks are mutually uncorrelated and identified by a stated restriction (recursive ordering, long-run, sign restrictions), and the system is correctly specified and stable.

**9.** Feedback: `var_feedback()` ("A VAR allows feedback between series"). Predictive: `granger_predictability()`. Long-run: `cointegration()` and `vecm_adjustment()`. Shock propagation: `impulse_response()`.

**10.** For $A=\begin{pmatrix}0.5&0.2\\-0.1&0.4\end{pmatrix}$: $\operatorname{tr}A=0.9$, $\det A=0.22$, so $\lambda^2-0.9\lambda+0.22=0$ and $\lambda=0.45\pm0.1323i$, modulus $\sqrt{0.22}=0.469$. A simulated series has autocorrelations that decay roughly like $0.47^k$. The fitted VAR(2) on 1000 simulated points gave first-lag coefficients $\begin{pmatrix}0.49&0.16\\-0.12&0.38\end{pmatrix}$ (near $A$), second-lag coefficients near $0$, and `is_stable()` was `True`.

**11.** On the same simulated data (true order 1), AIC selected order $2$ and BIC selected order $1$. Check residual cross-correlation of the smaller model first; keep the larger one only if the smaller one leaves structure.

**12.** See Question 3 and Question 17 for the simulation and its result.

**13.** Differenced VAR: stationary, but throws away long-run level information. VECM: adds $\alpha\beta^\top y_{t-1}$ so short-run dynamics correct deviations from equilibrium; it keeps both short- and long-run relationships and is the correct form when the cointegration rank is positive.

**14.** Run `grangercausalitytests` on both column orders. In the stable VAR above both directions are significant because the off-diagonal entries $0.2$ and $-0.1$ are nonzero. Predictive content in either direction does not show what would happen under an intervention.

**15.** Orthogonalized responses use $\Sigma=PP^\top$ with $P$ lower triangular. The first variable in the ordering can affect the second on impact but not vice versa, so changing the order changes the impact responses (and hence the later ones) whenever $\Sigma$ has nonzero off-diagonal covariance. Generalized impulse responses do not depend on order but are not orthogonal.

**16.** Same calculation as Question 10: eigenvalues $0.45\pm0.1323i$, both inside the unit circle, so the system is stable.

**17.** With $n=200$ and 1000 replications of independent random walks: mean $R^2=0.24$, median $0.16$, $P(R^2>0.3)=0.34$, $P(R^2>0.5)=0.165$.

**18.** Question 4: $\hat\beta=1.397$, and the spread $y_t-1.397x_t-\hat\alpha$ is stationary-looking around $0$ (ADF $p\approx0.000$).

**19.** Levels VAR: consistent but estimates are non-standard, so inference is delicate, and it keeps long-run relationships implicitly. Differenced VAR: stable and standard, but loses the equilibrium. VECM: represents both with the error-correction term; it requires the rank and deterministic terms to be chosen.

**20.** Reordering $(x,z)\to(z,x)$ changes $P$. The variable placed first is unaffected on impact by the other variable's shock, and the variable placed second responds on impact to the first; swapping the order moves that zero from one off-diagonal impact response to the other.

**21.** The test compares nested regressions at a chosen lag length; too few lags leave autocorrelation (invalid $F$), too many reduce power, and omitted deterministic terms or unit roots break the usual $F$/Wald distribution. Hence use lag order from criteria plus residual checks and robustness across lags.

## Submission check

Report the system dimensions, transformations, lag order, stability evidence, identification assumptions, and joint forecast-validation design.
