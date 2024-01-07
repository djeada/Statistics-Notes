## Central Limit Theorem (CLT)

The Central Limit Theorem is a fundamental statistical principle that explains why many distributions tend to approximate a normal distribution (bell curve) as their sample size increases, regardless of the shape of the population distribution.

### Mathematical Background

- **Statement**: If you have a population with mean $\mu$ and standard deviation $\sigma$, and take sufficiently large random samples from the population (with replacement), then the distribution of the sample means will be approximately normally distributed.
- **Formula**: 
  - The mean of the sample means will be approximately equal to the population mean ($\mu$).
  - The standard deviation of the sample means (standard error) will be $\frac{\sigma}{\sqrt{n}}$, where $n$ is the sample size.

### Key Points

1. **Sufficiently Large Samples**: "Large" is typically considered to be a sample size of 30 or more, though this can vary based on the distribution's initial shape.

2. **Independence**: Samples should be independent of each other.

3. **Sample Means**: It's the distribution of the means of these samples that becomes normal, not the distribution of the individual data points.

### Applications

- **Estimation**: The CLT allows for the estimation of population parameters using sample statistics.
- **Inferential Statistics**: Fundamental to hypothesis testing, confidence interval estimation, and many other inferential statistics techniques.

### Example

Consider a population with a non-normal distribution (e.g., skewed to the right). If you were to take 1000 samples of size 50 from this population and calculate the mean of each sample:

- According to the CLT, the distribution of these 1000 sample means will be approximately normal.
- The mean of these sample means will be close to the true population mean $\mu$.
- The standard error (standard deviation of the sample means) will be $\frac{\sigma}{\sqrt{50}}$, assuming $\sigma$ is the population standard deviation.

### Visualization

A histogram of the sample means will tend to form a bell-shaped curve as the number of samples increases, reflecting the normal distribution predicted by the CLT.

#### Data Generation

- **Population Data**: Generated from a non-normal (exponential) distribution.
- **Distribution Used**: Exponential distribution with a scale parameter of 1.0.
- **Population Size**: 10,000 data points.
- **Sample Details**:
  - Number of Samples: 1000
  - Sample Size: 50

#### Calculation of Sample Means

- **Method**: For each of the 1000 samples, a sample mean is calculated.
- **Formula**: $\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i$, where $\bar{x}$ is the sample mean, $n$ is the sample size, and $x_i$ are the data points in the sample.

#### Visualization

- A histogram is created to show the distribution of these 1000 sample means.
- According to the Central Limit Theorem, this distribution should approximate a normal distribution.

![fbb216aa-d334-4871-bd7d-bbc581bcb657](https://github.com/djeada/Statistics-Notes/assets/37275728/fba99241-8f11-4cc2-98ac-5951bd02e6f7)

#### Statistical Results

- **Mean of Population Data**: Approximately 1.01.
- **Mean of Sample Means**: Also approximately 1.01.
  - This indicates that the average of the sample means is very close to the population mean, aligning with the CLT's prediction.

- **Standard Error**: Calculated as $\frac{\sigma}{\sqrt{n}}$, where $\sigma$ is the population standard deviation and $n$ is the sample size.
  - The calculated standard error was approximately 0.14.

#### Conclusion

- The histogram of the sample means formed a bell-shaped curve, indicating a normal distribution as predicted by the Central Limit Theorem.
- The close alignment of the mean of the sample means with the population mean, and the calculated standard error, further confirm the theorem's predictions.
- This example underscores the theorem's key insight: for a sufficiently large sample size, the sampling distribution of the sample mean will approximate a normal distribution, regardless of the population's original distribution.


### Limitations

- The CLT does not apply to small samples.
- The approximation to a normal distribution might not be good if the original population is extremely non-normal.

