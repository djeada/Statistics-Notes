# Statistical Inference Quiz

Notes: [Hypothesis Testing](../notes/hypothesis_testing_and_confidence_intervals/hypothesis_testing.md), [Null and Alternative Hypotheses](../notes/hypothesis_testing_and_confidence_intervals/null_hypothesis.md), [Confidence Intervals](../notes/hypothesis_testing_and_confidence_intervals/confidence_intervals.md), [Type I and Type II Errors](../notes/hypothesis_testing_and_confidence_intervals/type_i_and_type_ii_errors.md), [Multiple Comparisons](../notes/hypothesis_testing_and_confidence_intervals/multiple_comparisons.md), [Chi-Square Tests](../notes/hypothesis_testing_and_confidence_intervals/analysis_of_categorical_data.md), [ANOVA](../notes/regression/analysis_of_variance.md), [Student's t Distribution](../notes/sampling_and_sampling_distributions/student_t_distribution.md), [F Distribution](../notes/sampling_and_sampling_distributions/f_distribution.md)

Check your understanding of hypothesis tests, p-values, confidence intervals, error rates, power, t, chi-square and ANOVA tests, and multiple testing.

#### Q. What is the **null hypothesis** in a two-sample t-test comparing two population means?

* [x] $H_0: \mu_1 = \mu_2$
* [ ] $H_0: \mu_1 \neq \mu_2$
* [ ] $H_0: \sigma_1^2 = \sigma_2^2$
* [ ] $H_0: \bar{x}_1 = \bar{x}_2$

> **Explanation:** Hypotheses are statements about population parameters, and the null states no difference. A claim about sample means $\bar{x}_1, \bar{x}_2$ is not a hypothesis, since those are observed.

#### Q. Which test compares the **variances** of two normally distributed populations?

* [ ] Independent-samples t-test
* [x] F-test for the ratio of two variances
* [ ] Chi-square test of independence
* [ ] Paired t-test

> **Explanation:** Under $H_0: \sigma_1^2 = \sigma_2^2$ the ratio $s_1^2/s_2^2$ follows an F distribution with $(n_1 - 1, n_2 - 1)$ degrees of freedom. This test is sensitive to non-normality.

#### Q. What does a **95% confidence level** mean?

* [ ] There is a 95% chance the null hypothesis is true
* [x] In repeated sampling, about 95% of intervals built this way contain the true parameter
* [ ] There is a 95% probability the parameter lies in this particular computed interval
* [ ] 95% of the individual observations fall inside the interval

> **Explanation:** The 95% describes the long-run success rate of the procedure. Once an interval is computed, the fixed parameter is either in it or not, and the interval is about the mean, not individual values.

#### Q. All else being equal, which change makes a confidence interval for a mean **wider**?

* [ ] Lowering the confidence level from 95% to 90%
* [x] Decreasing the sample size
* [ ] Reducing the population standard deviation
* [ ] Increasing the sample size

> **Explanation:** The margin of error is $z^* \sigma/\sqrt{n}$. A smaller $n$ increases the standard error. Lowering the confidence level, reducing $\sigma$ or increasing $n$ all make the interval narrower.

#### Q. What is the **pooled variance** in a two-sample t-test?

* [ ] A weighted average of the two sample means
* [x] A weighted average of the two sample variances, weighted by degrees of freedom
* [ ] The difference between the two sample variances
* [ ] The sum of the two population variances

> **Explanation:** $s_p^2 = \frac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1+n_2-2}$. It estimates the common variance under the equal-variance assumption.

#### Q. What feature of the study design calls for a **paired** t-test instead of an independent-samples t-test?

* [ ] The two groups have equal variances
* [ ] The data come from two unrelated sets of subjects
* [x] Each observation in one sample is matched to one in the other
* [ ] Both samples contain more than 30 observations

> **Explanation:** Paired designs, such as before-and-after measurements on the same subjects, produce dependent samples. The test analyses the within-pair differences, which removes between-subject variability.

#### Q. What does the **Bonferroni correction** adjust for?

* [ ] Small sample sizes
* [x] Multiple comparisons, to control the family-wise error rate
* [ ] Non-normal data distributions
* [ ] Unequal variances between groups

> **Explanation:** Testing each of $m$ hypotheses at level $\alpha/m$ keeps the probability of at least one false rejection at or below $\alpha$.

#### Q. Which non-parametric test is the usual alternative to the **paired t-test**?

