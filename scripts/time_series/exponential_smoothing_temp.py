"""Holt-Winters exponential smoothing on a synthetic monthly temperature series."""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing


def simulate_temperature(years=5, seed=42):
    """Trend + annual seasonality + noise, indexed by month end."""
    rng = np.random.default_rng(seed)
    months_per_year = 12
    total_months = years * months_per_year
    index = pd.date_range(start="2015-01-01", periods=total_months, freq="ME")
    trend = 10 + 0.5 * np.arange(total_months)
    phase = 2 * np.pi * np.arange(months_per_year) / months_per_year
    seasonal = np.tile(5 * np.sin(phase), years)
    noise = rng.normal(0, 1, total_months)
    return pd.Series(trend + seasonal + noise, index=index)


def main():
    temperature = simulate_temperature()

    model = ExponentialSmoothing(
        temperature, trend="additive", seasonal="additive", seasonal_periods=12
    )
    fit = model.fit()
    forecast = fit.forecast(24)
    print(f"alpha={fit.params['smoothing_level']:.3f}, "
          f"beta={fit.params['smoothing_trend']:.3f}, "
          f"gamma={fit.params['smoothing_seasonal']:.3f}")
    print(f"first forecast values: {np.round(forecast.values[:3], 2)}")

    plt.figure(figsize=(12, 5))
    plt.plot(temperature, label="Actual temperature", color="blue")
    plt.plot(forecast, label="Forecast", color="green", linestyle="dashed")
    plt.title("Temperature series and Holt-Winters forecast")
    plt.xlabel("Date")
    plt.ylabel("Temperature (Celsius)")
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
