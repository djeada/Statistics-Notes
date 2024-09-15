## Hypothesis Testing

A hypothesis is a statement that might be true.

Hypothesis testing is a key tool in the field of statistics and forms the backbone of scientific research. It helps us make decisions about population parameters using sample data. Hypothesis testing is used across a wide variety of fields - from testing the effectiveness of a new drug in medical trials, to understanding customer behavior in business analytics.

### Inputs and Outputs of Hypothesis Testing

**Inputs**:

1. The **null hypothesis ($H_0$)** represents the default assumption or the status quo, indicating no effect or no difference. Hypothesis testing aims to challenge this statement.
2. The **alternative hypothesis ($H_1$ or $H_a$)** is the claim that the test seeks to support, indicating the presence of an effect or difference.
3. The **significance level ($\alpha$)** is a pre-determined threshold, usually set at 0.05, which defines the risk of rejecting the null hypothesis when it is actually true (Type I error).
4. **Sample data** refers to the collected data from observations, experiments, or surveys, providing the basis for calculating the test statistic and the p-value.

**Output**:

- The **p-value** is the probability of observing data as extreme as, or more extreme than, the sample data, assuming the null hypothesis is true. A small p-value (typically ≤ $\alpha$) provides strong evidence against the null hypothesis.

### Overview of Hypothesis Testing Steps

Hypothesis testing is a structured process involving several steps:

1. The process begins by **formulating hypotheses**, where the null and alternative hypotheses are defined based on the research question.
2. Next, a **significance level ($\alpha$)** is chosen, often set at 0.05, but it can be adjusted depending on the study's requirements or field norms.
3. **Data collection** is conducted systematically to ensure the data is representative and free from bias.
4. After collecting the data, the **test statistic** is calculated using an appropriate formula to convert the sample data into a value suitable for hypothesis testing.
5. The **p-value** is then determined, representing the probability of obtaining the observed or more extreme test statistic under the null hypothesis.
6. In **decision making**, $H_0$ is rejected if the p-value is less than $\alpha$; otherwise, you fail to reject $H_0$.
7. Finally, **interpreting results** involves understanding the decision in the context of the research question. Failing to reject $H_0$ does not prove it is true, only that there isn’t strong evidence against it.

### Example: Marble Bags
Imagine two bags: Bag A with a mix of 5 white and 5 black marbles, and Bag B with only black marbles.

```
  Bag A            Bag B
  _____            _____
 / • •  \         / O O  \
|  • •  |        |  O O  |    O = White Marble
|  O O  |        |  O O  |    • = Black Marble
|  O O  |        |  O O  |    
|  • O  |        |  O O  |
 \_____/          \_____/
```


Suspecting you have Bag B, you decide to test this hypothesis:

- The **null hypothesis ($H_0$)** states that the bag in question is Bag A.
- The **alternative hypothesis ($H_a$)** asserts that the bag in question is Bag B.

Drawing `n` marbles and finding them all black leads to calculating p-values to test these hypotheses. For Bag A, the chance of drawing a black marble is 0.5. Hence, drawing `n` black marbles consecutively from Bag A has a probability of $(0.5)^n$.

- For n=2, p-value = $(0.5)^2 = 0.25$
- For n=3, p-value = $(0.5)^3 = 0.125$
- For n=5, p-value = $(0.5)^5 = 0.03125$

A smaller p-value indicates stronger evidence against $H_0$. As `n` increases, the likelihood that you have Bag B (only black marbles) increases.

## Null and Alternative Hypotheses for a Mean

When testing the population mean, hypothesis testing considers three possibilities, each with distinct null and alternative hypotheses:

### Types of Tests

**I. Left-Tailed Test**

- The **null hypothesis ($H_0$)** states that the population mean $\mu$ is equal to a specific value $\mu_0$ ($\mu = \mu_0$).
- The **alternative hypothesis ($H_a$)** claims that $\mu$ is less than $\mu_0$ ($\mu < \mu_0$).

**II. Right-Tailed Test**

- The **null hypothesis ($H_0$)** suggests that $\mu$ is equal to $\mu_0$ ($\mu = \mu_0$).
- The **alternative hypothesis ($H_a$)** asserts that $\mu$ is greater than $\mu_0$ ($$\mu > \mu_0$).

**III. Two-Tailed Test**

- The **null hypothesis ($H_0$)** states that $\mu$ is equal to $\mu_0$ ($\mu = \mu_0$).
- The **alternative hypothesis ($H_a$)** proposes that $\mu$ is not equal to $\mu_0$ ($\mu \neq \mu_0$).

The null hypothesis always assumes that the population mean $\mu$ equals a predetermined value $\mu_0$. The alternative hypothesis presents a contrary statement: the population mean $\mu$ is less than, greater than, or not equal to $\mu_0$.

**Important Note:** Left-tailed and right-tailed tests are typically used when the effect is expected to occur in only one direction or when only one-directional effects are relevant. In most research scenarios, a two-tailed test is preferred unless there's strong justification for a one-tailed test.

### Examples

**I. Testing the Effectiveness of a New Diet (Two-Tailed Test)**

- The **null hypothesis ($H_0$)** is that the average daily energy expenditure $\mu$ equals the standard diet average $\mu_0$.
- The **alternative hypothesis ($H_a$)** is that the average daily energy expenditure $\mu$ differs from the standard diet average $\mu_0$ ($\mu \neq \mu_0$).

**II. Evaluating Customer Service Efficiency (Left-Tailed Test)**

- The **null hypothesis ($H_0$)** states that the average resolution time $\mu$ equals the industry standard of 10 minutes.
- The **alternative hypothesis ($H_a$)** is that the average resolution time $\mu$ is less than 10 minutes ($\mu < 10$).

