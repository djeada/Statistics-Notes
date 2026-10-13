"""Expanding-window forecast evaluation with simple baselines and AR(1)."""

import numpy as np
from statsmodels.tsa.ar_model import AutoReg


def mae(actual, forecast):
    return float(np.mean(np.abs(actual - forecast)))


def rmse(actual, forecast):
    return float(np.sqrt(np.mean((actual - forecast) ** 2)))


def mase(actual, forecast, scale):
    return float(np.mean(np.abs(actual - forecast)) / scale)


def simulate_ar1(n, phi=0.7, seed=42):
    rng = np.random.default_rng(seed)
    y = np.zeros(n)
    for t in range(1, n):
        y[t] = phi * y[t - 1] + rng.normal(scale=1.0)
    return y


def main():
    y = simulate_ar1(180)
    n = len(y)
    initial_window = 80
    # In-sample naive scale from the initial training window only.
    scale = np.mean(np.abs(np.diff(y[:initial_window])))

    actual, naive_forecast, ar_forecast = [], [], []
    for origin in range(initial_window, n):
        train = y[:origin]
        actual.append(y[origin])
        naive_forecast.append(train[-1])
        model = AutoReg(train, lags=1, trend="c").fit()
        ar_forecast.append(model.predict(start=origin, end=origin)[0])

    actual = np.asarray(actual)
    forecasts = {
        "Naive": np.asarray(naive_forecast),
        "AR(1)": np.asarray(ar_forecast),
    }
    for name, forecast in forecasts.items():
        print(
            f"{name:6s}  "
            f"MAE={mae(actual, forecast):.3f}  "
            f"RMSE={rmse(actual, forecast):.3f}  "
            f"MASE={mase(actual, forecast, scale):.3f}"
        )


if __name__ == "__main__":
    main()
