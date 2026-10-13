"""Standard normal curve with the z-scores of two fathers' heights."""
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

MU_HEIGHT = 68.3     # inches
SIGMA_HEIGHT = 1.8   # inches


def z_score(x, mu, sigma):
    return (x - mu) / sigma


def main():
    x1, x2 = 71.9, 67.4
    z1 = z_score(x1, MU_HEIGHT, SIGMA_HEIGHT)
    z2 = z_score(x2, MU_HEIGHT, SIGMA_HEIGHT)
    area = norm.cdf(z1) - norm.cdf(z2)
    print(f"z(71.9) = {z1:.2f}, z(67.4) = {z2:.2f}")
    print(f"P(67.4 <= height <= 71.9) = {area:.4f}")

    x = np.linspace(-4, 4, 1000)
    pdf = norm.pdf(x)

    plt.figure(figsize=(10, 6))
    plt.plot(x, pdf, label="Standard Normal Distribution", color="green")
    plt.axvline(z1, color="blue", linestyle="--", label=f"z for 71.9 in: {z1:.1f}")
    plt.axvline(z2, color="red", linestyle="--", label=f"z for 67.4 in: {z2:.1f}")
    plt.fill_between(x, 0, pdf, where=(x >= z2) & (x <= z1), color="orange", alpha=0.3,
                     label=f"Area between z-scores = {area:.4f}")
    plt.title("Standard Normal Distribution and Z-Scores")
    plt.xlabel("z")
    plt.ylabel("Probability density")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
