# Null Hypotheses and Alternative Hypotheses

In statistical hypothesis testing, we construct two opposing hypotheses to make inferences about a population parameter based on sample data:

1. **Null Hypothesis ($H_0$)**: A statement asserting that there is no effect, no difference, or no change in the population. It represents the default assumption or status quo.

2. **Alternative Hypothesis ($H_1$ or $H_a$)**: A statement that contradicts the null hypothesis, suggesting that there is an effect, a difference, or a change in the population.

The goal is to use statistical evidence from sample data to decide whether to reject the null hypothesis in favor of the alternative hypothesis.

---

![Null Hypothesis Testing Illustration](https://github.com/djeada/Statistics-Notes/assets/37275728/d45fdb61-9d6f-4adf-a54b-4106382d2087)

*Figure: Visualization of the null hypothesis testing process.*

---

## Understanding the Plot

The plot illustrates the distribution of a test statistic under the assumption that the null hypothesis $H_0$ is true. Here's a detailed explanation of the components:

- **Green Curve (Null Distribution)**: Represents the probability density function (pdf) of the test statistic under $H_0$. Often, this is a standard normal distribution centered at zero.

- **Vertical Dashed Red Line**: Indicates the observed value of the test statistic from the sample data (e.g., $z = 2.0$).

- **Orange Shaded Area (Tail Area)**: Represents the probability of observing a test statistic as extreme as or more extreme than the observed value under $H_0$. This area corresponds to the p-value in a one-tailed test. In a two-tailed test, an equivalent area on the opposite tail would also be considered.

---

## The Language of Hypothesis Testing

### Rejecting vs. Failing to Reject $H_0$

- **Reject $H_0$**: If the evidence (based on the p-value) is strong enough, we reject the null hypothesis, suggesting that there is statistically significant evidence in favor of the alternative hypothesis.

- **Fail to Reject $H_0$**: If the evidence is insufficient, we fail to reject the null hypothesis. This does not mean that we accept $H_0$ as true; rather, we do not have enough evidence to conclude that it is false.

### Importance of Precise Terminology

- **Avoid "Accepting" $H_0$**: Statistical tests are designed to assess whether there is sufficient evidence against $H_0$, not to prove that $H_0$ is true.

- **Type I and Type II Errors**:
  - **Type I Error**: Incorrectly rejecting $H_0$ when it is true (false positive).
  - **Type II Error**: Failing to reject $H_0$ when $H_1$ is true (false negative).

---

## Interpretation of the P-value

### Definition

The **p-value** is the probability of obtaining a test statistic at least as extreme as the one observed, assuming that the null hypothesis $H_0$ is true.

### Misconceptions

- **Not the Probability $H_0$ is True**: The p-value does not indicate the probability that $H_0$ is true or false.

- **Large P-value Doesn't Prove $H_0$**: A large p-value means the data are consistent with $H_0$, but it doesn't prove $H_0$ is true.

### Interpretation

- **Small P-value ($p < \alpha$)**: Strong evidence against $H_0$; reject $H_0$.

- **Large P-value ($p \geq \alpha$)**: Insufficient evidence to reject $H_0$; fail to reject $H_0$.

---

## Example: Coin Toss Experiment

### Hypotheses

- **Null Hypothesis ($H_0$)**: The coin is fair; $P(\text{heads}) = 0.5$.

- **Alternative Hypothesis ($H_1$)**: The coin is not fair; $P(\text{heads}) \neq 0.5$.

### Experiment Details

- **Number of Tosses**: $n = 10$.

- **Observed Outcome**: 4 heads and 6 tails.

### Statistical Test

We use the **binomial test** to calculate the p-value for the observed outcome.

#### Calculating the P-value

1. **Compute the probability of observing exactly 4 heads** under $H_0$:

   $$
   P(X = 4) = \binom{10}{4} (0.5)^{4} (0.5)^{6} = \frac{210 \times 0.0625 \times 0.015625}{1} = 0.2051
   $$

2. **Compute the probabilities for more extreme outcomes** (0 to 4 heads and 6 to 10 heads) since it's a two-tailed test.

3. **Total P-value**:

   $$
   \text{p-value} = 2 \times \left( P(X \leq 4) \right) = 2 \times \left( \sum_{k=0}^{4} P(X = k) \right)
   $$

4. **Sum of Probabilities**:

   $$
   \begin{align*}
   P(X = 0) &= 0.00098 \\
   P(X = 1) &= 0.00977 \\
   P(X = 2) &= 0.04395 \\
   P(X = 3) &= 0.11719 \\
   P(X = 4) &= 0.20508 \\
   \sum_{k=0}^{4} P(X = k) &= 0.37697
   \end{align*}
   $$

5. **Compute P-value**:

   $$
   \text{p-value} = 2 \times 0.37697 = 0.75394
   $$

### Decision

- **Significance Level ($\alpha$)**: Typically 0.05.

- **Comparison**: $\text{p-value} = 0.75394 > 0.05$.

- **Conclusion**: Fail to reject $H_0$; insufficient evidence to conclude the coin is biased.

### Interpretation

- **Failing to Reject $H_0$**: We cannot conclude that the coin is unfair based on this data.

- **Not Accepting $H_0$**: The result does not prove the coin is fair; it merely indicates that the observed data are consistent with a fair coin.

---

## Key Takeaways

1. **Null and Alternative Hypotheses**: Formulate clear hypotheses before testing.

2. **P-value**: Understand that it measures the probability of observing the data under $H_0$.

3. **Decision Making**: Use the p-value to decide whether to reject $H_0$, based on the predetermined significance level.

4. **Interpreting Results**: Failing to reject $H_0$ does not confirm it is true.

5. **Sample Size Matters**: Small samples may lack the power to detect significant effects.

---

## Additional Considerations

### Statistical Power

- **Definition**: The probability of correctly rejecting $H_0$ when $H_1$ is true.

- **Influence of Sample Size**: Larger samples increase power.

### One-Tailed vs. Two-Tailed Tests

- **One-Tailed Test**: Tests for an effect in one direction (e.g., $P(\text{heads}) > 0.5$).

- **Two-Tailed Test**: Tests for an effect in either direction (e.g., $P(\text{heads}) \neq 0.5$).

### Confidence Intervals

- Provide an estimated range of values likely to include the population parameter.

- **Relation to Hypothesis Testing**: If the confidence interval for a parameter does not include the null hypothesis value, $H_0$ can be rejected.

