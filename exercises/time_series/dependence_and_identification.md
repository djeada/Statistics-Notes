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
