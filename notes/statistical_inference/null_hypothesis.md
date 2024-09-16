## Null Hypotheses and Alternative Hypotheses

In statistical hypothesis testing, we construct two opposing hypotheses to make inferences about a population parameter based on sample data:
Here’s the revision with clear points and no nesting:

1. The **null hypothesis ($H_0$)** represents the assumption that there is no effect, no difference, or no change in the population. It serves as the default assumption in hypothesis testing.
2. The **alternative hypothesis ($H_1$ or $H_a$)** challenges the null hypothesis by suggesting that there is an effect, a difference, or a change in the population.

The goal is to use statistical evidence from sample data to decide whether to reject the null hypothesis in favor of the alternative hypothesis.

![Null Hypothesis Testing Illustration](https://github.com/djeada/Statistics-Notes/assets/37275728/d45fdb61-9d6f-4adf-a54b-4106382d2087)

The plot illustrates the distribution of a test statistic under the assumption that the null hypothesis $H_0$ is true. Here's a detailed explanation of the components:

- The **green curve (null distribution)** represents the probability density function (pdf) of the test statistic under the null hypothesis ($H_0$). This is often a standard normal distribution centered at zero.
- The **vertical dashed red line** marks the observed value of the test statistic from the sample data, such as $z = 2.0$.
- The **orange shaded area (tail area)** shows the probability of observing a test statistic as extreme as, or more extreme than, the observed value under $H_0$. In a one-tailed test, this corresponds to the p-value, while in a two-tailed test, an equivalent area on the opposite side is also considered.

### The Language of Hypothesis Testing

- If the evidence (based on the p-value) is strong enough, we **reject $H_0$**, suggesting that there is statistically significant evidence in favor of the alternative hypothesis.
- When the evidence is insufficient, we **fail to reject $H_0$**. This does not mean we accept $H_0$ as true, but rather that we do not have enough evidence to conclude it is false.
- It's important to **avoid "accepting" $H_0$**, as statistical tests are meant to assess whether there is sufficient evidence against $H_0$, not to prove that $H_0$ is true.
- **Type I error** occurs when we incorrectly reject $H_0$ even though it is true (a false positive).
- **Type II error** happens when we fail to reject $H_0$ even though $H_1$ is true (a false negative).

### Interpretation of the P-value

The **p-value** is the probability of obtaining a test statistic at least as extreme as the one observed, assuming that the null hypothesis $H_0$ is true.

- The **p-value** does not represent the probability that $H_0$ is true or false. It simply measures how consistent the data are with the null hypothesis.
- A **large p-value** means the data are consistent with $H_0$, but this does not prove that $H_0$ is true.
- A **small p-value** (when $p < \alpha$) provides strong evidence against $H_0$, leading to the rejection of the null hypothesis.
- A **large p-value** (when $p \geq \alpha$) indicates insufficient evidence to reject $H_0$, so we fail to reject it.

### Example: Coin Toss Experiment

- The **null hypothesis ($H_0$)** states that the coin is fair, meaning the probability of heads is $P(\text{heads}) = 0.5$.
- The **alternative hypothesis ($H_1$)** suggests that the coin is not fair, so the probability of heads is $P(\text{heads}) \neq 0.5$.
- The experiment involved a total of **10 tosses** ($n = 10$).
- The **observed outcome** was 4 heads and 6 tails.

#### Statistical Test

We use the **binomial test** to calculate the p-value for the observed outcome.

I. **Compute the probability of observing exactly 4 heads** under $H_0$:

$$
P(X = 4) = \binom{10}{4} (0.5)^{4} (0.5)^{6} = \frac{210 \times 0.0625 \times 0.015625}{1} = 0.2051
$$

II. **Compute the probabilities for more extreme outcomes** (0 to 4 heads and 6 to 10 heads) since it's a two-tailed test.

III. **Total P-value**:

$$
\text{p-value} = 2 \times \left( P(X \leq 4) \right) = 2 \times \left( \sum_{k=0}^{4} P(X = k) \right)
$$

IV. **Sum of Probabilities**:

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

V. **Compute P-value**:

$$
\text{p-value} = 2 \times 0.37697 = 0.75394
$$

#### Decision

- The **significance level ($\alpha$)** is typically set at 0.05.
- In this case, the **comparison** shows that the p-value is $0.75394$, which is greater than $0.05$.
- As a result, we are **failing to reject $H_0$**, meaning we cannot conclude that the coin is unfair based on this data.
- However, this does not mean we are **accepting $H_0$**. The result does not prove the coin is fair; it simply indicates that the observed data are consistent with a fair coin.

### Additional Considerations

- **Statistical power** is the probability of correctly rejecting $H_0$ when $H_1$ is true.
- The **sample size** influences power, with larger samples leading to increased power.
- A **one-tailed test** checks for an effect in one specific direction, such as $P(\text{heads}) > 0.5$.
- A **two-tailed test** examines for an effect in either direction, for example, $P(\text{heads}) \neq 0.5$.
- **Confidence intervals** provide an estimated range of values that are likely to include the population parameter.
- In relation to **hypothesis testing**, if the confidence interval does not include the null hypothesis value, $H_0$ can be rejected.
