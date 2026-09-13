# Frequency-Domain Analysis

Time-domain methods describe dependence through lags. Frequency-domain methods describe how variability is distributed across cycles of different frequencies. The two views are complementary.

## Sinusoids and Frequency

A sinusoidal component can be written as

$$
x_t=A\cos(2\pi f t+\phi),
$$

where $f$ is cycles per sampling interval. Its period is

$$
P=\frac{1}{f}.
$$

A frequency of $1/12$ cycles per month corresponds to a 12-month cycle.

## Discrete Fourier Transform

The discrete Fourier transform decomposes a finite sequence into complex sinusoidal components. For observations $x_0,\ldots,x_{N-1}$,

$$
X_k=\sum_{t=0}^{N-1}x_t e^{-i2\pi kt/N}.
$$

The squared magnitude $|X_k|^2$ measures the contribution associated with Fourier frequency $k/N$.

## Periodogram and Spectral Density

A **periodogram** is a sample estimate of spectral power across frequencies. Peaks can reveal dominant periodic behavior not obvious in a raw time plot.

The theoretical **spectral density** of a weakly stationary process is the Fourier transform of its autocovariance function. Therefore the ACF and spectrum contain the same second-order information expressed in different coordinates.

## Nyquist Frequency and Aliasing

With one observation per unit of time, the highest distinguishable frequency is the Nyquist frequency, $1/2$ cycle per sampling interval. Frequencies above it are reflected into lower frequencies, a phenomenon called **aliasing**.

Sampling design therefore determines which cycles can be identified.

## Spectral Leakage

A finite observation window rarely contains an exact integer number of cycles. Power then spreads into neighboring Fourier frequencies. This is **spectral leakage**. Windowing/tapering can reduce leakage at the cost of broadening peaks.

## Detrending and the Spectrum

Strong trend contributes substantial low-frequency power and can obscure periodic structure. Detrending or differencing may be appropriate before spectral analysis, but transformations change the spectrum and should be justified by the analysis goal.

## Cross-Spectra and Coherence

For two stationary series, cross-spectral methods examine how shared variation depends on frequency. **Coherence** is a frequency-specific analogue of squared correlation, ranging from 0 to 1. High coherence at a frequency indicates a strong linear relationship between the series at that cycle length, but it does not establish causality.

## Practical Workflow

1. Plot the series and inspect trend, seasonality, and sampling frequency.
2. Remove a strong deterministic trend when it would dominate the frequencies of interest.
3. Compute a periodogram or smoothed spectral estimate.
4. Convert notable frequencies to periods for interpretation.
5. Check whether peaks correspond to plausible domain cycles.
6. Consider leakage, aliasing, and multiple-testing/data-snooping concerns before treating a peak as a discovery.

See `scripts/time_series_analysis/frequency_domain.py` for a simulated example with two known periodic components.
