# Logistic Regression

Logistic regression is a statistical method used for modeling the probability of a binary outcome based on one or more predictor variables. It is widely used in various fields such as medicine, social sciences, and machine learning for classification problems where the dependent variable is dichotomous (e.g., success/failure, yes/no, positive/negative).

## The Logistic Regression Model

### Binary Outcomes

In logistic regression, the dependent variable $y$ takes on binary values:

$$
y_i = \begin{cases}
1 & \text{if event occurs (e.g., success)} \\
0 & \text{if event does not occur (e.g., failure)}
\end{cases}
$$

### Logistic Function (Sigmoid Function)

The logistic function models the probability that $y = 1$ given the predictor variables $x_1, x_2, \dots, x_p$:

$$
p(x) = P(y = 1 \mid x) = \frac{1}{1 + e^{-(\beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_p x_p)}}
$$

This function maps any real-valued number into a value between 0 and 1, making it suitable for probability estimation.

### Odds and Logit Function

The **odds** of an event occurring is the ratio of the probability that the event occurs to the probability that it does not occur.

$$
\text{Odds}(x) = \frac{p(x)}{1 - p(x)}
$$

The natural logarithm of the odds is called the **logit function**.

$$
\text{logit}(p(x)) = \ln \left( \frac{p(x)}{1 - p(x)} \right) = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_p x_p
$$

The logit function establishes a linear relationship between the predictor variables and the log-odds of the outcome.

### Interpretation of Coefficients

- The **intercept ($\beta_0$)** represents the log-odds of the outcome when all predictor variables are zero.
- The **coefficients ($\beta_j$)** indicate the change in the log-odds of the outcome for a one-unit increase in $x_j$, while keeping all other variables constant.

Exponentiating the coefficients provides the **odds ratios**:

$$
\text{Odds Ratio for } x_j = e^{\beta_j}
$$

An odds ratio greater than 1 indicates that as $x_j$ increases, the odds of the outcome occurring increase.

## Estimation of Coefficients

Unlike linear regression, logistic regression does not have a closed-form solution for estimating the coefficients. Instead, coefficients are estimated using **Maximum Likelihood Estimation (MLE)**.

### Likelihood Function

Given $n$ independent observations, the likelihood function $L(\boldsymbol{\beta})$ is the product of the probabilities of observing the data:

$$
L(\boldsymbol{\beta}) = \prod_{i=1}^{n} [p(x_i)]^{y_i} [1 - p(x_i)]^{1 - y_i}
$$

### Log-Likelihood Function

Taking the natural logarithm simplifies the product into a sum:

$$
\ell(\boldsymbol{\beta}) = \ln L(\boldsymbol{\beta}) = \sum_{i=1}^{n} \left[ y_i \ln p(x_i) + (1 - y_i) \ln (1 - p(x_i)) \right]
$$

### Maximizing the Log-Likelihood

The goal is to find the coefficients $\boldsymbol{\beta}$ that maximize $\ell(\boldsymbol{\beta})$. This is typically done using iterative numerical methods such as:

- Newton-Raphson method
- Fisher Scoring
- Gradient Descent

### Newton-Raphson Method

An iterative method that updates the coefficient estimates using:

$$
\boldsymbol{\beta}^{(k+1)} = \boldsymbol{\beta}^{(k)} - [\mathbf{H}(\boldsymbol{\beta}^{(k)})]^{-1} \mathbf{g}(\boldsymbol{\beta}^{(k)})
$$

Where:

- $\mathbf{g}(\boldsymbol{\beta})$ is the gradient (first derivative) of the log-likelihood function.
- $\mathbf{H}(\boldsymbol{\beta})$ is the Hessian matrix (second derivative) of the log-likelihood function.

## Assumptions of Logistic Regression

1. The **binary outcome** indicates that the dependent variable has two possible values.
2. **Independent observations** ensure that each data point is independent of the others.
3. **Linearity in log-odds** means that the logit of the outcome is a linear function of the predictor variables.
4. **No perfect (and little severe) multicollinearity** among the predictors; otherwise coefficients are unstable.
5. **No complete separation**: if a linear combination of predictors perfectly splits the classes, the MLE does not exist.
6. A **large sample size** is preferred, as maximum likelihood estimation (MLE) performs better with more data.

## Example

### Problem Statement

We aim to predict whether a student will pass a test ($y = 1$) or fail ($y = 0$) based on:

- $x_1$: Number of hours studied
- $x_2$: Number of practice exams taken

### Data

