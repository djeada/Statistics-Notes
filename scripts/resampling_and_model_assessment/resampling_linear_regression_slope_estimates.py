"""Residual-resampling bootstrap for the slope of a simple linear regression."""

import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm


def main() -> None:
    np.random.seed(42)

    # Step 1: Generate synthetic data
    n = 100
    true_a, true_b = 3, 2
    X = np.random.uniform(0, 10, size=n)
    Y = true_a + true_b * X + np.random.normal(0, 1, size=n)

    # Step 2: Fit the original model
    X_with_const = sm.add_constant(X)
    model = sm.OLS(Y, X_with_const).fit()
    a_hat, b_hat = model.params
    residuals = model.resid

    # Step 3: Residual resampling bootstrap
    B = 1000
    bootstrap_b = np.empty(B)
    for i in range(B):
        resampled_residuals = np.random.choice(residuals, size=n, replace=True)
        Y_star = a_hat + b_hat * X + resampled_residuals
        bootstrap_b[i] = sm.OLS(Y_star, X_with_const).fit().params[1]

    # Step 4: Bootstrap standard error (sample SD with B - 1, as in the note)
    standard_error_b = np.std(bootstrap_b, ddof=1)

    # Step 5: Plot
    plt.figure(figsize=(10, 6))
    plt.hist(bootstrap_b, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
    plt.axvline(b_hat, color='red', linestyle='dashed', linewidth=2,
                label=f"Original Slope = {b_hat:.4f}")
    plt.title('Bootstrap Distribution of Slope Estimates', fontsize=16)
    plt.xlabel('Slope Estimate', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.legend(fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()

    print(f"Original Slope Estimate: {b_hat:.4f}")
    print(f"Bootstrap Standard Error of Slope: {standard_error_b:.4f}")
    print(f"OLS Standard Error of Slope:       {model.bse[1]:.4f}")


if __name__ == "__main__":
    main()
