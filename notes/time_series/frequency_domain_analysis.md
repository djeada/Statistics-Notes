# Frequency-Domain Analysis

Time-domain methods describe dependence through lags. Frequency-domain methods describe how variability is distributed across cycles of different frequencies. The views are complementary.

A sinusoidal component can be written as

$$
x_t=A\cos(2\pi ft+\phi),
$$

with period $P=1/f$. A frequency of $1/12$ cycles per month corresponds to a 12-month cycle.

## Fourier Transform and Periodogram

For observations $x_0,\ldots,x_{N-1}$, the discrete Fourier transform is

$$
X_k=\sum_{t=0}^{N-1}x_te^{-i2\pi kt/N}.
$$

A **periodogram** estimates spectral power across frequencies. The theoretical spectral density of a weakly stationary process is the Fourier transform of its autocovariance function, so the ACF and spectrum encode the same second-order information in different coordinates.

## Nyquist Frequency and Aliasing

With one observation per sampling interval, the highest distinguishable frequency is the Nyquist frequency, $1/2$ cycle per interval. Higher frequencies are reflected into lower frequencies through **aliasing**.

## Spectral Leakage

A finite observation window rarely contains an exact integer number of cycles, so power spreads into neighboring Fourier frequencies. Windowing/tapering can reduce leakage at the cost of broader peaks. Strong trend can also dominate low-frequency power; detrending or differencing may be useful when justified by the analysis goal.

For two stationary series, cross-spectral methods examine shared variation by frequency. **Coherence** is a frequency-specific analogue of squared correlation, but high coherence does not establish causality.

A practical workflow is: inspect trend and sampling frequency, transform only when justified, compute a periodogram or smoothed spectrum, translate peaks into periods, and interpret them with aliasing/leakage/data-snooping concerns in mind.

See [`frequency_domain.py`](../../scripts/time_series/frequency_domain.py) and the [state-space/frequency notebook](../../notebooks/time_series/state_space_and_frequency.ipynb).