**III. Assessing the Impact of a New Teaching Method (Right-Tailed Test)**

- The **null hypothesis ($H_0$)** suggests that the average test score $\mu$ equals the district average of 75%.
- The **alternative hypothesis ($H_a$)** asserts that the average test score $\mu$ exceeds the district average of 75% ($\mu > 75$).

## The P-value

Once the data is collected and the sample statistic computed, the researcher computes the P-value.

The P-value is the probability of obtaining a measurement at least as extreme as the one we measured, under the assumption that the null hypothesis is true.

![79292b56-d3c7-4eec-b30d-0c64a11d58ac](https://github.com/djeada/Statistics-Notes/assets/37275728/67c8823a-e0b8-479c-84f2-7d2908c9a482)

- In a **left-tailed test**, the shaded area represents the **p-value**, which is the area under the curve to the left of the sample statistic.
- In a **right-tailed test**, the shaded area represents the **p-value**, which is the area under the curve to the right of the sample statistic.

By at least as extreme, we mean a value at least as far to the left or right of the measured value.

## Choosing the Right Statistical Test

Selecting a suitable statistical test is critical in hypothesis testing, and several factors determine the appropriate choice:

### Factors to Consider

1. The **type of data** (categorical, ordinal, interval, or ratio) significantly influences the choice of statistical test, as different types of data require different methods.
2. The **number of variables** under analysis determines the test type, with specific tests designed for univariate (one variable), bivariate (two variables), and multivariate (more than two variables) analyses.
3. The **distribution of the data** is crucial, as parametric tests assume a normal distribution. If the data does not meet this assumption, a non-parametric test is more appropriate.
4. The **study design**, such as comparing groups or measuring changes over time within a group, also plays a role in selecting the correct statistical test.

### Examples of Statistical Tests

- A **t-test** is ideal for comparing the means of two groups with interval or ratio data that is normally distributed. For non-normally distributed data or ordinal data, consider a non-parametric alternative like the **Mann-Whitney U test**.
- To compare means across more than two groups, an **Analysis of Variance (ANOVA)** is appropriate. 
- For categorical data, a **chi-square test** is often used to examine differences in proportions.

The following table summarizes some common statistical tests and their applications:

| Test                         | Data Type           | Number of Groups | Assumptions                                      |
|------------------------------|---------------------|------------------|--------------------------------------------------|
| **T-Test**                   | Interval/Ratio      | Two              | Normally distributed, independent samples        |
| **Paired T-Test**            | Interval/Ratio      | Two              | Normally distributed, dependent samples          |
| **One-way ANOVA**            | Interval/Ratio      | More than Two    | Normally distributed, independent samples        |
| **Two-way ANOVA**            | Interval/Ratio      | More than Two    | Normally distributed, independent samples        |
| **Chi-Square Test**          | Categorical         | Two or more      | Independence between variables                   |
| **Pearson Correlation**      | Interval/Ratio      | Two              | Normally distributed, linear relationship        |
| **Spearman Correlation**     | Ordinal             | Two              | Non-parametric, monotonic relationship           |
| **Mann-Whitney U Test**      | Ordinal/Continuous  | Two              | Non-parametric, independent samples              |
| **Kruskal-Wallis H Test**    | Ordinal/Continuous  | More than Two    | Non-parametric, independent samples              |
| **Wilcoxon Signed-Rank Test**| Ordinal/Continuous  | Two              | Non-parametric, dependent samples                |
| **Friedman Test**            | Ordinal/Continuous  | More than Two    | Non-parametric, dependent samples                |

### Key Considerations

- **Left-tailed** and **right-tailed tests** are specific to the direction of the hypothesis. A left-tailed test is used when the research hypothesis suggests a decrease or lower value, while a right-tailed test is for an increase or higher value.
- **Two-tailed tests** are applied when the research question does not specify a direction of effect. These tests are more conservative and broadly applicable.
- **Parametric tests** assume underlying statistical distributions and typically require interval or ratio data. In contrast, **non-parametric tests** do not assume a specific distribution and are often used with ordinal data or when the assumptions of parametric tests are not met.
  
### Example: Hypothesis Test for the Mean

An agronomist suggests that a new fertilizer increases the average yield of a particular crop to more than 2 tons per hectare. To test this claim, a study is conducted where the new fertilizer is applied to randomly selected plots. The yield of 25 plots is measured, resulting in a mean yield of 2.1 tons per hectare and a standard deviation of 0.3 tons per hectare. Is the new fertilizer effective at increasing the average yield at a significance level of $\alpha = 0.05$?

**Hypothesis Setup**:

- Null Hypothesis ($H_0$): $\mu = 2$ tons per hectare (The fertilizer does not increase yield)
- Alternative Hypothesis ($H_a$): $\mu > 2$ tons per hectare (The fertilizer increases yield)

**Test Statistic**:

For the test statistic, we use the one-sample z-test since the sample size is greater than 30:

$$z = \frac{\bar{x} - \mu_0}{\sigma/\sqrt{n}}$$

where:

- $\bar{x}$ is the sample mean,
- $\mu_0$ is the hypothesized population mean,
- $\sigma$ is the population standard deviation (approximated here by the sample standard deviation),
- $n$ is the sample size.

**Plugging in the values**:

$$z = \frac{2.1 - 2}{0.3/\sqrt{25}}$$

$$z = \frac{0.1}{0.06}$$

$$z \approx 1.667$$

**Conclusion**:

We look up the critical z-value for a right-tailed test at $\alpha = 0.05$, which is approximately 1.645. Since our calculated z-value of 1.667 is greater than 1.645, we reject the null hypothesis.

There is sufficient evidence at the $\alpha = 0.05$ significance level to support the claim that the new fertilizer increases the average yield of the crop to more than 2 tons per hectare.
