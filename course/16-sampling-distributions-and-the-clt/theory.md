# Theory: sampling distributions and the central limit theorem

## Why this matters

Every number computed from a sample (a mean, a median, a conversion rate, a regression slope) would have come out slightly
different if you had drawn another sample. Statistical inference is the discipline of describing *how much* it would differ.
The failure it prevents is reading a single sample statistic as if it were the truth: deciding that a campaign "lifted" order value by
$3 when a different sample of the same size would show $-4, or promising precision that your sample size cannot deliver.

## The sampling distribution

The **sampling distribution** of a statistic is its distribution over all possible samples of a given size $n$ from the population.
It is a theoretical object, but we can approximate it by simulation, which is what the dataset in this lesson does: 250 repeated
samples of size 50 are stored, and the means of the first 5, 20 and 50 draws of each row are compared.

For the sample mean $\bar X$ of $n$ independent draws from a population with mean $\mu$ and standard deviation $\sigma$:

$$
E[\bar X] = \mu,\qquad \operatorname{Var}(\bar X) = \frac{\sigma^2}{n},\qquad \operatorname{SE}(\bar X) = \frac{\sigma}{\sqrt n}.
$$

The first says $\bar X$ is **unbiased**. The second is the reason a larger sample is more precise, and also why precision is expensive:
to halve the standard error you need four times the data.

**Worked example (exact).** Population $\{2,4,6,12\}$: $\mu = 6$, $\sigma^2 = (16+4+0+36)/4 = 14$. List all 16 equally likely samples of size 2
(with replacement). The means range from 2 (one sample) to 12 (one sample); their average is exactly $6$, and their variance is exactly $7 = 14/2$,
so $\operatorname{SE} = \sqrt 7 = 2.65$. The means are less spread out than the single values: standard deviation $2.65$ against $\sigma = 3.74$.

## Standard error versus standard deviation

The **standard deviation** $\sigma$ (or its estimate $s$) describes how much *individual observations* vary. The **standard error** describes how much
the *estimate* varies from sample to sample. A population can be wildly variable and still be estimated precisely, given enough data.
In practice $\sigma$ is unknown and estimated by $s$ from the one sample you have: $\widehat{\operatorname{SE}} = s/\sqrt n$. Use
`STDEV` (divides by $n-1$) for $s$, and `STDEVP` only when you really hold the entire population, as in the first section of the workbook.

## The central limit theorem

If the draws are independent with finite variance, then for large $n$

$$
\frac{\bar X - \mu}{\sigma/\sqrt n} \;\approx\; N(0,1),
$$

**whatever the shape of the population**. This is what justifies normal-based intervals and tests for means. The theorem is a limit statement; how large $n$
must be depends on how far the population is from normal. A useful measure is skewness: the skewness of $\bar X$ is the population skewness divided by $\sqrt n$,
so a very skewed population needs a much larger $n$ than a symmetric one (the folklore "$n \ge 30$" is a rule of thumb, not a law). With very
heavy tails (for example income, file sizes or insurance claims) the convergence can be so slow that the mean of a few hundred observations is still dominated by the
largest values; then use medians, transformations or the bootstrap (lesson 17).

Related: the **law of large numbers** says $\bar X \to \mu$ as $n$ grows (the centre), whereas the CLT describes the *shape and size of the fluctuation* around it.

## Using it

- **Probability statements about a mean.** For a hypothetical $\sigma = 40$ and $n = 25$: $\operatorname{SE} = 8$; if $\mu = 100$ then
  $P(\bar X > 110) \approx 1 - \Phi\!\left(\tfrac{110-100}{8}\right) = 1 - \Phi(1.25) = 0.106$.
- **Planning sample size.** To reach $\operatorname{SE} \le \varepsilon$ you need $n \ge (\sigma/\varepsilon)^2$. With $\sigma=40$ and $\varepsilon = 4$: $n \ge 100$.
- **Interval for a mean.** $\bar x \pm t_{n-1,\,0.975}\, s/\sqrt n$ covers $\mu$ in about 95 % of repeated samples *if* the sampling distribution is close to
  normal. With skewed data and small $n$ the real coverage is lower, because $s$ is itself noisy and correlated with $\bar x$.

## Assumptions and pitfalls

1. **Independence.** $\sigma/\sqrt n$ is wrong for autocorrelated data (lesson 14): consecutive minutes of traffic are not independent draws, and the effective $n$ is smaller.
2. **Sampling bias.** A biased sample has a perfectly nice sampling distribution centred on the wrong value (lesson 05); more data does not fix it.
3. **Finite populations.** If you sample without replacement more than ~5 % of the population, multiply the variance by $(N-n)/(N-1)$. The simulation here samples with replacement.
4. **Confusing the histogram of the data with the sampling distribution.** The first stays skewed however large $n$ is; the second changes with $n$.
5. **The mean is not always the right statistic.** The CLT helps for sums and means; medians and extreme percentiles have different sampling distributions (lesson 03).
6. **Do not use $n \ge 30$ blindly**: check the shape with a histogram of repeated samples or a bootstrap.

## Related notes

- [Distribution shapes and heavy tails](../01-distribution-shapes-and-heavy-tails/theory.md)
- [Sampling bias and Simpson's paradox](../05-sampling-bias-and-simpson-s-paradox/theory.md)
- [Bootstrapping and confidence intervals](../17-bootstrapping-and-confidence-intervals/theory.md)
- [A/B testing and effect sizes](../19-a-b-testing-and-effect-sizes/theory.md)
- Repo notes: [Central limit theorem](../../notes/sampling_and_sampling_distributions/central_limit_theorem.md),
  [Standard error and LLN](../../notes/sampling_and_sampling_distributions/standard_error_and_lln.md)
