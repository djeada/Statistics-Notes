## Hypothesis Testing

A hypothesis is a statement that might be true.

Hypothesis testing is a key tool in the field of statistics and forms the backbone of scientific research. It helps us make decisions about population parameters using sample data. Hypothesis testing is used across a wide variety of fields - from testing the effectiveness of a new drug in medical trials, to understanding customer behavior in business analytics.

### Inputs and Outputs of Hypothesis Testing

Inputs:

1. **Null Hypothesis ($H_0$):** Represents the default position or the status quo. It is a statement that indicates no effect or no difference. The hypothesis testing aims to challenge this hypothesis.
   
2. **Alternative Hypothesis ($H_1$ or $H_a$):** It's the claim that the test seeks to support. It is a statement indicating the presence of an effect or a difference.
   
3. **Significance Level ($\alpha$):** A threshold probability set before the testing begins, usually set at 0.05. It defines the risk of rejecting the null hypothesis when it is actually true (Type I error).

4. **Sample Data:** The collected data from observations, experiments, or surveys. It provides the empirical basis for calculating the test statistic and ultimately the p-value.

Output:

- **P-Value:** The probability of observing data as extreme as, or more extreme than, the sample data, assuming the null hypothesis is true. A small p-value (typically ≤ $\alpha$) indicates strong evidence against the null hypothesis.

### Overview of Hypothesis Testing Steps

Hypothesis testing is a structured process involving several steps:

1. **Formulating Hypotheses:** Define the null and alternative hypotheses, contextualizing them within the research question.
   
2. **Choosing a Significance Level:** Set $\alpha$, often at 0.05, though it can vary based on the study's requirements or norms in the field.
   
3. **Data Collection:** Gather data systematically to ensure it's representative and unbiased.
   
4. **Calculating the Test Statistic:** Use an appropriate formula to convert the sample data into a test statistic.
   
5. **Determining the P-Value:** Calculate the probability of the observed (or more extreme) test statistic under the null hypothesis.
   
6. **Decision Making:** Reject $H_0$ if the p-value is less than $\alpha$, otherwise fail to reject $H_0$.
   
7. **Interpreting Results:** Understand the decision in the context of the research question. Note that not rejecting $H_0$ doesn't prove it's true, just that there isn't strong evidence against it.

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

- **Null Hypothesis ($H_0$):** The bag in question is Bag A.
- **Alternative Hypothesis ($H_a$):** The bag in question is Bag B.

Drawing `n` marbles and finding them all black leads to calculating p-values to test these hypotheses. For Bag A, the chance of drawing a black marble is 0.5. Hence, drawing `n` black marbles consecutively from Bag A has a probability of $(0.5)^n$.

- For n=2, p-value = $(0.5)^2 = 0.25$.
- For n=3, p-value = $(0.5)^3 = 0.125$.
- For n=5, p-value = $(0.5)^5 = 0.03125$.

A smaller p-value indicates stronger evidence against $H_0$. As `n` increases, the likelihood that you have Bag B (only black marbles) increases.

## Null and Alternative Hypotheses for a Mean

When testing the population mean, hypothesis testing considers three possibilities, each with distinct null and alternative hypotheses:

### Types of Tests

1. **Left-Tailed Test**
   - **Null Hypothesis ($H_0$):** The population mean $\mu$ equals a specific value $\mu_0$, denoted as $\mu = \mu_0$.
   - **Alternative Hypothesis ($H_a$):** The population mean $\mu$ is less than the specified value $\mu_0$, denoted as $\mu < \mu_0$.

2. **Right-Tailed Test**
   - **Null Hypothesis ($H_0$):** Here, $\mu$ is again hypothesized to be equal to $\mu_0$, $\mu = \mu_0$.
   - **Alternative Hypothesis ($H_a$):** The claim is that $\mu$ is greater than $\mu_0$, $\mu > \mu_0$.

3. **Two-Tailed Test**
   - **Null Hypothesis ($H_0$):** Similar to the other tests, it states that $\mu$ equals $\mu_0$, $\mu = \mu_0$.
   - **Alternative Hypothesis ($H_a$):** In this case, $\mu$ is hypothesized to be not equal to $\mu_0$, $\mu \neq \mu_0$.

The null hypothesis always assumes that the population mean $\mu$ equals a predetermined value $\mu_0$. The alternative hypothesis presents a contrary statement: the population mean $\mu$ is less than, greater than, or not equal to $\mu_0$.

**Important Note:** Left-tailed and right-tailed tests are typically used when the effect is expected to occur in only one direction or when only one-directional effects are relevant. In most research scenarios, a two-tailed test is preferred unless there's strong justification for a one-tailed test.

### Examples

