# Detailed Notes on Chi-Square Tests and Categorical Data Analysis

## Categorical Data and Contingency Tables

### Categorical Data

**Categorical data** involves variables that represent groupings or categories rather than numerical values. These categories are usually qualitative and can be nominal (no inherent order) or ordinal (with a logical order). Each data point falls into one and only one category.

- **Example**: The survival status of passengers on the Titanic, categorized by ticket class.
  - **Survival Status**: "Survived" or "Died".
  - **Ticket Class**: First, Second, Third, Crew.

### Contingency Tables

A **contingency table** (also known as a cross-tabulation or crosstab) is a matrix used to display the frequency distribution of variables. It allows us to analyze the relationship between two or more categorical variables.

- **Example**: The Titanic survival data organized into a 2×4 contingency table:

|               | First Class | Second Class | Third Class | Crew | **Total** |
|---------------|-------------|--------------|-------------|------|-----------|
| **Survived**  |      a      |       b      |      c      |  d   |     S     |
| **Died**      |      e      |       f      |      g      |  h   |     D     |
| **Total**     |     325     |      285     |     706     | 885  |   2,201   |

Here, $a$ to $h$ represent the observed counts in each category.

## Chi-Square Tests: Overview

The **chi-square ($\chi^2$) test** is a statistical method used to determine if there is a significant difference between expected and observed frequencies in one or more categories. It helps assess whether any observed deviations could be due to chance.

### Types of Chi-Square Tests

1. **Goodness-of-Fit Test**: Determines if an observed frequency distribution matches an expected distribution.
2. **Test of Homogeneity**: Assesses whether different populations have the same distribution of a single categorical variable.
3. **Test of Independence**: Evaluates whether two categorical variables are independent within a single population.

---

## 1. Testing Goodness-of-Fit

### Hypotheses

- **Null Hypothesis ($H_0$)**: The observed frequencies match the expected frequencies. There is no significant difference between the observed and expected distributions.
- **Alternative Hypothesis ($H_A$)**: The observed frequencies do not match the expected frequencies.

### Example: M&M Color Distribution

Suppose we want to test if the color distribution of M&Ms has changed since 2008.

**2008 Expected Color Distribution**:

| Color   | Percentage (%) |
|---------|----------------|
| Blue    |       24       |
| Orange  |       20       |
| Green   |       16       |
| Yellow  |       14       |
| Red     |       13       |
| Brown   |       13       |

**Observed Counts**: From a sample of 410 M&Ms, we record the number of each color.

### Calculating Expected Counts

For each color, calculate the expected count ($E_i$):

$$
E_i = N \times P_i
$$

- $N$: Total sample size (410).
- $P_i$: Expected proportion for color $i$ (e.g., 24% for blue).

**Example for Blue M&Ms**:

$$
E_{\text{blue}} = 410 \times 0.24 = 98.4
$$

### Computing the Chi-Square Statistic

The chi-square statistic is:

$$
\chi^2 = \sum_{i=1}^{k} \frac{(O_i - E_i)^2}{E_i}
$$

- $O_i$: Observed frequency for category $i$.
- $E_i$: Expected frequency for category $i$.
- $k$: Number of categories (6 colors).

**Calculate** $\chi^2$ by summing over all colors.

### Degrees of Freedom

$$
\text{Degrees of Freedom (df)} = k - 1
$$

- For 6 colors:

$$
df = 6 - 1 = 5
$$

### Decision Rule

- **Significance Level ($\alpha$)**: Commonly set at 0.05.
- **Critical Value**: Obtain from chi-square distribution table with $df = 5$.
- **Compare** the calculated $\chi^2$ with the critical value.
  - If $\chi^2_{\text{calculated}} > \chi^2_{\text{critical}}$, reject $H_0$.
  - Otherwise, fail to reject $H_0$.

### Interpretation

- **Rejecting $H_0$** suggests that the color distribution has changed since 2008.
- **Failing to Reject $H_0$** indicates no significant change in the color distribution.

---

## 2. Testing Homogeneity

### Hypotheses

- **Null Hypothesis ($H_0$)**: Different populations have the same distribution of the categorical variable.
- **Alternative Hypothesis ($H_A$)**: At least one population has a different distribution.

### Example: Titanic Survival by Ticket Class

We want to test whether survival rates are the same across ticket classes.

**Data Summary**:

|               | Survived | Died | **Total** |
|---------------|----------|------|-----------|
| First Class   |    203   | 122  |    325    |
| Second Class  |    118   | 167  |    285    |
| Third Class   |    178   | 528  |    706    |
| Crew          |    212   | 673  |    885    |
| **Total**     |    711   | 1,490 |   2,201  |

### Calculating Expected Counts

Expected count for each cell:

$$
E_{ij} = \frac{(\text{Row Total}_i \times \text{Column Total}_j)}{\text{Grand Total}}
$$

- **Example for First Class Survivors**:

$$
E_{11} = \frac{(325 \times 711)}{2,201} \approx 105.0
$$

### Computing the Chi-Square Statistic

