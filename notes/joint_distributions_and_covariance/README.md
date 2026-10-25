# Joint Distributions and Covariance

A joint distribution describes several random variables together. It answers questions about combinations of outcomes, such as the probability that demand is high while supply is low. Marginal distributions describe each variable separately; conditional distributions describe one variable after another is known.

## Full models and numerical summaries

Two joint distributions can have identical marginals and different dependence. Knowing individual means and variances therefore does not determine the probability of a joint event. Independence supplies a particular factorization of the joint distribution, rather than a conclusion that can be inferred from similar marginal shapes.

Covariance averages the product of centered deviations. Its sign indicates whether large values of the two variables tend to occur together or in opposite directions. Its magnitude depends on measurement units. Pearson correlation divides by both standard deviations to produce a dimensionless measure of linear association.

Neither summary records every kind of dependence. A symmetric variable and its square can have zero covariance while being deterministically related. Rank correlations address monotonic association, but they also cannot replace the full joint model.

## Why dependence matters

The variance of a sum includes covariance terms, so dependence changes the uncertainty of averages, portfolios, and combined measurements. Regression uses conditional structure to model a response given predictors. Time-series and spatial models extend the same idea to measurements separated by time or location. These applications require distinguishing independence, zero covariance, and a particular fitted relationship rather than treating them as interchangeable.
