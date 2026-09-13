"""Identify dominant periods in a simulated series with a periodogram."""

import numpy as np
from scipy.signal import periodogram

rng = np.random.default_rng(9)
n = 360
t = np.arange(n)
series = (
    2.0 * np.sin(2 * np.pi * t / 12)
    + 1.2 * np.sin(2 * np.pi * t / 30)
    + rng.normal(scale=1.0, size=n)
)

frequency, power = periodogram(series, detrend="linear")
positive = frequency > 0
frequency = frequency[positive]
power = power[positive]

indices = np.argsort(power)[-5:][::-1]
print("Strongest periodogram peaks:")
for index in indices:
    print(
        f"frequency={frequency[index]:.4f} cycles/sample, "
        f"period={1 / frequency[index]:.2f} samples, "
        f"power={power[index]:.2f}"
    )
