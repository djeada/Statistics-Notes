# Validation and Model Selection

A fitted model is optimized using observed data. Model assessment asks a different question: how well will the modeling procedure perform on new data generated under comparable conditions?

## Training, Validation, and Test Data

A basic workflow separates data into roles:

- **training data** are used to estimate model parameters;
- **validation data** are used to compare candidate models or tune hyperparameters;
- **test data** are reserved for a final assessment after modeling choices have been made.

Using the test set repeatedly during model development turns it into another validation set and makes the reported performance optimistic.

## Cross-Validation

When data are limited, $K$-fold cross-validation reuses observations efficiently. The data are partitioned into $K$ folds. Each fold is held out in turn, the model is fitted on the remaining folds, and performance is evaluated on the held-out fold.

The resulting scores estimate how the **modeling procedure** performs when refit on similar data. They are not independent repeated experiments, so small differences between models should not automatically be overinterpreted.

## Hyperparameter Tuning

If hyperparameters are chosen using cross-validation, the same cross-validation scores are part of the selection process. Reporting the best tuning score as if it were an unbiased final estimate can be optimistic.

A cleaner strategy is **nested cross-validation**:

1. an inner loop selects hyperparameters;
2. an outer loop evaluates the entire selection-and-fitting procedure on data not used by the inner loop.

## Data Leakage

Leakage occurs when information unavailable at prediction time influences model fitting or preprocessing. Common examples include:

- scaling all observations before splitting into folds;
- selecting features using the complete dataset before cross-validation;
- imputing missing values using statistics computed from future or held-out observations;
- tuning thresholds using the final test set;
- randomly shuffling time-series observations when future values contain information about the past split.

Preprocessing should be fitted inside the same training partition as the model.

## Choosing a Metric

No metric is universally best. The choice depends on the task and error costs.

For regression, common metrics include MAE, MSE/RMSE, and $R^2$. For classification, common choices include accuracy, precision, recall, F-scores, ROC-AUC, log loss, and calibration measures.

The detailed formulas and examples are collected in **[Metrics](metrics.md)**.

## Baselines

A model should be compared with a simple reference. Examples include predicting the sample mean in regression, the majority class in classification, or a seasonal-naive forecast in time series.

A complicated model that cannot outperform an appropriate simple baseline has not demonstrated useful predictive value.

## Model Selection vs Scientific Interpretation

The model with the best predictive score is not automatically the most interpretable, scientifically meaningful, or causally valid model. Prediction, explanation, and causal inference are different goals and can favor different modeling choices.

## Time-Ordered and Spatial Data

Ordinary random cross-validation assumes observations are exchangeable enough that shuffling does not destroy the data-generating structure. That assumption is often wrong for dependent data.

For time series, use forward-chaining, rolling-origin, or expanding-window evaluation. For spatial data, consider spatial blocking or other schemes that respect spatial dependence when the goal is prediction at new locations.

Continue to **[Metrics](metrics.md)** and then to the dependent-data units if relevant.
