# Sampling Distributions

A statistic is computed from a sample, but before the sample is observed the statistic is itself a random variable. Its probability distribution over hypothetical repeated samples is called its **sampling distribution**.

## The Sampling Design Is Part of the Distribution

To define a repeated-sampling experiment, specify what can be sampled, how many units are drawn, whether units can be drawn again, and what is held fixed. In an i.i.d. model, independent observations are drawn from one population distribution. In a finite-population design, the population values can be fixed while the selected subset is random. In a cluster design, selecting one unit can bring several related measurements into the sample.

The parameter and the statistic also have distinct roles. The population mean $\mu$ is fixed in the experiment, while $\bar X$ varies across samples. Once the observed data have been supplied, $\bar x$ denotes one realized value. Calculating it exactly does not eliminate the sampling variability that existed before the draw.

A dataset's histogram shows the observed individual values. A histogram of means from repeated samples instead shows the sampling distribution of a mean. In practice we often observe only one sample, so the latter distribution must be derived from a probability model or approximated by an appropriate simulation or resampling scheme.

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
\mathrm{Var}(\bar X)=\frac{\sigma^2}{n}.
$$

Therefore the standard deviation of the sampling distribution of $\bar X$ is

$$
\mathrm{SE}(\bar X)=\frac{\sigma}{\sqrt n}.
$$

When $\sigma$ is unknown, this standard error is estimated using the sample standard deviation.

The variance formula follows by expanding the variance of the sum:

