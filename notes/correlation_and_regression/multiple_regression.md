# Multiple Linear Regression

Multiple linear regression is a statistical technique used to model the relationship between a single dependent variable and two or more independent variables. It extends the concept of simple linear regression by incorporating multiple predictors to explain the variability in the dependent variable. This method is widely used in fields such as economics, engineering, social sciences, and natural sciences to predict outcomes and understand the impact of various factors.

## The Multiple Linear Regression Model

The general form of the multiple linear regression model is:

$$
y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_p x_p + \varepsilon
$$

Where:

- $y$ is the dependent variable (response variable).
- $x_1, x_2, \dots, x_p $ are the independent variables (predictor variables).
- $\beta_0 $ is the intercept term (the expected value of $y$ when all $x_j = 0 $).
- $\beta_1, \beta_2, \dots, \beta_p $ are the coefficients representing the change in $y$ for a one-unit change in $x_j $, holding all other variables constant.
- $\varepsilon $ is the random error term, accounting for the variability in $y$ not explained by the linear relationship.

### Matrix Representation

In matrix notation, the model can be expressed as:

$$
\mathbf{y} = \mathbf{X} \boldsymbol{\beta} + \boldsymbol{\varepsilon}
$$

Where:

- $\mathbf{y}$ is an $n \times 1$ vector of observations of the dependent variable.
- $\mathbf{X}$ is an $n \times (p+1)$ matrix of independent variables, including a column of ones for the intercept.
- $\boldsymbol{\beta}$ is a $(p+1) \times 1$ vector of coefficients.
- $\boldsymbol{\varepsilon}$ is an $n \times 1$ vector of error terms.

## Assumptions of the Model

For the multiple linear regression model to provide valid results, several key assumptions must be met:

1. **Linearity** means that the relationship between the dependent variable and each independent variable is linear.
2. **Independence** assumes that the observations are independent of one another.
3. **Homoscedasticity** ensures that the variance of the error terms remains constant across all levels of the independent variables.
4. **Normality** requires that the error terms are normally distributed with a mean of zero.
5. Finally, **no multicollinearity** ensures that the independent variables are not perfectly correlated with each other.

## Estimation of Coefficients

### Least Squares Method

The coefficients $\boldsymbol{\beta}$ are estimated using the Ordinary Least Squares (OLS) method, which minimizes the sum of squared residuals (the differences between observed and predicted values of $y$).

The objective is to find $\hat{\boldsymbol{\beta}}$ such that:

$$
\hat{\boldsymbol{\beta}} = \underset{\boldsymbol{\beta}}{\text{argmin}} \, (\mathbf{y} - \mathbf{X} \boldsymbol{\beta})^\top (\mathbf{y} - \mathbf{X} \boldsymbol{\beta})
$$

### Solution Using Matrix Algebra

By taking the derivative of the sum of squared residuals with respect to $\boldsymbol{\beta}$ and setting it to zero, we obtain the normal equations:

$$
\mathbf{X}^\top \mathbf{X} \hat{\boldsymbol{\beta}} = \mathbf{X}^\top \mathbf{y}
$$

Solving for $\hat{\boldsymbol{\beta}}$:

$$
\hat{\boldsymbol{\beta}} = (\mathbf{X}^\top \mathbf{X})^{-1} \mathbf{X}^\top \mathbf{y}
$$

**Conditions for Invertibility**:

- The matrix $\mathbf{X}^\top \mathbf{X}$ must be invertible.
- This requires that the columns of $\mathbf{X}$ are linearly independent (no perfect multicollinearity).

## Interpretation of Coefficients

- The **intercept ($\hat{\beta}_0$)** represents the expected value of $y$ when all independent variables are zero.
- The **slope coefficients ($\hat{\beta}_j$)** indicate the expected change in $y$ for a one-unit increase in $x_j$, while holding all other variables constant.

## Assessing Model Fit

### Coefficient of Determination ($R^2$)

$$
R^2 = 1 - \frac{\text{SSR}}{\text{SST}}
$$

