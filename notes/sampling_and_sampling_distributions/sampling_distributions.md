# Sampling Distributions

A statistic is computed from a sample, but before the sample is observed the statistic is itself a random variable. Its probability distribution over hypothetical repeated samples is called its **sampling distribution**.

## Statistics as Random Variables

Suppose $X_1,\ldots,X_n$ are sampled from a population with mean $\mu$ and variance $\sigma^2$. The sample mean

$$
\bar X=\frac{1}{n}\sum_{i=1}^n X_i
$$

changes from sample to sample. Under independent sampling,

$$
E[\bar X]=\mu
$$

and

$$
\operatorname{Var}(\bar X)=\frac{\sigma^2}{n}.
$$

Therefore the standard deviation of the sampling distribution of $\bar X$ is

$$
\operatorname{SE}(\bar X)=\frac{\sigma}{\sqrt n}.
$$

When $\sigma$ is unknown, this standard error is estimated using the sample standard deviation.

The variance formula follows by expanding the variance of the sum:

```math
\operatorname{Var}(\bar X)
=\frac{1}{n^2}\left(\sum_i\operatorname{Var}(X_i)
+2\sum_{i<j}\operatorname{Cov}(X_i,X_j)\right).
```

Independence makes the covariance terms zero, and equal variances leave $n\sigma^2/n^2$. Positive dependence can make the standard error larger, so counting more rows does not always add as much information as the independent-sample formula suggests. Linearity of expectation, in contrast, does not require independence for $E[\bar X]=\mu$ when each observation has mean $\mu$.

## Sampling Variability

Two random samples from the same population will rarely produce identical values of $\bar X$, $S^2$, a correlation coefficient, or a regression coefficient. This variability is not a mistake in the calculation; it is an inherent consequence of sampling.

A sampling distribution answers questions such as:

- How variable is the estimator?
- Is it centered on the target parameter?
- Is its distribution approximately symmetric or skewed?
- What standardized reference distribution can be used for intervals or tests?

### A small sampling distribution that can be listed exactly

Suppose two independent Bernoulli observations each have success probability $1/2$. The possible ordered samples are $(0,0)$, $(0,1)$, $(1,0)$, and $(1,1)$, each with probability $1/4$. Their means are $0$, $1/2$, $1/2$, and $1$. Thus the sampling distribution assigns probabilities $1/4$, $1/2$, and $1/4$ to those three distinct means.

The individual data distribution has only values zero and one, but the mean's distribution includes one half. Its expectation is $1/2$, and its variance is $1/8=\{(1/2)(1-1/2)\}/2$. This example constructs a sampling distribution without any normal approximation.

## Bias and Standard Error

For an estimator $\hat\theta$ of a parameter $\theta$,

$$
\operatorname{Bias}(\hat\theta)=E[\hat\theta]-\theta.
$$

The standard error describes spread:

$$
\operatorname{SE}(\hat\theta)=\sqrt{\operatorname{Var}(\hat\theta)}.
$$

Bias and standard error describe different aspects of estimator quality. An estimator can be unbiased but noisy, or biased but tightly concentrated.

## Exact and Approximate Sampling Distributions

Some sampling distributions are available exactly under specific assumptions. For example, normal-sample theory leads to exact Student's t, chi-square, and F reference distributions for several common statistics.

In many other settings the exact distribution is difficult to derive. Large-sample approximations then become important. The **Central Limit Theorem** explains why many standardized sums and averages become approximately normal as the sample size grows under suitable conditions.

Resampling methods provide another route when analytic sampling distributions are unavailable or inconvenient. A bootstrap approximates repeated sampling using an empirical distribution, with the resampling unit chosen to reflect the original design and dependence.

## Sampling Distribution vs Data Distribution

Do not infer the shape of one directly from the other. A strongly skewed population can still produce an approximately normal sampling distribution for the sample mean when the sample size is sufficiently large and the CLT assumptions are appropriate. Conversely, a normal-looking histogram of observed data does not by itself establish the sampling distribution of every statistic computed from those data.

## From Sampling to Inference

Sampling distributions connect observed statistics to confidence intervals and hypothesis tests. For any procedure, identify the target parameter, the estimator, and the distribution or approximation used to describe its variation. This makes it possible to assess coverage or error rates under the same model that generated the data.

A simulation histogram estimates a sampling distribution; it does not change the distribution by using more simulation repetitions. Sample size controls the statistic being studied, while the number of repetitions controls the accuracy of the simulation summary.
