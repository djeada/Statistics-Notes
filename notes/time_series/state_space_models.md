# State-Space Models and the Kalman Filter

A noisy measurement need not equal the underlying quantity we want to track. Daily observations can jump because the true level changed, because measurement error changed, or both. A **state-space model** writes one equation for the hidden state and another for the observation, making those sources of variation explicit.

The state can contain a level, a slope, seasonal components, regression coefficients, or a compact representation of ARMA dynamics. It is not directly observed; it is inferred from measurements and from assumptions about how it evolves. That separation gives a common language for signal estimation, missing observations, and forecasting.

The Kalman filter repeatedly performs two operations. It **predicts** the next state from the previous estimate and the transition equation. It then **updates** that prediction with the new measurement, weighting the discrepancy by the relative uncertainties. Under the linear Gaussian assumptions, it computes the conditional state mean and covariance exactly. The covariance is as central as the mean: it determines how much a surprising observation should change the estimate.

## Worked calculation: one local-level Kalman update

Suppose the predicted level is $a_{t\mid t-1}=10$, its predicted variance is $P_{t\mid t-1}=1.25$, and the observation is $y_t=12$ with measurement variance $R=1$. The innovation is

$$
v_t=12-10=2,
\qquad
F_t=1.25+1=2.25.
$$

The Kalman gain is

$$
K_t=\frac{1.25}{2.25}=0.5556.
$$

The updated estimate and variance are

$$
a_{t\mid t}=10+0.5556(2)\approx11.1111,
\qquad
P_{t\mid t}=(1-0.5556)(1.25)\approx0.5556.
$$

The new observation is 2 above the prediction. A gain of $5/9$ uses about 56% of that discrepancy, so the level moves from 10 to about 11.11 rather than all the way to 12. The posterior variance falls from 1.25 to about 0.556 because the measurement adds information. This posterior variance concerns the hidden level, not a future noisy observation; observation forecasting must also account for measurement variance.

