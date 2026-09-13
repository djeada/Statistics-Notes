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

## Sampling Variability

Two random samples from the same population will rarely produce identical values of $\bar X$, $S^2$, a correlation coefficient, or a regression coefficient. This variability is not a mistake in the calculation; it is an inherent consequence of sampling.

A sampling distribution answers questions such as:

- How variable is the estimator?
- Is it centered on the target parameter?
- Is its distribution approximately symmetric or skewed?
- What standardized reference distribution can be used for intervals or tests?

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

Resampling methods provide another route when analytic sampling distributions are unavailable or inconvenient; see **[Resampling & Model Assessment](../resampling_and_model_assessment/README.md)** later in the curriculum.

## Sampling Distribution vs Data Distribution

Do not infer the shape of one directly from the other. A strongly skewed population can still produce an approximately normal sampling distribution for the sample mean when the sample size is sufficiently large and the CLT assumptions are appropriate. Conversely, a normal-looking histogram of observed data does not by itself establish the sampling distribution of every statistic computed from those data.

## From Sampling to Inference

Sampling distributions provide the machinery used later to construct confidence intervals and hypothesis tests. Before doing that, the next unit focuses on **estimators themselves**: what they target and how their quality is judged.

Continue to **[Central Limit Theorem](central_limit_theorem.md)** and then **[Estimation](../estimation/README.md)**.
