import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def create_data():
    """Hours studied (x1), practice exams (x2 = x1 / 2, perfectly collinear) and test scores (y)."""
    data = {'Hours_Studied (x1)': [2, 4, 6, 8],
            'Practice_Exams (x2)': [1, 2, 3, 4],
            'Test_Score (y)': [50, 60, 70, 80]}
    return pd.DataFrame(data)


def fit_model(df):
    """Fit OLS on the collinear design; the coefficients are not unique (min-norm solution)."""
    X = df[['Hours_Studied (x1)', 'Practice_Exams (x2)']].values
    y = df['Test_Score (y)'].values
    model = LinearRegression().fit(X, y)
    return model, X


def plot_plane(df, model):
    """3D scatter of the data with the fitted plane (the data lie on a line in x1-x2 space)."""
    x1_range = np.linspace(df['Hours_Studied (x1)'].min(), df['Hours_Studied (x1)'].max(), 10)
    x2_range = np.linspace(df['Practice_Exams (x2)'].min(), df['Practice_Exams (x2)'].max(), 10)
    x1_grid, x2_grid = np.meshgrid(x1_range, x2_range)
    y_grid = model.predict(np.c_[x1_grid.ravel(), x2_grid.ravel()]).reshape(x1_grid.shape)

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(df['Hours_Studied (x1)'], df['Practice_Exams (x2)'], df['Test_Score (y)'],
               color='blue', label='Actual Data')
    ax.plot_surface(x1_grid, x2_grid, y_grid, color='red', alpha=0.5, rstride=100, cstride=100)
    ax.set_title('3D Linear Regression: Hours Studied, Practice Exams, and Test Scores', fontsize=14)
    ax.set_xlabel('Hours Studied ($x_1$)')
    ax.set_ylabel('Practice Exams ($x_2$)')
    ax.set_zlabel('Test Score ($y$)')
    plt.show()


def main():
    df = create_data()
    model, X = fit_model(df)
    plot_plane(df, model)

    Xc = np.c_[np.ones(len(X)), X]
    print(f"Rank of design matrix: {np.linalg.matrix_rank(Xc)} (3 columns -> rank deficient)")
    print(f"cond(X'X) = {np.linalg.cond(Xc.T @ Xc):.3g}")
    print(f"Coefficients (non-unique, minimum-norm): {model.coef_}, intercept: {model.intercept_:.3f}")
    print(f"Identified combination b1 + b2/2 = {model.coef_[0] + model.coef_[1] / 2:.3f}")


if __name__ == "__main__":
    main()
