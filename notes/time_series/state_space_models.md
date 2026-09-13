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

## Student guide: prediction, update, and uncertainty

State-space notation separates what is observed from the process that is being inferred. This is especially useful when the signal is noisy, observations are missing, or the dynamic behavior is easier to express through a latent level, slope, or seasonal state.

### General linear Gaussian form

Write the transition and measurement equations as

$$
\alpha_t=T_t\alpha_{t-1}+R_t\eta_t,
\qquad
y_t=Z_t\alpha_t+d_t+\varepsilon_t,
$$

with

$$
\eta_t\sim N(0,Q_t),
\qquad
\varepsilon_t\sim N(0,H_t).
$$

The state $\alpha_t$ can contain several quantities. For a local linear trend it may contain level and slope:

$$
\alpha_t=
\begin{bmatrix}
\ell_t\\
b_t
\end{bmatrix}.
$$

For a seasonal model it may contain a set of seasonal states. For a dynamic regression it may contain coefficients or an ARMA error state.

### The scalar local-level update

The local-level model is

$$
\mu_t=\mu_{t-1}+\eta_t,
\qquad
y_t=\mu_t+\varepsilon_t.
$$

Suppose $a_{t|t-1}=10$, $P_{t|t-1}=1.25$, $y_t=12$, and $R=1$. Then:

$$
v_t=y_t-a_{t|t-1}=2,
$$

$$
F_t=P_{t|t-1}+R=2.25,
$$

$$
K_t=\frac{1.25}{2.25}=0.5556.
$$

The updated state is

$$
a_{t|t}=10+0.5556(2)=11.1112,
$$

and the updated variance is

$$
P_{t|t}=(1-0.5556)(1.25)\approx0.5555.
$$

The innovation is the new information in the observation after the prior prediction. The gain decides how much of it is used.

### How the variance ratio changes the gain

For a scalar local-level update,

$$
K_t=\frac{P_{t|t-1}}{P_{t|t-1}+R}.
$$

If $R$ is very small, the measurement is precise and $K_t$ approaches 1. If $R$ is large, the observation is noisy and $K_t$ approaches 0. If process variance $Q$ is large, the state prediction is uncertain and the filter also gives more weight to the new observation.

This is the same tradeoff as a weighted average. With prior level 10 and observation 12:

| $P_{t|t-1}$ | $R$ | gain | updated level |
|---:|---:|---:|---:|
| 1.25 | 1 | 0.556 | 11.111 |
| 1.25 | 4 | 0.238 | 10.476 |
| 4 | 1 | 0.800 | 11.600 |

The update is not a mysterious smoothing operation; it is a variance-weighted combination of a prior prediction and an observation.

### Filtering, smoothing, and forecasting

Filtering calculates

$$
p(\alpha_t\mid y_1,\ldots,y_t).
$$

It is a real-time estimate because it only uses data available through $t$.

Smoothing calculates

$$
p(\alpha_t\mid y_1,\ldots,y_T),
\qquad T>t.
$$

It uses later observations to revise the estimate of a past state. This is useful for historical decomposition, signal extraction, and retrospective reporting, but it is not a real-time forecast.

Forecasting propagates the filtered state:

$$
a_{t+h|t}=T_{t+h}\cdots T_{t+1}a_{t|t}.
$$

Prediction uncertainty accumulates transition noise and measurement uncertainty. A plot that uses a smoothed state to assess real-time performance has used future information unless the smoothing operation was part of the actual deployment procedure.

### Missing observations

If $y_t$ is missing, omit the measurement update:

$$
a_{t|t}=a_{t|t-1},
\qquad
P_{t|t}=P_{t|t-1}.
$$

The next transition still occurs:

$$
a_{t+1|t}=T_{t+1}a_{t|t},
\qquad
P_{t+1|t}=T_{t+1}P_{t|t}T_{t+1}^{\top}+R_{t+1}Q_{t+1}R_{t+1}^{\top}.
$$

As the gap grows, uncertainty generally increases. The filter does not invent observations; it carries forward the model's uncertainty.

### Innovations and likelihood

Under Gaussian disturbances, the one-step innovation $v_t$ has variance $F_t$. The contribution to the log-likelihood is

$$
\ell_t
=-\frac12\left[
\log(2\pi)+\log(F_t)+\frac{v_t^2}{F_t}
\right]
$$

in the scalar case. Summing over time gives a likelihood that can be optimized over unknown $Q$, $R$, transition coefficients, and regression parameters.

This gives a direct diagnostic: standardized innovations

$$
\tilde v_t=\frac{v_t}{\sqrt{F_t}}
$$

should have approximately constant variance and little serial dependence when the model is adequate.

### Relation to familiar models

Many models have equivalent state-space forms:

- a local level is related to simple exponential smoothing;
- a local level plus slope is related to Holt-style trend smoothing;
- ARIMA models can be written with a finite-dimensional state;
- seasonal components can be represented with seasonal states;
- missing data and irregular observations can be handled without deleting the whole series.

Equivalent forecasts can still differ in initialization, parameter estimation, or treatment of deterministic terms. Compare equations and likelihood conventions rather than relying on model labels.

### Diagnostics and limitations

After fitting, inspect:

1. standardized innovations over time;
2. innovation ACF;
3. squared innovation ACF;
4. outliers and missingness;
5. parameter stability;
6. forecast errors on temporal backtests.

A Gaussian state-space model can produce smooth-looking states even when the noise distribution is heavy-tailed or the system has a break. Smoothing a misspecified model does not repair its assumptions.

### Visual companions

Run [state_space_frequency_visualizations.py](../../scripts/time_series/state_space_frequency_visualizations.py):

![Local-level filter](../../assets/time_series/state_space_frequency/01_local_level_filter.png)

![Kalman gain](../../assets/time_series/state_space_frequency/02_kalman_gain.png)

![Missing observations](../../assets/time_series/state_space_frequency/03_missing_observations.png)

![Filtering and smoothing](../../assets/time_series/state_space_frequency/04_filtering_vs_smoothing.png)

The frequency-domain companions are in the [frequency-domain chapter](frequency_domain_analysis.md).

See [`kalman_filter.py`](../../scripts/time_series/kalman_filter.py) and the [state-space/frequency notebook](../../notebooks/time_series/state_space_and_frequency.ipynb).
