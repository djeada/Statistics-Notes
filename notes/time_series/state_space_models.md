# State-Space Models and the Kalman Filter

## Worked calculation: one local-level Kalman update

Suppose the predicted level is $a_{t|t-1}=10$, its predicted variance is $P_{t|t-1}=1.25$, and the observation is $y_t=12$ with measurement variance $R=1$. The innovation is

$$
v_t=12-10=2,
\qquad
F_t=1.25+1=2.25.
$$

The Kalman gain is

$$
K_t=\frac{1.25}{2.25}=0.5556.
$$

The updated estimate and variance are therefore

$$
a_{t|t}=10+0.5556(2)=11.1112,
\qquad
P_{t|t}=(1-0.5556)(1.25)\approx0.5555.
$$

The update moves partway toward the observation because both the prior state and the measurement are noisy. A larger measurement variance would make the gain smaller and the filter trust the prior more.

![Filtering a noisy local level](../../assets/time_series/student/18_state_space_filter.png)

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