| Student ($i$) | Hours Studied ($x_{1i}$) | Practice Exams ($x_{2i}$) | Pass ($y_i$) |
|---|---|---|---|
| 1  | 1  | 0 | 0 |
| 2  | 2  | 1 | 0 |
| 3  | 3  | 2 | 0 |
| 4  | 4  | 3 | 1 |
| 5  | 5  | 0 | 0 |
| 6  | 6  | 2 | 1 |
| 7  | 7  | 3 | 0 |
| 8  | 8  | 1 | 1 |
| 9  | 9  | 4 | 1 |
| 10 | 10 | 2 | 1 |

The classes overlap (student 4 passes with 4 hours, student 7 fails with 7 hours), so a finite maximum likelihood estimate exists. If one class could be separated perfectly from the other by a hyperplane (complete separation), the likelihood would increase forever as the coefficients grow and the MLE would not exist; software then reports huge coefficients or a convergence warning.

### Step-by-Step Estimation

#### 1. Initial Setup

We need to estimate $\beta_0$, $\beta_1$, and $\beta_2$ in the logistic regression model:

$$
p(x) = \frac{1}{1 + e^{-(\beta_0 + \beta_1 x_1 + \beta_2 x_2)}}
$$

#### 2. Construct the Design Matrix and Response Vector

Let $\mathbf{X}$ be the $10 \times 3$ design matrix whose first column is the intercept, and $\mathbf{y}$ the response vector:

$$
\mathbf{X} = \begin{bmatrix}
1 & 1 & 0 \\
1 & 2 & 1 \\
1 & 3 & 2 \\
1 & 4 & 3 \\
1 & 5 & 0 \\
1 & 6 & 2 \\
1 & 7 & 3 \\
1 & 8 & 1 \\
1 & 9 & 4 \\
1 & 10 & 2
\end{bmatrix}, \qquad
\mathbf{y} = (0,0,0,1,0,1,0,1,1,1)^\top
$$

#### 3. Initialize Coefficients

Start with $\boldsymbol{\beta}^{(0)} = (0, 0, 0)^\top$. Then every $p_i^{(0)} = 1/2$.

#### 4. One Newton-Raphson Step by Hand

The gradient and Hessian of the log-likelihood are

$$
\mathbf{g}(\boldsymbol{\beta}) = \mathbf{X}^\top(\mathbf{y} - \mathbf{p}), \qquad
\mathbf{H}(\boldsymbol{\beta}) = -\mathbf{X}^\top \mathbf{W} \mathbf{X}, \quad \mathbf{W} = \operatorname{diag}\big(p_i(1-p_i)\big).
$$

At $\boldsymbol{\beta}^{(0)}$, $\mathbf{y}-\mathbf{p} = \pm 0.5$ and $\mathbf{W} = 0.25\,\mathbf{I}$, so

$$
\mathbf{g} = \begin{bmatrix} 0 \\ 9.5 \\ 3 \end{bmatrix}, \qquad
\mathbf{H} = -0.25 \begin{bmatrix} 10 & 55 & 18 \\ 55 & 385 & 117 \\ 18 & 117 & 48 \end{bmatrix}.
$$

The update $\boldsymbol{\beta}^{(1)} = -\mathbf{H}^{-1}\mathbf{g}$ gives $\boldsymbol{\beta}^{(1)} \approx (-2.724,\ 0.391,\ 0.318)^\top$. Repeating the step, the iterates are $(-3.961, 0.549, 0.515)$, $(-4.463, 0.610, 0.601)$, $(-4.529, 0.618, 0.613)$, and $(-4.530, 0.618, 0.613)$; the estimates have converged after about five iterations.

#### 5. Estimated Coefficients

$$
\hat{\beta}_0 = -4.530, \quad \hat{\beta}_1 = 0.618, \quad \hat{\beta}_2 = 0.613
$$

with standard errors $\approx 2.90,\ 0.42,\ 0.84$ (from $\sqrt{\operatorname{diag}(\mathbf{X}^\top\mathbf{W}\mathbf{X})^{-1}}$ at the solution). With only 10 observations neither slope is individually significant (Wald $z \approx 1.47$ and $0.73$); the example is meant to show the mechanics, not a strong effect. The maximized log-likelihood is $\ell(\hat{\boldsymbol\beta}) \approx -4.034$, compared with $10 \ln 0.5 \approx -6.931$ for the intercept-only model.

#### 6. Logistic Regression Equation

$$
\hat p(x) = \frac{1}{1 + e^{-(-4.530 + 0.618 x_1 + 0.613 x_2)}}
$$

### Interpretation of Coefficients

