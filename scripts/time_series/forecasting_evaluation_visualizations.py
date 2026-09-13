"""Forecasting, uncertainty, and temporal validation visualizations."""

import matplotlib.pyplot as plt
import numpy as np

from student_plot_utils import output_dir, save_figure, simulate_ar1


FIGURE_DIR = output_dir("forecasting")


def baseline_comparison() -> None:
    rng = np.random.default_rng(501)
    n = 190
    t = np.arange(n)
    values = 20 + 0.04 * t + 2 * np.sin(2 * np.pi * t / 12) + rng.normal(
        scale=0.8, size=n
    )
    origin = 140
    horizon = np.arange(1, 25)
    naive = np.repeat(values[origin - 1], len(horizon))
    drift = values[origin - 1] + horizon * (
        values[origin - 1] - values[0]
    ) / (origin - 1)
    seasonal = values[origin - 12 + (horizon - 1) % 12]
    actual = values[origin : origin + len(horizon)]
    print(
        "baseline MAE: "
        f"naive={np.mean(np.abs(actual-naive)):.3f}, "
        f"drift={np.mean(np.abs(actual-drift)):.3f}, "
        f"seasonal-naive={np.mean(np.abs(actual-seasonal)):.3f}"
    )

    plt.figure(figsize=(9, 4))
    plt.plot(np.arange(origin), values[:origin], color="0.35", label="history")
    future_t = np.arange(origin, origin + len(horizon))
    plt.plot(future_t, actual, color="black", label="actual")
    plt.plot(future_t, naive, label="naive")
    plt.plot(future_t, drift, label="drift")
    plt.plot(future_t, seasonal, label="seasonal naive")
    plt.axvline(origin - 0.5, color="0.4", linestyle=":")
    plt.title("Forecast baselines define the standard to beat")
    plt.xlabel("t")
    plt.ylabel("value")
    plt.legend(ncol=2)
    save_figure(FIGURE_DIR, "01_baseline_forecasts.png")


def rolling_origins() -> None:
    n = 170
    initial = 80
    horizon = 3
    origins = [initial, initial + 20, initial + 40, initial + 60]
    print(
        "rolling origins: "
        + ", ".join(f"origin {origin} trains on 0:{origin}" for origin in origins)
    )

    fig, ax = plt.subplots(figsize=(9, 4))
    for row, origin in enumerate(origins):
        ax.plot([0, origin], [row, row], linewidth=8, solid_capstyle="butt")
        ax.plot(
            [origin, origin + horizon],
            [row, row],
            linewidth=8,
            color="tab:orange",
            solid_capstyle="butt",
        )
        ax.text(2, row + 0.12, f"origin {origin}", fontsize=9)
    ax.set_xlim(0, n)
    ax.set_yticks([])
    ax.set_xlabel("time")
    ax.set_title("Expanding-window rolling-origin evaluation")
    ax.text(12, -0.45, "training history", color="tab:blue")
    ax.text(104, -0.45, "forecast horizon", color="tab:orange")
    save_figure(FIGURE_DIR, "02_rolling_origins.png")


def point_metrics() -> None:
    actual = np.array([10.0, 12.0, 9.0, 15.0, 11.0])
    forecasts = {
        "model A": np.array([9.0, 11.0, 10.0, 14.0, 12.0]),
        "model B": np.array([10.0, 10.0, 10.0, 10.0, 10.0]),
    }
    scores = {}
    for name, forecast in forecasts.items():
        errors = actual - forecast
        scores[name] = {
            "MAE": np.mean(np.abs(errors)),
            "RMSE": np.sqrt(np.mean(errors**2)),
        }
        print(
            f"{name}: errors={errors}, MAE={scores[name]['MAE']:.3f}, "
            f"RMSE={scores[name]['RMSE']:.3f}"
        )

    names = list(forecasts)
    metrics = ["MAE", "RMSE"]
    x = np.arange(len(names))
    width = 0.35
    plt.figure(figsize=(8, 4))
    for i, metric in enumerate(metrics):
        plt.bar(
            x + (i - 0.5) * width,
            [scores[name][metric] for name in names],
            width,
            label=metric,
        )
    plt.xticks(x, names)
    plt.ylabel("error")
    plt.title("MAE and RMSE emphasize different aspects of error")
    plt.legend()
    save_figure(FIGURE_DIR, "03_point_metrics.png")


