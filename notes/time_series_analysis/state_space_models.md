# State-Space Models and the Kalman Filter

State-space models distinguish an unobserved **state** from noisy observations. This makes them a flexible language for trends, seasonality, regression effects, missing observations, and time-varying latent processes.

## General Form

A linear Gaussian state-space model can be written as

$$
\alpha_t = T_t\alpha_{t-1} + R_t\eta_t,
$$

$$
y_t = Z_t\alpha_t + d_t + \varepsilon_t,
$$

where $\alpha_t$ is the latent state, $y_t$ is observed, and the disturbances are usually modeled as Gaussian with known covariance structure up to estimated parameters.

The first equation is the **state/transition equation**. The second is the **observation/measurement equation**.

## Local-Level Model

A simple example is

$$
\mu_t = \mu_{t-1}+\eta_t,
$$

$$
y_t = \mu_t+\varepsilon_t.
$$

The latent level $\mu_t$ can drift through time while observations contain measurement noise.

## Kalman Filter

The Kalman filter recursively computes the distribution of the current state given observations available up to time $t$.

For a scalar local-level model, the prediction step is

$$
a_{t|t-1}=a_{t-1|t-1},
\qquad
P_{t|t-1}=P_{t-1|t-1}+Q.
$$

The innovation is

$$
v_t=y_t-a_{t|t-1},
$$

with innovation variance

$$
F_t=P_{t|t-1}+R.
$$

The Kalman gain is

$$
K_t=\frac{P_{t|t-1}}{F_t},
$$

and the update is

$$
a_{t|t}=a_{t|t-1}+K_tv_t,
\qquad
P_{t|t}=(1-K_t)P_{t|t-1}.
$$

The filter balances model uncertainty against measurement uncertainty.

## Filtering vs Smoothing vs Forecasting

- **Filtering** estimates the state at time $t$ using data through $t$.
- **Prediction/forecasting** estimates future states or observations using data through the current time.
- **Smoothing** estimates historical states using the full sample, including observations that occurred later.

Smoothing is therefore useful for retrospective signal extraction but must not be confused with real-time forecasting.

## Missing Observations

State-space methods handle missing observations naturally: when $y_t$ is unavailable, the state can be propagated with the transition equation without a measurement update.

## Relationship to Familiar Models

Many ARIMA and exponential-smoothing models admit state-space representations. State-space form provides a common computational framework for likelihood evaluation, filtering, smoothing, and forecasting.

## Parameter Estimation

The Kalman filter supplies one-step-ahead innovations and their variances. These quantities can be used to evaluate the likelihood and estimate unknown noise variances or structural parameters numerically.

## Diagnostics

After fitting, inspect standardized innovations for remaining autocorrelation, changing variance, outliers, and distributional problems. A state-space representation does not remove the need for residual diagnostics or backtesting.

See `scripts/time_series_analysis/kalman_filter.py` for a minimal scalar implementation of the local-level filter.
