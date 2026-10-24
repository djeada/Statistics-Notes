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
<summary>What is correlation?</summary>

**Correlation** measures the strength and direction of the **linear** relationship between two numerical variables. Pearson's correlation coefficient is

$$r = \frac{\text{Cov}(X, Y)}{s_X s_Y}$$

and it always lies between −1 and 1:

- $r = 1$: perfect positive linear relationship.
- $r = -1$: perfect negative linear relationship.
- $r = 0$: no linear relationship, although a non-linear relationship may still exist.

</details>

<details>
<summary>What is a positive correlation?</summary>

A **positive correlation** ($r > 0$) means that higher values of one variable tend to go with higher values of the other. For example, days with higher temperatures tend to have higher ice-cream sales. The points in a scatter plot then drift upwards from left to right.

</details>

<details>
<summary>What is a negative correlation?</summary>

A **negative correlation** ($r < 0$) means that higher values of one variable tend to go with lower values of the other. For example, higher outdoor temperatures tend to go with lower heating costs. The points in a scatter plot then drift downwards from left to right.

</details>

<details>
<summary>What is the difference between correlation and causation?</summary>

**Correlation** means two variables vary together. **Causation** means changing one variable produces a change in the other. A correlation can arise from a confounding variable (hot weather raises both ice-cream sales and drownings), from reverse causation, or from chance. Establishing causation usually needs a randomised experiment or careful causal analysis.

</details>

<details>
<summary>How do you interpret the value of the Pearson correlation coefficient?</summary>

The sign gives the direction and $|r|$ gives the strength of the linear relationship. A common rough rule of thumb, which varies by field, is:

- $|r| = 1$: perfect linear relationship.
- $0.7 \le |r| < 1$: strong.
- $0.3 \le |r| < 0.7$: moderate.
- $0 < |r| < 0.3$: weak.
- $r = 0$: no linear relationship.

Always look at a scatter plot as well, because outliers and curved patterns can mislead $r$.

</details>

## Linear Regression

<details>
<summary>What is simple linear regression?</summary>

**Simple linear regression** models a response $Y$ as a straight-line function of one predictor $X$ plus random error:

$$Y = \beta_0 + \beta_1 X + \epsilon$$

where $\beta_0$ is the intercept, $\beta_1$ is the slope and $\epsilon$ is the error term. The coefficients are usually estimated by least squares, which minimises the sum of squared vertical distances (residuals) between the observed and fitted values.

</details>

<details>
<summary>How do you interpret the slope and intercept in linear regression?</summary>

- The **slope** ($\beta_1$) is the expected change in $Y$ for a one-unit increase in $X$. A positive slope means $Y$ tends to increase with $X$, and a negative slope means it tends to decrease.
- The **intercept** ($\beta_0$) is the expected value of $Y$ when $X = 0$. It is only meaningful if $X = 0$ is within or near the range of the data.

</details>

<details>
<summary>What is the residual in a regression model?</summary>

A **residual** is the difference between an observed value and the value the model predicts:

$$e_i = y_i - \hat{y}_i$$

Residuals estimate the unobserved errors. With an intercept, least-squares residuals sum to zero. Plotting them reveals non-linearity, non-constant variance and outliers.

</details>

<details>
<summary>What is the objective of the least squares method in linear regression?</summary>

**Least squares** chooses the coefficients that minimise the sum of squared residuals, $\sum (y_i - \hat{y}_i)^2$. In simple regression this gives

$$b_1 = r\frac{s_y}{s_x}$$

and $b_0 = \bar{y} - b_1\bar{x}$, so the fitted line always passes through $(\bar{x}, \bar{y})$.

</details>

## Multiple Regression

<details>
<summary>What is multiple linear regression?</summary>

**Multiple linear regression** extends simple regression to two or more predictors:

$$Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \dots + \beta_p X_p + \epsilon$$

Each coefficient $\beta_j$ is the expected change in $Y$ for a one-unit increase in $X_j$, **holding the other predictors constant**.

</details>

<details>
<summary>What does multicollinearity mean in multiple regression?</summary>

**Multicollinearity** occurs when two or more predictors are highly correlated with each other. It becomes hard to separate their individual effects, so the standard errors of the coefficients grow and the estimates become unstable and sensitive to small changes in the data. Predictions within the range of the data can still be fine. Perfect multicollinearity makes the coefficients impossible to estimate uniquely.

</details>

<details>
<summary>How can you detect multicollinearity?</summary>

Multicollinearity can be detected in several ways:

1. **Variance inflation factor (VIF)**: $VIF_j = 1/(1 - R_j^2)$. Values above about 5–10 are commonly taken as a sign of problematic multicollinearity.
2. **Correlation matrix**: large pairwise correlations between predictors are a warning sign, though they can miss relationships among three or more variables.
3. **Eigenvalues and condition number**: near-zero eigenvalues of $X^\top X$, or a large condition number, indicate near-linear dependence.

</details>

<details>
<summary>What is the adjusted R² in multiple regression?</summary>

**Adjusted R²** penalises $R^2$ for the number of predictors $p$ relative to the sample size $n$:

