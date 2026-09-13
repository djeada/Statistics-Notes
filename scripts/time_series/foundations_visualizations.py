"""Foundations visualizations for the time-series student notes.

The script calculates the examples directly and prints the values used in
the chapter explanations.  It writes eight figures to
assets/time_series/foundations/.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from student_plot_utils import output_dir, save_figure


FIGURE_DIR = output_dir("foundations")


def geometric_series() -> None:
    r = 0.5
    powers = np.arange(16)
    partial = np.cumsum(r**powers)
    limit = 1.0 / (1.0 - r)
    print(
        f"geometric series: S_4={partial[4]:.6f}, "
        f"S_15={partial[-1]:.6f}, limit={limit:.6f}, "
        f"tail after S_4={limit - partial[4]:.6f}"
    )

    plt.figure(figsize=(8, 4))
    plt.plot(powers, partial, marker="o", label="partial sum")
    plt.axhline(limit, color="tab:red", linestyle="--", label="infinite sum")
    plt.xlabel("largest included power")
    plt.ylabel("sum")
    plt.title("A convergent geometric series")
    plt.legend()
    save_figure(FIGURE_DIR, "01_geometric_series.png")


def difference_equations() -> None:
    n = 50
    t = np.arange(n)
    cases = {
        "stable: phi=0.7": 0.7**t,
        "alternating: phi=-0.7": (-0.7) ** t,
        "unit root: phi=1": np.ones(n),
        "explosive: phi=1.03": 1.03**t,
    }
    for label, values in cases.items():
        print(f"difference equation: {label}, value at t=10={values[10]:.6f}")

    plt.figure(figsize=(9, 4))
    for label, values in cases.items():
        plt.plot(t, values, label=label)
    plt.axhline(0, color="0.35", linewidth=0.8)
    plt.xlabel("t")
    plt.ylabel("deviation from equilibrium")
    plt.title("The coefficient controls the solution of x_t = phi x_(t-1)")
    plt.legend(ncol=2)
    save_figure(FIGURE_DIR, "02_difference_equation_stability.png")


def components() -> None:
    rng = np.random.default_rng(202)
    n = 180
    t = np.arange(n)
    trend = 0.035 * t
    seasonal = 2.5 * np.sin(2 * np.pi * t / 12)
    noise = rng.normal(scale=0.7, size=n)
    series = 10 + trend + seasonal + noise
    print(
        f"components: y_6={series[6]:.4f}; deterministic y_6="
        f"{10 + trend[6] + seasonal[6]:.4f}; noise_6={noise[6]:.4f}"
    )

    fig, axes = plt.subplots(4, 1, figsize=(9, 8), sharex=True)
    for ax, values, title in zip(
        axes,
        [series, trend + 10, seasonal, noise],
        ["observed series", "level plus trend", "seasonal component", "irregular component"],
    ):
        ax.plot(values)
        ax.set_title(title)
    axes[-1].set_xlabel("t")
    save_figure(FIGURE_DIR, "03_series_components.png")


def moments() -> None:
    rng = np.random.default_rng(203)
    n = 240
    stable = 10 + rng.normal(scale=0.6, size=n)
    changing_mean = 8 + 0.02 * np.arange(n) + rng.normal(scale=0.6, size=n)
    changing_variance = 10 + rng.normal(
        scale=np.where(np.arange(n) < n // 2, 0.5, 1.8), size=n
    )
    print(
        "moments: stable mean/variance="
        f"{stable.mean():.3f}/{stable.var():.3f}; "
        "changing-mean first/last means="
        f"{changing_mean[:80].mean():.3f}/{changing_mean[-80:].mean():.3f}; "
        "changing-variance first/last variances="
        f"{changing_variance[:120].var():.3f}/{changing_variance[-120:].var():.3f}"
    )

    fig, axes = plt.subplots(3, 1, figsize=(9, 7), sharex=True)
    axes[0].plot(stable)
    axes[0].set_title("Approximately constant mean and variance")
    axes[1].plot(changing_mean)
    axes[1].set_title("Changing mean")
    axes[2].plot(changing_variance)
    axes[2].set_title("Changing variance")
    axes[-1].set_xlabel("t")
    save_figure(FIGURE_DIR, "04_moments_change_over_time.png")


def white_noise_and_random_walk() -> None:
    rng = np.random.default_rng(204)
    n = 220
    shocks = rng.normal(size=n)
    walk = np.cumsum(shocks)
    windows = [25, 50, 100, 200]
    print(
        "random walk variance benchmark: theoretical Var(X_t-X_0)=t "
        + ", ".join(f"{window}:{window:.1f}" for window in windows)
    )

    fig, axes = plt.subplots(2, 1, figsize=(9, 6), sharex=True)
    axes[0].plot(shocks, color="tab:blue")
    axes[0].axhline(0, color="0.35", linewidth=0.8)
    axes[0].set_title("White-noise increments")
    axes[1].plot(walk, color="tab:orange")
    axes[1].set_title("The accumulated random walk")
    axes[1].set_xlabel("t")
    save_figure(FIGURE_DIR, "05_white_noise_random_walk.png")


def stationarity_cases() -> None:
    rng = np.random.default_rng(205)
    n = 180
    stationary = np.zeros(n)
    unit_root = np.zeros(n)
    explosive = np.zeros(n)
    shocks = rng.normal(size=(3, n))
    for t in range(1, n):
        stationary[t] = 0.7 * stationary[t - 1] + shocks[0, t]
        unit_root[t] = unit_root[t - 1] + shocks[1, t]
        explosive[t] = 1.02 * explosive[t - 1] + shocks[2, t]
    print("stationarity condition for AR(1): |phi| < 1")

    fig, axes = plt.subplots(3, 1, figsize=(9, 7), sharex=True)
    for ax, values, title in zip(
        axes,
        [stationary, unit_root, explosive],
        ["stationary, phi=0.7", "unit root, phi=1", "explosive, phi=1.02"],
    ):
        ax.plot(values)
        ax.set_title(title)
    axes[-1].set_xlabel("t")
    save_figure(FIGURE_DIR, "06_stationarity_cases.png")


def observations_and_sampling() -> None:
    fine_t = np.linspace(0, 10, 1000)
    signal = np.sin(2 * np.pi * 0.18 * fine_t)
    regular_t = np.arange(0, 10.01, 0.5)
    regular_values = np.sin(2 * np.pi * 0.18 * regular_t)
    irregular_t = np.sort(np.random.default_rng(206).uniform(0, 10, 22))
    irregular_values = np.sin(2 * np.pi * 0.18 * irregular_t)
    print(
        f"sampling: regular observations={len(regular_t)}, "
        f"irregular observations={len(irregular_t)}, "
        f"first regular value={regular_values[0]:.3f}"
    )

    plt.figure(figsize=(9, 4))
    plt.plot(fine_t, signal, color="0.7", label="underlying signal")
    plt.scatter(regular_t, regular_values, label="regular sampling")
    plt.scatter(irregular_t, irregular_values, marker="x", label="irregular sampling")
    plt.xlabel("time")
    plt.ylabel("value")
    plt.title("A time series is a measurement process as well as a vector of values")
    plt.legend()
    save_figure(FIGURE_DIR, "07_regular_and_irregular_sampling.png")


def linear_filter() -> None:
    rng = np.random.default_rng(207)
    n = 180
    t = np.arange(n)
    series = 0.03 * t + np.sin(2 * np.pi * t / 18) + rng.normal(scale=0.7, size=n)
    window = 9
    weights = np.ones(window) / window
    smoothed = np.convolve(series, weights, mode="same")
    print(f"linear filter: nine-point weights sum to {weights.sum():.1f}")

    plt.figure(figsize=(9, 4))
    plt.plot(series, color="0.65", label="series")
    plt.plot(smoothed, color="tab:red", linewidth=2, label="nine-point average")
    plt.xlabel("t")
    plt.ylabel("value")
    plt.title("A moving average is a linear filter")
    plt.legend()
    save_figure(FIGURE_DIR, "08_linear_filter.png")


def main() -> None:
    geometric_series()
    difference_equations()
    components()
    moments()
    white_noise_and_random_walk()
    stationarity_cases()
    observations_and_sampling()
    linear_filter()


if __name__ == "__main__":
    main()
