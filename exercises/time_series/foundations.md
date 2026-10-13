# Foundations

Read [stochastic processes and white noise](../../notes/time_series/stochastic_processes_and_white_noise.md), [difference equations](../../notes/time_series/difference_equations.md), and [random walks](../../notes/time_series/random_walk.md) first.

1. For the geometric series with ratio $r=0.5$, calculate the partial sum through $r^4$ and the infinite sum. What is the size of the omitted tail?
2. Solve $x_t=0.7x_{t-1}+2$ with $x_0=10$. Calculate $x_1$, $x_2$, and the equilibrium. Explain why the distance from equilibrium shrinks.
3. For $(2,4,4,6)$, calculate the mean, population-style variance, and unbiased sample variance. Explain why the two variance denominators answer different questions.
4. Let $\varepsilon_t$ be independent with variance 4. What are $\gamma(0)$ and $\gamma(h)$ for $h\ne0$? Does this alone prove independence for an arbitrary white-noise process?
5. A random walk starts at $X_0=5$ and has shocks $1,-2,0.5$. Calculate $X_1$, $X_2$, and $X_3$. If shock variance is 1, calculate $\operatorname{Var}(X_3\mid X_0)$.
6. Simulate 500 observations of white noise and a random walk with the same shocks. Compare their plots and sample variances. Which variance should change as the sample length grows?
7. Write one example of a process with zero linear autocorrelation but nonlinear dependence. Explain why a residual ACF may miss it.

## Checks

- The geometric partial sum is $1.9375$, the limit is $2$, and the omitted tail is $0.0625$.
- The recursion gives $x_1=9$, $x_2=8.3$, and equilibrium $2/(1-0.7)=6.\overline6$.
- The variance values are $2$ with denominator $n$ and $8/3$ with denominator $n-1$.
- The random-walk variance after three independent unit-variance shocks is $3$.

## Applied practice

8. Run [foundations_visualizations.py](../../scripts/time_series/foundations_visualizations.py). Change the AR coefficient from $0.7$ to $0.95$. Describe what changes in the path, ACF, and forecast horizon.
9. Construct an additive series with trend $0.2t$, period-12 seasonality, and Gaussian noise. At $t=6$, calculate the trend and seasonal contributions before simulating the noise.
10. Generate regular and irregular sampling of the same continuous signal. Explain which ACF and spectral calculations assume a regular grid.
11. Apply a nine-point moving average to a noisy trend. Identify the boundary observations that use incomplete or padded windows.
12. Simulate a stationary AR(1), a random walk, and an explosive AR(1). Compare rolling means and variances rather than relying on one plot.
13. Explain why a changing marginal variance can make a process unsuitable for a constant-variance Gaussian model even when its mean is approximately zero.

## Reflection

For each simulation, write down the data-generating equation, the information available at the forecast origin, and the feature that would make the process difficult for an independent-sample method.

## Additional checks

- For $x_t=0.95x_{t-1}+\varepsilon_t$, the shock effect decays much more slowly than for $\phi=0.7$.
- A period-12 sinusoid has frequency $1/12$ cycles per observation.
- A centered smoother is acceptable for retrospective description but uses future observations as a real-time feature.

## Extension tasks

14. Derive the closed-form solution for $x_t=c+\phi x_{t-1}$ and verify it numerically for $c=2$, $\phi=0.7$, and $x_0=10$.
15. Simulate two series with the same histogram but different ACFs. Explain why independent resampling fails to reproduce one of them.
16. Compare a centered and trailing moving average at the final five observations. Identify which values would be available in real time.
17. Add a level shift to a stationary series. Decide whether a global variance and mean are meaningful summaries.
18. Write a data dictionary that states the time support, sampling interval, unit, and release time for a series of your choice.
19. Explain how changing from hourly observations to daily totals can alter variance, seasonality, and dependence.

## Worked solutions

1. $S_4=\sum_{k=0}^{4}0.5^k=1+0.5+0.25+0.125+0.0625=1.9375$, or $(1-0.5^5)/(1-0.5)=0.96875/0.5$. The infinite sum is $1/(1-0.5)=2$, so the tail is $0.5^5/(1-0.5)=0.0625$.
2. $x_1=0.7(10)+2=9$ and $x_2=0.7(9)+2=8.3$. The equilibrium solves $x^*=0.7x^*+2$, so $x^*=2/0.3=6.\overline6$. Subtracting, $x_t-x^*=0.7(x_{t-1}-x^*)$, so the distance is multiplied by $0.7$ each step ($3.\overline3,\,2.3\overline3,\,1.63\overline3,\dots$) and shrinks because $|0.7|<1$.
3. Mean $=16/4=4$. Deviations $(-2,0,0,2)$, sum of squares $=8$. Population-style variance $=8/4=2$; unbiased sample variance $=8/3\approx2.667$. The $n$ version describes these four values as the whole population; the $n-1$ version corrects for having used the same data to estimate the mean, so it estimates the variance of the process that generated the sample.
4. $\gamma(0)=\operatorname{Var}(\varepsilon_t)=4$ and $\gamma(h)=0$ for $h\ne0$. No: zero autocovariance is only uncorrelatedness. White noise requires only uncorrelated terms with constant variance; dependence in higher moments (for example ARCH) is still possible. Independence was assumed in the problem, not derived from $\gamma$.
5. $X_1=5+1=6$, $X_2=6-2=4$, $X_3=4+0.5=4.5$. Since $X_3=X_0+\varepsilon_1+\varepsilon_2+\varepsilon_3$ with independent shocks, $\operatorname{Var}(X_3\mid X_0)=3(1)=3$.
6. Model answer:
   ```python
   rng = np.random.default_rng(0)
   e = rng.normal(size=500)
   rw = np.cumsum(e)
   print(e.var(), rw.var())
   ```
   White noise fluctuates around 0 with variance about 1. The random walk wanders, and its sample variance depends on the sample (typically tens to hundreds). The variance that grows with length is the random-walk marginal variance $\operatorname{Var}(X_t)=t\sigma^2$; the white-noise variance stays at $\sigma^2$.
