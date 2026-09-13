"""ARIMA, differencing, and seasonal-pattern visualizations."""

import matplotlib.pyplot as plt
import numpy as np

from student_plot_utils import acf, output_dir, save_figure, stem


FIGURE_DIR = output_dir("arima_seasonality")


def ordinary_and_seasonal_differences() -> None:
    rng = np.random.default_rng(401)
    n = 180
    t = np.arange(n)
    series = (
        40
        + 0.08 * t
        + 5 * np.sin(2 * np.pi * t / 12)
        + rng.normal(scale=0.8, size=n)
    )
    first = np.diff(series)
    seasonal = series[12:] - series[:-12]
    combined = np.diff(seasonal)
    print(
        f"differencing: original length={len(series)}, first={len(first)}, "
        f"seasonal={len(seasonal)}, combined={len(combined)}; "
        f"first observation={series[0]:.3f}"
    )

    fig, axes = plt.subplots(2, 2, figsize=(10, 6))
    axes[0, 0].plot(series)
    axes[0, 0].set_title("trend plus seasonality")
    axes[0, 1].plot(first)
    axes[0, 1].set_title("ordinary difference")
    axes[1, 0].plot(seasonal)
    axes[1, 0].set_title("seasonal difference, lag 12")
    axes[1, 1].plot(combined)
    axes[1, 1].set_title("ordinary plus seasonal difference")
    save_figure(FIGURE_DIR, "01_differencing_orders.png")


def additive_and_multiplicative() -> None:
    rng = np.random.default_rng(402)
    t = np.arange(144)
    additive = 50 + 0.1 * t + 6 * np.sin(2 * np.pi * t / 12) + rng.normal(
        scale=1.0, size=len(t)
    )
    multiplicative = (50 + 0.1 * t) * (
        1 + 0.12 * np.sin(2 * np.pi * t / 12)
    ) + rng.normal(scale=1.0, size=len(t))
    print(
        f"seasonality: additive peak-to-trough={additive[:12].max()-additive[:12].min():.3f}; "
        f"multiplicative peak-to-trough first/last="
        f"{multiplicative[:12].max()-multiplicative[:12].min():.3f}/"
        f"{multiplicative[-12:].max()-multiplicative[-12:].min():.3f}"
    )

    fig, axes = plt.subplots(2, 1, figsize=(9, 6), sharex=True)
    axes[0].plot(additive)
    axes[0].set_title("Additive seasonality: stable absolute amplitude")
    axes[1].plot(multiplicative)
    axes[1].set_title("Multiplicative seasonality: amplitude grows with level")
    axes[-1].set_xlabel("t")
    save_figure(FIGURE_DIR, "02_additive_multiplicative_seasonality.png")


def decomposition() -> None:
    rng = np.random.default_rng(403)
    n = 156
    t = np.arange(n)
    trend = 20 + 0.08 * t
    seasonal = 4 * np.sin(2 * np.pi * t / 12)
    remainder = rng.normal(scale=0.7, size=n)
    series = trend + seasonal + remainder
    window = 12
    smooth = np.convolve(series, np.ones(window) / window, mode="same")
    centered = series - smooth
    print(
        f"decomposition: t=24 trend={trend[24]:.3f}, seasonal={seasonal[24]:.3f}, "
        f"remainder={remainder[24]:.3f}, series={series[24]:.3f}"
    )

    fig, axes = plt.subplots(4, 1, figsize=(9, 8), sharex=True)
    for ax, values, title in zip(
        axes,
        [series, smooth, seasonal, remainder],
        ["observed", "12-point moving average", "known seasonal component", "irregular remainder"],
    ):
        ax.plot(values)
        ax.set_title(title)
    axes[-1].set_xlabel("t")
    save_figure(FIGURE_DIR, "03_additive_decomposition.png")


def acf_after_differencing() -> None:
    rng = np.random.default_rng(404)
    n = 260
    random_walk = np.cumsum(rng.normal(size=n))
    stationary = np.diff(random_walk)
    level_acf = acf(random_walk, 20)
    difference_acf = acf(stationary, 20)
    print(
        f"ACF after differencing: level rho_1={level_acf[1]:.4f}; "
        f"difference rho_1={difference_acf[1]:.4f}"
    )

    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    stem(axes[0], level_acf, "random-walk level ACF")
    stem(axes[1], difference_acf, "first-difference ACF", "tab:orange")
    save_figure(FIGURE_DIR, "04_acf_before_after_differencing.png")


