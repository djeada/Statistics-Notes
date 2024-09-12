# ANOVA and the Analysis of Variance for Multiple Groups

## Scenario: Peer Assessment and Student Learning

### Research Question

**Does peer assessment enhance student learning?**

In a study to answer this question, students were randomly assigned to one of three treatment groups:

1. **Homework Only**: Students complete homework assignments without any peer assessment.
2. **Homework with Peer Assessment (PA)**: Students complete homework assignments and participate in peer assessment.
3. **Study Without Homework**: Students study the material independently without homework assignments.

The final exam scores for students in each group were collected and summarized using boxplots. The primary objective is to determine whether these different instructional methods lead to different learning outcomes, as measured by the final exam scores.

---

## Formulating the Hypotheses

To statistically assess the impact of the different treatments, we set up the following hypotheses:

- **Null Hypothesis ($H_0$)**: All group means are equal. That is, there is no significant difference in final exam scores between the three treatment groups.
  
  $$
  H_0: \mu_1 = \mu_2 = \mu_3
  $$
  
- **Alternative Hypothesis ($H_A$)**: At least one group mean is different, indicating that the treatments have different effects on student learning.
  
  $$
  H_A: \text{At least one } \mu_j \text{ differs}
  $$

---

## Comparing Two Groups: The Two-Sample t-Test

When comparing only two groups, the **two-sample t-test** is appropriate. It tests whether there is a significant difference between the means of two independent groups.

### t-Test Formula

The t-statistic is calculated as:

$$
t = \frac{\bar{y}_1 - \bar{y}_2}{SE_{\bar{y}_1 - \bar{y}_2}}
$$

- $\bar{y}_1, \bar{y}_2$: Sample means of groups 1 and 2.
- $SE_{\bar{y}_1 - \bar{y}_2}$: Standard error of the difference between the two sample means.

### Standard Error Calculation

Assuming equal variances:

$$
SE_{\bar{y}_1 - \bar{y}_2} = \sqrt{\frac{s^2}{n_1} + \frac{s^2}{n_2}}
$$

- $s^2$: Pooled sample variance.
- $n_1, n_2$: Sample sizes of groups 1 and 2.

### Limitations

- The t-test is limited to comparing **two** groups.
- When dealing with more than two groups, the risk of Type I error increases with multiple t-tests.

---

## ANOVA: Analysis of Variance for Multiple Groups

To compare **three or more groups**, we use **Analysis of Variance (ANOVA)**. ANOVA tests for significant differences among group means by analyzing variances.

### Key Concepts

- **Between-Groups Variance**: Variability due to the interaction between the groups (treatments).
- **Within-Groups Variance**: Variability within each group due to individual differences.

### ANOVA Hypotheses

- **Null Hypothesis ($H_0$)**: All group means are equal.
- **Alternative Hypothesis ($H_A$)**: Not all group means are equal.

---

## The ANOVA Methodology

ANOVA partitions the total variability in the data into components attributable to various sources.

### Total Sum of Squares (SSTotal)

The **Total Sum of Squares** measures the total variability in the data:

$$
SSTotal = \sum_{i=1}^{N} (y_i - \bar{y})^2
$$

- $y_i$: Individual observations.
- $\bar{y}$: Overall mean of all observations.
- $N$: Total number of observations.

### 1. Treatment Variance (Between-Groups Variability)

**Sum of Squares for Treatments (SST)** measures the variability between the group means and the overall mean:

$$
SST = \sum_{j=1}^{k} n_j (\bar{y}_j - \bar{y})^2
$$

- $n_j$: Sample size of group $j$.
- $\bar{y}_j$: Mean of group $j$.
- $k$: Number of groups.

**Treatment Mean Square (MST)** is the average treatment variability:

$$
MST = \frac{SST}{k - 1}
$$

- Degrees of freedom for treatments: $df_{\text{Treatment}} = k - 1$.

### 2. Error Variance (Within-Groups Variability)

**Sum of Squares for Error (SSE)** measures the variability within the groups:

$$
SSE = \sum_{j=1}^{k} \sum_{i=1}^{n_j} (y_{ij} - \bar{y}_j)^2
$$

