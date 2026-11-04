# Theory: permutation tests

## The question a permutation test answers

You gave 5 people a new onboarding flow and 5 people the old one, and the new group was faster on average. Was that the
flow, or just which people landed in which group? A permutation test answers directly: **if the label did not matter, how often
would shuffling the labels produce a difference at least this large?** No normal distribution and no formula for a standard error
are needed - only the data and a computer. It prevents the failure of declaring victory because of a number that random assignment alone often produces.

## The logic

- **Null hypothesis (exchangeability):** the outcome of each participant would have been the same whichever group they were in, so every
  relabeling of the data is as likely as the one observed.
- **Test statistic** $T$: any number that measures the effect, e.g. $T = \bar x_{new} - \bar x_{old}$ (or a difference of medians, a ratio, a correlation).
- **Reference distribution:** compute $T$ for every relabeling. With $n_1 + n_2 = n$ people there are $\binom{n}{n_1}$ of them.
- **p-value:** the proportion of relabelings whose statistic is at least as extreme as the observed one:

$$
p = \frac{\#\{\text{labelings with } |T^*| \ge |T_{obs}|\}}{\binom{n}{n_1}}.
$$

The observed labeling is one of the labelings, so $p \ge 1/\binom{n}{n_1}$ and it is never exactly zero.

## Worked example (3 vs 3, computed)

Group A $=\{4,5,6\}$, group B $=\{7,9,11\}$: $\bar x_A = 5$, $\bar x_B = 9$, $T_{obs} = -4$. There are
$\binom{6}{3} = 20$ ways to choose which 3 values are called "A". Their mean differences take the values
$\pm 4,\ \pm 3.33,\ \pm 2.67,\ \pm 2,\ \pm 1.33,\ \pm 0.67,\ 0$; only two labelings reach $|T| \ge 4$
(the observed one and its mirror image). So $p = 2/20 = 0.10$ two-sided, or $0.05$ one-sided. The pooled t-test on the same
data gives $t = -3.10$, $p = 0.036$ - it "finds" an effect the exact test says is impossible to establish with 6 observations:
**the smallest two-sided p-value 3 vs 3 can produce is 0.10**.

## Exact versus Monte Carlo

$\binom{10}{5} = 252$ labelings are easy to enumerate in a spreadsheet (this lesson does exactly that). $\binom{20}{10} = 184\,756$ is
already too many for a sheet, and $\binom{100}{50} \approx 10^{29}$ is impossible. Then you draw $B$ random relabelings
(thousands, in code) and use

$$
\hat p = \frac{1 + \#\{|T^*_b| \ge |T_{obs}|\}}{B + 1},
$$

where the "+1" counts the observed labeling and keeps $\hat p > 0$. The Monte Carlo error is about $\sqrt{p(1-p)/B}$. In a
spreadsheet the random labelings must be pre-generated (see [Monte Carlo simulation](../20-monte-carlo-simulation/theory.md)) so that the answer is reproducible.

## Comparison with the t-test

The two-sample t-test computes the same kind of statistic but gets its reference distribution from a theoretical formula: it assumes
normal data (or enough data for the CLT) and, in the pooled version, equal variances. With large $n$ or well-behaved data the two p-values are close.
With small, skewed samples they can disagree in either direction. The permutation test is not "more powerful"; its advantage is
that its validity rests on **random assignment**, not on a distribution. In the lesson's data the t-test just clears 0.05 while the permutation test just misses.

## Two-sided, one-sided, and other statistics

Use two-sided counts $|T^*| \ge |T_{obs}|$ unless a direction was committed to *before* seeing the data. The same recipe tests any
statistic: difference of medians, difference of proportions (A/B tests, [lesson 19](../19-a-b-testing-and-effect-sizes/theory.md)),
correlation (shuffle one column), a difference of variances. Discrete statistics produce ties and coarse p-values (a median of 5 values takes few distinct values).

## Assumptions and pitfalls

1. **Exchangeability is not automatic.** It holds when units were *randomly assigned*; with observational groups (e.g. users who chose the new flow) the test is valid
   only for "no association", not for "no causal effect".
2. **The p-value is not the probability the null is true** nor the probability of the result being "chance"; it is a tail proportion computed under the null.
3. **Tiny samples have a floor on p** (see the 3 vs 3 example); say so instead of reporting "p = 0.00".
4. **Dependent observations** (repeated measures, time series) must be permuted in blocks or within subject; shuffling individual rows breaks the dependence.
5. **A single outlier** changes means a lot; choose the statistic (mean, median, trimmed mean) before looking at the data, and report the effect size, not just $p$.
6. Do not run many statistics until one passes: each one needs its own multiplicity correction.

## Connections

- Bootstrap (resampling *with* replacement, to estimate uncertainty) in [lesson 17](../17-bootstrapping-and-confidence-intervals/theory.md); permutation (resampling *without* replacement, to test a null).
- Sampling variability of a difference of means: [lesson 16](../16-sampling-distributions-and-the-clt/theory.md).
- Repo notes: [hypothesis testing](../../notes/hypothesis_testing_and_confidence_intervals/hypothesis_testing.md),
  [null hypothesis](../../notes/hypothesis_testing_and_confidence_intervals/null_hypothesis.md),
  [resampling](../../notes/resampling_and_model_assessment/resampling.md).
