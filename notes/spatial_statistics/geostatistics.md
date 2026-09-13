# Geostatistics

Geostatistics models a spatially indexed random field

$$
\{Z(s): s\in D\}
$$

when a continuous quantity is observed at sampled coordinates and the goal is to understand or predict the field between those locations.

Examples include soil chemistry, groundwater level, rainfall, temperature, and pollution concentration.

## Mean and Residual Field

A useful decomposition is

$$
Z(s)=m(s)+\varepsilon(s),
$$

where $m(s)$ is the large-scale mean or trend and $\varepsilon(s)$ is residual spatial variation.

This separation matters. A smooth mean trend can produce apparent long-range dependence if the trend is not modeled before estimating covariance or a variogram.

## Second-Order Stationarity

A random field is second-order stationary when

$$
E[Z(s)] = \mu
$$

is constant and

$$
\operatorname{Cov}[Z(s),Z(s+h)] = C(h)
$$

depends on separation $h$, not on absolute location.

If dependence depends only on distance $\|h\|$, not direction, the model is **isotropic**.

Stationarity and isotropy are modeling assumptions, not universal properties of spatial data.

## Intrinsic Stationarity and the Semivariogram

A weaker framework models increments. The semivariogram is

$$
\gamma(h)
=
\frac{1}{2}
\operatorname{Var}[Z(s+h)-Z(s)].
$$

Under second-order stationarity,

$$
\gamma(h)=C(0)-C(h).
$$

The semivariogram is especially useful because it describes how dissimilarity grows with separation.

## Empirical Semivariogram

For a lag bin around distance $h$,

$$
\hat{\gamma}(h)
=
\frac{1}{2N(h)}
\sum_{(i,j)\in N(h)}
\left[Z(s_i)-Z(s_j)\right]^2.
$$

This is a descriptive estimator. Its points are not independent observations with equal variance, so fitting a smooth variogram model by ordinary unweighted regression is not generally justified.

The companion script [`variogram_and_kriging.py`](../../scripts/spatial_statistics/variogram_and_kriging.py) uses pair counts as simple fitting weights for an educational example.

## Nugget, Partial Sill, and Sill

A common model is

$$
\gamma(h)
=
c_0+c\left(1-e^{-\|h\|/a}\right),
\qquad \|h\|>0,
$$

with $\gamma(0)=0$.

Here:

- $c_0$ is the **nugget**;
- $c$ is the **partial sill**;
- $c_0+c$ is the asymptotic sill;
- $a$ controls the distance scale of correlation.

A nugget can represent measurement error, unresolved microscale variation, or both. Those interpretations matter when predicting the latent process versus a future noisy observation.

For the exponential model above, $a$ is a scale parameter rather than a hard cutoff. The semivariogram approaches the sill asymptotically.

## Common Valid Models

### Exponential

$$
\gamma(h)=c_0+c\left(1-e^{-\|h\|/a}\right).
$$

### Gaussian

$$
\gamma(h)=c_0+c\left(1-e^{-(\|h\|/a)^2}\right).
$$

### Spherical

For $0<\|h\|\le a$,

$$
\gamma(h)
=
c_0+c
\left[
\frac{3}{2}\frac{\|h\|}{a}
-
\frac{1}{2}\left(\frac{\|h\|}{a}\right)^3
\right],
$$

and for $\|h\|>a$,

$$
\gamma(h)=c_0+c.
$$

A covariance/variogram function must satisfy mathematical validity conditions; not every visually convenient curve is a valid spatial dependence model.

## Anisotropy

Dependence may change with direction. For example, pollutant transport can be longer-ranged along prevailing wind direction than across it.

Directional empirical variograms can reveal anisotropy. Common models transform distance by rotation and axis-specific scaling before applying an isotropic covariance function.

## Sampling Design Matters

The empirical variogram is only informative over separations represented by the sample.

- dense short-range sampling helps estimate the nugget and near-origin behavior;
- broad spatial coverage helps estimate long-range structure;
- clustered sampling can overrepresent some distances;
- large holes in the sampling design produce weakly constrained predictions.

## Trend and Universal Kriging

If

$$
m(s)=x(s)^\top\beta
$$

varies with predictors or coordinates, forcing a constant-mean ordinary-kriging model can make the covariance absorb trend.

A better strategy is to model the mean and residual field together through universal kriging, regression kriging, or a spatial regression model.

## Diagnostics

A geostatistical workflow should inspect:

- raw maps and covariates;
- residual trend;
- directional dependence;
- empirical variogram stability;
- outliers;
- standardized prediction errors;
- sensitivity to the variogram family and fitting range.

The next chapter, [Kriging](kriging.md), turns the covariance/variogram model into spatial predictions.
