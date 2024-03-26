## Correlation

Correlation is a statistical measure that quantifies the extent and nature of the relationship between two variables. This concept is pivotal in statistical analysis to understand how variables influence each other. Pearson and Spearman correlation coefficients are the most commonly used metrics.

### Pearson Correlation Coefficient

The Pearson correlation coefficient ($r$) measures the linear relationship between two variables. Its value ranges from -1 to 1:

- **-1**: Strong negative correlation (one variable increases as the other decreases).
- **1**: Strong positive correlation (both variables increase or decrease together).
- **0**: No linear correlation (variables do not linearly influence each other).

The formula is:

$$
r = \frac{\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^n (x_i - \bar{x})^2} \sqrt{\sum_{i=1}^n (y_i - \bar{y})^2}}
$$

where $n$ is the number of observations, and $x_i$, $y_i$ are the individual data values, with $\bar{x}$, $\bar{y}$ being their respective means.

#### Example

Consider the following data:

| Hours Studied | Test Score |
|---------------|------------|
| 1             | 50         |
| 2             | 60         |
| 3             | 70         |
| 4             | 80         |
| 5             | 90         |

For this data, Pearson's $r$ can be calculated, which turns out to be 0, indicating no linear correlation.

### Spearman Rank Correlation Coefficient

Spearman's rank correlation coefficient ($\rho$) assesses the monotonic relationship between two variables, particularly when Pearson's assumptions are not met.

The formula is:

$$
\rho = 1 - \frac{6 \sum_{i=1}^n d_i^2}{n(n^2 - 1)}
$$

where $n$ is the number of observations, and $d_i$ is the difference in ranks of each pair of data points.

#### Example

Using the same dataset:

| Hours Studied | Test Score |
|---------------|------------|
| 1             | 50         |
| 2             | 60         |
| 3             | 70         |
| 4             | 80         |
| 5             | 90         |

The calculation of Spearman's $\rho$ reveals a coefficient of 1, indicating a strong positive monotonic relationship.

### Correlation of Two Random Variables

For any two random variables $X$ and $Y$ with positive variances, the correlation coefficient is:

$$
\rho(X, Y) = \frac{\text{Cov}(X, Y)}{\sqrt{\text{Var}(X)\text{Var}(Y)}}
$$

It ranges from -1 to 1, where 0 implies minimal linearity, and values near +1 or -1 indicate strong positive or negative linear relationships, respectively.
