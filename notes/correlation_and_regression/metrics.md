# Evaluation Metrics

Evaluation metrics are used to assess the performance of machine learning models, especially for classification and regression tasks. They help to understand how well the model is predicting and provide insights for model improvement.

## Classification Metrics

### Confusion Matrix

A confusion matrix is a table that is used to describe the performance of a classification model on a set of data for which the true values are known. The confusion matrix consists of four elements:

- True Positive (TP): The number of correct positive predictions
- True Negative (TN): The number of correct negative predictions
- False Positive (FP): The number of incorrect positive predictions
- False Negative (FN): The number of incorrect negative predictions

### Accuracy

Accuracy is the proportion of correctly classified instances out of the total instances:

$$
\text{Accuracy} = \frac{\text{TP} + \text{TN}}{\text{TP} + \text{TN} + \text{FP} + \text{FN}}
$$

### Precision

Precision is the proportion of true positive predictions among all positive predictions:

$$
\text{Precision} = \frac{\text{TP}}{\text{TP} + \text{FP}}
$$

### Recall (Sensitivity)

Recall is the proportion of true positive predictions among all actual positive instances:

$$
\text{Recall} = \frac{\text{TP}}{\text{TP} + \text{FN}}
$$

### Intuitive explanation

Suppose you are tasked with picking apples from an orchard, but you must avoid picking oranges. In this scenario, apples represent relevant items, and oranges represent irrelevant items.

* **Recall**: Recall measures the proportion of apples you managed to pick out of all the apples in the orchard. Imagine you picked 90 apples out of a total of 100 apples in the orchard. In this case, your recall would be 90% (you picked 90 out of the 100 available apples).

* **Precision**: Precision measures the proportion of apples you picked out of all the fruits you picked (both apples and oranges). Let's say you picked a total of 120 fruits, including the 90 apples and 30 oranges by mistake. In this case, your precision would be 75% (you picked 90 apples out of the 120 total fruits you picked).

### Specificity

Specificity is the proportion of true negative predictions among all actual negative instances:

$$
\text{Specificity} = \frac{\text{TN}}{\text{TN} + \text{FP}}
$$

### F1 Score

F1 Score is the harmonic mean of precision and recall:

$$
\text{F1 Score} = 2 * \frac{\text{Precision} * \text{Recall}}{\text{Precision} + \text{Recall}}
$$

### Area Under the Receiver Operating Characteristic (ROC) Curve (AUC-ROC)

AUC-ROC is a performance measurement for classification problems at various thresholds settings. It represents the model's ability to discriminate between positive and negative classes. An AUC-ROC close to 1 indicates a good model, while an AUC-ROC close to 0.5 indicates a random classifier.

## Regression Metrics

### Mean Absolute Error (MAE)

Mean Absolute Error is the average of the absolute differences between the predicted and actual values:

$$
\text{MAE} = \frac{1}{n} \sum_{i=1}^n |y_i - \hat{y}_i|
$$

### Mean Squared Error (MSE)

Mean Squared Error is the average of the squared differences between the predicted and actual values:

$$
\text{MSE} = \frac{1}{n} \sum_{i=1}^n (y_i - \hat{y}_i)^2
$$

### Root Mean Squared Error (RMSE)

Root Mean Squared Error is the square root of the mean squared error:

$$
\text{RMSE} = \sqrt{\frac{1}{n} \sum_{i=1}^n (y_i - \hat{y}_i)^2}
$$

### Coefficient of Determination (R²)

R-Squared (R²) is a metric for assessing the performance of regression machine learning models. Unlike other metrics such as Mean Absolute Error (MAE) or Root Mean Squared Error (RMSE), R² is not a measure of prediction accuracy, but rather a measure of how well the model fits the data. The R² score gives an indication of how much of the variation in the dependent variable is explained by the independent variables in the model.

The R² score can be calculated using the following formula:

$$
R² = 1 - \frac{\sum_{i=1}^n (y_i - \hat{y}_i)^2}{\sum_{i=1}^n (y_i - \bar{y})^2}
$$

Where:

- $y_i$ is the actual value of the dependent variable for the $i$-th observation
- $\hat{y}_i$ is the predicted value of the dependent variable for the $i$-th observation
- $\bar{y}$ is the mean value of the dependent variable

The R² score ranges from 1 to negative values for under-performing models:

- A score of 1 is the perfect score, indicating that all the variance in the dependent variable is explained by the independent variables.
- A score of 0 indicates that the independent variables don't explain any of the variance in the dependent variable.
- A negative score below 0 indicates that the independent variables aren't explaining the variance and are actually contributing negatively to the model's fit.

It is important to remember that R² scores from different models cannot be directly compared, as the variance found in a dataset is not comparable across datasets.

