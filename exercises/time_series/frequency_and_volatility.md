# Frequency and Volatility

Read [frequency-domain analysis](../../notes/time_series/frequency_domain_analysis.md) and [financial time-series models](../../notes/time_series/financial_time_series_models.md).

1. A signal repeats every 12 observations. Calculate its frequency in cycles per observation.
2. With 240 observations, calculate the Fourier frequency spacing and identify the nearest bin for a period-12 signal.
3. Explain aliasing using a signal above the Nyquist frequency. What additional sampling information would prevent it?
4. Simulate a period-12 sinusoid plus noise and use a periodogram to recover the dominant period.
5. Add a strong trend to the simulated signal. Compare the periodogram before and after detrending and explain the low-frequency difference.
6. A price moves from 100 to 102. Calculate the log return to four decimal places.
7. For $\alpha_0=0.01$, $\alpha_1=0.10$, $\beta_1=0.85$, $r_{t-1}=0.2$, and $h_{t-1}=0.04$, calculate $h_t$ and its conditional standard deviation.
8. Explain why raw returns can have weak autocorrelation while squared returns show volatility clustering.

## Checks

- The period-12 frequency is $1/12\approx0.08333$.
- Frequency spacing is $1/240\approx0.004167$, and the period-12 component is near bin 20.
- The log return is $\log(1.02)\approx0.0198$.
- The conditional variance is $0.048$ and the conditional standard deviation is about $0.219$.

## Applied practice

9. Run [state_space_frequency_visualizations.py](../../scripts/time_series/state_space_frequency_visualizations.py). Convert each visible spectral peak to a period and state the sampling assumptions.
10. Compare a rectangular and tapered window for a frequency that does not fall exactly on a Fourier bin. Describe leakage and peak width.
11. Sample a high-frequency sinusoid at two different rates. Demonstrate when aliasing appears.
12. Detrend a periodic signal before calculating its periodogram. Compare low-frequency power and the peak of interest.
13. Simulate two series with a shared cycle and calculate a frequency-specific coherence-like measure. Explain why it is not causal evidence.
14. Run [financial_time_series_visualizations.py](../../scripts/time_series/financial_time_series_visualizations.py). Compare ACF of returns and squared returns.
15. Calculate ARCH and GARCH variance paths after a positive and negative shock. Add an asymmetric term and compare.
16. Backtest a one-day 95% VaR forecast. Record exceedance count, clustering, and the innovation distribution used.

## Reflection

Report the sampling interval, frequency resolution, detrending/window choice, return definition, variance recursion, tail distribution, and temporal validation design.

## Extension tasks

17. Calculate the Nyquist limit for data sampled every 15 minutes and express a one-day cycle in cycles per sample.
18. Generate a sinusoid whose frequency lies halfway between Fourier bins. Compare leakage under two windows.
19. Explain why a periodogram peak can move when a structural break changes the phase or amplitude.
20. Fit or simulate a volatility model with $\alpha+\beta=0.99$. Discuss long-run variance and finite-sample persistence.
21. Compare Gaussian and Student-$t$ tail probabilities at a chosen risk threshold.
22. Evaluate VaR exceedances for clustering, not only total count.

## Worked solutions

Numerical simulation results use seeded runs (`numpy.random.default_rng`, SciPy `periodogram`); other seeds change the digits, not the conclusions.

**1.** Frequency $=1/\text{period}=1/12\approx0.08333$ cycles per observation.

**2.** Spacing $=1/n=1/240\approx0.004167$. The Fourier frequencies are $k/240$, and $1/12=20/240$, so the period-12 component lies exactly on bin $k=20$.

**3.** Sampling every $\Delta$ units only distinguishes frequencies up to $f_N=1/(2\Delta)$. A frequency $f$ above $f_N$ is indistinguishable from $|f-k/\Delta|$ for the integer $k$ that brings it into $[0,f_N]$. Example: a sinusoid with 9 cycles per unit sampled 10 times per unit gives the same samples as one at 1 cycle per unit (up to sign). Prevent it by sampling faster, applying an analogue low-pass filter before sampling, or knowing the signal is band-limited.

**4.**

```python
import numpy as np
from scipy import signal

rng = np.random.default_rng(0)
n = 240
t = np.arange(n)
x = np.sin(2 * np.pi * t / 12) + rng.normal(size=n)
f, p = signal.periodogram(x, window="boxcar", detrend=False)
k = np.argmax(p)
print(f[k], 1 / f[k])
```

The peak is at bin $20$, $f=0.08333$, period $12.0$.

**5.** Adding $0.05t$ puts a huge amount of power into the lowest frequencies. In the seeded run the periodogram at bins 1, 2, 3 is about $1637$, $437$, $226$, and the largest ordinate is at the lowest frequencies rather than at the period-12 bin. After linear detrending the same bins carry power of only about $0.6$, $2.7$, $4.5$, and the period-12 peak (bin 20) is the maximum. A trend is a very low-frequency component, and the rectangular window leaks its power over the spectrum.

**6.** $\log(102/100)=\log 1.02=0.0198$.

**7.** $h_t=\alpha_0+\alpha_1r_{t-1}^2+\beta_1h_{t-1}=0.01+0.10(0.04)+0.85(0.04)=0.01+0.004+0.034=0.048$. The conditional standard deviation is $\sqrt{0.048}\approx0.2191$.

