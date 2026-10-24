# Statistical Moments and Time Series

A mean or variance summarizes a distribution, but a time series adds two questions: **which date's distribution**, and **how are values at different dates related**? A single average of the whole record cannot answer both. A rising level can be hidden by that average, and two sequences with identical histograms can have completely different patterns of persistence.

The mean function $\mu_t=E(X_t)$ describes the center at each date. The variance describes uncertainty around that date's mean. Autocovariance then connects two dates by asking whether their deviations tend to have the same sign or opposite signs. Keeping these quantities separate is the starting point for describing temporal structure.

Population moments refer to the underlying process across possible realizations. Sample means, sample variances, and rolling estimates are calculations on the one realized path we observe. Stationarity can make observations at different dates informative about common population moments, but it does not make them independent. The estimation uncertainty still depends on temporal covariance, which is why independent-sample formulas cannot simply be carried over unchanged.

## Worked calculation: mean, variance, and lag covariance

For the four observations

$$
2,\quad4,\quad4,\quad6,
$$

the sample mean is

$$
\bar x=\frac{2+4+4+6}{4}=4.
$$

The empirical variance with divisor $n=4$ is

$$
\frac{(-2)^2+0^2+0^2+2^2}{4}=2,
$$

Using the divisor $n-1=3$ instead gives $8/3\approx2.667$. This familiar correction is unbiased for IID observations with finite variance. For serially correlated observations, dividing by $n-1$ does not generally remove the bias, because the sample mean and the squared deviations also depend on the serial covariance structure.

At lag 1, the paired centered products are

$$
(-2)(0)+(0)(0)+(0)(2)=0.
$$

Every adjacent product contains at least one zero, so the lag-1 sum vanishes for this particular ordering. That arithmetic does not show that the data were generated independently. A sample covariance is one noisy summary, and positive and negative contributions can also cancel in other samples. To learn about the process, inspect several relevant lags and consider the assumptions that justify estimating one common lag covariance.

