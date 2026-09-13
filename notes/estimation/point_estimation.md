# Point Estimation

A **parameter** is an unknown feature of a population or statistical model, such as a mean $\mu$, variance $\sigma^2$, probability $p$, or regression coefficient $\beta$. A **point estimator** is a rule or statistic computed from sample data and used to estimate that parameter.

Before the data are observed, an estimator such as $\hat\theta$ is a random variable because its value varies from sample to sample. After the data are observed, the resulting numerical value is called an **estimate**.

## Estimator vs Estimate

Suppose $X_1,\ldots,X_n$ are sampled from a population with mean $\mu$. The sample mean

```math
\bar X=\frac{1}{n}\sum_{i=1}^n X_i
```

is an estimator of $\mu$. If the observed sample gives $\bar x=12.4$, then $12.4$ is the corresponding estimate.

This distinction matters because properties such as bias, variance, and consistency describe the estimator and its sampling behavior, not a single realized estimate.

## Bias

The bias of an estimator $\hat\theta$ is

```math
\mathrm{Bias}(\hat\theta)=E[\hat\theta]-\theta.
```

An estimator is **unbiased** if

```math
E[\hat\theta]=\theta.
```

In other words, across repeated samples, its average value equals the parameter being estimated.

Unbiasedness is useful, but it is not the only desirable property. An unbiased estimator with high variability may be less useful than a slightly biased estimator with substantially lower variance.

## Variance and Standard Error

The sampling variance of an estimator is

```math
\mathrm{Var}(\hat\theta),
```

which describes how much the estimator varies across repeated samples.

Its standard error is the standard deviation of its sampling distribution:

```math
\mathrm{SE}(\hat\theta)=\sqrt{\mathrm{Var}(\hat\theta)}.
```

In practice, the true standard error often depends on unknown population parameters. We therefore estimate it from the observed data, producing an **estimated standard error**.

A smaller standard error generally indicates a more precise estimator.

## Mean-Squared Error

Bias and variance can be considered together through the mean-squared error:

```math
\mathrm{MSE}(\hat\theta)
=
E[(\hat\theta-\theta)^2]
=
\mathrm{Var}(\hat\theta)
+
\mathrm{Bias}(\hat\theta)^2.
```

This decomposition makes the bias-variance trade-off explicit. An estimator can have some bias yet still achieve a smaller MSE if the reduction in variance is large enough.

## Consistency

An estimator is **consistent** if it converges to the true parameter as the sample size grows. More formally, $\hat\theta_n$ is consistent for $\theta$ if, for every $\varepsilon>0$,

```math
P(|\hat\theta_n-\theta|>\varepsilon)\to 0
\qquad \text{as } n\to\infty.
```

Informally, as more data become available, the estimator becomes increasingly concentrated near the true parameter.

Consistency is an asymptotic property. A consistent estimator can still perform poorly in small samples, so finite-sample properties such as bias and variance remain important.

## Method of Moments

The **method of moments** estimates parameters by equating sample moments with their corresponding theoretical population moments and solving for the unknown parameters.

For example, if a model satisfies

```math
E[X]=g(\theta),
```

we can replace the population mean with the sample mean and solve

```math
\bar X=g(\hat\theta).
```

If the model contains several unknown parameters, additional moments such as $E[X^2]$, $E[X^3]$, and their sample counterparts can be used to obtain enough equations to solve for them.

The method of moments is often simple and intuitive, although it does not necessarily produce the most efficient estimator.

## Maximum Likelihood

Suppose the observed data are $x_1,\ldots,x_n$ and the statistical model has parameter $\theta$. Once the data have been observed, their joint probability mass function or probability density can be viewed as a function of $\theta$. This function is called the **likelihood**:

```math
L(\theta;x_1,\ldots,x_n).
```

A **maximum-likelihood estimator (MLE)** chooses the parameter value that makes the observed data most likely under the model:

```math
\hat\theta_{\mathrm{MLE}}
=
\arg\max_\theta L(\theta;x_1,\ldots,x_n).
```

In practice, it is often easier to maximize the **log-likelihood**

```math
\ell(\theta)=\log L(\theta),
```

because logarithms turn products into sums. Since the logarithm is strictly increasing, maximizing the log-likelihood gives the same parameter value as maximizing the likelihood.

### Bernoulli Example

Suppose $X_1,\ldots,X_n$ are independent Bernoulli observations with success probability $p$:

```math
X_i\sim\mathrm{Bernoulli}(p).
```

The likelihood is

```math
L(p)
=
p^{\sum_i x_i}
(1-p)^{n-\sum_i x_i}.
```

Let

```math
S=\sum_{i=1}^n x_i
```

be the number of observed successes. Then the log-likelihood is

```math
\ell(p)
=
S\log p
+
(n-S)\log(1-p).
```

Maximizing this expression gives

```math
\hat p_{\mathrm{MLE}}
=
\frac{S}{n}
=
\bar X.
```

Thus, for Bernoulli data, the maximum-likelihood estimate of $p$ is simply the observed proportion of successes.

## Estimation Is Not Yet Inference

A point estimator provides a single value for estimating an unknown parameter. By itself, however, it does not tell us how uncertain that estimate is.

For example, two samples may produce the same point estimate but very different levels of precision if their sample sizes differ substantially.

To quantify uncertainty, we need additional information about the estimator's sampling distribution. Depending on the problem, this may come from an exact distribution, an asymptotic approximation, or a resampling method such as the bootstrap.

These ideas lead naturally to confidence intervals and hypothesis tests.

Continue to **[Hypothesis Testing & Confidence Intervals](../hypothesis_testing_and_confidence_intervals/README.md)**.
