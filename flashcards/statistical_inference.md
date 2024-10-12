# Quizzes on Statistical Inference

This series of quizzes covers essential topics in statistical inference, including:

- **Hypothesis Testing**: Test your understanding of null and alternative hypotheses, types of statistical tests, and how to interpret p-values.
- **Confidence Intervals**: Learn how to construct and interpret confidence intervals and understand their relationship to population parameters.
- **Type I and Type II Errors**: Assess your knowledge of the different types of errors in hypothesis testing, and explore the trade-offs between significance level, power, and sample size.
- **P-values**: Explore the meaning of p-values, their role in hypothesis testing, and common misconceptions.
- **Significance Levels**: Learn about alpha levels, the concept of statistical significance, and how to choose appropriate significance levels for different tests.
- **Power of a Test**: Understand how to calculate and interpret the power of a test, and how it relates to sample size and effect size.
- **One-Tailed vs Two-Tailed Tests**: Assess your knowledge of when to use one-tailed vs two-tailed tests and how they affect hypothesis testing conclusions.

## Hypothesis Testing

<details>

<summary>What is a null hypothesis?</summary><br>

The **null hypothesis** (denoted $H_0$) is a statement that there is no effect or no difference, and it serves as the default assumption in hypothesis testing. It is the hypothesis that researchers aim to test or reject. For example, in a test comparing two means, the null hypothesis might state that the means are equal:

$$H_0: \mu_1 = \mu_2$$

</details>

<details>

<summary>What is an alternative hypothesis?</summary><br>

The **alternative hypothesis** (denoted $H_a$ or $H_1$) is the statement that contradicts the null hypothesis. It proposes that there is an effect or a difference. For example, in the same test comparing two means, the alternative hypothesis might state:

$$H_a: \mu_1 \neq \mu_2$$

The alternative hypothesis is what researchers aim to support through evidence.

</details>

<details>

<summary>What are the steps in hypothesis testing?</summary><br>
The basic steps in hypothesis testing are:
1. **State the null and alternative hypotheses**.
2. **Choose a significance level** ($\alpha$), commonly set at 0.05.
3. **Select the appropriate test** (e.g., t-test, z-test, chi-square test).
4. **Calculate the test statistic** based on the sample data.
5. **Determine the p-value** or critical value for the test statistic.
6. **Make a decision**: Reject or fail to reject the null hypothesis based on the comparison of the p-value and the significance level.
7. **Interpret the results** in the context of the original research question.

</details>

<details>

<summary>When should you reject the null hypothesis?</summary><br>

The null hypothesis is rejected if the p-value is less than or equal to the significance level ($\alpha$), indicating that the observed data is unlikely to occur if the null hypothesis were true. For example, if $\alpha = 0.05$ and the p-value is 0.03, you would reject the null hypothesis.

</details>

<details>

<summary>What is a one-tailed test?</summary><br>

A **one-tailed test** is a hypothesis test where the alternative hypothesis specifies a direction of the effect (e.g., greater than or less than). It tests whether the parameter is either larger or smaller than the null hypothesis value, but not both. For example:

$$H_a: \mu_1 > \mu_2$$

This test is used when the research question has a specific directional expectation.

</details>

<details>

<summary>What is a two-tailed test?</summary><br>

A **two-tailed test** is a hypothesis test where the alternative hypothesis does not specify a direction, meaning it checks for any difference from the null hypothesis value in either direction. For example:

$$H_a: \mu_1 \neq \mu_2$$

It tests for both possibilities (greater or less), and is used when there is no specific directional assumption in the research.

</details>

---

## Confidence Intervals

<details>

<summary>What is a confidence interval?</summary><br>

A **confidence interval** is a range of values, derived from the sample data, that is likely to contain the true population parameter with a specified level of confidence. For example, a 95% confidence interval means that if the experiment were repeated many times, approximately 95% of the intervals would contain the true population parameter.

</details>

<details>

<summary>How do you interpret a 95% confidence interval?</summary><br>

A 95% confidence interval indicates that you are 95% confident that the true population parameter lies within the calculated range. It does not mean that there is a 95% chance the parameter is within the interval; rather, it reflects the confidence in the method used to estimate the interval.

</details>

<details>

<summary>What is the formula for a confidence interval for the mean?</summary><br>

The formula for a confidence interval for the population mean, assuming a normally distributed population and known standard deviation, is:

$$\text{CI} = \bar{X} \pm Z \times \frac{\sigma}{\sqrt{n}}$$

where:
- $\bar{X}$ is the sample mean,
- $Z$ is the critical value from the standard normal distribution corresponding to the desired confidence level (e.g., 1.96 for 95% confidence),
- $\sigma$ is the population standard deviation (or sample standard deviation if $\sigma$ is unknown),
- $n$ is the sample size.

</details>

<details>

