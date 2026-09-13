from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    np.random.seed(11)

    n = 240
    t = np.arange(n)
    trend = 0.02 * t + 0.0003 * (t - 120) ** 2
    seasonal = 1.5 * np.sin(2 * np.pi * t / 24)
    high_freq = 0.6 * np.sin(2 * np.pi * t / 4)
    noise = np.random.normal(0, 0.5, n)
    series = trend + seasonal + high_freq + noise

    freqs = np.fft.rfftfreq(n, d=1.0)
    spectrum = np.fft.rfft(series)
    cutoff = 0.08
    filtered = spectrum.copy()
    filtered[freqs > cutoff] = 0
    smooth = np.fft.irfft(filtered, n=n)

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(t, series, color="0.35", alpha=0.7, label="Series")
    ax.plot(t, smooth, color="tab:purple", linewidth=2, label="Low-pass smoothed")
    ax.set_title("Spectral Smoothing (Low-Pass Filter)")
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    ax.grid(True, alpha=0.3)
    ax.legend()

    output_path = (
        Path(__file__).resolve().parents[2]
        / "notes"
        / "assets"
        / "time_series"
        / "spectral_smoothing.png"
    )
    fig.tight_layout()
    fig.savefig(output_path, dpi=150)


if __name__ == "__main__":
    main()
