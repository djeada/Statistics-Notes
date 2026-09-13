# Spatial Statistics

Spatial statistics studies data for which **location, distance, neighborhood, or spatial support are part of the data-generating structure**. Ordinary methods often treat observations as exchangeable after conditioning on predictors; spatial methods make the remaining dependence explicit.

This unit comes after covariance, regression, and model assessment because spatial dependence changes both the model and the way uncertainty and validation should be handled.

## Learning Path

1. **[Spatial Data, Support, and Distance](spatial_data_and_distance.md)** — identify the spatial object, coordinate system, support, scale, and distance metric before modeling.
2. **[Spatial Weights and Spatial Lags](spatial_weights.md)** — encode neighborhood structure for areal or irregular observations.
3. **[Spatial Autocorrelation](spatial_autocorrelation.md)** — global and local dependence summaries, permutation inference, and multiple-testing cautions.
4. **[Geostatistics](geostatistics.md)** — random fields, stationarity, covariance, empirical variograms, anisotropy, nugget, sill, and range.
5. **[Kriging](kriging.md)** — spatial prediction from a covariance/variogram model, including uncertainty and cross-validation.
6. **[Spatial Regression](spatial_regression.md)** — regression when residual dependence remains after modeling the mean.
7. **[Point Processes](point_processes.md)** — intensity and interaction when the event locations themselves are random.
8. **[Spatial Validation](spatial_validation.md)** — random folds, spatial blocks, buffers, interpolation, extrapolation, and leakage.

## Choose the Model by the Spatial Object

| Data object | Example | Main representation | Typical tools |
|---|---|---|---|
| Areal / lattice observations | disease rate by district | regions + neighbor graph | spatial weights, Moran's I, SAR/SEM ideas |
| Point-referenced measurements | soil pH sampled at coordinates | coordinates + measured value | covariance, variogram, kriging, spatial regression |
| Point pattern | tree or crime-event locations | event coordinates, possibly marks | intensity, nearest-neighbor summaries, Ripley's K |
| Raster / gridded field | temperature grid | values on cells | random fields, covariance, convolution/spectral tools |

A point-referenced measurement and a point pattern are not the same object. In the first case, locations are usually treated as sampling sites and the **measured value** is modeled. In the second, the **locations themselves** are the random outcome.

## Core Distinctions

- **Coordinate reference system vs distance metric:** longitude/latitude are angular coordinates; Euclidean distance in degrees is usually not a meaningful physical distance.
- **Location vs support:** a value may represent a point, pixel, polygon average, or other spatial support.
- **First-order vs second-order structure:** mean/intensity variation can create apparent clustering; dependence should not be inferred before modeling broad spatial trend.
- **Weights vs covariance:** a spatial weights matrix encodes a neighborhood graph; a covariance function models stochastic dependence as a function of separation.
- **Interpolation vs extrapolation:** predicting inside a sampled region is easier than transferring to a geographically separated region.
- **Association vs causation:** spatial clustering or spatial regression coefficients do not by themselves identify causal effects.

## Code Companions

Runnable examples are in [`scripts/spatial_statistics/`](../../scripts/spatial_statistics/README.md), and interactive companions are in [`notebooks/spatial_statistics/`](../../notebooks/spatial_statistics/README.md).

The code uses the repository's existing NumPy/SciPy/statsmodels/scikit-learn stack and implements the core formulas directly. This keeps the examples reproducible without requiring a separate GIS environment. Production spatial analysis often uses specialized libraries such as PySAL, GeoPandas, PyKrige, GSTools, or `spatstat`, but software should not hide the statistical object being modeled.

## Recommended Workflow

1. Define the spatial object and prediction/inference target.
2. Inspect coordinates, support, scale, and potential boundary effects.
3. Model broad mean/intensity structure before interpreting local dependence.
4. Choose either a neighborhood representation, covariance model, or point-process model appropriate to the data object.
5. Diagnose residual spatial structure.
6. Quantify uncertainty with assumptions stated explicitly.
7. Validate with a split that matches the intended geographic deployment task.
