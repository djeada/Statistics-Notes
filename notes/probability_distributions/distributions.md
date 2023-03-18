## Introduction to Distributions

A distribution is a function that describes the probability of a random variable. It helps to understand the underlying patterns and characteristics of a dataset. Distributions are widely used in statistics, data analysis, and machine learning for tasks such as hypothesis testing, confidence intervals, and predictive modeling.

## Probability Distributions

* **Probability Density Function (PDF):** For continuous variables, it gives the probability density at a given value x: $f_X(x)$
* **Probability Mass Function (PMF):** For discrete variables, it gives the probability that a random variable takes on the value x: $p_X(x) = P(X=x)$
* **Cumulative Density Function (CDF):** Gives the probability that a random variable is less than or equal to x: $F_X(x) = P(X\leq x)$

## Moments and Moment Generating Functions

Moments are statistical measures that describe various aspects of a distribution, such as central tendency, dispersion, and shape. The $n$th moment of a random variable $X$ about a constant $c$ is defined as the expected value of $(X - c)^n$:

$E[(X - c)^n]$

The moment-generating function (MGF) of a random variable $X$ is a function that, when differentiated $n$ times and evaluated at $t=0$, gives the $n$th moment about the origin:

$M_X(t) = E[e^{tX}]$

The mean (first moment) and variance (second moment) can be derived from the MGF:

* **Mean (first moment):** $E[X] = \mu = M_X^{(1)}(0)$
* **Variance (second moment):** $Var(X) = \sigma^2 = E[X^2] - (E[X])^2 = M_X^{(2)}(0) - (M_X^{(1)}(0))^2$

## Types of Distributions

1. **Uniform distribution:** All values have equal probability of occurring.
2. **Normal distribution (Gaussian distribution):** A continuous distribution where data is symmetrically distributed around the mean.
3. **Exponential distribution:** A continuous distribution where data decreases exponentially as the value increases.
4. **Poisson distribution:** A discrete distribution for counting the number of events in a fixed interval of time or space.

## Measures of Central Tendency

Measures of central tendency describe the center of a distribution:

* **Mean (average):** The sum of all data points divided by the number of data points: $\mu = \frac{\sum_{i=1}^{n} x_i}{n}$
* **Median:** The middle value when data is ordered from smallest to largest.
* **Mode:** The value(s) that occurs most frequently in the data.

## Measures of Dispersion

Measures of dispersion describe the spread of a distribution:

* **Range:** The difference between the maximum and minimum values.
* **Variance:** The average of the squared differences from the mean: $\sigma^2 = \frac{\sum_{i=1}^{n} (x_i - \mu)^2}{n}$
* **Standard deviation:** The square root of the variance: $\sigma = \sqrt{\sigma^2}$

## Measures of Shape

Measures of shape describe the skewness and kurtosis of a distribution:

* **Skewness:** A measure of the asymmetry of the distribution.
* **Kurtosis:** A measure of the "tailedness" of the distribution.

## Sampling and Sampling Distributions

When working with statistics, we usually base our calculations on a sample and not the full population of data. Taking multiple samples and combining the resulting means forms a sampling distribution. The larger the sample size, the closer the data will be to a perfect normal distribution, and the less variance around the mean there will be.

## The Central Limit Theorem

The Central Limit Theorem states that with a large enough sample size, the distribution of values for a random variable starts to form an approximately normal curve. This applies to any distribution of sample data if the size of the sample is large enough.

## Mean and Standard Error of a Sampling Distribution

* **Mean**: The mean of a sampling distribution is the mean of all the sample means.
* **Standard Error (SE)**: The standard deviation of a sampling distribution. For a distribution of proportion means, SE is calculated as: $\text{SE} = \sqrt{\frac{p(1-p)}{n}}$. For a distribution of sample means, the standard error is: $\text{SE} = \frac{\sigma}{\sqrt{n}}$.