* [x] Wilcoxon signed-rank test
* [ ] Mann–Whitney U test
* [ ] Kruskal–Wallis test
* [ ] Chi-square goodness-of-fit test

> **Explanation:** The Wilcoxon signed-rank test ranks the within-pair differences. Mann–Whitney U is the alternative for two independent samples, and Kruskal–Wallis for more than two independent groups.

#### Q. Which non-parametric test is the usual alternative to the **independent-samples t-test**?

* [ ] Wilcoxon signed-rank test
* [x] Mann–Whitney U test
* [ ] Friedman test
* [ ] F-test for two variances

> **Explanation:** The Mann–Whitney U test compares two independent samples using ranks. The signed-rank test is for paired data and Friedman's test is for three or more repeated measurements.

#### Q. What is the main advantage of a **non-parametric** hypothesis test?

* [ ] It has more power than a t-test when the data are normal
* [x] It does not assume a specific distributional form for the data
* [ ] It always gives narrower confidence intervals
* [ ] It removes the need for independent observations

> **Explanation:** Rank-based tests rely on fewer distributional assumptions, which helps with skewed data or outliers. When normality holds they are usually slightly less powerful, and they still assume independence.

#### Q. In a one-way ANOVA, what does a significant F-statistic indicate?

* [x] At least one group mean differs from the others
* [ ] All the group means differ from each other
* [ ] All the group variances are equal
* [ ] The data are normally distributed

> **Explanation:** ANOVA tests $H_0: \mu_1 = \dots = \mu_k$ against the alternative that not all means are equal. Finding out which means differ needs post-hoc comparisons.

#### Q. Which question is a **chi-square test of independence** designed to answer?

* [ ] Do two independent groups have different means?
* [ ] Is the correlation between two continuous variables zero?
* [x] Are two categorical variables associated in a contingency table?
* [ ] Do three or more groups have different medians?

> **Explanation:** The test compares observed cell counts with the counts expected if the row and column variables were independent. Mean comparisons use t-tests or ANOVA.

#### Q. Which change **increases the power** of a test, holding everything else fixed?

* [ ] Decreasing the sample size
* [x] Raising the significance level from 0.01 to 0.05
* [ ] Increasing the variability of the measurements
* [ ] Testing for a smaller true effect

> **Explanation:** A larger $\alpha$ enlarges the rejection region, so a false $H_0$ is rejected more often, at the cost of more Type I errors. The other three changes all reduce power.

#### Q. Two studies estimate the same mean with 95% intervals and the same sample standard deviation. Study A's interval is **twice as wide** as Study B's. What is the most likely reason?

* [ ] Study A used about twice as many observations
* [ ] Study A used about half as many observations
* [x] Study A used about a quarter as many observations
* [ ] Study A used about four times as many observations

> **Explanation:** Width is proportional to $s/\sqrt{n}$. Doubling the width requires $\sqrt{n}$ to halve, so $n_A \approx n_B/4$.

#### Q. Which test compares the **means of two independent groups** with roughly normal data?

* [ ] Paired t-test
* [x] Independent-samples t-test
* [ ] Chi-square test
* [ ] Wilcoxon signed-rank test

> **Explanation:** The independent-samples t-test is designed for two unrelated groups. A paired t-test needs matched observations, and chi-square tests are for categorical counts.

#### Q. What does the significance level **α** represent in hypothesis testing?

* [ ] The probability that the alternative hypothesis is true
* [x] The probability of rejecting the null hypothesis when it is true
* [ ] The p-value calculated from the sample
* [ ] The probability of failing to reject a false null hypothesis

> **Explanation:** $\alpha$ is the Type I error rate you choose before seeing the data. The probability of failing to reject a false null is $\beta$.

#### Q. Which condition justifies using a **one-sample t-test** for a mean?

* [ ] The sample size must be larger than 100
* [ ] The population variance must be known
* [x] The data come from a roughly normal population, or n is reasonably large
* [ ] The data must be categorical

> **Explanation:** The t-test estimates $\sigma$ with $s$ and relies on approximate normality, which the CLT provides for large $n$. A known population variance is the setting for a z-test.

#### Q. What does a **p-value** represent?

* [ ] The probability that the null hypothesis is true
* [x] The probability, assuming $H_0$ is true, of a result at least as extreme as the one observed
* [ ] The probability that the result happened by chance alone
* [ ] The significance level chosen for the test

> **Explanation:** A p-value is computed under the assumption that $H_0$ holds. It is not the probability that $H_0$ is true, and it is not the probability that chance alone produced the result.

