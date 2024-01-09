## Correlation

Correlation is a statistical technique that can show whether, and how strongly, pairs of variables are related. This statistical measure helps to comprehend the strength and direction of the relationship between two variables. The most common measure of correlation is the Pearson correlation coefficient, also known as Pearson's r, which provides a linear correlation coefficient. There's also the Spearman correlation coefficient which is used when the assumptions of Pearson's correlation are violated.


## Pearson Correlation Coefficient

The Pearson correlation coefficient, denoted as $r$, quantifies the linear relationship between two variables. It ranges from -1 to 1, where:

- -1 indicates a strong negative correlation (i.e., as one variable increases, the other decreases)
- 1 indicates a strong positive correlation (i.e., both variables increase or decrease together)
- 0 indicates no correlation (i.e., the variables do not influence each other)

The formula for the Pearson correlation coefficient is given by:

$$
r = \frac{\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^n (x_i - \bar{x})^2} \sqrt{\sum_{i=1}^n (y_i - \bar{y})^2}}
$$

In this formula, $n$ denotes the number of data points, $x_i$ and $y_i$ are individual data points, and $\bar{x}$ and $\bar{y}$ are the means of $x$ and $y$, respectively.

## Spearman Rank Correlation Coefficient

In contrast to Pearson's r, the Spearman rank correlation coefficient (also known as Spearman's rho, denoted as $\rho$) measures the monotonic relationship between two variables. This method is based on the ranks of the data rather than the actual numerical values, thus making it less sensitive to outliers and non-linear relationships.

The formula for the Spearman rank correlation coefficient is given by:

$$
\rho = 1 - \frac{6 \sum_{i=1}^n d_i^2}{n(n^2 - 1)}
$$

where $n$ is the number of data points and $d_i$ is the difference in ranks for each pair of data points.

### Example

Given the following data:

| Hours Studied | Test Score |
|---------------|------------|
| 1             | 50         |
| 2             | 60         |
| 3             | 70         |
| 4             | 80         |
| 5             | 90         |

The Pearson correlation coefficient and Spearman rank correlation coefficient can be calculated as follows:

#### Pearson Correlation Coefficient

For Pearson's correlation, the means $\bar{x}$ and $\bar{y}$ are 3 and 70, respectively. We can then compute each component of the formula and sum them:

$$
\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y}) = 20 + 10 + 0 - 10 - 20 = 0
$$

$$
\sqrt{\sum_{i=1}^n (x_i - \bar{x})^2} = \sqrt{4 + 1 + 0 + 1 + 4} = \sqrt{10}
$$

$$
\sqrt{\sum_{i=1}^n (y_i - \bar{y})^2} = \sqrt{400 + 100 + 0 + 100 + 400} = \sqrt{1000}
$$

Hence, the Pearson correlation coefficient is:

$$
r = \frac{0}{\sqrt{10} \cdot \sqrt{1000}} = 0
$$

This indicates no linear correlation between hours studied and test scores, according to Pearson's correlation.

#### Spearman Rank Correlation Coefficient

For Spearman's rho, we rank the data (lowest to highest) and use these ranks in our formula. Given our data, the rank is the same as the actual value. The difference in ranks $d_i$ for all data points is 0.

Thus, the Spearman rank correlation coefficient is:

$$
\rho = 1 - \frac{6 \sum_{i=1}^n d_i^2}{n(n^2 - 1)} = 1 - \frac{6 \cdot 0}{5 \cdot (5^2 - 1)} = 1
$$

This indicates a strong positive monotonic relationship between hours studied and test scores, according to Spearman's rho.

These two results tell us that while there is no *linear* relationship (as indicated by Pearson's r), there is a *monotonic* relationship (as indicated by Spearman's rho). This difference can occur when the relationship between variables is not linear, but consistently increases or decreases.

## Correlation of 2 Random Variables

As long as \( \text{Var}(X) \) and \( \text{Var}(Y) \) are both positive, the correlation of X and Y is denoted as

\[ \rho(X, Y) = \frac{\text{Cov}(X, Y)}{\sqrt{\text{Var}(X)\text{Var}(Y)}} \]

It can be shown that \( -1 \leq \rho(X, Y) \leq 1 \)

The correlation coefficient is a measure of the degree of linearity between X and Y

\( \rho(X, Y) = 0 \) means very little linearity

\( \rho(X, Y) \) near \( +1 \) means X and Y increase and decrease together

\( \rho(X, Y) \) near \( -1 \) means X and Y increase and decrease inversely

