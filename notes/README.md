# Statistics Notes Learning Map

The `notes/` directory is organized as a dependency-aware learning path rather than as six unrelated folders. Individual chapters can still be read on their own, but the section indexes below make prerequisites, conceptual boundaries, and useful next steps explicit.

## Recommended Path

1. **[Basic Concepts](basic_concepts/README.md)** — populations and samples, descriptive statistics, probability, conditional probability, Bayes' theorem, and the law of large numbers.
2. **[Probability Distributions](probability_distributions/README.md)** — random variables, PMFs/PDFs/CDFs, moments, common discrete and continuous families, and the Central Limit Theorem.
3. **[Statistical Inference](statistical_inference/README.md)** — confidence intervals, hypotheses, tests, errors, multiple comparisons, ANOVA, categorical-data analysis, and resampling.
4. **[Correlation and Regression](correlation_and_regression/README.md)** — covariance, correlation, linear models, logistic regression, and model-performance metrics. The descriptive parts can be read earlier, but the inferential parts build on confidence intervals and hypothesis testing.
5. **Dependent-data extensions** — **[Time Series Analysis](time_series_analysis/README.md)** for dependence across time and **[Spatial Statistics](spatial_statistics/README.md)** for dependence across space.

This order is not the only valid route. A reader interested mainly in prediction can move from probability distributions into regression earlier, then return to statistical inference before interpreting coefficient tests or confidence intervals.

## How the Sections Fit Together

| Question | Start here | Why |
|---|---|---|
| How do I summarize observed data? | [Basic Concepts](basic_concepts/README.md) | Descriptive statistics and sampling vocabulary come first. |
| How do I model randomness? | [Probability Distributions](probability_distributions/README.md) | Random variables and distributions provide the probability models used later. |
| How do I generalize from a sample to a population? | [Statistical Inference](statistical_inference/README.md) | Sampling distributions, uncertainty, tests, and intervals are the core tools. |
| How do two or more variables relate or predict one another? | [Correlation and Regression](correlation_and_regression/README.md) | Covariance, association, prediction, and regression live here. |
| What changes when observations are dependent? | [Time Series Analysis](time_series_analysis/README.md), [Spatial Statistics](spatial_statistics/README.md) | Ordinary independent-sample intuition must be adapted to serial or spatial dependence. |

## Shared Conventions

The notes use the notation and writing conventions in **[CONVENTIONS.md](CONVENTIONS.md)**. The most important distinctions are:

- probability is not probability density;
- a population parameter is not the same object as its sample estimate;
- an error term is not the same object as a fitted residual;
- correlation or predictive association does not by itself establish causation;
- assumptions needed to compute a statistic should be distinguished from assumptions needed for a particular inferential procedure.

When a chapter introduces a specialized convention, that local convention should be stated explicitly.