

#### Scenario: Peer Assessment and Learning
- **Research Question**: Does peer assessment enhance student learning? Students were randomly assigned to one of three groups:
  - **Homework only**
  - **Homework with Peer Assessment (PA)**
  - **Study without homework**
  
- The final exam scores were summarized using boxplots. The key question is whether the three different treatments lead to different outcomes.

#### Hypotheses
- **Null Hypothesis (H0)**: All group means are equal (i.e., no significant difference between treatments).
- **Alternative Hypothesis (HA)**: The group means differ, indicating that the treatments have different effects.

#### Two-Sample t-Test for Two Groups
- For comparing only two groups, a two-sample t-test can be used:
  \[
  t = \frac{\text{difference in sample means}}{\text{SE of difference}}
  \]
  - This test compares the difference in sample means relative to the chance variability (SE).
  
#### ANOVA: Generalizing for Multiple Groups
- **Analysis of Variance (ANOVA)**: Generalizes the t-test to compare more than two groups.
  - The key idea is to compare the variance between the group means to the variance within the groups.

#### The ANOVA Methodology
1. **Treatment Variance**: Measures how much the group means differ from the overall mean.
    - **Sum of squares for treatments (SST)**:
      \[
      SST = \sum (\bar{y}_j - \bar{y})^2
      \]
      where \( \bar{y}_j \) is the mean of group \( j \), and \( \bar{y} \) is the overall mean.
      
    - **Treatment mean square (MST)**: 
      \[
      MST = \frac{SST}{k - 1}
      \]
      where \( k \) is the number of groups.
      
2. **Error Variance**: Measures how much individual scores within each group differ from their group mean.
    - **Sum of squares for error (SSE)**:
      \[
      SSE = \sum (y_{ij} - \bar{y}_j)^2
      \]
      where \( y_{ij} \) is an individual score, and \( \bar{y}_j \) is the mean of group \( j \).
      
    - **Error mean square (MSE)**: 
      \[
      MSE = \frac{SSE}{N - k}
      \]
      where \( N \) is the total number of observations and \( k \) is the number of groups.

3. **F-statistic**: Compares the variance between the groups to the variance within the groups:
    \[
    F = \frac{MST}{MSE}
    \]
    - Under H0, the F-statistic should be close to 1. Large F-values suggest significant differences between the group means.
    - The F-distribution with degrees of freedom \( k - 1 \) and \( N - k \) is used to determine the p-value.

#### Example: Peer Assessment Data
- **ANOVA Table for the Example**:
  \[
  \begin{array}{|c|c|c|c|c|}
  \hline
  \text{Source} & \text{df} & \text{Sum of Squares} & \text{Mean Square} & F \\
  \hline
  \text{Treatment} & 2 & 98.4 & 47.2 & 2.49 \\
  \text{Error} & 38 & 723.8 & 19.1 & \\
  \text{Total} & 40 & 822.2 & & \\
  \hline
  \end{array}
  \]
  - **p-value** = 0.097: There is not enough evidence to reject H0 at the 5% significance level.

#### Interpretation of ANOVA
- If the p-value is small (e.g., less than 0.05), we reject H0 and conclude that at least one group mean differs from the others.
- If the p-value is large (e.g., 0.097), as in this case, we do not have sufficient evidence to reject H0, meaning the group means might be equal.

#### The One-Way ANOVA Model
- **Model**: \( y_{ij} = \mu_j + \epsilon_{ij} \)
    - \( \mu_j \): Mean of the jth group.
    - \( \epsilon_{ij} \): Random error term with mean 0 and variance \( \sigma^2 \).
  
- **Alternative View**: Instead of focusing on group means \( \mu_j \), we examine deviations \( \tau_j = \mu_j - \mu \), where \( \mu \) is the overall mean.

#### F-Test Assumptions
1. **Equal Variances**: Assumes that the variances within all groups are equal.
    - This can be visually checked with boxplots or tested formally.
2. **Independence**: Assumes that observations within and across groups are independent, typically ensured through random assignment.

#### Post-ANOVA Testing
- If ANOVA rejects H0, further analysis is needed to understand how the groups differ.
    - **Pairwise Comparisons**: A two-sample t-test can be conducted between each pair of group means, but multiple comparisons require adjustments (e.g., Bonferroni correction) to avoid inflating the Type I error rate.
