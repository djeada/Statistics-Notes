"""VAR, Granger predictability, Johansen cointegration, and VECM example."""

import numpy as np
import pandas as pd
from statsmodels.tsa.api import VAR
from statsmodels.tsa.vector_ar.vecm import VECM, coint_johansen

rng = np.random.default_rng(11)
n = 350
x = np.cumsum(rng.normal(size=n))
stationary_spread = np.zeros(n)
for t in range(1, n):
    stationary_spread[t] = 0.6 * stationary_spread[t - 1] + rng.normal(scale=0.5)
y = 1.25 * x + stationary_spread

levels = pd.DataFrame({"x": x, "y": y})
differences = levels.diff().dropna().rename(columns={"x": "dx", "y": "dy"})

var_result = VAR(differences).fit(1)
print(var_result.summary())
print(var_result.test_causality("dy", ["dx"], kind="f").summary())

johansen = coint_johansen(levels, det_order=0, k_ar_diff=1)
print("\nJohansen trace statistics:", johansen.lr1)
print("95% critical values:", johansen.cvt[:, 1])

vecm = VECM(levels, k_ar_diff=1, coint_rank=1, deterministic="co").fit()
print("\nEstimated cointegrating vector (beta):")
print(vecm.beta)
print("Adjustment coefficients (alpha):")
print(vecm.alpha)
