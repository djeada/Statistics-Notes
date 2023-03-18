# Logistic Regression

Logistic regression is a type of regression analysis used for predicting the probability of an outcome in a binary classification problem. It models the relationship between a binary dependent variable (response variable) and one or more independent variables (predictor variables).

## Sigmoid (Logistic) Function

In logistic regression, the sigmoid (logistic) function is used to convert the linear combination of independent variables into a probability value between 0 and 1:

$$
p(x) = \frac{1}{1 + e^{-(\beta_0 + \beta_1x_1 + \beta_2x_2 + ... + \beta_nx_n)}}
$$

Where:
- $p(x)$ is the probability of the outcome being 1 given the independent variables
- $x_1, x_2, ..., x_n$ are the independent variables
- $\beta_0$ is the intercept
- $\beta_1, \beta_2, ..., \beta_n$ are the coefficients

## Odds Ratio

The odds ratio is the ratio of the probability of the event occurring to the probability of the event not occurring:

$$
\text{Odds}(x) = \frac{p(x)}{1 - p(x)}
$$

## Logit Function (Log-Odds)

The logit function is the natural logarithm of the odds ratio:

$$
\text{logit}(p) = \ln \left(\frac{p(x)}{1 - p(x)}\right) = \beta_0 + \beta_1x_1 + \beta_2x_2 + ... + \beta_nx_n
$$

## Estimation of Coefficients

The coefficients are estimated using the maximum likelihood method, which maximizes the likelihood function that represents the probability of observing the given data. Statistical software or optimization algorithms are used to find the coefficients that maximize the likelihood function.

## Example

Suppose we want to predict if a student will pass a test (1 for pass, 0 for fail) based on the number of hours studied (x1) and the number of practice exams taken (x2). We have the following data:

| Hours Studied (x1) | Practice Exams (x2) | Pass (y) |
|--------------------|---------------------|----------|
| 2                  | 1                   | 0        |
| 4                  | 2                   | 1        |
| 6                  | 3                   | 1        |
| 8                  | 4                   | 1        |

Using statistical software or optimization algorithms, we can calculate the coefficients for the logistic regression model:

$$
p(x) = \frac{1}{1 + e^{-(\beta_0 + \beta_1x_1 + \beta_2x_2)}}
$$

After the calculations, we obtain the coefficients:

$$
\hat{\beta_0} = -8, \; \hat{\beta_1} = 1.5, \; \hat{\beta_2} = 1
$$

So the best-fitting logistic regression model is:

$$
p(x) = \frac{1}{1 + e^{-( -8 + 1.5x_1 + 1x_2)}}
$$
