"""Sample skewness: right-skewed gamma data versus symmetric normal data."""
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import skew


def main():
    rng = np.random.default_rng(42)
    data1 = rng.gamma(4, 1, 1000)   # theoretical skewness 2 / sqrt(4) = 1
    data2 = rng.normal(6, 2, 1000)  # theoretical skewness 0

    skewness1, skewness2 = skew(data1), skew(data2)
    print(f"gamma(4, 1): skewness = {skewness1:.3f} (theory 1.0)")
    print(f"normal(6, 2): skewness = {skewness2:.3f} (theory 0.0)")

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    for ax, data, color, sk in [(ax1, data1, "blue", skewness1), (ax2, data2, "orange", skewness2)]:
        ax.hist(data, bins=30, alpha=0.5, color=color)
        ax.axvline(np.mean(data), color="red", linestyle="dashed", linewidth=1, label="mean")
        ax.axvline(np.median(data), color="green", linestyle="dashed", linewidth=1, label="median")
        ax.set_title(f"Skewness: {sk:.2f}", fontsize=16)
        ax.set_xlabel("Data Values")
        ax.set_ylabel("Frequency")
        ax.legend()
    plt.show()


if __name__ == "__main__":
    main()
