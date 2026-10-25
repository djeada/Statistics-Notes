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

The training size in each ordinary $K$-fold fit is about $n(K-1)/K$, so its score describes a procedure trained on that amount of data rather than exactly the eventual all-data fit. Fold scores are dependent because their training sets overlap. Their standard deviation describes variation across the chosen folds; dividing it by $\sqrt K$ does not automatically yield a valid standard error for generalization performance.

If folds have different sizes, aggregate additive losses by observation count or pool the held-out predictions before calculating the loss. Nonlinear metrics, such as F1 or $R^2$, can differ between an average of fold scores and a score on pooled predictions. State which summary is used.

## Hyperparameter Tuning

If hyperparameters are chosen using cross-validation, the same cross-validation scores are part of the selection process. Reporting the best tuning score as if it were an unbiased final estimate can be optimistic.

A cleaner strategy is **nested cross-validation**:

1. an inner loop selects hyperparameters;
2. an outer loop evaluates the entire selection-and-fitting procedure on data not used by the inner loop.

Every outer training set runs the complete inner search independently. Its selected hyperparameters are then used to refit on that outer training set and predict the outer test fold. The outer score assesses the procedure including selection, rather than only one hyperparameter combination. After assessment, one can repeat the prespecified selection process on all development data to train a final model. Looking at outer scores and repeatedly redesigning the search makes the outer layer part of development, so further independent assessment may be needed.

## Data Leakage

Leakage occurs when information unavailable at prediction time influences model fitting or preprocessing. Common examples include:

- scaling all observations before splitting into folds;
- selecting features using the complete dataset before cross-validation;
- imputing missing values using statistics computed from future or held-out observations;
- tuning thresholds using the final test set;
- randomly shuffling time-series observations so that the model is trained on the future and evaluated on the past.

Preprocessing should be fitted inside the same training partition as the model.

For example, in one cross-validation fold, compute an imputation median using only that fold's training rows. Use that stored median to transform both the training and held-out rows, then fit and score the model. Repeat the imputation fit in the next fold. Feature selection using the response is especially prone to leakage: selecting correlated columns on the full dataset allows held-out outcomes to influence which model is evaluated. A fitted pipeline makes these dependencies explicit.

## Choosing a Metric

No metric is universally best. The choice depends on the task and error costs.

For regression, common metrics include MAE, MSE/RMSE, and $R^2$. For classification, common choices include accuracy, precision, recall, F-scores, ROC-AUC, log loss, and calibration measures.

The detailed formulas and examples are collected in **[Metrics](https://github.com/djeada/Statistics-Notes/blob/main/notes/resampling_and_model_assessment/metrics.md)**. Bootstrap-based assessment is covered in **[Resampling](https://github.com/djeada/Statistics-Notes/blob/main/notes/resampling_and_model_assessment/resampling.md)**.

## Baselines

A model should be compared with a simple reference fitted using the same training information. Examples include a training-sample mean for squared-error regression, a training-sample median for absolute-error regression, the training majority class for accuracy, and a seasonal-naive forecast. Computing a baseline from held-out outcomes would give it information unavailable at deployment and would no longer represent a usable forecasting rule.

A complicated model that cannot outperform an appropriate simple baseline has not demonstrated useful predictive value.

## Model Selection vs Scientific Interpretation

The model with the best predictive score is not automatically the most interpretable, scientifically meaningful, or causally valid model. Prediction, explanation, and causal inference are different goals and can favor different modeling choices.

## Time-Ordered and Spatial Data

Ordinary random cross-validation assumes observations are exchangeable enough that shuffling does not destroy the data-generating structure. That assumption is often wrong for dependent data.

For time series, use forward-chaining, rolling-origin, or expanding-window evaluation. For spatial data, consider spatial blocking or other schemes that respect spatial dependence when the goal is prediction at new locations.

Repeated measurements require the same attention to the target. Holding out individual visits estimates prediction for additional visits when information about the same subjects is available. Holding out entire subjects estimates transfer to previously unseen subjects. Spatial blocks and time-forward splits make analogous distinctions. Choose the split first from the intended use, then compare candidate models on identical partitions and metrics.


## Report the Procedure Behind the Score

A reviewable assessment identifies the target population, independent sampling unit, prediction horizon or separation, split sizes, preprocessing, selection search, metric, and baseline. Include variability across appropriate repetitions or uncertainty estimates when feasible, while recognizing that repeated folds do not create independent datasets. Investigate whether performance differs across relevant groups or regions; an acceptable average can hide a poor result for a small but important subgroup.
