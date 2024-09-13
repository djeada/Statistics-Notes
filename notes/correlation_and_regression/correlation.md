# Correlation

**Correlation** is a statistical measure that quantifies the strength and direction of the linear relationship between two variables. It is a fundamental concept in statistics, enabling researchers and analysts to understand how one variable may predict or relate to another. The most commonly used correlation coefficients are the **Pearson correlation coefficient** and the **Spearman rank correlation coefficient**.

## Understanding Correlation

- A **positive correlation** occurs when, as one variable increases, the other tends to rise as well.
- In contrast, a **negative correlation** happens when an increase in one variable results in the other decreasing.
- Lastly, a **zero correlation** indicates that there is no linear relationship between the variables.

**Important Note**: Correlation does not imply causation. A high correlation between two variables does not mean that one variable causes changes in the other.

## Pearson Correlation Coefficient ($r$)

The **Pearson correlation coefficient** measures the strength and direction of the linear relationship between two continuous variables. It is sensitive to outliers and assumes that the relationship is linear and that both variables are normally distributed.

### Definition

The Pearson correlation coefficient $r$ is defined as:

$$
r = \frac{\text{Cov}(X, Y)}{\sigma_X \sigma_Y}
$$

Where:

- $\text{Cov}(X, Y)$ is the covariance between variables $X$ and $Y$.
- $\sigma_X$ and $\sigma_Y$ are the standard deviations of $X$ and $Y$, respectively.

**Alternative Formula**:

$$
r = \frac{\sum_{i=1}^{n} (X_i - \bar{X})(Y_i - \bar{Y})}{\sqrt{\sum_{i=1}^{n} (X_i - \bar{X})^2} \sqrt{\sum_{i=1}^{n} (Y_i - \bar{Y})^2}}
$$

Where:

- $n$ is the number of observations.
- $X_i$ and $Y_i$ are the $i $-th observations of $X$ and $Y$.
- $\bar{X}$ and $\bar{Y}$ are the sample means of $X$ and $Y$.

### Interpretation

- $r = 1 $: Perfect positive linear correlation.
- $r = -1 $: Perfect negative linear correlation.
- $r = 0 $: No linear correlation.

General Guidelines:

| **Correlation Strength**            | **Range (r)**    |
|-------------------------------------|------------------|
| Strong Positive Correlation         | 0.7 ≤ r ≤ 1.0    |
| Moderate Positive Correlation       | 0.3 ≤ r < 0.7    |
| Weak Positive Correlation           | 0 < r < 0.3      |
| No Correlation                      | r = 0            |
| Weak Negative Correlation           | -0.3 < r < 0     |
| Moderate Negative Correlation       | -0.7 < r ≤ -0.3  |
| Strong Negative Correlation         | -1.0 ≤ r ≤ -0.7  |

### Example: Calculating Pearson's $r$

#### Dataset

Consider the following data on the number of hours studied ($X$) and test scores ($Y$):

| Observation ($i $) | Hours Studied ($X_i$) | Test Score ($Y_i$) |
|-----------------------|---------------------------|-------------------------|
| 1                     | 1                         | 50                      |
| 2                     | 2                         | 60                      |
| 3                     | 3                         | 70                      |
| 4                     | 4                         | 80                      |
| 5                     | 5                         | 90                      |

#### Step 1: Calculate the Means

$$
\bar{X} = \frac{1}{5}(1 + 2 + 3 + 4 + 5) = \frac{15}{5} = 3
$$

$$
\bar{Y} = \frac{1}{5}(50 + 60 + 70 + 80 + 90) = \frac{350}{5} = 70
$$

#### Step 2: Calculate Deviations and Products

Compute $(X_i - \bar{X})$, $(Y_i - \bar{Y})$, and their products:

