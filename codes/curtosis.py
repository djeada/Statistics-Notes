import numpy as np
from scipy.stats import t as t_dist
from scipy.stats import kurtosis as kurt
from scipy.stats import norm
import matplotlib.pyplot as plt

x1 = np.random.normal(0, 1, 1000)
x2 = np.random.normal(0, 2, 1000)
x3 = np.random.normal(0, 3, 1000)

k1 = round(kurt(x1), 4)
k2 = round(kurt(x2), 4)
k3 = round(kurt(x3), 4)

plt.figure(figsize=(8,5))
plt.title('Kurtosis For Normal Data With Different $\sigma$ Values',
fontsize=16)
plt.hist(x3, alpha=0.5)
plt.hist(x2, alpha=0.5)
plt.hist(x1, alpha=1.0)
plt.legend(
[f'$\sigma$=3, k={k3}', f'$\sigma$=2, k={k2}', f'$\sigma$=1, k={k1}'],
fontsize=14)
plt.show()
