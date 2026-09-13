# Sampling & Sampling Distributions

This unit is the bridge from probability models to statistical inference. It asks what happens to a statistic when the sampling process is repeated.

## Reading Order

1. **[Standard Error and the Law of Large Numbers](standard_error_and_lln.md)** — repeated-sample stability and the scale of sampling variability.
2. **[Sampling Distributions](sampling_distributions.md)** — statistics as random variables, sampling distributions, standard errors, bias, and exact versus asymptotic reference distributions.
3. **[Central Limit Theorem](central_limit_theorem.md)** — why standardized sums and sample means often become approximately normal.
4. **[Student's t Distribution](student_t_distribution.md)** — reference distribution for standardized estimates when variance is estimated.
5. **[Chi-Square Distribution](chi_square_distribution.md)** — reference distribution for sums of squared standard normals and normal-sample variance calculations.
6. **[F Distribution](f_distribution.md)** — ratio of scaled chi-square variables, used in ANOVA and regression inference.

## Population Distribution vs Sampling Distribution

These are different objects. A population distribution describes individual observations such as $X$. A sampling distribution describes a statistic such as $\bar X$, $S^2$, or a fitted coefficient over hypothetical repeated samples.

That distinction is what gives meaning to a **standard error**: it is the standard deviation of a statistic's sampling distribution (or an estimate of that quantity), not the standard deviation of the raw observations.

## Why t, Chi-Square, and F Live Here

These distributions can be studied abstractly, but in this repository they are most useful as distributions of standardized statistics under particular assumptions. Teaching them here makes later confidence intervals, tests, ANOVA, and regression inference depend on concepts already introduced rather than on unexplained lookup tables.

## Next

Continue to **[Estimation](../estimation/README.md)**.