#### Q. For a test statistic with a symmetric null distribution, such as z or t, how is the **two-tailed p-value** computed?

* [ ] As $P(T \ge t_{obs})$, the upper-tail area only
* [x] As $2P(T \ge |t_{obs}|)$, the area in both tails beyond $|t_{obs}|$
* [ ] As $1 - P(T \ge |t_{obs}|)$, the central area
* [ ] As $P(T \ge t_{obs})/2$, half the upper-tail area

> **Explanation:** A two-tailed test treats departures in either direction as evidence against $H_0$, so it adds the two equal tail areas. That is twice the one-tailed p-value.

#### Q. A researcher wants to show that a new drug **lowers** mean systolic blood pressure below 140 mmHg. Which alternative hypothesis fits?

* [ ] $H_1: \mu \neq 140$
* [x] $H_1: \mu < 140$
* [ ] $H_1: \mu > 140$
* [ ] $H_1: \mu = 140$

> **Explanation:** A directional claim gives a one-tailed (left-tailed) alternative. The equality $\mu = 140$ belongs to the null hypothesis, and $\neq$ would be a two-tailed test.

#### Q. What does the **null hypothesis** $H_0$ usually represent?

* [x] No effect or no difference, the default claim being tested
* [ ] The effect the researcher hopes to demonstrate
* [ ] The claim that the sample mean exceeds the population mean
* [ ] The claim that the p-value is below α

> **Explanation:** $H_0$ is the status quo that the data must provide evidence against. The researcher's claim usually goes in the alternative $H_1$.

#### Q. When the **p-value is less than or equal to α**, what is the correct conclusion?

* [ ] Fail to reject the null hypothesis
* [ ] Accept the null hypothesis as proven
* [x] Reject the null hypothesis
* [ ] Accept the alternative hypothesis as proven

> **Explanation:** $p \le \alpha$ means the result would be unusual if $H_0$ were true, so $H_0$ is rejected. Rejection is evidence for $H_1$, not proof of it.

#### Q. What is the **critical region** of a hypothesis test?

* [ ] The values of the statistic close to the hypothesised parameter
* [x] The set of test-statistic values for which $H_0$ is rejected
* [ ] The set of values for which $H_0$ is proven true
* [ ] The entire distribution of the sample data

> **Explanation:** The critical (rejection) region has probability $\alpha$ under $H_0$ and lies in the tail or tails named by $H_1$. Values outside it lead to failing to reject, which does not prove $H_0$.

#### Q. A test gives **p = 0.08** with α = 0.05. What is the correct conclusion?

* [ ] Reject $H_0$; the result is statistically significant
* [ ] Accept $H_0$; the null hypothesis has been shown to be true
* [x] Fail to reject $H_0$; the evidence against it is insufficient at this level
* [ ] Reject $H_0$ because p is close to α

> **Explanation:** Since $0.08 > 0.05$ we fail to reject $H_0$. That is not the same as showing $H_0$ is true: the study may simply lack power.

#### Q. In a **paired t-test**, which quantity is assumed to be approximately normally distributed?

* [x] The within-pair differences
* [ ] The raw values in each group separately
* [ ] The pooled values from both groups combined
* [ ] The ranks of the observations

> **Explanation:** A paired t-test is a one-sample t-test on the differences $d_i = x_i - y_i$, so normality is needed only for the differences.

#### Q. What does the **standard error of the mean** measure?

* [ ] The spread of individual values in the population
* [x] The standard deviation of the sampling distribution of $\bar{x}$
* [ ] The probability of a Type I error
* [ ] The distance between the sample mean and the median

> **Explanation:** $SE(\bar{x}) = \sigma/\sqrt{n}$ describes how much the sample mean varies from sample to sample. The population SD $\sigma$ describes individual values.

#### Q. What is a **Type I error**?

* [x] Rejecting the null hypothesis when it is true
* [ ] Failing to reject the null hypothesis when it is false
* [ ] Choosing a significance level that is too large
* [ ] Using a one-tailed test when a two-tailed test was needed

> **Explanation:** A Type I error is a false positive, and its probability is $\alpha$. Failing to reject a false null is a Type II error.

#### Q. Which outcome is a **Type II error**?

* [ ] Rejecting the null hypothesis when it is true
* [x] Failing to reject the null hypothesis when it is false
* [ ] Rejecting the null hypothesis when it is false
* [ ] Failing to reject the null hypothesis when it is true

> **Explanation:** A Type II error is a false negative, and its probability is $\beta$. Rejecting a false null and keeping a true null are both correct decisions.

