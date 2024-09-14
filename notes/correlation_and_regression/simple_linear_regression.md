# Simple Linear Regression

Simple linear regression is a fundamental statistical method used to model the relationship between a single dependent variable and one independent variable. It aims to find the best-fitting straight line through the data points, which can be used to predict the dependent variable based on the independent variable.

## The Simple Linear Regression Model

The mathematical representation of the simple linear regression model is:

$$
y_i = \beta_0 + \beta_1 x_i + \varepsilon_i, \quad i = 1, 2, \dots, n
$$

Where:

- $y_i$ is the $i $-th observation of the dependent variable.
- $x_i$ is the $i $-th observation of the independent variable.
- $\beta_0$ is the intercept (the expected value of $y$ when $x = 0$).
- $\beta_1$ is the slope (the average change in $y$ for a one-unit change in $x$).
- $\varepsilon_i$ is the error term, assumed to be independently and identically distributed with mean zero and constant variance $\sigma^2 $.

### Assumptions of the Model

For the simple linear regression model to be valid, several key assumptions must be met:

1. **Linearity** indicates that the relationship between $x$ and $y$ is linear.
2. **Independence** means the residuals (errors) $\varepsilon_i$ are independent of one another.
3. **Homoscedasticity** suggests that the residuals have a constant variance ($\sigma^2$) across all values of $x$.
4. **Normality** assumes that the residuals follow a normal distribution.
5. Finally, **no measurement error in $x** ensures that the independent variable $x$ is measured without error.

## Estimation of Coefficients Using the Least Squares Method

The goal is to find estimates $\hat{\beta}_0$ and $\hat{\beta}_1$ that minimize the sum of squared residuals (differences between observed and predicted values):

$$
\text{SSE} = \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 = \sum_{i=1}^{n} (y_i - \hat{\beta}_0 - \hat{\beta}_1 x_i)^2
$$

### Calculating the Slope ($\hat{\beta}_1$) and Intercept ($\hat{\beta}_0$)

The least squares estimates are calculated using the following formulas:

#### Slope ($\hat{\beta}_1$):

$$
\hat{\beta}_1 = \frac{\sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^{n} (x_i - \bar{x})^2} = \frac{\text{Cov}(x, y)}{\text{Var}(x)}
$$

#### Intercept ($\hat{\beta}_0$):

$$
\hat{\beta}_0 = \bar{y} - \hat{\beta}_1 \bar{x}
$$

Where:

- $\bar{x} = \dfrac{1}{n} \sum_{i=1}^{n} x_i$ is the mean of the independent variable.
- $\bar{y} = \dfrac{1}{n} \sum_{i=1}^{n} y_i$ is the mean of the dependent variable.

## Interpretation of the Coefficients

- The **intercept ($\hat{\beta}_0$)** represents the expected value of $y$ when $x = 0$, marking the point where the regression line intersects the $y$-axis.
- The **slope ($\hat{\beta}_1$)** indicates the average change in $y$ for each one-unit increase in $x$.

## Assessing the Fit of the Model

### Total Sum of Squares (SST)

Measures the total variability in the dependent variable:

$$
\text{SST} = \sum_{i=1}^{n} (y_i - \bar{y})^2
$$

### Regression Sum of Squares (SSR)

Measures the variability explained by the regression:

$$
\text{SSR} = \sum_{i=1}^{n} (\hat{y}_i - \bar{y})^2
$$

### Sum of Squared Errors (SSE)

Measures the unexplained variability:

$$
\text{SSE} = \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
$$

### Coefficient of Determination ($R^2 $)

Indicates the proportion of variance in $y$ explained by $x$:

$$
R^2 = \frac{\text{SSR}}{\text{SST}} = 1 - \frac{\text{SSE}}{\text{SST}}
$$

An $R^2 $ value close to 1 suggests a strong linear relationship.

## Hypothesis Testing

### Testing the Significance of the Slope

- **Null Hypothesis ($H_0$)**: $\beta_1 = 0$ (no linear relationship)
- **Alternative Hypothesis ($H_a $)**: $\beta_1 \neq 0$

**Test Statistic**:

$$
t = \frac{\hat{\beta}_1}{\text{SE}(\hat{\beta}_1)}
$$

Where:

