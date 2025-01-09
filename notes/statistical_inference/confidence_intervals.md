## Confidence Intervals

Confidence intervals (CIs) provide a range of values which are believed, with a certain degree of confidence, to contain a population parameter, like the mean or proportion. They are constructed from a sampled data set and offer an interval estimate for the parameter of interest.

### Definition and Components

A **confidence interval (CI)** provides a range of values within which we expect a population parameter (such as a mean or proportion) to lie, based on sample data. It is typically expressed as:

$$
(\text{Point Estimate} - \text{Margin of Error}, \ \text{Point Estimate} + \text{Margin of Error})
$$

Where:

- **Point Estimate** is the best single estimate for a population parameter based on the sample data (e.g., the sample mean).
- **Margin of Error** represents the extent of uncertainty around the point estimate. It depends on the standard error and a critical value from a distribution (typically a normal or t-distribution) appropriate for the selected confidence level.

The formula for the margin of error is:

$$
\text{Margin of Error} = \text{Critical Value} \times \text{Standard Error}
$$

The **confidence level** (e.g., 90%, 95%, or 99%) reflects how confident we are that the interval contains the true population parameter. A higher confidence level implies a wider interval, offering greater certainty but less precision.

#### Example: Confidence Interval for the Mean

Suppose we generate sample data from a population with a true mean of 50 and a standard deviation of 5. Based on this sample, we calculate the sample mean and construct a confidence interval around it.

