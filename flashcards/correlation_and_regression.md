# Quizzes on Correlation and Regression

This series of quizzes covers essential topics in correlation and regression analysis, including:

- **Correlation**: Test your understanding of correlation coefficients, how to interpret them, and the difference between positive, negative, and zero correlation.
- **Linear Regression**: Learn about the fundamentals of simple linear regression, including the interpretation of slope and intercept.
- **Multiple Regression**: Assess your knowledge of multiple linear regression, where more than one independent variable is used to predict a dependent variable.
- **Assumptions of Regression**: Explore the assumptions that must be met for regression models to be valid, such as linearity, homoscedasticity, and normality of residuals.
- **Coefficient of Determination (R²)**: Understand how to interpret R², which measures the proportion of variance in the dependent variable explained by the independent variables.
- **Multicollinearity**: Learn about multicollinearity in multiple regression, how to detect it, and its impact on the regression model.
- **Residual Analysis**: Explore the role of residuals in diagnosing the fit of regression models and detecting violations of regression assumptions.
- **Logistic Regression**: Assess your understanding of logistic regression, which is used when the dependent variable is binary.

## Correlation

<details>
<summary>What is correlation?</summary><br>
**Correlation** is a statistical measure that describes the strength and direction of a linear relationship between two variables. It is quantified by the **correlation coefficient** (denoted by \(r\)), which ranges from -1 to 1:
- **\(r = 1\)**: Perfect positive correlation.
- **\(r = -1\)**: Perfect negative correlation.
- **\(r = 0\)**: No linear correlation.
</details>

<details>
<summary>What is a positive correlation?</summary><br>
A **positive correlation** occurs when an increase in one variable is associated with an increase in another variable. For example, in a dataset, if higher temperatures tend to correspond with higher ice cream sales, this indicates a positive correlation.
</details>

<details>
<summary>What is a negative correlation?</summary><br>
A **negative correlation** occurs when an increase in one variable is associated with a decrease in another variable. For instance, if higher temperatures lead to lower heating costs, this reflects a negative correlation.
</details>

<details>
<summary>What is the difference between correlation and causation?</summary><br>
**Correlation** indicates that two variables are related, but it does not imply that one variable causes the other. **Causation**, on the other hand, means that changes in one variable directly cause changes in the other. Correlation does not establish causality without further analysis.
</details>

<details>
<summary>How do you interpret the value of the Pearson correlation coefficient?</summary><br>
The **Pearson correlation coefficient** (denoted \(r\)) measures the strength and direction of a linear relationship between two variables:
- **\(r = 1\)**: Perfect positive linear relationship.
- **\(r = -1\)**: Perfect negative linear relationship.
- **\(0.7 \leq r < 1\)**: Strong positive correlation.
- **\(0.3 \leq r < 0.7\)**: Moderate positive correlation.
- **\(0 < r < 0.3\)**: Weak positive correlation.
- **\(r = 0\)**: No correlation.
The same scale applies for negative values.
</details>

---

## Linear Regression

<details>
<summary>What is simple linear regression?</summary><br>
**Simple linear regression** is a statistical method used to model the relationship between two variables: one **independent variable** (predictor) and one **dependent variable** (outcome). The goal is to find the best-fitting straight line (regression line) that minimizes the distance between observed values and predicted values. The equation of the regression line is:
\[ Y = \beta_0 + \beta_1 X + \epsilon \]
where \(Y\) is the dependent variable, \(X\) is the independent variable, \(\beta_0\) is the intercept, \(\beta_1\) is the slope, and \(\epsilon\) is the error term.
</details>

<details>
<summary>How do you interpret the slope and intercept in linear regression?</summary><br>
- The **slope** (\(\beta_1\)) represents the change in the dependent variable (\(Y\)) for every one-unit increase in the independent variable (\(X\)). If \(\beta_1\) is positive, \(Y\) increases as \(X\) increases; if \(\beta_1\) is negative, \(Y\) decreases as \(X\) increases.
- The **intercept** (\(\beta_0\)) is the predicted value of \(Y\) when \(X = 0\). It indicates the starting point of the regression line on the Y-axis.
</details>

<details>
<summary>What is the residual in a regression model?</summary><br>
A **residual** is the difference between an observed value and the value predicted by the regression model. It is calculated as:
\[ \text{Residual} = Y_{\text{observed}} - Y_{\text{predicted}} \]
Residuals are used to evaluate the fit of the model, with smaller residuals indicating a better fit.
</details>

<details>
<summary>What is the objective of the least squares method in linear regression?</summary><br>
The **least squares method** aims to minimize the sum of the squared residuals (the differences between observed and predicted values). By minimizing this quantity, the regression line is optimized to fit the data as closely as possible.
</details>

---

## Multiple Regression

<details>
<summary>What is multiple linear regression?</summary><br>
**Multiple linear regression** is an extension of simple linear regression that models the relationship between a dependent variable and two or more independent variables. The regression equation is:
\[ Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \dots + \beta_n X_n + \epsilon \]
where \(X_1, X_2, ..., X_n\) are the independent variables, and \(\beta_1, \beta_2, ..., \beta_n\) are their respective coefficients.
</details>

<details>
<summary>What does multicollinearity mean in multiple regression?</summary><br>
**Multicollinearity** occurs when two or more independent variables in a multiple regression model are highly correlated with each other. This can make it difficult to determine the individual effect of each variable on the dependent variable, leading to inflated standard errors and unreliable coefficient estimates.
</details>

