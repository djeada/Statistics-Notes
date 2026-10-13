"""Chi-square test of independence on simulated beverage preferences."""

import numpy as np
from scipy.stats import chi2_contingency


def main() -> None:
    rng = np.random.default_rng(42)

    n = 1000  # people per gender
    males = rng.choice(["Tea", "Coffee"], size=n, p=[0.6, 0.4])
    females = rng.choice(["Tea", "Coffee"], size=n, p=[0.4, 0.6])

    contingency_table = np.array([
        [np.sum(males == "Tea"), np.sum(males == "Coffee")],
        [np.sum(females == "Tea"), np.sum(females == "Coffee")],
    ])

    chi2, p, dof, _ = chi2_contingency(contingency_table)

    print(f"Contingency table (rows: male, female; columns: tea, coffee):\n{contingency_table}")
    print(f"Chi-square statistic: {chi2:.2f}")
    print(f"Degrees of freedom: {dof}")
    print(f"p-value: {p:.3g}")

    alpha = 0.05
    if p <= alpha:
        print("There is a significant association between gender and beverage preference.")
    else:
        print("There is no significant association between gender and beverage preference.")


if __name__ == "__main__":
    main()
