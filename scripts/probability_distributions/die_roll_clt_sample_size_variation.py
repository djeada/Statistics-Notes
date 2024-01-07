import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

class DieRollCLTSampleSizeVariation:
    def __init__(self, sides, sample_sizes):
        self.sides = sides
        self.sample_sizes = sample_sizes
    
    def run_experiment(self):
        for size in self.sample_sizes:
            means = [np.mean(np.random.choice(self.sides, size)) for _ in range(1000)]
            mean, std = np.mean(means), np.std(means)
            x = np.linspace(min(means), max(means), 100)
            y = norm.pdf(x, mean, std)
            plt.plot(x, y, label=f'Sample Size = {size}')

        plt.title("Die Roll CLT Sample Size Variation")
        plt.xlabel("Sample Means")
        plt.ylabel("Probability Density")
        plt.legend()
        plt.show()

die_sides = [1, 2, 3, 4, 5, 6]
sample_sizes = [2, 4, 8, 16, 32]
experiment = DieRollCLTSampleSizeVariation(die_sides, sample_sizes)
experiment.run_experiment()