- $y_{ij}$: Individual observation in group $j$.
- $\bar{y}_j$: Mean of group $j$.

**Error Mean Square (MSE)** is the average within-group variability:

$$
MSE = \frac{SSE}{N - k}
$$

- Degrees of freedom for error: $df_{\text{Error}} = N - k$.

### 3. Calculating the F-Statistic

The **F-statistic** compares the between-groups variance to the within-groups variance:

$$
F = \frac{MST}{MSE}
$$

- Under $H_0$, $MST$ and $MSE$ estimate the same variance, so $F \approx 1$.
- A large $F$ value suggests that between-group variability is greater than within-group variability, indicating significant differences among group means.

### F-Distribution

- The F-statistic follows an F-distribution with $df_1 = k - 1$ (numerator degrees of freedom) and $df_2 = N - k$ (denominator degrees of freedom).
- The p-value is determined based on the F-distribution.

---

## Example: Peer Assessment Data

### Data Summary

Suppose we have the following data:

- **Group Sizes**:
  - Homework Only: $n_1$
  - Homework with PA: $n_2$
  - Study Without Homework: $n_3$
- **Group Means ($\bar{y}_j$)** and Variances ($s_j^2$) are calculated from the data.
- **Total Observations**: $N = n_1 + n_2 + n_3$

### ANOVA Table Construction

**ANOVA Table** summarizes the calculations:

| Source      | df            | Sum of Squares (SS) | Mean Square (MS)      | F       |
|-------------|---------------|---------------------|-----------------------|---------|
| Treatment   | $k - 1$   | SST                 | $MST = \frac{SST}{k - 1}$ | $F = \frac{MST}{MSE}$ |
| Error       | $N - k$   | SSE                 | $MSE = \frac{SSE}{N - k}$ |         |
| Total       | $N - 1$   | SSTotal             |                       |         |

**Given Example**:

| Source      | df  | Sum of Squares | Mean Square | F     |
|-------------|-----|----------------|-------------|-------|
| Treatment   | 2   | 98.4           | 49.2        | 2.57  |
| Error       | 38  | 723.8          | 19.05       |       |
| Total       | 40  | 822.2          |             |       |

### Calculations

1. **SSTotal**:

   $$
   SSTotal = SST + SSE = 98.4 + 723.8 = 822.2
   $$

2. **Degrees of Freedom**:

   - $df_{\text{Treatment}} = k - 1 = 3 - 1 = 2$
   - $df_{\text{Error}} = N - k = 41 - 3 = 38$
   - $df_{\text{Total}} = N - 1 = 41 - 1 = 40$

3. **Mean Squares**:

   - $MST = \frac{SST}{df_{\text{Treatment}}} = \frac{98.4}{2} = 49.2$
   - $MSE = \frac{SSE}{df_{\text{Error}}} = \frac{723.8}{38} \approx 19.05$

4. **F-Statistic**:

   $$
   F = \frac{MST}{MSE} = \frac{49.2}{19.05} \approx 2.58
   $$

5. **P-Value**:

   - Using F-distribution tables or software, with $df_1 = 2$ and $df_2 = 38$, we find:
   - **p-value** ≈ 0.087

### Decision

- At a significance level $\alpha = 0.05$:
  - Since $p = 0.087 > 0.05$, we **fail to reject $H_0$**.
  - There is not enough evidence to conclude that the treatments have different effects on student learning.

---

## Interpretation of ANOVA Results

### Understanding the F-Statistic

- **Small F-Value** ($\approx 1$):
  - Suggests that the variability between group means is similar to the variability within groups.
  - Implies no significant difference among group means.
  
- **Large F-Value**:
  - Indicates that the variability between group means is greater than within groups.
  - Suggests significant differences among group means.

### P-Value Interpretation

- **p-value < $\alpha$**:
  - Reject $H_0$.
  - Conclude that at least one group mean is different.
  
- **p-value ≥ $\alpha$**:
  - Fail to reject $H_0$.
  - Cannot conclude that there are differences among group means.

### Conclusion for the Example

