# Randomness and Trend Tests

## Worked calculation: counting turning points

For the short sequence

$$
1,\ 3,\ 2,\ 4,\ 3,
$$

the interior observations at positions 2, 3, and 4 are turning points: the sequence goes up then down at 3, down then up at 2, and up then down at 4. Thus the count is 3. A turning-point test compares the observed count with the distribution expected under randomness; it is not a general test of every possible dependence pattern.

For a fitted model, the more important question is whether residuals still contain predictable structure. A residual ACF, a Ljung-Box test, and a plot of residual squares answer different questions and should be read together.

![Turning points in a synthetic series](../../assets/time_series/turning_points_example.png)

When a series looks noisy, it is still useful to check whether the noise is **random** or whether weak structure (trend or dependence) is present. The tests below are lightweight diagnostics for an IID or weak-dependence null.

### Ljung-Box Q Test (Independence)

The **Ljung-Box** test checks whether a collection of autocorrelations is jointly zero:

$$
Q = n(n + 2) \sum_{k=1}^{m} \frac{\hat{r}_k^2}{n - k}
$$

where $\hat{r}_k$ is the sample autocorrelation at lag $k$, and $m$ is the maximum lag. Under the IID null, $Q$ is approximately $\chi^2_m$ (or $\chi^2_{m - p - q}$ when testing model residuals).

### McLeod-Li Test (Squared Series)

The **McLeod-Li** test applies the Ljung-Box statistic to **squared** data (or squared residuals) to detect conditional heteroskedasticity:

$$
Q_{\text{ML}} = n(n + 2) \sum_{k=1}^{m} \frac{\hat{r}_{k, \text{sq}}^2}{n - k}
$$

Significant autocorrelation in the squared series indicates volatility clustering and suggests ARCH/GARCH effects.

### Turning Point Test (IID vs. Not IID)

A **turning point** occurs at time $t$ if the series changes direction:

$$
(x_{t-1} < x_t > x_{t+1}) \quad \text{or} \quad (x_{t-1} > x_t < x_{t+1})
$$

Let $T$ be the number of turning points in a series of length $n$. For a continuous IID sequence:

$$
E[T] = \frac{2(n - 2)}{3}, \quad \text{Var}(T) = \frac{16n - 29}{90}
$$

A standardized score $(T - E[T]) / \sqrt{\text{Var}(T)}$ can be compared to a normal reference.

Turning points marked on a synthetic series:

![turning points example](../../assets/time_series/turning_points_example.png)

### Difference-Sign Test (Randomness)

This test looks at the signs of successive differences:

$$
d_t = x_t - x_{t-1}, \quad t = 2, \ldots, n
$$

Let $s_t = \text{sign}(d_t) \in \{-1, +1\}$. Under a randomness assumption with a continuous distribution, the signs are approximately independent and equally likely.

One common version counts **sign changes** between adjacent differences:

$$
C = \sum_{t=3}^{n} I(s_t \neq s_{t-1})
$$

For $m = n - 1$ signs, there are $m - 1$ possible changes. Under the null:

- $E[C] \approx (n - 2) / 2$
- $\text{Var}(C) \approx (n - 2) / 4$

Large deviations from the expected number of sign changes suggest non-random structure (e.g., trend or negative dependence).

### Rank Test (Detecting Trend)

The rank test checks for a monotonic trend without assuming normality.

1. Replace the series values with their ranks $r_t$.
2. Compute **Spearman's rank correlation** between time $t$ and rank $r_t$:

$$
\rho_s = 1 - \frac{6 \sum_{t=1}^{n} (r_t - t)^2}{n(n^2 - 1)}
$$

If $\rho_s$ is far from zero, the series likely has a monotone trend. This test is robust to outliers and does not require a parametric model.

Because multiple tests are often applied together, the probability of at least one false positive increases. Treat these as screening tools and follow up with model-based diagnostics (ACF/PACF, unit root tests, or regression diagnostics).

## Student guide: randomness is a collection of null hypotheses

There is no single test that proves a time series is random. Different tests ask different questions:

- are adjacent values linearly dependent?
- are there too many or too few turning points?
- is there a monotone trend?
- are squared residuals dependent?
- is the process compatible with a unit-root null?

Choose the diagnostic to match the model failure that matters.

### Turning points

For the sequence

$$
1,\ 3,\ 2,\ 4,\ 3,
$$

the interior observations at positions 2, 3, and 4 are local turning points, so the count is 3. A turning-point test compares the count with a reference distribution under a random-order or continuous iid null. Ties need a stated convention.

Too few turning points can indicate persistence or trend. Too many can indicate alternation or negative dependence. The test does not distinguish a smooth trend from every other source of persistence.

### Runs

Convert observations to signs relative to a reference level, often the median. A run is a maximal sequence of equal signs. For signs

$$
++--+--,
$$

there are four runs: $++$, $--$, $+$, and $--$. Too few runs suggest clustering; too many suggest alternation. A median choice can discard information, so use it as a simple diagnostic rather than a complete dependence analysis.

### Ljung-Box residual test

The Ljung-Box statistic through lag $m$ is

$$
Q(m)=n(n+2)\sum_{h=1}^{m}\frac{\hat\rho(h)^2}{n-h}.
$$

The null is that autocorrelations through the tested lags are jointly zero, with degrees-of-freedom adjustments needed after fitting parameters. A p-value of $0.002$ is evidence that the residuals retain serial structure at one or more tested lags. It does not identify the correct new model.

### Trend tests and breaks

A monotone trend test can be useful when a linear trend is not justified, but a monotone trend and a structural break can look similar in a short record. Plot the series, rolling moments, and residuals around the suspected change before interpreting a test.

### Multiple diagnostics

If ten independent tests are each run at level $0.05$, the probability of at least one false rejection is

$$
1-(1-0.05)^{10}\approx0.401.
$$

Time-series tests are usually dependent, so this is not an exact family-wise error probability, but it demonstrates why a collection of p-values should not be read as ten independent discoveries.

### A practical diagnostic sequence

1. Inspect the raw plot and timestamp structure.
2. Remove or model known trend/seasonality.
3. Inspect residual ACF and Ljung-Box results.
4. Inspect squared residuals for variance dependence.
5. Use turning-point or runs tests for a complementary ordering check.
6. Investigate breaks and outliers.
7. Validate the resulting model by forecasting.

### Visual companion

Run [dependence_visualizations.py](../../scripts/time_series/dependence_visualizations.py):

![Randomness and residual diagnostics](../../assets/time_series/dependence/08_randomness_residual_diagnostics.png)
