## Confidence Intervals

Confidence intervals (CIs) provide a range of values which are believed, with a certain degree of confidence, to contain a population parameter, like the mean or proportion. They are constructed from a sampled data set and offer an interval estimate for the parameter of interest.

### Definition and Components

A confidence interval is typically expressed as:

$$
(\text{Point Estimate} - \text{Margin of Error}, \ \text{Point Estimate} + \text{Margin of Error})
$$

Where:
- **Point Estimate**: The best single estimate for a parameter based on the sample data (e.g., sample mean).
- **Margin of Error**: An indication of the precision of the point estimate, incorporating the standard error and the critical value from a distribution appropriate for the confidence level.

### Confidence Level and Interpretation

The confidence level signifies the probability that the interval will capture the true population parameter across many samples. Common levels include 90%, 95%, and 99%. A 95% confidence level means that if we were to take 100 different samples and construct CIs for each, we expect about 95 of them to contain the true parameter.

### Example: Health App Steps Count

Consider two health apps estimating daily steps:

- **App X**: Reports an average of 10,300 steps/day.
- **App Y**: Provides a 90% CI for the average as 10,000 ± 500 steps/day.

App Y, by including a confidence interval, acknowledges data variability and seems more reliable, provided the data collection methods are sound.

### Example: Carry-on Baggage Weight

Suppose the average weight of a sample of carry-on bags is 3.2 kg with a standard error of 0.053 kg. To find the 95% CI:

$$
\text{Confidence Interval} = \text{Sample Mean} \pm (\text{Standard Error} \times \text{Critical Value})
$$

With a 95% confidence level, the critical value (Z-score) is approximately 1.96.

$$
\text{Confidence Interval} = 3.2 \pm (0.053 \times 1.96) = (3.09612, \ 3.30388)
$$

This CI suggests that the mean weight of all carry-on bags is likely between 3.09612 kg and 3.30388 kg, with 95% confidence.

### Example: Calibrating Digital Thermometer

What range of error should be allowed when calibrating a digital thermometer to ensure it accurately reflects the actual temperature 95% of the time?

When calibrating instruments like a digital thermometer, ensuring accuracy within a specific confidence interval is crucial. For a normal distribution, 95% of the data falls within 1.96 standard deviations from the mean. Therefore, the calibration error range should be set to 1.96 times the standard error (SE) around the mean expected temperature reading.

The formula for a 95% Confidence Interval (CI) for the thermometer's temperature reading ($T$) is:

$$
CI = T \pm Z \times SE
$$

Where:

- $T$ is the mean temperature reading from the thermometer.
- $Z$ is the Z-score that corresponds to the 95% confidence level, which is 1.96.
- $SE$ is the standard error, which is the standard deviation ($\sigma$) of the thermometer's readings over multiple trials divided by the square root of the number of trials ($n$):

$$
SE = \frac{\sigma}{\sqrt{n}}
$$

Suppose we've tested the thermometer and found that the mean reading ($T$) is 37.0°C with a standard deviation ($\sigma$) of 0.5°C over 30 trials. The SE and CI would be calculated as follows:

$$
SE = \frac{0.5}{\sqrt{30}} \approx 0.091
$$

Thus, the 95% CI for the thermometer's readings would be:

$$
CI = 37.0 \pm 1.96 \times 0.091 \approx (37.0 \pm 0.178) = (36.822, 37.178)
$$

The acceptable calibration error range would therefore be from 36.822°C to 37.178°C to be 95% confident in the thermometer's accuracy.

### Misconceptions and Clarifications

It's a common misconception that a 95% CI means there's a 95% chance the true mean lies within the interval. Instead, the correct interpretation is that 95% of such constructed intervals from repeated random sampling will contain the true mean. This distinction emphasizes the reliability of the interval estimation process, not the probability of a specific interval.
