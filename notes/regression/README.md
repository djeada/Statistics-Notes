# Regression

Regression models a response variable conditionally on one or more predictors. This unit builds on joint distributions, estimation, confidence intervals, and hypothesis testing.

## Prerequisites

- **[Joint Distributions & Covariance](../joint_distributions_and_covariance/README.md)** for covariance, correlation, and conditional distributions.
- **[Estimation](../estimation/README.md)** for estimator concepts.
- **[Hypothesis Testing & Confidence Intervals](../hypothesis_testing_and_confidence_intervals/README.md)** for standard errors, intervals, tests, and F/t reference distributions.

## Reading Order

1. **[Simple Linear Regression](simple_linear_regression.md)** — one predictor, least squares, residuals, fit, and slope inference.
2. **[Multiple Regression](multiple_regression.md)** — several predictors, partial effects, confounding, multicollinearity, and model interpretation.
3. **[Analysis of Variance](analysis_of_variance.md)** — group comparisons understood through sums of squares and F tests; closely related to linear regression.
4. **[Logistic Regression](logistic_regression.md)** — conditional probabilities for binary outcomes using a generalized linear-model perspective.

## Conceptual Boundaries

**Correlation is not regression.** Correlation is symmetric; regression distinguishes response and predictors and models a conditional quantity such as $E[Y\mid X=x]$ or $P(Y=1\mid X=x)$.

**Residuals are not errors.** Model errors are unobserved random variables; residuals are computed after fitting and are used for diagnostics.

**Fitting is not model assessment.** A model can fit the observed sample well and still generalize poorly. Out-of-sample validation, cross-validation, model-selection cautions, and predictive metrics live in **[Resampling & Model Assessment](../resampling_and_model_assessment/README.md)**.

**Association is not causation.** Regression coefficients become causal only under a suitable design or explicit causal assumptions.

## Next

Continue to **[Resampling & Model Assessment](../resampling_and_model_assessment/README.md)** before moving to dependent-data models such as time series.
