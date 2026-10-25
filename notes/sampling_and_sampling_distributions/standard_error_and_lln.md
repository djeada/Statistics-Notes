# Standard Error and Law of Large Numbers

## Expected Value

**Expected Value (E)**, also known as the mean, is the long-run average of a random variable, representing the value we anticipate on average from repeated random draws from a population.

I. For a single random draw from a population with mean $\mu$, the expected value is given by:

$$
E(X) = \mu
$$

II. For a sample of size $n$, the expected value of the sample mean $\bar{x}_n$ is equal to the population mean:

$$
E(\bar{x}_n) = \mu
$$

This is the statement that the sample mean is an unbiased estimator of the population mean; it follows from linearity of expectation.

## Standard Error

**Standard Error (SE)** quantifies the dispersion or variability of a sample statistic, such as the sample mean, from its expected value. It reflects the precision of the sample statistic as an estimator of the population parameter.

The standard error is defined as the standard deviation of the sample mean's sampling distribution. For independent observations with a common finite variance $\sigma^2$, this definition gives:

$$
SE(\bar{x}_n) = \frac{\sigma}{\sqrt{n}}
$$

where:

- $\sigma$ is the population standard deviation, and
- $n$ is the sample size.

As $n$ increases, $SE(\bar{x}_n)$ decreases, implying that larger samples yield more precise estimates of the population mean. The relationship between the standard error and the sample size follows an inverse square root law, meaning that quadrupling the sample size halves the standard error. This emphasizes the diminishing returns effect in terms of accuracy gained by increasing the sample size. When $\sigma$ is unknown it is replaced by the sample standard deviation $s$, giving the estimated standard error $s/\sqrt{n}$.

### Standard Error for the Sum and Percentages

When dealing with the sum of random draws rather than the sample mean, the expected value and standard error follow these formulas:

I. **Expected Value for the Sum**

The expected value of the sum is the total number of draws $n$ multiplied by the population mean $\mu$:

$$
E(S_n) = n \mu
$$

For example, if $\mu = 5$ and $n = 100$, then:

$$
E(S_n) = 100 \times 5 = 500
$$

This means that, on average, the sum of 100 random draws would be 500.

II. **Standard Error for the Sum**

The standard error of the sum increases with the square root of the sample size and is calculated as:

$$
SE(S_n) = \sqrt{n} \sigma
$$

where $\sigma$ is the population standard deviation. For example, if $\sigma = 2$ and $n = 100$, then:

$$
SE(S_n) = \sqrt{100} \times 2 = 10 \times 2 = 20
$$

This means that the standard deviation of the sum of 100 draws is 20, reflecting the expected variability in the sum.

These values locate the center and a one-standard-error scale for the sum. They do not alone specify a coverage probability. An approximately normal sum has about 68% of its distribution within one standard error of the center; other distributions can have different coverage. The shorthand is:

$$
S_n \approx 500 \pm 20
$$

### Standard Error for Percentages

Percentages are often used in scenarios where the variable is binary, such as 1 for success and 0 for failure. In this case, you are interested in the percentage of 1s (successes) in a sample. The formulas for the expected value and standard error of percentages are closely related to those for the mean and sum but scaled to represent percentages.

I. **Expected Value for Percentages**

The expected value of the percentage of successes is simply the population proportion $\mu$ multiplied by 100 to convert it to a percentage:

$$
E(\text{percentage of 1s}) = \mu \times 100\%
$$

For example, if $\mu = 0.6$ (i.e., 60% of the population are successes), then:

$$
E(\text{percentage of 1s}) = 0.6 \times 100\% = 60\%
$$

This means we expect 60% of the sample to be successes.

II. **Standard Error for Percentages**

The standard error for the percentage of 1s is calculated as:

$$
SE(\text{percentage of 1s}) = \frac{\sigma}{\sqrt{n}} \times 100\%
$$

where $\sigma$ is the population standard deviation for the binary outcome. In the case of a binary variable, the population standard deviation is given by:

