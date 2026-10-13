# State Space

Read [state-space models](../../notes/time_series/state_space_models.md).

1. In the local-level model, use $a_{t|t-1}=10$, $P_{t|t-1}=1.25$, $y_t=12$, and $R=1$ to calculate the innovation, innovation variance, Kalman gain, updated level, and updated variance.
2. Repeat question 1 with $R=4$. Which direction does the Kalman gain move and why?
3. Explain the difference between filtering, smoothing, and forecasting. Which one is valid for a real-time estimate at time $t$?
4. Remove one observation from a simulated series. Show how the state prediction proceeds without a measurement update.
5. Simulate a local-level process and compare raw-observation RMSE with filtered-state RMSE.
6. Explain how the innovation sequence contributes to a Gaussian state-space likelihood.
7. Give one example where a state-space model is preferable to a simple regression with time as a predictor.

## Checks

- The innovation is 2, its variance is 2.25, and the gain is $1.25/2.25=0.5556$.
- The updated level is approximately $11.1111$ and the updated variance is approximately $0.5556$.
- Increasing measurement variance makes the filter trust the prior state more, so the gain decreases.

## Applied practice

8. Run [state_space_frequency_visualizations.py](../../scripts/time_series/state_space_frequency_visualizations.py) and identify the difference between filtering and smoothing in the plotted data.
9. Repeat the scalar update for $(P,R)=(1.25,0.1)$, $(1.25,1)$, and $(1.25,4)$. Plot the gain against $R$.
10. Introduce a block of missing observations. Compare filtered variance before, during, and after the gap.
11. Estimate $Q$ and $R$ on simulated local-level data by a grid search. Plot the innovation sum of squares over the grid.
12. Compare a local-level model with a regression on time when the latent level changes randomly. Explain which uncertainty each model represents.
13. Calculate standardized innovations and inspect their ACF and squared ACF.
14. Explain why a smoothed historical state cannot be used as a real-time feature without recreating the full-sample future information.

## Reflection

State the transition equation, measurement equation, disturbance assumptions, initialization, missing-data rule, and forecast target for your state-space model.

## Extension tasks

15. Derive the local-level update from minimizing a variance-weighted quadratic loss.
16. Compare filtered and smoothed estimates around an abrupt level change.
17. Calculate the innovation log-likelihood contribution for $v_t=2$ and $F_t=2.25$.
18. Simulate two processes with the same observations but different $(Q,R)$ ratios. Compare gains and filtered paths.
19. Explain how a local trend state differs from a regression on time.
20. Create a missing block at the beginning, middle, and end of a series. Compare uncertainty behavior.

## Worked solutions

**1.** Innovation: $v_t=y_t-a_{t|t-1}=12-10=2$. Innovation variance: $F_t=P_{t|t-1}+R=1.25+1=2.25$. Gain: $K_t=1.25/2.25=0.5556$. Updated level: $a_{t|t}=10+0.5556(2)=11.1111$. Updated variance: $P_{t|t}=(1-0.5556)(1.25)=0.5556$ (equivalently $PR/(P+R)=1.25/2.25$).

**2.** With $R=4$: $F_t=5.25$, $K_t=1.25/5.25=0.2381$, $a_{t|t}=10+0.2381(2)=10.4762$, $P_{t|t}=(1-0.2381)(1.25)=0.9524$. The gain falls because the measurement is noisier, so the filter relies more on the prediction, and the posterior variance stays larger.

**3.** Filtering estimates $\alpha_t$ from $y_1,\ldots,y_t$; forecasting estimates $\alpha_{t+h}$ or $y_{t+h}$ from $y_1,\ldots,y_t$ by propagating the filtered state; smoothing estimates $\alpha_t$ from the whole sample $y_1,\ldots,y_T$. Filtering (and forecasting) is valid in real time; smoothing uses the future.

**4.** At a missing $t$ there is no $v_t$, so $a_{t|t}=a_{t|t-1}$ and $P_{t|t}=P_{t|t-1}$. The next step then predicts $a_{t+1|t}=a_{t|t}$ and $P_{t+1|t}=P_{t|t}+Q$. In the local-level model the state prediction is flat and the variance grows by $Q$ for each missing step.

**5.**

```python
import numpy as np

rng = np.random.default_rng(0)
n, Q, R = 200, 0.5, 1.0
mu = np.cumsum(rng.normal(scale=np.sqrt(Q), size=n))
y = mu + rng.normal(scale=np.sqrt(R), size=n)

a, P = 0.0, 1e6                      # near-diffuse start
filtered = np.empty(n)
for t in range(n):
    if t > 0:
        P += Q
    K = P / (P + R)
    a += K * (y[t] - a)
    P *= 1 - K
    filtered[t] = a

print(np.sqrt(np.mean((y - mu) ** 2)), np.sqrt(np.mean((filtered - mu) ** 2)))
```

Raw-observation RMSE is $1.029$ (about $\sqrt R$); filtered-state RMSE is $0.732$, close to the steady-state value $\sqrt{P_{t|t}}=\sqrt{0.5}=0.707$. Steady state solves $P_p=P_f+Q$, $P_f=P_pR/(P_p+R)$, which for $Q=0.5,R=1$ gives $P_p=1$ and $K=0.5$.