$$
\chi^2 = \sum_{i=1}^{r} \sum_{j=1}^{c} \frac{(O_{ij} - E_{ij})^2}{E_{ij}}
$$

- $r$: Number of rows (4 ticket classes).
- $c$: Number of columns (2 survival statuses).

**Calculate** $\chi^2$ by summing over all 8 cells.

### Degrees of Freedom

$$
df = (r - 1) \times (c - 1)
$$

- For 4 ticket classes and 2 survival statuses:

$$
df = (4 - 1) \times (2 - 1) = 3 \times 1 = 3
$$

### Decision Rule

- **Significance Level ($\alpha$)**: Usually 0.05.
- **Critical Value**: From chi-square table with $df = 3$.
- **Compare** $\chi^2_{\text{calculated}}$ with $\chi^2_{\text{critical}}$.
  - If $\chi^2_{\text{calculated}} > \chi^2_{\text{critical}}$, reject $H_0$.
  - Otherwise, fail to reject $H_0$.

### Interpretation

- **Rejecting $H_0$** indicates that survival rates differ across ticket classes.
- **Failing to Reject $H_0$** suggests no significant difference in survival rates among classes.

---

## 3. Testing Independence

### Hypotheses

- **Null Hypothesis ($H_0$)**: The two categorical variables are independent.
- **Alternative Hypothesis ($H_A$)**: The variables are associated (not independent).

### Example: Gender and Voting Preference

Suppose we survey individuals to see if gender is associated with voting preference.

**Data Summary**:

|                 | Liberal | Conservative | **Total** |
|-----------------|---------|--------------|-----------|
| Male            |   40    |      60      |    100    |
| Female          |   70    |      30      |    100    |
| **Total**       |   110   |      90      |    200    |

### Calculating Expected Counts

$$
E_{ij} = \frac{(\text{Row Total}_i \times \text{Column Total}_j)}{\text{Grand Total}}
$$

- **Example for Male Liberals**:

$$
E_{11} = \frac{(100 \times 110)}{200} = 55
$$

### Computing the Chi-Square Statistic

$$
\chi^2 = \sum_{i=1}^{2} \sum_{j=1}^{2} \frac{(O_{ij} - E_{ij})^2}{E_{ij}}
$$

**Calculate** $\chi^2$ by summing over all 4 cells.

### Degrees of Freedom

$$
df = (2 - 1) \times (2 - 1) = 1 \times 1 = 1
$$

### Yates' Correction for Continuity (Optional)

For a 2×2 table, apply Yates' correction to adjust for continuity:

$$
\chi^2 = \sum \frac{(|O_{ij} - E_{ij}| - 0.5)^2}{E_{ij}}
$$

### Decision Rule

- **Significance Level ($\alpha$)**: Commonly 0.05.
- **Critical Value**: From chi-square table with $df = 1$.
- **Compare** $\chi^2_{\text{calculated}}$ with $\chi^2_{\text{critical}}$.
  - If $\chi^2_{\text{calculated}} > \chi^2_{\text{critical}}$, reject $H_0$.
  - Otherwise, fail to reject $H_0$.

### Interpretation

- **Rejecting $H_0$** suggests a significant association between gender and voting preference.
- **Failing to Reject $H_0$** indicates no significant association.

---

## Comparing Homogeneity and Independence Tests

Although both tests use the chi-square statistic and similar computations, they differ in their applications and interpretations.

### Chi-Square Test of Homogeneity

- **Objective**: To determine if multiple populations have the same distribution of a single categorical variable.
- **Data Structure**: Separate random samples from different populations.
- **Example**: Comparing M&M color distributions across different product lines (milk chocolate, peanut, caramel).

### Chi-Square Test of Independence

- **Objective**: To assess whether two categorical variables are independent within a single population.
- **Data Structure**: One random sample, observations categorized by two variables.
- **Example**: Investigating the relationship between gender and voting preference in a survey.

### Key Differences

- **Population**:
  - **Homogeneity Test**: Multiple populations.
  - **Independence Test**: Single population.
- **Research Question**:
  - **Homogeneity Test**: Are distributions the same across populations?
  - **Independence Test**: Are variables associated within the population?

---

## Assumptions and Conditions

For chi-square tests to be valid, certain conditions must be met:

1. **Random Sampling**: Data should be collected through random sampling methods.
2. **Expected Frequency**: Expected counts in each cell should be at least 5.
3. **Independence**: Observations must be independent of each other.
4. **Categorical Data**: Variables should be categorical.

---

## Practical Application Steps

1. **State the Hypotheses**: Define $H_0$ and $H_A$.
2. **Collect Data**: Organize observed frequencies into a contingency table.
3. **Calculate Expected Counts**: Use appropriate formulas based on the test.
4. **Compute the Chi-Square Statistic**: Apply the chi-square formula.
5. **Determine Degrees of Freedom**: Based on the table dimensions.
6. **Find the Critical Value or P-value**: Use chi-square distribution tables or software.
7. **Make a Decision**: Compare $\chi^2_{\text{calculated}}$ with $\chi^2_{\text{critical}}$.
8. **Interpret the Results**: Draw conclusions in the context of the research question.
