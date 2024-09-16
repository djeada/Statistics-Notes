## Multiple Comparisons

When conducting multiple hypothesis tests simultaneously, the likelihood of committing at least one Type I error (falsely rejecting a true null hypothesis) increases. This increase is due to the problem known as the "multiple comparisons problem" or the "look-elsewhere effect". The methods to address this issue typically involve adjustments to the significance level or p-values, and each has its advantages and disadvantages. 

### Data Snooping and the Multiple Testing Fallacy

- A **1992 Swedish study** suggested a statistically significant link between living near power lines and childhood leukemia, but follow-up studies failed to replicate the finding.
- The study performed **800 statistical tests**, which greatly increased the chance of finding false positives due to random chance.
- The **multiple testing fallacy** occurs when running a large number of tests. Even when no true effect exists, some tests will yield significant results by coincidence. For example, if the significance level is 1%, you would expect 8 false positives from 800 tests.

#### Multiple Comparisons Problem

- The **p-value** represents the probability of obtaining a result as extreme as the observed one if the null hypothesis is true. A smaller p-value indicates stronger evidence against the null hypothesis.
- The **look-elsewhere effect** or **data snooping** refers to the issue that, when many tests are conducted, some will appear significant just by chance, even if no real effect is present.

#### Reproducibility and Replicability Crisis

- **Reproducibility** refers to achieving the same results when using the same data and methods, while **replicability** involves obtaining similar results when using different data or methods.
- A growing concern about the reliability of scientific findings, known as the **reproducibility and replicability crisis**, has been highlighted by issues such as data snooping. For example, John Ioannidis’s 2005 paper, *"Why Most Published Research Findings Are False,"* underscores this problem in scientific research.

#### Addressing the Multiple Testing Problem

- The **Bonferroni correction** adjusts p-values by multiplying them by the number of tests conducted, ensuring that the overall probability of making at least one false positive is no more than 5%. However, it is very conservative and may render true effects insignificant.
- The **false discovery proportion (FDP)** offers a more flexible approach, focusing on controlling the proportion of false discoveries among all findings. For instance, if 80 true discoveries are made alongside 41 false discoveries, the FDP is 34%, meaning 34% of the discoveries are false positives.

#### False Discovery Rate (FDR)

- The **false discovery rate (FDR)** represents the expected proportion of false discoveries among all discoveries.
- The **Benjamini-Hochberg procedure** controls the FDR by ranking p-values and selecting the largest p-value that satisfies a certain condition, ensuring a controlled rate of false discoveries, such as 5%.

#### Using a Validation Set to Avoid Data Snooping

- The **validation set approach** involves splitting the data into two distinct sets to prevent data snooping.
- The **model-building set** is used to explore the data and identify potential relationships during the analysis phase.
- The **validation set** is reserved for testing hypotheses that emerge from the model-building phase, ensuring an unbiased evaluation of the findings.
- It is **crucial** that the validation set remains unexamined during the exploratory phase to avoid introducing bias or data snooping into the results.

### Family-wise Error Rate (FWER)

The family-wise error rate (FWER) is the probability of making at least one Type I error among all the tests in a family. Controlling FWER maintains overall confidence in the results when conducting multiple tests.

#### Bonferroni Correction

The Bonferroni correction is a common method for controlling the FWER. It adjusts the significance level (α) by dividing it by the number of tests performed (n):

$$
\alpha_{\text{{adjusted}}} = \frac{\alpha}{n}
$$

This adjusted significance level is then used to compute the critical values for each test. The Bonferroni correction is inherently conservative, making it more likely to commit Type II errors (falsely accepting a false null hypothesis), especially when there are many tests or the tests are not independent.
Here is an improved version of your example with better LaTeX formatting and more explanation:

#### Example: Bonferroni Correction

Suppose we are conducting 20 independent hypothesis tests, and the significance level for the family-wise error rate is $\alpha = 0.05$. To control for multiple comparisons using the Bonferroni correction, we adjust the significance level by dividing $\alpha$ by the number of tests.

The Bonferroni-adjusted significance level, $\alpha_{\text{adjusted}}$, is calculated as follows:

$$
\alpha_{\text{adjusted}} = \frac{\alpha}{m} = \frac{0.05}{20} = 0.0025
$$

where:

- $\alpha = 0.05$ is the desired overall significance level,
- $m = 20$ is the number of tests being conducted.

**Conclusion:**

After applying the Bonferroni correction, we would reject the null hypothesis for an individual test only if its p-value is less than $0.0025$. This correction helps control the family-wise error rate, reducing the chance of Type I errors (false positives) across multiple tests. However, it also makes the test more conservative, increasing the likelihood of Type II errors (false negatives).

### False Discovery Rate (FDR)

In contrast to FWER, the false discovery rate (FDR) controls for the expected proportion of false positives among all rejected null hypotheses. FDR controlling procedures are generally more powerful than FWER controlling methods, making them particularly suitable for exploratory studies where the discovery of new findings is prioritized.

#### Benjamini-Hochberg Procedure

The Benjamini-Hochberg (BH) procedure is widely used for controlling the FDR. This method involves ordering the p-values from smallest to largest and then comparing each p-value to an adjusted significance level that depends on its rank (i) and the total number of tests (n):

$$
\alpha_{\text{{adjusted}}} = \frac{\alpha \times i}{n}
$$

We reject the null hypothesis for all tests where the p-value is less than or equal to the adjusted significance level. 

Here is an improved and clearer version of your example with better formatting and clearer explanation:


#### Example: Multiple Hypothesis Testing

Suppose we are conducting six hypothesis tests, and the p-values obtained from these tests are:

$$
\{0.001, 0.008, 0.039, 0.041, 0.042, 0.06\}
$$

We will apply the Bonferroni-Holm correction to control the family-wise error rate at $\alpha = 0.05$. The procedure requires us to compare each ordered p-value to a sequentially adjusted significance level.

**Step-by-Step Procedure:**

I. **Order the p-values** in ascending order: 

$$
0.001, 0.008, 0.039, 0.041, 0.042, 0.06
$$

II. **Adjust the significance level** for each test. The adjusted significance level for the $i$-th test is calculated as:

$$
\alpha_i = \frac{\alpha}{n - i + 1}
$$

where $n$ is the total number of tests (in this case, $n = 6$) and $\alpha = 0.05$.

III. **Compare each p-value to its adjusted $\alpha_i$**:

For $p_1 = 0.001$:

$$
0.001 < \frac{0.05}{6} \approx 0.00833 \quad \text{(Reject $H_0$)}
$$

For $p_2 = 0.008$:

$$
0.008 < \frac{0.05}{5} = 0.01 \quad \text{(Reject $H_0$)}
$$

For $p_3 = 0.039$:

$$
0.039 > \frac{0.05}{4} = 0.0125 \quad \text{(Fail to Reject $H_0$)}
$$

Since we fail to reject $H_0$ at this step, there is no need to test further hypotheses, as the procedure stops here.

**Conclusion:**

Using the Bonferroni-Holm procedure, we reject the null hypothesis for the first two tests but fail to reject for the remaining tests.

This method helps reduce the probability of Type I errors (false positives) when conducting multiple comparisons. However, as with all statistical procedures, there is a trade-off, potentially increasing the risk of Type II errors (false negatives). Researchers must balance these risks depending on the context and goals of their study.
