"""Shared numerical and plotting helpers for the time-series student pack."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


REPO_ROOT = Path(__file__).resolve().parents[2]


def output_dir(topic: str) -> Path:
    directory = REPO_ROOT / "assets" / "time_series" / topic
    directory.mkdir(parents=True, exist_ok=True)
    return directory


def save_figure(directory: Path, name: str) -> None:
    path = directory / name
    plt.tight_layout()
    plt.savefig(path, dpi=180, bbox_inches="tight")
    plt.close()
    print(f"created {path.relative_to(REPO_ROOT)}")


def acf(values: np.ndarray, max_lag: int) -> np.ndarray:
    values = np.asarray(values, dtype=float)
    centered = values - values.mean()
    denominator = np.dot(centered, centered)
    result = np.empty(max_lag + 1)
    result[0] = 1.0
    for lag in range(1, max_lag + 1):
        result[lag] = np.dot(centered[:-lag], centered[lag:]) / denominator
    return result


def pacf_from_acf(acf_values: np.ndarray) -> np.ndarray:
    """Calculate partial autocorrelations with the Durbin-Levinson recursion."""
    max_lag = len(acf_values) - 1
    coefficients = np.zeros((max_lag + 1, max_lag + 1))
    partial = np.zeros(max_lag + 1)
    partial[0] = 1.0

    for order in range(1, max_lag + 1):
        numerator = acf_values[order]
        denominator = 1.0
        for j in range(1, order):
            numerator -= coefficients[order - 1, j] * acf_values[order - j]
            denominator -= coefficients[order - 1, j] * acf_values[j]
        coefficients[order, order] = numerator / denominator
        for j in range(1, order):
            coefficients[order, j] = (
                coefficients[order - 1, j]
                - coefficients[order, order] * coefficients[order - 1, order - j]
            )
        partial[order] = coefficients[order, order]
    return partial


def stem(ax: plt.Axes, values: np.ndarray, title: str, color: str = "tab:blue") -> None:
    lags = np.arange(len(values))
    ax.stem(lags, values, linefmt=color, markerfmt="o", basefmt=" ")
    ax.axhline(0.0, color="0.35", linewidth=0.8)
    ax.set_title(title)
    ax.set_xlabel("Lag")


def simulate_ar1(
    rng: np.random.Generator,
    phi: float,
    n: int = 300,
    intercept: float = 0.0,
    innovation_scale: float = 1.0,
) -> np.ndarray:
    values = np.zeros(n)
    shocks = rng.normal(scale=innovation_scale, size=n)
    for t in range(1, n):
        values[t] = intercept + phi * values[t - 1] + shocks[t]
    return values


def simulate_ar2(
    rng: np.random.Generator,
    phi1: float = 0.65,
    phi2: float = -0.25,
    n: int = 300,
    innovation_scale: float = 1.0,
) -> np.ndarray:
    values = np.zeros(n)
    shocks = rng.normal(scale=innovation_scale, size=n)
    for t in range(2, n):
        values[t] = phi1 * values[t - 1] + phi2 * values[t - 2] + shocks[t]
    return values


def simulate_ma1(
    rng: np.random.Generator,
    theta: float = 0.7,
    n: int = 300,
    innovation_scale: float = 1.0,
) -> np.ndarray:
    shocks = rng.normal(scale=innovation_scale, size=n + 1)
    return shocks[1:] + theta * shocks[:-1]


def simulate_local_level(
    rng: np.random.Generator,
    n: int = 240,
    process_variance: float = 0.10,
    measurement_variance: float = 1.0,
) -> tuple[np.ndarray, np.ndarray]:
    state = np.zeros(n)
    state[0] = 2.0
    state[1:] = state[0] + np.cumsum(
        rng.normal(scale=np.sqrt(process_variance), size=n - 1)
    )
    observations = state + rng.normal(
        scale=np.sqrt(measurement_variance), size=n
    )
    return state, observations


def kalman_filter(
    observations: np.ndarray,
    process_variance: float,
    measurement_variance: float,
    initial_level: float = 0.0,
    initial_variance: float = 1.0,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    filtered = np.zeros(len(observations))
    gains = np.zeros(len(observations))
    variances = np.zeros(len(observations))
    level = initial_level
    variance = initial_variance

    for t, observation in enumerate(observations):
        predicted_variance = variance + process_variance
        innovation_variance = predicted_variance + measurement_variance
        gain = predicted_variance / innovation_variance
        if np.isfinite(observation):
            level += gain * (observation - level)
            variance = (1.0 - gain) * predicted_variance
        else:
            gain = 0.0
            variance = predicted_variance
        filtered[t] = level
        gains[t] = gain
        variances[t] = variance
    return filtered, gains, variances
