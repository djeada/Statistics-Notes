# Dependence and Identification

Read [autocovariance](../../notes/time_series/autocovariance_function.md), [autocorrelation](../../notes/time_series/autocorrelation_function.md), [autoregressive models](../../notes/time_series/autoregressive_models.md), [moving-average models](../../notes/time_series/moving_average_models.md), and [Yule-Walker equations](../../notes/time_series/yule_walker_equations.md).

1. For $x=(1,2,4,3)$, calculate the mean, centered values, $\hat\gamma(0)$, and the lag-1 autocovariance using denominator $n$. State how the result changes if the lag-1 denominator is $n-1$.
2. For the stationary AR(1) $X_t=0.7X_{t-1}+\varepsilon_t$, calculate $\rho(1)$, $\rho(2)$, and $\rho(3)$. Sketch the expected ACF.
3. For an MA(1) $X_t=\varepsilon_t+0.5\varepsilon_{t-1}$ with innovation variance 1, calculate $\gamma(0)$, $\gamma(1)$, and $\rho(1)$.
4. Explain why an AR(1) ACF tails off while an MA(1) ACF cuts off after lag 1. What would finite-sample noise do to each pattern?
5. For $X_t=1+0.8X_{t-1}+\varepsilon_t$ with innovation variance 1, calculate the stationary mean and variance. Repeat the stationarity argument for $\phi=1$.
6. For the AR(2) coefficients $\phi_1=0.6$ and $\phi_2=-0.2$, use Yule-Walker equations to calculate $\rho_1$, $\rho_2$, and $\rho_3$.
7. For an MA(1) with $\theta=0.5$, write the first four coefficients of the inverse filter. Explain why $\theta=2$ gives an unstable inverse representation.
8. Simulate an AR(2) process and estimate its ACF and PACF. Which feature should be more sharply concentrated at the first two lags?

## Checks

- $\hat\gamma(0)=1.25$ and the lag-1 covariance is $0.1875$ under the denominator-$n$ convention.
- For the AR(1), $\rho(1)=0.7$, $\rho(2)=0.49$, and $\rho(3)=0.343$.
- For the MA(1), $\gamma(0)=1.25$, $\gamma(1)=0.5$, and $\rho(1)=0.4$.
- The AR(2) values are $\rho_1=0.5$, $\rho_2=0.1$, and $\rho_3=-0.04$.

## Applied practice

9. Run [dependence_visualizations.py](../../scripts/time_series/dependence_visualizations.py). Match each figure to an AR, MA, invertibility, or diagnostic concept.
10. Simulate AR(1) processes with $\phi=0.2$, $0.7$, and $-0.7$. Compare their sample ACFs and explain the alternating pattern for negative dependence.
11. Use the same innovation sequence to simulate an MA(1) with $\theta=0.5$ and $\theta=2$. Which representation has a stable inverse?
12. Calculate the roots of $1-0.6z+0.2z^2$ and explain what their moduli imply for an AR(2) process.
13. Construct a residual series with zero lag-1 ACF but dependence in its squared values. Explain why a mean-only diagnostic can miss it.
14. For a monthly series with a large ACF spike at lag 12, list three competing explanations and a diagnostic that separates each pair.
15. Compare the denominator-$n$ and denominator-$n-h$ sample autocovariance conventions on a short series. State which one your software uses.

## Reflection

Write a model-identification paragraph that names the transformation, ACF/PACF evidence, candidate models, residual checks, and out-of-sample comparison. Do not call a cutoff pattern a proof.

## Extension tasks

16. Calculate $\gamma(0)$ and $\gamma(1)$ for an AR(1) with $\phi=0.8$ and innovation variance 2.
17. Use a simulated AR(2) with complex roots to explain a damped oscillation in the ACF.
18. Show that replacing an MA(1) parameter by its reciprocal can preserve second-order behavior after rescaling the innovation variance.
19. Compare a residual ACF, a squared-residual ACF, and a turning-point count for the same series.
20. Calculate the approximate white-noise ACF band for $n=400$ and explain its limitations.
21. Fit an AR model using Yule-Walker and conditional least squares. Compare coefficients and root locations.

## Worked solutions

