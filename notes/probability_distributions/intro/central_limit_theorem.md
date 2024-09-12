## Central Limit Theorem (CLT)

The Central Limit Theorem (CLT) is a fundamental concept in statistics, explaining why the distribution of sample means approximates a normal distribution, often known as the bell curve, as the sample size becomes larger, irrespective of the population's original distribution.

### Mathematical Background

- The CLT states that if you have a population with a mean $\mu$ and a standard deviation $\sigma$, and you take sufficiently large random samples from this population (with replacement), then the distribution of the sample means will approximate a normal distribution.
- The mean of the sample means ($\bar{X}$) will be approximately equal to the population mean ($\mu$).
- The standard deviation of the sample means, also known as the standard error, will be $\frac{\sigma}{\sqrt{n}}$, where $n$ is the sample size.

### Formal Description

Let $X_1, X_2, \ldots, X_n$ be a sequence of independent and identically distributed random variables, each with a mean $\mu$ and a variance $\sigma^2$.

As $n$ (the sample size) tends to infinity, the distribution of the standardized sum

$$\frac{X_1 + X_2 + \ldots + X_n - n\mu}{\sigma\sqrt{n}}$$

converges in distribution to a standard normal distribution. Mathematically, this is expressed as:

$$P\left(\frac{X_1 + X_2 + \ldots + X_n - n\mu}{\sigma\sqrt{n}} \leq a\right) \to \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{a} e^{-x^2/2} \, dx$$

Key Points:

1. "Large" is typically considered to be a sample size of 30 or more, though this can vary based on the distribution's initial shape.
2. Samples should be independent of each other.
3. It's the distribution of the means (and other statistics like sum and percentage) of these samples that becomes normal, not the distribution of the individual data points (it can still be skewed).

### Implications and Applications

The CLT allows us to use the normal distribution to approximate probabilities and percentages in large samples. For instance:

In an online game where you have a 20% chance of winning a small prize, the number of small prizes won in nn plays follows a binomial distribution, which can be approximated by a normal distribution when nn is large.

- The CLT is applicable to almost any population distribution, given a sufficiently large sample size. This includes distributions that are not normally distributed.
- It allows statisticians to make inferences about population parameters using sample statistics, particularly when dealing with large datasets.
- It underpins many statistical procedures and experiments, where it's often impractical or impossible to observe an entire population.

### Limitations

- **Sample Size**: The theorem applies only when the sample size is large enough. "Large enough" varies depending on the underlying distribution, but a common rule of thumb is a sample size greater than 30.
- **Independence**: The sampled values must be independent of each other. This assumption can be violated in many real-world scenarios.

### Visualization

A histogram of the sample means will tend to form a bell-shaped curve as the number of samples increases, reflecting the normal distribution predicted by the CLT.

#### Data Generation

- **Population Data**: Generated from a non-normal (exponential) distribution.
- **Distribution Used**: Exponential distribution with a scale parameter of 1.0.
- **Population Size**: 10,000 data points.
- **Sample Details**: Number of Samples = 1000, Sample Size = 50.

The plot below shows the non-normal exponential distribution, which is right-skewed:

