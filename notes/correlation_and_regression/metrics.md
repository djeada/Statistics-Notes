# Evaluation Metrics in Machine Learning

Evaluation metrics are essential tools for assessing the performance of machine learning models. They provide quantitative measures that help us understand how well a model is performing and where improvements can be made. In both classification and regression tasks, selecting appropriate evaluation metrics is crucial for model selection, tuning, and validation.

## Classification Metrics

In classification tasks, the goal is to assign input data into predefined categories or classes. Evaluating classification models requires metrics that capture the correctness and reliability of the predictions.

### Confusion Matrix

A **confusion matrix** is a tabular representation of the performance of a classification model. It compares the actual target values with those predicted by the model, providing a breakdown of correct and incorrect predictions. The confusion matrix for a binary classification problem is typically structured as follows:

|                      | **Predicted Positive** | **Predicted Negative** |
|----------------------|------------------------|------------------------|
| **Actual Positive**  | True Positive (TP)     | False Negative (FN)    |
| **Actual Negative**  | False Positive (FP)    | True Negative (TN)     |

- **True Positive (TP)**: The model correctly predicts a positive class.
- **True Negative (TN)**: The model correctly predicts a negative class.
- **False Positive (FP)**: The model incorrectly predicts a positive class (Type I error).
- **False Negative (FN)**: The model incorrectly predicts a negative class (Type II error).

### Key Metrics Derived from the Confusion Matrix

#### Accuracy

**Accuracy** measures the proportion of total correct predictions made by the model:

$$
\text{Accuracy} = \frac{\text{TP} + \text{TN}}{\text{TP} + \text{TN} + \text{FP} + \text{FN}}
$$

While accuracy is intuitive, it can be misleading in imbalanced datasets where one class significantly outnumbers the other.

#### Precision

**Precision** quantifies the correctness of positive predictions made by the model:

$$
\text{Precision} = \frac{\text{TP}}{\text{TP} + \text{FP}}
$$

High precision indicates a low rate of false positives.

#### Recall (Sensitivity or True Positive Rate)

**Recall** measures the model's ability to identify all actual positive cases:

$$
\text{Recall} = \frac{\text{TP}}{\text{TP} + \text{FN}}
$$

High recall indicates a low rate of false negatives.

#### Specificity (True Negative Rate)

**Specificity** assesses the model's ability to identify all actual negative cases:

$$
\text{Specificity} = \frac{\text{TN}}{\text{TN} + \text{FP}}
$$

High specificity indicates a low rate of false positives.

#### F1 Score

The **F1 Score** is the harmonic mean of precision and recall, providing a balance between the two metrics:

$$
\text{F1 Score} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}
$$

The F1 Score is particularly useful when dealing with imbalanced classes.

### Intuitive Explanation of Precision and Recall

Imagine you are a librarian tasked with retrieving science fiction books from a large library that contains various genres.

- **Precision**: Of all the books you retrieved, how many are actually science fiction?
  
  - If you retrieved 50 books and 40 of them are science fiction, your precision is $\frac{40}{50} = 0.8 $ or 80%.
  
- **Recall**: Of all the science fiction books in the library, how many did you successfully retrieve?
  
  - If there are 100 science fiction books in total and you retrieved 40, your recall is $\frac{40}{100} = 0.4 $ or 40%.

High precision means that most of the books you picked are relevant (few false positives), while high recall means you found most of the relevant books (few false negatives).

### Example Calculation

Suppose we have a binary classification problem with the following confusion matrix:

|                      | **Predicted Positive** | **Predicted Negative** | **Total** |
|----------------------|------------------------|------------------------|-----------|
| **Actual Positive**  | TP = 70                | FN = 30                | 100       |
| **Actual Negative**  | FP = 20                | TN = 80                | 100       |
| **Total**            | 90                     | 110                    | 200       |

- **Accuracy**:

  $$
  \text{Accuracy} = \frac{70 + 80}{200} = \frac{150}{200} = 0.75 \text{ or } 75\%
  $$

- **Precision**:

  $$
  \text{Precision} = \frac{70}{70 + 20} = \frac{70}{90} \approx 0.778 \text{ or } 77.8\%
  $$

- **Recall**:

  $$
  \text{Recall} = \frac{70}{70 + 30} = \frac{70}{100} = 0.7 \text{ or } 70\%
  $$