| $i $ | $X_i$ | $Y_i$ | $X_i - \bar{X}$ | $Y_i - \bar{Y}$ | $(X_i - \bar{X})(Y_i - \bar{Y})$ | $(X_i - \bar{X})^2 $ | $(Y_i - \bar{Y})^2 $ |
|---------|-----------|-----------|----------------------|----------------------|---------------------------------------|-------------------------|-------------------------|
| 1       | 1         | 50        | -2                   | -20                  | 40                                    | 4                       | 400                     |
| 2       | 2         | 60        | -1                   | -10                  | 10                                    | 1                       | 100                     |
| 3       | 3         | 70        | 0                    | 0                    | 0                                     | 0                       | 0                       |
| 4       | 4         | 80        | 1                    | 10                   | 10                                    | 1                       | 100                     |
| 5       | 5         | 90        | 2                    | 20                   | 40                                    | 4                       | 400                     |
| **Sum** |           |           |                      |                      | **100**                               | **10**                  | **1000**                |

#### Step 3: Compute the Pearson Correlation Coefficient

$$
r = \frac{\sum_{i=1}^{5} (X_i - \bar{X})(Y_i - \bar{Y})}{\sqrt{\sum_{i=1}^{5} (X_i - \bar{X})^2} \sqrt{\sum_{i=1}^{5} (Y_i - \bar{Y})^2}} = \frac{100}{\sqrt{10} \times \sqrt{1000}}
$$

Compute the denominators:

$$
\sqrt{10} \approx 3.1623, \quad \sqrt{1000} \approx 31.6228
$$

Compute $r$:

$$
r = \frac{100}{3.1623 \times 31.6228} = \frac{100}{100} = 1
$$

#### Visualization