![output(8)](https://github.com/user-attachments/assets/66b67dc3-a589-41a3-b812-0b9fb347f78b)

#### Distribution of Sample Means 

- **Method**: For each of the 1000 samples, a sample mean is calculated.
- **Formula**: $\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i$, where $\bar{x}$ is the sample mean, $n$ is the sample size, and $x_i$ are the data points in the sample.

The second plot demonstrates the distribution of sample means, where the sample means form a bell-shaped (approximately normal) distribution, even though the original population is non-normal. This illustrates the Central Limit Theorem in action.

![output(9)](https://github.com/user-attachments/assets/207b027a-b3f9-4d92-beca-c7a1517de754)

- **Mean of Population Data**: Approximately 0.9775.
- **Mean of Sample Means**: Also approximately 0.9843. This indicates that the average of the sample means is very close to the population mean, aligning with the CLT's prediction.
- **Standard Error**: Calculated as $\frac{\sigma}{\sqrt{n}}$, where $\sigma$ is the population standard deviation and $n$ is the sample size. The calculated standard error was approximately 0.1378.
- The histogram of the sample means formed a bell-shaped curve, indicating a normal distribution as predicted by the Central Limit Theorem.
- The close alignment of the mean of the sample means with the population mean, and the calculated standard error, further confirm the theorem's predictions.
- This example underscores the theorem's key insight: for a sufficiently large sample size, the sampling distribution of the sample mean will approximate a normal distribution, regardless of the population's original distribution.

### Standardizing Using CLT

    To standardize a sample statistic:
    z=statistic−expected valueSE of the statistic
    z=SE of the statisticstatistic−expected value​
    For example, if we sample nn incomes with population mean μ=67,000μ=67,000 and standard deviation σ=38,000σ=38,000, the standard error for the sample mean is:
    SE(xˉn)=38,000n
    SE(xˉn​)=n

​38,000​

### Example: Applying CLT

Consider a scenario where the heights of a certain plant species are normally distributed with a population mean $\mu = 15$ cm and a population standard deviation $\sigma = 3$ cm. We will analyze random samples of different sizes and calculate the probability that the sample mean falls between 14 cm and 16 cm.

#### Definitions:

- $\mu = 15$: Population mean height.
- $\sigma = 3$: Population standard deviation of heights.
- $n$: Sample size.
- Standard Error of the Mean (SEM): $\text{SEM} = \frac{\sigma}{\sqrt{n}}$.
- Z-score formula: $Z = \frac{X - \mu_{\text{sample mean}}}{\text{SEM}}$.

We will calculate the probability that the sample mean is between 14 cm and 16 cm for various sample sizes.

#### Step 1: Sample Size of 16 Plants

**Goal**: Estimate the probability that the sample mean height of 16 plants lies between 14 cm and 16 cm.

1. **Calculate the Standard Error of the Mean (SEM)**:
   $$
   \text{SEM} = \frac{\sigma}{\sqrt{n}} = \frac{3}{\sqrt{16}} = \frac{3}{4} = 0.75
   $$
   
2. **Calculate the Z-scores for 14 cm and 16 cm**:
   - For $X = 14$:
     $$
     Z_{14} = \frac{14 - 15}{0.75} = \frac{-1}{0.75} = -1.33
     $$
   - For $X = 16$:
     $$
     Z_{16} = \frac{16 - 15}{0.75} = \frac{1}{0.75} = 1.33
     $$

3. **Find the probabilities associated with the Z-scores**:
   Using standard normal distribution tables (or a calculator):
   - $P(Z \leq -1.33) \approx 0.0918$
   - $P(Z \leq 1.33) \approx 0.9082$
   
4. **Calculate the probability that the sample mean lies between 14 and 16 cm**:
   $$
   P(14 \leq \bar{X} \leq 16) = P(Z \leq 1.33) - P(Z \leq -1.33)
   $$
   $$
   P(14 \leq \bar{X} \leq 16) = 0.9082 - 0.0918 = 0.8164
   $$
   Thus, the probability is approximately **81.64%**.

#### Step 2: Sample Size of 64 Plants

**Goal**: Estimate the probability that the sample mean height of 64 plants lies between 14 cm and 16 cm.

1. **Calculate the Standard Error of the Mean (SEM)**:
   $$
   \text{SEM} = \frac{\sigma}{\sqrt{n}} = \frac{3}{\sqrt{64}} = \frac{3}{8} = 0.375
   $$

2. **Calculate the Z-scores for 14 cm and 16 cm**:
   - For $X = 14$:
     $$
     Z_{14} = \frac{14 - 15}{0.375} = \frac{-1}{0.375} = -2.67
     $$
   - For $X = 16$:
     $$
     Z_{16} = \frac{16 - 15}{0.375} = \frac{1}{0.375} = 2.67
     $$

3. **Find the probabilities associated with the Z-scores**:
   Using standard normal distribution tables (or a calculator):
   - $P(Z \leq -2.67) \approx 0.0038$
   - $P(Z \leq 2.67) \approx 0.9962$

4. **Calculate the probability that the sample mean lies between 14 and 16 cm**:
   $$
   P(14 \leq \bar{X} \leq 16) = P(Z \leq 2.67) - P(Z \leq -2.67)
   $$
   $$
   P(14 \leq \bar{X} \leq 16) = 0.9962 - 0.0038 = 0.9924
   $$
   Thus, the probability is approximately **99.24%**.

#### Step 3: Sample Size of 144 Plants

**Goal**: Estimate the probability that the sample mean height of 144 plants lies between 14 cm and 16 cm.

1. **Calculate the Standard Error of the Mean (SEM)**:
   $$
   \text{SEM} = \frac{\sigma}{\sqrt{n}} = \frac{3}{\sqrt{144}} = \frac{3}{12} = 0.25
   $$

2. **Calculate the Z-scores for 14 cm and 16 cm**:
   - For $X = 14$:
     $$
     Z_{14} = \frac{14 - 15}{0.25} = \frac{-1}{0.25} = -4
     $$
   - For $X = 16$:
     $$
     Z_{16} = \frac{16 - 15}{0.25} = \frac{1}{0.25} = 4
     $$

3. **Find the probabilities associated with the Z-scores**:
   Using standard normal distribution tables (or a calculator):
   - $P(Z \leq -4) \approx 0.00003$
   - $P(Z \leq 4) \approx 0.99997$

4. **Calculate the probability that the sample mean lies between 14 and 16 cm**:
   $$
   P(14 \leq \bar{X} \leq 16) = P(Z \leq 4) - P(Z \leq -4)
   $$
   $$
   P(14 \leq \bar{X} \leq 16) = 0.99997 - 0.00003 = 0.99994
   $$
   Thus, the probability is approximately **99.99%**.

#### Step 4: Unknown Population Distribution

**Goal**: Estimate the probability for the same range if the population distribution is unknown.

If the distribution of plant heights is unknown, the Central Limit Theorem assures us that the sampling distribution of the sample mean will still approximate normality as long as the sample size is sufficiently large (usually $n \geq 30$).

#### CLT Estimation:
- For a sample size $n = 64$ (as in Step 2), the sampling distribution of the sample mean will still be approximately normal, even if the population distribution is not normal.
- Therefore, the same calculations as in Step 2 can be applied, and the probability remains approximately **99.24%**.