$$
\text{SE}(\hat{\beta}_1) = \frac{s}{\sqrt{\sum_{i=1}^{n} (x_i - \bar{x})^2}}
$$

And:

$$
s = \sqrt{\frac{\text{SSE}}{n - 2}}
$$

The test statistic follows a $t $-distribution with $n - 2 $ degrees of freedom.

## Example

Suppose we have the following data on the number of hours studied ($x$) and the test scores ($y$):

| Hours Studied ($x$) | Test Score ($y$) |
|-------------------------|-----------------------|
| 2                       | 50                    |
| 4                       | 60                    |
| 6                       | 70                    |
| 8                       | 80                    |

### Step-by-Step Calculation

#### 1. Calculate the Means

$$
\bar{x} = \frac{2 + 4 + 6 + 8}{4} = 5
$$

$$
\bar{y} = \frac{50 + 60 + 70 + 80}{4} = 65
$$

#### 2. Compute the Sum of Squares and Cross-Products

Create a table to organize calculations:

| $x_i$ | $y_i$ | $x_i - \bar{x} $ | $y_i - \bar{y} $ | $(x_i - \bar{x})(y_i - \bar{y})$ | $(x_i - \bar{x})^2 $ |
|-----------|-----------|---------------------|---------------------|--------------------------------------|-------------------------|
| 2         | 50        | -3                  | -15                 | 45                                   | 9                       |
| 4         | 60        | -1                  | -5                  | 5                                    | 1                       |
| 6         | 70        | 1                   | 5                   | 5                                    | 1                       |
| 8         | 80        | 3                   | 15                  | 45                                   | 9                       |
| **Total** |           |                     |                     | **100**                               | **20**                  |

**Sum of Cross-Products**:

$$
\sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y}) = 100
$$

**Sum of Squares of $x$**:

$$
\sum_{i=1}^{n} (x_i - \bar{x})^2 = 20
$$

#### 3. Calculate the Slope ($\hat{\beta}_1$)

$$
\hat{\beta}_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} = \frac{100}{20} = 5
$$

#### 4. Calculate the Intercept ($\hat{\beta}_0$)

$$
\hat{\beta}_0 = \bar{y} - \hat{\beta}_1 \bar{x} = 65 - (5)(5) = 40
$$

#### 5. Formulate the Regression Equation

$$
\hat{y} = 40 + 5x
$$

#### 6. Predict the Test Scores and Calculate Residuals

| $x_i$ | $y_i$ | $\hat{y}_i = 40 + 5x_i$ | Residuals ($y_i - \hat{y}_i$) |
|-----------|-----------|------------------------------|-----------------------------------|
| 2         | 50        | 50                           | 0                                 |
| 4         | 60        | 60                           | 0                                 |
| 6         | 70        | 70                           | 0                                 |
| 8         | 80        | 80                           | 0                                 |

#### 7. Calculate the Sum of Squares

**Total Sum of Squares (SST)**:

$$
\text{SST} = \sum (y_i - \bar{y})^2 = (-15)^2 + (-5)^2 + 5^2 + 15^2 = 500
$$

**Sum of Squared Errors (SSE)**:

$$
\text{SSE} = \sum (y_i - \hat{y}_i)^2 = 0
$$

**Regression Sum of Squares (SSR)**:

$$
\text{SSR} = \text{SST} - \text{SSE} = 500 - 0 = 500
$$

#### 8. Compute the Coefficient of Determination ($R^2 $)

$$
R^2 = \frac{\text{SSR}}{\text{SST}} = \frac{500}{500} = 1
$$

An $R^2 $ value of 1 indicates that the model perfectly explains the variability in the test scores.

![output(18)](https://github.com/user-attachments/assets/033767fc-d920-4f36-9827-5e8af81e4760)

#### 9. Calculate the Standard Error of the Estimate ($s $)

$$
s = \sqrt{\frac{\text{SSE}}{n - 2}} = \sqrt{\frac{0}{2}} = 0
$$

Since $s = 0$, the standard errors of the coefficients are zero, which is a result of the perfect fit.

#### 10. Hypothesis Testing (Optional)

In this case, the test statistic for $\hat{\beta}_1$ is undefined due to division by zero in the standard error. However, in practice, with more realistic data where $s > 0$, you would perform a $t $-test to assess the significance of the slope.
