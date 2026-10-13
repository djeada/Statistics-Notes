import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.special import expit  # Sigmoid function


def create_data():
    """Return the hours studied, practice exams and pass/fail data used in the note."""
    data = {
        "Hours Studied (x1)": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "Practice Exams (x2)": [0, 1, 2, 3, 0, 2, 3, 1, 4, 2],
        "Pass (y)": [0, 0, 0, 1, 0, 1, 0, 1, 1, 1],
    }
    return pd.DataFrame(data)


def prepare_data(df):
    """Return the design matrix X (with intercept column) and response vector y."""
    X = np.column_stack((np.ones(df.shape[0]), df["Hours Studied (x1)"], df["Practice Exams (x2)"]))
    y = df["Pass (y)"].to_numpy(dtype=float)
    return X, y


def logistic_function(X, beta):
    """Predicted probabilities expit(X @ beta)."""
    return expit(X @ beta)


def fit_logistic_newton(X, y, n_iter=25, tol=1e-10):
    """Maximum likelihood fit by Newton-Raphson. Requires non-separable data."""
    beta = np.zeros(X.shape[1])
    for _ in range(n_iter):
        p = logistic_function(X, beta)
        gradient = X.T @ (y - p)
        hessian = -(X.T * (p * (1 - p))) @ X
        step = np.linalg.solve(hessian, gradient)
        beta = beta - step
        if np.max(np.abs(step)) < tol:
            break
    return beta


def create_decision_boundary(x1_range, x2_range, beta):
    """Evaluate fitted probabilities on a grid."""
    X1, X2 = np.meshgrid(x1_range, x2_range)
    grid = np.column_stack((np.ones(X1.size), X1.ravel(), X2.ravel()))
    Z = logistic_function(grid, beta).reshape(X1.shape)
    return X1, X2, Z


def plot_data_and_boundary(df, X1, X2, Z):
    """Plot the data with shaded predicted-class regions (0.5 boundary)."""
    plt.figure(figsize=(10, 6))
    plt.contourf(X1, X2, Z, levels=[0, 0.5, 1], alpha=0.2, colors=["red", "green"])

    failed = df[df["Pass (y)"] == 0]
    passed = df[df["Pass (y)"] == 1]
    plt.scatter(failed["Hours Studied (x1)"], failed["Practice Exams (x2)"],
                color="red", label="Fail (y=0)", s=100)
    plt.scatter(passed["Hours Studied (x1)"], passed["Practice Exams (x2)"],
                color="green", label="Pass (y=1)", s=100)

    plt.title("Logistic Regression: Hours Studied vs Practice Exams\nwith Decision Boundary", fontsize=14)
    plt.xlabel("Hours Studied (x1)", fontsize=12)
    plt.ylabel("Practice Exams (x2)", fontsize=12)
    plt.legend()
    plt.show()


def main():
    df = create_data()
    X, y = prepare_data(df)

    beta_hat = fit_logistic_newton(X, y)
    p_hat = logistic_function(X, beta_hat)
    pred = (p_hat >= 0.5).astype(int)
    print("beta_hat:", np.round(beta_hat, 3))
    print("odds ratios:", np.round(np.exp(beta_hat[1:]), 2))
    print("fitted probabilities:", np.round(p_hat, 3))
    print("accuracy:", np.mean(pred == y))

    x1_range = np.linspace(df["Hours Studied (x1)"].min() - 1, df["Hours Studied (x1)"].max() + 1, 200)
    x2_range = np.linspace(df["Practice Exams (x2)"].min() - 1, df["Practice Exams (x2)"].max() + 1, 200)
    X1, X2, Z = create_decision_boundary(x1_range, x2_range, beta_hat)
    plot_data_and_boundary(df, X1, X2, Z)


if __name__ == "__main__":
    main()
