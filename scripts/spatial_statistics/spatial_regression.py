"""Regression with spatially correlated errors: OLS diagnosis and GLS illustration."""

from __future__ import annotations

import numpy as np
import statsmodels.api as sm
from scipy.spatial.distance import cdist

from moran_permutation import moran_i
from spatial_weights import knn_weights, row_standardize


def simulate_spatial_regression(n=180, seed=1):
    rng = np.random.default_rng(seed)
    coordinates = rng.uniform(0.0, 1.0, size=(n, 2))
    predictor = rng.normal(size=n)

    distances = cdist(coordinates, coordinates)
    spatial_covariance = 0.8 * np.exp(-distances / 0.18)
    covariance = spatial_covariance + 0.25 * np.eye(n)

    error = rng.multivariate_normal(np.zeros(n), covariance)
    response = 1.0 + 2.0 * predictor + error

    design = sm.add_constant(predictor)
    return coordinates, design, response, covariance


def main():
    coordinates, design, response, covariance = simulate_spatial_regression()

    ols = sm.OLS(response, design).fit()
    gls = sm.GLS(response, design, sigma=covariance).fit()

    weights = row_standardize(knn_weights(coordinates, k=6))
    residual_moran = moran_i(ols.resid, weights)

    print("True coefficients: [1.0, 2.0]")
    print("OLS estimates:     ", np.round(ols.params, 3))
    print("OLS std. errors:   ", np.round(ols.bse, 3))
    print("GLS estimates:     ", np.round(gls.params, 3))
    print("GLS std. errors:   ", np.round(gls.bse, 3))
    print(f"Moran's I of OLS residuals: {residual_moran:.3f}")
    print(
        "\nGLS uses the known covariance here only to isolate the lesson: "
        "spatial dependence changes uncertainty and efficiency. In practice "
        "the covariance model must be estimated or otherwise justified."
    )


if __name__ == "__main__":
    main()
