# Spatial Autocorrelation

Spatial autocorrelation asks whether values attached to locations are arranged more similarly or more dissimilarly than expected under a stated reference mechanism.

The statistic alone is not the model. Its interpretation depends on the spatial weights matrix and on the null hypothesis used for inference.

## Global Moran's I

Let

$$
z_i = x_i-\bar{x},
\qquad
S_0=\sum_i\sum_j w_{ij}.
$$

Global Moran's $I$ is

$$
I =
\frac{n}{S_0}
\frac{\sum_i\sum_j w_{ij}z_i z_j}
{\sum_i z_i^2}.
$$

Positive values indicate that connected observations tend to have deviations with the same sign. Negative values indicate that connected observations tend to have opposite-signed deviations.

### Moran's I is not generally bounded by -1 and 1

Unlike an ordinary Pearson correlation, the exact attainable range of Moran's $I$ depends on the spatial weights structure. It should therefore not be interpreted by mechanically applying the usual correlation bounds.

Under the common randomization null in which observed values are exchangeable over the fixed locations,

$$
E[I]=-\frac{1}{n-1}.
$$

Thus “no spatial autocorrelation” is not represented exactly by zero in finite samples.

## Permutation Inference

A transparent inferential strategy keeps the locations and $W$ fixed and repeatedly permutes the observed values across locations.

For $M$ permutations, a Monte Carlo pseudo-$p$ value can be computed as

$$
p = \frac{R+1}{M+1},
$$

where $R$ counts simulated statistics at least as extreme as the observed statistic according to the chosen one- or two-sided alternative.

Permutation inference tests a specific exchangeability/randomization null. It does not show that a process is stationary, causal, or correctly modeled.

The companion [`moran_permutation.py`](../../scripts/spatial_statistics/moran_permutation.py) implements Moran's $I$ and the permutation test from first principles.

## Geary's C

Geary's $C$ emphasizes squared neighbor differences:

$$
C =
\frac{n-1}{2S_0}
\frac{\sum_i\sum_j w_{ij}(x_i-x_j)^2}
{\sum_i(x_i-\bar{x})^2}.
$$

Under a common null reference, values near $1$ indicate little spatial autocorrelation, values below $1$ indicate positive spatial autocorrelation, and values above $1$ indicate negative spatial autocorrelation.

Because it uses pairwise differences, Geary's $C$ responds differently from Moran's cross-product statistic.

## Local Moran Statistics

A global statistic can hide local clusters and spatial outliers.

One common local Moran form is

$$
I_i =
\frac{z_i}{m_2}
\sum_j w_{ij}z_j,
\qquad
m_2=\frac{1}{n}\sum_i z_i^2.
$$

With row-standardized weights, the sign combination of $z_i$ and its spatial lag gives the familiar Moran-scatterplot categories:

- high-high;
- low-low;
- high-low;
- low-high.

A large local value is not automatically “significant.” Local statistics require their own reference distributions.

## Multiple Testing

Computing a local statistic at every location creates a multiple-testing problem. A map of unadjusted $p<0.05$ locations will contain false positives even under spatial randomness.

Possible responses include:

- false-discovery-rate control;
- family-wise adjustments;
- simulation envelopes;
- treating local maps as exploratory rather than confirmatory.

## First-Order Structure Can Mimic Dependence

Suppose

$$
X(s)=m(s)+\varepsilon(s)
$$

and the mean $m(s)$ changes smoothly across space. Nearby observations can look similar even if the residual process $\varepsilon(s)$ is independent.

Before interpreting a positive Moran statistic as residual spatial dependence, ask whether a broad trend, omitted covariate, or regional mean structure explains the pattern.

This distinction leads naturally to [spatial regression](spatial_regression.md) and [geostatistics](geostatistics.md).

## Moran Scatterplot

For centered values $z$, plot

$$
z_i
\quad \text{against} \quad
(Wz)_i.
$$

With row-standardized $W$, the slope of the appropriate standardized Moran scatterplot is closely related to global Moran's $I$. The plot is useful for diagnosing clusters and influential observations, but it does not replace formal inference.

## What Moran's I Does Not Tell You

A significant Moran statistic does not identify:

- the physical mechanism generating dependence;
- the correct spatial scale;
- whether a regression coefficient is causal;
- whether a geostatistical covariance model is valid;
- whether a point pattern is clustered.

Those are separate modeling questions.