- **Specificity**:

  $$
  \text{Specificity} = \frac{80}{80 + 20} = \frac{80}{100} = 0.8 \text{ or } 80\%
  $$

- **F1 Score**:

  $$
  \text{F1 Score} = 2 \times \frac{0.778 \times 0.7}{0.778 + 0.7} \approx 2 \times \frac{0.5446}{1.478} \approx 0.736 \text{ or } 73.6\%
  $$

### Receiver Operating Characteristic (ROC) Curve and AUC

The **Receiver Operating Characteristic (ROC) curve** plots the True Positive Rate (Recall) against the False Positive Rate (1 - Specificity) at various threshold settings. It provides a comprehensive view of the model's performance across all classification thresholds.

- **True Positive Rate (TPR)**:

  $$
  \text{TPR} = \text{Recall} = \frac{\text{TP}}{\text{TP} + \text{FN}}
  $$

- **False Positive Rate (FPR)**:

  $$
  \text{FPR} = \frac{\text{FP}}{\text{FP} + \text{TN}}
  $$

The **Area Under the ROC Curve (AUC-ROC)** is a single scalar value summarizing the model's ability to discriminate between positive and negative classes. An AUC of:

- **1.0**: Perfect classifier.
- **0.5**: No discriminative ability (equivalent to random guessing).
- **Less than 0.5**: Worse than random guessing (model may be inverted).

#### Interpretation

- A higher AUC indicates better model performance.
- The ROC curve helps in selecting the optimal threshold that balances sensitivity and specificity.

### Precision-Recall Curve and AUC

In cases of imbalanced datasets, the **Precision-Recall (PR) curve** is more informative than the ROC curve. It plots Precision against Recall for different thresholds.

- The **Area Under the PR Curve (AUC-PR)** provides a summary metric that is sensitive to class imbalance.
- A higher area under the PR curve indicates better performance in identifying the positive class.

# Regression Metrics

Evaluation metrics are crucial in assessing the performance of regression models, which predict a continuous outcome variable based on one or more predictor variables. These metrics quantify the discrepancy between the predicted values and the actual observed values, providing insights into the accuracy and reliability of the model.

## Evaluating Regression Models

In regression analysis, the goal is to build a model that accurately predicts the dependent variable $y $ from one or more independent variables $x $. After fitting a regression model, it is essential to assess its performance using appropriate evaluation metrics. The most commonly used regression metrics include:

- **Mean Absolute Error (MAE)**
- **Mean Squared Error (MSE)**
- **Root Mean Squared Error (RMSE)**
- **Coefficient of Determination ($R^2 $)**

These metrics provide different perspectives on the model's predictive capabilities and can be used to compare different models or to tune model parameters.

## Visualizing Regression Performance

Consider a dataset where we have generated data points from a sine wave with added noise. We fit a linear regression model to this data to predict $y $ based on $x $. The following plot illustrates the data and the fitted regression line:

