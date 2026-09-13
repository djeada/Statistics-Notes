# Spatial Regression

Regression models a mean relationship. Spatial regression becomes necessary when location-dependent structure remains after the mean has been modeled.

A useful starting point is

$$
y = X\beta+\varepsilon,
$$

with

$$
E[\varepsilon]=0,
\qquad
\operatorname{Cov}(\varepsilon)=\Sigma.
$$

Ordinary least squares assumes, for its usual standard-error formulas, a much simpler covariance structure than many spatial datasets exhibit.

## Diagnose the Mean Before Adding a Spatial Model

Residual spatial autocorrelation can come from:

- omitted spatially varying predictors;
- an incorrect nonlinear mean function;
- regional fixed effects that were omitted;
- genuine residual spatial dependence.

Adding a spatial covariance model before checking the mean can make the dependence term absorb systematic trend.

## Generalized Least Squares

If $\Sigma$ is known,

$$
\hat\beta_{\mathrm{GLS}}
=
(X^\top\Sigma^{-1}X)^{-1}
X^\top\Sigma^{-1}y.
$$

This reduces to OLS when

$$
\Sigma=\sigma^2 I.
$$

In practice $\Sigma$ is not known and must be estimated or specified through a structured covariance model.

The script [`spatial_regression.py`](../../scripts/spatial_statistics/spatial_regression.py) simulates spatially correlated errors, diagnoses OLS residual autocorrelation with Moran's $I$, and compares OLS with GLS using the known simulation covariance only as a teaching device.

## Spatial Error Models

For areal data, a spatial error model can be written

$$
y=X\beta+u,
$$

$$
u=\lambda Wu+\varepsilon.
$$

Equivalently,

$$
u=(I-\lambda W)^{-1}\varepsilon.
$$

The spatial parameter describes dependence in the disturbance process. It does not mean neighboring outcomes directly cause one another.

## Spatial Lag / SAR Models

A spatial autoregressive outcome model is

$$
y=\rho Wy+X\beta+\varepsilon.
$$

Then

$$
y=(I-\rho W)^{-1}(X\beta+\varepsilon).
$$

Because $Wy$ is endogenous to the simultaneous system, fitting this model by ordinary OLS is generally inappropriate.

Interpretation also differs from ordinary regression: changing one predictor can propagate through the spatial multiplier, producing direct and indirect effects.

## Choosing Between Mean, Error, and Lag Structure

A Moran test on residuals can tell you that structure remains, but it does not uniquely choose a model.

Questions to ask include:

- Is there a missing spatial covariate or nonlinear trend?
- Is dependence better represented continuously by distance or discretely by $W$?
- Does the scientific mechanism imply outcome interaction or merely correlated disturbances?
- Are boundaries and neighboring units substantively meaningful?
- Is the goal prediction, association, or causal estimation?

## Spatial Confounding

Spatial predictors and latent spatial effects often vary on similar scales. Flexible spatial random effects can absorb variation that would otherwise be attributed to a spatially smooth predictor.

This can make coefficient estimates sensitive to:

- covariance range;
- basis functions;
- priors or penalties;
- spatial resolution;
- included covariates.

A coefficient is not made causal simply because spatial autocorrelation has been modeled.

## Residual Diagnostics

After fitting, inspect:

- residual map;
- residual Moran's $I$ under the chosen $W$;
- residual variogram for point-referenced data;
- heteroskedasticity;
- influential locations;
- predictive residuals under spatially structured validation.

## Prediction vs Parameter Inference

A model can predict well because location serves as a strong proxy for omitted processes while still giving a poor scientific interpretation of $\beta$.

Keep the prediction target and inferential target separate, and use [spatial validation](spatial_validation.md) for performance claims.
