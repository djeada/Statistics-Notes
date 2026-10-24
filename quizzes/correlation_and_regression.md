# Correlation and Regression Quiz

Notes: [Covariance](../notes/joint_distributions_and_covariance/covariance.md), [Correlation](../notes/joint_distributions_and_covariance/correlation.md), [Simple Linear Regression](../notes/regression/simple_linear_regression.md), [Multiple Regression](../notes/regression/multiple_regression.md), [Logistic Regression](../notes/regression/logistic_regression.md)

Check your understanding of covariance, correlation, least-squares regression, model assumptions and diagnostics.

#### Q. What does a **correlation coefficient** of $r = -1$ imply?

* [ ] A perfect positive linear relationship
* [ ] No linear relationship
* [x] A perfect negative linear relationship
* [ ] A weak negative linear relationship

> **Explanation:** $r = -1$ means every point lies exactly on a straight line with negative slope. The sign gives the direction and $|r|$ gives the strength.

#### Q. In an ordinary least-squares regression that **includes an intercept**, what do the residuals always sum to?

* [ ] One
* [x] Zero
* [ ] The sum of the observed responses
* [ ] The residual standard error

> **Explanation:** The least-squares normal equation for the intercept forces $\sum e_i = 0$. As a result the fitted line passes through $(\bar{x}, \bar{y})$.

#### Q. Two variables have covariance 12, and their standard deviations are 3 and 5. What is their **correlation**?

* [ ] 0.08
* [ ] 0.48
* [x] 0.8
* [ ] 12

> **Explanation:** $r = \frac{\text{Cov}(X,Y)}{s_X s_Y} = \frac{12}{3 \times 5} = 0.8$. Standardising by the SDs makes the correlation unit-free, unlike the covariance.

#### Q. Heights are recorded in centimetres and then converted to inches. What happens to their **correlation** with weight?

* [ ] It is multiplied by 2.54
* [ ] It is divided by 2.54
* [x] It does not change
* [ ] It changes sign

> **Explanation:** Correlation does not change under positive linear changes of scale or location in either variable. Covariance does change with the units.

#### Q. What does a correlation coefficient of $r = 0$ imply?

* [ ] A strong positive relationship
* [ ] The variables are independent
* [x] No linear relationship between the variables
* [ ] A perfect positive correlation

> **Explanation:** $r$ measures only linear association. Variables can be strongly related in a non-linear way, such as $y = x^2$ on a symmetric range, and still have $r = 0$, so zero correlation does not imply independence.

#### Q. In simple linear regression, what does the **slope** represent?

* [ ] The predicted value of the response when x is 0
* [x] The predicted change in the response for a one-unit increase in x
* [ ] The proportion of variation in the response explained
* [ ] The average size of the residuals

> **Explanation:** In $\hat{y} = b_0 + b_1 x$, $b_1$ is the change in $\hat{y}$ per unit of $x$. The intercept $b_0$ is the prediction at $x = 0$.

#### Q. What does **multicollinearity** mean in a multiple regression model?

* [x] Two or more predictors are highly correlated with each other
* [ ] The response is highly correlated with the predictors
* [ ] The residuals are not normally distributed
* [ ] The regression coefficients are all close to zero

> **Explanation:** Correlated predictors make it hard to separate their individual effects. This inflates coefficient standard errors and makes the estimates unstable. A strong predictor–response correlation is desirable.

#### Q. A simple linear regression has correlation $r = -0.6$ between x and y. What is $R^2$?

* [ ] −0.36
* [x] 0.36
* [ ] 0.6
* [ ] 0.77

> **Explanation:** In simple linear regression $R^2 = r^2 = (-0.6)^2 = 0.36$, so 36% of the variation in y is explained by x. $R^2$ cannot be negative.

#### Q. A correlation coefficient of about **0.9** indicates:

* [ ] No linear correlation
* [ ] A weak positive linear correlation
* [x] A strong positive linear correlation
* [ ] A strong negative linear correlation