- With a p-value of 0.087:
  - We do not have sufficient evidence at the 5% significance level to claim that peer assessment enhances student learning over the other methods.
  - However, the p-value is relatively close to 0.05, suggesting a trend that might be significant with a larger sample size.

---

## The One-Way ANOVA Model

### Statistical Model

The **one-way ANOVA model** expresses each observation as:

$$
y_{ij} = \mu_j + \epsilon_{ij}
$$

- $y_{ij}$: Observation $i$ in group $j$.
- $\mu_j$: Mean of group $j$.
- $\epsilon_{ij}$: Random error term, assumed to be independently and identically distributed (i.i.d.) with:
  - Mean $E[\epsilon_{ij}] = 0$
  - Variance $Var(\epsilon_{ij}) = \sigma^2$

### Alternative Representation

We can express the model in terms of the overall mean $\mu$ and group effects $\tau_j$:

$$
y_{ij} = \mu + \tau_j + \epsilon_{ij}
$$

- $\mu$: Overall mean.
- $\tau_j = \mu_j - \mu$: Effect of treatment $j$.

### Assumptions of the Model

1. **Normality**: The residuals $\epsilon_{ij}$ are normally distributed.
2. **Independence**: Observations are independent.
3. **Homogeneity of Variance**: The variances within each group are equal ($\sigma^2$ is constant across groups).

---

## Assumptions of the F-Test

For the results of the ANOVA F-test to be valid, certain assumptions must be met:

### 1. Equal Variances (Homogeneity of Variance)

- **Assumption**: The variances within each group are equal.
- **Checking**:
  - **Boxplots**: Visual inspection for similar spread among groups.
  - **Levene's Test**: Statistical test for equal variances.
  - **Rule of Thumb**: If the largest sample standard deviation is no more than twice the smallest, the assumption is reasonable.

### 2. Independence of Observations

- **Assumption**: Observations are independent both within and across groups.
- **Ensured By**:
  - **Random Assignment**: In experimental studies.
  - **Random Sampling**: In observational studies.

### 3. Normality of Residuals

- **Assumption**: The residuals $\epsilon_{ij}$ are normally distributed.
- **Checking**:
  - **Normal Probability Plots**: Assess the normality of residuals.
  - **Shapiro-Wilk Test**: Formal statistical test for normality.

---

## Post-ANOVA Testing

If the ANOVA F-test leads us to reject $H_0$, indicating that not all group means are equal, we may want to identify **which groups differ**.

### Multiple Comparison Procedures

Performing multiple t-tests increases the risk of Type I error (false positives). To control for this, we use:

#### 1. Bonferroni Correction

- Adjusts the significance level:
  
  $$
  \alpha' = \frac{\alpha}{\text{Number of Comparisons}}
  $$
  
- Example: For 3 groups, there are $\frac{3 \times 2}{2} = 3$ comparisons.

#### 2. Tukey's Honest Significant Difference (HSD) Test

- Controls the family-wise error rate.
- Computes confidence intervals for all pairwise differences.

### Steps for Pairwise Comparisons

1. **Calculate the Standard Error for Differences**:

   $$
   SE_{\bar{y}_i - \bar{y}_j} = \sqrt{MSE \left( \frac{1}{n_i} + \frac{1}{n_j} \right)}
   $$

2. **Compute the t-Statistic for Each Pair**:

   $$
   t = \frac{\bar{y}_i - \bar{y}_j}{SE_{\bar{y}_i - \bar{y}_j}}
   $$

3. **Determine the Adjusted p-Values**:

   - Use the adjusted significance level or critical values from Tukey's distribution.

---

## Practical Application Steps

### 1. Conduct ANOVA

- Compute SST, SSE, MST, MSE, and F-statistic.
- Determine the p-value using the F-distribution.
- Decide whether to reject $H_0$ based on the p-value.

### 2. Check Assumptions

- **Equal Variances**: Use boxplots or formal tests.
- **Normality**: Assess residuals.
- **Independence**: Ensure study design supports independence.

### 3. Interpret Results

- If $H_0$ is not rejected:
  - Conclude that there is no significant difference among group means.
- If $H_0$ is rejected:
  - Proceed to post-hoc tests to identify specific group differences.
