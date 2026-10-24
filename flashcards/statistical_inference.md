# Quizzes on Statistical Inference

This series of quizzes covers essential topics in statistical inference, including:

- **Hypothesis Testing**: Test your understanding of null and alternative hypotheses, types of statistical tests, and how to interpret p-values.
- **Confidence Intervals**: Learn how to construct and interpret confidence intervals and understand their relationship to population parameters.
- **Type I and Type II Errors**: Assess your knowledge of the different types of errors in hypothesis testing, and explore the trade-offs between significance level, power, and sample size.
- **P-values**: Explore the meaning of p-values, their role in hypothesis testing, and common misconceptions.
- **Significance Levels**: Learn about alpha levels, the concept of statistical significance, and how to choose appropriate significance levels for different tests.
- **Power of a Test**: Understand how to calculate and interpret the power of a test, and how it relates to sample size and effect size.
- **One-Tailed vs Two-Tailed Tests**: Assess your knowledge of when to use one-tailed vs two-tailed tests and how they affect hypothesis testing conclusions.
- **Multiple Testing and Common Tests**: Review how to control error rates across many tests and when to use t, chi-square and ANOVA tests.

## Hypothesis Testing

<details>
<summary>What is a null hypothesis?</summary>

The **null hypothesis** ($H_0$) is the default claim being tested, usually that there is no effect or no difference. The test asks whether the data provide enough evidence to reject it. For example, in a test comparing two population means:

$$H_0: \mu_1 = \mu_2$$

Failing to reject $H_0$ does not prove that it is true.

</details>

<details>
<summary>What is an alternative hypothesis?</summary>

The **alternative hypothesis** ($H_a$ or $H_1$) is the competing claim that holds if $H_0$ is false, typically that an effect or difference exists. For the comparison of two means:

$$H_a: \mu_1 \neq \mu_2$$

It is usually the claim the researcher hopes to support, and it decides whether the test is one-tailed or two-tailed.

</details>

<details>
<summary>What are the steps in hypothesis testing?</summary>

The basic steps are:

1. **State the null and alternative hypotheses**.
2. **Choose a significance level** ($\alpha$), commonly 0.05, before looking at the results.
3. **Select an appropriate test** (e.g. t-test, z-test, chi-square test) for the data and design.
4. **Calculate the test statistic** from the sample data.
5. **Find the p-value**, or compare the statistic with a critical value.
6. **Decide**: reject $H_0$ if $p \le \alpha$; otherwise fail to reject $H_0$.
7. **Interpret the result** in the context of the research question, including the effect size.

</details>

<details>
<summary>When should you reject the null hypothesis?</summary>

Reject $H_0$ when the p-value is less than or equal to the significance level $\alpha$, or equivalently when the test statistic falls in the critical region. This means the observed data would be unusual if $H_0$ were true. For example, with $\alpha = 0.05$ and $p = 0.03$ you reject $H_0$. With $p = 0.08$ you fail to reject it.

</details>

<details>
<summary>What is a one-tailed test?</summary>

A **one-tailed test** has a directional alternative hypothesis, such as:

$$H_a: \mu_1 > \mu_2$$

The whole rejection region of size $\alpha$ lies in one tail, so the test is more powerful in that direction but cannot detect an effect in the other. Choose the direction before seeing the data.

</details>

<details>
<summary>What is a two-tailed test?</summary>

A **two-tailed test** has a non-directional alternative hypothesis:

$$H_a: \mu_1 \neq \mu_2$$

It detects departures from $H_0$ in either direction by splitting $\alpha$ between the two tails. For a symmetric statistic the p-value is $2P(T \ge |t_{obs}|)$.

</details>

## Confidence Intervals

<details>
<summary>What is a confidence interval?</summary>

A **confidence interval** is a range of plausible values for a population parameter, calculated from sample data by a method with a stated long-run success rate. A 95% confidence interval comes from a procedure that, if the study were repeated many times, would produce intervals containing the true parameter about 95% of the time.

</details>

<details>
<summary>How do you interpret a 95% confidence interval?</summary>

