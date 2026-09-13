# Frequency-Domain Analysis

## Worked calculation: frequency, period, and resolution

For a seasonal signal that repeats every 12 observations,

$$
f=\frac{1}{12}\approx0.08333
\quad\text{cycles per observation}.
$$

With $N=240$ observations, the Fourier frequency spacing is $1/N=0.004167$, so the period-12 component lies near Fourier bin $240/12=20$. The Nyquist frequency is $0.5$ cycles per observation; a signal above that limit cannot be distinguished from an aliased lower frequency.

The periodogram peak should therefore be translated back into a period before interpretation. A peak near $0.0833$ means “about twelve observations per cycle,” not “frequency 12.”

![A period-12 signal and its periodogram](../../assets/time_series/student/19_frequency_periodogram.png)

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

## Student guide: read a spectrum as a decomposition of variation

Frequency analysis does not replace time-domain analysis. It answers a different question:

> At which cycle lengths is the series variable, and are those cycle lengths shared by another series?

The answer depends on sampling rate, observation length, trend treatment, windowing, and the stationarity assumptions behind the spectrum.

### From period to frequency

If a pattern repeats every $P$ sampling intervals, its frequency is

$$
f=\frac1P.
$$

For a 12-month cycle,

$$
f=\frac1{12}=0.08333
\quad\text{cycles per month}.
$$

If observations are every 15 minutes, the same formula is expressed in cycles per 15-minute interval. Convert the period to the desired physical unit only after recording the sampling interval.

The Nyquist frequency is half the sampling rate. With one observation per unit interval it is $0.5$ cycles per observation. A signal with frequency $0.65$ cycles per observation is sampled as a lower-frequency alias because the sampling rate is too slow to distinguish it.

### DFT and frequency resolution

For $N$ observations, the Fourier frequencies are

$$
f_k=\frac{k}{N},\qquad k=0,\ldots,\left\lfloor\frac N2\right\rfloor.
$$

The spacing is $1/N$. With $N=240$, the spacing is

$$
\Delta f=\frac1{240}=0.004167.
$$

A period-12 component has $f=1/12$ and lies at bin

$$
k=Nf=240\left(\frac1{12}\right)=20.
$$

Longer series provide finer frequency resolution, but additional observations do not automatically make a changing-frequency process stationary.

### Periodogram scaling

Let $\tilde x_t=x_t-\bar x$ and

$$
X_k=\sum_{t=0}^{N-1}\tilde x_t e^{-2\pi i kt/N}.
$$

A common periodogram scale is proportional to

$$
I(f_k)=\frac1N|X_k|^2.
$$

The constant factor varies by software and sampling interval. Interpret relative peaks only after checking the normalization.

The periodogram is noisy. A high peak may reflect a genuine cycle, leakage from a nearby strong frequency, a trend, a transient event, or repeated searching over many frequencies.

### Trend and low-frequency power

A deterministic trend produces strong low-frequency power because it changes slowly. If the purpose is to study cycles around a trend, detrend first:

$$
x_t=m_t+r_t.
$$

Then analyze $r_t$. Differencing is another option:

$$
\nabla x_t=x_t-x_{t-1},
$$

but differencing changes the frequency response and emphasizes higher frequencies. A transformation should follow the scientific question, not the desire to make a visually cleaner periodogram.

### Spectral leakage and windows

The finite sample is multiplied by an observation window. A rectangular window has sharp edges, and when the sample does not contain an integer number of cycles, power spreads into neighboring bins. This is spectral leakage.

Tapering with a Hann or cosine window reduces side lobes but broadens the central peak. Window choice is a bias-variance tradeoff:

- less leakage can make nearby frequencies harder to separate;
- a sharp window can make a weak frequency appear in many neighboring bins;
- a broader peak does not necessarily mean the physical cycle is unstable.

Report the window and detrending settings when comparing spectra.

### Cross-spectrum and coherence

For two series $x_t$ and $y_t$, the cross-periodogram is related to

$$
I_{xy}(f)=X(f)\overline{Y(f)}.
$$

A smoothed squared coherence has the form

$$
C^2_{xy}(f)
=\frac{|S_{xy}(f)|^2}{S_{xx}(f)S_{yy}(f)}.
$$

Values near 1 indicate a strong linear association at that frequency. Coherence does not identify direction, timing, or causality. A common seasonal driver can create high coherence in both series.

### A numerical periodogram example

Let

$$
x_t=1.8\sin\left(\frac{2\pi t}{12}\right)+0.8\sin\left(\frac{2\pi t}{30}\right)+\varepsilon_t.
$$

The first component has period 12 and the second period 30. If the noise is moderate, the periodogram should show peaks near $1/12\approx0.0833$ and $1/30\approx0.0333$. The larger amplitude does not guarantee the larger observed peak in a short noisy sample, so inspect stability across windows or replications.

### Practical interpretation checklist

Before treating a spectral peak as evidence:

1. verify the sampling interval and maximum identifiable frequency;
2. inspect the raw series and its trend;
3. record the detrending, differencing, and window settings;
4. convert the peak frequency to a period;
5. check whether the peak lies near a boundary or harmonic;
6. repeat over adjacent time windows if stationarity is doubtful;
7. compare against simulated noise or a domain baseline;
8. account for multiple frequencies examined;
9. avoid causal claims based on coherence alone.

### Visual companions

Run [state_space_frequency_visualizations.py](../../scripts/time_series/state_space_frequency_visualizations.py):

![Periodogram](../../assets/time_series/state_space_frequency/05_periodogram.png)

![Spectral leakage and windowing](../../assets/time_series/state_space_frequency/06_spectral_leakage_windowing.png)

![Aliasing](../../assets/time_series/state_space_frequency/07_aliasing.png)

![Frequency relationship](../../assets/time_series/state_space_frequency/08_frequency_relationship.png)

The state-space companions are in the [state-space chapter](state_space_models.md).

See [`frequency_domain.py`](../../scripts/time_series/frequency_domain.py) and the [state-space/frequency notebook](../../notebooks/time_series/state_space_and_frequency.ipynb).