#### Q. What is the **power** of a test?

* [x] The probability of rejecting $H_0$ when it is false
* [ ] The probability of failing to reject $H_0$ when it is false
* [ ] The probability of rejecting $H_0$ when it is true
* [ ] The probability that $H_0$ is true given the data

> **Explanation:** Power $= 1 - \beta$ is the chance of detecting a real effect. The second option is $\beta$ and the third is $\alpha$.

#### Q. What does the one-way ANOVA **F-statistic** compare?

* [ ] The largest group mean with the smallest group mean
* [x] The between-group mean square with the within-group mean square
* [ ] The variance of one group with the variance of another group
* [ ] The observed cell counts with the expected cell counts

> **Explanation:** $F = MST/MSE$. When the group means are equal both mean squares estimate $\sigma^2$, so $F \approx 1$. Large values suggest the means differ.

#### Q. A sample of $n = 36$ has mean $\bar{x} = 52$ and standard deviation $s = 6$. What is the t-statistic for testing $H_0: \mu = 50$?

* [ ] 0.33
* [ ] 12.0
* [x] 2.0
* [ ] 0.5

> **Explanation:** $t = \frac{\bar{x} - \mu_0}{s/\sqrt{n}} = \frac{52 - 50}{6/\sqrt{36}} = \frac{2}{1} = 2.0$, with $n - 1 = 35$ degrees of freedom. Forgetting the $\sqrt{n}$ gives 0.33.

#### Q. A sample of $n = 25$ has mean 100, and the population standard deviation is known to be $\sigma = 15$. What is the **95% confidence interval** for $\mu$?

* [x] (94.12, 105.88)
* [ ] (70.60, 129.40)
* [ ] (95.07, 104.93)
* [ ] (97.00, 103.00)

> **Explanation:** $SE = 15/\sqrt{25} = 3$ and the interval is $100 \pm 1.96 \times 3 = 100 \pm 5.88$. Using $z = 1.645$ would give the 90% interval (95.07, 104.93).

#### Q. A survey wants to **halve the margin of error** of a confidence interval for a mean, keeping the confidence level fixed. By what factor must the sample size grow?

* [ ] 2
* [x] 4
* [ ] $\sqrt{2}$
* [ ] 8

> **Explanation:** The margin of error is proportional to $1/\sqrt{n}$. To halve it, $\sqrt{n}$ must double, so $n$ must quadruple.

#### Q. Roughly how much wider is a **99%** z-interval than a **95%** z-interval built from the same data?

* [ ] About 1% wider
* [ ] About 4% wider
* [x] About 31% wider
* [ ] About twice as wide

> **Explanation:** The width is proportional to the critical value, and $z_{0.995}/z_{0.975} = 2.576/1.960 \approx 1.31$. Higher confidence costs precision.

#### Q. In a poll of 100 people, 40 support a proposal. What is the approximate **95% margin of error** for the population proportion?

* [ ] 0.049
* [x] 0.096
* [ ] 0.040
* [ ] 0.240

> **Explanation:** $SE = \sqrt{\hat{p}(1-\hat{p})/n} = \sqrt{0.4 \times 0.6/100} \approx 0.049$, and the margin is $1.96 \times 0.049 \approx 0.096$. The value 0.049 is the standard error alone.

#### Q. The 95% confidence interval for a difference in means $\mu_1 - \mu_2$ is $(-0.4, 3.2)$. What does a two-sided test of $H_0: \mu_1 = \mu_2$ at α = 0.05 conclude?

* [ ] Reject $H_0$, because most of the interval is positive
* [x] Fail to reject $H_0$, because the interval contains 0
* [ ] Reject $H_0$, because the interval is wider than 3
* [ ] The interval gives no information about the test

> **Explanation:** A 95% interval contains exactly the null values that a two-sided test at $\alpha = 0.05$ would not reject. Since 0 is inside $(-0.4, 3.2)$, $H_0$ is not rejected.

#### Q. A two-sided z-test gives a statistic of **z = 2.5**. What is the p-value, approximately?

* [ ] 0.0062
* [x] 0.0124
* [ ] 0.0500
* [ ] 0.9938

> **Explanation:** $P(Z \ge 2.5) \approx 0.0062$, and a two-sided test doubles it: $2 \times 0.0062 \approx 0.0124$. The value 0.0062 is the one-sided p-value.

#### Q. A test has **power 0.80**. What is the probability of a Type II error for that effect size?

