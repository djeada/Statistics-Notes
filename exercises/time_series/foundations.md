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
