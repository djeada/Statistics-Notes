# Spatial Statistics Scripts

Runnable companions for [`notes/spatial_statistics/`](../../notes/spatial_statistics/README.md).

The examples are ordered to match the redesigned learning path and use only dependencies already listed in `requirements.txt`.

| Script | Main lesson |
|---|---|
| [`spatial_data_and_distance.py`](spatial_data_and_distance.py) | coordinate units, great-circle distance, and change of support |
| [`spatial_weights.py`](spatial_weights.py) | distance-band and k-nearest-neighbor weights, row standardization, spatial lags |
| [`moran_permutation.py`](moran_permutation.py) | global/local Moran statistics and permutation inference |
| [`variogram_and_kriging.py`](variogram_and_kriging.py) | empirical semivariogram, exponential model fit, ordinary kriging, LOO diagnostics |
| [`spatial_regression.py`](spatial_regression.py) | OLS residual dependence and GLS with a known simulation covariance |
| [`point_pattern_analysis.py`](point_pattern_analysis.py) | unconditional Poisson simulation, Thomas clustering, nearest-neighbor distance, border-corrected Ripley K |
| [`spatial_validation.py`](spatial_validation.py) | random vs blocked vs buffered geographic validation |

The student-pack visualization programs generate the figures used in the expanded chapters:

| Visualization script | Main lesson | Figure output |
|---|---|---|
| [`spatial_data_support_distance_visualizations.py`](spatial_data_support_distance_visualizations.py) | spatial objects, support, distance metrics, and boundaries | [`assets/spatial_statistics/data_support_distance/`](../../assets/spatial_statistics/data_support_distance/) |
| [`spatial_weights_visualizations.py`](spatial_weights_visualizations.py) | contiguity, distance bands, \(k\)-NN, islands, and sensitivity | [`assets/spatial_statistics/spatial_weights/`](../../assets/spatial_statistics/spatial_weights/) |
| [`spatial_autocorrelation_visualizations.py`](spatial_autocorrelation_visualizations.py) | Moran's \(I\), Geary's \(C\), local categories, and permutation inference | [`assets/spatial_statistics/spatial_autocorrelation/`](../../assets/spatial_statistics/spatial_autocorrelation/) |
| [`geostatistics_visualizations.py`](geostatistics_visualizations.py) | random fields, empirical variograms, anisotropy, and sampling design | [`assets/spatial_statistics/geostatistics/`](../../assets/spatial_statistics/geostatistics/) |
| [`kriging_visualizations.py`](kriging_visualizations.py) | kriging weights, prediction, uncertainty, nugget behavior, and cross-validation | [`assets/spatial_statistics/kriging/`](../../assets/spatial_statistics/kriging/) |
| [`spatial_regression_visualizations.py`](spatial_regression_visualizations.py) | correlated errors, GLS, SAR impacts, confounding, and transfer | [`assets/spatial_statistics/spatial_regression/`](../../assets/spatial_statistics/spatial_regression/) |
| [`point_process_visualizations.py`](point_process_visualizations.py) | Poisson, clustered, inhibited, and marked point patterns | [`assets/spatial_statistics/point_processes/`](../../assets/spatial_statistics/point_processes/) |
| [`spatial_validation_visualizations.py`](spatial_validation_visualizations.py) | random, blocked, buffered, and region-transfer evaluation | [`assets/spatial_statistics/spatial_validation/`](../../assets/spatial_statistics/spatial_validation/) |

For example:

```bash
python scripts/spatial_statistics/geostatistics_visualizations.py
python scripts/spatial_statistics/kriging_visualizations.py
```

The visualization scripts require only the NumPy and Matplotlib dependencies already listed in `requirements.txt`. They write to the repository's asset directories regardless of the current working directory.

## Design

These scripts implement the important formulas directly with NumPy/SciPy/statsmodels/scikit-learn instead of requiring a specialized GIS stack. That makes the statistical assumptions visible and keeps the examples runnable after a normal `pip install -r requirements.txt`.

For production work, specialized spatial libraries can provide richer geometry handling, projections, sparse weights, formal spatial econometrics, and additional geostatistical or point-process estimators.
