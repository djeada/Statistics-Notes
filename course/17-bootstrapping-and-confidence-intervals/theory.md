# Theory: bootstrapping and confidence intervals

## The problem: one sample, no repeat experiments

You measured 30 tickets and the mean is 9.4 hours. How far could the *true* mean be from that? Classical statistics answers
with a formula built on assumptions (normal data, or a sample large enough for the CLT, see
[sampling distributions](../16-sampling-distributions-and-the-clt/theory.md)). The **bootstrap** answers with a
computer: treat the sample as a stand-in for the population, redraw samples from it, and watch how much the statistic
moves. It works for statistics that have no convenient formula (median, percentile, ratio, trimmed mean).

## The percentile bootstrap

Given data $x_1,\dots,x_n$ and a statistic $\hat\theta = T(x_1,\dots,x_n)$:

1. Draw $n$ values **with replacement** from the data: a *resample* $x^*_1,\dots,x^*_n$ (some points appear twice, some not at all).
2. Compute $\hat\theta^* = T(x^*_1,\dots,x^*_n)$.
3. Repeat $B$ times to get $\hat\theta^*_1,\dots,\hat\theta^*_B$.

The distribution of $\hat\theta^*$ approximates the sampling distribution of $\hat\theta$. Then:

- **bootstrap standard error**: $\widehat{SE}_{boot} = \text{sd}(\hat\theta^*_1,\dots,\hat\theta^*_B)$;
- **percentile interval** with confidence $1-\alpha$: $[\,q_{\alpha/2},\ q_{1-\alpha/2}\,]$, the empirical quantiles of the $\hat\theta^*$ values.

In a spreadsheet no `RAND` is needed: pre-generate an index table (row = resample, column = position, entry = which observation
to take), look values up with `INDEX`, and use `AVERAGE`, `MEDIAN` or `PERCENTILE` on the resulting rows. That is exactly
what the *Resamples* sheet of the solution does, and why the answers never change when you recalculate.

## The classical interval for comparison

For a mean, $\bar x \pm t_{n-1,\,1-\alpha/2}\; s/\sqrt n$ (`TINV(alpha, n-1)` in Excel and Sheets, which is two-sided).
It assumes the sample mean is approximately normal and is **always symmetric** around $\bar x$.

## Worked example ($n = 5$, computed)

Data $\{4, 6, 7, 9, 14\}$: $\bar x = 8$, $s = 3.808$, $s/\sqrt n = 1.703$, $t_{4,0.975} = 2.776$, so the t interval is
$8 \pm 4.73 = [3.27,\ 12.73]$. Three example resamples: $\{7,4,7,14,9\}$ has mean 8.2, $\{14,14,6,9,4\}$ has mean 9.4,
$\{4,6,6,7,9\}$ has mean 6.4. With $B = 2000$ resamples the bootstrap standard error is about 1.51 (the plug-in value is
$\sqrt{(n-1)/n}\,s/\sqrt n = 1.52$) and the percentile interval is about $[5.4,\ 11.0]$. Notice what happened: the
bootstrap interval is **narrower** than the t interval, and shifted up. With $n=5$ the percentile bootstrap does not pay the
price for estimating $\sigma$ that the t quantile builds in, so it tends to be too optimistic. The bootstrap is not magic for tiny samples.

## What "95 %" means

A 95 % interval is the output of a **procedure**: if you repeated the whole study many times and built an interval each
time, about 95 % of those intervals would contain the true value. For *this* interval the truth is either inside or
not; saying "there is a 95 % probability that the true mean lies in $[7.0, 12.4]$" is a Bayesian statement the frequentist
interval does not make. Width, not coverage, is what you control with $n$: halving the width needs about four times the data.

## Assumptions

- Observations are **independent** and drawn from the population you care about (a biased sample bootstraps to a biased answer).
- The sample is large and representative enough to mimic the population; the bootstrap cannot add information that
  is not in the data.
- The statistic is *smooth enough*: means, medians (with mild caveats), percentiles in the body of the distribution.

## When it fails and common pitfalls

1. **Extremes**: the bootstrap of the maximum or of P99.9 is wrong - a resample can never exceed the observed maximum
   (see [percentiles and extreme values](../03-percentiles-and-extreme-values/theory.md)).
2. **Tiny $n$ or heavy tails**: percentile intervals under-cover (see the example above); with $n < 15$ prefer exact methods.
3. **Dependent data**: resampling individual points from an autocorrelated series destroys the dependence; use block
   bootstrap.
4. **Too few resamples**: $B = 400$ fits a spreadsheet, but the interval ends are still noisy (they move by tenths of an hour); use at least 1000-10000 in code.
5. **Skew**: with right-skewed data the bootstrap interval is asymmetric (long upper arm). Forcing a symmetric interval hides
   how high the true mean could plausibly be.
6. Confusing the **standard deviation of the data** (spread of individuals) with the **standard error** (uncertainty of the estimate).

## Connections

- The bootstrap distribution is an empirical [sampling distribution](../16-sampling-distributions-and-the-clt/theory.md).
- [Permutation tests](../18-permutation-tests/theory.md) resample *without* replacement to test a hypothesis; the
  bootstrap resamples *with* replacement to estimate uncertainty.
- [Robust statistics](../02-robust-statistics/theory.md) provides the medians and trimmed means whose uncertainty only the bootstrap can quantify easily.
- Repo notes: [resampling](../../notes/resampling_and_model_assessment/resampling.md),
  [confidence intervals](../../notes/hypothesis_testing_and_confidence_intervals/confidence_intervals.md).
