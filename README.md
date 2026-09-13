# Statistics Notes

A dependency-aware statistics curriculum with conceptual notes, runnable Python examples, interactive notebooks, exercises, quizzes, and flashcards.

The repository is organized around **how statistical ideas depend on one another**, not around historical folder names. The three primary learning layers now share the same unit structure:

- **[`notes/`](notes/README.md)** — concepts, derivations, assumptions, and interpretation;
- **[`scripts/`](scripts/README.md)** — small standalone implementations and simulations;
- **[`notebooks/`](notebooks/README.md)** — interactive experiments, repeated sampling, and model exploration.

## Curriculum

| # | Unit | Notes | Scripts | Notebooks |
|---:|---|---|---|---|
| 1 | Foundations | [read](notes/foundations/README.md) | [run](scripts/foundations/) | [explore](notebooks/foundations/) |
| 2 | Probability | [read](notes/probability/README.md) | [run](scripts/probability/) | [explore](notebooks/probability/) |
| 3 | Random Variables & Distributions | [read](notes/random_variables_and_distributions/README.md) | [run](scripts/random_variables_and_distributions/) | [explore](notebooks/random_variables_and_distributions/) |
| 4 | Joint Distributions & Covariance | [read](notes/joint_distributions_and_covariance/README.md) | [run](scripts/joint_distributions_and_covariance/) | [explore](notebooks/joint_distributions_and_covariance/) |
| 5 | Sampling & Sampling Distributions | [read](notes/sampling_and_sampling_distributions/README.md) | [run](scripts/sampling_and_sampling_distributions/) | [explore](notebooks/sampling_and_sampling_distributions/) |
| 6 | Estimation | [read](notes/estimation/README.md) | [run](scripts/estimation/) | [explore](notebooks/estimation/) |
| 7 | Hypothesis Testing & Confidence Intervals | [read](notes/hypothesis_testing_and_confidence_intervals/README.md) | [run](scripts/hypothesis_testing_and_confidence_intervals/) | [explore](notebooks/hypothesis_testing_and_confidence_intervals/) |
| 8 | Regression | [read](notes/regression/README.md) | [run](scripts/regression/) | [explore](notebooks/regression/) |
| 9 | Resampling & Model Assessment | [read](notes/resampling_and_model_assessment/README.md) | [run](scripts/resampling_and_model_assessment/) | [explore](notebooks/resampling_and_model_assessment/) |
| 10 | Time Series | [read](notes/time_series/README.md) | [run](scripts/time_series/) | [explore](notebooks/time_series/) |
| 11 | Spatial Statistics | [read](notes/spatial_statistics/README.md) | [run](scripts/spatial_statistics/) | [explore](notebooks/spatial_statistics/) |
| 12 | Extensions | [read](notes/extensions/README.md) | [run](scripts/extensions/) | [explore](notebooks/extensions/) |

The intended learning sequence is:

**Foundations → Probability → Random Variables & Distributions → Joint Distributions & Covariance → Sampling & Sampling Distributions → Estimation → Hypothesis Testing & Confidence Intervals → Regression → Resampling & Model Assessment → Time Series → Spatial Statistics → Extensions**

## How to Use the Repository

For a new unit, use the same three-step loop:

1. **Read the unit README and notes.** Learn the definitions, assumptions, equations, and interpretation before treating software output as meaningful.
2. **Run a small script.** Scripts isolate one idea at a time and make numerical behavior reproducible.
3. **Open a notebook.** Use notebooks for simulation, repeated sampling, visual exploration, and comparing modeling choices.

Then use [`exercises/`](exercises/) for practice and [`flashcards/`](flashcards/) / [`quizzes/`](quizzes/) for retrieval.

### Example: estimation

```bash
python scripts/estimation/point_estimation.py
```

Then open:

```text
notebooks/estimation/point_estimation.ipynb
```

The note that explains the statistical ideas is:

```text
notes/estimation/point_estimation.md
```

### Example: forecast evaluation

```bash
python scripts/time_series/forecast_backtesting.py
```

Pair it with:

- [`notes/time_series/forecast_evaluation.md`](notes/time_series/forecast_evaluation.md)
- [`notebooks/time_series/forecast_backtesting.ipynb`](notebooks/time_series/forecast_backtesting.ipynb)

## Why the Curriculum Is Split This Way

Several distinctions are easy to blur when statistics is organized as a flat list of topics:

- **Probability vs random variables:** probability assigns mass to events; random variables map outcomes to numerical values.
- **Population vs sampling distributions:** the distribution of observations is not the same object as the distribution of a statistic across repeated samples.
- **Estimation vs inference:** an estimator produces a value; confidence intervals and tests quantify uncertainty around claims using sampling behavior.
- **Dependence vs regression:** covariance and correlation describe joint variation before regression introduces a conditional model.
- **Fitting vs assessment:** a model can fit training data well and still generalize poorly; validation belongs after fitting and must avoid leakage.
- **Independent vs dependent data:** time-series and spatial methods require evaluation schemes that preserve temporal or spatial structure.

This is why Student's t, chi-square, and F are placed with sampling distributions, ANOVA is placed with regression, and predictive metrics are placed with model assessment.

## Coverage Highlights

The implementation layer now includes focused examples for concepts that previously existed only as prose:

- joint, marginal, and conditional distributions;
- sampling distributions and standard errors;
- point estimation, bias, variance, MSE, method of moments, and maximum likelihood;
- leakage-safe validation and model selection;
- expanding-window time-series backtesting;
- dynamic regression with serially correlated errors;
- VAR, Granger predictability, cointegration, and VECM;
- Kalman filtering and state-space ideas;
- frequency-domain analysis with periodograms;
- spatial block validation for dependent observations.

## Repository Layout

```text
Statistics-Notes/
├── notes/          # conceptual curriculum
├── scripts/        # standalone executable examples
├── notebooks/      # interactive companions
├── exercises/      # practice problems
├── flashcards/     # compact retrieval prompts
├── quizzes/        # self-check questions
├── assets/         # figures used by notes
└── requirements.txt
```

The first three directories use the **same curriculum unit names**, so moving from explanation to code does not require translating between different taxonomies.

## Environment Setup

Python examples use NumPy, SciPy, pandas, matplotlib, statsmodels, scikit-learn, SymPy, and Jupyter as listed in [`requirements.txt`](requirements.txt).

Create a virtual environment:

```bash
python3 -m venv env
```

Activate it:

```bash
# Unix / macOS
source env/bin/activate

# Windows
# env\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run a script:

```bash
python scripts/joint_distributions_and_covariance/joint_distributions.py
```

Or start Jupyter:

```bash
jupyter notebook
```

## Reproducibility and Conventions

New simulation examples use explicit random-number generators and deterministic seeds where practical. Model-assessment examples keep preprocessing and model selection inside the training/development process and reserve final test data for final evaluation.

Shared notation and writing conventions for the conceptual material are documented in [`notes/CONVENTIONS.md`](notes/CONVENTIONS.md).

## Contributing

When adding a new topic:

1. place the conceptual explanation in the curriculum unit where its prerequisites naturally lead;
2. add a small script when a numerical demonstration clarifies the idea;
3. add a notebook when interactivity, simulation, or richer exploration materially helps;
4. link the three layers using relative paths;
5. preserve the distinction between fitting, inference, and evaluation rather than duplicating the same material across units.

The goal is not to give every note a notebook mechanically. The goal is a coherent learning path in which implementations appear where computation adds understanding.
