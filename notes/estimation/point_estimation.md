# Point Estimation

A **parameter** is an unknown feature of a population or statistical model, such as a mean $\mu$, variance $\sigma^2$, probability $p$, or regression coefficient $\beta$. A **point estimator** is a rule computed from sample data and intended to approximate that parameter.

Before the data are observed, an estimator such as $\hat\theta$ is a random variable because it changes from sample to sample. After observing the data, its realized numerical value is an **estimate**.

## Estimator vs Estimate

Suppose $X_1,\ldots,X_n$ are sampled from a population with mean $\mu$. The sample mean

$$
\bar X=\frac{1}{n}\sum_{i=1}^n X_i
$$

is an estimator of $\mu$. If the observed sample produces $\bar x=12.4$, then $12.4$ is the estimate.

The distinction matters because properties such as bias and variance are properties of the estimator's sampling distribution, not of one realized estimate.

## Bias

The bias of an estimator $\hat\theta$ is

$$
\operatorname{Bias}(\hat\theta)=E[\hat\theta]-\theta.
$$

An estimator is **unbiased** when its expected value equals the target parameter. Unbiasedness is useful, but it is not the only criterion that matters. A highly variable unbiased estimator can be less useful than a slightly biased estimator with much smaller variance.

## Variance and Standard Error

The sampling variance of an estimator is

$$
\operatorname{Var}(\hat\theta),
$$

and its standard error is

$$
\operatorname{SE}(\hat\theta)=\sqrt{\operatorname{Var}(\hat\theta)}.
$$

In practice the standard error is often itself estimated because the true population parameters appearing in the variance formula are unknown.

## Mean-Squared Error

Bias and variance can be combined through mean-squared error:

$$
\operatorname{MSE}(\hat\theta)=E[(\hat\theta-\theta)^2]
=\operatorname{Var}(\hat\theta)+\operatorname{Bias}(\hat\theta)^2.
$$

This decomposition makes the bias-variance trade-off explicit.

## Consistency

An estimator is **consistent** if it converges to the true parameter as the sample size grows. Informally, more data should make the estimator concentrate around the target.

Consistency is an asymptotic property. An estimator can be consistent yet perform poorly in small samples, so finite-sample bias and variance still matter.

## Method of Moments

The method of moments equates sample moments with their population counterparts and solves for the unknown parameters.

For example, if a model has

$$
E[X]=g(\theta),
$$

then a method-of-moments estimator may solve

$$
\bar X=g(\hat\theta).
$$

The method is often simple and intuitive, though it is not always the most statistically efficient choice.

## Maximum Likelihood

Suppose the observed data are $x_1,\ldots,x_n$ and the model has parameter $\theta$. The likelihood is the joint model for the observed data viewed as a function of $\theta$:

$$
L(\theta;x_1,\ldots,x_n).
$$

A **maximum-likelihood estimator (MLE)** chooses the parameter value that maximizes this likelihood:

$$
\hat\theta_{\text{MLE}}=\arg\max_\theta L(\theta;x_1,\ldots,x_n).
$$

It is usually easier to maximize the log-likelihood because products become sums.

### Bernoulli Example

If $X_1,\ldots,X_n$ are independent Bernoulli observations with success probability $p$, the likelihood is

$$
L(p)=p^{\sum_i x_i}(1-p)^{n-\sum_i x_i}.
$$

The MLE is

$$
\hat p=\bar X,
$$

the observed fraction of successes.

## Estimation Is Not Yet Inference

A point estimator answers “what value should we use as our best single estimate?” It does not by itself answer “how uncertain is that estimate?”

Uncertainty requires the estimator's sampling distribution, an asymptotic approximation, or a resampling method. Those ideas lead to confidence intervals and hypothesis tests.

Continue to **[Hypothesis Testing & Confidence Intervals](../hypothesis_testing_and_confidence_intervals/README.md)**.
