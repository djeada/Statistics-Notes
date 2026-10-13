"""Empirical (68-95-99.7) rule for normally distributed heights of fathers."""
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

MU_HEIGHT = 68.3     # mean height in inches
SIGMA_HEIGHT = 1.8   # standard deviation in inches


def main():
    mu, sigma = MU_HEIGHT, SIGMA_HEIGHT
    x = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 1000)
    pdf = norm.pdf(x, mu, sigma)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x, pdf, label=f"Normal: mu={mu}, sigma={sigma}", color="green")
    ax.axvline(mu, color="black", linestyle="--", label=f"Mean = {mu}")

    for k, color, pct in [(1, "blue", "68%"), (2, "orange", "95%"), (3, "red", "99.7%")]:
        lo, hi = mu - k * sigma, mu + k * sigma
        exact = norm.cdf(k) - norm.cdf(-k)
        ax.axvline(lo, color=color, linestyle="--", label=f"mu - {k}sigma = {lo:.1f}")
        ax.axvline(hi, color=color, linestyle="--", label=f"mu + {k}sigma = {hi:.1f}")
        ax.fill_between(x, 0, pdf, where=(x >= lo) & (x <= hi), color=color, alpha=0.2,
                        label=f"{pct} of data (exact {exact:.4f})")
        print(f"mu +/- {k} sigma = ({lo:.1f}, {hi:.1f}): exact probability {exact:.4f}")

    ax.set_title("Empirical Rule (68-95-99.7 Rule) for Heights of Fathers")
    ax.set_xlabel("Height (inches)")
    ax.set_ylabel("Probability density")
    ax.legend()
    ax.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