<summary>What factors affect the width of a confidence interval?</summary><br>
The width of a confidence interval depends on:
1. **Sample size**: Larger sample sizes result in narrower confidence intervals.
2. **Confidence level**: Higher confidence levels (e.g., 99% vs. 95%) result in wider intervals.
3. **Standard deviation**: Larger variability (standard deviation) increases the width of the confidence interval.

</details>

<details>

<summary>What is the relationship between confidence intervals and hypothesis testing?</summary><br>

Confidence intervals and hypothesis testing are closely related. If the value specified in the null hypothesis lies outside the confidence interval, the null hypothesis can be rejected at the corresponding significance level. For example, if a 95% confidence interval for a mean does not include the null hypothesis value, you would reject the null hypothesis at $\alpha = 0.05$.

</details>

---

## Type I and Type II Errors

<details>

<summary>What is a Type I error?</summary><br>

A **Type I error** occurs when the null hypothesis is rejected when it is actually true. This is also known as a "false positive" or rejecting a true null hypothesis. The probability of making a Type I error is denoted by $\alpha$, which is the significance level of the test (e.g., $\alpha = 0.05$ means a 5% chance of a Type I error).

</details>

<details>

<summary>What is a Type II error?</summary><br>

A **Type II error** occurs when the null hypothesis is not rejected when it is actually false. This is also known as a "false negative" or failing to reject a false null hypothesis. The probability of making a Type II error is denoted by $\beta$.

</details>

<details>

<summary>What is the relationship between Type I and Type II errors?</summary><br>

There is an inverse relationship between Type I and Type II errors. Reducing the risk of a Type I error (lowering $\alpha$) increases the risk of a Type II error ($\beta$), and vice versa. Balancing the two types of errors often involves choosing an appropriate significance level based on the context of the research.

</details>

<details>

<summary>How can you reduce Type I and Type II errors?</summary><br>
You can reduce Type I and Type II errors by:
1. **Increasing the sample size**: This increases the power of the test, reducing $\beta$.
2. **Adjusting the significance level**: Lowering $\alpha$ reduces Type I errors, though it may increase Type II errors.
3. **Improving the precision of measurements**: Better data collection reduces variability, which can lower both types of errors.

</details>

---

## P-values

<details>

<summary>What is a p-value?</summary><br>

A **p-value** is the probability of obtaining results as extreme as, or more extreme than, the observed data under the assumption that the null hypothesis is true. It quantifies the strength of evidence against the null hypothesis. A smaller p-value indicates stronger evidence to reject the null hypothesis.

</details>

<details>
<summary>How do you interpret a p-value?</summary><br>
- If the **p-value** is less than or equal to the significance level ($\alpha$), you reject the null hypothesis.
- If the p-value is greater than $\alpha$, you fail to reject the null hypothesis.

For example, with $\alpha = 0.05$, a p-value of 0.02 suggests significant evidence against the null hypothesis.

</details>

<details>

<summary>What are some common misconceptions about p-values?</summary><br>
Common misconceptions include:
- A **p-value** does not measure the probability that the null hypothesis is true.
- A **p-value** does not indicate the size or importance of an effect.
- A **p-value** greater than 0.05 does not "prove" that the null hypothesis is true; it only suggests insufficient evidence to reject it.

</details>

---

## Significance Levels

<details>

<summary>What is a significance level?</summary><br>

The **significance level** (denoted $\alpha$) is the threshold used to decide whether to reject the null hypothesis. It represents the probability of making a Type I error (rejecting a true null hypothesis). Common significance levels include 0.05, 0.01, and 0.10.

</details>

<details>

<summary>How do you choose an appropriate significance level?</summary><br>
The choice of **significance level** depends on the context of the research:
- In fields like medicine, a lower $\alpha$ (e.g., 0.01) may be used to minimize the risk of Type I errors (false positives).
- In exploratory research, a higher $\alpha$ (e.g., 0.10) may be acceptable to balance the risk of Type II errors (false negatives).

</details>

---

## Power of a Test

<details>

<summary>What is the power of a test?</summary><br>

The **power** of a test is the probability that the test correctly rejects the null hypothesis when it is false (i.e., it avoids a Type II error). Power is calculated as $1 - \beta$, where $\beta$ is the probability of a Type II error. High power means the test is more likely to detect an effect if it exists.

</details>

<details>

<summary>What factors affect the power of a test?</summary><br>
Factors that affect the power of a test include:
1. **Sample size**: Larger sample sizes increase power.
2. **Effect size**: Larger effects are easier to detect, increasing power.
3. **Significance level ($\alpha$)**: A higher $\alpha$ increases power but also increases the chance of a Type I error.
4. **Variance**: Lower variability in the data increases power.

</details>

<details>

<summary>Why is the power of a test important?</summary><br>

The power of a test is important because it determines the likelihood of detecting an effect if one truly exists. Low-power tests have a higher risk of producing false negatives (Type II errors), potentially missing important findings. Power analysis is often conducted before an experiment to ensure sufficient sample size.

</details>