![Linear Regression on Sine Wave with Noise](https://github.com/djeada/Statistics-Notes/assets/37275728/aaf787b6-9b17-41cc-b1a6-54400b410e1b)

- **Blue Points**: Actual data points (sine wave with noise)
- **Red Line**: Prediction from the linear regression model
- **Gray Dotted Lines**: Errors (residuals) for each data point, connecting the actual value to the predicted value

This visualization helps to understand how well the linear model captures the underlying pattern in the data and highlights the discrepancies between the predictions and actual values.

## Regression Evaluation Metrics

### Mean Absolute Error (MAE)

**Definition**:

The **Mean Absolute Error (MAE)** measures the average magnitude of the errors in a set of predictions, without considering their direction. It is the average over the test sample of the absolute differences between predicted and actual observations.

**Formula**:

$$
\text{MAE} = \frac{1}{n} \sum_{i=1}^{n} | y_i - \hat{y}_i |
$$

Where:

- $n $ is the number of observations
- $y_i $ is the actual value of the dependent variable for the $i $-th observation
- $\hat{y}_i $ is the predicted value for the $i $-th observation

**Interpretation**:

- MAE is in the same units as the dependent variable.
- It provides a linear score, meaning all individual differences are weighted equally.

**Properties**:

- MAE is robust to outliers compared to MSE because it does not square the errors.
- It gives a straightforward measure of average error magnitude.

### Mean Squared Error (MSE)

**Definition**:

The **Mean Squared Error (MSE)** measures the average of the squares of the errors—that is, the average squared difference between the estimated values and the actual value.

**Formula**:

$$
\text{MSE} = \frac{1}{n} \sum_{i=1}^{n} ( y_i - \hat{y}_i )^2
$$

**Interpretation**:

- MSE penalizes larger errors more severely due to squaring the errors.
- It is sensitive to outliers since larger errors have a disproportionate effect.

**Properties**:

- MSE is always non-negative; values closer to zero indicate a better fit.
- It is in squared units of the dependent variable, which can make interpretation less intuitive.

### Root Mean Squared Error (RMSE)

**Definition**:

The **Root Mean Squared Error (RMSE)** is the square root of the MSE. It brings the error metric back to the same units as the dependent variable, making interpretation more intuitive.

**Formula**:

$$
\text{RMSE} = \sqrt{\text{MSE}} = \sqrt{ \frac{1}{n} \sum_{i=1}^{n} ( y_i - \hat{y}_i )^2 }
$$

**Interpretation**:

- RMSE represents the standard deviation of the residuals (prediction errors).
- It indicates how concentrated the data is around the line of best fit.

**Properties**:

- Like MSE, RMSE is sensitive to outliers due to the squaring of errors.
- RMSE is in the same units as the dependent variable.

### Coefficient of Determination ($R^2 $)

**Definition**:

The **Coefficient of Determination**, denoted as $R^2 $, is a statistical measure that represents the proportion of the variance in the dependent variable that is predictable from the independent variables.

**Formula**:

$$
R^2 = 1 - \frac{ \text{SS}_{\text{res}} }{ \text{SS}_{\text{tot}} } = 1 - \frac{ \sum_{i=1}^{n} ( y_i - \hat{y}_i )^2 }{ \sum_{i=1}^{n} ( y_i - \bar{y} )^2 }
$$

Where:

- $\text{SS}_{\text{res}} $ is the residual sum of squares (sum of squared residuals)
- $\text{SS}_{\text{tot}} $ is the total sum of squares (sum of squared deviations from the mean)
- $\bar{y} $ is the mean of the observed data

**Interpretation**:

- $R^2 $ values range from 0 to 1.
- An $R^2 $ of 1 indicates that the regression predictions perfectly fit the data.
- An $R^2 $ of 0 indicates that the model does not explain any of the variability of the response data around its mean.

**Properties**:

- $R^2 $ can also be negative in cases where the model fits the data worse than a horizontal line (mean of the data).
- Higher $R^2 $ values indicate a better fit to the data.

**Note**:

- $R^2 $ alone does not indicate whether a regression model is adequate. It is possible to have a high $R^2 $ value for a model that is inappropriate.
- It does not indicate whether independent variables are a cause of the dependent variable.
- $R^2 $ does not account for the number of predictors in the model. **Adjusted $R^2 $** is used when comparing models with different numbers of predictors.

### Adjusted $R^2 $

**Definition**:

**Adjusted $R^2 $** adjusts the $R^2 $ value based on the number of predictors in the model relative to the number of data points. It penalizes the addition of unnecessary predictors to the model.

**Formula**:

$$
\text{Adjusted } R^2 = 1 - \left( \frac{ (1 - R^2)(n - 1) }{ n - p - 1 } \right)
$$

Where:

- $n $ is the number of observations
- $p $ is the number of predictors (independent variables)

**Interpretation**:

- Adjusted $R^2 $ increases only if the new predictor improves the model more than would be expected by chance.
- It can be used for model selection, especially when comparing models with different numbers of predictors.

## Comparing Regression Metrics

### Sensitivity to Outliers

- **MAE**: Less sensitive to outliers compared to MSE and RMSE because it does not square the errors.
- **MSE/RMSE**: More sensitive to outliers due to the squaring of errors, which amplifies the effect of larger errors.

### Units and Interpretability

- **MAE and RMSE**: Both are in the same units as the dependent variable, making interpretation more intuitive.
- **MSE**: In squared units of the dependent variable, which can be less interpretable.

### Usage in Model Evaluation

- **MAE**: Useful when all errors are equally important and when outliers are not a major concern.
- **MSE/RMSE**: Preferred when large errors are particularly undesirable, and when penalizing larger errors more severely is important.
- **$R^2 $**: Provides a measure of how well the observed outcomes are replicated by the model, relative to the mean of the dependent variable.

## Example Calculation

Let's consider a small dataset:

| $i $ | $x_i $ | $y_i $ | $\hat{y}_i $ |
|---------|-----------|-----------|----------------|
| 1       | 1.0       | 2.0       | 2.5            |
| 2       | 2.0       | 4.0       | 3.8            |
| 3       | 3.0       | 6.0       | 5.9            |
| 4       | 4.0       | 8.0       | 8.2            |
| 5       | 5.0       | 10.0      | 10.1           |

Compute the residuals:

$$
\text{Residuals} = y_i - \hat{y}_i
$$

Compute **MAE**:

$$
\text{MAE} = \frac{1}{5} \left( |2.0 - 2.5| + |4.0 - 3.8| + |6.0 - 5.9| + |8.0 - 8.2| + |10.0 - 10.1| \right) = \frac{1}{5} (0.5 + 0.2 + 0.1 + 0.2 + 0.1) = 0.22
$$

Compute **MSE**:

$$
\text{MSE} = \frac{1}{5} \left( (2.0 - 2.5)^2 + (4.0 - 3.8)^2 + (6.0 - 5.9)^2 + (8.0 - 8.2)^2 + (10.0 - 10.1)^2 \right) = \frac{1}{5} (0.25 + 0.04 + 0.01 + 0.04 + 0.01) = 0.07
$$

Compute **RMSE**:

$$
\text{RMSE} = \sqrt{ \text{MSE} } = \sqrt{0.07} \approx 0.265
$$

Compute $R^2 $:

First, compute the total sum of squares:

$$
\bar{y} = \frac{1}{5} (2.0 + 4.0 + 6.0 + 8.0 + 10.0) = 6.0
$$

$$
\text{SS}_{\text{tot}} = \sum_{i=1}^{5} ( y_i - \bar{y} )^2 = (2.0 - 6.0)^2 + (4.0 - 6.0)^2 + (6.0 - 6.0)^2 + (8.0 - 6.0)^2 + (10.0 - 6.0)^2 = 16 + 4 + 0 + 4 + 16 = 40
$$

Compute the residual sum of squares:

$$
\text{SS}_{\text{res}} = \sum_{i=1}^{5} ( y_i - \hat{y}_i )^2 = 0.25 + 0.04 + 0.01 + 0.04 + 0.01 = 0.35
$$

Compute $R^2 $:

$$
R^2 = 1 - \frac{ \text{SS}_{\text{res}} }{ \text{SS}_{\text{tot}} } = 1 - \frac{0.35}{40} = 1 - 0.00875 = 0.99125
$$

**Interpretation**:

- The model explains approximately 99.125% of the variance in the dependent variable.
- The high $R^2 $ value indicates a strong fit to the data.

## Negative $R^2 $ Values

Although $R^2 $ typically ranges from 0 to 1, it can be negative when the model is worse than simply predicting the mean of the observed data. This can happen if the residual sum of squares is greater than the total sum of squares.

**Example**:

Suppose we have a model that makes poor predictions resulting in a high residual sum of squares:

- $\text{SS}_{\text{res}} = 50 $
- $\text{SS}_{\text{tot}} = 40 $

Compute $R^2 $:

$$
R^2 = 1 - \frac{50}{40} = 1 - 1.25 = -0.25
$$

**Interpretation**:

- A negative $R^2 $ indicates that the model performs worse than a horizontal line at $\bar{y} $.
- It suggests that the model fails to capture the underlying patterns in the data.

## Practical Considerations

- **Model Selection**: Use multiple metrics to evaluate and compare models. No single metric provides a complete picture.
- **Outliers**: Consider the impact of outliers on MSE and RMSE. Outliers can disproportionately affect these metrics.
- **Overfitting**: A very high $R^2 $ does not guarantee that the model generalizes well to new data. Always validate the model on unseen data.
- **Residual Analysis**: Examine residual plots to check assumptions of linearity, homoscedasticity (constant variance), and normality of errors.
- **Adjusted $R^2 $**: Use adjusted $R^2 $ when comparing models with different numbers of predictors to account for model complexity.
