import numpy as np
import matplotlib.pyplot as plt

class GeometricDistribution:
    def __init__(self, p, size=100):
        self.p = p
        self.size = size

    def pmf(self, k):
        return (1 - self.p)**(k - 1) * self.p

    def cdf(self, k):
        return 1 - (1 - self.p)**k

p_values = [0.2, 0.4, 0.6, 0.8]
k = np.arange(1, 21)

# Plot PDFs
for p in p_values:
    gd = GeometricDistribution(p=p)
    plt.plot(k, gd.pmf(k), label=f'p={p}')

plt.title('Geometric Distribution PMF')
plt.xlabel('k')
plt.ylabel('P(X=k)')
plt.legend()
plt.show()

# Plot CDFs
for p in p_values:
    gd = GeometricDistribution(p=p)
    plt.plot(k, gd.cdf(k), label=f'p={p}')

plt.title('Geometric Distribution CDF')
plt.xlabel('k')
plt.ylabel('P(X<=k)')
plt.legend()
plt.show()
