## Confidence Intervals

A confidence interval is a range of values, derived from a data sample, that is used to estimate an unknown population parameter. It provides an interval estimate that is likely to contain the true population parameter with a certain level of confidence. The confidence level is a measure of the certainty that the interval contains the true parameter.

### Definition

A confidence interval is defined as:

$$
(\text{Point Estimate} - \text{Margin of Error}, \text{Point Estimate} + \text{Margin of Error})
$$

Where:

* Point Estimate: The best single estimate of the population parameter based on the sample data.
* Margin of Error: A measure of the uncertainty in the point estimate.

### Confidence Level

The confidence level represents the degree of certainty that the true population parameter lies within the confidence interval. Common confidence levels are 90%, 95%, and 99%. A higher confidence level indicates greater certainty that the interval contains the true parameter, but the interval will be wider.

### Example: Estimating the Mean of a Population

Suppose we have a sample of 100 individuals with a mean age of 35 and a standard deviation of 5 years. We want to estimate the mean age of the entire population.

To calculate a 95% confidence interval for the mean, we would use the following formula:

$$
\text{Confidence Interval} = \text{Sample Mean} \pm \frac{\text{Standard Error}}{\sqrt{\text{Sample Size}}} * \text{Critical Value}
$$

For a 95% confidence level, the critical value (from the standard normal distribution) is 1.96.

$$
\text{Confidence Interval} = 35 \pm \frac{5}{\sqrt{100}} * 1.96 = (33.08, 36.92)
$$

Thus, we can say with 95% confidence that the mean age of the entire population lies within the interval (33.08, 36.92) years.

It is important to note that the confidence interval does not mean that there is a 95% chance that the true population mean lies within the interval. Instead, it means that if we were to repeat the sampling process many times, 95% of the confidence intervals calculated from those samples would contain the true population mean.

## OTHER NOTES

Confidence Intervals

A confidence interval is a range of values around a sample statistic within which we are confident that the true parameter lies. For example, our bag weight sampling distribution is based on samples of the weights of bags carried by passengers through our airport security line. We know that the mean weight (the expected value for the weight of a bag) in our sampling distribution is 3.2, and we assume this is also the population mean for all bags; but how confident can we be that the true mean weight of all carry-on bags is close to the value?

Let's start to put some precision onto these terms. We could state the question another way. What's the range of weights within which are confident that the mean weight of a carry-on bag will be 95% of the time? To calculate this, we need to determine the range of values within which the population mean weight is likely to be in 95% of samples. This is known as a confidence interval; and it's based on the Z-scores inherent in a normal distribution.

Confidence intervals are expressed as a sample statistic ± (plus or minus) a margin of error. To calculate the margin of error, you need to determine the confidence level you want to find (for example, 95%), and determine the Z score that marks the threshold above or below which the values that are not within the chosen interval reside. For example, to calculate a 95% confidence interval, you need the critical Z scores that exclude 5% of the values under the curve; with 2.5% of them being lower than the values in the confidence interval range, and 2.5% being higher. In a normal distribution, 95% of the area under the curve is between a Z score of ± 1.96. The following table shows the critical Z values for some other popular confidence interval ranges:
Confidence 	Z Score
90% 	1.645
95% 	1.96
99% 	2.576

To calculate a confidence interval around a sample statistic, we simply calculate the standard error for that statistic as described previously, and multiply this by the approriate Z score for the confidence interval we want.

To calculate the 95% confidence interval margin of error for our bag weights, we multiply our standard error of 0.053 by the Z score for a 95% confidence level, which is 1.96:

So we can say that we're confident that the population mean weight is in the range of the sample mean ± 0.10388 with 95% confidence. Thanks to the central limit theorem, if we used an even bigger sample size, the confidence interval would become smaller as the amount of variance in the distribution is reduced. If the number of samples were infinite, the standard error would be 0 and the confidence interval would become a certain value that reflects the true mean weight for all carry-on bags:
In Python, you can use the scipy.stats.norm.interval** function to calculate a confidence interval for a normal distribution. Run the following code to recreate the sampling distribution for bag searches with the same parameters, and display the 95% confidence interval for the mean (again, this may take some time to run):
