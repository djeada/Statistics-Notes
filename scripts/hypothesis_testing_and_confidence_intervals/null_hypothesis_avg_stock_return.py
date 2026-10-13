"""One-sample t-test of whether a synthetic stock's mean daily return is zero."""

import numpy as np
import scipy.stats as stats


def simulate_daily_returns(rng: np.random.Generator, days: int = 252,
                           mean: float = 0.0005, volatility: float = 0.015) -> np.ndarray:
    """Simulate daily returns as independent normal draws (no market data is downloaded)."""
    return rng.normal(loc=mean, scale=volatility, size=days)


def hypothesis_test(data: np.ndarray, hypothesized_mean: float = 0.0, alpha: float = 0.05) -> dict:
    """Two-tailed one-sample t-test of H0: mu = hypothesized_mean."""
    n = len(data)
    sample_mean = np.mean(data)
    sample_std = np.std(data, ddof=1)

    t_statistic = (sample_mean - hypothesized_mean) / (sample_std / np.sqrt(n))
    p_value = 2 * stats.t.sf(abs(t_statistic), df=n - 1)

    return {
        "Sample Mean": sample_mean,
        "Sample Standard Deviation": sample_std,
        "T-Statistic": t_statistic,
        "Degrees of Freedom": n - 1,
        "P-Value": p_value,
        "Reject Null Hypothesis": p_value <= alpha,
    }


def main() -> None:
    rng = np.random.default_rng(42)
    returns = simulate_daily_returns(rng)

    result = hypothesis_test(returns, alpha=0.05)
    print("Hypothesis test result (H0: mean daily return = 0):")
    for key, value in result.items():
        print(f"  {key}: {value}")

    if result["Reject Null Hypothesis"]:
        print("\nConclusion: reject H0; the data suggest the mean daily return differs from 0.")
    else:
        print("\nConclusion: fail to reject H0; not enough evidence that the mean daily return differs from 0.")

    # Power check: the true mean is nonzero (0.05% per day), but it is small
    # relative to the standard error with only 252 noisy observations.
    true_effect_in_se = 0.0005 / (0.015 / np.sqrt(252))
    print(f"\nTrue mean is {true_effect_in_se:.2f} standard errors from 0, so power is low at n = 252.")


if __name__ == "__main__":
    main()