7. Example: $X_t=\varepsilon_t\varepsilon_{t-1}$ with iid $N(0,1)$ shocks, or an ARCH process $X_t=\sigma_t z_t$. Here $\operatorname{Corr}(X_t,X_{t-h})=0$ for $h\ge1$ but $X_t^2$ is dependent on past squares. A residual ACF measures only linear dependence in the levels, so it is blind to dependence in magnitudes; the ACF of $X_t^2$ or $|X_t|$ would show it.
8. The path and ACF of $\phi=0.95$ are far more persistent: excursions last longer, the ACF decays as $0.95^h$ (still $0.77$ at lag 5 versus $0.17$ for $\phi=0.7$), and forecasts take much longer to revert to the mean, so the forecast horizon over which the origin still matters is roughly $\log(0.05)/\log\phi\approx58$ steps versus $8$.
9. At $t=6$ the trend is $0.2(6)=1.2$. For a period-12 seasonal such as $s_t=A\sin(2\pi t/12)$, $s_6=A\sin(\pi)=0$; with a cosine it would be $-A$. Add the two (and noise later): $y_6=1.2+s_6+\varepsilon_6$.
   ```python
   t = np.arange(1, 121)
   y = 0.2*t + 3*np.sin(2*np.pi*t/12) + rng.normal(size=t.size)
   ```
10. A regular grid is required by the lag-based ACF (lag $h$ means a fixed time gap), by the FFT/periodogram frequencies $k/n$, and by AR/ARMA recursions. With irregular sampling these quantities need interpolation, binning by time gap, or methods such as Lomb-Scargle and continuous-time models.
11. A centered 9-point window needs 4 observations on each side, so observations $1$–$4$ and $n-3$–$n$ (8 points in total) lack a complete window. They are either dropped (NaN) or computed from padded/shrinking windows, which biases them.
    ```python
    ma = pd.Series(y).rolling(9, center=True).mean()   # first 4 and last 4 are NaN
    ```
12. Model answer: simulate $\phi=0.7$, $\phi=1$, and $\phi=1.05$ with the same shocks and compute `rolling(50).mean()` and `rolling(50).var()`. The stationary AR(1) has rolling mean and variance that hover around constants ($0$ and $1/(1-0.49)\approx1.96$); the random walk has a drifting mean and rolling variance with level changes; the explosive series has rolling mean and variance that grow geometrically.
13. A constant-variance Gaussian model assigns the same spread to all times. If the marginal variance changes, prediction intervals are too wide in calm periods and too narrow in volatile ones, the likelihood is misspecified, and a single global $\hat\sigma^2$ describes no actual time. A zero mean does not help; the second moment is the failure.
14. Write $x_t=c+\phi x_{t-1}$. Iterating, $x_t=c(1+\phi+\dots+\phi^{t-1})+\phi^tx_0=c\,\dfrac{1-\phi^t}{1-\phi}+\phi^tx_0$, equivalently $x_t=x^*+\phi^t(x_0-x^*)$ with $x^*=c/(1-\phi)$. For $c=2,\phi=0.7,x_0=10$: $x_1=6.\overline6+0.7(3.\overline3)=9$, $x_2=6.\overline6+0.49(3.\overline3)=8.3$, $x_3=7.81$, matching the recursion.
15. Example: an iid sample and the same values re-ordered into a smooth sequence (for instance sorted within blocks) or an AR(1) with $\phi=0.8$ versus a shuffle of it. The histograms agree, but the ACFs differ. Independent resampling draws from the marginal distribution only, so it destroys the lag structure and reproduces the iid ACF (about 0) rather than the AR ACF.
16. Centered MA at time $t$ uses $y_{t-k},\dots,y_{t+k}$; at the last $k$ observations it needs future values and is undefined. The trailing MA uses $y_{t-2k},\dots,y_t$, so it is available at every time $t\ge 2k+1$. Only the trailing values are available in real time (and they lag the trend by about $k$ steps).
17. A level shift makes the global mean a blend of two regimes that describes neither, and the global variance is inflated by the between-regime gap. Both are meaningful only conditionally on regime (segment-wise estimates). The series is not weakly stationary, so global ACF estimates are also inflated at all lags.
18. Model answer: "Daily mean PM2.5 at station X: time support = calendar day (24-hour mean, local time); sampling interval 1 day, regular; unit $\mu\mathrm{g/m^3}$; released with a 2-day lag after validation, revisions possible for 30 days."
19. Daily totals of hourly data (i) smooth out short-term noise relative to the level, while the variance of the total scales with the number of hours and the dependence between them; (ii) remove the 24-hour cycle, so the shortest remaining seasonality is weekly; (iii) change the dependence structure, since daily ACF mixes many hourly lags and typically looks smoother and more persistent. Hourly and daily models are therefore not interchangeable.

## Submission check

Include the generating equation, seed, parameter values, one hand calculation, one figure, and a paragraph explaining what the simulation does not establish.
