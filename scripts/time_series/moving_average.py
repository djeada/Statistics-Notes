"""Simulate an MA(2) process and plot its sample autocovariance and ACF."""

import matplotlib.pyplot as plt
import numpy as np


def simulate_ma(n=1000, beta=(1.0, 0.5, 0.3), seed=42):
    rng = np.random.default_rng(seed)
    q = len(beta) - 1
    white_noise = rng.normal(0, 1, n + q)
    return np.convolve(white_noise, beta, mode="valid")


def sample_autocovariance(x, max_lag=50):
    """Biased sample autocovariance for lags -max_lag..max_lag."""
    x = x - x.mean()
    n = len(x)
    full = np.correlate(x, x, mode="full") / n
    return np.arange(-max_lag, max_lag + 1), full[n - 1 - max_lag:n + max_lag]


def main():
    ma_process = simulate_ma()
    lags, autocovariance = sample_autocovariance(ma_process)
    autocorrelation = autocovariance / autocovariance[len(lags) // 2]

    plt.figure(figsize=(12, 10))

    plt.subplot(3, 1, 1)
    plt.plot(ma_process, label="MA(2) Process", color="black")
    plt.title("Moving Average (MA) Process Time Series")
    plt.xlabel("Time")
    plt.ylabel("Value")
    plt.grid(True)
    plt.legend()

    plt.subplot(3, 1, 2)
    plt.stem(lags, autocovariance, linefmt="black", markerfmt="o", basefmt=" ")
    plt.title("Autocovariance Function")
    plt.xlabel("Lag")
    plt.ylabel(r"$\gamma(k)$")
    plt.grid(True)

    plt.subplot(3, 1, 3)
    plt.stem(lags, autocorrelation, linefmt="black", markerfmt="o", basefmt=" ")
    plt.title("Autocorrelation Function")
    plt.xlabel("Lag")
    plt.ylabel(r"$\rho(k)$")
    plt.grid(True)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
