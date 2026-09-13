# Spatial Validation

Spatial prediction performance depends strongly on **where the test locations are relative to the training locations**.

Random train/test splits often answer an interpolation question: can the model predict a location whose nearby neighbors are already represented in training? A geographically separated holdout answers a different and often harder question.

## Match Validation to Deployment

Three common targets are:

### Interpolation

Predict inside the sampled region with nearby training observations.

Random folds may sometimes approximate this task, although dependence between train and test observations can still make uncertainty estimates optimistic.

### Spatial transfer

Predict in a contiguous region not used for training.

Use spatial blocks or leave-region-out validation.

### Extrapolation beyond observed conditions

Predict in a new region whose covariates or spatial process differ from the training domain.

No resampling design can manufacture evidence for unsupported extrapolation. Validation must include genuinely representative transfer regions if this is the deployment target.

## Spatial Blocks

Partition the study region into geographic blocks and hold out entire blocks.

The block size should reflect the spatial dependence scale and the intended deployment distance. Tiny blocks can leave test observations almost adjacent to training observations, defeating the purpose.

## Buffers

A **buffered** split removes training observations within distance $b$ of the test region.

This creates explicit separation between train and test sets and can be useful when the goal is prediction away from observed sites.

The script [`spatial_validation.py`](../../scripts/spatial_statistics/spatial_validation.py) compares:

- shuffled random folds;
- contiguous spatial blocks;
- buffered spatial blocks.

## Leakage Can Be Spatial

Spatial leakage is not limited to the split itself.

Examples include:

- computing a neighborhood feature using future/test observations;
- interpolating a covariate using the full dataset before splitting;
- selecting a bandwidth or variogram model using test locations;
- normalizing or imputing with information from held-out regions;
- using a spatial aggregate that contains the target observation.

All data-dependent preprocessing must be constructed using only the training information available for that fold.

## Cross-Validation for Kriging

Leave-one-out kriging often tests short-distance interpolation because each omitted site remains surrounded by other sites.

For a mapping task this may be appropriate. For prediction in a new geographic zone, use blocked or buffered holdouts and refit the variogram/covariance model inside each training fold when model-selection bias matters.

## Comparing Validation Schemes

Do not ask which validation design is “most correct” in the abstract.

Instead ask:

> Which design most closely reproduces the spatial separation and information availability expected at deployment?

It is often useful to report more than one scheme because they answer different questions.

## Uncertainty of the Performance Estimate

Spatial folds are themselves dependent and often few in number. A mean RMSE across five regions does not imply the same precision as five independent experimental replicates.

Report fold-level performance and inspect geographic variation rather than relying only on a single average.

## Final Test Region

When tuning hyperparameters, selecting covariance families, or choosing block size using cross-validation, reserve a final geographic test region if the dataset is large enough.

The same principle from ordinary model assessment applies: model selection and final evaluation should not use the same information.
