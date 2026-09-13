# Foundations

Read [stochastic processes and white noise](../../notes/time_series/stochastic_processes_and_white_noise.md), [difference equations](../../notes/time_series/difference_equations.md), and [random walks](../../notes/time_series/random_walk.md) first.

1. For the geometric series with ratio $r=0.5$, calculate the partial sum through $r^4$ and the infinite sum. What is the size of the omitted tail?
2. Solve $x_t=0.7x_{t-1}+2$ with $x_0=10$. Calculate $x_1$, $x_2$, and the equilibrium. Explain why the distance from equilibrium shrinks.
3. For $(2,4,4,6)$, calculate the mean, population-style variance, and unbiased sample variance. Explain why the two variance denominators answer different questions.
4. Let $\varepsilon_t$ be independent with variance 4. What are $\gamma(0)$ and $\gamma(h)$ for $h\ne0$? Does this alone prove independence for an arbitrary white-noise process?
5. A random walk starts at $X_0=5$ and has shocks $1,-2,0.5$. Calculate $X_1$, $X_2$, and $X_3$. If shock variance is 1, calculate $\operatorname{Var}(X_3\mid X_0)$.
6. Simulate 500 observations of white noise and a random walk with the same shocks. Compare their plots and sample variances. Which variance should change as the sample length grows?
7. Write one example of a process with zero linear autocorrelation but nonlinear dependence. Explain why a residual ACF may miss it.

## Checks

- The geometric partial sum is $1.9375$, the limit is $2$, and the omitted tail is $0.0625$.
- The recursion gives $x_1=9$, $x_2=8.3$, and equilibrium $2/(1-0.7)=6.\overline6$.
- The variance values are $2$ with denominator $n$ and $8/3$ with denominator $n-1$.
- The random-walk variance after three independent unit-variance shocks is $3$.

## Applied practice

8. Run [foundations_visualizations.py](../../scripts/time_series/foundations_visualizations.py). Change the AR coefficient from $0.7$ to $0.95$. Describe what changes in the path, ACF, and forecast horizon.
9. Construct an additive series with trend $0.2t$, period-12 seasonality, and Gaussian noise. At $t=6$, calculate the trend and seasonal contributions before simulating the noise.
10. Generate regular and irregular sampling of the same continuous signal. Explain which ACF and spectral calculations assume a regular grid.
11. Apply a nine-point moving average to a noisy trend. Identify the boundary observations that use incomplete or padded windows.
12. Simulate a stationary AR(1), a random walk, and an explosive AR(1). Compare rolling means and variances rather than relying on one plot.
13. Explain why a changing marginal variance can make a process unsuitable for a constant-variance Gaussian model even when its mean is approximately zero.

## Reflection

For each simulation, write down the data-generating equation, the information available at the forecast origin, and the feature that would make the process difficult for an independent-sample method.

## Additional checks

- For $x_t=0.95x_{t-1}+\varepsilon_t$, the shock effect decays much more slowly than for $\phi=0.7$.
- A period-12 sinusoid has frequency $1/12$ cycles per observation.
- A centered smoother is acceptable for retrospective description but uses future observations as a real-time feature.

## Extension tasks

14. Derive the closed-form solution for $x_t=c+\phi x_{t-1}$ and verify it numerically for $c=2$, $\phi=0.7$, and $x_0=10$.
15. Simulate two series with the same histogram but different ACFs. Explain why independent resampling fails to reproduce one of them.
16. Compare a centered and trailing moving average at the final five observations. Identify which values would be available in real time.
17. Add a level shift to a stationary series. Decide whether a global variance and mean are meaningful summaries.
18. Write a data dictionary that states the time support, sampling interval, unit, and release time for a series of your choice.
19. Explain how changing from hourly observations to daily totals can alter variance, seasonality, and dependence.

## Submission check

Include the generating equation, seed, parameter values, one hand calculation, one figure, and a paragraph explaining what the simulation does not establish.