def interval_coverage() -> None:
    rng = np.random.default_rng(502)
    actual = rng.normal(size=40)
    center = actual + rng.normal(scale=0.55, size=40)
    lower = center - 1.96 * 0.7
    upper = center + 1.96 * 0.7
    covered = (actual >= lower) & (actual <= upper)
    coverage = covered.mean()
    width = np.mean(upper - lower)
    print(f"intervals: empirical coverage={coverage:.3f}, average width={width:.3f}")

    order = np.arange(len(actual))
    plt.figure(figsize=(9, 4))
    for i, inside in enumerate(covered):
        color = "tab:blue" if inside else "tab:red"
        plt.plot([order[i], order[i]], [lower[i], upper[i]], color=color)
        plt.scatter(order[i], actual[i], color=color, s=18)
    plt.plot(order, center, color="0.25", linewidth=1, label="point forecast")
    plt.xlabel("forecast case")
    plt.ylabel("value")
    plt.title("Prediction intervals: coverage and width")
    plt.legend()
    save_figure(FIGURE_DIR, "04_interval_coverage.png")


def horizon_error() -> None:
    rng = np.random.default_rng(503)
    n = 240
    values = simulate_ar1(rng, 0.8, n)
    horizons = np.arange(1, 13)
    errors = []
    for horizon in horizons:
        origins = np.arange(100, n - horizon)
        predictions = values[origins - 1] * 0.8**horizon
        errors.append(np.sqrt(np.mean((values[origins + horizon] - predictions) ** 2)))
    print(
        "horizon RMSE: "
        + ", ".join(f"h={h}:{error:.3f}" for h, error in zip(horizons[:4], errors[:4]))
    )

    plt.figure(figsize=(8, 4))
    plt.plot(horizons, errors, marker="o")
    plt.xlabel("forecast horizon")
    plt.ylabel("RMSE")
    plt.title("Forecast error generally grows with horizon")
    save_figure(FIGURE_DIR, "05_error_by_horizon.png")


def exponential_smoothing() -> None:
    rng = np.random.default_rng(504)
    n = 160
    t = np.arange(n)
    values = 20 + 0.04 * t + rng.normal(scale=1.0, size=n)
    alphas = [0.15, 0.55, 0.9]
    forecasts = {}
    for alpha in alphas:
        level = values[0]
        fitted = np.empty(n)
        fitted[0] = level
        for i in range(1, n):
            fitted[i] = level
            level = alpha * values[i] + (1 - alpha) * level
        forecasts[alpha] = fitted
        print(f"SES alpha={alpha}: final level={level:.3f}")

    plt.figure(figsize=(9, 4))
    plt.plot(values, color="0.6", label="observed")
    for alpha, fitted in forecasts.items():
        plt.plot(fitted, label=f"alpha={alpha}")
    plt.xlabel("t")
    plt.ylabel("value")
    plt.title("The smoothing parameter controls responsiveness")
    plt.legend()
    save_figure(FIGURE_DIR, "06_exponential_smoothing.png")


def leakage() -> None:
    rng = np.random.default_rng(505)
    n = 160
    values = np.cumsum(rng.normal(size=n))
    origins = np.arange(80, 140)
    safe = []
    leaked = []
    for origin in origins:
        safe.append(values[origin - 1] - values[:origin].mean())
        leaked.append(values[origin - 1] - values.mean())
    print(
        f"leakage example: first safe feature={safe[0]:.3f}; "
        f"first full-data feature={leaked[0]:.3f}"
    )

    plt.figure(figsize=(9, 4))
    plt.plot(origins, safe, label="feature computed through origin")
    plt.plot(origins, leaked, label="feature using full data", linestyle="--")
    plt.xlabel("forecast origin")
    plt.ylabel("feature value")
    plt.title("Future-aware preprocessing changes the information set")
    plt.legend()
    save_figure(FIGURE_DIR, "07_temporal_leakage.png")


def forecast_error_over_time() -> None:
    rng = np.random.default_rng(506)
    n = 200
    values = simulate_ar1(rng, 0.7, n)
    origins = np.arange(80, n)
    actual = values[origins]
    naive_error = actual - values[origins - 1]
    ar_error = actual - 0.7 * values[origins - 1]
    print(
        f"error stability: naive mean error={naive_error.mean():.4f}; "
        f"AR mean error={ar_error.mean():.4f}"
    )

    plt.figure(figsize=(9, 4))
    plt.plot(origins, naive_error, label="naive error")
    plt.plot(origins, ar_error, label="AR error")
    plt.axhline(0, color="0.35", linewidth=0.8)
    plt.xlabel("forecast origin")
    plt.ylabel("actual - forecast")
    plt.title("Inspect forecast errors over time, not only their average")
    plt.legend()
    save_figure(FIGURE_DIR, "08_forecast_errors_over_time.png")


def main() -> None:
    baseline_comparison()
    rolling_origins()
    point_metrics()
    interval_coverage()
    horizon_error()
    exponential_smoothing()
    leakage()
    forecast_error_over_time()


if __name__ == "__main__":
    main()