**8.** Returns are close to a martingale difference, so there is little linear predictability (small ACF). Large movements of either sign are followed by large movements, so $r_t^2$ (or $|r_t|$) is positively autocorrelated; this is conditional heteroskedasticity.

**9.** The periodogram has two peaks. Bin positions: $f=8/240=0.0333$ (period $30$) and $f=20/240=0.0833$ (period $12$), assuming one observation per time unit and 240 observations.

**10.** For a frequency halfway between bins, a rectangular window concentrates power into the adjacent bins and shows sidelobes that decay slowly. A taper (Hann, Hamming) lowers sidelobes at the price of a wider main lobe. The rectangular window has the narrowest peak but the worst leakage.

**11.** Sample $\sin(2\pi\cdot9t)$ at 10 samples per unit ($f_N=5$): the sample sequence equals $-\sin(2\pi\cdot1\cdot t)$, an alias at frequency 1. Sampling at 40 per unit shows the 9-cycle oscillation correctly.

**12.** Detrending removes the low-frequency pile-up, so the periodogram near $0$ falls by orders of magnitude (Question 5), while the periodic peak remains (here $88\to127$ in power units; the change comes from trend leakage interfering with the peak's bin before detrending).

**13.** For $x_t=\cos(\omega t)+e_t$ and $y_t=\cos(\omega t+\varphi)+u_t$, estimate smoothed cross-spectra and compute $\hat C(f)=|\hat f_{xy}|^2/(\hat f_{xx}\hat f_{yy})$. It is near $1$ at the shared frequency and near $0$ elsewhere. It measures linear association at that frequency, with no direction, so a common driver gives the same result.

**14.** In the "ACF of returns" and "ACF of squared returns" panels, the ACF of returns stays inside the white-noise band, while the ACF of squared returns is positive over many lags.

**15.** With $r_{t-1}=\pm0.2$ and $h_{t-1}=0.04$, symmetric ARCH/GARCH gives the same $h_t=0.048$ for both signs. With a GJR term $\gamma\,r^2\mathbf 1[r<0]$, $\gamma=0.1$: positive shock $h_t=0.048$, negative shock $h_t=0.048+0.1(0.04)=0.052$. Expected later variances follow $h_{t+k}=\alpha_0+(\alpha_1+\beta_1)h_{t+k-1}$ (the GJR version adds $\gamma/2$ to the persistence for a symmetric shock distribution): $0.048,\ 0.0556,\ 0.0628,\ 0.0697,\ldots$, rising towards the long-run variance $0.01/(1-0.95)=0.2$ because $0.04$ starts below it. The negative-shock GJR path starts at $0.052$ and stays above the symmetric path in the following steps.

**16.** Simulate GARCH, compute VaR$_t=-1.645\sqrt{h_t}$ for the return $r_t$ (as a loss threshold), count $r_t<$ VaR$_t$. In one seeded run of 1000 days there were 46 exceedances (rate $0.046$ against nominal $0.05$) with 4 on consecutive days. Kupiec's test checks the count; Christoffersen's test checks clustering. Record the innovation distribution, since Gaussian quantiles understate tails for $t$-distributed shocks.

**17.** Sampling every 15 minutes: Nyquist limit $=1/(2\cdot15)=1/30$ cycle per minute ($0.5$ cycle per sample, shortest identifiable period 30 minutes). One day $=96$ samples, so a daily cycle has frequency $1/96\approx0.0104$ cycles per sample.

**18.** Use $f=20.5/240$. With a rectangular window the peak splits across bins 20 and 21 with strong sidelobes; with a Hann window the peak is wider but sidelobes are much smaller. Padding with zeros interpolates the spectrum but does not improve resolution.

**19.** A break in phase or amplitude makes the signal a different sinusoid before and after the break, so the single-sinusoid model is wrong: the periodogram averages the two regimes and can split or shift the peak. Use a windowed or wavelet spectrum to see the change.

**20.** The long-run variance is $\omega/(1-\alpha-\beta)$, e.g. $0.01/0.01=1$, but shocks decay at rate $0.99^k$ (half-life $\ln 0.5/\ln0.99\approx69$ periods), so in finite samples the variance rarely settles and estimates of $\omega$ are unstable. Near-integrated GARCH is also confused with structural breaks in variance.

**21.** For a unit-variance threshold $-3$: Gaussian $P(Z<-3)=0.00135$; Student-$t_5$ scaled to unit variance has $P(X<-3)=P(T_5<-3/\sqrt{0.6})=0.0059$ (about $4$ times more likely). The 5% quantiles are $-1.645$ (Gaussian) and $-1.561$ (unit-variance $t_5$), so the $t$ is less extreme at moderate levels; at 1% they are $-2.326$ and $-2.606$, and the $t$ is more extreme in the tail.

**22.** Compute exceedance indicators $I_t$ and test independence (Christoffersen), or count consecutive pairs ($4$ of $46$ in Question 16). A correct unconditional rate with clusters means VaR failed in high-variance regimes.

## Submission check

Include the sampling and return definitions, numerical frequency/variance calculations, one spectral figure, one volatility figure, and a statement of what the diagnostics cannot identify.
