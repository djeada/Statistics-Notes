from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    np.random.seed(7)

    n = 160
    t = np.arange(n)
    trend = 0.04 * t + 0.0008 * (t - 80) ** 2
    seasonal = 2.2 * np.sin(2 * np.pi * t / 12)
    noise = np.random.normal(0, 0.9, n)
    series = trend + seasonal + noise

    window = 13
    ma_weights = np.ones(window) / window
    moving_avg = np.convolve(series, ma_weights, mode="same")

    spencer_weights = np.array(
        [-3, -6, -5, 3, 21, 46, 67, 74, 67, 46, 21, 3, -5, -6, -3],
        dtype=float,
    ) / 320
    spencer = np.convolve(series, spencer_weights, mode="same")

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(t, series, color="0.35", alpha=0.7, label="Series")
    ax.plot(t, moving_avg, color="tab:blue", linewidth=2, label="13-point moving average")
    ax.plot(t, spencer, color="tab:orange", linewidth=2, label="Spencer 15-point")
    ax.set_title("Trend Smoothing with Linear Filters")
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    ax.grid(True, alpha=0.3)
    ax.legend()

    output_path = (
        Path(__file__).resolve().parents[2]
        / "notes"
        / "assets"
        / "time_series"
        / "trend_smoothing_filters.png"
    )
    fig.tight_layout()
    fig.savefig(output_path, dpi=150)


if __name__ == "__main__":
    main()
