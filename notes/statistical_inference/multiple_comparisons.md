## Multiple Comparisons

When conducting multiple hypothesis tests simultaneously, the likelihood of committing at least one Type I error (falsely rejecting a true null hypothesis) increases. This increase is due to the problem known as the "multiple comparisons problem" or the "look-elsewhere effect". The methods to address this issue typically involve adjustments to the significance level or p-values, and each has its advantages and disadvantages. 


#### Data Snooping and the Multiple Testing Fallacy
- **Example**: A 1992 Swedish study found a statistically significant link between living near power lines and childhood leukemia. However, follow-up analyses could not replicate this finding.
  
- **Explanation**: The study performed 800 different statistical tests, increasing the likelihood of finding false-positive results purely by chance.
    - **Multiple Testing Fallacy**: If we run a large number of tests, even if there is no true effect, we expect a certain number of significant results just by random chance.
    - For example, if the significance level is 1%, we expect \( 800 \times 1\% = 8 \) false positives.

#### Multiple Comparisons Problem
- **P-value**: Represents the probability of obtaining a result as extreme as the observed one if the null hypothesis is true.
    - A smaller p-value indicates stronger evidence against the null hypothesis.
    - If \( p < 0.01 \), the result is considered *highly significant*.
  
- **Issue**: When many tests are conducted, some tests will produce significant results purely due to chance. This phenomenon is called the *look-elsewhere effect* or *data snooping*.

#### Reproducibility and Replicability Crisis
- **Reproducibility**: Getting the same results when using the same data and methods.
- **Replicability**: Getting similar results when using different data, samples, or methods.
  
- **Crisis**: Data snooping and other issues have led to a growing concern about the reliability of scientific findings.
    - Example: John Ioannidis's 2005 paper, *"Why Most Published Research Findings Are False,"* highlighted this problem in scientific research.

#### Addressing the Multiple Testing Problem
1. **Bonferroni Correction**:
   - Adjusts p-values by multiplying them by the number of tests conducted (\( m \)).
   - Ensures that the probability of making at least one false positive is no more than 5%.
   - **Downside**: Very conservative; adjusted p-values may no longer be significant, even if a real effect is present.

2. **False Discovery Proportion (FDP)**:
   - A more flexible approach, focusing on controlling the proportion of false discoveries among all discoveries.
   - **FDP formula**: 
     \[
     \text{FDP} = \frac{\text{Number of false discoveries}}{\text{Total number of discoveries}}
     \]
   - **Example**: If we test 1,000 hypotheses, 900 are true null hypotheses, and 100 are true alternative hypotheses. If we make 80 true discoveries and 41 false discoveries, the FDP is:
     \[
     \text{FDP} = \frac{41}{121} = 0.34
     \]
     meaning 34% of the discoveries are false positives.

#### False Discovery Rate (FDR)
- **FDR**: The expected proportion of false discoveries among all discoveries.
    - **Benjamini-Hochberg Procedure**: Controls FDR at a chosen level (e.g., 5%).
        1. Sort the p-values in increasing order.
        2. Find the largest \( k \) such that \( p(k) \leq \frac{k}{m} \alpha \), where \( m \) is the number of tests and \( \alpha \) is the desired significance level (e.g., 5%).
        3. Declare discoveries for all tests up to \( k \).

#### Using a Validation Set to Avoid Data Snooping
- **Validation Set Approach**:
    - Split the data into two sets:
      - **Model-building set**: Used to explore data and find potential relationships.
      - **Validation set**: Used to test hypotheses found in the model-building phase.
  
    - **Important**: During the exploratory phase, the validation set should not be examined to ensure the results are not influenced by data snooping.





### Family-wise Error Rate (FWER)

The family-wise error rate (FWER) is the probability of making at least one Type I error among all the tests in a family. Controlling FWER maintains overall confidence in the results when conducting multiple tests.

#### Bonferroni Correction

The Bonferroni correction is a common method for controlling the FWER. It adjusts the significance level (α) by dividing it by the number of tests performed (n):

$$
\alpha_{\text{{adjusted}}} = \frac{\alpha}{n}
$$

This adjusted significance level is then used to compute the critical values for each test. The Bonferroni correction is inherently conservative, making it more likely to commit Type II errors (falsely accepting a false null hypothesis), especially when there are many tests or the tests are not independent.

#### Example

Suppose we have α = 0.05 and we are conducting 20 independent tests. Then, the Bonferroni corrected α is:

$$
\alpha_{\text{{adjusted}}} = \frac{0.05}{20} = 0.0025
$$

Thus, for each test, we would reject the null hypothesis only if the p-value is less than 0.0025.

### False Discovery Rate (FDR)

In contrast to FWER, the false discovery rate (FDR) controls for the expected proportion of false positives among all rejected null hypotheses. FDR controlling procedures are generally more powerful than FWER controlling methods, making them particularly suitable for exploratory studies where the discovery of new findings is prioritized.

#### Benjamini-Hochberg Procedure

The Benjamini-Hochberg (BH) procedure is widely used for controlling the FDR. This method involves ordering the p-values from smallest to largest and then comparing each p-value to an adjusted significance level that depends on its rank (i) and the total number of tests (n):

$$
\alpha_{\text{{adjusted}}} = \frac{\alpha \times i}{n}
$$

We reject the null hypothesis for all tests where the p-value is less than or equal to the adjusted significance level. 

#### Example

Suppose we have a set of p-values {0.001, 0.008, 0.039, 0.041, 0.042, 0.06} for six tests with α = 0.05. 

We order the p-values and compare to the adjusted α:

1. 0.001 < 0.05 * 1/6 = 0.00833 - reject
2. 0.008 < 0.05 * 2/6 = 0.01667 - reject
3. 0.039 < 0.05 * 3/6 = 0.02500 - reject
4. 0.041 < 0.05 * 4/6 = 0.03333 - reject
5. 0.042 > 0.05 * 5/6 = 0.04167 - fail to reject
6. 0.06 > 0.05 * 6/6 = 0.05000 - fail to reject

Thus, we would reject the null hypothesis for the first four tests and fail to reject for the last two.

In the world of multiple comparisons, researchers must carefully balance the risk of Type I and Type II errors based on the context and goals of their study.