- **SSR (Sum of Squared Residuals)** measures the unexplained variation in the model, representing the error.
- **SST (Total Sum of Squares)** captures the total variation in $y$, showing the overall variability in the dependent variable.

An $R^2$ value close to 1 indicates a good fit.

### Adjusted $R^2$

Adjusts $R^2$ for the number of predictors in the model:

$$
\text{Adjusted } R^2 = 1 - \left( \frac{\text{SSR} / (n - p - 1)}{\text{SST} / (n - 1)} \right)
$$

## Hypothesis Testing

### Testing Individual Coefficients

- **Null Hypothesis ($H_0 $)**: $\beta_j = 0 $
- **Alternative Hypothesis ($H_a $)**: $\beta_j \neq 0 $
- **Test Statistic**:

$$
t_j = \frac{\hat{\beta}_j}{\text{SE}(\hat{\beta}_j)}
$$

- **Degrees of Freedom**: $n - p - 1$

### Testing Overall Model Significance

- **Null Hypothesis ($H_0 $)**: All $\beta_j = 0 $
- **Alternative Hypothesis ($H_a $)**: At least one $\beta_j \neq 0 $
- **F-Statistic**:

$$
F = \frac{(\text{SST} - \text{SSR}) / p}{\text{SSR} / (n - p - 1)}
$$

- **Degrees of Freedom**: $p $ and $n - p - 1$

## Diagnosing Multicollinearity

### Variance Inflation Factor (VIF)

Measures how much the variance of an estimated coefficient increases due to multicollinearity:

$$
\text{VIF}_j = \frac{1}{1 - R_j^2}
$$

- $R_j^2$ is the $R^2$ from regressing $x_j $ on the other predictors.
- A VIF value greater than 5 or 10 indicates high multicollinearity.

### Remedies

- **Remove variables** by excluding one of the correlated variables from the model.
- **Combine variables** to create composite or aggregated variables that reduce redundancy.
- **Regularization** techniques, such as ridge regression, can be applied to handle multicollinearity effectively.

## Assumption Diagnostics

### Residual Analysis

- **Plot residuals vs. fitted values** to check for any patterns that may indicate non-linearity or heteroscedasticity.
- **Normal Q-Q plot** to assess whether the residuals follow a normal distribution.
  
### Durbin-Watson Test

Checks for autocorrelation in residuals:

$$
D = \frac{\sum_{i=2}^n (e_i - e_{i-1})^2}{\sum_{i=1}^n e_i^2}
$$

Values close to 2 indicate no autocorrelation.

## Extensions

### Interaction Terms

Include products of independent variables to model interactions:

$$
y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \beta_3 (x_1 x_2) + \varepsilon
$$

### Polynomial Regression

Model non-linear relationships by including polynomial terms:

$$
y = \beta_0 + \beta_1 x + \beta_2 x^2 + \dots + \beta_k x^k + \varepsilon
$$

### Regularization Techniques

**Ridge Regression**: Adds penalty for large coefficients.

$$
\hat{\boldsymbol{\beta}}_{\text{ridge}} = (\mathbf{X}^\top \mathbf{X} + \lambda \mathbf{I})^{-1} \mathbf{X}^\top \mathbf{y}
$$

**Lasso Regression**: Encourages sparsity in coefficients.

$$
\text{Minimize } \sum_{i=1}^n (y_i - \hat{y}_i)^2 + \lambda \sum_{j=1}^p |\beta_j|
$$

## Example: Multicollinearity Between Variables

Suppose we have the following data on the number of hours studied ($x_1$), the number of practice exams taken ($x_2$), and the test scores ($y$):

| Hours Studied ($x_1$) | Practice Exams ($x_2$) | Test Score ($y$) |
|---------------------------|----------------------------|-----------------------|
| 2                         | 1                          | 50                    |
| 4                         | 2                          | 60                    |
| 6                         | 3                          | 70                    |
| 8                         | 4                          | 80                    |

### Observations

Before proceeding, it's important to notice that $x_2$ is directly proportional to $x_1$:

$$
x_2 = \frac{1}{2} x_1
$$

