"""Expanding-window forecast evaluation with simple baselines and AR(1)."""

import numpy as np
from statsmodels.tsa.ar_model import AutoReg


def mae(actual, forecast):
    return float(np.mean(np.abs(actual - forecast)))


def rmse(actual, forecast):
    return float(np.sqrt(np.mean((actual - forecast) ** 2)))


def mase(actual, forecast, scale):
    return float(np.mean(np.abs(actual - forecast)) / scale)


rng = np.random.default_rng(42)
n = 180
y = np.zeros(n)
for t in range(1, n):
    y[t] = 0.7 * y[t - 1] + rng.normal(scale=1.0)

initial_window = 80
scale = np.mean(np.abs(np.diff(y[:initial_window])))
actual = []
naive_forecast = []
ar_forecast = []

for origin in range(initial_window, n):
    train = y[:origin]
    actual.append(y[origin])
    naive_forecast.append(train[-1])

    model = AutoReg(train, lags=1, trend="c", old_names=False).fit()
    ar_forecast.append(model.predict(start=origin, end=origin)[0])

actual = np.asarray(actual)
naive_forecast = np.asarray(naive_forecast)
ar_forecast = np.asarray(ar_forecast)

for name, forecast in {"Naive": naive_forecast, "AR(1)": ar_forecast}.items():
    print(
        f"{name:6s}  "
        f"MAE={mae(actual, forecast):.3f}  "
        f"RMSE={rmse(actual, forecast):.3f}  "
        f"MASE={mase(actual, forecast, scale):.3f}"
    )