* [ ] 0.05
* [ ] 0.80
* [x] 0.20
* [ ] 0.95

> **Explanation:** Power $= 1 - \beta$, so $\beta = 1 - 0.80 = 0.20$. This is unrelated to $\alpha$, which governs Type I errors.

#### Q. A one-sample two-sided z-test at α = 0.05 should have power 0.80 to detect a shift of $\Delta = 5$ when $\sigma = 10$. About how many observations are needed?

* [ ] 16
* [x] 32
* [ ] 63
* [ ] 126

> **Explanation:** $n \approx (z_{0.975} + z_{0.80})^2\sigma^2/\Delta^2 = (1.96 + 0.84)^2 \times 100/25 \approx 31.4$, so round up to 32. The value 63 is the per-group size for a two-sample test.

#### Q. Group means are 105 and 100, and the pooled standard deviation is 10. What is **Cohen's d**?

* [ ] 0.05
* [x] 0.5
* [ ] 5.0
* [ ] 2.0

> **Explanation:** $d = (\bar{x}_1 - \bar{x}_2)/s_p = 5/10 = 0.5$, conventionally a medium effect. Effect size describes magnitude, which a p-value does not.

#### Q. A trial with 200,000 participants finds that a drug lowers blood pressure by 0.3 mmHg, with p < 0.001. What is the best interpretation?

* [ ] The effect must be clinically important because p is tiny
* [x] The effect is statistically significant but may be too small to matter
* [ ] The p-value shows there is a 99.9% chance the drug works
* [ ] The result is a Type I error because the effect is small

> **Explanation:** With huge samples even trivial effects give tiny p-values. Statistical significance is not practical significance, so the effect size must be judged on its own.

#### Q. If 10 independent tests are each run at α = 0.05 and **all null hypotheses are true**, what is the probability of at least one false rejection?

* [ ] 0.05
* [ ] 0.50
* [x] About 0.40
* [ ] About 0.005

> **Explanation:** $P(\text{at least one}) = 1 - (1 - 0.05)^{10} = 1 - 0.95^{10} \approx 0.401$. This inflation of the family-wise error rate is the multiple-comparisons problem.

#### Q. A study runs **10 tests** and wants the family-wise error rate at most 0.05. What per-test threshold does the Bonferroni correction use?

* [ ] 0.05
* [x] 0.005
* [ ] 0.0005
* [ ] 0.5

> **Explanation:** Bonferroni tests each hypothesis at $\alpha/m = 0.05/10 = 0.005$. It is simple but conservative, so it can miss real effects.

#### Q. Five tests give ordered p-values 0.001, 0.012, 0.020, 0.041, 0.300. Using the **Benjamini–Hochberg** procedure at FDR level 0.05, how many hypotheses are rejected?

* [ ] 1
* [ ] 2
* [x] 3
* [ ] 4

> **Explanation:** Compare $p_{(i)}$ with $\frac{i}{5}(0.05)$: 0.001 ≤ 0.01, 0.012 ≤ 0.02, 0.020 ≤ 0.03, but 0.041 > 0.04 and 0.300 > 0.05. The largest passing rank is 3, so the three smallest are rejected.

#### Q. How does controlling the **false discovery rate (FDR)** differ from controlling the family-wise error rate (FWER)?

* [ ] FDR limits the probability of making any false rejection at all
* [x] FDR limits the expected proportion of false rejections among all rejections
* [ ] FDR limits the probability of a Type II error in each test
* [ ] FDR applies only when exactly two hypotheses are tested

> **Explanation:** FWER control (e.g. Bonferroni, Holm) bounds the chance of even one false positive. FDR control (e.g. Benjamini–Hochberg) tolerates some false positives, which gives more power when many tests are run.

#### Q. What are the **degrees of freedom** for a chi-square test of independence on a 3 × 4 contingency table?

* [ ] 12
* [ ] 11
* [x] 6
* [ ] 7

> **Explanation:** $df = (r-1)(c-1) = (3-1)(4-1) = 6$. The 11 would be $rc - 1$, which ignores that the row and column totals are fixed.

#### Q. In a contingency table with grand total 200, a cell's row total is 60 and its column total is 50. What is its **expected count** under independence?

* [ ] 30
* [ ] 25
* [x] 15
* [ ] 110

> **Explanation:** $E = \frac{\text{row total} \times \text{column total}}{\text{grand total}} = \frac{60 \times 50}{200} = 15$.

#### Q. A coin is tossed 50 times and lands heads 30 times. What is the **chi-square goodness-of-fit statistic** for testing that the coin is fair?

