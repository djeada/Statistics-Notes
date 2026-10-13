# Spatial Statistics Notebooks

Interactive companions for [`notes/spatial_statistics/`](../../notes/spatial_statistics/README.md).

Recommended order:

1. [`01_spatial_structure.ipynb`](01_spatial_structure.ipynb) — weights, spatial lags, Moran's I, and permutation inference.
2. [`02_variograms_and_kriging.ipynb`](02_variograms_and_kriging.ipynb) — empirical semivariograms, model fitting, prediction, and kriging variance.
3. [`03_spatial_regression.ipynb`](03_spatial_regression.ipynb) — residual spatial dependence and covariance-aware regression.
4. [`04_point_patterns.ipynb`](04_point_patterns.ipynb) — Poisson vs clustered patterns, nearest-neighbor behavior, and Ripley's K.
5. [`05_spatial_validation.ipynb`](05_spatial_validation.ipynb) — random, blocked, and buffered validation designs.

## Per-note notebooks

Each note also has a shorter companion notebook of the same name:
[`spatial_data_and_distance`](spatial_data_and_distance.ipynb),
[`spatial_weights`](spatial_weights.ipynb),
[`spatial_autocorrelation`](spatial_autocorrelation.ipynb),
[`geostatistics`](geostatistics.ipynb),
[`kriging`](kriging.ipynb),
[`spatial_regression`](spatial_regression.ipynb),
[`point_processes`](point_processes.ipynb), and
[`spatial_validation`](spatial_validation.ipynb).

The notebooks are intentionally self-contained so that the statistical machinery can be inspected and modified without requiring GeoPandas, PySAL, or PyKrige.