The 95% refers to the method: about 95% of intervals built this way capture the true parameter. Any single computed interval either contains the fixed parameter or does not, so it is incorrect to say there is a 95% probability that the parameter lies in that particular interval. The interval is also about the parameter (e.g. the mean), not about individual observations.

</details>

<details>
<summary>What is the formula for a confidence interval for the mean?</summary>

If the population standard deviation $\sigma$ is known and the data are normal or $n$ is large:

$$\bar{x} \pm z^* \frac{\sigma}{\sqrt{n}}$$

where $z^*$ is the standard normal critical value (1.96 for 95%). If $\sigma$ is unknown, replace it with the sample standard deviation $s$ and use the t critical value with $n - 1$ degrees of freedom:

$$\bar{x} \pm t^*_{n-1} \frac{s}{\sqrt{n}}$$

</details>

<details>
<summary>What factors affect the width of a confidence interval?</summary>

The width is $2 \times \text{critical value} \times \text{standard error}$, so it depends on:

1. **Sample size**: larger $n$ gives narrower intervals. Halving the width needs about four times the sample size.
2. **Confidence level**: higher confidence (99% vs 95%) gives wider intervals.
3. **Variability**: a larger standard deviation gives wider intervals.

</details>

<details>
<summary>What is the relationship between confidence intervals and hypothesis testing?</summary>

A $100(1-\alpha)\%$ confidence interval contains exactly the parameter values that a two-sided test at level $\alpha$ would not reject. So if the null value lies outside a 95% interval, $H_0$ is rejected at $\alpha = 0.05$. If the null value is inside the interval, $H_0$ is not rejected. The interval also shows the size of the effect, which a p-value does not.

</details>

## Type I and Type II Errors

<details>
<summary>What is a Type I error?</summary>

A **Type I error** is rejecting the null hypothesis when it is actually true, a "false positive". Its probability, when $H_0$ is true, is the significance level $\alpha$. For example, $\alpha = 0.05$ means a true null is wrongly rejected 5% of the time.

</details>

<details>
<summary>What is a Type II error?</summary>

A **Type II error** is failing to reject the null hypothesis when it is actually false, a "false negative". Its probability is denoted $\beta$. It depends on the true effect size, the sample size, the variability and $\alpha$. Power is $1 - \beta$.

</details>

<details>
<summary>What is the relationship between Type I and Type II errors?</summary>

For a fixed sample size, effect size and variability, there is a trade-off. Lowering $\alpha$ makes the test stricter, which reduces Type I errors but increases $\beta$, the Type II error rate. Choosing $\alpha$ therefore means weighing the consequences of false positives against false negatives in the context of the study.

</details>

<details>
<summary>How can you reduce Type I and Type II errors?</summary>

The Type I error rate is set directly by choosing $\alpha$. To reduce Type II errors without raising $\alpha$, increase power:

1. **Increase the sample size**: this shrinks the standard error and reduces $\beta$.
2. **Reduce variability**: more precise measurement or a paired or blocked design increases power.
3. **Use a one-sided test** when only one direction is of genuine interest and the direction is fixed in advance.

Only these power-increasing changes let you lower both error rates at once.

</details>

## P-values

<details>
<summary>What is a p-value?</summary>

A **p-value** is the probability, calculated assuming the null hypothesis is true, of obtaining a test statistic at least as extreme as the one observed. Smaller p-values mean the data are less compatible with $H_0$, so they are stronger evidence against it.

</details>

<details>
<summary>How do you interpret a p-value?</summary>

Compare it with the significance level $\alpha$ chosen in advance:

- If $p \le \alpha$, reject the null hypothesis: the result is statistically significant.
- If $p > \alpha$, fail to reject the null hypothesis: the evidence is insufficient.

For example, with $\alpha = 0.05$ a p-value of 0.02 is significant evidence against $H_0$.

</details>

<details>
<summary>What are some common misconceptions about p-values?</summary>

Common misconceptions include:

- A p-value is **not** the probability that the null hypothesis is true.
- A p-value does **not** measure the size or practical importance of an effect. Huge samples can make trivial effects significant.
- A p-value above 0.05 does **not** prove the null hypothesis. It only means the evidence is insufficient to reject it.
- $1 - p$ is **not** the probability that the alternative hypothesis is true.

