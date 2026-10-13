"""Simulate an AR(2) process and plot its series, ACF, and PACF."""

import matplotlib.pyplot as plt
import numpy as np
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf


def simulate_ar2(n=500, phi1=0.6, phi2=-0.3, seed=42):
    rng = np.random.default_rng(seed)
    noise = rng.normal(0, 1, n)
    data = np.zeros(n)
    for t in range(2, n):
        data[t] = phi1 * data[t - 1] + phi2 * data[t - 2] + noise[t]
    return data


def main():
    data = simulate_ar2()

    plt.figure(figsize=(10, 15))

    plt.subplot(3, 1, 1)
    plt.plot(data, color="black")
    plt.title("Synthetic AR(2) Process Time Series")
    plt.xlabel("Time")
    plt.ylabel("Value")
    plt.grid(True)

    plt.subplot(3, 1, 2)
    plot_acf(data, lags=40, ax=plt.gca(), color="black")
    plt.title("Autocorrelation Function (ACF)")

    plt.subplot(3, 1, 3)
    plot_pacf(data, lags=40, ax=plt.gca(), method="ywm", color="black")
    plt.title("Partial Autocorrelation Function (PACF)")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
