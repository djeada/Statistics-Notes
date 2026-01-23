from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    np.random.seed(4)

    n = 60
    t = np.arange(n)
    series = np.cumsum(np.random.normal(0, 1, n)) + 0.15 * np.sin(2 * np.pi * t / 8)

    turning_points = []
    for i in range(1, n - 1):
        if (series[i - 1] < series[i] > series[i + 1]) or (
            series[i - 1] > series[i] < series[i + 1]
        ):
            turning_points.append(i)

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(t, series, color="tab:blue", label="Series")
    ax.scatter(
        t[turning_points],
        series[turning_points],
        color="tab:red",
        zorder=3,
        label="Turning points",
    )
    ax.set_title("Turning Points in a Synthetic Series")
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    ax.grid(True, alpha=0.3)
    ax.legend()

    ax.text(
        0.02,
        0.95,
        f"Count: {len(turning_points)}",
        transform=ax.transAxes,
        ha="left",
        va="top",
        fontsize=10,
        bbox={"facecolor": "white", "alpha": 0.8, "edgecolor": "0.7"},
    )

    output_path = (
        Path(__file__).resolve().parents[2]
        / "notes"
        / "assets"
        / "time_series"
        / "turning_points_example.png"
    )
    fig.tight_layout()
    fig.savefig(output_path, dpi=150)


if __name__ == "__main__":
    main()
