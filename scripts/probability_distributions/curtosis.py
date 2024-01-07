import numpy as np
from scipy.stats import t as t_dist
from scipy.stats import kurtosis as kurt
from scipy.stats import norm
import matplotlib.pyplot as plt

sigmas = [1, 2, 3]

plt.figure(figsize=(8,5))
plt.title('Kurtosis For Normal Data With Different $\sigma$ Values',
          fontsize=16)

for i, sigma in enumerate(sigmas):
    x = np.random.normal(0, sigma, 1000)
    k = round(kurt(x), 4)
    plt.hist(x, alpha=0.5, label=f'$\sigma$={sigma}, k={k}')

plt.legend(fontsize=14)
plt.show()
