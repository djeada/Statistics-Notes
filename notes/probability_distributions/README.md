# Probability Distributions

Probability distributions connect the probability foundations in `basic_concepts` to the sampling models used in regression and statistical inference.

## Prerequisites

Read **[Introduction to Probability](../basic_concepts/introduction_to_probability.md)** and, ideally, **[Axioms of Probability](../basic_concepts/axioms_of_probability.md)** first.

## 1. Distribution Foundations

Read the introductory notes in this order:

1. **[Introduction to Distributions](intro/introduction_to_distributions.md)** — random variables, PMFs, PDFs, and CDFs.
2. **[Statistical Moments](intro/statistical_moments.md)** — expectation, variance, higher moments, and moment-generating functions.
3. **[Normal Curve and Z-Scores](intro/normal_curve_and_z_score.md)** — standardization and areas under the normal curve.
4. **[Central Limit Theorem](intro/central_limit_theorem.md)** — why normal approximations and standard errors appear throughout inference.

See **[intro/README.md](intro/README.md)** for the scope of each introductory note.

## 2. Discrete Families

Use **[discrete_distributions/README.md](discrete_distributions/README.md)** as a family-selection guide.

A useful progression is:

- **Binomial** — number of successes in a fixed number of Bernoulli trials.
- **Geometric** — number of trials until the first success.
- **Negative binomial** — number of trials until the $r$-th success.
- **Poisson** — number of events in an interval under a constant-rate Poisson model.

## 3. Continuous Families

Use **[continuous_distributions/README.md](continuous_distributions/README.md)** to choose among bounded, positive, symmetric, and inference-related families.

Particularly important connections are:

- exponential $\rightarrow$ gamma for waiting-time models;
- normal $\rightarrow$ log-normal after exponentiation;
- normal samples $\rightarrow$ Student's t, chi-square, and F reference distributions used in classical inference.

## PMF, PDF, and CDF

- A **PMF** assigns probabilities to possible values of a discrete random variable.
- A **PDF** assigns density to a continuous random variable; probabilities are areas/integrals, not pointwise density values.
- A **CDF**, $F(x)=P(X\le x)$, applies to either type.

## Parameterization Warning

Distribution names do not uniquely determine parameter conventions. Always check whether a source or software library uses a **rate** or **scale** parameter, and check whether a negative-binomial variable counts trials, failures, or successes. The formulas in each chapter define the convention used there.

## Next Steps

- **[Statistical Inference](../statistical_inference/README.md)** uses sampling distributions to quantify uncertainty.
- **[Correlation and Regression](../correlation_and_regression/README.md)** uses distributional assumptions to support regression inference and diagnostics.