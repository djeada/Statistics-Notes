"""Exponential MGF: closed form versus Monte Carlo estimates of E[exp(tX)]."""
import matplotlib.pyplot as plt
import numpy as np


def mgf_exponential(t, lam=1.0):
    """M_X(t) = lam / (lam - t), valid for t < lam."""
    return lam / (lam - t)


def main():
    lam = 1.0
    n = 10000
    rng = np.random.default_rng(42)
    samples = rng.exponential(scale=1 / lam, size=n)

    t_empirical = np.linspace(-0.5, 0.9, 40)
    t_curve = np.linspace(-0.5, 0.9, 400)
    m_hat = np.array([np.exp(t * samples).mean() for t in t_empirical])

    # Moments from derivatives at 0: M'(0) = 1/lam, M''(0) = 2/lam^2
    print(f"E[X]   sample={samples.mean():.3f}  theory={1 / lam:.3f}")
    print(f"E[X^2] sample={(samples**2).mean():.3f}  theory={2 / lam**2:.3f}")

    fig, ax = plt.subplots()
    ax.plot(t_curve, mgf_exponential(t_curve, lam), label="Theoretical MGF $M_X(t)$")
    ax.scatter(t_empirical, m_hat, marker="o", label="Monte Carlo estimates $\\hat M(t)$")
    ax.set_xlabel("$t$")
    ax.set_ylabel("$M_X(t)$")
    ax.set_title("Exponential Distribution (lambda=1): Theoretical vs Empirical MGF")
    ax.legend()
    ax.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
