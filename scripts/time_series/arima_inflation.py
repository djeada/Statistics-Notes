"""ARIMA workflow on a seeded synthetic inflation-like price index.

The index is simulated (no live data download): log prices follow a random
walk with drift whose growth rate is an AR(1) process, mimicking monthly CPI.
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller


def simulate_cpi(n=516, seed=42):
    """Monthly CPI-like index from 1980-01: log growth is AR(1) around 0.25%."""
    rng = np.random.default_rng(seed)
    mu, phi, sigma = 0.0025, 0.6, 0.002
    growth = np.zeros(n)
    growth[0] = mu
    for t in range(1, n):
        growth[t] = mu + phi * (growth[t - 1] - mu) + rng.normal(scale=sigma)
    index = pd.date_range("1980-01-01", periods=n, freq="MS")
    return pd.Series(78.0 * np.exp(np.cumsum(growth)), index=index, name="CPI")


def adf_test(series, label):
    result = adfuller(series)
    print(f"ADF test for {label}")
    print("ADF Statistic:", result[0])
    print("p-value:", result[1])
    for key, value in result[4].items():
        print(f"Critical Value ({key}): {value}")


def main():
    cpi = simulate_cpi()

    plt.figure(figsize=(10, 6))
    plt.plot(cpi, label="Synthetic CPI (inflation index)")
    plt.title("Synthetic Consumer Price Index Over Time")
    plt.xlabel("Year")
    plt.ylabel("CPI")
    plt.legend()
    plt.show()

    adf_test(cpi, "CPI level")

    cpi_diff = cpi.diff().dropna()
    plt.figure(figsize=(10, 6))
    plt.plot(cpi_diff, label="Differenced CPI")
    plt.title("Differenced CPI Over Time")
    plt.xlabel("Year")
    plt.ylabel("Differenced CPI")
    plt.legend()
    plt.show()

    adf_test(cpi_diff, "differenced CPI")

    fig, ax = plt.subplots(1, 2, figsize=(16, 6))
    sm.graphics.tsa.plot_acf(cpi_diff, lags=40, ax=ax[0])
    sm.graphics.tsa.plot_pacf(cpi_diff, lags=40, ax=ax[1])
    plt.show()

    fitted = ARIMA(cpi, order=(1, 1, 1)).fit()
    print(fitted.summary())

    forecast = fitted.get_forecast(steps=12)
    mean = forecast.predicted_mean
    ci = forecast.conf_int()

    plt.figure(figsize=(10, 6))
    plt.plot(cpi, label="Historical CPI")
    plt.plot(mean.index, mean, label="Forecasted CPI", color="red")
    plt.fill_between(ci.index, ci.iloc[:, 0], ci.iloc[:, 1], color="pink", alpha=0.3)
    plt.title("CPI Forecast for Next 12 Months")
    plt.xlabel("Year")
    plt.ylabel("CPI")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