<details>
<summary>How can you detect multicollinearity?</summary><br>
Multicollinearity can be detected using several methods:
1. **Variance Inflation Factor (VIF)**: A VIF value greater than 10 indicates high multicollinearity.
2. **Correlation matrix**: High correlations between independent variables suggest multicollinearity.
3. **Eigenvalues**: Small eigenvalues of the correlation matrix can indicate multicollinearity.
</details>

<details>
<summary>What is the adjusted R² in multiple regression?</summary><br>
The **adjusted R²** is a modified version of the R² that accounts for the number of independent variables in the model. It adjusts for the fact that adding more variables can artificially increase the R², even if those variables do not improve the model. Adjusted R² provides a more accurate measure of the model's explanatory power.
</details>

---

## Assumptions of Regression

<details>
<summary>What are the key assumptions of linear regression?</summary><br>
The key assumptions of linear regression are:
1. **Linearity**: The relationship between the independent and dependent variables is linear.
2. **Independence**: The observations are independent of each other.
3. **Homoscedasticity**: The variance of residuals is constant across all levels of the independent variables.
4. **Normality**: The residuals are normally distributed.
5. **No multicollinearity** (for multiple regression): The independent variables are not highly correlated with each other.
</details>

<details>
<summary>What is homoscedasticity?</summary><br>
**Homoscedasticity** refers to the assumption that the variance of the residuals is constant across all levels of the independent variables. In other words, the spread of the residuals should be roughly the same regardless of the value of the independent variables. A violation of this assumption can lead to inefficient estimates in the regression model.
</details>

<details>
<summary>How do you check for normality of residuals in a regression model?</summary><br>
To check for normality of residuals, you can:
1. **Plot a histogram** of the residuals: If the residuals are normally distributed, the histogram should resemble a bell curve.
2. **Use a Q-Q plot**: In a Q-Q (quantile-quantile) plot, the points should fall along a straight line if the residuals are normally distributed.
3. **Perform a normality test**: Tests like the Shapiro-Wilk test or Kolmogorov-Smirnov test can be used to assess the normality of residuals.
</details>

---

## Coefficient of Determination (R²)

<details>
<summary>What is the coefficient of determination (R²)?</summary><br>
The **coefficient of determination (R²)** measures the proportion of the variance in the dependent variable that is

 explained by the independent variables in the model. It ranges from 0 to 1:
- **R² = 1**: Perfect fit (the model explains 100% of the variance).
- **R² = 0**: The model explains none of the variance.
</details>

<details>
<summary>How do you interpret R²?</summary><br>
- A higher **R²** value indicates that a larger proportion of the variance in the dependent variable is explained by the independent variable(s).
- For example, an R² of 0.80 means that 80% of the variation in the dependent variable is explained by the independent variable(s), and 20% is unexplained.
</details>

<details>
<summary>What are the limitations of R²?</summary><br>
While **R²** indicates the goodness of fit of a model, it has limitations:
- **R² increases** as more variables are added to the model, even if those variables do not improve the model’s predictive power. This can lead to overfitting.
- It does not indicate whether the independent variables are meaningful predictors or whether the model assumptions are met.
For multiple regression, **adjusted R²** is used to address these limitations.
</details>

---

## Residual Analysis

<details>
<summary>What is residual analysis in regression?</summary><br>
**Residual analysis** involves examining the residuals (the differences between observed and predicted values) to evaluate the fit of a regression model. Residual analysis helps in identifying violations of assumptions like linearity, homoscedasticity, and normality, and can uncover outliers or influential data points.
</details>

<details>
<summary>How do you detect heteroscedasticity in residuals?</summary><br>
**Heteroscedasticity** occurs when the variance of the residuals is not constant. To detect heteroscedasticity, you can:
1. **Plot residuals vs. predicted values**: If the spread of residuals increases or decreases as the predicted values change, heteroscedasticity may be present.
2. **Breusch-Pagan test**: A statistical test that can be used to detect heteroscedasticity.
3. **White’s test**: Another test for heteroscedasticity that does not assume a specific form for the relationship between the residual variance and predictors.
</details>

---

## Logistic Regression

<details>
<summary>What is logistic regression?</summary><br>
**Logistic regression** is used when the dependent variable is binary (e.g., 0 or 1, yes or no). It models the probability that a certain event will occur, based on one or more independent variables. The logistic regression model uses the **logit function** to map predicted values to a probability between 0 and 1:
\[ \text{logit}(p) = \ln\left(\frac{p}{1-p}\right) = \beta_0 + \beta_1 X_1 + \dots + \beta_n X_n \]
where \(p\) is the probability of the event occurring.
</details>

<details>
<summary>How do you interpret coefficients in logistic regression?</summary><br>
In **logistic regression**, the coefficients (\(\beta\)) represent the change in the **log-odds** of the dependent variable occurring for a one-unit change in the independent variable. The exponentiated coefficient (\(e^{\beta}\)) gives the **odds ratio**, which can be interpreted as the change in the odds of the event occurring for a one-unit increase in the independent variable.
</details>

<details>
<summary>What is the difference between linear and logistic regression?</summary><br>
- **Linear regression** is used to predict a continuous dependent variable, while **logistic regression** is used to predict a binary outcome.
- In linear regression, the relationship between the independent and dependent variables is linear, whereas logistic regression models the probability of an event occurring using the logit function, producing outputs between 0 and 1.
</details>
