import matplotlib.pyplot as plt


class Beta_Distribution:
    def __init__(self, alpha, beta, panels=10000):
        self.alpha = alpha
        self.beta = beta
        self.panels = panels
        self.__Beta_Function__()

    def __Beta_Function__(self):
        width = 1 / self.panels
        X = [x / self.panels for x in range(self.panels)]
        # makes total integral of beta_PDF sum to 1
        self.B = sum(
            [(x ** (self.alpha - 1) * (1 - x) ** (self.beta - 1)) * width for x in X]
        )

    def beta_PDF(self, x):
        return x ** (self.alpha - 1) * (1 - x) ** (self.beta - 1) / self.B

    def beta_CDF(self, x):
        cdf = 0
        width = 1 / self.panels
        X = [x / self.panels for x in range(self.panels)]
        for xi in X:
            if xi <= x:
                cdf += (xi ** (self.alpha - 1) * (1 - xi) ** (self.beta - 1)) * width
        return cdf / self.B


X = [x / 1000 for x in range(1000 + 1)]
beta_values = [1, 2, 5, 10, 20]

fig, axs = plt.subplots(2, 1, figsize=(8, 10))

# Plot PDFs for different beta values
for beta in beta_values:
    bd = Beta_Distribution(5, beta)
    Y_pdf = [bd.beta_PDF(x) for x in X]
    axs[0].plot(X, Y_pdf, label=f"Beta = {beta}")
axs[0].set_title(label="Probability Density Function (PDF)")
axs[0].set_xlabel(xlabel="Values")
axs[0].set_ylabel(ylabel="Probabilities")
axs[0].legend()

# Plot CDFs for different beta values
for beta in beta_values:
    bd = Beta_Distribution(5, beta)
    Y_cdf = [bd.beta_CDF(x) for x in X]
    axs[1].plot(X, Y_cdf, label=f"Beta = {beta}")
axs[1].set_title(label="Cumulative Density Function (CDF)")
axs[1].set_xlabel(xlabel="Values")
axs[1].set_ylabel(ylabel="Probabilities")
axs[1].legend()

plt.tight_layout()
plt.show()