![Filtering a noisy local level](https://raw.githubusercontent.com/djeada/Statistics-Notes/main/assets/time_series/student/18_state_space_filter.png)

The figure shows the role of the latent state: the observed series is noisy, while the filter updates an estimate of the underlying level as each new observation arrives.

## State and observation equations

State-space models distinguish an unobserved **state** from noisy observations. They provide a common framework for latent trends, seasonal components, regression effects, missing observations, and other dynamic structures.

A linear Gaussian state-space model can be written as

$$
\alpha_t=T_t\alpha_{t-1}+R_t\eta_t,
$$

$$
y_t=Z_t\alpha_t+d_t+\varepsilon_t.
$$

The first equation describes how the latent state evolves. The second describes how that state produces the observation. The matrices can vary with time, although many familiar models use constant matrices. In the standard linear Gaussian specification, state and observation disturbances have mean zero, the stated covariance matrices, and no serial or mutual correlation, and they are independent of the initial state. The familiar Kalman formulas below use that disturbance specification.

## Local-Level Model

A simple state-space model is

$$
\mu_t=\mu_{t-1}+\eta_t,
\qquad
y_t=\mu_t+\varepsilon_t.
$$

The two disturbances have different roles. A state shock changes the latent level and influences later observations through that level. An observation shock changes the current measurement without necessarily changing the hidden state. Their variances, $Q$ and $R$, determine which explanation the filter favors when it sees a departure. A large isolated measurement need not imply a permanent level jump.

![Local-level filter](https://raw.githubusercontent.com/djeada/Statistics-Notes/main/assets/time_series/state_space_frequency/01_local_level_filter.png)

The local-level figure shows the observed series together with the filtered latent level. The filter follows sustained changes in the signal while avoiding a full reaction to every noisy observation.

## Kalman Filter

For the scalar local-level model, the prediction step is

$$
a_{t\mid t-1}=a_{t-1\mid t-1},
\qquad
P_{t\mid t-1}=P_{t-1\mid t-1}+Q,
$$

where $Q$ is the state-innovation variance.

The observation produces the innovation

$$
v_t=y_t-a_{t\mid t-1},
$$

with innovation variance

$$
F_t=P_{t\mid t-1}+R,
$$

where $R$ is the measurement-error variance in this scalar notation. The Kalman gain is

$$
K_t=\frac{P_{t\mid t-1}}{F_t},
$$

and the update is

$$
a_{t\mid t}=a_{t\mid t-1}+K_tv_t,
\qquad
P_{t\mid t}=(1-K_t)P_{t\mid t-1}.
$$

![Kalman gain](https://raw.githubusercontent.com/djeada/Statistics-Notes/main/assets/time_series/state_space_frequency/02_kalman_gain.png)

For a scalar level observation, $K_t=P_{t\mid t-1}/(P_{t\mid t-1}+R)$. If the prior level is precise relative to the measurement, the gain is small and the observation receives little weight. If the prior is uncertain, the gain is larger. The variance update also makes a run of informative measurements increase confidence, affecting how the filter responds to the next observation.

**Filtering** conditions on observations through the date being estimated. **Smoothing** conditions on a later endpoint as well, allowing future measurements to revise that earlier estimate. **Forecasting** conditions on the current available record and propagates the state beyond it. These operations can use the same fitted model while answering different questions, so a smooth historical state estimate is not interchangeable with the filtered state that would have existed in real time.

![Filtering and smoothing](https://raw.githubusercontent.com/djeada/Statistics-Notes/main/assets/time_series/state_space_frequency/04_filtering_vs_smoothing.png)

The figure shows why the distinction matters. The smoothed path can use future observations to revise a past state and will often appear cleaner than the real-time filtered path. Using it to evaluate a real-time procedure would leak future information.

A missing measurement removes the update, not the transition. Propagate the predicted state and covariance to the next date, then resume updating when a measurement arrives. This uses the model's uncertainty rather than filling in a value and treating it as observed. Many ARIMA and exponential-smoothing models have state-space representations, so the same machinery can support their likelihoods, missing-data treatment, and forecasts.

## Uncertainty weighting, missing measurements, and likelihood

The general notation extends the scalar calculation without changing its logic. A vector state can carry several hidden components, and the observation matrix selects or combines them into measured quantities. The covariance matrices describe uncertainty and dependence across components. When constructing a model, specify the dimensions and roles of these matrices before applying a filter formula; an observation-noise covariance and a state-disturbance loading are different objects even if a text uses similar symbols.

### General linear Gaussian form

Write

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

Here $R_t$ is a loading matrix for state disturbances, while $H_t$ is the observation-noise covariance. This general notation should not be confused with the scalar symbol $R$ used above for a measurement variance.

The state $\alpha_t$ can contain several quantities. For a local linear trend, for example,

$$
\alpha_t=
\begin{bmatrix}
\ell_t\\
b_t
\end{bmatrix}
$$

can store level and slope. A seasonal model can store a vector of seasonal states, and a dynamic regression can include time-varying coefficients or an ARMA error state.

### The scalar local-level update

For

$$
\mu_t=\mu_{t-1}+\eta_t,
\qquad
y_t=\mu_t+\varepsilon_t,
$$

suppose $a_{t\mid t-1}=10$, $P_{t\mid t-1}=1.25$, $y_t=12$, and $R=1$. Then

$$
v_t=y_t-a_{t\mid t-1}=2,
$$

$$
F_t=P_{t\mid t-1}+R=2.25,
$$

and

$$
K_t=\frac{1.25}{2.25}=0.5556.
$$

The state update is

$$
a_{t\mid t}=10+0.5556(2)\approx11.1111,
$$

while the posterior variance is

$$
P_{t\mid t}=(1-0.5556)(1.25)\approx0.5556.
$$

The innovation is the discrepancy between the actual measurement and the model's one-step observation prediction. It is the information that the new measurement contributes beyond the past. The gain converts that discrepancy into a state revision, while the covariance update records the remaining uncertainty after the measurement has been used. Updating the mean without updating its covariance would lose the information needed to weight the next observation.

### How the variance ratio changes the gain

For the scalar local-level update,

$$
K_t=\frac{P_{t\mid t-1}}{P_{t\mid t-1}+R}.
$$

A smaller $R$ makes a given measurement more credible relative to the prior state estimate. A larger $Q$ has a different effect: it increases uncertainty during the transition because the state may have moved. Both can produce a larger response to a new measurement, but they imply different sources of uncertainty. Estimate or justify their ratio from the model and data rather than selecting a smooth-looking state path alone.

For a prior level of 10 and an observation of 12:

| $P_{t\mid t-1}$ | $R$ | gain | updated level |
|---:|---:|---:|---:|
| 1.25 | 1 | 0.556 | 11.111 |
| 1.25 | 4 | 0.238 | 10.476 |
| 4 | 1 | 0.800 | 11.600 |

The update is therefore a variance-weighted compromise between the model prediction and the new measurement.

### Filtering, smoothing, and forecasting

Filtering targets

$$
p(\alpha_t\mid y_1,\ldots,y_t).
$$

It is a real-time estimate because it uses only information available through time $t$.

Smoothing targets

$$
p(\alpha_t\mid y_1,\ldots,y_T),
\qquad T>t.
$$

It uses later observations to revise a past state. This is useful for historical decomposition and signal extraction, but it is not available in real time.

Forecasting propagates the filtered state forward. In a time-varying system,

$$
a_{t+h\mid t}=T_{t+h}\cdots T_{t+1}a_{t\mid t}.
$$

Forecast uncertainty accumulates state disturbances and, for future observations, measurement uncertainty. A performance evaluation that uses smoothed states at past forecast origins has used future information unless that retrospective procedure is explicitly the target.

### Missing observations

If $y_t$ is missing, there is no measurement innovation to use, so the update is skipped:

$$
a_{t\mid t}=a_{t\mid t-1},
\qquad
P_{t\mid t}=P_{t\mid t-1}.
$$

The next transition still proceeds:

$$
a_{t+1\mid t}=T_{t+1}a_{t\mid t},
$$

$$
P_{t+1\mid t}=T_{t+1}P_{t\mid t}T_{t+1}^{\top}
+R_{t+1}Q_{t+1}R_{t+1}^{\top}.
$$

![Missing observations](https://raw.githubusercontent.com/djeada/Statistics-Notes/main/assets/time_series/state_space_frequency/03_missing_observations.png)

The figure shows the prediction-only step across a missing measurement. In this local-level model, the state variance increases by $Q$ at each unobserved step until a new measurement supplies an update. In a general state-space model, the covariance follows its transition equation and need not increase monotonically.

### Innovations and likelihood

Under Gaussian disturbances, the one-step innovation $v_t$ has variance $F_t$. In the scalar case, its log-likelihood contribution is

$$
\ell_t
=-\frac12\left[
\log(2\pi)+\log(F_t)+\frac{v_t^2}{F_t}
\right].
$$

The likelihood judges innovations relative to their predicted variances. The term $v_t^2/F_t$ penalizes a surprise in units of the uncertainty the model assigned, while $\log F_t$ prevents the model from escaping that penalty simply by making every variance enormous. Summing contributions provides a criterion for estimating transition, variance, and regression parameters, subject to a stated initial-state treatment.

Standardized innovations

$$
\tilde v_t=\frac{v_t}{\sqrt{F_t}}
$$

provide a scale-adjusted diagnostic. A raw innovation can legitimately be large when its predicted variance is large; the standardized value asks whether it is large relative to that prediction. Under a well-specified model, standardized innovations should have approximately unit variance and no remaining systematic serial structure. Examine their squares and tails as well as their ordinary ACF.

### Relation to familiar models

Many familiar time-series models have state-space forms:

- a local level is closely related to simple exponential smoothing;
- a local level plus slope is related to Holt-style trend smoothing;
- ARIMA models can be represented with a finite-dimensional state;
- seasonal behavior can be encoded through seasonal states;
- missing observations can be handled without discarding the surrounding series.

Equivalent model labels do not guarantee numerically identical results. Initialization, parameter estimation, deterministic terms, and likelihood conventions can all affect fitted states and forecasts.

### Diagnostics and limitations

After fitting, inspect standardized innovations, their ACF, squared innovations, outliers, missingness patterns, parameter stability, and temporal forecast errors.

A visually smooth state estimate is partly a consequence of the chosen transition and noise assumptions. An abrupt genuine change may be spread over several dates if the model permits only gradual level movement; an outlying measurement can instead be mistaken for state movement if measurement noise is understated. Diagnose innovations and compare forecasts, and consider whether the state equation represents the type of change in the data.

The related frequency-domain material is covered in the [frequency-domain chapter](https://github.com/djeada/Statistics-Notes/blob/main/notes/time_series/frequency_domain_analysis.md), and the [state-space/frequency notebook](https://github.com/djeada/Statistics-Notes/blob/main/notebooks/time_series/state_space_and_frequency.ipynb) provides an additional worked environment.

## Formula reference

| Step / model | General formula | Notes / special case |
|---|---|---|
| State equation | $\alpha_t=T_t\alpha_{t-1}+R_t\eta_t$ | $\eta_t\sim N(0,Q_t)$ in the linear Gaussian model. |
| Observation equation | $y_t=Z_t\alpha_t+d_t+\varepsilon_t$ | $\varepsilon_t\sim N(0,H_t)$. |
| State prediction | $a_{t\mid t-1}=T_ta_{t-1\mid t-1}$ | Add deterministic state terms if the model contains them. |
| Prediction covariance | $P_{t\mid t-1}=T_tP_{t-1\mid t-1}T_t^\top+R_tQ_tR_t^\top$ | Propagates previous uncertainty plus state noise. |
| Innovation | $v_t=y_t-Z_ta_{t\mid t-1}-d_t$ | One-step forecast error. |
| Innovation covariance | $F_t=Z_tP_{t\mid t-1}Z_t^\top+H_t$ | Uncertainty of the one-step observation forecast. |
| Kalman gain | $K_t=P_{t\mid t-1}Z_t^\top F_t^{-1}$ | Determines the weight placed on the new observation. |
| State update | $a_{t\mid t}=a_{t\mid t-1}+K_tv_t$ | Filtering step. |
| Covariance update | $P_{t\mid t}=P_{t\mid t-1}-K_tF_tK_t^\top$ | Equivalent stable forms are also used numerically. |
| Local-level model | $\mu_t=\mu_{t-1}+\eta_t$, $y_t=\mu_t+\varepsilon_t$ | Scalar special case with latent random-walk level. |
| $h$-step state forecast | $a_{t+h\mid t}=T_{t+h}\cdots T_{t+1}a_{t\mid t}$ | For constant $T$, this is $T^ha_{t\mid t}$. |
| Gaussian log-likelihood contribution | $\ell_t=-\tfrac12[m_t\log(2\pi)+\log\lvert F_t\rvert+v_t^\top F_t^{-1}v_t]$ | $m_t$ is the number of observed components; $m_t=1$ in the scalar examples. |
| Standardized innovation | $\tilde v_t=F_t^{-1/2}v_t$ | Should resemble white noise under an adequate model. |