* [ ] 1.0
* [x] 2.0
* [ ] 4.0
* [ ] 10.0

> **Explanation:** The expected counts are 25 and 25, so $\chi^2 = \frac{(30-25)^2}{25} + \frac{(20-25)^2}{25} = 1 + 1 = 2.0$, with $df = 1$. This is below the 0.05 critical value 3.84.

#### Q. Which condition is commonly required for the chi-square approximation to be reliable?

* [ ] Every observed count is at least 30
* [x] The expected counts are large enough, typically at least 5 per cell
* [ ] The data are normally distributed within each category
* [ ] The row and column totals are all equal

> **Explanation:** The chi-square distribution is a large-sample approximation that depends on expected counts, not observed ones. With small expected counts, combine categories or use an exact test.

#### Q. A one-way ANOVA compares **k = 4 groups** with **N = 40 observations** in total. What are the degrees of freedom of the F-statistic?

* [ ] (4, 40)
* [ ] (3, 39)
* [x] (3, 36)
* [ ] (4, 36)

> **Explanation:** The numerator (between groups) has $k - 1 = 3$ df and the denominator (within groups) has $N - k = 36$ df. The total df is $N - 1 = 39$.

#### Q. A one-way ANOVA with 3 groups and 30 observations has SSB = 60 and SSW = 270. What is the **F-statistic**?

* [ ] 0.22
* [ ] 2.0
* [x] 3.0
* [ ] 6.0

> **Explanation:** $MSB = 60/(3-1) = 30$ and $MSW = 270/(30-3) = 10$, so $F = 30/10 = 3.0$ on (2, 27) df. Dividing the raw sums of squares would give 0.22.

#### Q. Why is one-way ANOVA preferred over running a t-test for **every pair** of five groups?

* [ ] Pairwise t-tests cannot handle more than two groups at once
* [x] Ten separate tests at α = 0.05 inflate the overall chance of a false positive
* [ ] ANOVA does not require any assumptions about the data
* [ ] ANOVA tells you directly which pairs of means differ

> **Explanation:** Five groups give $\binom{5}{2} = 10$ pairwise tests, so the family-wise error rate is far above 0.05. ANOVA tests all means at once; post-hoc methods then identify which pairs differ.

#### Q. After a significant one-way ANOVA, which method compares **all pairs of group means** while controlling the family-wise error rate?

* [ ] Levene's test
* [x] Tukey's honest significant difference (HSD)
* [ ] Chi-square test of independence
* [ ] Shapiro–Wilk test

> **Explanation:** Tukey's HSD is a post-hoc procedure for all pairwise comparisons. Levene's test checks equal variances and Shapiro–Wilk checks normality, both of which are assumption checks.

#### Q. What are the **degrees of freedom** for a one-sample t-test with n = 16 observations?

* [ ] 16
* [x] 15
* [ ] 14
* [ ] 32

> **Explanation:** Estimating the mean uses up one degree of freedom, so $df = n - 1 = 15$. The two-tailed 5% critical value is then about 2.131.

#### Q. Why does a t-interval use a **larger critical value** than a z-interval at the same confidence level?

* [ ] Because the sample mean is biased when σ is unknown
* [x] Because estimating σ with s adds uncertainty, giving the t distribution heavier tails
* [ ] Because the t distribution is skewed to the right
* [ ] Because t-intervals are used only for large samples

> **Explanation:** The t distribution accounts for the extra variability of $s$. Its tails are heavier than the normal's for small $df$ and it approaches $N(0,1)$ as $df$ grows.

#### Q. Which version of the two-sample t-test should you use when the two groups appear to have **clearly unequal variances**?

* [ ] Pooled-variance t-test
* [x] Welch's t-test
* [ ] Paired t-test
* [ ] One-sample t-test

> **Explanation:** Welch's test uses separate variance estimates and approximate degrees of freedom, so it does not rely on equal variances. The pooled test assumes $\sigma_1^2 = \sigma_2^2$.

#### Q. In a paired study of 25 subjects, the differences have mean 1.5 and standard deviation 3. What is the **paired t-statistic**?

* [ ] 0.5
* [ ] 12.5
* [x] 2.5
* [ ] 7.5

> **Explanation:** $t = \frac{\bar{d}}{s_d/\sqrt{n}} = \frac{1.5}{3/\sqrt{25}} = \frac{1.5}{0.6} = 2.5$ on 24 df. Omitting $\sqrt{n}$ gives 0.5.
