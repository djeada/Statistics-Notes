# Sampling and Sampling Distributions

A population distribution describes an individual observation. A sampling distribution describes a statistic computed from a random sample. Repeating the sampling process produces new observations and a new statistic each time, even when the population parameter remains fixed.

## What changes when the sample grows

For independent observations with variance $\sigma^2$, the sample mean has variance $\sigma^2/n$. Its standard error is therefore $\sigma/\sqrt n$. This explains why averaging improves precision, and why four times as many observations are needed to halve the standard error. Dependence can add covariance terms and invalidate this simple calculation.

The law of large numbers states that an average converges to its expectation under suitable conditions. The central limit theorem describes the shape of its fluctuations after centering and scaling. The first result concerns concentration; the second concerns an approximate distribution. Neither states that the raw observations become normally distributed.

## Reference distributions arise from statistics

With independent normal data, standardizing a mean by a known standard deviation gives a standard normal statistic. Replacing that standard deviation with an independent estimate introduces additional uncertainty and leads to Student's t. Sums of squared independent standard normals produce chi-square distributions. Ratios of independent chi-square variables divided by their degrees of freedom produce F distributions.

These constructions explain why each distribution appears in inference and what assumptions make it applicable. A reference distribution is exact only under its stated model. Large-sample approximations and resampling methods can extend the analysis, but their validity still depends on sampling, dependence, and the statistic being studied.


The sampling unit and any dependence between units determine how much information a statistic contains; the row count alone does not settle that question.
