# Hypothesis Testing & Confidence Intervals

This unit uses sampling distributions to quantify uncertainty and compare observed data with claims about population parameters or statistical models.

## Reading Order

1. **[Confidence Intervals](confidence_intervals.md)** — interval estimation and repeated-sampling coverage.
2. **[Null and Alternative Hypotheses](null_hypothesis.md)** — the meaning of $H_0$, $H_a$, and p-values.
3. **[Hypothesis Testing](hypothesis_testing.md)** — the full workflow: hypotheses, test statistic, reference distribution, p-value, decision, interpretation.
4. **[Type I and Type II Errors](type_i_and_type_ii_errors.md)** — false positives, false negatives, power, and the trade-offs created by a decision threshold.
5. **[Multiple Comparisons](multiple_comparisons.md)** — error control when many hypotheses are examined.
6. **[Analysis of Categorical Data](analysis_of_categorical_data.md)** — inference for counts, proportions, and contingency tables.

## Confidence Intervals and Tests Are Related

Both procedures use the sampling behavior of an estimator or test statistic. A two-sided test and a corresponding confidence interval often encode the same evidence in different forms: one asks whether a hypothesized value is plausible under a chosen error rate, while the other reports a range of parameter values compatible with the data under the procedure's assumptions.

Neither procedure repairs poor sampling, dependence that was ignored, model misspecification, or data-dependent analysis choices.

## Interpretation Principles

- A p-value is computed **assuming the null hypothesis**; it is not the probability that the null hypothesis is true.
- Failing to reject $H_0$ is not the same as proving or accepting $H_0$.
- Statistical significance is not the same as practical importance or large effect size.
- Confidence levels are properties of repeated-sampling procedures, not posterior probabilities for fixed parameters in the usual frequentist interpretation.
- Multiplicity matters when many hypotheses are tested or many analysis choices are explored.

## Where ANOVA Goes

ANOVA is organized with **[Regression](../regression/README.md)** rather than here because it is most coherent as a linear-model framework whose F tests are one inferential component. The sampling distribution and hypothesis-testing ideas required for ANOVA are learned in this unit first.

## Next

Continue to **[Regression](../regression/README.md)**.