This means that there is perfect multicollinearity between $x_1$ and $x_2$. In multiple linear regression, perfect multicollinearity causes the design matrix to be singular, making it impossible to uniquely estimate the regression coefficients for $x_1$ and $x_2$.

### Implications of Multicollinearity

When independent variables are perfectly correlated, the matrix $X^\top X $ (where $X $ is the design matrix) becomes singular (non-invertible). This prevents us from calculating the coefficients using the normal equation:

$$
\hat{\boldsymbol{\beta}} = (X^\top X)^{-1} X^\top \boldsymbol{y}
$$

### Adjusted Approach

Given the perfect linear relationship between $x_1$ and $x_2$, we can simplify the model by combining $x_1$ and $x_2$ into a single variable or by using only one of them in the regression.

#### Simplifying the Model

Since $x_2 = \frac{1}{2} x_1$, we can express $y$ solely in terms of $x_1$:

$$
y = \beta_0 + \beta_1 x_1 + \beta_2 \left( \frac{1}{2} x_1 \right) = \beta_0 + \left( \beta_1 + \frac{\beta_2}{2} \right) x_1
$$

Let $\gamma = \beta_1 + \frac{\beta_2}{2}$. The model becomes:

$$
y = \beta_0 + \gamma x_1
$$

Now, we can proceed with a simple linear regression of $y$ on $x_1$.

### Step-by-Step Calculation

#### 1. Calculate the Means

Compute the mean of $x_1$ and $y$:

$$
\bar{x}_1 = \frac{2 + 4 + 6 + 8}{4} = \frac{20}{4} = 5
$$

$$
\bar{y} = \frac{50 + 60 + 70 + 80}{4} = \frac{260}{4} = 65
$$

#### 2. Calculate the Sum of Squares

Compute the sum of squares for $x_1$ and the cross-product of $x_1$ and $y$:

$$
SS_{x_1 x_1} = \sum_{i=1}^{n} (x_{1i} - \bar{x}_1)^2 = (2 - 5)^2 + (4 - 5)^2 + (6 - 5)^2 + (8 - 5)^2 = 20
$$

$$
SS_{x_1 y} = \sum_{i=1}^{n} (x_{1i} - \bar{x}_1)(y_i - \bar{y}) = (2 - 5)(50 - 65) + (4 - 5)(60 - 65) + (6 - 5)(70 - 65) + (8 - 5)(80 - 65) = 100
$$

#### 3. Calculate the Regression Coefficients

Compute the slope ($\hat{\gamma}$) and intercept ($\hat{\beta}_0 $):

$$
\hat{\gamma} = \frac{SS_{x_1 y}}{SS_{x_1 x_1}} = \frac{100}{20} = 5
$$

$$
\hat{\beta}_0 = \bar{y} - \hat{\gamma} \bar{x}_1 = 65 - (5)(5) = 40
$$

#### 4. Write the Regression Equation

The best-fitting line is:

$$
\hat{y} = 40 + 5 x_1
$$

#### 5. Verify the Model with the Data

Compute the predicted $y$ values using the regression equation:

For $x_1 = 2$:

$$
\hat{y} = 40 + 5(2) = 50
$$

For $x_1 = 4 $:

$$
\hat{y} = 40 + 5(4) = 60
$$

For $x_1 = 6 $:

$$
\hat{y} = 40 + 5(6) = 70
$$

For $x_1 = 8 $:

$$
\hat{y} = 40 + 5(8) = 80
$$

The predicted values match the actual test scores perfectly.

Plot:

