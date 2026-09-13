# Correlation and Regression

This section moves from symmetric measures of association to models with an explicit response variable.

## Suggested Reading Order

1. **[Covariance](covariance.md)** — how two variables vary together and why units matter.
2. **[Correlation](correlation.md)** — standardized linear association and rank-based monotonic association.
3. **[Simple Linear Regression](simple_linear_regression.md)** — one predictor, least squares, residuals, fit, and slope inference.
4. **[Multiple Regression](multiple_regression.md)** — several predictors and the interpretation challenges that follow.
5. **[Logistic Regression](logistic_regression.md)** — regression for binary outcomes.
6. **[Metrics](metrics.md)** — evaluate fitted or predictive models with metrics appropriate to the task.

## Conceptual Boundaries

**Correlation is symmetric; regression is not.** Correlation asks how two variables move together. Regression distinguishes a response from one or more predictors and models a conditional mean or probability.

**Association is not causation.** A regression coefficient or strong correlation does not become causal merely because it is statistically significant. Causal interpretation requires an appropriate design or explicit causal assumptions.

**Computation and inference have different assumptions.** Pearson's $r$ and ordinary least squares estimates can be computed without normal marginal data. Distributional assumptions become relevant when deriving particular standard errors, confidence intervals, or hypothesis tests. In the classical linear model, normal errors are primarily an exact small-sample inference assumption, not a prerequisite for drawing the least-squares line.

## Connections

- Review **[Statistical Moments](../probability_distributions/intro/statistical_moments.md)** before covariance.
- Use **[Statistical Inference](../statistical_inference/README.md)** for the general logic behind confidence intervals, tests, multiple comparisons, and resampling.
- In time-indexed regression, independent-error assumptions may fail; see **[Regression with ARMA Errors](../time_series_analysis/regression_with_arma_errors.md)**.