# Spatial Statistics

Spatial statistics studies observations whose dependence is structured by location. This unit comes after the core probability, covariance, inference, regression, and model-assessment material because spatial dependence changes how ordinary independent-sample reasoning should be applied.

## Choose by Data Type

| Spatial data | Start here | Typical question |
|---|---|---|
| Locations of events themselves | **[Point Processes](point_processes.md)** | Are events clustered, inhibited, or consistent with a reference point process? |
| Measurements attached to regions or neighboring units | **[Spatial Autocorrelation](spatial_autocorrelation.md)** | Are nearby areas more similar than expected under spatial randomness? |
| A continuous quantity observed at sampled coordinates | **[Geostatistics](geostatistics.md)** | How does similarity change with distance, and how can values be interpolated? |

## Prerequisites and Connections

- **[Joint Distributions & Covariance](../joint_distributions_and_covariance/README.md)** provides covariance and correlation concepts.
- **[Regression](../regression/README.md)** provides the conditional-modeling perspective used by many spatial models.
- **[Resampling & Model Assessment](../resampling_and_model_assessment/README.md)** is important because random validation can be optimistic when nearby observations are strongly dependent.
- **[Time Series](../time_series/README.md)** is the temporal analogue: both fields model structured dependence rather than exchangeable observations.

## Terminology Boundary

Do not use “spatial autocorrelation,” “geostatistics,” and “point process” interchangeably. They can all describe spatial structure, but they model different data objects and answer different questions. Identifying the observed spatial object is the first modeling decision.

## Model Assessment

Prediction at unsampled locations may require spatially blocked validation rather than random folds. The validation design should mimic the actual prediction task: interpolation near observed locations is different from extrapolation to a new region.