![output(12)](https://github.com/user-attachments/assets/36a1926f-d285-4a2f-b025-6b2dfa2f1a5e)

**Pearson's $r = 1 $** indicates a perfect positive linear relationship between hours studied and test scores. As the number of hours studied increases, the test score increases proportionally.

### Note on Initial Error Correction

In the initial content, it was incorrectly stated that Pearson's $r$ for this data is zero, indicating no linear correlation. This is inaccurate because the data shows a clear linear relationship. The correct calculation, as shown above, yields $r = 1 $, confirming a strong positive linear correlation.

## Spearman Rank Correlation Coefficient ($\rho$)

The **Spearman rank correlation coefficient** measures the strength and direction of the monotonic relationship between two ranked variables. It is a non-parametric measure, meaning it does not assume a specific distribution for the variables and is less sensitive to outliers.

### Definition

The Spearman correlation coefficient $\rho$ is defined as:

$$
\rho = 1 - \frac{6 \sum_{i=1}^{n} d_i^2}{n(n^2 - 1)}
$$

Where:

- $d_i = R(X_i) - R(Y_i)$ is the difference between the ranks of $X_i$ and $Y_i$.
- $R(X_i)$ and $R(Y_i)$ are the ranks of $X_i$ and $Y_i$, respectively.
- $n $ is the number of observations.

### Calculation Steps

1. **Assign Ranks** to the data points in $X$ and $Y$ separately.
2. **Compute the Differences of Ranks** $d_i$.
3. **Square the Differences** $d_i^2 $.
4. **Compute $\rho$** using the formula.

### Example: Calculating Spearman's $\rho$

Using the same dataset:

| Observation ($i $) | Hours Studied ($X_i$) | Test Score ($Y_i$) |
|-----------------------|---------------------------|-------------------------|
| 1                     | 1                         | 50                      |
| 2                     | 2                         | 60                      |
| 3                     | 3                         | 70                      |
| 4                     | 4                         | 80                      |
| 5                     | 5                         | 90                      |

#### Step 1: Assign Ranks

Since the data is already ordered, the ranks correspond to the order of observations.

| $i $ | $X_i$ | Rank $R(X_i)$ | $Y_i$ | Rank $R(Y_i)$ |
|---------|-----------|--------------------|-----------|--------------------|
| 1       | 1         | 1                  | 50        | 1                  |
| 2       | 2         | 2                  | 60        | 2                  |
| 3       | 3         | 3                  | 70        | 3                  |
| 4       | 4         | 4                  | 80        | 4                  |
| 5       | 5         | 5                  | 90        | 5                  |

#### Step 2: Compute Differences of Ranks

Calculate $d_i = R(X_i) - R(Y_i)$:

| $i $ | Rank $R(X_i)$ | Rank $R(Y_i)$ | $d_i$ | $d_i^2 $ |
|---------|--------------------|--------------------|-----------|-------------|
| 1       | 1                  | 1                  | 0         | 0           |
| 2       | 2                  | 2                  | 0         | 0           |
| 3       | 3                  | 3                  | 0         | 0           |
| 4       | 4                  | 4                  | 0         | 0           |
| 5       | 5                  | 5                  | 0         | 0           |
| **Sum** |                    |                    |           | **0**       |

#### Step 3: Compute Spearman's $\rho$

$$
\rho = 1 - \frac{6 \times 0}{5(5^2 - 1)} = 1 - 0 = 1
$$

#### Interpretation

**Spearman's $\rho = 1 $** indicates a perfect positive monotonic relationship between hours studied and test scores.

### When to Use Spearman's $\rho$

- When data is ordinal.
- When the relationship between variables is monotonic but not necessarily linear.
- When there are outliers that might affect Pearson's $r$.
- When the variables are not normally distributed.

## Comparison of Pearson's $r$ and Spearman's $\rho$

- **Pearson's $r$** measures the strength of a linear relationship.
- **Spearman's $\rho$** measures the strength of a monotonic relationship.
- Both coefficients range from -1 to 1.
- Spearman's $\rho$ is less sensitive to outliers and does not require the assumption of normality.

## Correlation of Two Random Variables

For two random variables $X$ and $Y$ with positive variances, the **population correlation coefficient** $\rho_{XY}$ is defined as:

$$
\rho_{XY} = \frac{\text{Cov}(X, Y)}{\sigma_X \sigma_Y}
$$

Where:

- $\text{Cov}(X, Y)$ is the covariance between $X$ and $Y$.
- $\sigma_X$ and $\sigma_Y$ are the standard deviations of $X$ and $Y$.

### Properties

| **Property**       | **Description**                                                                 |
|--------------------|---------------------------------------------------------------------------------|
| **Range**          | $-1 \leq \rho_{XY} \leq 1$                                                      |
| **Symmetry**       | $\rho_{XY} = \rho_{YX}$                                                         |
| **Dimensionless**  | The correlation coefficient is unitless.                                        |
| **Linearity**      | If $\rho_{XY} = \pm 1 $, $Y$ is a perfect linear function of $X$.               |
| **Independence**   | If $X$ and $Y$ are independent, $\rho_{XY} = 0$. However, $\rho_{XY} = 0$ does not imply independence unless the variables are jointly normally distributed. |

### Interpretation

- **$\rho_{XY} > 0 $**: Positive linear relationship.
- **$\rho_{XY} < 0 $**: Negative linear relationship.
- **$\rho_{XY} = 0 $**: No linear relationship.

### Example with Random Variables

Suppose $X$ and $Y$ are random variables with the following properties:

- $\mu_X = \mathbb{E}[X] = 5$
- $\mu_Y = \mathbb{E}[Y] = 10$
- $\sigma_X = \sqrt{\text{Var}(X)} = 2$
- $\sigma_Y = \sqrt{\text{Var}(Y)} = 4$
- $\text{Cov}(X, Y) = 6$

Compute the correlation coefficient:

$$
\rho_{XY} = \frac{\text{Cov}(X, Y)}{\sigma_X \sigma_Y} = \frac{6}{2 \times 4} = \frac{6}{8} = 0.75
$$

Interpretation:

- A correlation coefficient of $0.75$ indicates a strong positive linear relationship between $X$ and $Y$.

## Important Considerations

### Correlation vs. Causation

- **Correlation does not imply causation**. A high correlation between two variables does not mean that one variable causes changes in the other.

### Outliers

- **Pearson's $r$** is sensitive to outliers, which can distort the correlation coefficient.
- **Spearman's $\rho$** is more robust to outliers due to ranking.

### Non-linear Relationships

- Variables can have a strong non-linear relationship but a low Pearson correlation coefficient.
- In such cases, Spearman's $\rho$ may detect the monotonic relationship.

### Assumptions of Pearson's $r$

1. **Linearity** means that the relationship between $X$ and $Y$ is straight and follows a linear pattern.
2. **Normality** refers to the condition where both $X$ and $Y$ are normally distributed.
3. Lastly, **homoscedasticity** implies that the variance of $Y$ remains consistent across all values of $X$.

If these assumptions are violated, Pearson's $r$ may not be an appropriate measure of correlation.
