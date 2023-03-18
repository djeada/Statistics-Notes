# Correlation

Correlation is a statistical measure that describes the strength and direction of the relationship between two variables. The most common measure of correlation is the Pearson correlation coefficient, also known as Pearson's r.

## Pearson Correlation Coefficient

The Pearson correlation coefficient measures the linear relationship between two variables. It ranges from -1 to 1, where -1 indicates a strong negative correlation, 1 indicates a strong positive correlation, and 0 indicates no correlation.

Formula for Pearson correlation coefficient:

$$
r = \frac{\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^n (x_i - \bar{x})^2} \sqrt{\sum_{i=1}^n (y_i - \bar{y})^2}}
$$

where $n$ is the number of data points, $x_i$ and $y_i$ are the individual data points, and $\bar{x}$ and $\bar{y}$ are the means of $x$ and $y$, respectively.

### Example

Suppose we have the following data on the number of hours studied and test scores for five students:

| Hours Studied | Test Score |
|---------------|------------|
| 1             | 50         |
| 2             | 60         |
| 3             | 70         |
| 4             | 80         |
| 5             | 90         |

Calculate the Pearson correlation coefficient between hours studied and test scores.

## Spearman Rank Correlation Coefficient

The Spearman rank correlation coefficient, also known as Spearman's rho, measures the monotonic relationship between two variables. It is based on the ranks of the data rather than the actual values and is less sensitive to outliers than Pearson's r.

Formula for Spearman rank correlation coefficient:

$$
\rho = 1 - \frac{6 \sum_{i=1}^n d_i^2}{n(n^2 - 1)}
$$

where $n$ is the number of data points and $d_i$ is the difference in ranks for each pair of data points.

### Example

Using the same data as in the previous example, calculate the Spearman rank correlation coefficient between hours studied and test scores.