1. $\bar x=10/4=2.5$; centered values $(-1.5,-0.5,1.5,0.5)$. $\hat\gamma(0)=\frac14(2.25+0.25+2.25+0.25)=5/4=1.25$. Lag-1 cross-products: $(-1.5)(-0.5)+(-0.5)(1.5)+(1.5)(0.5)=0.75-0.75+0.75=0.75$, so $\hat\gamma(1)=0.75/4=0.1875$. With denominator $n-1=3$ it is $0.25$ (and the matching $\hat\gamma(0)$ would be $5/3$).
2. $\rho(h)=\phi^h$: $\rho(1)=0.7$, $\rho(2)=0.49$, $\rho(3)=0.343$. The sketch is a positive geometric decay (tails off, never exactly zero).
3. $\gamma(0)=\sigma^2(1+\theta^2)=1.25$, $\gamma(1)=\theta\sigma^2=0.5$, $\rho(1)=0.5/1.25=0.4$. Note the bound $|\rho(1)|\le0.5$.
4. For AR(1), $\rho(h)=\phi\rho(h-1)$ so each lag inherits dependence from the previous one and decays geometrically, never hitting zero. For MA(1), $X_t$ and $X_{t+h}$ share no shocks when $h\ge2$, so $\gamma(h)=0$. In finite samples, sample ACFs carry noise of order $1/\sqrt n$: the AR(1) tail merges into the noise band after a few lags, and the MA(1) shows a few spurious spikes beyond lag 1 (about 5% outside the bands).
5. Mean: $\mu=1/(1-0.8)=5$. Variance: $\sigma^2/(1-\phi^2)=1/(1-0.64)=1/0.36\approx2.778$. For $\phi=1$ the process is $X_t=1+X_{t-1}+\varepsilon_t$, a random walk with drift: the root of $1-\phi z$ is on the unit circle, there is no finite stationary mean or variance, $\operatorname{Var}(X_t)=t\sigma^2$ grows without bound, and the drift gives mean $X_0+t$.
6. Yule-Walker: $\rho_1=\phi_1/(1-\phi_2)=0.6/1.2=0.5$. $\rho_2=\phi_1\rho_1+\phi_2=0.3-0.2=0.1$. $\rho_3=\phi_1\rho_2+\phi_2\rho_1=0.06-0.10=-0.04$.
7. $\pi(B)=1/(1+\theta B)=\sum(-\theta)^jB^j$, so coefficients $1,-0.5,0.25,-0.125$ (and $(-0.5)^j$ onwards, summable). For $\theta=2$ they are $1,-2,4,-8,\dots$, which diverge, so $\varepsilon_t$ cannot be written as a convergent combination of the past $X$.
8. The PACF of an AR(2) cuts off after lag 2 (sharp, with later lags inside the band) while the ACF tails off. Code:
   ```python
   from statsmodels.tsa.arima_process import ArmaProcess
   x = ArmaProcess([1,-0.6,0.2],[1]).generate_sample(1000, distrvs=rng.normal)
   plot_acf(x); plot_pacf(x)
   ```
9. Model answer: the AR plots (path, geometric ACF, PACF cutoff) illustrate AR; the cutoff ACF plots illustrate MA; the unit-circle or inverse-filter weight plots show invertibility/stationarity; residual ACF/Q-Q plots are diagnostics. Run the script and map each panel's title to these four.
10. Model answer: $\phi=0.2$ has a small lag-1 spike and quickly disappears; $\phi=0.7$ decays slowly ($0.7,0.49,\dots$); $\phi=-0.7$ gives $(-0.7)^h$, alternating signs with the same magnitude decay, because each value tends to be pushed to the opposite side of the mean.
    ```python
    for phi in (0.2, 0.7, -0.7):
        x = ArmaProcess([1,-phi],[1]).generate_sample(500, distrvs=rng.normal)
        print(phi, acf(x, nlags=4))
    ```
