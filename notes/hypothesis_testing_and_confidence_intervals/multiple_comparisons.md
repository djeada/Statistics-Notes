## Multiple Comparisons

When performing multiple hypothesis tests simultaneously, the chance of making a type I error (falsely rejecting a true null hypothesis) increases. This phenomenon is known as the multiple comparisons problem. To account for this issue, several correction methods have been developed.

### Family-wise Error Rate (FWER)

Family-wise error rate (FWER) is the probability of making at least one type I error across all tests in a family. It is important to control the FWER when conducting multiple tests to maintain the overall confidence in the results.

#### Bonferroni Correction

One of the most common methods for controlling FWER is the Bonferroni correction. This method adjusts the significance level (α) by dividing it by the number of tests performed:

$$
\alpha_{adjusted} = \frac{\alpha}{n}
$$

where $n$ is the number of tests being conducted. This adjusted significance level is then used to determine the critical value for each test. The Bonferroni correction is considered to be conservative, as it may be too strict, especially when there is a large number of tests.

### False Discovery Rate (FDR)

An alternative approach to controlling the FWER is controlling the false discovery rate (FDR), which is the expected proportion of false positives among all rejected null hypotheses. This approach is less conservative than controlling the FWER and can be more powerful in certain situations.

#### Benjamini-Hochberg Procedure

The Benjamini-Hochberg (BH) procedure is a widely used method for controlling the FDR. It works by ordering the p-values from the multiple tests and comparing each p-value to an adjusted significance level:

$$
\alpha_{adjusted} = \frac{\alpha \times i}{n}
$$

where $i$ is the rank of the p-value in the ordered list and $n$ is the number of tests. The null hypothesis is rejected for all tests with p-values less than or equal to the adjusted significance level. The BH procedure is less conservative than the Bonferroni correction and provides better control of the FDR.

It is important to choose an appropriate method for adjusting for multiple comparisons based on the specific goals and requirements of the study.
