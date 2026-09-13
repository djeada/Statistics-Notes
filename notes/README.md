# Statistics Notes Curriculum

The `notes/` directory follows a learning dependency graph rather than grouping material only by historical topic names:

**Foundations → Probability → Random Variables & Distributions → Joint Distributions & Covariance → Sampling & Sampling Distributions → Estimation → Hypothesis Testing & Confidence Intervals → Regression → Resampling & Model Assessment → Time Series → Spatial Statistics → Extensions**

Each unit has a `README.md` that explains prerequisites, reading order, and the boundary between neighboring topics.

## Core Sequence

1. **[Foundations](foundations/README.md)** — data, variables, populations, samples, and descriptive summaries.
2. **[Probability](probability/README.md)** — events, probability laws, conditioning, and Bayes' theorem.
3. **[Random Variables & Distributions](random_variables_and_distributions/README.md)** — numerical outcomes, PMFs/PDFs/CDFs, moments, and common distribution families.
4. **[Joint Distributions & Covariance](joint_distributions_and_covariance/README.md)** — multivariate distributions, conditional structure, covariance, and correlation.
5. **[Sampling & Sampling Distributions](sampling_and_sampling_distributions/README.md)** — repeated-sampling behavior, standard errors, CLT, and reference distributions.
6. **[Estimation](estimation/README.md)** — point estimators, bias, variance, consistency, method of moments, and likelihood.
7. **[Hypothesis Testing & Confidence Intervals](hypothesis_testing_and_confidence_intervals/README.md)** — intervals, tests, error rates, multiplicity, and inferential decisions.
8. **[Regression](regression/README.md)** — linear models, ANOVA, multiple regression, and logistic regression.
9. **[Resampling & Model Assessment](resampling_and_model_assessment/README.md)** — bootstrap/permutation ideas, validation, model selection, leakage, and metrics.
10. **[Time Series](time_series/README.md)** — serial dependence, stationarity, forecasting, dynamic regression, multivariate systems, state space, and spectra.
11. **[Spatial Statistics](spatial_statistics/README.md)** — spatial dependence, geostatistics, point processes, and spatially aware validation.
12. **[Extensions](extensions/README.md)** — broader inferential perspectives that do not belong to the main prerequisite chain.

## Companion Layers

The implementation layers mirror the same unit names and order:

- [`scripts/`](../scripts/README.md) contains small runnable demonstrations;
- [`notebooks/`](../notebooks/README.md) contains interactive simulations and model explorations.

Use the unit name to move horizontally between explanation, runnable example, and notebook. For example, **Estimation** is available at `notes/estimation/`, `scripts/estimation/`, and `notebooks/estimation/`.

## Why This Split

The important boundaries are conceptual:

- probability describes events before random variables attach numbers to those events;
- univariate distributions come before joint distributions and covariance;
- a population distribution differs from the sampling distribution of a statistic;
- sampling behavior comes before estimation, confidence intervals, and tests;
- fitting a model differs from evaluating how well it generalizes;
- time-series and spatial methods extend the core material by relaxing independent-observation assumptions.

Student's t, chi-square, and F live with sampling distributions because that is where their inferential role becomes meaningful. Covariance and correlation come before regression because regression builds on multivariate dependence rather than defining it.

## Navigation Rules

Section READMEs are the canonical entry points. Individual chapters should focus on their topic rather than repeat the whole prerequisite chain. Cross-links should point backward to prerequisites and forward to the most natural next unit.

Shared notation, terminology, and document conventions are in **[CONVENTIONS.md](CONVENTIONS.md)**.
