# Random Walk Model

A random walk says that the current level is the previous level plus a new increment. If today's shock raises the level by 2, tomorrow starts from that raised level. There is no mean-reverting term that gradually pulls the effect back toward a fixed baseline. Each shock therefore appears once in the changes and remains in all subsequent levels.

This mechanism can create long apparent rises and falls even when the expected increment is zero. A visually persistent slope in one realization is not the same as a deterministic trend in the process mean. The cumulative equation and its variance make that distinction precise.

The model is useful in two ways. It is a simple description of a stochastic trend, and it supplies the naive forecast against which more complicated methods can be compared. Its level is nonstationary because uncertainty accumulates over time. Its first differences can nevertheless be stationary, because differencing reverses the cumulative construction and recovers the increments.

## Worked calculation: one path and one forecast

Let $X_0=5$ and let the first three shocks be $1,-2,$ and $0.5$. Then

$$
X_1=6,\qquad X_2=4,\qquad X_3=4.5.
$$

If the shocks are independent with variance $\sigma^2=1$, then

$$
\mathrm{Var}(X_3\mid X_0)=3.
$$

For a zero-drift random walk, the conditional-mean forecast from time 3 is

$$
E(X_{3+h}\mid X_3)=X_3=4.5
$$

for every horizon $h$. The point forecast stays flat, but its uncertainty grows:

$$
\mathrm{Var}(X_{3+h}\mid X_3)=h\sigma^2.
$$