</details>

## Significance Levels

<details>
<summary>What is a significance level?</summary>

The **significance level** ($\alpha$) is the threshold, fixed before the analysis, for deciding whether to reject the null hypothesis. It equals the probability of a Type I error, that is, of rejecting a true null. Common choices are 0.05, 0.01 and 0.10.

</details>

<details>
<summary>How do you choose an appropriate significance level?</summary>

The choice depends on the costs of each kind of error:

- When false positives are costly, as in confirmatory medical trials or particle physics, a smaller $\alpha$ (e.g. 0.01 or less) is used.
- In exploratory research, a larger $\alpha$ (e.g. 0.10) may be acceptable to reduce the risk of missing real effects.

When many tests are run, $\alpha$ must also be adjusted for multiple comparisons.

</details>

## Power of a Test

<details>
<summary>What is the power of a test?</summary>

The **power** of a test is the probability that it correctly rejects the null hypothesis when the null is false, that is, when a specific alternative is true. Power is $1 - \beta$, where $\beta$ is the Type II error probability. A conventional target is 0.80.

</details>

<details>
<summary>What factors affect the power of a test?</summary>

Factors that affect power include:

1. **Sample size**: larger samples increase power.
2. **Effect size**: larger true effects are easier to detect.
3. **Significance level** ($\alpha$): a larger $\alpha$ increases power but also the Type I error rate.
4. **Variability**: less variability in the data increases power.
5. **Direction**: a one-sided test has more power in the hypothesised direction.

</details>

<details>
<summary>Why is power analysis done before collecting data?</summary>

Power analysis finds the sample size needed to detect the smallest effect of practical interest with a chosen $\alpha$ and power. For a two-sample z-test the size per group is approximately $n \approx \frac{(z_{1-\alpha/2} + z_{1-\beta})^2 \cdot 2\sigma^2}{\Delta^2}$. With $\sigma = 10$, $\Delta = 5$, $\alpha = 0.05$ and power 0.80, this gives about 63 per group. Underpowered studies often miss real effects.

</details>

## Multiple Testing

<details>
<summary>Why is running many hypothesis tests a problem?</summary>

Each test at level $\alpha$ has its own chance of a false positive, so the chance of at least one false positive grows with the number of tests. For $m$ independent tests with all nulls true:

$$P(\text{at least one false rejection}) = 1 - (1 - \alpha)^m$$

With $m = 20$ and $\alpha = 0.05$ this is about 0.64. Data snooping, where you test many patterns and report the significant ones, has the same effect.

</details>

<details>
<summary>How do Bonferroni and Benjamini–Hochberg corrections differ?</summary>

- **Bonferroni** controls the **family-wise error rate** (the probability of any false rejection) by testing each hypothesis at $\alpha/m$. It is simple but conservative.
- **Benjamini–Hochberg** controls the **false discovery rate** (the expected proportion of false rejections among rejections). Sort the p-values, find the largest $k$ with $p_{(k)} \le \frac{k}{m}\alpha$, and reject the $k$ smallest. It is more powerful when many tests are run.

</details>

## Common Tests

<details>
<summary>How do you choose between a two-sample t-test, a paired t-test and their non-parametric alternatives?</summary>

- **Independent groups**: use a two-sample t-test (Welch's version if the variances differ). The rank-based alternative is the Mann–Whitney U test.
- **Matched pairs** (e.g. before and after on the same subjects): use a paired t-test on the differences. The rank-based alternative is the Wilcoxon signed-rank test.

Rank-based tests make fewer distributional assumptions but are slightly less powerful when the data really are normal.

</details>

<details>
<summary>What do chi-square tests and one-way ANOVA test?</summary>

- **Chi-square tests** compare observed and expected counts for categorical data. They test goodness of fit ($df = k - 1$) or independence/homogeneity in an $r \times c$ table ($df = (r-1)(c-1)$), and they need expected counts of roughly 5 or more.
- **One-way ANOVA** tests $H_0: \mu_1 = \dots = \mu_k$ with $F = MST/MSE$ on $(k-1, N-k)$ degrees of freedom. A significant F is followed by post-hoc comparisons such as Tukey's HSD.

</details>
