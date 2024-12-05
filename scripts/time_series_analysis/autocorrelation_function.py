import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import acf, pacf

# Function to generate time series
def generate_ar1(phi, n=100):
    series = [np.random.normal()]
    for t in range(1, n):
        series.append(phi * series[-1] + np.random.normal())
    return np.array(series)

def generate_ar2(phi1, phi2, n=100):
    series = [np.random.normal(), np.random.normal()]
    for t in range(2, n):
        series.append(phi1 * series[-1] + phi2 * series[-2] + np.random.normal())
    return np.array(series)

def generate_ma1(theta, n=100):
    series = np.random.normal(size=n)
    return series + theta * np.roll(series, 1)

def generate_ma2(theta1, theta2, n=100):
    series = np.random.normal(size=n)
    return series + theta1 * np.roll(series, 1) + theta2 * np.roll(series, 2)

def generate_linear(n=100):
    return np.arange(n)

def generate_constant(value, n=100):
    return np.full(n, value)

def generate_sine_with_noise(n=100):
    return np.sin(np.linspace(0, 4 * np.pi, n)) + np.random.normal(scale=0.1, size=n)

def generate_white_noise(n=100):
    return np.random.normal(size=n)

# Generate all time series
types = [
    ("AR(1)", generate_ar1(0.5)),
    ("AR(2)", generate_ar2(0.5, -0.25)),
    ("MA(1)", generate_ma1(0.5)),
    ("MA(2)", generate_ma2(0.5, 0.3)),
    ("Linear Growing", generate_linear()),
    ("Constant", generate_constant(10)),
    ("Sine with Noise", generate_sine_with_noise()),
    ("White Noise", generate_white_noise())
]

# Set up the plot
n_rows = len(types)
fig, axes = plt.subplots(n_rows, 3, figsize=(15, 3 * n_rows))
fig.suptitle("Time Series, ACF, and PACF", fontsize=16)
plt.subplots_adjust(hspace=0.5)

# Plot each type with error handling
for i, (title, series) in enumerate(types):
    # Time series plot
    axes[i, 0].plot(series)
    axes[i, 0].set_title(f"{title} - Time Series")
    
    # ACF plot with error handling
    try:
        acf_vals = acf(series, nlags=20)
        axes[i, 1].stem(acf_vals, use_line_collection=True)
        axes[i, 1].set_title(f"{title} - ACF")
    except Exception as e:
        axes[i, 1].text(0.5, 0.5, f"ACF Error: {e}", ha='center', va='center')
        axes[i, 1].set_title(f"{title} - ACF (Error)")

    # PACF plot with error handling
    try:
        pacf_vals = pacf(series, nlags=20)
        axes[i, 2].stem(pacf_vals, use_line_collection=True)
        axes[i, 2].set_title(f"{title} - PACF")
    except Exception as e:
        axes[i, 2].text(0.5, 0.5, f"PACF Error: {e}", ha='center', va='center')
        axes[i, 2].set_title(f"{title} - PACF (Error)")

# Show the plot
plt.show()
