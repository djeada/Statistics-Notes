# Kriging

Kriging is linear prediction under an explicit spatial covariance or variogram model. The word “best” in **best linear unbiased predictor** is conditional on the assumed mean structure and dependence model.

Kriging is therefore not a generic smoothing algorithm.

## Ordinary Kriging

Suppose measurements

$$
Z(s_1),\ldots,Z(s_n)
$$

come from a random field with an unknown constant mean.

Predict at unsampled location $s_0$ with

$$
\hat Z(s_0)
=
\sum_{i=1}^n \lambda_i Z(s_i).
$$

Unbiasedness for an unknown constant mean requires

$$
\sum_i \lambda_i=1.
$$

## Variogram System

Using a valid semivariogram $\gamma$, ordinary-kriging weights solve

$$
\begin{bmatrix}
\Gamma & \mathbf{1}\\
\mathbf{1}^\top & 0
\end{bmatrix}
\begin{bmatrix}
\lambda\\
\mu
\end{bmatrix}
=
\begin{bmatrix}
\gamma_0\\
1
\end{bmatrix},
$$

where

$$
\Gamma_{ij}=\gamma(s_i-s_j)
$$

and

$$
(\gamma_0)_i=\gamma(s_i-s_0).
$$

The prediction is

$$
\hat Z(s_0)=\lambda^\top z.
$$

With this sign convention for the Lagrange multiplier, the ordinary-kriging variance is

$$
\sigma_K^2(s_0)
=
\lambda^\top\gamma_0+\mu.
$$

Different texts may define the multiplier with the opposite sign. The equations and variance expression must use the same convention.

## Simple Kriging

If the mean $\mu$ is known,

$$
\hat Z(s_0)
=
\mu+c_0^\top C^{-1}(z-\mu\mathbf{1}),
$$

where $C$ is the observation covariance matrix and $c_0$ is covariance between the observations and target.

Simple kriging does not need the sum-to-one constraint because the mean is assumed known.

## Universal Kriging

If the mean varies as

$$
m(s)=f(s)^\top\beta,
$$

the kriging system includes constraints that preserve the trend basis. Universal kriging is appropriate when broad spatial structure is represented through coordinates or covariates rather than forced into the covariance.

## Interpolation and the Nugget

Whether kriging exactly reproduces an observed value depends on what the nugget represents and what is being predicted.

If the nugget is treated as microscale process variation, an exact interpolation convention may be reasonable for the observed process value. If it is known measurement error and the target is the latent error-free field, smoothing at sampled locations can be appropriate.

“Does kriging interpolate exactly?” therefore has no single answer without defining the target.

## Kriging Uncertainty

The kriging variance is determined by:

- sampling geometry;
- covariance/variogram parameters;
- target location;
- mean-model constraints.

Under the standard second-order framework, it does not depend directly on the observed data values after the covariance parameters are fixed.

Low kriging variance does not protect against a wrong trend model, wrong covariance family, unmodeled anisotropy, or a distributional misspecification.

## Cross-Validation

Leave-one-out diagnostics commonly examine

$$
e_i=Z(s_i)-\hat Z_{-i}(s_i)
$$

and standardized errors

$$
e_i^*
=
\frac{e_i}{\hat\sigma_{K,-i}(s_i)}.
$$

Useful summaries include:

- mean error near zero;
- RMSE;
- mean standardized error near zero;
- standardized-error spread near one;
- maps of residuals to reveal remaining spatial structure.

Leave-one-out prediction usually resembles **interpolation near existing samples**. It may be much too optimistic for prediction in a distant unsampled region. Use [spatial validation](spatial_validation.md) when geographic transfer is the actual task.

## Computational Scaling

Dense kriging with $n$ observations involves an $n\times n$ system and can become expensive as $n$ grows.

Large-data approaches include:

- local-neighborhood kriging;
- covariance tapering;
- low-rank basis models;
- sparse Gaussian Markov random fields;
- nearest-neighbor Gaussian processes;
- multi-resolution approximations.

The educational companion [`variogram_and_kriging.py`](../../scripts/spatial_statistics/variogram_and_kriging.py) implements empirical variograms and ordinary kriging directly with NumPy/SciPy.
