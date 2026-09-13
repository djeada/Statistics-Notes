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

## Submission check

Include the sampling and return definitions, numerical frequency/variance calculations, one spectral figure, one volatility figure, and a statement of what the diagnostics cannot identify.