![confidence_interval_mean_example](https://github.com/djeada/Statistics-Notes/assets/37275728/1c398ecf-066c-4211-be9c-9fce04c3fb8e)

In this example:

- The **red dashed line** represents the sample mean, which is the point estimate for the population mean.
- The **green and blue dashed lines** represent the lower and upper bounds of the 95% confidence interval, respectively. 

This interval suggests that we can be 95% confident that the true mean lies between the lower and upper bounds. Note that the true population mean may or may not fall within this interval in any particular sample, but over many repeated samples, 95% of such intervals will capture the true mean.

#### Example: Confidence Intervals for Simulated Stock Returns

![confidence_interval_stock_returns](https://github.com/user-attachments/assets/6ef55b49-6c87-4c69-985c-8c6703f6e554)

The plot above shows confidence intervals for simulated stock returns at various confidence levels (90%, 95%, and 99%). Here’s what the visualization shows:

- **Lower Bound (Red)**: The lower limit of the confidence interval decreases as the confidence level increases. This widening reflects the need for a larger range to ensure that the true mean is captured at higher confidence levels.
- **Upper Bound (Green)**: Similarly, the upper limit increases as the confidence level increases.
- **Shaded Area**: The gray area represents the width of the confidence interval. As the confidence level increases, this shaded region expands, indicating a trade-off between precision and certainty.

The horizontal line at zero helps indicate whether the confidence intervals capture positive or negative stock returns.

Key Insights:

- At **90% confidence**, the interval is narrow, offering more precision but less certainty.
- At **99% confidence**, the interval is wider, reflecting greater certainty that the true mean is within the range but with reduced precision.

This demonstrates the key trade-off in confidence intervals, namely as you increase the confidence level, the interval becomes wider, sacrificing precision to gain certainty.

### Confidence Interval Construction

Suppose 62% of 150 million likely voters approve of the President. A Gallup poll surveys 1,200 voters to estimate this percentage, but the result includes some sampling error. The standard error (SE) quantifies this error.

#### Step 1: Use the Central Limit Theorem (CLT)

According to the CLT, the sample proportion (or mean) follows a normal distribution. For example, in this case, where 62% of likely voters approve of the President's performance, we can calculate the standard error (SE) for the sample proportion as follows:

$$
SE = \sqrt{\frac{p(1 - p)}{n}}
$$

Where:

- $p = 0.62$ is the population proportion.
- $n = 1,200$ is the sample size.

Substitute the values into the formula:

$$
SE = \sqrt{\frac{0.62 \times 0.38}{1,200}} = \sqrt{\frac{0.2356}{1,200}} = \sqrt{0.0001963} = 0.014 \text{ or } 1.4\\%
$$

This means the standard error is approximately 1.4%.

#### Step 2: Construct the 95% Confidence Interval

According to the empirical rule (or 68-95-99.7 rule), there is a 95% chance that the sample proportion is within 2 standard errors (SEs) of the true population proportion.

For example, if the sample result from the Gallup poll is 60%, we can calculate the 95% confidence interval as:

$$
\text{Confidence Interval} = [\hat{p} \pm 2 \times SE]
$$

Where:

- $\hat{p} = 60\%$ is the sample proportion.
- $SE = 1.4\%$ is the standard error.

Thus, the confidence interval is:

$$
60\\% \pm 2 \times 1.4\\% = 60\\% \pm 2.8\\% = 57.2\\% \text{ to } 62.8\\%
$$

This means we are 95% confident that the true population approval percentage falls between 57.2% and 62.8%.

#### Step 3: Understanding "Confidence" vs. "Probability"

The term "95% confidence" refers to the long-run success of this sampling method. Specifically:

- The population parameter (e.g., the true approval percentage) is a fixed value, denoted by $\mu$, which either falls within the interval or does not.
- The "95% confidence" means that if we repeated this polling procedure many times, 95% of the resulting confidence intervals would contain the true population parameter.
- However, for any single interval, we cannot say the population proportion is within the interval with 95% probability, since the parameter itself is fixed. Instead, we are confident that the method of constructing the interval is accurate in 95% of cases.

### Confidence Level and Z-Scores

The **confidence level** represents how confident we are that a calculated interval contains the true population parameter (e.g., mean or proportion). Common confidence levels and their corresponding Z-scores are:

- **95% confidence level** → $z = 1.96$
- **90% confidence level** → $z = 1.65$
- **99% confidence level** → $z = 2.58$

The formula for constructing a confidence interval is:

$$
\text{Confidence Interval} = \text{estimate} \pm z \times SE
$$

Where:

- "Estimate" refers to the sample statistic (e.g., mean or proportion).
- $z$ is the Z-score corresponding to the desired confidence level.
- $SE$ is the standard error.

### Bootstrap Principle for Estimating Standard Error (SE)

When the population standard deviation ($\sigma$) is unknown, we can use the **bootstrap principle** to estimate it. The bootstrap principle uses the sample standard deviation ($s$) as an approximation for the unknown population standard deviation ($\sigma$).

Example: In a survey where 60% of the sample approves of the President’s job, the standard error (SE) can be estimated as follows:

$$
SE = \sqrt{\frac{p(1 - p)}{n}}
$$

Where:

- $p = 0.60$ is the sample proportion.
- $n = 1,000$ is the sample size.

Substitute the values:

$$
SE = \sqrt{\frac{0.60 \times 0.40}{1,000}} = \sqrt{\frac{0.24}{1,000}} = \sqrt{0.00024} = 0.0155 \text{ or } 1.55\\%
$$

#### Constructing the Confidence Interval

Using the **95% confidence level** ($z = 1.96$), the confidence interval is calculated as:

$$
\text{Confidence Interval} = 60\\% \pm 1.96 \times 1.55\\%
$$

$$
\text{Confidence Interval} = 60\\% \pm 3.04\% = 56.96\\% \text{ to } 63.04\\%
$$

This means we are 95% confident that the true approval rating lies between 56.96% and 63.04%.

### Width of Confidence Intervals and Margin of Error

The **width** of a confidence interval is determined by the **margin of error**, which is calculated as:

$$
\text{Margin of Error} = z \times SE
$$

Where:

- $z$ is the Z-score corresponding to the desired confidence level.
- $SE$ is the standard error of the sample statistic.

Impact:

- A larger **sample size** reduces the standard error, which in turn decreases the margin of error and narrows the confidence interval. However, to **halve the width** of a confidence interval, the sample size must be increased by a factor of four. This is because the standard error is inversely proportional to the square root of the sample size.
- Reducing the **confidence level** (e.g., from 95% to 90%) decreases the Z-score, which reduces the width of the confidence interval. However, this comes at the cost of reduced certainty that the interval contains the true population parameter.

### Confidence Level and Interpretation

The **confidence level** indicates the proportion of confidence intervals, constructed from repeated samples, that would capture the true population parameter. Common confidence levels are 90%, 95%, and 99%. For example, a 95% confidence level means that if we were to take 100 different samples and calculate confidence intervals (CIs) for each, we expect about 95 of those intervals to contain the true population parameter.

### Example: Health App Steps Count

Consider two health apps estimating daily steps:

- **App X**: Reports an average of 10,300 steps/day.
- **App Y**: Provides a 90% CI for the average as 10,000 ± 500 steps/day (i.e., 9,500 to 10,500 steps/day).

App Y, by including a confidence interval, acknowledges the inherent variability in the data and offers a more reliable range, assuming its data collection methods are sound.

### 95% Confidence Interval for a Parameter

When the distribution of the point estimate follows the **Central Limit Theorem** (i.e., when sample sizes are sufficiently large), the estimate tends to follow a normal distribution. In this case, we can construct a 95% confidence interval using the formula:

$$
\text{Point Estimate} \pm 1.96 \times SE
$$

The value **1.96** comes from the standard normal distribution, where 95% of the data falls within 1.96 standard deviations from the mean.

### Example: Carry-on Baggage Weight

Suppose the average weight of a sample of carry-on bags is 3.2 kg with a standard error (SE) of 0.053 kg. To calculate the 95% CI:

$$
\text{Confidence Interval} = \text{Sample Mean} \pm (\text{Critical Value} \times \text{Standard Error})
$$

For a 95% confidence level, the critical value (Z-score) is approximately 1.96. Therefore:

$$
\text{Confidence Interval} = 3.2 \pm (1.96 \times 0.053) = (3.09612, \ 3.30388)
$$

This interval suggests that the true mean weight of all carry-on bags is likely between **3.09612 kg** and **3.30388 kg**, with 95% confidence.

### Example: Calibrating a Digital Thermometer

When calibrating a digital thermometer, it's important to determine an error range such that the thermometer reflects the actual temperature with 95% accuracy. For a normal distribution, 95% of the data lies within 1.96 standard deviations from the mean. Thus, the calibration error should be set to **1.96 times the standard error (SE)** around the expected mean reading.

The formula for a 95% Confidence Interval (CI) for the thermometer’s temperature reading ($T$) is:

$$
CI = T \pm Z \times SE
$$

Where:
- $T$ is the mean temperature reading.
- $Z$ is the Z-score for the 95% confidence level, which is 1.96.
- $SE$ is the standard error, calculated as:

$$
SE = \frac{\sigma}{\sqrt{n}}
$$

Where $\sigma$ is the standard deviation of the thermometer’s readings and $n$ is the number of trials.

Suppose the thermometer was tested over 30 trials, yielding a mean reading ($T$) of 37.0°C with a standard deviation ($\sigma$) of 0.5°C. We calculate the standard error (SE) as:

$$
SE = \frac{0.5}{\sqrt{30}} \approx 0.091
$$

Now, using this SE to find the 95% CI:

$$
CI = 37.0 \pm (1.96 \times 0.091) \approx 37.0 \pm 0.178 = (36.822, 37.178)
$$

Thus, the acceptable calibration range for the thermometer is from **36.822°C to 37.178°C**, meaning we can be 95% confident that the true temperature lies within this interval.

### Misconceptions and Clarifications

A common misconception about confidence intervals (CIs) is to interpret them as saying, "There is a 95% chance that the true mean lies within this specific interval." This is **incorrect** because the true population parameter (like the mean) is fixed, not random. The interval calculated from the sample data either **contains** the true mean, or it **does not**—there's no probability attached to this fact for a single interval.

The correct interpretation is that if we were to repeatedly sample from the population and construct a confidence interval for each sample, **95% of those intervals would contain the true mean** (for a 95% confidence level). This reflects the **long-term reliability** of the method used to create the intervals, not the probability that a specific interval from a single sample contains the true mean.

#### Changing the Confidence Level

If the point estimate follows a normal distribution with a known standard error (SE), the confidence interval for the population parameter is given by:

$$
\text{Point Estimate} \pm z^* \times SE
$$

Where:
- $z^*$ is the critical value corresponding to the selected confidence level (e.g., 1.645 for 90%, 1.96 for 95%, 2.576 for 99%).
- $z^* \times SE$ is the **margin of error**, which determines the width of the confidence interval.

#### Example: Blood Pressure Readings

Consider a case where the blood pressure readings of a group of patients are normally distributed, but the population mean is unknown. The population standard deviation is 12 mmHg, and a random sample of 50 patients has a sample mean of 130 mmHg. We will calculate the 90% and 99% confidence intervals for the population mean blood pressure.

##### Step 1: Calculate the Standard Error (SE)

The standard error is calculated as:

$$
SE = \frac{\sigma}{\sqrt{n}} = \frac{12}{\sqrt{50}} \approx 1.697
$$

##### Step 2: Determine Critical Values ($z^*$)

- For a **90% confidence level**, $z^*$ is approximately 1.645.
- For a **99% confidence level**, $z^*$ is approximately 2.576.

##### Step 3: Calculate the Confidence Intervals

**90% Confidence Interval:**

$$
130 \pm 1.645 \times 1.697 = 130 \pm 2.79 = (127.21, 132.79)
$$

**99% Confidence Interval:**

$$
130 \pm 2.576 \times 1.697 = 130 \pm 4.37 = (125.63, 134.37)
$$

#### Interpretation of Results

- With **90% confidence**, we can state that the true mean blood pressure of the population is likely between **127.21 mmHg** and **132.79 mmHg**.
- With **99% confidence**, we can state that the true mean is likely between **125.63 mmHg** and **134.37 mmHg**.

Note how the **99% confidence interval** is wider than the **90% confidence interval**. This reflects the trade-off between **certainty** (higher confidence levels) and **precision** (narrower intervals).
