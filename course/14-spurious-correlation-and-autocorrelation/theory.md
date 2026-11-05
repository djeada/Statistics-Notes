# Theory: spurious correlation and autocorrelation

## Why this matters

Two quantities that have nothing to do with each other can show a correlation of 0.9 and a "highly significant" p-value.
The failure is routine in time-series work: someone finds a "leading indicator", builds a forecast or an alert on it, and it
falls apart in the next quarter. The cause is **autocorrelation**: when today's value is mostly yesterday's value, neighbouring
observations are not independent, so the sample contains far less information than its length suggests and the textbook
significance test is invalid.

## Autocorrelation

The lag-$k$ autocorrelation of a series $x_1,\dots,x_n$ with mean $\bar x$ is

$$
r_k = \frac{\sum_{t=k+1}^{n} (x_t-\bar x)(x_{t-k}-\bar x)}{\sum_{t=1}^{n} (x_t-\bar x)^2}.
$$

For white noise, $r_k$ is approximately normal with standard deviation $1/\sqrt{n}$, so values outside $\pm 2/\sqrt n$ are
signals. **Worked example**: $x = 10,12,13,15,16,18$ has $\bar x = 14$, numerator $19$, denominator $42$, so $r_1 = 0.452$. A series
that trends or wanders has a large $r_1$ and slowly decaying $r_k$ (see the autocorrelation chart in the dashboard).

## Random walks and spurious correlation

A **random walk** $x_t = x_{t-1} + \varepsilon_t$ is the sum of its shocks, so it never returns to a mean and its $r_k$ stays near 1.
Two *independent* random walks have sample correlations that are widely spread over $(-1,1)$, not concentrated near 0: in a
simulation of 10,000 independent pairs of length 250, about 40 % had $|r| > 0.5$. Trends (a shared upward drift,
growth, inflation, seasonality) create the same illusion. This is the **spurious regression** problem (Yule 1926; Granger and
Newbold 1974): the usual $t$ and $R^2$ are misleading, and a tell-tale sign is a high $R^2$ together with a low Durbin-Watson.

**Worked example (toy).** $A = 10,12,13,15,16,18$ and $B = 5,6,8,8,9,11$ both rise, so $\mathrm{corr}(A,B)=0.969$. Their
daily changes are $2,1,2,1,2$ and $1,2,0,1,2$, and those are correlated at $-0.33$ (with only 5 points, no evidence of anything).
All of the levels correlation came from both series going up.

## The remedies

1. **Difference** (or take growth rates, lesson 09): correlate $\Delta x_t = x_t - x_{t-1}$ with $\Delta y_t$. A relationship that
   survives differencing is not just two things trending together.
2. **Detrend / de-season** and model the remainder (lessons 07-08).
3. **Model the dynamics**: include lagged $y$ as a predictor, or use regression with autocorrelated errors.
4. **Reduce the sample size honestly**: with autocorrelations $\rho_x,\rho_y$, the effective sample size is roughly
   $n_{\text{eff}} \approx n\,\dfrac{1-\rho_x\rho_y}{1+\rho_x\rho_y}$ (Bartlett). Use it in the $t$ test of a correlation.

## Durbin-Watson

For regression residuals $e_t$:

$$
DW = \frac{\sum_{t=2}^{n} (e_t-e_{t-1})^2}{\sum_{t=1}^{n} e_t^2} \approx 2\,(1-r_1(e)).
$$

$DW\approx 2$ means no first-order autocorrelation, $DW\to 0$ strong positive autocorrelation, $DW\to 4$ negative. **Worked
example**: residuals $1.0, 0.8, 0.5, -0.2, -0.6, -0.9$ give $\sum(\Delta e)^2 = 0.87$, $\sum e^2 = 3.10$, so $DW = 0.28$: smooth,
strongly positively autocorrelated residuals. Rule of thumb (Granger-Newbold): $R^2 > DW$ is a warning of a spurious regression.
Formal critical values depend on $n$ and the number of predictors; for diagnostics here the approximation $2(1-r_1)$ is enough.

## Assumptions and pitfalls

1. **Differencing removes information** about long-run (cointegrated) relationships: two random walks that share a common stochastic
   trend are related even though their changes may be weakly correlated. Testing for this is beyond this course; the point is
   that high correlation of levels is never sufficient evidence.
2. **A significant correlation of changes is not causation either**; look for a mechanism and out-of-sample stability.
3. **Lead-lag claims** ("A leads B by 3 days") must be tested on differenced or pre-whitened data (lesson 11).
4. **Rolling correlations** that jump between large positive and negative values are a symptom of this problem.
5. **Over-differencing** adds negative autocorrelation (an artificial $r_1 \approx -0.5$); stop when the changes look like noise.
6. Seasonal data need seasonal differencing (lag 7 or 12), not just first differences.

## Related notes

- [Correlation and lagged relationships](../11-correlation-and-lagged-relationships/theory.md)
- [Differencing and growth rates](../09-differencing-and-growth-rates/theory.md)
- [Trend, seasonality and noise](../07-trend-seasonality-and-noise/theory.md)
- [Residual analysis and model diagnostics](../15-residual-analysis-and-model-diagnostics/theory.md)
- Repo notes: [Random walk](../../notes/time_series/random_walk.md), [Autocorrelation function](../../notes/time_series/autocorrelation_function.md)
