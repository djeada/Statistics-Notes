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
