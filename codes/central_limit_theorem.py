import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

die_values = [1, 2, 3, 4, 5, 6]
sample_sizes = [2, 4, 8, 16, 32]

for experiment in range(1):
for sample_size in sample_sizes:
sample_means = []
for num_samples in range(1000):
die_cast = np.random.choice(
die_values, size=sample_size)
sample_mean = np.mean(die_cast)
sample_means.append(sample_mean)

experiment_mean = np.mean(sample_means)
experiment_std = np.std(sample_means)
x_min = min(sample_means)
x_max = max(sample_means)
x = np.arange(x_min, x_max, 0.01)
y = norm.pdf(x, experiment_mean, experiment_std)
plt.plot(x, y)

legend_texts = [f'Sample Size = {v}' for v in sample_sizes]
plt.legend(legend_texts)
plt.title("Distribution Changes By Sample Size")
plt.show()