> **Explanation:** Values of $r$ near +1 mean the points lie close to an upward-sloping line. The sign gives the direction, so 0.9 is positive.

#### Q. In simple linear regression, what does the **intercept** represent?

* [ ] The predicted change in the response for a one-unit increase in x
* [x] The predicted value of the response when x equals 0
* [ ] The residual sum of squares of the model
* [ ] The correlation between x and the response

> **Explanation:** $b_0 = \hat{y}$ at $x = 0$. It is only meaningful if $x = 0$ is within or near the range of the observed data.

#### Q. Which is a standard assumption of the classical **linear regression** model?

* [ ] The predictors must be normally distributed
* [ ] The relationship between x and y is non-linear
* [x] The errors are independent with constant variance and, for exact inference, normal
* [ ] The response must take only the values 0 and 1

> **Explanation:** The usual assumptions are linearity, independent errors, constant error variance and normal errors for t and F inference. The predictors themselves need not be normal, and a 0/1 response calls for logistic regression.

#### Q. Which pattern most clearly signals that a multiple regression model is **overfitting**?

* [x] High $R^2$ on the training data but poor accuracy on new data
* [ ] Low $R^2$ on both the training data and new data
* [ ] Normally distributed residuals with constant variance
* [ ] Similar prediction error on training data and new data

> **Explanation:** An overfit model learns noise in the training sample, so it fits that sample well but generalises poorly. Low $R^2$ everywhere points to underfitting instead.

#### Q. What does the **Durbin–Watson test** assess in a regression model?

* [ ] Multicollinearity among the predictors
* [ ] Constant variance of the residuals
* [x] Autocorrelation (lack of independence) in the residuals
* [ ] Whether the coefficients are jointly significant

> **Explanation:** The Durbin–Watson statistic tests for first-order autocorrelation in residuals, which is common with time-ordered data. Values near 2 suggest no autocorrelation.

#### Q. The p-value for the slope in a simple linear regression is **0.01**. What can you conclude at the 5% level?

* [x] There is significant evidence that the true slope is not zero
* [ ] The predictor has no effect on the response
* [ ] The model's $R^2$ must be high
* [ ] The residuals are normally distributed

> **Explanation:** The p-value tests $H_0: \beta_1 = 0$, and $0.01 < 0.05$ rejects it. A significant slope can still come with a low $R^2$, and it says nothing about the residual assumptions.

#### Q. What does it mean if the residuals of a regression model are **heteroscedastic**?

* [ ] The residuals have constant variance
* [x] The spread of the residuals changes with the fitted values or predictors
* [ ] The residuals are normally distributed
* [ ] The residuals are correlated with each other over time

> **Explanation:** Heteroscedasticity means non-constant error variance, often seen as a funnel shape in a residuals-versus-fitted plot. Correlation over time is autocorrelation, a different problem.

#### Q. What kind of **response variable** is standard logistic regression designed for?

* [ ] A continuous, unbounded variable
* [x] A binary variable such as yes/no or 0/1
* [ ] A count with no upper limit
* [ ] A normally distributed variable

> **Explanation:** Logistic regression models the probability of the outcome being 1 through the log-odds, $\ln\frac{p}{1-p} = \beta_0 + \beta_1 x$. Unbounded counts are usually modelled with Poisson regression.

#### Q. In regression, what does the **coefficient of determination** $R^2$ represent?

* [x] The proportion of variance in the response explained by the model
* [ ] The slope of the fitted regression line
* [ ] The mean of the residuals
* [ ] The total variance of the predictor

> **Explanation:** $R^2 = 1 - SSE/SST$, the share of the total variation in $y$ that the fitted model accounts for. It ranges from 0 to 1 for least squares with an intercept.

#### Q. What does a **high variance inflation factor (VIF)** indicate?

* [ ] The predictor explains most of the variation in the response
* [x] The predictor is strongly correlated with the other predictors
* [ ] The residuals are normally distributed
* [ ] The model fits the data poorly

