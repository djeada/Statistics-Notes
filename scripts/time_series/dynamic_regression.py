"""Regression with an exogenous predictor and AR(1) errors."""

import numpy as np
import statsmodels.api as sm
from statsmodels.stats.diagnostic import acorr_ljungbox
from statsmodels.tsa.statespace.sarimax import SARIMAX

rng = np.random.default_rng(7)
n = 250
x = rng.normal(size=n)
error = np.zeros(n)
for t in range(1, n):
    error[t] = 0.8 * error[t - 1] + rng.normal(scale=0.7)

y = 2.0 + 1.5 * x + error

ols = sm.OLS(y, sm.add_constant(x)).fit()
dynamic = SARIMAX(y, exog=x, order=(1, 0, 0), trend="c").fit(disp=False)

print("OLS coefficients:")
print(ols.params)
print("\nDynamic-regression parameters:")
print(dynamic.params)

ols_lb = acorr_ljungbox(ols.resid, lags=[10], return_df=True)
dyn_lb = acorr_ljungbox(dynamic.resid, lags=[10], return_df=True)
print("\nLjung-Box p-value at lag 10")
print(f"OLS residuals:     {ols_lb['lb_pvalue'].iloc[0]:.4f}")
print(f"Dynamic residuals: {dyn_lb['lb_pvalue'].iloc[0]:.4f}")
