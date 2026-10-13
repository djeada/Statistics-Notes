"""Two-sample t-test comparing simulated apple weights from two farms."""

import numpy as np
import scipy.stats as stats


def main() -> None:
    rng = np.random.default_rng(42)

    farm_a = rng.normal(loc=150, scale=10, size=50)
    farm_b = rng.normal(loc=155, scale=10, size=50)

    print(f"Mean weight of apples from Farm A: {farm_a.mean():.2f} g")
    print(f"Mean weight of apples from Farm B: {farm_b.mean():.2f} g")

    # Pooled two-sample t-test (equal variances assumed).
    t_stat, p_value = stats.ttest_ind(farm_a, farm_b)
    df = len(farm_a) + len(farm_b) - 2

    pooled_sd = np.sqrt((farm_a.var(ddof=1) + farm_b.var(ddof=1)) / 2)  # equal group sizes
    cohens_d = (farm_a.mean() - farm_b.mean()) / pooled_sd

    print(f"t-statistic: {t_stat:.2f} (df = {df})")
    print(f"p-value: {p_value:.4f}")
    print(f"Cohen's d: {cohens_d:.2f}")

    alpha = 0.05
    if p_value <= alpha:
        print("Reject H0: the average apple weights differ between the two farms.")
    else:
        print("Fail to reject H0: no evidence that the average apple weights differ.")


if __name__ == "__main__":
    main()
