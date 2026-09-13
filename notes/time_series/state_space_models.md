# State-Space Models and the Kalman Filter

State-space models distinguish an unobserved **state** from noisy observations. They provide a flexible language for trends, seasonality, regression effects, missing observations, and time-varying latent processes.

A linear Gaussian state-space model can be written as

$$
\alpha_t=T_t\alpha_{t-1}+R_t\eta_t,
$$

$$
y_t=Z_t\alpha_t+d_t+\varepsilon_t.
$$

The first is the state/transition equation; the second is the observation/measurement equation.

## Local-Level Model

A simple example is

$$
\mu_t=\mu_{t-1}+\eta_t,
\qquad
y_t=\mu_t+\varepsilon_t.
$$

The latent level can drift while observations contain measurement noise.

## Kalman Filter

For the scalar local-level model, prediction gives

$$
a_{t|t-1}=a_{t-1|t-1},
\qquad
P_{t|t-1}=P_{t-1|t-1}+Q.
$$

With innovation $v_t=y_t-a_{t|t-1}$ and variance $F_t=P_{t|t-1}+R$, the Kalman gain is

$$
K_t=\frac{P_{t|t-1}}{F_t},
$$

and the update is

$$
a_{t|t}=a_{t|t-1}+K_tv_t,
\qquad
P_{t|t}=(1-K_t)P_{t|t-1}.
$$

**Filtering** estimates the current state using data through the current time. **Forecasting** predicts future states or observations. **Smoothing** estimates historical states using the full sample, including later observations, so it must not be confused with real-time forecasting.

When an observation is missing, the state can be propagated without a measurement update. Many ARIMA and exponential-smoothing models admit state-space representations, giving a common framework for likelihood, filtering, smoothing, and forecasting.

See [`kalman_filter.py`](../../scripts/time_series/kalman_filter.py) and the [state-space/frequency notebook](../../notebooks/time_series/state_space_and_frequency.ipynb).
