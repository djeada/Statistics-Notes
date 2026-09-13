# Joint Distributions & Covariance

This unit moves from one random variable to several random variables considered together. It supplies the dependence concepts used later by regression, time series, and spatial statistics.

## Reading Order

1. **[Joint Distributions](joint_distributions.md)** — joint, marginal, and conditional distributions; independence; expectations of functions of several variables.
2. **[Covariance](covariance.md)** — signed linear co-variation and its algebraic properties.
3. **[Correlation](correlation.md)** — standardized linear association and rank-based monotonic association.

## Conceptual Boundaries

A joint distribution is the full probability model for variables considered together. Covariance and correlation are summaries of that joint structure; they do not replace it.

Zero covariance means no **linear** association, not necessarily independence. Independence implies zero covariance when the relevant moments exist, but the converse generally fails.

Correlation is symmetric in $X$ and $Y$. Regression, introduced later, is asymmetric because it models a response conditional on predictors.

## Next

Continue to **[Sampling & Sampling Distributions](../sampling_and_sampling_distributions/README.md)** for repeated-sample behavior, or keep this unit in mind as a prerequisite for **[Regression](../regression/README.md)**.
