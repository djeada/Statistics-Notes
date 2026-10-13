"""Simple exponential smoothing on a seeded synthetic inflation-like price index.

The index is simulated (no live data download): log growth is AR(1) around
0.25% per month, mimicking monthly CPI.
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def simulate_cpi(n=516, seed=42):
    """Monthly CPI-like index from 1980-01: log growth is AR(1) around 0.25%."""
    rng = np.random.default_rng(seed)
    mu, phi, sigma = 0.0025, 0.6, 0.002
    growth = np.zeros(n)
    growth[0] = mu
    for t in range(1, n):
        growth[t] = mu + phi * (growth[t - 1] - mu) + rng.normal(scale=sigma)
    index = pd.date_range("1980-01-01", periods=n, freq="MS")
    return pd.DataFrame({"CPIAUCSL": 78.0 * np.exp(np.cumsum(growth))}, index=index)


# Define SES forecast function
def ses_forecast(data, alpha):
    forecast_values = [data[0]]  # First forecast is the first data point
    for i in range(1, len(data)):
        forecast = alpha * data[i-1] + (1 - alpha) * forecast_values[i-1]
        forecast_values.append(forecast)
    return forecast_values

# Define SSE calculation
def calculate_sse(data, forecast_values):
    # forecast_values[i] predicts data[i]; the first one is the seed value
    return np.sum((data[1:] - np.asarray(forecast_values)[1:]) ** 2)


def main() -> None:
    cpi_data = simulate_cpi()

    # Plot original data
    plt.figure(figsize=(10,6))
    plt.plot(cpi_data, label='Synthetic CPI')
    plt.title('Synthetic CPI Data (monthly, 43 years)')
    plt.xlabel('Year')
    plt.ylabel('CPI')
    plt.show()

    # Calculate SES for a given alpha
    alpha = 0.2
    forecast_values = ses_forecast(cpi_data['CPIAUCSL'].values, alpha)

    # Plot SES with alpha=0.2
    plt.figure(figsize=(10,6))
    plt.plot(cpi_data.index, cpi_data, label='Original Data')
    plt.plot(cpi_data.index, forecast_values, label=f'SES Forecast (alpha={alpha})', color='red')
    plt.title('SES Forecast for CPI Data')
    plt.legend()
    plt.show()

    # Find optimal alpha by minimizing SSE
    alpha_values = np.linspace(0.001, 0.999, 100)
    sse_values = []
    for alpha in alpha_values:
        forecast_values = ses_forecast(cpi_data['CPIAUCSL'].values, alpha)
        sse = calculate_sse(cpi_data['CPIAUCSL'].values, forecast_values)
        sse_values.append(sse)

    # Plot SSE vs Alpha
    plt.figure(figsize=(10,6))
    plt.plot(alpha_values, sse_values, color='purple')
    plt.title('SSE vs Alpha for SES')
    plt.xlabel('Alpha')
    plt.ylabel('Sum of Squared Errors (SSE)')
    plt.show()

    # Find the optimal alpha
    optimal_alpha = alpha_values[np.argmin(sse_values)]
    print(f"Optimal Alpha: {optimal_alpha}")

    # Calculate forecast with optimal alpha
    optimal_forecast = ses_forecast(cpi_data['CPIAUCSL'].values, optimal_alpha)

    # Plot forecast with optimal alpha
    plt.figure(figsize=(10,6))
    plt.plot(cpi_data.index, cpi_data, label='Original Data')
    plt.plot(cpi_data.index, optimal_forecast, label=f'Optimal SES Forecast (alpha={optimal_alpha})', color='green')
    plt.title('SES Forecast with Optimal Alpha for CPI Data')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