> **Explanation:** $VIF_j = 1/(1 - R_j^2)$, where $R_j^2$ comes from regressing predictor $j$ on the other predictors. Values above about 5–10 signal problematic multicollinearity.

#### Q. What does a **negative correlation** coefficient imply?

* [ ] As one variable increases, the other tends to increase
* [x] As one variable increases, the other tends to decrease
* [ ] There is no relationship between the variables
* [ ] The variables move in perfect unison

> **Explanation:** A negative $r$ means high values of one variable go with low values of the other. "Tends to" matters: unless $r = -1$, the pattern is not exact.

#### Q. What does **adjusted $R^2$** account for that ordinary $R^2$ does not?

* [ ] The correlation among the predictors
* [x] The number of predictors relative to the sample size
* [ ] The significance of each regression coefficient
* [ ] The normality of the residuals

> **Explanation:** Ordinary $R^2$ never decreases when a predictor is added. Adjusted $R^2 = 1 - (1 - R^2)\frac{n-1}{n-p-1}$ penalises extra predictors, so it can fall when a useless variable is added.

#### Q. A model with $p = 4$ predictors fitted to $n = 25$ observations has $R^2 = 0.80$. What is the **adjusted $R^2$**?

* [ ] 0.80
* [x] 0.76
* [ ] 0.84
* [ ] 0.64

> **Explanation:** $R^2_{adj} = 1 - (1 - 0.80)\frac{25 - 1}{25 - 4 - 1} = 1 - 0.2 \times \frac{24}{20} = 1 - 0.24 = 0.76$.

#### Q. The correlation between x and y is 0.5, with $s_x = 2$ and $s_y = 10$. What is the least-squares **slope** for predicting y from x?

* [ ] 0.1
* [ ] 1.0
* [x] 2.5
* [ ] 10

> **Explanation:** $b_1 = r\frac{s_y}{s_x} = 0.5 \times \frac{10}{2} = 2.5$. Swapping the SDs gives 0.1, which is the slope for predicting x from y.

#### Q. A fitted line has slope 2.5, and the data have $\bar{x} = 4$ and $\bar{y} = 50$. What is the predicted y at **x = 6**?

* [ ] 40
* [ ] 52.5
* [x] 55
* [ ] 65

> **Explanation:** The intercept is $b_0 = \bar{y} - b_1\bar{x} = 50 - 2.5 \times 4 = 40$, so $\hat{y} = 40 + 2.5 \times 6 = 55$.

#### Q. In a logistic regression, a predictor has coefficient $\beta = 0.693$. What happens to the **odds** of the outcome when that predictor increases by one unit?

* [ ] They increase by 0.693
* [x] They roughly double
* [ ] They roughly halve
* [ ] The probability increases by 69.3 percentage points

> **Explanation:** The odds ratio is $e^{\beta} = e^{0.693} \approx 2$, so the odds are multiplied by about 2. The coefficient acts on the log-odds, not directly on the probability.

#### Q. Two variables have a strong **monotonic but curved** relationship, with one extreme outlier. Which correlation measure is most suitable?

* [ ] Pearson correlation
* [x] Spearman rank correlation
* [ ] Covariance
* [ ] Coefficient of determination

> **Explanation:** Spearman's $\rho$ is Pearson's $r$ computed on ranks. It captures any monotonic relationship and is resistant to outliers, while Pearson's $r$ measures only linear association.

#### Q. A study finds that cities with more ice-cream sales have more drownings. What is the most reasonable interpretation?

* [ ] Ice-cream consumption causes drowning
* [ ] Drowning causes higher ice-cream sales
* [x] A lurking variable, such as hot weather, may drive both
* [ ] The correlation must be a calculation error

> **Explanation:** Correlation does not establish causation. Hot weather raises both ice-cream sales and swimming, and a confounder like this can produce a strong correlation without any direct causal link.
