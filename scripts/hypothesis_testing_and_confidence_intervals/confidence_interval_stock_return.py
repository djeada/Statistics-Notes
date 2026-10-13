"""Confidence intervals for the mean daily return of a synthetic stock."""

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats


def simulate_daily_returns(rng: np.random.Generator, days: int = 252,
                           mean: float = 0.001, volatility: float = 0.02) -> np.ndarray:
    """Simulate daily returns as independent normal draws (no market data is downloaded)."""
    return rng.normal(loc=mean, scale=volatility, size=days)


def calculate_confidence_interval(data: np.ndarray, confidence_level: float) -> dict:
    """t-based confidence interval for the mean of `data`."""
    n = len(data)
    sample_mean = np.mean(data)
    standard_error = np.std(data, ddof=1) / np.sqrt(n)
    t_critical = stats.t.ppf(1 - (1 - confidence_level) / 2, df=n - 1)
    margin_of_error = t_critical * standard_error
    return {
        "mean": sample_mean,
        "margin_of_error": margin_of_error,
        "confidence_interval": (sample_mean - margin_of_error, sample_mean + margin_of_error),
        "t_critical": t_critical,
    }


def plot_confidence_intervals(intervals: dict, stock_name: str) -> None:
    """Plot interval bounds against confidence level."""
    levels = list(intervals.keys())
    lower = [intervals[level]["confidence_interval"][0] for level in levels]
    upper = [intervals[level]["confidence_interval"][1] for level in levels]

    plt.figure(figsize=(10, 6))
    plt.plot(levels, lower, marker="o", label="Lower bound", color="red")
    plt.plot(levels, upper, marker="o", label="Upper bound", color="green")
    plt.fill_between(levels, lower, upper, color="gray", alpha=0.2)
    plt.axhline(0, color="black", linestyle="--")
    plt.title(f"Confidence intervals for mean daily return ({stock_name})")
    plt.xlabel("Confidence level")
    plt.ylabel("Mean daily return")
    plt.legend()
    plt.grid(True)
    plt.show()


def main() -> None:
    rng = np.random.default_rng(42)
    returns = simulate_daily_returns(rng)

    intervals = {}
    for level in [0.90, 0.95, 0.99]:
        intervals[level] = calculate_confidence_interval(returns, level)
        low, high = intervals[level]["confidence_interval"]
        print(f"{level:.0%} CI for mean daily return: ({low:.5f}, {high:.5f})  "
              f"width = {high - low:.5f}")

    plot_confidence_intervals(intervals, "synthetic data")


if __name__ == "__main__":
    main()