11. Both have $\rho(1)=0.4$, so the ACFs match. Only $\theta=0.5$ is invertible: its inverse filter $\sum(-0.5)^jB^j$ converges. $\theta=2$ has a divergent inverse; its invertible equivalent is $\theta=0.5$ with variance $\sigma^2\cdot4$.
12. $0.2z^2-0.6z+1=0$: $z=\dfrac{0.6\pm\sqrt{0.36-0.8}}{0.4}=1.5\pm1.658i$. Modulus $\sqrt{2.25+2.75}=\sqrt5\approx2.236>1$, so the AR(2) is stationary (equivalently the characteristic roots $1/z$ have modulus $0.447<1$). Complex roots imply a damped pseudo-cycle with period about $2\pi/\arccos(\phi_1/(2\sqrt{-\phi_2}))=2\pi/\arccos(0.671)\approx 7.5$ steps.
13. Example: $r_t=\sigma_tz_t$ with $\sigma_t^2=0.2+0.7r_{t-1}^2$, $z_t$ iid $N(0,1)$. Then $\operatorname{Corr}(r_t,r_{t-1})=0$ but $\operatorname{Corr}(r_t^2,r_{t-1}^2)=0.7$. A mean-only diagnostic (ACF of $r_t$, Ljung-Box on $r_t$) tests only linear predictability of the level, so it passes; use the ACF of $r_t^2$ or an ARCH-LM test.
14. Candidate explanations: (i) deterministic seasonal mean pattern: check seasonal means/dummy regression; (ii) stochastic seasonal unit root: check seasonal-difference ACF and seasonal unit-root test; (iii) seasonal MA/AR term or a one-off outlier/calendar effect: compare seasonal-ARMA fits, and look for an isolated spike in residuals. Each pair is separated by fitting both and comparing residual ACF at lags 12, 24 and out-of-sample error.
15. For $x=(1,2,4,3)$ at $h=1$: denominator $n$ gives $0.1875$; denominator $n-h=3$ gives $0.25$. The $n$ version guarantees a positive semidefinite autocovariance sequence and is used by `statsmodels.acf` (by default `adjusted=False`) and R `acf`. Report which your software uses.
16. $\gamma(0)=\sigma^2/(1-\phi^2)=2/0.36=5.\overline5$, $\gamma(1)=\phi\gamma(0)=0.8(5.\overline5)=4.\overline4$.
17. Complex roots $re^{\pm i\omega}$ give $\rho(h)\propto r^{h}\cos(\omega h+\psi)$ with $r=\sqrt{-\phi_2}$. For $\phi_1=1.2,\phi_2=-0.8$: $r=0.894$, $\cos\omega=\phi_1/(2r)=0.671$, $\omega\approx0.83$ rad, period $\approx7.5$ steps. The ACF oscillates with that period and amplitude shrinks by $0.894$ per step.
18. $\gamma(0)=\sigma^2(1+\theta^2)$ and $\gamma(1)=\theta\sigma^2$. Replace $(\theta,\sigma^2)$ by $(1/\theta,\theta^2\sigma^2)$: $\theta^2\sigma^2(1+1/\theta^2)=\sigma^2(\theta^2+1)$ and $(1/\theta)\theta^2\sigma^2=\theta\sigma^2$. Same $\gamma$, so same second-order behavior; only one choice (with $|\theta|<1$) is invertible.
19. Compute `acf(res)`, `acf(res**2)` and the turning-point count (expected $2(n-2)/3$, variance $(16n-29)/90$). A white-noise but ARCH series passes the first and the turning-point test and fails the second; a series with remaining linear dependence fails the first. Each statistic detects a different departure from iid.
20. Approximate 95% band $\pm1.96/\sqrt{400}=\pm0.098$. Limitations: it assumes iid noise (invalid for residuals of a fitted model, where it is conservative at small lags), ignores multiple testing (about 1 in 20 lags exceeds it by chance), and is asymptotic.
21. Model answer:
    ```python
    from statsmodels.regression.linear_model import yule_walker
    from statsmodels.tsa.ar_model import AutoReg
    rho, _ = yule_walker(x, order=2, method="mle")
    cls = AutoReg(x, lags=2, trend="n").fit().params
    np.roots(np.r_[1, -rho]), np.roots(np.r_[1, -cls])
    ```
    The coefficients agree closely for long series; in short samples Yule-Walker estimates are biased toward zero (roots pulled away from the unit circle) when the process is near-nonstationary, while conditional least squares conditions on, and so drops, the first two observations.

## Submission check

State the covariance convention, sign convention for the MA polynomial, stationarity/invertibility conditions, and why the final model is adequate for the stated task.
