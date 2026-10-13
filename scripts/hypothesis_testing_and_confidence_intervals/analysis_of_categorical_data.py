"""Chi-square goodness-of-fit test: M&M colour distribution versus 2008 proportions."""

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats


def goodness_of_fit(observed: np.ndarray, proportions: np.ndarray, alpha: float = 0.05) -> dict:
    """Run a chi-square goodness-of-fit test against specified proportions."""
    expected = observed.sum() * proportions
    chi_square, p_value = stats.chisquare(observed, expected)
    df = len(observed) - 1
    critical_value = stats.chi2.ppf(1 - alpha, df)
    return {
        "expected": expected,
        "chi_square": chi_square,
        "p_value": p_value,
        "df": df,
        "critical_value": critical_value,
        "reject": chi_square > critical_value,
    }


def plot_observed_vs_expected(colors, observed, expected) -> None:
    """Grouped bar chart of observed and expected counts."""
    index = np.arange(len(colors))
    width = 0.35
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(index, observed, width, label="Observed", color="blue", alpha=0.7)
    ax.bar(index + width, expected, width, label="Expected", color="orange", alpha=0.7)
    ax.set_xlabel("M&M colors")
    ax.set_ylabel("Counts")
    ax.set_title("Observed vs expected M&M color distribution")
    ax.set_xticks(index + width / 2)
    ax.set_xticklabels(colors)
    ax.legend()
    plt.tight_layout()
    plt.show()


def main() -> None:
    colors = ["Blue", "Orange", "Green", "Yellow", "Red", "Brown"]
    proportions = np.array([0.24, 0.20, 0.16, 0.14, 0.13, 0.13])
    observed = np.array([105, 91, 70, 50, 45, 49])

    result = goodness_of_fit(observed, proportions)
    print(f"Chi-square statistic: {result['chi_square']:.2f}")
    print(f"Degrees of freedom: {result['df']}")
    print(f"p-value: {result['p_value']:.4f}")
    print(f"Critical value: {result['critical_value']:.2f}")
    if result["reject"]:
        print("Reject H0: the color distribution differs from the 2008 proportions.")
    else:
        print("Fail to reject H0: no evidence the distribution differs from 2008.")

    plot_observed_vs_expected(colors, observed, result["expected"])


if __name__ == "__main__":
    main()