**6.** The prediction-error decomposition: $\log L=\sum_t\ell_t$ with $\ell_t=-\tfrac12[\log2\pi+\log F_t+v_t^2/F_t]$, where $v_t$ and $F_t$ come from the Kalman recursion. Because $v_t\mid y_{1:t-1}\sim N(0,F_t)$, the joint density factorizes into these conditional densities. Missing observations contribute no term.

**7.** Example: weekly sales whose underlying level drifts after promotions and is measured with noise. A regression on time imposes a deterministic line and treats all deviations as noise, whereas a local-level model lets the level move and gives forecast intervals that widen at the correct rate; it also handles gaps in the data.

**8.** In `filtering_vs_smoothing` ("Filtering is real-time; smoothing uses later observations"), the filtered path lags behind turns and is rougher at the right end, while the smoothed path is cleaner because it uses future observations.

**9.** Gains $K=1.25/(1.25+R)$ and updates:

| $R$ | $F$ | $K$ | $a_{t\mid t}$ | $P_{t\mid t}$ |
|---:|---:|---:|---:|---:|
| 0.1 | 1.35 | 0.9259 | 11.8519 | 0.0926 |
| 1 | 2.25 | 0.5556 | 11.1111 | 0.5556 |
| 4 | 5.25 | 0.2381 | 10.4762 | 0.9524 |

Plotting $K$ against $R$ gives a decreasing curve from $1$ (as $R\to0$) towards $0$.

**10.** With $Q=0.5$, $R=1$ the steady filtered variance is $0.5$. During a gap of 20 observations the variance grows linearly: $0.5\to0.5+0.5k$, reaching $10.5$ at the end of the gap. When data resume, one observation brings the variance down to $\approx0.92$ and about ten observations later it is back near $0.5$.

**11.** Evaluate the Gaussian log-likelihood from Question 6 (or the innovation sum of squares $\sum v_t^2/F_t$ plus $\sum\log F_t$) over a grid of $(Q,R)$. On the seeded series with true $(0.5,1)$ and grid $\{0.1,0.25,0.5,1,2\}^2$, the minimum negative log-likelihood is $364.9$ at $(Q,R)=(0.5,1)$. The surface is typically flat along a ridge in $(Q,R)$ because the gain depends mainly on $Q/R$.

**12.** A regression on time estimates one fixed line; its uncertainty is parameter uncertainty and the residual variance. A local-level model has a stochastic level, so forecast variance is $P_{T|T}+hQ+R$, growing with the horizon. If the level really wanders, the regression residuals are autocorrelated and its intervals are too narrow.

**13.** $\tilde v_t=v_t/\sqrt{F_t}$ should be roughly $N(0,1)$ and serially uncorrelated; ACF spikes suggest missing dynamics, and a positive ACF of $\tilde v_t^2$ suggests changing variance.

**14.** The smoothed state at $t$ is conditioned on $y_{t+1},\ldots,y_T$. A model trained or evaluated with it has used future information at the forecast origin, so backtests overstate accuracy. Use filtered states (recomputed or truncated at the origin).

**15.** Minimize $J(a)=\dfrac{(y-a)^2}{R}+\dfrac{(a-a_{t|t-1})^2}{P}$. Setting $J'(a)=0$ gives

$$
\hat a=\frac{a_{t|t-1}/P+y/R}{1/P+1/R}=a_{t|t-1}+\frac{P}{P+R}(y-a_{t|t-1}),
$$

and the curvature gives $P_{t|t}=(1/P+1/R)^{-1}=PR/(P+R)=(1-K)P$.

**16.** At an abrupt jump the filtered estimate catches up over several observations (speed governed by $K$), while the smoothed estimate moves earlier, before the jump, because later observations pull it, giving a smoother and often more accurate historical path.

**17.** $\ell_t=-\tfrac12[\log(2\pi)+\log2.25+4/2.25]=-\tfrac12[1.8379+0.8109+1.7778]=-2.2133$.

**18.** The steady-state gain depends only on $q=Q/R$. For $Q=0.5,R=1$: $P_p=\tfrac12[Q+\sqrt{Q^2+4QR}]=1$ and $K=0.5$. For $Q=0.05,R=1$: $P_p=0.25$ and $K=0.2$, so the filtered path is smoother but slower to react. Doubling both $Q$ and $R$ leaves the gain unchanged.

**19.** A local linear trend has states $(\ell_t,b_t)$ with $\ell_t=\ell_{t-1}+b_{t-1}+\eta_t$ and $b_t=b_{t-1}+\zeta_t$; the slope can evolve and is estimated from the data recursively. A regression on time has a fixed slope for the whole sample (the case $\mathrm{Var}(\eta)=\mathrm{Var}(\zeta)=0$).

**20.** Start: the filtered variance equals the prior variance until observations arrive, so uncertainty is large and the level is unidentified. Middle: variance rises by $Q$ per step and drops when data resume. End: the series simply becomes a forecast, so the variance keeps growing and the observation-level interval widens as $P_{t|t}+kQ+R$.

## Submission check

Include the state and measurement equations, one hand update, a gain or variance figure, missing-data behavior, and a real-time versus retrospective interpretation.
