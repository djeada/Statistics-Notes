"""Chi-square test of independence: gender and voting preference (2x2 table)."""

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


def main() -> None:
    # Rows: Male, Female.  Columns: Liberal, Conservative.
    observed = np.array([
        [40, 60],
        [70, 30],
    ])
    groups = ["Male", "Female"]

    alpha = 0.05
    chi_pearson, p_pearson, df, expected = stats.chi2_contingency(observed, correction=False)
    chi_yates, p_yates, _, _ = stats.chi2_contingency(observed, correction=True)
    critical_value = stats.chi2.ppf(1 - alpha, df)

    print(f"Expected counts:\n{expected}")
    print(f"Pearson chi-square: {chi_pearson:.2f} (p = {p_pearson:.3g})")
    print(f"Yates chi-square:   {chi_yates:.2f} (p = {p_yates:.3g})")
    print(f"Critical value (df={df}): {critical_value:.2f}")
    if chi_yates > critical_value:
        print("Reject H0: gender and voting preference are associated.")
    else:
        print("Fail to reject H0: no evidence of association.")

    index = np.arange(len(groups))
    width = 0.35
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(index - width / 2, observed[:, 0], width, label="Observed Liberal", color="#4682B4", alpha=0.8)
    ax.bar(index + width / 2, expected[:, 0], width, label="Expected Liberal", color="#A9A9A9", alpha=0.8)
    ax.bar(index - width / 2, observed[:, 1], width, bottom=observed[:, 0],
           label="Observed Conservative", color="#4682B4", alpha=0.5)
    ax.bar(index + width / 2, expected[:, 1], width, bottom=expected[:, 0],
           label="Expected Conservative", color="#A9A9A9", alpha=0.5)
    ax.set_xlabel("Gender")
    ax.set_ylabel("Counts")
    ax.set_title("Observed vs expected voting preferences by gender")
    ax.set_xticks(index)
    ax.set_xticklabels(groups)
    ax.grid(True, linestyle="--", alpha=0.6, axis="y")
    ax.legend(loc="upper right")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
