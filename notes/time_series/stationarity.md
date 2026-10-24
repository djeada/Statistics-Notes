# Stationarity in Time Series

Stationarity is a statement about a process across possible realizations, not a demand that one plotted path look flat. Imagine moving an observation window from one date to another. If the relevant probability laws stay the same after that common shift, information from one part of the record can describe another part under those laws.

**Weak stationarity** requires a common finite mean and variance, with covariance determined by lag. **Strict stationarity** requires every finite joint distribution to be unchanged by a time shift. A process can fluctuate strongly and remain stationary; it can also look quiet over a short interval while violating stationarity over the full record.

Stationary ARMA theory uses common moments and lag relationships to make estimation and forecasting tractable. A changing deterministic mean, a unit root, a break, and changing variance violate different parts of that setup. Their remedies differ: removing a fitted trend, differencing an accumulated level, including an intervention, and modeling variance are not interchangeable ways of making a plot appear stable.

## Worked calculation: the stationary AR(1) mean and variance

Consider

$$
X_t=1+0.8X_{t-1}+\varepsilon_t,
\qquad \mathrm{Var}(\varepsilon_t)=1.
$$

The stationary mean solves

$$
\mu=1+0.8\mu
\quad\Longrightarrow\quad
\mu=5.
$$

After centering around 5, the stationary variance is

$$
\mathrm{Var}(X_t)
=\frac{1}{1-0.8^2}
=\frac{1}{0.36}
\approx2.778.
$$

Taking expectations gives $\mu=1+0.8\mu$, hence $\mu=5$. Centering leaves a recursion for deviations. Its variance satisfies $v=0.8^2v+1$, because the new shock is uncorrelated with the previous value. Solving yields $v=1/(1-0.8^2)$. The condition $|0.8|<1$ makes the past-driven shock weights decay. At a unit root they do not decay, and from a fixed starting value the variance keeps increasing.

The figure below contrasts these cases. A stationary AR(1) fluctuates around a stable level, a unit-root process wanders as shocks accumulate, and an explosive process moves increasingly far from its starting region.