$$
\sigma = \sqrt{\mu(1 - \mu)}
$$

For example, if $\mu = 0.6$, then:

$$
\sigma = \sqrt{0.6 \times (1 - 0.6)} = \sqrt{0.6 \times 0.4} = \sqrt{0.24} \approx 0.49
$$

Now, if we take a sample of size $n = 100$, the standard error is:

$$
SE(\text{percentage of 1s}) = \frac{0.49}{\sqrt{100}} \times 100\% = \frac{0.49}{10} \times 100\% = 4.9\%
$$

The estimated sampling spread is 4.9 **percentage points**. This is an absolute difference on the percentage scale: 60% plus 4.9 percentage points is 64.9%. A relative increase of 4.9% would instead multiply 60% by 1.049. The interval below shows one standard-error distance from the expectation and is not a 95% confidence interval:

$$
\text{Percentage of 1s} \approx 60\% \pm 4.9\%
$$

### Law of Large Numbers (LLN)

The Law of Large Numbers (LLN) states that as the sample size $n$ increases, the sample mean $\bar{x}_n$ will tend to converge towards the population mean $\mu$. In other words, the larger the sample size, the closer the sample mean gets to the true mean of the population.

Mathematically, as $n \to \infty$:

$$
\bar{x}_n \to \mu
$$

This principle ensures that with a sufficiently large sample, the sample mean becomes a reliable estimator of the population mean.

There are two forms of the Law of Large Numbers:

- The **Weak Law of Large Numbers** (WLLN) states that for any positive number $\epsilon$, the probability that the sample mean deviates from the population mean by more than $\epsilon$ approaches zero as the sample size grows:

$$
\lim_{n \to \infty} P\left(|\bar{x}_n - \mu| > \epsilon\right) = 0
$$

This is known as convergence in probability. It guarantees that large deviations become increasingly unlikely, but does not rule out occasional deviations for any finite sample.

- The **Strong Law of Large Numbers** (SLLN) provides a stronger guarantee: the sample mean converges to the population mean almost surely, meaning:

$$
P\left(\lim_{n \to \infty} \bar{x}_n = \mu\right) = 1
$$

Almost sure convergence means that, except on a set of infinite sample sequences with probability zero, for every tolerance $\epsilon>0$ there is a point beyond which all subsequent averages remain within that tolerance of $\mu$. They need not equal $\mu$ exactly and can continue fluctuating on progressively smaller scales. For independent, identically distributed observations, $E[|X_1|]<\infty$ is sufficient for both the weak and strong laws. Finite variance is not required for these laws, although it is needed for the finite standard-error calculations used here.

With finite variance, Chebyshev's inequality gives a direct explanation of the weak law:

```math
P(|\bar X_n-\mu|>\epsilon)
\leq\frac{\operatorname{Var}(\bar X_n)}{\epsilon^2}
=\frac{\sigma^2}{n\epsilon^2}\longrightarrow0.
```

This argument bounds the chance of a fixed-size error without assuming a normal distribution. It is a sufficient proof under finite variance; other arguments establish the LLN under the weaker finite-absolute-mean condition stated above.

- **Impact on Standard Error**:

The **Standard Error (SE)** of the sample mean $\bar{x}_n$, which measures the variability of the sample mean around the population mean, decreases as the sample size increases. The SE is given by:

$$
SE(\bar{x}_n) = \frac{\sigma}{\sqrt{n}}
$$

where:

- $\sigma$ is the population standard deviation, and
- $n$ is the sample size.

As $n$ increases, $\sqrt{n}$ increases, and thus the SE decreases. This means that larger samples produce more precise and reliable estimates of the population mean.

For example, if $\sigma = 10$ and:

- For $n = 25$, the standard error is:

$$
SE(\bar{x}_{25}) = \frac{10}{\sqrt{25}} = \frac{10}{5} = 2
$$

- For $n = 100$, the standard error is:

