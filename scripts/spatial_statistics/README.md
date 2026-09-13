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

## Design

These scripts implement the important formulas directly with NumPy/SciPy/statsmodels/scikit-learn instead of requiring a specialized GIS stack. That makes the statistical assumptions visible and keeps the examples runnable after a normal `pip install -r requirements.txt`.

For production work, specialized spatial libraries can provide richer geometry handling, projections, sparse weights, formal spatial econometrics, and additional geostatistical or point-process estimators.
