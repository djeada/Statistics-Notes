# Hypothesis Testing and Confidence Intervals

Inference connects an observed statistic to uncertainty about a population or statistical model. A confidence interval reports a set of parameter values obtained by a procedure with a specified coverage rate. A hypothesis test compares the observed statistic with what a null model predicts and controls an error rate through its decision rule.

## The same sampling model supports both tasks

An estimate alone does not show how surprising its distance from a hypothesized value is. The relevant distance depends on its sampling variability. Dividing an estimated difference by a standard error produces a statistic that can be compared with a reference distribution, provided the model and sampling assumptions justify that distribution.

For matched procedures, a two-sided level-$\alpha$ test rejects exactly those parameter values excluded by its corresponding $100(1-\alpha)\%$ confidence set. This relationship follows by inverting the tests. It should not be assumed when an interval and a test use different approximations, standard errors, or tail conventions.

## Interpreting evidence and decisions

A p-value describes a tail probability under the null model, including nuisance assumptions and the chosen statistic. It does not assign a probability to the truth of that model. Failing to reject can reflect weak information, while rejecting can reflect a small effect measured precisely. Effect sizes and intervals help distinguish those situations.

Type I error is rejection when the null is true. Type II error is failure to reject at a specified alternative. Power depends on that alternative, sample size, variability, and the decision threshold. Examining many hypotheses creates more opportunities for false discoveries, so the family of questions and the error criterion must be specified.

## Counts and group comparisons

Categorical outcomes lead to inference for proportions and contingency-table probabilities. Expected counts under a null model determine whether an asymptotic chi-square approximation is suitable. ANOVA uses a linear model and an F statistic to compare group means through explained and unexplained variability. Both examples rely on the same principle: the null distribution must correspond to the way the data were generated and analyzed.

No inferential calculation repairs systematic selection bias or unmodeled dependence. Its uncertainty statement applies to the stated sampling or probability model, rather than to every possible source of error in the study.
