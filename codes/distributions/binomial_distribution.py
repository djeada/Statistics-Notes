import numpy as np
import matplotlib.pyplot as plt

class Binomial_Distribution:
    def __init__(self, n, p):
        self.n = n
        self.p = p
        self.__binomial_coefficient__()
        
    def __binomial_coefficient__(self):
        self.coefficients = [np.math.comb(self.n, k) for k in range(self.n+1)]
        
    def binomial_PMF(self, k):
        return self.coefficients[k] * (self.p**k) * ((1-self.p)**(self.n-k))

# Set parameters for the distribution
n = 10
p = 0.4

# Create the binomial distribution object
bd = Binomial_Distribution(n, p)

# Calculate the probability mass function for all possible values of k
k_values = np.arange(0, n+1)
PMF_values = [bd.binomial_PMF(k) for k in k_values]

# Plot the probability mass function
plt.bar(k_values, PMF_values)
plt.title(f"Binomial Distribution (n={n}, p={p})")
plt.xlabel("k")
plt.ylabel("Probability")
plt.show()