$$R^2_{adj} = 1 - (1 - R^2)\frac{n - 1}{n - p - 1}$$

Ordinary $R^2$ never decreases when a predictor is added. Adjusted $R^2$ rises only if the new predictor improves the fit more than expected by chance, which makes it more useful for comparing models of different sizes.

</details>

## Assumptions of Regression

<details>
<summary>What are the key assumptions of linear regression?</summary>

The key assumptions of the classical linear regression model are:

1. **Linearity**: the mean of $Y$ is a linear function of the predictors.
2. **Independence**: the errors are independent of each other.
3. **Homoscedasticity**: the errors have constant variance at all predictor values.
4. **Normality**: the errors are normally distributed, which is needed for exact small-sample t and F inference.
5. **No perfect multicollinearity** (multiple regression): no predictor is an exact linear combination of the others.

</details>

<details>
<summary>What is homoscedasticity?</summary>

**Homoscedasticity** means the error variance is constant across all values of the predictors, so the residuals show a roughly even band in a residuals-versus-fitted plot. When it fails (heteroscedasticity), least-squares estimates remain unbiased but are no longer efficient, and the usual standard errors, tests and confidence intervals become unreliable.

</details>

<details>
<summary>How do you check for normality of residuals in a regression model?</summary>

To check whether the residuals are normal:

1. **Plot a histogram** of the residuals and look for a roughly symmetric bell shape.
2. **Use a Q-Q plot**: if the residuals are normal, the points lie close to a straight line.
3. **Run a normality test**, such as Shapiro–Wilk. In large samples it flags trivial departures, so rely mainly on the plots.

</details>

## Coefficient of Determination (R²)

<details>
<summary>What is the coefficient of determination (R²)?</summary>

The **coefficient of determination** is the proportion of the variance in the response that the model explains:

$$R^2 = 1 - \frac{SSE}{SST}$$

For least squares with an intercept it lies between 0 and 1:

- $R^2 = 1$: the model fits the data perfectly.
- $R^2 = 0$: the model explains none of the variation beyond the mean.

In simple linear regression $R^2 = r^2$.

</details>

<details>
<summary>How do you interpret R²?</summary>

- A higher $R^2$ means a larger share of the variation in the response is accounted for by the predictors.
- For example, $R^2 = 0.80$ means 80% of the variation in the response is explained by the model and 20% remains in the residuals.

A high $R^2$ does not prove that the model is correct or causal, and a low $R^2$ can still come with significant, useful predictors.

</details>

<details>
<summary>What are the limitations of R²?</summary>

$R^2$ has several limitations:

- It **never decreases** when predictors are added, even useless ones, so it rewards overfitting.
- It says nothing about whether the predictors are meaningful, whether the assumptions hold, or how well the model predicts new data.
- It can be high for a misspecified model, such as a straight line fitted to a curve.

Adjusted $R^2$, information criteria and out-of-sample validation address some of these issues.

</details>

## Residual Analysis

<details>
<summary>What is residual analysis in regression?</summary>

**Residual analysis** examines the residuals $e_i = y_i - \hat{y}_i$ to check a fitted model. Plots of residuals against fitted values, against each predictor, against time and on a Q-Q plot reveal non-linearity, heteroscedasticity, autocorrelation, non-normality, outliers and influential points.

</details>

<details>
<summary>How do you detect heteroscedasticity in residuals?</summary>

**Heteroscedasticity** means the error variance is not constant. To detect it:

1. **Plot residuals against fitted values**: a funnel or fan shape suggests heteroscedasticity.
2. **Breusch–Pagan test**: regresses the squared residuals on the predictors to test whether the variance depends on them.
3. **White's test**: a more general test that does not assume a specific form for how the variance changes.

</details>

## Logistic Regression

<details>
<summary>What is logistic regression?</summary>

**Logistic regression** models a binary response (0/1, yes/no). It assumes the **log-odds** of the event are linear in the predictors:

$$\text{logit}(p) = \ln\left(\frac{p}{1-p}\right) = \beta_0 + \beta_1 X_1 + \dots + \beta_k X_k$$

The inverse of the logit, the logistic (sigmoid) function, $p = 1/(1 + e^{-(\beta_0 + \beta_1 X_1 + \dots)})$, maps the linear predictor to a probability between 0 and 1. The coefficients are estimated by maximum likelihood.

</details>

<details>
<summary>How do you interpret coefficients in logistic regression?</summary>

A coefficient $\beta_j$ is the change in the **log-odds** of the event for a one-unit increase in $X_j$, holding the other predictors fixed. Exponentiating gives the **odds ratio**: $e^{\beta_j}$ is the factor by which the odds are multiplied. For example, $\beta = 0.693$ gives $e^{0.693} \approx 2$, so the odds double. The effect on the probability itself depends on the starting probability.

</details>

<details>
<summary>What is the difference between linear and logistic regression?</summary>

- **Linear regression** predicts a continuous response, models its mean as a linear function of the predictors, and is usually fitted by least squares.
- **Logistic regression** predicts the probability of a binary outcome, models the log-odds as a linear function, and is fitted by maximum likelihood, so its predicted probabilities always lie between 0 and 1.

</details>