![A simulated random walk](https://raw.githubusercontent.com/djeada/Statistics-Notes/main/assets/time_series/intro_random_walk.png)

The plotted path can wander for long periods in one direction even though the model has no deterministic slope. That distinction between a realized path and the process mean is central to understanding random walks.

## Model definition and assumptions

The defining feature is the coefficient 1 on the previous level. A stationary AR(1) multiplies an earlier shock by successive powers of a coefficient with magnitude below 1, so its effect decays. Here the successive weights are all 1. The following equation therefore describes permanent shock effects, even though the new increment itself can be unpredictable and short-lived.

For the zero-drift form,

$$
X_t=X_{t-1}+\varepsilon_t,
$$

where $\varepsilon_t$ has mean zero and variance $\sigma^2$. The moment calculations use uncorrelated increments. The conditional-mean forecasts below use the stronger assumption that each new increment has mean zero given the observed past; independent mean-zero increments satisfy that assumption. Weak white noise alone does not rule out every nonlinear predictable pattern.

- $X_t$ is the level at time $t$.
- $X_{t-1}$ is the previous level.
- $\varepsilon_t$ is the new innovation arriving at time $t$.

Under the conditional-mean assumption, the best squared-error forecast of the next increment is zero. That does not make the next level unpredictable in the same sense: it is centered on the latest observed level. Most of the level's information comes from its accumulated history; only the new increment remains unknown. This is why a flat naive forecast can be appropriate for a highly variable path.

## Evolution of a Random Walk Over Time

Starting from $X_0$, repeated substitution gives

$$
X_1=X_0+\varepsilon_1,
$$

$$
X_2=X_0+\varepsilon_1+\varepsilon_2,
$$

$$
X_3=X_0+\varepsilon_1+\varepsilon_2+\varepsilon_3,
$$

and, in general,

$$
X_t=X_0+\sum_{i=1}^{t}\varepsilon_i.
$$

The same shock remains in the formulas for $X_t$, $X_{t+1}$, and every later level. Comparing two paths that receive identical later shocks but differ by one shock today would leave a permanent gap between them. Comparing levels at nearby dates instead reveals substantial overlap in their accumulated shock histories, which explains their strong dependence.

## Mean and Variance of a Random Walk

The moments of the level follow directly from the cumulative sum. Assume $X_0$ is fixed and the innovations are independent with mean zero and variance $\sigma^2$.

### Expected Value

Then

$$
E(X_t)=X_0.
$$

Across repeated realizations starting at the same $X_0$, positive and negative mean-zero increments cancel in expectation. The average level therefore stays at $X_0$. Individual paths need not return there, and their spread around it increases. A constant mean is only one part of weak stationarity; the growing variance is enough to rule stationarity out.

If the increments instead have nonzero mean $\delta$, it is clearer to write that mean explicitly as drift, as in the next section.

### Variance

Because the innovations are independent,

$$
\mathrm{Var}(X_t\mid X_0)
=\mathrm{Var}\left(\sum_{i=1}^{t}\varepsilon_i\right)
=t\sigma^2.
$$

The variance therefore grows linearly with time. This time-varying variance is enough to violate weak stationarity, even though the zero-drift mean remains constant.

## Random Walk with Drift

A **random walk with drift** is

$$
X_t=\delta+X_{t-1}+\varepsilon_t,
$$

with $E(\varepsilon_t)=0$. Expanding from $X_0$ gives

$$
X_t=X_0+\delta t+\sum_{i=1}^{t}\varepsilon_i.
$$

Thus,

| Property | Random Walk ($\delta=0$) | Random Walk with Drift ($\delta\ne0$) |
|---|---|---|
| $E(X_t)$ | $X_0$ | $X_0+\delta t$ |
| $\mathrm{Var}(X_t\mid X_0)$ | $\sigma^2t$ | $\sigma^2t$ |
| Mean path | flat | linear with slope $\delta$ |

Drift changes the center of the possible paths from $X_0$ to $X_0+\delta t$. It does not alter the independent-shock variance $t\sigma^2$ when $\delta$ is fixed. Subtracting a known drift line therefore removes a deterministic mean but leaves the random-walk accumulation. The detrended level still has growing variance and must not be treated as a stationary error process.

## Simulation of a Random Walk in Python

A simulation makes the cumulative structure visible. The following code draws independent standard-normal shocks and forms their cumulative sum.

```python
import numpy as np
import matplotlib.pyplot as plt

N = 1000
Z = np.random.normal(loc=0, scale=1, size=N)
X = np.cumsum(np.insert(Z, 0, 0))

plt.figure(figsize=(10, 6))
plt.plot(X, label="Random Walk")
plt.title("Simulation of a Random Walk")
plt.xlabel("Time")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.show()
```

The simulation separates the two objects explicitly: `Z` stores the increments, while `X` stores the level after those increments have accumulated. Repeating the simulation changes the apparent path, not the mechanism. To study the variance statement experimentally, compare values at the same time index across many simulated paths; a rolling variance along one path is a different calculation.

Here is an example realization:

![One simulated random-walk path](https://github.com/user-attachments/assets/0328869d-6a94-4f9b-b623-09e9d3e42311)

The opening synthetic figure shows the same qualitative behavior: local runs and apparent slopes can emerge purely from accumulated noise.

## Autocorrelation of the Random Walk

Because a random walk is non-stationary, it does not have the stationary population ACF used for ARMA processes. A **sample ACF** can still be plotted, and it typically shows large, slowly decaying values because nearby levels share most of the same accumulated shocks.

```python
from statsmodels.graphics.tsaplots import plot_acf

plot_acf(X, lags=50)
plt.show()
```

An example sample ACF is shown below:

![Slowly decaying sample ACF of random-walk levels](https://github.com/user-attachments/assets/82260af5-9278-4e44-b527-554a5ef12aa5)

The large sample autocorrelations arise because successive levels share nearly all their earlier increments. This is not a population stationary ACF whose value depends only on lag. For a fixed start, the level covariance is proportional to the smaller of the two time indices, so both dates matter. A familiar-looking correlogram does not justify applying stationary ARMA identification rules to the level.

## Removing the Trend with the Difference Operator

The random walk has a **stochastic trend**: shocks accumulate permanently rather than decaying. Even with zero drift, its variance changes with time. First differencing removes this accumulation:

$$
\Delta X_t=X_t-X_{t-1}=\varepsilon_t.
$$

For the model assumed here, the differenced series is white noise. The transformation therefore changes the modeling target from the non-stationary level to stationary one-period changes.

## Differencing in Python

The same operation can be computed directly:

```python
diff_X = np.diff(X)

plt.figure(figsize=(10, 6))
plt.plot(diff_X, label="Differenced Random Walk")
plt.title("Differenced Time Series (White Noise)")
plt.xlabel("Time")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.show()

plot_acf(diff_X, lags=50)
plt.show()
```

`np.diff()` subtracts each observation from the next. Because the simulation explicitly prepends the starting value 0, `np.diff(X)` recovers all `N` generated increments in `Z`, with no increment lost at the boundary. The differenced series should fluctuate around zero with roughly constant variance, while its sample ACF should show no persistent serial correlation beyond ordinary sampling noise.

The corresponding plots are:

![First differences of the simulated random walk](https://github.com/user-attachments/assets/91b7c7e2-9354-42ff-a6da-0312e4bb258b)

![Sample ACF of the recovered random-walk increments](https://github.com/user-attachments/assets/d3b952e4-27aa-4edf-a6f9-955fcc54fee3)

The first figure shows the stationary-looking increments; the second shows that their sample autocorrelations are concentrated around zero rather than decaying slowly from a large positive value.

## Correlogram of a Random Walk

The contrast between the level and differenced correlograms summarizes the model. In levels, adjacent observations share almost the entire accumulated history, so sample autocorrelations are often high and decay slowly. After differencing, only the new innovations remain, and the persistent correlation pattern disappears under the white-noise assumption.

First differencing is justified here by the model equation: subtracting the previous level cancels every earlier shock and leaves exactly the new increment. That is a stronger argument than flattening a plot. If a different mechanism produced the apparent trend, the same difference could alter useful signal or introduce unnecessary dependence. Establish which mechanism the transformation is meant to reverse.

## Reading a path and forecasting beyond its endpoint

The random walk is the canonical example of a non-stationary level with stationary increments:

$$
X_t=X_{t-1}+\varepsilon_t.
$$

Repeated substitution gives

$$
X_t=X_0+\varepsilon_1+\cdots+\varepsilon_t.
$$

Each shock has a permanent effect on the level because it remains inside every later cumulative sum.

### Numerical path

Let $X_0=5$ and shocks $(1,-2,0.5,1.5)$. Then

$$
X_1=6,\quad X_2=4,\quad X_3=4.5,\quad X_4=6.
$$

The first differences recover the shocks:

$$
\Delta X_t=X_t-X_{t-1}.
$$

If the shocks have variance $\sigma^2=1$, then

$$
\mathrm{Var}(X_4\mid X_0)=4.
$$

The four observed increments sum to 1, leaving a final level of 6. Their realized average is positive, but the example was generated under a zero-mean increment model. Estimating a long-run drift from such a short path would mistake a noisy sample average for strong evidence about a persistent mean change. More observations help, but breaks and changing regimes can still make a constant drift inappropriate.

### Forecasts

For a zero-drift random walk,

$$
\hat X_{T+h\mid T}=X_T.
$$

For the numerical path above at $T=4$, every point forecast equals 6. The forecast-error variance is

$$
\mathrm{Var}(X_{T+h}-\hat X_{T+h\mid T}\mid X_T)=h\sigma^2.
$$

If a drift $\delta$ is included,

$$
X_t=\delta+X_{t-1}+\varepsilon_t,
$$

then

$$
\hat X_{T+h\mid T}=X_T+h\delta.
$$

The displayed forecast treats the drift as fixed and known. If the drift is estimated, uncertainty about that estimate contributes additional forecast uncertainty beyond the future-shock variance $h\sigma^2$. A structural break or a temporary slope can also make a single drift estimate unreliable across the whole record, so inspect its stability when evaluating longer-horizon forecasts.

### Why levels are misleading

A levels regression can confuse shared persistence with a meaningful relationship. Two independent random walks may both spend long stretches above their starting levels, creating a large fitted association even though their new shocks are independent. Check whether a proposed relationship concerns one-period changes, a stationary deviation from a deterministic trend, or a cointegrating combination of levels; these imply different model specifications.

Differencing removes the unit-root accumulation:

$$
\nabla X_t=(1-B)X_t=\varepsilon_t.
$$

The differenced series is the innovation sequence itself. This does not mean every trending-looking series should be differenced automatically: deterministic trends, structural breaks, seasonal patterns, and cointegrated systems require different treatment.

### Extensions

- A **random walk with drift** adds a deterministic increment to each step.
- A **local level model** allows an unobserved level to evolve while observations include measurement noise.
- A **fractionally integrated process** can exhibit persistence between short-memory stationarity and a unit root.
- A **cointegrated system** can contain non-stationary component series whose particular linear combination is stationary.

### Diagnostics

Inspect the level plot, first differences, rolling variation, and sample ACF before and after differencing. Unit-root tests can provide supporting evidence, but their conclusions depend on deterministic terms, lag choices, sample length, and structural breaks. Report the transformation and model assumption rather than only a p-value.

## Formula reference

| Quantity / variant | General formula | Interpretation / special case |
|---|---|---|
| Random walk | $X_t=X_{t-1}+\varepsilon_t$ | Equivalent to ARIMA$(0,1,0)$. |
| Cumulative form | $X_t=X_0+\sum_{j=1}^{t}\varepsilon_j$ | Every shock has a permanent effect on the level. |
| First difference | $\Delta X_t=(1-B)X_t=\varepsilon_t$ | The increments are stationary white noise in the basic model. |
| Mean, no drift | $E[X_t\mid X_0]=X_0$ | Individual paths still wander. |
| Variance, no drift | $\mathrm{Var}(X_t\mid X_0)=t\sigma^2$ | Increasing variance makes the level nonstationary. |
| Covariance | $\mathrm{Cov}(X_s,X_t\mid X_0)=\min(s,t)\sigma^2$ | For independent increments. |
| Random walk with drift | $X_t=\delta+X_{t-1}+\varepsilon_t$ | ARIMA$(0,1,0)$ with drift under the usual parameterization. |
| Drift cumulative form | $X_t=X_0+\delta t+\sum_{j=1}^{t}\varepsilon_j$ | $E[X_t\mid X_0]=X_0+\delta t$. |
| $h$-step forecast | $\hat X_{T+h\mid T}=X_T+h\delta$ | Set $\delta=0$ for the zero-drift random walk. |
| Forecast-error variance | $\mathrm{Var}(X_{T+h}-\hat X_{T+h\mid T}\mid\mathcal F_T)=h\sigma^2$ | Forecast uncertainty grows linearly in horizon. |
| Gaussian forecast interval | $\hat X_{T+h\mid T}\pm z_{1-\alpha/2}\sigma\sqrt h$ | Requires Gaussian or approximate Gaussian innovations. |
| Geometric random walk | $P_t=P_{t-1}e^{\mu+\varepsilon_t}$ | In logs: $\log P_t=\log P_{t-1}+\mu+\varepsilon_t$. |
