# Resampling and Model Assessment

Repeatedly rearranging or partitioning a dataset can answer several statistical questions. The interpretation comes from what is resampled and what quantity is recalculated. Similar-looking computer loops can estimate a standard error, test a null hypothesis, or assess predictive performance, but those targets require different assumptions.

## Three distinct uses of repeated fitting

A bootstrap draws from an empirical distribution to approximate how an estimator would vary across new samples. A permutation test rearranges values in a way that is valid under a null hypothesis, then compares the observed statistic with the resulting null distribution. Cross-validation fits on one part of the data and evaluates on held-out observations to estimate performance on a specified prediction task.

An ordinary bootstrap requires an appropriate representation of the sampling units. A permutation test requires exchangeability under the null, rather than permission to shuffle arbitrary columns. A validation split requires separation that matches deployment: new rows from familiar subjects and observations from entirely new subjects are different prediction targets.

## Selection is part of training

Scaling, imputation, feature selection, hyperparameter tuning, and threshold choice all use information from data. Fit these steps on training data within each split. If evaluation results influence a modeling choice, those data have become part of selection and no longer provide an untouched assessment of the final choice.

Nested validation separates these roles by using inner folds for selection and outer folds for assessment. A final reserved test set can serve the same purpose when there is enough data and it remains unused until the modeling process is fixed.

## A score needs a target

Regression losses measure different costs of numerical errors. Classification metrics emphasize different combinations of false positives, false negatives, rankings, and probability quality. Compare with simple baselines and report the sample and split strategy alongside the score. Temporal order, spatial proximity, and repeated observations within groups may require structured splits so that evaluation reflects the information available when the model will actually be used.