def over_differencing() -> None:
    rng = np.random.default_rng(405)
    stationary = 0.7 * rng.normal(size=180) + rng.normal(size=180)
    first = np.diff(stationary)
    second = np.diff(first)
    values = [acf(stationary, 12), acf(first, 12), acf(second, 12)]
    print(
        f"over-differencing: lag-1 ACF original/first/second="
        f"{values[0][1]:.4f}/{values[1][1]:.4f}/{values[2][1]:.4f}"
    )

    fig, axes = plt.subplots(1, 3, figsize=(12, 4))
    for ax, acf_values, title in zip(
        axes,
        values,
        ["stationary series", "one difference", "two differences"],
    ):
        stem(ax, acf_values, title)
    save_figure(FIGURE_DIR, "05_over_differencing.png")


def arima_forecasts() -> None:
    rng = np.random.default_rng(406)
    n = 150
    differences = rng.normal(scale=0.8, size=n)
    levels = 20 + np.cumsum(differences)
    origin = 120
    history = levels[:origin]
    horizons = np.arange(1, 25)
    drift = np.mean(np.diff(history[-40:]))
    forecast = history[-1] + drift * horizons
    forecast_sd = 0.8 * np.sqrt(horizons)
    future = levels[origin : origin + len(horizons)]
    print(
        f"ARIMA-style forecast: estimated drift={drift:.4f}; "
        f"h=1 forecast={forecast[0]:.3f}; h=24 forecast={forecast[-1]:.3f}"
    )

    index = np.arange(origin + len(horizons))
    plt.figure(figsize=(9, 4))
    plt.plot(np.arange(origin), history, color="0.35", label="history")
    plt.plot(index[origin:], future, color="black", label="future")
    plt.plot(index[origin:], forecast, color="tab:blue", label="forecast")
    plt.fill_between(
        index[origin:],
        forecast - 1.96 * forecast_sd,
        forecast + 1.96 * forecast_sd,
        color="tab:blue",
        alpha=0.18,
        label="approx. 95% interval",
    )
    plt.axvline(origin - 0.5, color="0.4", linestyle=":")
    plt.title("Differenced model forecasts return to the level scale")
    plt.xlabel("t")
    plt.ylabel("level")
    plt.legend()
    save_figure(FIGURE_DIR, "06_arima_level_forecast.png")


def seasonal_naive() -> None:
    rng = np.random.default_rng(407)
    n = 180
    t = np.arange(n)
    series = 50 + 0.1 * t + 8 * np.sin(2 * np.pi * t / 12) + rng.normal(
        scale=1.0, size=n
    )
    origin = 144
    horizon = np.arange(1, 25)
    forecast = series[origin - 12 + (horizon - 1) % 12]
    actual = series[origin : origin + len(horizon)]
    print(
        f"seasonal naive: first forecast={forecast[0]:.3f}; "
        f"MAE over 24 months={np.mean(np.abs(actual-forecast)):.3f}"
    )

    plt.figure(figsize=(9, 4))
    plt.plot(np.arange(origin), series[:origin], label="history")
    plt.plot(np.arange(origin, origin + len(horizon)), actual, label="actual")
    plt.plot(np.arange(origin, origin + len(horizon)), forecast, label="seasonal naive")
    plt.axvline(origin - 0.5, color="0.4", linestyle=":")
    plt.title("Seasonal naive forecasts reuse the latest complete cycle")
    plt.xlabel("t")
    plt.ylabel("value")
    plt.legend()
    save_figure(FIGURE_DIR, "07_seasonal_naive_forecast.png")


def model_order_grid() -> None:
    rng = np.random.default_rng(408)
    values = 0.6 * np.sin(2 * np.pi * np.arange(100) / 12) + rng.normal(
        scale=0.7, size=100
    )
    candidate_orders = [(0, 0, 0), (1, 0, 0), (0, 0, 1), (1, 0, 1), (2, 0, 1)]
    scores = []
    n = len(values)
    for p, d, q in candidate_orders:
        parameters = p + q + 1
        residual_variance = np.var(values) / (1 + 0.12 * p + 0.08 * q)
        log_likelihood = -0.5 * n * np.log(2 * np.pi * residual_variance) - n / 2
        scores.append(-2 * log_likelihood + 2 * parameters)
    print(
        "candidate order AIC: "
        + ", ".join(f"{order}={score:.2f}" for order, score in zip(candidate_orders, scores))
    )

    plt.figure(figsize=(8, 4))
    labels = [str(order) for order in candidate_orders]
    plt.bar(labels, scores, color="tab:purple")
    plt.ylabel("illustrative AIC")
    plt.title("Order selection balances fit and parameter count")
    save_figure(FIGURE_DIR, "08_model_order_selection.png")


def main() -> None:
    ordinary_and_seasonal_differences()
    additive_and_multiplicative()
    decomposition()
    acf_after_differencing()
    over_differencing()
    arima_forecasts()
    seasonal_naive()
    model_order_grid()


if __name__ == "__main__":
    main()
