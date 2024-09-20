## The Normal Curve and Z-Scores

### The Normal Curve

A **normal distribution** (often referred to as the *normal curve* or *Gaussian distribution*) is a continuous probability distribution that is symmetric about the mean, where most of the observations cluster around the central peak and taper off symmetrically towards both ends. Many real-world datasets such as human heights, IQ scores, and measurement errors exhibit this kind of distribution.

The probability density function (PDF) of the normal distribution is given by:

$$
f(x | \mu, \sigma^2) = \frac{1}{\sigma \sqrt{2 \pi}} e^{ -\frac{(x - \mu)^2}{2\sigma^2} }
$$

where:

- $\mu$ is the mean,
- $\sigma^2$ is the variance (with $\sigma$ being the standard deviation),
- $e$ is Euler's number,
- $\pi$ is the constant Pi.

This formula describes the shape of the curve mathematically. The mean $\mu$ determines the center of the distribution, and the standard deviation $\sigma$ determines the width of the bell curve.

![output](https://github.com/user-attachments/assets/32acef3f-7617-464c-9527-31ea78679bda)

#### Examples

- The distribution of adult **heights** usually follows a normal pattern, where most individuals cluster around the average height, with fewer people being much shorter or taller.
- When it comes to **IQ scores**, they are designed to follow a normal distribution, with the average score set at 100 and a standard deviation of 15, meaning most people score close to this mean.
- Not all data sets are normally distributed; for example, **incomes** tend to be skewed because a small proportion of people earn extremely high salaries, which significantly raises the overall average.
- Similarly, **house prices** are often skewed, as a small number of very expensive properties can disproportionately affect the overall data, making the mean house price higher than what most people actually pay.

### The Empirical Rule (68-95-99.7 Rule)

The **Empirical Rule** provides a rough estimate for the spread of data in a normal distribution. It applies to any dataset that approximately follows the normal distribution.

- **68% of the data** falls within **1 standard deviation** of the mean, i.e., between $\mu - \sigma$ and $\mu + \sigma$.
- **95% of the data** falls within **2 standard deviations** of the mean, i.e., between $\mu - 2\sigma$ and $\mu + 2\sigma$.
- **99.7% of the data** falls within **3 standard deviations** of the mean, i.e., between $\mu - 3\sigma$ and $\mu + 3\sigma$.

#### Example
Suppose we have a dataset where the heights of fathers are normally distributed with:

- Mean height $\mu = 68.3$ inches,
- Standard deviation $\sigma = 1.8$ inches.

According to the Empirical Rule:

- About **68%** of the heights will lie between $68.3 - 1.8 = 66.5$ inches and $68.3 + 1.8 = 70.1$ inches.
- About **95%** of the heights will lie between $68.3 - 2(1.8) = 64.7$ inches and $68.3 + 2(1.8) = 71.9$ inches.
- About **99.7%** of the heights will lie between $68.3 - 3(1.8) = 62.9$ inches and $68.3 + 3(1.8) = 73.7$ inches.

These intervals can be visualized as follows:

$$
\text{Interval} \quad \mu \pm n\sigma \quad \text{Proportion of Data Contained}
$$

$$
\mu \pm \sigma \quad (66.5 \text{ to } 70.1) \quad \approx 68\%
$$

$$
\mu \pm 2\sigma \quad (64.7 \text{ to } 71.9) \quad \approx 95\%
$$

$$
\mu \pm 3\sigma \quad (62.9 \text{ to } 73.7) \quad \approx 99.7\%
$$

![output(1)](https://github.com/user-attachments/assets/b157d1a4-191d-46f4-b341-7822d4257733)

### Standardizing Data and Z-Scores

To compare values from different normal distributions or to work with a standardized form of a dataset, we can convert raw data values to **z-scores**.

#### Definition of Z-Score
The **z-score** is a way of describing a value in terms of how many standard deviations it is away from the mean. The formula for the z-score is:

$$
z = \frac{x - \mu}{\sigma}
$$

Where:

- $x$ is the raw score (the value you are standardizing),
- $\mu$ is the mean of the dataset,
- $\sigma$ is the standard deviation.

A z-score tells us:

- $z = 0$: The value is exactly at the mean.
- $z > 0$: The value is above the mean.
- $z < 0$: The value is below the mean.

#### Example
Suppose a father is 71.9 inches tall. We want to find his z-score given that the mean height is 68.3 inches and the standard deviation is 1.8 inches.

$$
z = \frac{71.9 - 68.3}{1.8} = \frac{3.6}{1.8} = 2
$$

This means that a height of 71.9 inches is 2 standard deviations above the mean.

Conversely, if a father is 67.4 inches tall:

$$
z = \frac{67.4 - 68.3}{1.8} = \frac{-0.9}{1.8} = -0.5
$$

This means that a height of 67.4 inches is 0.5 standard deviations below the mean.

#### Standard Normal Distribution
After converting all values in a normal distribution to z-scores, we obtain the **standard normal distribution**, which has:

- A mean $\mu = 0$,
- A standard deviation $\sigma = 1$.

The standard normal distribution is often used in statistics because it allows for easy computation of probabilities and comparison across different datasets.

### Finding Areas Under the Normal Curve

To find the proportion of data within a certain range, we can use **z-scores** to convert the raw data points and then look up the corresponding probabilities using a **z-table** or statistical software. The area under the normal curve between two z-scores represents the proportion of data that lies between those values.

#### Example
To find the proportion of fathers with heights between 67.4 inches and 71.9 inches, we first compute the z-scores for these heights:

For 67.4 inches:

$$
z_{67.4} = \frac{67.4 - 68.3}{1.8} = -0.5
$$

For 71.9 inches:

$$
z_{71.9} = \frac{71.9 - 68.3}{1.8} = 2
$$

Next, using a z-table (or software), we find the area to the left of these z-scores:

- The area to the left of $z = -0.5$ is approximately **0.3085** (30.85%).
- The area to the left of $z = 2$ is approximately **0.9772** (97.72%).

Thus, the proportion of fathers with heights between 67.4 and 71.9 inches is:

$$
P(67.4 \leq \text{height} \leq 71.9) = 0.9772 - 0.3085 = 0.6687 \approx 66.87\%
$$

![output(2)](https://github.com/user-attachments/assets/58bfcf9b-5769-4e49-af1c-7cced5a44195)

### Computing Percentiles

The **percentile** of a value in a normal distribution tells us the percentage of the data that is less than or equal to that value. To compute percentiles, we:

1. Find the z-score corresponding to the desired percentile using a z-table or statistical software.
2. Convert the z-score back into the raw data value.

#### Example
Suppose we want to compute the **30th percentile** of fathers' heights. Using a z-table, we find that the z-score corresponding to the 30th percentile is approximately $z = -0.52$.

To find the corresponding height, we use the z-score formula in reverse:

$$
\text{height} = \mu + z\sigma = 68.3 + (-0.52)(1.8) = 68.3 - 0.936 = 67.364 \text{ inches}.
$$

Thus, the 30th percentile corresponds to a height of approximately **67.36 inches**.

This process can be applied to any percentile by finding the appropriate z-score and converting it back to the original scale using the mean and standard deviation of the dataset.
