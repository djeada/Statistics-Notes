#!/usr/bin/env python3
"""
Generate synthetic time series plots inspired by course examples.
The outputs are intentionally not one-to-one copies of any original figures.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Callable, List

import numpy as np
import matplotlib.pyplot as plt


@dataclass
class PlotSpec:
    name: str
    title: str
    make: Callable[[np.random.Generator], np.ndarray]
    annotate: Callable[[plt.Axes, np.ndarray], None] | None = None


def moving_average(x: np.ndarray, window: int) -> np.ndarray:
    if window <= 1:
        return x.copy()
    kernel = np.ones(window) / window
    return np.convolve(x, kernel, mode="same")


def acf(x: np.ndarray, max_lag: int) -> np.ndarray:
    x = np.asarray(x)
    x = x - x.mean()
    n = len(x)
    var = np.dot(x, x) / n
    result = [1.0]
    for lag in range(1, max_lag + 1):
        cov = np.dot(x[:-lag], x[lag:]) / n
        result.append(cov / var)
    return np.array(result)


def pacf_from_acf(acf_vals: np.ndarray) -> np.ndarray:
    max_lag = len(acf_vals) - 1
    phi = np.zeros((max_lag + 1, max_lag + 1))
    pacf = np.zeros(max_lag + 1)
    pacf[0] = 1.0
    if max_lag >= 1:
        phi[1, 1] = acf_vals[1]
        pacf[1] = acf_vals[1]
    for k in range(2, max_lag + 1):
        num = acf_vals[k]
        den = 1.0
        for j in range(1, k):
            num -= phi[k - 1, j] * acf_vals[k - j]
            den -= phi[k - 1, j] * acf_vals[j]
        phi[k, k] = num / den if den != 0 else 0.0
        for j in range(1, k):
            phi[k, j] = phi[k - 1, j] - phi[k, k] * phi[k - 1, k - j]
        pacf[k] = phi[k, k]
    return pacf


def plot_series(ax: plt.Axes, x: np.ndarray, title: str) -> None:
    ax.plot(x, color="#1f77b4", linewidth=1.6)
    ax.set_title(title)
    ax.set_xlabel("Index")
    ax.set_ylabel("Value")


def make_nonlinear_trend(rng: np.random.Generator) -> np.ndarray:
    n = 140
    t = np.arange(n)
    trend = 12 + 70 / (1 + np.exp(-0.06 * (t - 70)))
    noise = rng.normal(0, 1.6, size=n)
    return trend + noise


def annotate_trend(ax: plt.Axes, x: np.ndarray) -> None:
    smooth = moving_average(x, 9)
    ax.plot(smooth, color="#d62728", linewidth=2.0, label="Smoothed trend")
    ax.legend(frameon=False)


def make_seasonal_heteroskedastic(rng: np.random.Generator) -> np.ndarray:
    n = 150
    t = np.arange(n)
    seasonal = 8 * np.sin(2 * np.pi * t / 10)
    trend = 0.15 * t
    scale = 0.5 + 0.02 * t
    noise = rng.normal(0, scale)
    return 40 + trend + seasonal + noise


def make_structural_break(rng: np.random.Generator) -> np.ndarray:
    n = 130
    t = np.arange(n)
    trend = np.where(t < 70, 30 + 0.12 * t, 38 + 0.03 * (t - 70))
    noise = rng.normal(0, 1.2, size=n)
    return trend + noise


def annotate_break(ax: plt.Axes, x: np.ndarray) -> None:
    ax.axvline(70, color="#7f7f7f", linestyle="--", linewidth=1.2, label="Shift")
    ax.legend(frameon=False)


def make_periodic_unknown(rng: np.random.Generator) -> np.ndarray:
    n = 160
    t = np.arange(n)
    periodic = 6 * np.sin(2 * np.pi * t / 17.5) + 2 * np.sin(2 * np.pi * t / 41)
    noise = rng.normal(0, 1.0, size=n)
    return 20 + periodic + noise


def make_negative_dependence(rng: np.random.Generator) -> np.ndarray:
    n = 140
    phi = -0.65
    x = np.zeros(n)
    noise = rng.normal(0, 1.0, size=n)
    for t in range(1, n):
        x[t] = phi * x[t - 1] + noise[t]
    return x + 5


def make_positive_dependence(rng: np.random.Generator) -> np.ndarray:
    n = 140
    phi = 0.7
    x = np.zeros(n)
    noise = rng.normal(0, 1.0, size=n)
    for t in range(1, n):
        x[t] = phi * x[t - 1] + noise[t]
    return x + 6


def make_white_noise(rng: np.random.Generator) -> np.ndarray:
    return rng.normal(0, 1.0, size=160)


def make_random_walk(rng: np.random.Generator) -> np.ndarray:
    steps = rng.normal(0, 1.0, size=160)
    return np.cumsum(steps)


def make_seasonal_structural_break(rng: np.random.Generator) -> np.ndarray:
    n = 180
    t = np.arange(n)
    break_point = 90
    amplitude = np.where(t < break_point, 4.5, 7.5)
    level = np.where(t < break_point, 35.0, 43.0)
    seasonal = amplitude * np.sin(2 * np.pi * t / 12)
    noise = rng.normal(0, 1.1, size=n)
    return level + seasonal + noise


def make_ar1(rng: np.random.Generator) -> np.ndarray:
    n = 200
    phi = 0.7
    x = np.zeros(n)
    noise = rng.normal(0, 1.0, size=n)
    for t in range(1, n):
        x[t] = phi * x[t - 1] + noise[t]
    return x


def plot_acf(ax: plt.Axes, x: np.ndarray, max_lag: int = 24) -> None:
    values = acf(x, max_lag)
    lags = np.arange(len(values))
    ax.stem(lags, values, basefmt=" ", linefmt="#1f77b4", markerfmt="o")
    bound = 1.96 / np.sqrt(len(x))
    ax.axhline(bound, color="#d62728", linestyle="--", linewidth=1.0)
    ax.axhline(-bound, color="#d62728", linestyle="--", linewidth=1.0)
    ax.set_title("Sample ACF (AR(1) example)")
    ax.set_xlabel("Lag")
    ax.set_ylabel("Autocorrelation")


def plot_pacf(ax: plt.Axes, x: np.ndarray, max_lag: int = 24) -> None:
    values = acf(x, max_lag)
    pacf_vals = pacf_from_acf(values)
    lags = np.arange(len(pacf_vals))
    ax.stem(lags, pacf_vals, basefmt=" ", linefmt="#2ca02c", markerfmt="o")
    bound = 1.96 / np.sqrt(len(x))
    ax.axhline(bound, color="#d62728", linestyle="--", linewidth=1.0)
    ax.axhline(-bound, color="#d62728", linestyle="--", linewidth=1.0)
    ax.set_title("Sample PACF")
    ax.set_xlabel("Lag")
    ax.set_ylabel("Partial autocorrelation")


def make_arma11(rng: np.random.Generator) -> np.ndarray:
    n = 200
    phi = 0.6
    theta = 0.4
    x = np.zeros(n)
    eps = rng.normal(0, 1.0, size=n)
    for t in range(1, n):
        x[t] = phi * x[t - 1] + eps[t] + theta * eps[t - 1]
    return x


def build_specs() -> List[PlotSpec]:
    return [
        PlotSpec(
            name="intro_nonlinear_trend.png",
            title="Urban growth index (synthetic)",
            make=make_nonlinear_trend,
            annotate=annotate_trend,
        ),
        PlotSpec(
            name="intro_seasonal_heteroskedastic.png",
            title="Warehouse demand index (synthetic)",
            make=make_seasonal_heteroskedastic,
        ),
        PlotSpec(
            name="intro_structural_break.png",
            title="Manufacturing output with a regime shift",
            make=make_structural_break,
            annotate=annotate_break,
        ),
        PlotSpec(
            name="intro_periodic_nonseasonal.png",
            title="Sensor signal with periodicity",
            make=make_periodic_unknown,
        ),
        PlotSpec(
            name="intro_negative_dependence.png",
            title="Alternating-control process",
            make=make_negative_dependence,
        ),
        PlotSpec(
            name="intro_white_noise.png",
            title="White noise example",
            make=make_white_noise,
        ),
        PlotSpec(
            name="intro_random_walk.png",
            title="Random walk example",
            make=make_random_walk,
        ),
        PlotSpec(
            name="intro_positive_dependence.png",
            title="Positive dependence with stable level",
            make=make_positive_dependence,
        ),
        PlotSpec(
            name="intro_seasonal_structural_break.png",
            title="Seasonal series with a structural break",
            make=make_seasonal_structural_break,
            annotate=annotate_break,
        ),
    ]


def save_series_plots(out_dir: Path, rng: np.random.Generator) -> None:
    for spec in build_specs():
        series = spec.make(rng)
        fig, ax = plt.subplots(figsize=(8, 3.6))
        plot_series(ax, series, spec.title)
        if spec.annotate is not None:
            spec.annotate(ax, series)
        fig.tight_layout()
        fig.savefig(out_dir / spec.name, dpi=160)
        plt.close(fig)


def save_acf_plot(out_dir: Path, rng: np.random.Generator) -> None:
    series = make_ar1(rng)
    fig, ax = plt.subplots(figsize=(7, 3.2))
    plot_acf(ax, series)
    fig.tight_layout()
    fig.savefig(out_dir / "acf_ar1_example.png", dpi=160)
    plt.close(fig)


def save_arma_acf_pacf_plot(out_dir: Path, rng: np.random.Generator) -> None:
    series = make_arma11(rng)
    fig, axes = plt.subplots(2, 1, figsize=(7, 5), sharex=True)
    plot_acf(axes[0], series, max_lag=24)
    axes[0].set_title("Sample ACF (ARMA(1,1) example)")
    plot_pacf(axes[1], series, max_lag=24)
    fig.tight_layout()
    fig.savefig(out_dir / "arma_acf_pacf.png", dpi=160)
    plt.close(fig)


def save_arima_differencing_plot(out_dir: Path, rng: np.random.Generator) -> None:
    n = 200
    drift = 0.3
    noise = rng.normal(0, 1.0, size=n)
    series = np.zeros(n)
    for t in range(1, n):
        series[t] = series[t - 1] + drift + noise[t]
    diff1 = np.diff(series)
    diff2 = np.diff(diff1)

    fig, axes = plt.subplots(3, 1, figsize=(8, 6), sharex=False)
    axes[0].plot(series, color="#1f77b4", linewidth=1.2)
    axes[0].set_title("Integrated series (synthetic)")
    axes[0].set_ylabel("Level")

    axes[1].plot(np.arange(1, n), diff1, color="#ff7f0e", linewidth=1.1)
    axes[1].axhline(0, color="#7f7f7f", linewidth=0.8)
    axes[1].set_title("First difference")
    axes[1].set_ylabel("Change")

    axes[2].plot(np.arange(2, n), diff2, color="#2ca02c", linewidth=1.0)
    axes[2].axhline(0, color="#7f7f7f", linewidth=0.8)
    axes[2].set_title("Second difference")
    axes[2].set_xlabel("Index")
    axes[2].set_ylabel("Change")

    fig.tight_layout()
    fig.savefig(out_dir / "arima_differencing.png", dpi=160)
    plt.close(fig)


def save_detrending_plot(out_dir: Path, rng: np.random.Generator) -> None:
    n = 160
    t = np.arange(n)
    trend = 0.25 * t
    seasonal = 6 * np.sin(2 * np.pi * t / 12)
    noise = rng.normal(0, 1.5, size=n)
    series = 20 + trend + seasonal + noise

    coeffs = np.polyfit(t, series, 1)
    trend_fit = np.polyval(coeffs, t)
    detrended = series - trend_fit

    fig, axes = plt.subplots(2, 1, figsize=(8, 5), sharex=True)
    axes[0].plot(series, color="#1f77b4", linewidth=1.5, label="Series")
    axes[0].plot(trend_fit, color="#d62728", linewidth=2.0, label="Linear trend")
    axes[0].set_title("Detrending example (synthetic)")
    axes[0].legend(frameon=False)
    axes[0].set_ylabel("Value")

    axes[1].plot(detrended, color="#2ca02c", linewidth=1.2)
    axes[1].axhline(0, color="#7f7f7f", linewidth=1.0)
    axes[1].set_title("Detrended series")
    axes[1].set_xlabel("Index")
    axes[1].set_ylabel("Value")

    fig.tight_layout()
    fig.savefig(out_dir / "detrending_example.png", dpi=160)
    plt.close(fig)


def save_seasonal_differencing_plot(out_dir: Path, rng: np.random.Generator) -> None:
    n = 180
    t = np.arange(n)
    trend = 0.05 * t
    seasonal = 4 * np.sin(2 * np.pi * t / 12)
    noise = rng.normal(0, 1.0, size=n)
    series = 50 + trend + seasonal + noise
    period = 12
    diff = series[period:] - series[:-period]

    fig, axes = plt.subplots(2, 1, figsize=(8, 5), sharex=False)
    axes[0].plot(series, color="#1f77b4", linewidth=1.5)
    axes[0].set_title("Seasonal series (synthetic, period 12)")
    axes[0].set_ylabel("Value")

    axes[1].plot(np.arange(period, n), diff, color="#ff7f0e", linewidth=1.3)
    axes[1].axhline(0, color="#7f7f7f", linewidth=1.0)
    axes[1].set_title("Seasonal differencing")
    axes[1].set_xlabel("Index")
    axes[1].set_ylabel("Value")

    fig.tight_layout()
    fig.savefig(out_dir / "seasonal_differencing.png", dpi=160)
    plt.close(fig)


def simple_seasonal_decompose(series: np.ndarray, period: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    trend = moving_average(series, period)
    detrended = series - trend
    seasonal = np.zeros_like(series)
    for i in range(period):
        seasonal[i::period] = np.nanmean(detrended[i::period])
    residual = series - trend - seasonal
    return trend, seasonal, residual


def save_simple_decomposition_plot(out_dir: Path, rng: np.random.Generator) -> None:
    n = 180
    t = np.arange(n)
    trend = 0.08 * t
    seasonal = 5 * np.sin(2 * np.pi * t / 12 + 0.4)
    noise = rng.normal(0, 1.0, size=n)
    series = 30 + trend + seasonal + noise
    trend_est, seasonal_est, residual = simple_seasonal_decompose(series, period=12)

    fig, axes = plt.subplots(4, 1, figsize=(8, 7), sharex=True)
    axes[0].plot(series, color="#1f77b4", linewidth=1.3)
    axes[0].set_title("Simple decomposition (synthetic)")
    axes[0].set_ylabel("Observed")

    axes[1].plot(trend_est, color="#d62728", linewidth=1.6)
    axes[1].set_ylabel("Trend")

    axes[2].plot(seasonal_est, color="#2ca02c", linewidth=1.2)
    axes[2].set_ylabel("Seasonal")

    axes[3].plot(residual, color="#7f7f7f", linewidth=1.0)
    axes[3].axhline(0, color="#7f7f7f", linewidth=0.8)
    axes[3].set_ylabel("Residual")
    axes[3].set_xlabel("Index")

    fig.tight_layout()
    fig.savefig(out_dir / "simple_decomposition.png", dpi=160)
    plt.close(fig)


def save_garch_plot(out_dir: Path, rng: np.random.Generator) -> None:
    n = 400
    alpha0 = 0.1
    alpha1 = 0.15
    beta1 = 0.8
    h = np.zeros(n)
    eps = np.zeros(n)
    h[0] = alpha0 / (1 - alpha1 - beta1)
    z = rng.normal(0, 1.0, size=n)
    for t in range(1, n):
        h[t] = alpha0 + alpha1 * eps[t - 1] ** 2 + beta1 * h[t - 1]
        eps[t] = np.sqrt(h[t]) * z[t]

    fig, axes = plt.subplots(2, 1, figsize=(8, 5), sharex=True)
    axes[0].plot(eps, color="#1f77b4", linewidth=1.0)
    axes[0].set_title("GARCH(1,1) style volatility clustering (synthetic)")
    axes[0].set_ylabel("Returns")

    axes[1].plot(np.sqrt(h), color="#d62728", linewidth=1.4)
    axes[1].set_ylabel("Volatility")
    axes[1].set_xlabel("Index")

    fig.tight_layout()
    fig.savefig(out_dir / "garch_volatility.png", dpi=160)
    plt.close(fig)


def main() -> None:
    out_dir = Path("notes/assets/time_series")
    out_dir.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(7)
    save_series_plots(out_dir, rng)
    save_acf_plot(out_dir, rng)
    save_arma_acf_pacf_plot(out_dir, rng)
    save_arima_differencing_plot(out_dir, rng)
    save_detrending_plot(out_dir, rng)
    save_seasonal_differencing_plot(out_dir, rng)
    save_simple_decomposition_plot(out_dir, rng)
    save_garch_plot(out_dir, rng)
    print(f"Wrote plots to {out_dir}")


if __name__ == "__main__":
    main()