1. Testing the Effectiveness of a New Diet (Two-Tailed Test):
   - **Null Hypothesis ($H_0$):** The average daily energy expenditure $\mu$ equals the standard diet average $\mu_0$.
   - **Alternative Hypothesis ($H_a$):** The average daily energy expenditure $\mu$ differs from the standard diet average $\mu_0$ ($\mu \neq \mu_0$).

2. Evaluating Customer Service Efficiency (Left-Tailed Test):
   - **Null Hypothesis ($H_0$):** The average resolution time $\mu$ equals the industry standard of 10 minutes.
   - **Alternative Hypothesis ($H_a$):** The average resolution time $\mu$ is less than 10 minutes ($\mu < 10$).

3. Assessing the Impact of a New Teaching Method (Right-Tailed Test):
   - **Null Hypothesis ($H_0$):** The average test score $\mu$ equals the district average of 75%.
   - **Alternative Hypothesis ($H_a$):** The average test score $\mu$ exceeds the district average of 75% ($\mu > 75$).

## The P-value

Once the data is collected and the sample statistic computed, the researcher computes the P-value.

The P-value is the probability of obtaining a measurement at least as extreme as the one we measured, under the assumption that the null hypothesis is true.

![79292b56-d3c7-4eec-b30d-0c64a11d58ac](https://github.com/djeada/Statistics-Notes/assets/37275728/67c8823a-e0b8-479c-84f2-7d2908c9a482)

- **Left-Tailed Test**
  - The shaded area represents the p-value, which is the area under the curve to the left of the sample statistic.

- **Right-Tailed Test**
  - The shaded area represents the p-value, which is the area under the curve to the right of the sample statistic.

By at least as extreme, we mean a value at least as far to the left or right of the measured value.

## Choosing the Right Statistical Test

Selecting a suitable statistical test is critical in hypothesis testing, and several factors determine the appropriate choice:

### Factors to Consider

1. **Type of Data:** The nature of your data (categorical, ordinal, interval, or ratio) greatly influences the choice of test. Different types of data require different statistical methods.

2. **Number of Variables:** The quantity of variables under analysis dictates the test type. There are specific tests for univariate (one variable), bivariate (two variables), and multivariate (more than two variables) analyses.

3. **Distribution of the Data:** The assumption about data distribution is vital. Parametric tests assume a normal distribution. If your data does not fit this criterion, a non-parametric test is preferable.

4. **Study Design:** The structure of your study, like comparing groups or measuring changes over time within a group, also affects the test selection.

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

- **Left-tailed and Right-tailed Tests:** These are specific to the direction of the hypothesis. A left-tailed test is used when the research hypothesis involves a decrease or a lower value, while a right-tailed test is for when an increase or higher value is hypothesized.

- **Two-tailed Tests:** These are used when the research question does not specify a direction of effect. They are more conservative and widely applicable.

- **Parametric vs. Non-parametric Tests:** Parametric tests assume underlying statistical distributions and usually require interval or ratio data. Non-parametric tests do not assume a specific distribution and are often used with ordinal data or when assumptions of parametric tests are not met.

### Example: Hypothesis Test for the Mean

An agronomist suggests that a new fertilizer increases the average yield of a particular crop to more than 2 tons per hectare. To test this claim, a study is conducted where the new fertilizer is applied to randomly selected plots. The yield of 25 plots is measured, resulting in a mean yield of 2.1 tons per hectare and a standard deviation of 0.3 tons per hectare. Is the new fertilizer effective at increasing the average yield at a significance level of $\alpha = 0.05$?

Hypothesis Setup:

- Null Hypothesis ($H_0$): $\mu = 2$ tons per hectare (The fertilizer does not increase yield)
- Alternative Hypothesis ($H_a$): $\mu > 2$ tons per hectare (The fertilizer increases yield)

Test Statistic:

For the test statistic, we use the one-sample z-test since the sample size is greater than 30:

$$z = \frac{\bar{x} - \mu_0}{\sigma/\sqrt{n}}$$

where:
- $\bar{x}$ is the sample mean,
- $\mu_0$ is the hypothesized population mean,
- $\sigma$ is the population standard deviation (approximated here by the sample standard deviation),
- $n$ is the sample size.

Plugging in the values:

$$z = \frac{2.1 - 2}{0.3/\sqrt{25}}$$
$$z = \frac{0.1}{0.06}$$
$$z \approx 1.667$$

Conclusion:

We look up the critical z-value for a right-tailed test at $\alpha = 0.05$, which is approximately 1.645. Since our calculated z-value of 1.667 is greater than 1.645, we reject the null hypothesis.

There is sufficient evidence at the $\alpha = 0.05$ significance level to support the claim that the new fertilizer increases the average yield of the crop to more than 2 tons per hectare.