![output(16)](https://github.com/user-attachments/assets/ee0c3bb1-ce28-4418-9bb9-def7d90f273e)

## Example: No Perfect Multicollinearity

Suppose we have the following data on the number of hours studied ($x_1$), attendance rate ($x_2$) as a percentage, and test scores ($y$):

| Student ($i $) | Hours Studied ($x_{1i}$) | Attendance Rate ($x_{2i}$) | Test Score ($y_i$) |
|-------------------|-------------------------------|---------------------------------|-------------------------|
| 1                 | 2                             | 70                              | 65                      |
| 2                 | 3                             | 80                              | 70                      |
| 3                 | 5                             | 60                              | 75                      |
| 4                 | 7                             | 90                              | 85                      |
| 5                 | 9                             | 95                              | 95                      |

### Objective

We aim to fit a multiple linear regression model of the form:

$$
y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \varepsilon
$$

where:

- $y$ is the dependent variable (test score),
- $x_1$ is the number of hours studied,
- $x_2$ is the attendance rate,
- $\varepsilon $ is the error term.

### Step-by-Step Calculation

#### 1. Organize the Data

First, compute the necessary sums and products:

| $i $ | $x_{1i}$ | $x_{2i}$ | $y_i$ | $x_{1i}^2$ | $x_{2i}^2$ | $x_{1i} x_{2i}$ | $x_{1i} y_i$ | $x_{2i} y_i$ |
|---------|--------------|--------------|-----------|----------------|----------------|---------------------|------------------|------------------|
| 1       | 2            | 70           | 65        | 4              | 4,900          | 140                 | 130              | 4,550            |
| 2       | 3            | 80           | 70        | 9              | 6,400          | 240                 | 210              | 5,600            |
| 3       | 5            | 60           | 75        | 25             | 3,600          | 300                 | 375              | 4,500            |
| 4       | 7            | 90           | 85        | 49             | 8,100          | 630                 | 595              | 7,650            |
| 5       | 9            | 95           | 95        | 81             | 9,025          | 855                 | 855              | 9,025            |
| **Total** | **26**        | **395**       | **390**     | **168**          | **32,025**        | **2,165**           | **2,165**        | **31,325**       |

#### 2. Compute the Means

$$
\bar{x}_1 = \frac{\sum x_{1i}}{n} = \frac{26}{5} = 5.2
$$

$$
\bar{x}_2 = \frac{\sum x_{2i}}{n} = \frac{395}{5} = 79
$$

$$
\bar{y} = \frac{\sum y_i}{n} = \frac{390}{5} = 78
$$

#### 3. Compute Sum of Squares and Cross Products

**Sum of Squares for $x_1$:**

$$
SS_{x_1 x_1} = \sum x_{1i}^2 - n \bar{x}_1^2 = 168 - 5 (5.2)^2 = 168 - 135.2 = 32.8
$$

**Sum of Squares for $x_2$:**

$$
SS_{x_2 x_2} = \sum x_{2i}^2 - n \bar{x}_2^2 = 32{,}025 - 5 (79)^2 = 32{,}025 - 31{,}205 = 820
$$

**Sum of Cross Products between $x_1$ and $x_2$:**

$$
SS_{x_1 x_2} = \sum x_{1i} x_{2i} - n \bar{x}_1 \bar{x}_2 = 2{,}165 - 5 (5.2)(79) = 2{,}165 - 2{,}054 = 111
$$

**Sum of Cross Products between $x_1$ and $y$:**

$$
SS_{x_1 y} = \sum x_{1i} y_i - n \bar{x}_1 \bar{y} = 2{,}165 - 5 (5.2)(78) = 2{,}165 - 2{,}028 = 137
$$

**Sum of Cross Products between $x_2$ and $y$:**

$$
SS_{x_2 y} = \sum x_{2i} y_i - n \bar{x}_2 \bar{y} = 31{,}325 - 5 (79)(78) = 31{,}325 - 30{,}810 = 515
$$

#### 4. Compute the Regression Coefficients

We use the formulas for multiple linear regression coefficients:

**Denominator (Determinant):**

$$
D = SS_{x_1 x_1} SS_{x_2 x_2} - (SS_{x_1 x_2})^2 = (32.8)(820) - (111)^2 = 26{,}896 - 12{,}321 = 14{,}575
$$

**Coefficient $\hat{\beta}_1$:**

$$
\hat{\beta}_1 = \frac{SS_{x_1 y} SS_{x_2 x_2} - SS_{x_1 x_2} SS_{x_2 y}}{D}
$$

$$
\hat{\beta}_1 = \frac{(137)(820) - (111)(515)}{14{,}575} = \frac{112{,}340 - 57{,}165}{14{,}575} = \frac{55{,}175}{14{,}575} \approx 3.785
$$

**Coefficient $\hat{\beta}_2$:**

$$
\hat{\beta}_2 = \frac{SS_{x_2 y} SS_{x_1 x_1} - SS_{x_1 x_2} SS_{x_1 y}}{D}
$$

$$
\hat{\beta}_2 = \frac{(515)(32.8) - (111)(137)}{14{,}575} = \frac{16{,}892 - 15{,}207}{14{,}575} = \frac{1{,}685}{14{,}575} \approx 0.116
$$

**Intercept $\hat{\beta}_0 $:**

$$
\hat{\beta}_0 = \bar{y} - \hat{\beta}_1 \bar{x}_1 - \hat{\beta}_2 \bar{x}_2
$$

$$
\hat{\beta}_0 = 78 - (3.785)(5.2) - (0.116)(79) = 78 - 19.642 - 9.164 \approx 49.194
$$

#### 5. Write the Regression Equation

The estimated multiple linear regression model is:

$$
\hat{y} = 49.194 + 3.785 x_1 + 0.116 x_2
$$

#### 6. Interpret the Coefficients

- The **intercept ($\beta_0 = 49.194$)** represents the estimated test score when both hours studied and attendance rate are zero. While this value may not have practical significance, it is necessary for constructing the mathematical model.
- The **coefficient of $x_1$ ($\beta_1 = 3.785$)** suggests that for each additional hour studied, the test score increases by approximately 3.785 points, assuming the attendance rate remains constant.
- The **coefficient of $x_2$ ($\beta_2 = 0.116$)** indicates that for each 1% increase in attendance rate, the test score rises by approximately 0.116 points, holding hours studied constant.

#### 7. Verify the Model with the Data

Compute the predicted test scores ($\hat{y}_i$) and residuals ($e_i = y_i - \hat{y}_i$).

**For Student 1:**

$$
\hat{y}_1 = 49.194 + 3.785 (2) + 0.116 (70) = 49.194 + 7.570 + 8.120 = 64.884
$$

$$
e_1 = y_1 - \hat{y}_1 = 65 - 64.884 = 0.116
$$

**For Student 2:**

$$
\hat{y}_2 = 49.194 + 3.785 (3) + 0.116 (80) = 49.194 + 11.355 + 9.280 = 69.829
$$

$$
e_2 = 70 - 69.829 = 0.171
$$

**For Student 3:**

$$
\hat{y}_3 = 49.194 + 3.785 (5) + 0.116 (60) = 49.194 + 18.925 + 6.960 = 75.079
$$

$$
e_3 = 75 - 75.079 = -0.079
$$

**For Student 4:**

$$
\hat{y}_4 = 49.194 + 3.785 (7) + 0.116 (90) = 49.194 + 26.495 + 10.440 = 86.129
$$

$$
e_4 = 85 - 86.129 = -1.129
$$

**For Student 5:**

$$
\hat{y}_5 = 49.194 + 3.785 (9) + 0.116 (95) = 49.194 + 34.065 + 11.020 = 94.279
$$

$$
e_5 = 95 - 94.279 = 0.721
$$

The residuals are small, indicating a good fit of the model to the data.

Plot:

![output(17)](https://github.com/user-attachments/assets/4cd38537-ee4a-4c6c-b788-fa614394967c)


### Checking for Multicollinearity

Compute the correlation coefficient between $x_1$ and $x_2$:

$$
r_{x_1 x_2} = \frac{SS_{x_1 x_2}}{\sqrt{SS_{x_1 x_1} \times SS_{x_2 x_2}}}
$$

$$
r_{x_1 x_2} = \frac{111}{\sqrt{32.8 \times 820}} = \frac{111}{\sqrt{26{,}896}} = \frac{111}{164} \approx 0.677
$$

A correlation coefficient of approximately 0.677 indicates a moderate correlation, not perfect multicollinearity.
