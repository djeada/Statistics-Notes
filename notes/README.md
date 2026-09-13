# Statistics Notes Curriculum

The `notes/` directory follows a learning dependency graph rather than grouping material only by historical topic names. The intended sequence is:

**Foundations → Probability → Random Variables & Distributions → Joint Distributions & Covariance → Sampling & Sampling Distributions → Estimation → Hypothesis Testing & Confidence Intervals → Regression → Resampling & Model Assessment → Time Series → Spatial Statistics → Extensions**

Each unit has a `README.md` that explains prerequisites, reading order, and the boundary between neighboring topics.

## Core Sequence

1. **[Foundations](foundations/README.md)** — what data, variables, populations, samples, and descriptive summaries are.
2. **[Probability](probability/README.md)** — how uncertainty is represented through events, probability laws, conditioning, and Bayes' theorem.
3. **[Random Variables & Distributions](random_variables_and_distributions/README.md)** — how numerical outcomes are represented by random variables and probability distributions.
4. **[Joint Distributions & Covariance](joint_distributions_and_covariance/README.md)** — how several random variables are modeled together and how dependence is summarized.
5. **[Sampling & Sampling Distributions](sampling_and_sampling_distributions/README.md)** — how statistics vary from sample to sample and why standard errors and limiting distributions matter.
6. **[Estimation](estimation/README.md)** — how unknown population parameters are estimated from data.
7. **[Hypothesis Testing & Confidence Intervals](hypothesis_testing_and_confidence_intervals/README.md)** — how uncertainty is converted into intervals, tests, error rates, and inferential decisions.
8. **[Regression](regression/README.md)** — how conditional means or probabilities are modeled using predictors.
9. **[Resampling & Model Assessment](resampling_and_model_assessment/README.md)** — how uncertainty and predictive performance are assessed with resampling, validation, and metrics.
10. **[Time Series](time_series/README.md)** — how modeling changes when observations are ordered in time and serially dependent.
11. **[Spatial Statistics](spatial_statistics/README.md)** — how modeling changes when dependence is structured by location.
12. **[Extensions](extensions/README.md)** — broader inferential perspectives and topics that do not belong to the main prerequisite chain.

## Why This Split

The most important boundaries are conceptual, not administrative:

- probability describes events before random variables attach numbers to those events;
- a univariate distribution comes before joint distributions and covariance;
- a population distribution is different from a sampling distribution of a statistic;
- sampling behavior comes before estimation, confidence intervals, and tests;
- fitting a model is different from evaluating how well it generalizes;
- time-series and spatial methods extend the core material by relaxing independent-observation assumptions.

This structure also prevents common terms from being introduced in the wrong place. For example, the Student's t, chi-square, and F distributions are taught with sampling distributions because that is where their inferential role becomes meaningful; covariance and correlation are taught before regression because regression builds on multivariate dependence rather than defining it.

## Navigation Rules

Section READMEs are the canonical entry points. Individual chapters should focus on their own topic rather than repeating an entire prerequisite chain. Cross-links should point backward to prerequisites and forward to the most natural next unit.

Shared notation, terminology, and document conventions are in **[CONVENTIONS.md](CONVENTIONS.md)**.
