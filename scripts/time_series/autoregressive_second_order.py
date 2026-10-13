"""Simulate an AR(2) series, fit it with AutoReg, and plot fitted values."""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from statsmodels.tsa.ar_model import AutoReg


def simulate_ar2(n=100, alpha=3.0, beta1=0.6, beta2=-0.2, seed=42):
    rng = np.random.default_rng(seed)
    x = [10.0, 5.0]  # X_0 and X_1
    for t in range(2, n):
        x.append(alpha + beta1 * x[t - 1] + beta2 * x[t - 2] + rng.normal())
    return pd.Series(x)


def main():
    n = 100
    series = simulate_ar2(n=n)

    fit = AutoReg(series, lags=2).fit()
    print(fit.params)
    predictions = fit.predict(start=2, end=n - 1)

    plt.figure(figsize=(12, 6))
    plt.plot(series, label="Generated Data", color="blue")
    plt.plot(predictions, label="AR(2) Predictions", color="red", linestyle="dashed")
    plt.title("Generated Time Series and AR(2) Model Predictions")
    plt.xlabel("Time Point")
    plt.ylabel("Value")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
