import numpy as np
import matplotlib.pyplot as plt

# Parameters
lam = 1.0            # Exponential rate λ
N = 10000            # Monte Carlo sample size
np.random.seed(42)   # Reproducibility

# Generate sample
samples = np.random.exponential(scale=1/lam, size=N)

# Theoretical MGF for t < λ
def mgf_exponential(t, lam=1.0):
    return lam / (lam - t)

# t values for empirical estimates (sparser) and for smooth curve
t_empirical = np.linspace(-0.5, 0.9, 40)
t_curve = np.linspace(-0.5, 0.9, 400)

# Empirical estimates
M_hat = [np.exp(t * samples).mean() for t in t_empirical]

# Plot
fig, ax = plt.subplots()
ax.plot(t_curve, mgf_exponential(t_curve, lam), label="Theoretical MGF $M_X(t)$")
ax.scatter(t_empirical, M_hat, marker='o', label="Monte Carlo estimates $\\hat M(t)$")
ax.set_xlabel("$t$")
ax.set_ylabel("$M_X(t)$")
ax.set_title("Exponential Distribution (λ=1): Theoretical vs Empirical MGF")
ax.legend()
ax.grid(True)

plt.show()
