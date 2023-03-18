# Simple Linear Regression

Simple linear regression is a statistical method used to examine the relationship between one dependent variable (response variable) and one independent variable (predictor variable). It helps to predict the value of the dependent variable based on the value of the independent variable.

## Equation of a Straight Line

The relationship between the dependent variable (y) and the independent variable (x) is represented by a straight line with the equation:

$$
y = \beta_0 + \beta_1x + \epsilon
$$

Where:
- $y$ is the dependent variable
- $x$ is the independent variable
- $\beta_0$ is the y-intercept (the value of y when x = 0)
- $\beta_1$ is the slope of the line (change in y per unit change in x)
- $\epsilon$ is the random error term

## Least Squares Method

The least squares method is used to find the best-fitting line by minimizing the sum of squared residuals (differences between the actual and predicted values). The coefficients $\beta_0$ and $\beta_1$ can be calculated as:

$$
\beta_1 = \frac{\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^{n}(x_i - \bar{x})^2}
$$

$$
\beta_0 = \bar{y} - \beta_1\bar{x}
$$

Where:
- $n$ is the number of observations
- $x_i$ and $y_i$ are individual data points
- $\bar{x}$ and $\bar{y}$ are the means of the x and y variables

## Example

Suppose we have the following data on the number of hours studied (x) and the test scores (y):

| Hours Studied (x) | Test Score (y) |
|-------------------|----------------|
| 2                 | 50             |
| 4                 | 60             |
| 6                 | 70             |
| 8                 | 80             |

We can calculate the slope and intercept using the formulas above:

1. Calculate the means: $\bar{x} = 5$, $\bar{y} = 65$
2. Calculate $\beta_1$: $\beta_1 = \frac{(2-5)(50-65) + (4-5)(60-65) + (6-5)(70-65) + (8-5)(80-65)}{(2-5)^2 + (4-5)^2 + (6-5)^2 + (8-5)^2} = 5$
3. Calculate $\beta_0$: $\beta_0 = 65 - 5(5) = 40$

So the best-fitting line is:

$$
y = 40 + 5x
$$
