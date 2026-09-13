# Statistical Inference

Statistical inference uses a probability model and the sampling behavior of statistics to quantify uncertainty about populations or data-generating processes.

## Prerequisites

The most useful prerequisites are:

- **[Standard Error and the Law of Large Numbers](../basic_concepts/standard_error_and_lln.md)**;
- **[Probability Distributions](../probability_distributions/README.md)**, especially the normal curve and Central Limit Theorem.

## Suggested Reading Order

1. **[Confidence Intervals](confidence_intervals.md)** — estimation with uncertainty and repeated-sampling coverage.
2. **[Null and Alternative Hypotheses](null_hypothesis.md)** — the language of $H_0$, $H_a$, and p-values.
3. **[Hypothesis Testing](hypothesis_testing.md)** — the full testing workflow: statistic, reference distribution, p-value, decision, interpretation.
4. **[Type I and Type II Errors](type_i_and_type_ii_errors.md)** — false positives, false negatives, and the trade-off between them.
5. **[Multiple Comparisons](multiple_comparisons.md)** — what changes when many hypotheses are tested.
6. **[Analysis of Variance](analysis_of_variance.md)** — comparing group means through an F-based framework.
7. **[Analysis of Categorical Data](analysis_of_categorical_data.md)** — inference for counts and contingency tables.
8. **[Resampling](resampling.md)** — bootstrap/permutation ideas when analytic sampling distributions are inconvenient or when resampling provides a clearer route.

## Scope of the Two Hypothesis-Testing Notes

The two introductory testing chapters intentionally have different jobs:

- `null_hypothesis.md` focuses on the meaning and interpretation of hypotheses and p-values;
- `hypothesis_testing.md` focuses on the end-to-end procedure and common test structures.

Use the first for concepts and the second as the workflow reference rather than treating them as two competing introductions.

## Interpretation Principles

- A p-value is computed **assuming the null hypothesis**, not the probability that the null hypothesis is true.
- Failing to reject $H_0$ is not the same as proving or accepting $H_0$.
- Statistical significance does not measure effect size or practical importance.
- Confidence intervals and tests describe uncertainty under a model; poor sampling or model assumptions are not repaired by a small p-value.
- If many hypotheses are examined, account for multiplicity rather than interpreting each test in isolation.