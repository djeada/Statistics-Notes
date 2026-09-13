# Stochastic Processes and White Noise

A time series is one observed path from an underlying **stochastic process**: a family of random variables indexed by time,

$$
\{X_t : t \in T\}.
$$

Thinking in terms of a stochastic process separates the observed data from the probabilistic mechanism used to model it.

## Random Variables, Realizations, and Sample Paths

For a fixed time $t$, $X_t$ is a random variable. After observation, its realized value is written $x_t$. A sequence such as

$$
x_1, x_2, \ldots, x_n
$$

is one **sample path** or realization of the process. Statistical modeling uses this path to learn about dependence, uncertainty, and the distribution of future values.

## Innovations

Many time-series models are written as a predictable component plus a new shock:

$$
X_t = m_t + \varepsilon_t.
$$

The term $m_t$ summarizes information available before time $t$, while $\varepsilon_t$ is the new information arriving at time $t$. In ARMA-type models these shocks are often called **innovations**.

## White Noise

A weak white-noise process $\{\varepsilon_t\}$ satisfies

$$
E[\varepsilon_t] = 0,
\qquad
\operatorname{Var}(\varepsilon_t)=\sigma^2,
\qquad
\operatorname{Cov}(\varepsilon_t,\varepsilon_{t-h})=0 \quad (h\ne 0).
$$

This means the process has zero mean, constant variance, and no linear serial correlation.

White noise is not automatically the same as independent noise. Uncorrelated random variables can still be dependent. **Independent white noise** adds independence across time. **Gaussian white noise** is usually taken to mean independent normal innovations with constant variance.

## Why White Noise Matters

A fitted time-series model should explain the systematic temporal structure in the data. Its residuals should therefore resemble white noise. If the residual ACF contains important structure or a Ljung-Box test rejects the absence of serial correlation, the model has left predictable information unused.

White-noise residuals do not prove that a model is correct. They only indicate that a particular kind of serial dependence is no longer obvious. Residual variance changes, non-Gaussian tails, structural breaks, or nonlinear dependence can still remain.

## White Noise vs Random Walk

White noise is stationary:

$$
\varepsilon_t \sim WN(0,\sigma^2).
$$

A random walk accumulates white-noise shocks:

$$
X_t = X_{t-1} + \varepsilon_t.
$$

Therefore

$$
X_t = X_0 + \sum_{j=1}^{t}\varepsilon_j,
$$

and its variance grows with time. The random walk is not weakly stationary even though its increments are white noise.

## Martingale Differences

A useful stronger forecasting concept is a **martingale difference sequence**. If $\mathcal{F}_{t-1}$ represents information available before time $t$, then

$$
E[\varepsilon_t \mid \mathcal{F}_{t-1}] = 0
$$

means that the next innovation has zero conditional mean given the past. This rules out predictable conditional-mean structure, while weak white noise only rules out linear autocorrelation.

## Simulation

A Gaussian white-noise sample can be generated with NumPy:

```python
import numpy as np

rng = np.random.default_rng(42)
epsilon = rng.normal(loc=0.0, scale=1.0, size=500)
```

The companion script `scripts/time_series_analysis/white_noise.py` demonstrates white-noise behavior. After this note, continue with [stationarity](stationarity.md), [autocovariance](autocovariance_function.md), and [autocorrelation](autocorrelation_function.md).
