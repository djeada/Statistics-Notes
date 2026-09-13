# Statistics Notes

This repository combines conceptual notes, Python implementations, notebooks, exercises, and flashcards for learning statistics. The notes are organized as a dependency-aware curriculum: probability comes before random variables, sampling comes before inference, and model assessment comes after model fitting.

## Learning Path

The main curriculum lives in [`notes/`](notes/README.md):

| Unit | Purpose |
|---|---|
| [Foundations](notes/foundations/README.md) | Statistical vocabulary, data, populations, samples, and descriptive summaries. |
| [Probability](notes/probability/README.md) | Events, axioms, conditioning, Bayes' theorem, and probability calculations. |
| [Random Variables & Distributions](notes/random_variables_and_distributions/README.md) | Random variables, moments, PMFs/PDFs/CDFs, and common distribution families. |
| [Joint Distributions & Covariance](notes/joint_distributions_and_covariance/README.md) | Multivariate distributions, marginal/conditional structure, covariance, and correlation. |
| [Sampling & Sampling Distributions](notes/sampling_and_sampling_distributions/README.md) | Law of large numbers, standard error, CLT, and reference distributions. |
| [Estimation](notes/estimation/README.md) | Point estimators, bias, variance, consistency, method of moments, and likelihood. |
| [Hypothesis Testing & Confidence Intervals](notes/hypothesis_testing_and_confidence_intervals/README.md) | Interval estimation, tests, errors, multiplicity, and categorical-data inference. |
| [Regression](notes/regression/README.md) | Linear models, ANOVA, multiple regression, and logistic regression. |
| [Resampling & Model Assessment](notes/resampling_and_model_assessment/README.md) | Bootstrap/permutation ideas, validation, model selection, and predictive metrics. |
| [Time Series](notes/time_series/README.md) | Serial dependence, stationarity, AR/MA/ARIMA models, diagnostics, and forecasting. |
| [Spatial Statistics](notes/spatial_statistics/README.md) | Spatial autocorrelation, geostatistics, and point processes. |
| [Extensions](notes/extensions/README.md) | Cross-cutting perspectives and topics beyond the main sequence. |

The shared notation and writing rules are documented in [`notes/CONVENTIONS.md`](notes/CONVENTIONS.md).

## Repository Layout

- [`notes/`](notes/README.md) — the conceptual curriculum.
- [`scripts/`](scripts/) — small Python implementations and demonstrations.
- [`notebooks/`](notebooks/) — interactive examples and visualizations.
- [`exercises/`](exercises/) — practice material.
- [`flashcards/`](flashcards/) — compact review prompts.
- [`assets/`](assets/) — local figures used by the notes.

The notes are organized pedagogically. The implementation folders retain their existing topic-oriented layout, so there is not always a one-to-one directory-name match between `notes/` and `scripts/` or `notebooks/`.

## Getting Started

Create and activate a virtual environment, then install the dependencies:

```bash
python3 -m venv env
source env/bin/activate        # Unix/macOS
# env\Scripts\activate         # Windows
pip install -r requirements.txt
```

Then run an implementation directly, for example:

```bash
python scripts/basic_concepts/averages.py
```

Or open one of the notebooks in [`notebooks/`](notebooks/).

## Suggested Study Workflow

Read the README for the current curriculum unit first. It explains prerequisites, reading order, and conceptual boundaries. Then read the individual note, reproduce a worked example, and use the matching script or notebook when one exists. Exercises and flashcards are most useful after the conceptual pass rather than as a substitute for it.

The curriculum is intentionally layered: later sections may use results from earlier sections without re-deriving them. When a topic feels abrupt, follow the prerequisite links in its section README before continuing.