![Series with different sample variances](https://raw.githubusercontent.com/djeada/Statistics-Notes/main/assets/time_series/student/03_moments_mean_and_variance.png)

The figure illustrates why the mean alone is not enough to describe a series: two sequences can be centered at similar levels while differing substantially in their spread.

The numerical examples illustrate two different summaries of the same data. Marginal moments describe the values without their order. Lagged moments describe pairs chosen by their time separation. Reordering observations leaves the marginal mean and variance unchanged but changes which pairs enter the lag calculation. Any summary intended to describe a time series should make clear which of these two types of information it retains.

## Introduction to Statistical Moments in Time Series

The **mean** is an expectation over possible outcomes at a fixed date, not a guarantee that the observed series stays near one number. The **variance** is the expected squared distance from that mean. Its square root, the standard deviation, returns the scale to the original units. For example, if observations are in units sold, variance is in squared units sold while standard deviation is again in units sold.

A time-varying mean and a time-varying variance can produce superficially similar plots. A changing mean moves the center around which observations fluctuate. A changing variance alters the size of the fluctuations around the center. Fitting a flexible trend to a variance change, or treating a level shift as a burst of volatility, can therefore lead to the wrong model even when the fitted curve looks plausible.

## Examples of Time Series with Varying Statistical Moments

Consider first a series whose location changes while its spread stays roughly stable, then a series whose spread changes while its central level remains similar.

### Time Series with a Varying Mean

![Time Series with Varying Mean](https://github.com/user-attachments/assets/848b516a-e4ab-476b-8f79-b62efcf28579)

In this example, the center of the series increases over time while the dispersion around that center remains relatively stable. The visual pattern suggests investigating a changing mean or level. A deterministic trend changes the population mean directly; a zero-drift random walk instead has a constant population mean but a wandering realized level and growing variance. A single path can suggest either mechanism, so its appearance alone does not distinguish them.

### Time Series with a Varying Standard Deviation

![Time Series with Varying Standard Deviation](https://github.com/user-attachments/assets/7216800d-c290-4617-853b-e44e0ef95272)

Here the deviations become larger or smaller without a comparable movement in the central level. To investigate that pattern, examine residuals around an appropriate mean model rather than interpreting large raw observations alone. A higher level can naturally produce larger absolute fluctuations, in which case a log transformation may help; volatility clustering can instead remain after that scale effect has been addressed.

The two figures demonstrate why stationarity involves more than checking whether a plot has an obvious trend. Both the level and the variance structure matter.

![Changing moments](https://raw.githubusercontent.com/djeada/Statistics-Notes/main/assets/time_series/foundations/04_moments_change_over_time.png)

This companion figure places the cases side by side so that changes in the mean and changes in the variance can be distinguished directly.

## Time Series vs. Independent Random Variables

A time series differs from an unordered sample because the observation order can carry information. Two datasets can have the same marginal distribution, mean, and variance while having very different temporal dependence.

The following visualization compares an observed sequence with a fitted marginal distribution.

![Time Series vs. Random Variables](https://github.com/user-attachments/assets/c657913b-fe5f-443d-a469-5fdc65bef7fa)

The fitted marginal distribution treats the observations as a collection of values. Simulating independent draws from it may reproduce the approximate range and histogram, but it randomizes the order. Runs of high values, alternating signs, or clustered large deviations will generally disappear. Matching the marginal distribution is therefore insufficient for reproducing a time series or assessing uncertainty about an aggregate over time.

A time index does not itself imply dependence: independent noise is also a time series. Weak white noise has zero autocorrelation but can still have nonlinear dependence. Time-series analysis therefore examines the type of dependence supported by the data instead of inferring independence from a flat sample ACF.

## Implications for Modeling and Analysis

Temporal covariance changes the amount of information in a sample. The variance of a sum contains both the individual variances and the cross-time covariance terms. Positive covariance can make nearby observations carry overlapping information, so the usual independent-sample standard error of an average can be too small. Negative covariance can have the opposite effect. This issue concerns estimation uncertainty even when the sample mean itself remains unbiased.

An **AR** model describes how past observed values contribute to the next value. An **MA** model describes how a finite history of shocks contributes, and an **ARMA** model combines both mechanisms. These equations imply particular covariance patterns; fitting them is one way of explaining the lagged moments. A trend, a seasonal mean, or a structural break must still be represented separately when the chosen stationary equation does not include it.

The ACF, PACF, residual diagnostics, and out-of-sample forecasts help determine whether a proposed dependence structure is useful.

## Estimating moments from one ordered path

For a cross-sectional sample, one mean and one variance may summarize the marginal distribution. For a time series, the relevant quantities include

$$
\mu_t=E(X_t),
\qquad
\gamma_t(0)=\mathrm{Var}(X_t),
\qquad
\gamma_t(h)=\mathrm{Cov}(X_t,X_{t-h}).
$$

Weak stationarity removes the date dependence from these first two moment descriptions: the mean is common across dates and the covariance depends on the separation $h$. This allows us to pool lag-$h$ pairs from different parts of the record to estimate one quantity. Without that assumption, the same pooled estimate can mix genuinely different regimes and need not describe any particular date well.

### Numerical moment calculation

For $(2,4,4,6)$,

$$
\bar x=4,
\qquad
\hat\sigma_n^2=\frac{(-2)^2+0^2+0^2+2^2}{4}=2.
$$

The sample variance using divisor $n-1$, which is unbiased under the IID assumptions described above, is

$$
s^2=\frac{8}{3}\approx2.667.
$$

At lag 1, the centered products are $0$, $0$, and $0$ for this ordering, so the lag-1 sample covariance is zero. This small example shows why a single zero covariance is weak evidence about the underlying process.

For the sequence $(1,2,4,3)$, the centered values are $(-1.5,-0.5,1.5,0.5)$ and the lag-1 covariance using denominator $n$ is $0.1875$.

Reorder the same values as $(1,2,3,4)$. The centered values become $(-1.5,-0.5,0.5,1.5)$, and the lag-1 covariance is $1.25/4=0.3125$. The marginal mean and variance have not changed, but the lag covariance has: it uses adjacent pairs, so it retains information about temporal order.

### Cross-moments and dependence

For two series $X_t$ and $Y_t$, the lagged cross-covariance is

$$
\gamma_{XY}(h)=\mathrm{Cov}(X_t,Y_{t-h}).
$$

With the convention shown above, positive $h$ pairs the current $X_t$ with an earlier $Y_{t-h}$. Reversing the series or the lag sign changes that timing interpretation. A peak can reflect a shared trend, a common seasonal driver, or different publication delays rather than an effect of one series on the other. Write down the actual paired timestamps before using a cross-covariance peak to select predictor lags.

### Rolling moments

A rolling mean and variance provide local descriptive summaries:

$$
\hat\mu_t^{(w)}=\frac1w\sum_{j=0}^{w-1}x_{t-j},
\qquad
\hat v_t^{(w)}=\frac1{w-1}\sum_{j=0}^{w-1}(x_{t-j}-\hat\mu_t^{(w)})^2.
$$

A short window emphasizes recent observations but gives a variable estimate because few observations enter it. A long window reduces that variability while averaging across changes that may matter. Neighboring windows also share most of their observations, so a smooth-looking rolling curve is partly a consequence of overlap. Treat the curve as an exploratory description, check sensitivity to $w$, and use a past-only window for real-time features.

### Moments do not identify a distribution

Matching the first two marginal moments leaves many features unspecified. Rare large values can produce different tail risk; asymmetric distributions can have different skewness; and the same values can be ordered to produce very different autocorrelation. Even stable unconditional variance can coexist with predictable conditional variance. A mean-and-variance description is useful precisely because it is limited: it isolates a few features that must then be combined with temporal and distributional checks.

Moments are therefore part of the description rather than a complete model. Plot how they evolve and examine temporal dependence separately before deciding whether a stationary model is appropriate.

### Visual companion

The changing-moments figure above summarizes the main visual lesson of this chapter: inspect the center and spread separately, then relate any changes to the dependence structure and modeling assumptions.

## Formula reference

| Moment / summary | General formula | Time-series interpretation |
|---|---|---|
| Raw $k$th moment | $m_k=E[X^k]$ | Describes the marginal distribution at a fixed time. |
| Central $k$th moment | $\mu_k=E[(X-E[X])^k]$ | $\mu_2$ is variance; higher moments describe shape. |
| Mean function | $\mu_t=E[X_t]$ | Constant in $t$ under weak stationarity. |
| Variance | $\mathrm{Var}(X_t)=E[(X_t-\mu_t)^2]$ | Constant in $t$ under weak stationarity. |
| Standard deviation | $\sigma_t=\sqrt{\mathrm{Var}(X_t)}$ | Expresses spread in the original units. |
| Skewness | $\gamma_1=E[(X-\mu)^3]/\sigma^3$ | Measures asymmetry of the marginal distribution. |
| Kurtosis | $\gamma_2=E[(X-\mu)^4]/\sigma^4$ | Normal distribution has kurtosis $3$; excess kurtosis subtracts $3$. |
| Autocovariance | $\gamma_t(h)=\mathrm{Cov}(X_t,X_{t-h})$ | Under weak stationarity, write $\gamma(h)$ because it depends only on lag. |
| Autocorrelation | $\rho(h)=\gamma(h)/\gamma(0)$ | Scale-free lag dependence. |
| Cross-covariance | $\gamma_{XY}(h)=\mathrm{Cov}(X_t,Y_{t-h})$ | Describes lead-lag linear association between two series. |
| Sample mean | $\bar x=n^{-1}\sum_{t=1}^{n}x_t$ | Global level estimate when one mean is meaningful. |
| Sample variance with divisor $n-1$ | $s^2=(n-1)^{-1}\sum_{t=1}^{n}(x_t-\bar x)^2$ | Unbiased for IID observations with finite variance; serial dependence changes that conclusion. |
| Rolling mean | $\hat\mu_t^{(w)}=w^{-1}\sum_{j=0}^{w-1}x_{t-j}$ | Local level over a window of width $w$. |
| Rolling variance | $\hat v_t^{(w)}=(w-1)^{-1}\sum_{j=0}^{w-1}(x_{t-j}-\hat\mu_t^{(w)})^2$ | Local spread over the same window. |
