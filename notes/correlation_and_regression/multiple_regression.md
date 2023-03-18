# Multiple Linear Regression

Multiple linear regression is an extension of simple linear regression used to examine the relationship between one dependent variable (response variable) and multiple independent variables (predictor variables). It helps to predict the value of the dependent variable based on the values of the independent variables.

## Equation of a Hyperplane

The relationship between the dependent variable (y) and the independent variables (x1, x2, ..., xn) is represented by a hyperplane with the equation:

$$
y = \beta_0 + \beta_1x_1 + \beta_2x_2 + ... + \beta_nx_n + \epsilon
$$

Where:
- $y$ is the dependent variable
- $x_1, x_2, ..., x_n$ are the independent variables
- $\beta_0$ is the intercept (the value of y when all x's are 0)
- $\beta_1, \beta_2, ..., \beta_n$ are the coefficients (the change in y per unit change in the corresponding x)
- $\epsilon$ is the random error term

## Estimation of Coefficients

Similar to simple linear regression, the coefficients are estimated using the least squares method, which minimizes the sum of squared residuals. The coefficients can be calculated using matrix algebra:

$$
\hat{\beta} = (X^TX)^{-1}X^Ty
$$

Where:
- $\hat{\beta}$ is the vector of estimated coefficients
- $X$ is the matrix of independent variables (with a column of 1's for the intercept)
- $y$ is the vector of dependent variable values

## Example

Suppose we have the following data on the number of hours studied (x1), the number of practice exams taken (x2), and the test scores (y):

| Hours Studied (x1) | Practice Exams (x2) | Test Score (y) |
|--------------------|---------------------|----------------|
| 2                  | 1                   | 50             |
| 4                  | 2                   | 60             |
| 6                  | 3                   | 70             |
| 8                  | 4                   | 80             |

Using statistical software or matrix algebra, we can calculate the coefficients for the multiple linear regression model:

$$
y = \beta_0 + \beta_1x_1 + \beta_2x_2
$$

After the calculations, we obtain the coefficients:

$$
\hat{\beta_0} = 30, \; \hat{\beta_1} = 5, \; \hat{\beta_2} = 2
$$

So the best-fitting hyperplane is:

$$
y = 30 + 5x_1 + 2x_2
$$
