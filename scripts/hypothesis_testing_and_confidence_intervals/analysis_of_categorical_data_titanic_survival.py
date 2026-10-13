"""Chi-square test of homogeneity: Titanic survival across ticket classes."""

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


def main() -> None:
    # Rows: First, Second, Third, Crew.  Columns: Survived, Died.
    observed = np.array([
        [203, 122],
        [118, 167],
        [178, 528],
        [212, 673],
    ])
    classes = ["First Class", "Second Class", "Third Class", "Crew"]

    chi_square, p_value, df, expected = stats.chi2_contingency(observed)
    alpha = 0.05
    critical_value = stats.chi2.ppf(1 - alpha, df)

    print(f"Chi-square statistic: {chi_square:.2f}")
    print(f"Degrees of freedom: {df}")
    print(f"p-value: {p_value:.3g}")
    print(f"Critical value: {critical_value:.2f}")
    if chi_square > critical_value:
        print("Reject H0: survival rates differ across ticket classes.")
    else:
        print("Fail to reject H0: no evidence that survival rates differ.")

    index = np.arange(len(classes))
    width = 0.35
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(index, observed[:, 0], width, label="Observed survived", color="blue", alpha=0.7)
    ax.bar(index + width, expected[:, 0], width, label="Expected survived", color="orange", alpha=0.7)
    ax.bar(index, observed[:, 1], width, bottom=observed[:, 0], label="Observed died", color="green", alpha=0.7)
    ax.bar(index + width, expected[:, 1], width, bottom=expected[:, 0], label="Expected died", color="red", alpha=0.7)
    ax.set_xlabel("Ticket class")
    ax.set_ylabel("Counts")
    ax.set_title("Observed vs expected Titanic survival by ticket class")
    ax.set_xticks(index + width / 2)
    ax.set_xticklabels(classes)
    ax.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
