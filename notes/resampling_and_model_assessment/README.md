# Resampling & Model Assessment

This unit separates two ideas that are often mixed together: using resampling to approximate uncertainty, and using held-out data to estimate predictive performance.

## Reading Order

1. **[Resampling](resampling.md)** — bootstrap and permutation ideas for approximating sampling behavior or null distributions.
2. **[Validation and Model Selection](validation_and_model_selection.md)** — train/test splits, cross-validation, leakage, tuning, and nested evaluation.
3. **[Metrics](metrics.md)** — regression and classification metrics and the questions each metric answers.

## Resampling for Inference vs Resampling for Prediction

The same computational pattern can serve different goals:

- a **bootstrap** often approximates an estimator's sampling distribution or standard error;
- a **permutation test** approximates a null distribution under an exchangeability assumption;
- **cross-validation** estimates predictive performance on data not used to fit a model;
- **nested cross-validation** separates model/tuning selection from final performance estimation.

Keeping the target clear prevents a resampling procedure from being interpreted as evidence for a different question than the one it actually estimates.

## Model Assessment Principles

- Evaluate performance on observations not used to fit or tune the model.
- Match the metric to the decision or scientific goal.
- Treat preprocessing and feature selection as part of the fitted pipeline to avoid leakage.
- Compare against simple baselines.
- Report uncertainty or variability in evaluation when possible.
- For time-ordered data, do not use shuffled validation schemes that leak future information into the past.

## Next

For independent observations, this completes the main modeling loop. Continue to **[Time Series](../time_series/README.md)** or **[Spatial Statistics](../spatial_statistics/README.md)** when dependence is structured by time or location.
