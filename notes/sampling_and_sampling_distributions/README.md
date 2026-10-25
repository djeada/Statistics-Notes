
# Sampling and Sampling Distributions

A population distribution describes the possible value of one observation. A sampling distribution describes the possible value of a statistic calculated from a sample. Keeping these objects separate explains why a dataset can be highly variable while its average is estimated precisely, why a larger sample does not remove selection bias, and why estimating a standard deviation changes a reference distribution.

Suppose individual measurements have mean 50 and standard deviation 12. With 36 independent measurements from that population, the sample mean still has expectation 50, but its standard deviation is $12/\sqrt{36}=2$. A new individual observation varies on the scale of 12 units; repeated sample means vary on the scale of two. The latter quantity is the mean's standard error. It is not an estimate of how much individuals differ from one another.

## Specify What Repeated Sampling Means

A sampling distribution depends on the population or probability model, the sample size, the statistic, and the sampling design. The same numerical sample mean can have different uncertainty under independent sampling, sampling without replacement, or sampling whole clusters.

For example, draw two values from the finite population $\{0,2,4\}$. With replacement, all nine ordered pairs are equally likely, and the mean can be 0, 1, 2, 3, or 4. Without replacement, the three unordered pairs give means 1, 2, and 3 with equal probability. Both means are unbiased for the population mean two, but their variances are $4/3$ and $2/3$. The design changes how much information the sample contains.

This randomness is considered before the sample is observed. After observing a particular sample, its calculated mean is a fixed number. In frequentist sampling calculations, the population parameter is held fixed and hypothetical new samples produce new estimates. A simulation approximates that repeated-sampling experiment; it does not make the population parameter vary.

## Precision, Bias, and Concentration

For independent observations with a common finite variance,

$$
E[\bar X]=\mu,\qquad
\mathrm{Var}(\bar X)=\frac{\sigma^2}{n},\qquad
\mathrm{SE}(\bar X)=\frac{\sigma}{\sqrt n}.
$$

The square-root relationship means that four times as many independent observations are needed to halve the standard error. A thousand duplicated copies of the same observation do not have the information in a thousand independent observations: their covariance terms remain.

Bias is the difference between an estimator's expectation and its target. Standard error measures spread around the estimator's own expectation. Mean squared error combines both:

$$
E[(\hat\theta-\theta)^2]
=\mathrm{Var}(\hat\theta)+\{E[\hat\theta]-\theta\}^2.
$$

An average of observations from an unrepresentative sampling mechanism can have a very small standard error and remain centered on the wrong population quantity. Increasing sample size helps precision under that mechanism; it does not establish representativeness.

The law of large numbers concerns concentration: under suitable assumptions, $\bar X_n$ approaches $\mu$. The central limit theorem concerns the shape of the remaining fluctuations:

$$
\frac{\sqrt n(\bar X_n-\mu)}{\sigma}
\ \xrightarrow{d}\ N(0,1).
$$

The scaling is essential. The unscaled mean concentrates near a constant, while the standardized fluctuation can have a nondegenerate limiting distribution. Neither result says that the individual observations become normal.

## Reference Distributions Come from Particular Constructions

For an independent sample from $N(\mu,\sigma^2)$, define

$$
S^2=\frac{1}{n-1}\sum_{i=1}^n(X_i-\bar X)^2.
$$

The normal model gives both a distribution for the standardized mean and an independent distribution for the residual sum of squares. These produce the familiar reference distributions:

| Quantity | Reference distribution | What makes it valid |
|---|---|---|
| $(\bar X-\mu)/(\sigma/\sqrt n)$ | Standard normal | Independent normal observations and the population standard deviation |
| $(n-1)S^2/\sigma^2$ | Chi-square with $n-1$ degrees of freedom | Normal residual directions after estimating one mean |
| $(\bar X-\mu)/(S/\sqrt n)$ | Student's t with $n-1$ degrees of freedom | Independent normal numerator and scaled chi-square denominator |
| $(U/d_1)/(V/d_2)$ | F with degrees of freedom $d_1,d_2$ | Independent chi-square variables $U,V$ divided by their respective degrees of freedom |

Replacing a population standard deviation by an arbitrary estimate does not automatically create an exact t statistic. Likewise, a positive ratio is not automatically F distributed. The statistic must have the stated construction, including independence.

Degrees of freedom count independent directions in these normal-sample constructions. Estimating a sample mean constrains the residuals to sum to zero, leaving $n-1$ directions. A regression with a full-rank design of $p$ columns leaves $n-p$ residual directions. This explains the denominators rather than treating them as corrections to memorize.

## Exact Results and Useful Approximations

The normal-sample results above are exact at finite sample sizes under their assumptions. A normal approximation to a binomial count or a chi-square approximation to a categorical goodness-of-fit statistic is a different kind of result. Its accuracy depends on the underlying probabilities, sample size, and the part of the distribution used.

Thirty independent Bernoulli trials with success probability 0.01 have expected count only 0.3 and probability about 0.740 of no successes. A sample-size rule alone does not make that count resemble a continuous symmetric curve. Conversely, an average of independent normal measurements is exactly normal even with two observations.

To use a sampling distribution for an interval or test, identify the target, the sampling mechanism, the statistic, and the assumptions that connect it to its reference law. A simulation should reproduce those same choices. Increasing the number of simulated samples reduces simulation error; increasing the number of observations in each sample changes the sampling distribution being studied.
