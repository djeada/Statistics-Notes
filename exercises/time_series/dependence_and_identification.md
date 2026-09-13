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

## Submission check

State the covariance convention, sign convention for the MA polynomial, stationarity/invertibility conditions, and why the final model is adequate for the stated task.