**Intercept ($\hat\beta_0 = -4.530$)**: The log-odds of passing when $x_1 = 0$ and $x_2 = 0$ (an extrapolation, since no student studied 0 hours).

**Coefficient for Hours Studied ($\hat\beta_1 = 0.618$)**: For each additional hour studied, the log-odds of passing increase by 0.618, holding $x_2$ constant.

$$
e^{0.618} \approx 1.86
$$

The odds of passing are multiplied by about 1.86 for each additional hour studied.

**Coefficient for Practice Exams ($\hat\beta_2 = 0.613$)**: For each additional practice exam, the log-odds of passing increase by 0.613, holding $x_1$ constant.

$$
e^{0.613} \approx 1.85
$$

The odds of passing are multiplied by about 1.85 for each additional practice exam.

Note that an odds ratio is a multiplicative change in the odds, not in the probability; the change in probability depends on where on the curve the student sits.

### Predicting Probabilities

#### A Student Who Studied 5 Hours and Took 2 Practice Exams

$$
\hat p = \frac{1}{1 + e^{-(-4.530 + 0.618 \times 5 + 0.613 \times 2)}} = \frac{1}{1 + e^{-(-0.214)}} = \frac{1}{1 + e^{0.214}} \approx 0.447
$$

The estimated probability of passing is about 44.7%.

#### A Student Who Studied 7 Hours and Took 3 Practice Exams

$$
\hat p = \frac{1}{1 + e^{-(-4.530 + 0.618 \times 7 + 0.613 \times 3)}} = \frac{1}{1 + e^{-1.635}} \approx 0.837
$$

The estimated probability of passing is about 83.7%.

A plot of the fitted probability surface and the 0.5 decision boundary is produced by [logistic_regression.py](../../scripts/regression/logistic_regression.py).

### Model Evaluation

#### Confusion Matrix

Using a threshold of 0.5 to classify predictions (training data, so these numbers are optimistic):

| Student ($i$) | $y_i$ | Predicted $\hat p_i$ | Predicted Class ($\hat{y}_i$) |
|---|---|---|---|
| 1  | 0 | 0.020 | 0 |
| 2  | 0 | 0.064 | 0 |
| 3  | 0 | 0.190 | 0 |
| 4  | 1 | 0.445 | 0 |
| 5  | 0 | 0.192 | 0 |
| 6  | 1 | 0.600 | 1 |
| 7  | 0 | 0.837 | 1 |
| 8  | 1 | 0.736 | 1 |
| 9  | 1 | 0.970 | 1 |
| 10 | 1 | 0.947 | 1 |

- **True Positives (TP)**: 4 (Students 6, 8, 9, 10)
- **True Negatives (TN)**: 4 (Students 1, 2, 3, 5)
- **False Negatives (FN)**: 1 (Student 4)
- **False Positives (FP)**: 1 (Student 7)

#### Accuracy

$$
\text{Accuracy} = \frac{\text{TP} + \text{TN}}{\text{Total}} = \frac{4 + 4}{10} = 0.8
$$

#### Precision

$$
\text{Precision} = \frac{\text{TP}}{\text{TP} + \text{FP}} = \frac{4}{4 + 1} = 0.8
$$

#### Recall (Sensitivity)

$$
\text{Recall} = \frac{\text{TP}}{\text{TP} + \text{FN}} = \frac{4}{4 + 1} = 0.8
$$

#### F1 Score

$$
\text{F1} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}} = 2 \times \frac{0.8 \times 0.8}{0.8 + 0.8} = 0.8
$$

### Receiver Operating Characteristic (ROC) Curve

- Plotting True Positive Rate (Recall) vs. False Positive Rate at various thresholds.
- Calculate Area Under the ROC Curve (AUC) to assess model performance. AUC equals the probability that a randomly chosen positive case receives a higher predicted probability than a randomly chosen negative case; 0.5 is chance and 1 is perfect ranking. For the example above, AUC $= 22/25 = 0.88$ (22 of the 25 pass/fail pairs are ranked correctly).

### Extensions to Multiple Classes

The logistic regression framework described above handles binary outcomes. When the dependent variable has more than two categories, two common extensions are used:

- **Multinomial logistic regression** generalizes binary logistic regression to $K > 2$ unordered classes. It models the log-odds of each class relative to a reference category, estimating a separate set of coefficients for each class.
- **Ordinal logistic regression** is appropriate when the outcome categories have a natural ordering (e.g., low, medium, high). It models cumulative log-odds using a single set of slope coefficients shared across all thresholds, with separate intercept terms for each cumulative split.