$$
SE(\bar{x}_{100}) = \frac{10}{\sqrt{100}} = \frac{10}{10} = 1
$$

- For $n = 400$, the standard error becomes:

$$
SE(\bar{x}_{400}) = \frac{10}{\sqrt{400}} = \frac{10}{20} = 0.5
$$

As the sample size increases from 25 to 400, the standard error decreases from 2 to 0.5, showing that the estimates of the sample mean become more precise with larger samples.

### Application to Averages and Percentages

The Law of Large Numbers applies to both sample means (averages) and sample proportions (percentages).

I. **For Averages**:
The larger the sample size, the closer the sample mean $\bar{x}_n$ gets to the population mean $\mu$, as shown by the decreasing standard error formula:

$$
SE(\bar{x}_n) = \frac{\sigma}{\sqrt{n}}
$$

II. **For Percentages**:  
The LLN also applies to sample percentages. As the sample size increases, the percentage of successes (or 1s) in the sample gets closer to the true population percentage. The standard error for the sample percentage is given by:

$$
SE(\text{percentage of 1s}) = \frac{\sigma}{\sqrt{n}} \times 100\%
$$

where $\sigma = \sqrt{\mu(1 - \mu)}$ is the standard deviation for binary outcomes.

For example, if $\mu = 0.6$ (i.e., 60% success rate), then $\sigma = \sqrt{0.6 \times 0.4} \approx 0.49$. Now, for different sample sizes, the standard error for percentages becomes:

- For $n = 25$:

$$
SE(\text{percentage}) = \frac{0.49}{\sqrt{25}} \times 100\% = \frac{0.49}{5} \times 100\% = 9.8\%
$$

- For $n = 100$:

$$
SE(\text{percentage}) = \frac{0.49}{\sqrt{100}} \times 100\% = \frac{0.49}{10} \times 100\% = 4.9\%
$$

- For $n = 400$:

$$
SE(\text{percentage}) = \frac{0.49}{\sqrt{400}} \times 100\% = \frac{0.49}{20} \times 100\% = 2.45\%
$$

The standard error decreases as the sample size increases, indicating that larger samples yield more reliable estimates of the population percentage.

III. **Important Note on Sums**:

The law concerns normalized sums: $S_n/n=\bar X_n$. For independent observations with positive finite variance, the unnormalized sum has standard deviation $\sigma\sqrt n$, so its absolute spread increases. Its expectation is $n\mu$: it grows positively for $\mu>0$, decreases for $\mu<0$, and remains zero for $\mu=0$. The mean can become more precise even while the sum's spread grows, because division by $n$ more than offsets that growth.

The standard error for the sum $S_n$ is given by:

$$
SE(S_n) = \sqrt{n} \sigma
$$

As $n$ increases, $\sqrt{n}$ increases, which means the variability of the sum increases with sample size. For $\mu\ne0$, the spread relative to the magnitude of the expectation is $SE(S_n)/|E(S_n)|=\sigma/(|\mu|\sqrt n)$, which shrinks as $n$ grows. This relative measure is undefined when $\mu=0$; concentration of the average still holds, but it must be described by absolute distance from zero rather than division by the expectation.

For example:

- If $\sigma = 10$ and $n = 25$:

$$
SE(S_{25}) = \sqrt{25} \times 10 = 5 \times 10 = 50
$$

- If $n = 100$:

$$
SE(S_{100}) = \sqrt{100} \times 10 = 10 \times 10 = 100
$$

- If $n = 400$:

$$
SE(S_{400}) = \sqrt{400} \times 10 = 20 \times 10 = 200
$$

The standard error for the sum increases with the square root of the sample size, which reflects the growing total sum's variability.

**Note**: all formulas above assume independent draws, such as sampling with replacement or from a very large population. When sampling without replacement from a finite population of size $N$, the standard errors are multiplied by the finite population correction $\sqrt{(N-n)/(N-1)}$.