```math
\mathrm{Var}(\bar X)
=\frac{1}{n^2}\left(\sum_i\mathrm{Var}(X_i)
+2\sum_{i<j}\mathrm{Cov}(X_i,X_j)\right).
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

### Changing Replacement Changes the Exact Distribution

Take the finite population $\{0,2,4\}$ and draw a sample of size two. With replacement, each of the nine ordered pairs has probability $1/9$. Grouping pairs with the same mean gives:

| Sample mean | 0 | 1 | 2 | 3 | 4 |
|---|---:|---:|---:|---:|---:|
| Probability with replacement | $1/9$ | $2/9$ | $3/9$ | $2/9$ | $1/9$ |

The mean of this distribution is two. Its variance is

$$
E[(\bar X-2)^2]
=\frac{4+2+0+2+4}{9}=\frac43.
$$

The population variance, defined here with denominator three, is $8/3$. Independent sampling with replacement gives $(8/3)/2=4/3$, agreeing with the enumeration.

Without replacement, the possible unordered samples are $\{0,2\}$, $\{0,4\}$, and $\{2,4\}$. Their means 1, 2, and 3 each have probability $1/3$, so the mean remains two and the variance becomes $2/3$. The finite population correction multiplies the with-replacement variance by $(N-n)/(N-1)=(3-2)/(3-1)=1/2$.

The change comes from negative dependence: drawing a large value removes it from the remaining choices. A sampling distribution therefore cannot be specified by sample size and statistic alone. Here replacement changes both the support and the variance of the mean.

## Bias and Standard Error

For an estimator $\hat\theta$ of a parameter $\theta$,

$$
\mathrm{Bias}(\hat\theta)=E[\hat\theta]-\theta.
$$

The standard error describes spread:

$$
\mathrm{SE}(\hat\theta)=\sqrt{\mathrm{Var}(\hat\theta)}.
$$

Bias and standard error describe different aspects of estimator quality. An estimator can be unbiased but noisy, or biased but tightly concentrated.

### Mean Squared Error Connects Bias and Variance

Insert and subtract $E[\hat\theta]$ inside the estimation error:

$$
\hat\theta-\theta
=(\hat\theta-E[\hat\theta])+(E[\hat\theta]-\theta).
$$

After squaring and taking expectations, the cross term vanishes because $E[\hat\theta-E[\hat\theta]]=0$. Consequently

$$
\mathrm{MSE}(\hat\theta)
=E[(\hat\theta-\theta)^2]
=\mathrm{Var}(\hat\theta)+\mathrm{Bias}(\hat\theta)^2.
$$

For a concrete tradeoff, suppose $\bar X$ has expectation two and variance one, and consider shrinking it toward zero by using $T=0.8\bar X$. Its expectation is 1.6, its bias is $-0.4$, and its variance is $0.8^2=0.64$. Its MSE is therefore $0.64+0.16=0.80$, smaller than the unbiased mean's MSE of one in this example.

This advantage depends on where the true mean lies relative to the chosen shrinkage target. If $\mathrm{Var}(\bar X)=1$ but $\mu=10$, the same rule has bias $-2$ and MSE 4.64. A smaller standard error by itself does not establish a better estimator. The target parameter and the losses assigned to bias and variability matter.

### Why Dividing by n Underestimates a Variance

For independent observations with common mean and variance, write the identity

$$
\sum_i(X_i-\bar X)^2
=\sum_i(X_i-\mu)^2-n(\bar X-\mu)^2.
$$

Its expectation is $n\sigma^2-n(\sigma^2/n)=(n-1)\sigma^2$. Thus $S^2=\sum_i(X_i-\bar X)^2/(n-1)$ is unbiased for $\sigma^2$, while division by n gives expectation $(n-1)\sigma^2/n$. Estimating the center has removed some of the observed squared variation.

This argument uses independence and finite variance, not normality. Normality is needed for the stronger claim that the scaled sample variance has an exact chi-square distribution. Unbiasedness of $S^2$ also does not imply unbiasedness of $S=\sqrt{S^2}$, because expectation does not commute with a nonlinear square root.

## Exact and Approximate Sampling Distributions

Some sampling distributions are available exactly under specific assumptions. For example, normal-sample theory leads to exact Student's t, chi-square, and F reference distributions for several common statistics.

In many other settings the exact distribution is difficult to derive. Large-sample approximations then become important. The **Central Limit Theorem** explains why many standardized sums and averages become approximately normal as the sample size grows under suitable conditions.

Resampling methods provide another route when analytic sampling distributions are unavailable or inconvenient. A bootstrap approximates repeated sampling using an empirical distribution, with the resampling unit chosen to reflect the original design and dependence.

### A Statistic Whose Limit Is Not Normal

Let $X_1,\ldots,X_n$ be independent Uniform$(0,\theta)$ observations and let $M_n=\max_iX_i$. For $0\leq m\leq\theta$,

$$
P(M_n\leq m)
=P(X_1\leq m,\ldots,X_n\leq m)
=\left(\frac m\theta\right)^n.
$$

The maximum is usually below the endpoint being estimated. Integrating its density gives $E[M_n]=n\theta/(n+1)$, so $(n+1)M_n/n$ is unbiased for $\theta$. Its distribution is still not the distribution of a sample mean.

For fixed $x\geq0$ and sufficiently large n,

$$
P\left(\frac{n(\theta-M_n)}{\theta}>x\right)
=\left(1-\frac xn\right)^n
\longrightarrow e^{-x}.
$$

The scaled endpoint gap approaches an exponential distribution, with scale $1/n$ for the unscaled gap. This differs from the mean's usual $1/\sqrt n$ scale and normal limit. Large sample size does not make every statistic normal; the statistic's mathematical form determines which asymptotic result applies.

## Sampling Distribution vs Data Distribution

Do not infer the shape of one directly from the other. A strongly skewed population can still produce an approximately normal sampling distribution for the sample mean when the sample size is sufficiently large and the CLT assumptions are appropriate. Conversely, a normal-looking histogram of observed data does not by itself establish the sampling distribution of every statistic computed from those data.

## A Sampling Distribution Can Check an Interval's Coverage

For a normal population with known $\sigma$, the interval $\bar X\pm1.96\sigma/\sqrt n$ covers the fixed mean in about 95% of repeated samples. Coverage is a probability over the random interval endpoints. It can be derived from the standardized mean without observing hundreds of actual samples.

A very small Bernoulli example shows why using a familiar formula without checking its reference can fail. For two independent Bernoulli observations, the usual uncorrected Wald interval is

$$
\hat p\pm1.96\sqrt{\frac{\hat p(1-\hat p)}2}.
$$

At the true value $p=1/2$, samples $(0,0)$ and $(1,1)$ produce estimated standard error zero and point intervals at zero and one. Neither covers $1/2$. The other two samples have $\hat p=1/2$ and intervals covering it. All four samples have probability $1/4$, so the actual coverage is only $1/2$, not 95%. Clipping the endpoints to $[0,1]$ does not repair this example.

The calculation is an exact coverage assessment of a particular procedure. It identifies the problem with a poor small-sample approximation rather than suggesting that all confidence intervals behave this way.

## Distinguish Sample Size from Simulation Size

Suppose B independent simulations each generate n observations and return a sample mean. Changing n changes the statistic's sampling distribution. Changing B estimates that fixed distribution more accurately. Under finite population variance $\sigma^2$, the average of the B simulated means has Monte Carlo standard error $\sigma/\sqrt{nB}$.

For an estimated probability, each simulated sample supplies an indicator. If the true probability is q, the Monte Carlo standard error of its simulated frequency is $\sqrt{q(1-q)/B}$. With $q=1/2$ and $B=1000$, it is about 0.0158. Even perfectly implemented code will show this simulation variation.

Each replicate must reproduce the intended sampling mechanism. Resampling individual rows from dependent clusters changes the mechanism and can estimate the wrong variability very precisely. More repetitions cannot correct a mismatch between the simulated experiment and the actual design.

## From Sampling to Inference

Sampling distributions connect observed statistics to confidence intervals and hypothesis tests. For any procedure, identify the target parameter, the estimator, and the distribution or approximation used to describe its variation. This makes it possible to assess coverage or error rates under the same model that generated the data.

A simulation histogram estimates a sampling distribution; it does not change the distribution by using more simulation repetitions. Sample size controls the statistic being studied, while the number of repetitions controls the accuracy of the simulation summary.