![Stationary, unit-root, and explosive AR(1) behavior](https://raw.githubusercontent.com/djeada/Statistics-Notes/main/assets/time_series/student/10_stationarity_cases.png)

![Stationarity cases](https://raw.githubusercontent.com/djeada/Statistics-Notes/main/assets/time_series/foundations/06_stationarity_cases.png)

Stationarity describes which probabilistic features of a time series remain stable as time shifts. For weak stationarity, the mean and variance are constant and autocovariance depends only on lag. This condition matters because ARMA models are formulated for stationary series, while ARIMA models handle certain non-stationary series by differencing them before applying an ARMA structure.

## What remains unchanged when time shifts?

Two common definitions are used:

1. Strict stationarity requires the entire joint distribution to be unchanged by a shift in time.
2. Weak, or second-order, stationarity requires a constant mean and variance and an autocovariance that depends only on lag.

## Why Do We Care About Stationarity?

Suppose synthetic stock prices contain an upward deterministic trend together with shorter-term fluctuations, and the goal is to study recurring seasonal variation. The changing level can obscure that seasonal structure, so the mean pattern should be addressed before interpreting the remaining dependence.

**Addressing non-stationarity by detrending**

If a linear trend is a reasonable description of the changing mean, it can be estimated by least squares:

$$
\text{Stock Price} = z + b \times \text{Time}.
$$

The fitted line estimates a deterministic mean, with intercept $z$ and slope $b$. Subtracting it changes the question from the level itself to departures around that line. If those departures have stable variance and lag dependence, a stationary residual model may be suitable. If the apparent trend was instead an accumulated random walk, subtracting a line does not undo the shock accumulation; a smooth residual plot alone cannot establish the required condition.

The next figure shows this progression: the upper panel contains the original series and fitted trend, while the lower panel shows the detrended residuals. The key point is that detrending changes the mean structure; it does not automatically guarantee stationarity.

![Synthetic Stock Prices Analysis](https://github.com/user-attachments/assets/db1f2c1c-f1ce-4aa8-b3e0-34d821a4a001)

The following examples provide two additional views of detrending and its effect on the series.

![detrending example](https://raw.githubusercontent.com/djeada/Statistics-Notes/main/assets/time_series/detrending_example.png)

![Detrending](https://raw.githubusercontent.com/djeada/Statistics-Notes/main/assets/time_series/diagnostics/01_detrending.png)

## Intuition for Stationary Time Series

A stationary series has a stable probabilistic structure over time. For weak stationarity:

- the mean does not systematically change with time;
- the variance remains constant; and
- dependence between observations is determined by their lag, not by their absolute position in time.

A fixed December uplift violates a constant unconditional mean, even if December behaves similarly every year. Modeling that uplift explicitly may leave stationary errors. Conversely, a stationary AR process can have long runs above its mean and oscillating covariance without any deterministic trend or seasonal mean. Stationarity concerns which probability features change with the time origin, not whether the process has visible temporal structure.

## Strict Stationarity

A process is said to be **strictly stationary** if the joint distribution of any subset of observations $X_{t_1}, X_{t_2}, \dots, X_{t_k}$ is the same as the distribution of $X_{t_1 + \tau}, X_{t_2 + \tau}, \dots, X_{t_k + \tau}$ for all $\tau$.

The shift must be common to every time in the selected collection. Matching each one-date marginal distribution is insufficient if the dependence between dates changes. Strict stationarity preserves the entire finite-dimensional distribution, including tail behavior and nonlinear dependence. It does not require moments to exist: an IID Cauchy process is strictly stationary even though its mean and variance are undefined.

## Weak (Second-Order) Stationarity

Weak stationarity, also known as **second-order stationarity**, requires only a constant **mean**, a constant finite **variance**, and an **autocovariance** that depends solely on the lag between observations, not on time itself.

A time series $\{X_t\}$ is weakly stationary if:

1. The **mean** of the series is constant: $E[X_t] = \mu$ for all $t$.
2. The **variance** is constant: $\mathrm{Var}(X_t) = \sigma^2$ for all $t$.
3. The **autocovariance** between $X_t$ and $X_{t+k}$ depends only on the lag $k$, not on $t$:

$$
\mathrm{Cov}(X_t, X_{t+k}) = \gamma(k)
$$

Weak stationarity makes second-order calculations reusable across dates without specifying the full joint law. It neither implies independence nor fixes higher moments. For example, independent observations could alternate between a standard normal distribution and equally likely values $-1$ and $1$. Every date then has mean 0 and variance 1, with zero cross-time covariance, but the marginal distribution alternates. The process is weakly stationary and not strictly stationary.

## Properties of Stationary Processes

### Mean, Variance, and Autocovariance Functions

To analyze a stationary process, we focus on three key functions:

- The **mean function** $\mu(t) = E[X_t]$ represents the expected value of the process at time $t$, and for a stationary process, this should remain constant.
- The **variance function** $\sigma^2(t) = \mathrm{Var}(X_t)$ gives the variance at time $t$, which must also be constant for stationarity.
- The **autocovariance function** $\gamma(k) = \mathrm{Cov}(X_t, X_{t+k})$ measures how the process correlates with itself at different time lags $k$, and for a stationary process, it depends only on the lag $k$, not on time $t$.

More generally, the covariance function can be written as:

$$
\gamma(r, s) = \mathrm{Cov}(X_r, X_s)
$$

Weak stationarity implies $\mu(t) = \mu$ and $\gamma(r, s)$ depends only on the lag $h = s - r$.

The figure below illustrates the contrast between stable moments and moments that change over time. Changes in the local mean or variance are visual evidence against global weak stationarity.

![Moments changing over time](https://raw.githubusercontent.com/djeada/Statistics-Notes/main/assets/time_series/foundations/04_moments_change_over_time.png)

### Autocorrelation and Bounds

For a weakly stationary process, the **autocorrelation function** $\rho(k)$, which measures the correlation between two points in the series separated by lag $k$, is bounded by -1 and 1:

$$
-1 \leq \rho(k) \leq 1
$$

This bound can be derived from basic linear algebra principles that apply to correlations between random variables.

### q-Dependence and q-Correlation

A **q-dependent** process makes groups of observations independent when the groups are separated by more than $q$ dates. An MA($q$) driven by independent shocks has this property because sufficiently separated groups use disjoint shock sets. An AR process generally retains a decaying contribution from a shock at arbitrarily long lags, so short memory does not necessarily mean independence after some finite cutoff.

A weaker property is **q-correlation**: the autocovariance is zero beyond lag $q$:

$$
\gamma(h) = 0 \quad \text{for} \quad |h| > q.
$$

Weak white noise is 0-correlated: all nonzero-lag covariances vanish. That statement concerns linear association and is weaker than independence. An MA($q$) with weak-white-noise shocks is q-correlated even when its shocks are not independent. Conversely, a valid stationary covariance sequence with a finite cutoff admits an appropriate finite MA second-order representation; this matches covariance behavior without establishing a unique independent-shock mechanism.

### Linear Processes and Linear Filters

If $\{Y_t\}$ is a stationary series with mean 0 and autocovariance $\gamma_Y$, then a linear filter:

$$
X_t = \sum_{j=-\infty}^{\infty} \psi_j Y_{t-j} = \psi(B) Y_t
$$

is weakly stationary under the sufficient condition $\sum_{j=-\infty}^{\infty}|\psi_j|<\infty$. The condition controls the infinite weighted sum and permits its second moments to be calculated consistently. A filter can nevertheless use future values when negative lags are included. Such a stationary filtered process may be suitable for retrospective analysis while the same filter would be unavailable for a live forecast at its endpoint.

The autocovariance of the filtered process is:

$$
\gamma_X(h) = \sum_{j=-\infty}^{\infty} \sum_{k=-\infty}^{\infty} \psi_j \psi_k\, \gamma_Y(h - k + j)
$$

## Examples of Stationary Processes

### IID Noise vs. White Noise

IID noise with mean 0 and variance $\sigma^2$ is the simplest stationary building block. White noise is slightly weaker: it only requires zero mean and zero autocovariance for nonzero lags (uncorrelated), not full independence.

### White Noise

White noise is a basic stationary building block. In the weak white-noise definition, the process has mean zero, constant finite variance, and zero autocovariance at every nonzero lag. Independence and Gaussianity are stronger assumptions, not part of the basic second-order definition. A common special case is Gaussian white noise, for which

$$
X_t \sim \mathcal{N}(0, \sigma^2).
$$

Its second-order properties are:

- the mean is $E[X_t]=0$;
- the variance is $\mathrm{Var}(X_t)=\sigma^2$;
- the autocovariance function is:

$$
\gamma(k) =
\begin{cases}
\sigma^2 & \text{if } k = 0 \\
0 & \text{if } k \neq 0
\end{cases}
$$

- the autocorrelation function is:

$$
\rho(k) =
\begin{cases}
1 & \text{if } k = 0 \\
0 & \text{if } k \neq 0
\end{cases}
$$

Below is a plot of synthetically generated white noise:

![Simulated white noise around a stable mean](https://github.com/user-attachments/assets/a24cc561-f34a-431e-bac0-2f9cd5e62a49)

These properties make weak white noise weakly stationary. Gaussian white noise is also strictly stationary because its joint Gaussian distribution is determined by the constant mean and lag-based covariance structure.

### Moving Average (MA) Process

A moving average process of order $q$, denoted MA($q$), is another weakly stationary model. It is defined as:

$$
X_t = \beta_0 Z_t + \beta_1 Z_{t-1} + \dots + \beta_q Z_{t-q}
$$

where $Z_t$ is independent white noise with variance $\sigma_Z^2$; Gaussian innovations are a common special case.

For an MA(q) process:

- The **mean** is zero: $E[X_t] = 0$.
- The **variance** is constant:

$$
\mathrm{Var}(X_t) = \sigma_Z^2 \sum_{i=0}^{q} \beta_i^2
$$

- The **autocovariance** function $\gamma(k)$ depends on the lag $k$:

$$
\gamma(k) =
\begin{cases}
\sigma_Z^2 \sum_{i=0}^{q-|k|} \beta_i \beta_{i+|k|}, & |k| \leq q, \\
0, & |k| > q.
\end{cases}
$$

The autocorrelation function $\rho(k)$ is obtained by normalizing the autocovariance by the variance:

$$
\rho(k) = \frac{\gamma(k)}{\gamma(0)}
$$

The following plot shows an MA(2) realization. Its values can look locally dependent even though the theoretical autocovariance is exactly zero beyond lag 2:

![A stationary MA(2) realization](https://github.com/user-attachments/assets/28e1d7fa-243b-4841-afba-afd2188ac400)

The MA(q) process is weakly stationary because its mean and variance are constant, and the autocovariance depends only on the lag.

## Non-Stationary Processes

Identify which feature fails before deciding how to respond. A deterministic linear trend changes the mean; a zero-drift random walk keeps the mean constant but has growing variance; a break can change several features at once. Conditional variance can also vary while unconditional moments remain stationary, as in a covariance-stationary GARCH model. Distinguish changing conditional volatility from a claim that global weak stationarity must fail.

Two important forms of non-stationarity are:

1. trend-stationary processes;
2. difference-stationary processes.

### Trend-Stationary Processes

A **trend-stationary** process has a deterministic trend plus a stationary remainder. Its mean can change with time because of the trend, while the remainder has stable moments and lag dependence. In the usual short-memory case, a shock to that remainder fades, so the process returns toward its trend rather than carrying the shock permanently in its level.

**Detrending.**

To achieve stationarity in such series, one can remove the trend component. This is typically done by fitting a trend line (e.g., linear or polynomial) to the data and subtracting it from the original series. The resulting series, with the trend removed, should exhibit stationary behavior.

### Difference-Stationary Processes

A difference-stationary process becomes stationary after an appropriate number of differences. The simplest case is a random walk: $X_t-X_{t-1}$ removes all previously accumulated shocks and leaves the new one. A fitted deterministic trend does not perform that cancellation. The distinction matters for forecasts because a shock to a trend-stationary remainder fades under the usual short-memory model, while a random-walk shock permanently shifts the forecast level.

**Differencing.**

Ordinary differencing compares adjacent dates; seasonal differencing compares the same position in successive cycles. Each is justified by a particular accumulation or repeating component that cancels in the subtraction. Afterward, inspect the transformed series again: differencing can leave variance changes, seasonal predictors, or structural breaks, and unnecessary differencing can create negative short-lag correlation rather than improve the model.

### Transformations to Achieve Stationarity

When a model requires a stationary input, choose a transformation that addresses the identified source of nonstationarity. In ARIMA, for example, the ARMA component is applied after the specified differences; the original level series can remain nonstationary. The transformations below have different purposes and should be assessed separately:

**Differencing**

- Differencing can remove a stochastic trend and stabilize the mean when the integration structure justifies it.
- It involves computing the difference between consecutive observations in the series.
- The first difference of a series $Y_t$ is defined as $\Delta Y_t = Y_t - Y_{t-1}$.
- Higher-order differencing can be applied if trends persist, such as the second difference $\Delta^2 Y_t = \Delta Y_t - \Delta Y_{t-1}$.
- Use the smallest differencing order that produces an adequately stationary series; unnecessary differencing can create additional dependence.

**Logarithmic Transformations**

- Logarithmic transformations stabilize variance when variability increases with the magnitude of the data.
- The natural logarithm (or another logarithm base) is applied to each data point in the series.
- For a series $Y_t$, the transformed series becomes $\log(Y_t)$.
- This method is particularly effective for data exhibiting exponential growth or multiplicative seasonality.
- It also compresses large values, which can make proportional changes easier to compare.

**Box-Cox Transformations**

The Box-Cox transform generalizes the log transform for positive series:

$$
Y_t^{(\lambda)} =
\begin{cases}
\frac{Y_t^{\lambda} - 1}{\lambda}, & \lambda \neq 0 \\
\log(Y_t), & \lambda = 0
\end{cases}
$$

Choosing $\lambda$ can stabilize variance and improve linearity before modeling.

**Detrending**

- Detrending removes long-term trends from data to highlight short-term fluctuations.
- A trend line is fitted to the data and then subtracted from the original series.
- For a linear trend $Y_t = \alpha + \beta t + \epsilon_t$, the detrended series is computed as $Y_t - (\alpha + \beta t)$.
- Non-linear trends can be removed by fitting polynomial or exponential functions.
- Detrending helps in isolating cyclical or seasonal patterns from broader trends.

## The Random Walk Model

A random walk is a classic difference-stationary process. Each value equals the previous value plus a new innovation, so shocks accumulate permanently in the level of the series.

### Definition

A random walk can be mathematically expressed as:

$$
X_t = X_{t-1} + Z_t
$$

where $Z_t$ is an uncorrelated innovation sequence with mean $\mu_Z$ (zero under the usual white-noise convention, nonzero when the increments include drift) and variance $\sigma_Z^2$. For a fixed starting value $X_0$, repeated substitution gives $X_t=X_0+\sum_{j=1}^t Z_j$.

### Properties of a Random Walk

**Mean.** With fixed $X_0$,

$$
E[X_t] = X_0 + t\mu_Z.
$$

For the common zero-drift random walk, $\mu_Z=0$, so the mean remains at $X_0$.

**Variance.** If the innovations are uncorrelated,

$$
\mathrm{Var}(X_t) = t\sigma_Z^2.
$$

Thus even a zero-drift random walk is non-stationary: its variance increases with time, and shocks have permanent effects on the level.

### Transforming a Random Walk into a Stationary Series

To apply a stationary model to the dynamics of a random walk, work with its **first differences**. This transformation reverses the accumulation of shocks exactly under the assumed model. Forecasts for changes can then be accumulated back to the level scale, with uncertainty propagated through that reconstruction.

#### Differencing Operator

For a random walk, the difference operator $\Delta$ removes the accumulated stochastic trend by recovering the innovation:

$$
\Delta X_t = X_t - X_{t-1} = Z_t.
$$

If $Z_t$ is stationary white noise, the differenced series $\Delta X_t$ is stationary.

The resulting series has the properties of the innovations:

- The differenced series has constant mean $\mu_Z$ (zero in the usual zero-drift example).
- The variance is constant over time.
- There is no autocorrelation in the differenced series if $Z_t$ is truly white noise.

Thus, first differencing a random walk recovers $Z_t$. If $Z_t$ is stationary white noise, the differenced series is stationary.

#### Example of Differencing

The following example simulates a zero-drift random walk and computes its first difference:

```python
import numpy as np
import matplotlib.pyplot as plt

# Simulate a random walk
np.random.seed(42)
N = 1000
Z = np.random.normal(0, 1, N)
X = np.cumsum(Z)  # Random walk as cumulative sum of white noise

# Apply differencing to make it stationary
diff_X = np.diff(X)

# Plot the original random walk and the differenced series
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(X, label='Random Walk')
plt.title('Random Walk (Non-Stationary)')
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(diff_X, label='Differenced Series')
plt.title('Differenced Series (Stationary)')
plt.grid(True)

plt.tight_layout()
plt.show()
```

**Simulating the random walk.**

- A random walk is generated by taking the cumulative sum of normally distributed random numbers. This produces a series where each value depends on the previous one plus some random noise.
- With a fixed initial value and zero-mean increments, this random walk has a constant expected level. It is nonstationary because its variance grows with time; the wandering appearance of one realized path is not evidence that its population mean changes.

**Differencing.**

- For this random walk, subtracting the previous observation from the current one recovers the simulated innovations. This removes the accumulated stochastic trend in the level series.
- The `np.diff()` call computes these consecutive differences directly.

The result plot would look like the following:

![A random-walk level and its stationary first differences](https://github.com/user-attachments/assets/2cebba56-7d3b-470c-9511-56d617be7159)

The upper panel shows the wandering random-walk level, while the lower panel shows the much more stable differenced series. The visual demonstrates why a difference-stationary process is modeled through its changes rather than by treating the original levels as stationary.

## Formal Tests for Stationarity

ADF and KPSS formalize different null hypotheses, so their p-values cannot be read with one common rule such as “small means stationary.” An ADF rejection is evidence against a unit-root specification; a KPSS rejection is evidence against the chosen level- or trend-stationarity specification. Their usefulness comes from comparing these targeted questions with the equation and deterministic terms appropriate to the series.

### Augmented Dickey–Fuller (ADF) Test

The ADF test evaluates a unit-root null using a regression of the form:

$$
\Delta X_t = \alpha + \beta t + \gamma X_{t-1} + \sum_{i=1}^{p} \delta_i \Delta X_{t-i} + \epsilon_t
$$

where $\Delta X_t = X_t - X_{t-1}$ and $p$ lagged differences absorb serial correlation. The hypotheses are:

- $H_0$: $\gamma=0$, corresponding to a unit root under the chosen deterministic specification.
- $H_1$: $\gamma<0$, corresponding to stationarity around the included deterministic terms.

In the ADF regression, $\gamma$ corresponds to the deviation of an AR coefficient from the unit-root value. Lagged differences absorb remaining short-run correlation, while an intercept or time trend changes the deterministic alternative. The null distribution is not the ordinary regression t distribution, so use unit-root critical values or the corresponding p-value calculation. A rejection applies to that specification rather than proving that every moment and every regime of the series is stationary.

### KPSS Test

The Kwiatkowski–Phillips–Schmidt–Shin (KPSS) test reverses the direction of evidence:

- $H_0$: the series is level-stationary or trend-stationary, depending on the test specification;
- $H_1$: the stationarity assumption is violated.

Using both tests helps organize the evidence:

| ADF result | KPSS result | Interpretation |
|---|---|---|
| Reject unit-root null | Fail to reject stationarity | Evidence supports stationarity |
| Fail to reject unit-root null | Reject stationarity | Evidence supports non-stationarity |
| Reject | Reject | Possible break, deterministic misspecification, or other model mismatch; inspect the series |
| Fail to reject | Fail to reject | Evidence is inconclusive; power may be limited |


## Choosing a stationary representation and interpreting test evidence

Stationarity is not a synonym for “the plot looks flat.” It describes which features of the joint distribution remain unchanged when the time index is shifted. The version needed depends on the model and question.

### Strict and weak stationarity

A process is strictly stationary if, for every collection of times and every shift $h$,

$$
(X_{t_1},\ldots,X_{t_k})
\overset{d}{=}
(X_{t_1+h},\ldots,X_{t_k+h}).
$$

Weak stationarity requires only:

$$
E(X_t)=\mu,
\qquad
\mathrm{Var}(X_t)=\gamma(0),
\qquad
\mathrm{Cov}(X_t,X_{t-h})=\gamma(h),
$$

with no dependence on $t$. Many ARMA calculations use weak stationarity. A jointly Gaussian process with a constant mean and covariance depending only on lag is also strictly stationary, because those moments determine every finite-dimensional Gaussian distribution. Weak stationarity does not generally imply strict stationarity for a non-Gaussian process.

### Numerical AR(1) example

Consider

$$
X_t=1+0.8X_{t-1}+\varepsilon_t,
\qquad
\mathrm{Var}(\varepsilon_t)=1.
$$

The stationary mean is

$$
\mu=\frac{1}{1-0.8}=5,
$$

and the stationary variance is

$$
\gamma(0)=\frac{1}{1-0.8^2}=2.7778.
$$

The lag-1 covariance is

$$
\gamma(1)=0.8\gamma(0)=2.2222,
$$

and the lag-1 correlation is $0.8$. The process can move substantially from one observation to the next while its distribution remains stable over time.

If $\phi=1$, the mean formula divides by zero and the variance does not settle. This is the unit-root boundary. If $|\phi|>1$, deviations grow and the process is explosive.

### Deterministic trend versus stochastic trend

For

$$
y_t=10+0.2t+\varepsilon_t,
$$

subtracting the deterministic trend can produce a stationary remainder. For a random walk,

$$
y_t=y_{t-1}+\varepsilon_t,
$$

the uncertainty accumulates permanently. Both can look like an upward trend in one realization, but their forecasts and variance behavior differ.

Use domain knowledge, differencing behavior, plots, and diagnostics together. A stationarity test can assess a statistical specification, but it cannot identify the scientific mechanism by itself.

### ADF and KPSS are complementary

The Augmented Dickey-Fuller test has a unit-root null. The KPSS test usually has a stationarity null. Their p-values are not interchangeable:

| ADF | KPSS | reading |
|---|---|---|
| reject unit root | fail to reject stationarity | evidence for stationarity |
| fail to reject unit root | reject stationarity | evidence against stationarity |
| both reject | possible trend stationarity, break, or misspecification | inspect plots and specifications |
| neither reject | low power or insufficient information | gather more evidence |

A trend omitted from the test regression can be mistaken for persistence. Too few lagged differences can leave serial correlation in the test errors; too many can reduce power. A break can make either null a poor approximation to the data. If ADF and KPSS disagree or both reject, inspect these specification choices and the time plot rather than forcing the result into a binary label.

### Transformations

Common transformations have different meanings:

- log or Box-Cox: stabilize a variance that grows with level;
- detrending: remove a specified deterministic mean structure;
- first difference: model changes from one period to the next;
- seasonal difference: compare observations one seasonal cycle apart;
- seasonal adjustment: remove a repeating component before modeling residual dynamics.

After transforming, inspect the transformed series. The goal is not to erase every pattern; it is to create a series whose remaining structure is appropriate for the proposed model.

### Local stationarity

Real data can be approximately stationary over a moving window and non-stationary globally. Examine rolling:

$$
\hat\mu_t=\frac1w\sum_{j=0}^{w-1}y_{t-j},
\qquad
\hat\sigma_t^2=\frac1{w-1}\sum_{j=0}^{w-1}(y_{t-j}-\hat\mu_t)^2.
$$

Rolling moments describe local behavior, not direct observations of the process mean and variance. Short windows are noisy; long windows average across changes. Overlapping windows share data, making adjacent estimates look smoothly related even under a stable process. Examine whether a change is sustained and meaningful relative to that sampling variation, then consider a local or time-varying model if one global specification is unsuitable.

### Stationarity workflow

1. Plot the level and relevant transforms.
2. Inspect rolling moments and missingness.
3. Check ACF behavior and seasonal lags.
4. State the deterministic terms used in any test.
5. Use ADF/KPSS or other tests as evidence, not as a single decision rule.
6. Fit a simple candidate after transformation.
7. Diagnose residuals and forecast behavior.
8. Reassess whether the transformation matches the deployment question.

## Formula reference

| Concept / case | General formula | Condition / interpretation |
|---|---|---|
| Strict stationarity | $(X_{t_1},\ldots,X_{t_k})\overset d=(X_{t_1+h},\ldots,X_{t_k+h})$ | Holds for every finite set of times and every common shift $h$. |
| Weak stationarity: mean | $E[X_t]=\mu$ | Constant over time. |
| Weak stationarity: variance | $\mathrm{Var}(X_t)=\gamma(0)<\infty$ | Constant finite variance. |
| Weak stationarity: covariance | $\mathrm{Cov}(X_t,X_{t-h})=\gamma(h)$ | Depends only on lag, not calendar time. |
| ACF | $\rho(h)=\gamma(h)/\gamma(0)$ | For a stationary process, $\rho(-h)=\rho(h)$. |
| White noise | $E\varepsilon_t=0$, $\mathrm{Var}(\varepsilon_t)=\sigma^2$, $\gamma(h)=0$ for $h\ne0$ | Basic stationary reference process. |
| MA($q$) covariance (with $\theta_0=1$) | $\gamma(h)=\sigma_\varepsilon^2\sum_{j=0}^{q-\lvert h\rvert}\theta_j\theta_{j+\lvert h\rvert}$ for $\lvert h\rvert\le q$ | Zero for $\lvert h\rvert>q$. |
| AR(1) | $X_t=c+\phi X_{t-1}+\varepsilon_t$ | Standard causal stationary solution requires $\lvert\phi\rvert<1$. |
| AR(1) mean | $\mu=c/(1-\phi)$ | Valid for the stationary solution. |
| AR(1) variance | $\gamma(0)=\sigma_\varepsilon^2/(1-\phi^2)$ | Finite only when $\lvert\phi\rvert<1$. |
| AR(1) ACF | $\rho(h)=\phi^{\lvert h\rvert}$ | Geometric or alternating decay. |
| AR($p$) stationarity/causality | $\phi(z)=1-\phi_1z-\cdots-\phi_pz^p=0\Rightarrow \lvert z\rvert>1$ | Standard backshift-root condition. |
| Linear filter | $X_t=\sum_j\psi_jY_{t-j}$ | Absolute summability $\sum_j\lvert\psi_j\rvert<\infty$ is a strong stability condition. |
| Random walk | $X_t=X_{t-1}+\varepsilon_t$ | Unit-root boundary; $\mathrm{Var}(X_t\mid X_0)=t\sigma^2$. |
| First difference | $\Delta X_t=(1-B)X_t=X_t-X_{t-1}$ | Removes one unit-root factor; a random walk becomes white noise. |
| Seasonal difference | $\Delta_sX_t=(1-B^s)X_t=X_t-X_{t-s}$ | Removes one seasonal unit-root factor at period $s$. |
| ADF regression | $\Delta X_t=\alpha+\beta t+\gamma X_{t-1}+\sum_{i=1}^{p}\delta_i\Delta X_{t-i}+\varepsilon_t$ | Unit-root null: $H_0:\gamma=0$. |
| KPSS decomposition | $X_t=d_t+r_t+u_t$, $r_t=r_{t-1}+\eta_t$ | Stationarity null corresponds to zero random-walk variance, $\mathrm{Var}(\eta_t)=0$. |
| Box-Cox transform | $g_\lambda(x)=(x^\lambda-1)/\lambda$ for $\lambda\ne0$; $g_0(x)=\log x$ | Used mainly to stabilize level-dependent variance, not to remove a unit root by itself. |
