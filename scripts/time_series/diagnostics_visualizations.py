"""Residual, stationarity, and model-checking visualizations."""

import matplotlib.pyplot as plt
import numpy as np
from statistics import NormalDist

from student_plot_utils import acf, output_dir, save_figure, simulate_ar1


FIGURE_DIR = output_dir("diagnostics")


def detrending() -> None:
    rng = np.random.default_rng(901)
    n = 180
    t = np.arange(n)
    series = 5 + 0.08 * t + rng.normal(scale=0.8, size=n)
    fit = np.polyfit(t, series, 1)
    trend = fit[0] * t + fit[1]
    residual = series - trend
    print(
        f"detrending: fitted slope={fit[0]:.4f}; residual mean={residual.mean():.6f}; "
        f"residual variance={residual.var():.4f}"
    )

    fig, axes = plt.subplots(2, 1, figsize=(9, 6), sharex=True)
    axes[0].plot(series, label="series")
    axes[0].plot(trend, color="tab:red", label="linear trend")
    axes[0].legend()
    axes[0].set_title("Trend can create slow ACF decay")
    axes[1].plot(residual, color="tab:green")
    axes[1].axhline(0, color="0.35", linewidth=0.8)
    axes[1].set_title("Residual after removing the fitted trend")
    axes[1].set_xlabel("t")
    save_figure(FIGURE_DIR, "01_detrending.png")


def residual_acf() -> None:
    rng = np.random.default_rng(902)
    residuals = simulate_ar1(rng, 0.65, 260)
    values = acf(residuals, 24)
    bound = 1.96 / np.sqrt(len(residuals))
    print(
        f"residual ACF: lag-1={values[1]:.4f}; approximate 95% bound={bound:.4f}"
    )

    plt.figure(figsize=(8, 4))
    lags = np.arange(len(values))
    plt.stem(lags, values, basefmt=" ")
    plt.axhline(bound, color="tab:red", linestyle="--")
    plt.axhline(-bound, color="tab:red", linestyle="--")
    plt.xlabel("lag")
    plt.ylabel("ACF")
    plt.title("Residual ACF reveals unmodeled serial dependence")
    save_figure(FIGURE_DIR, "02_residual_acf.png")


def residual_variance() -> None:
    rng = np.random.default_rng(903)
    n = 240
    scale = np.where(np.arange(n) < 120, 0.5, 2.0)
    residuals = rng.normal(scale=scale)
    first_variance = residuals[:120].var()
    second_variance = residuals[120:].var()
    print(
        f"residual variance: first half={first_variance:.4f}; "
        f"second half={second_variance:.4f}"
    )

    fig, axes = plt.subplots(2, 1, figsize=(9, 6), sharex=True)
    axes[0].plot(residuals)
    axes[0].axvline(119.5, color="0.4", linestyle=":")
    axes[0].set_title("Changing residual variance")
    axes[1].plot(residuals**2, color="tab:orange")
    axes[1].set_title("Squared residuals expose variance changes")
    axes[1].set_xlabel("t")
    save_figure(FIGURE_DIR, "03_residual_variance.png")


def residual_nonlinearity() -> None:
    rng = np.random.default_rng(904)
    x = rng.normal(size=300)
    y = x**2 + rng.normal(scale=0.25, size=300)
    linear_residuals = y - y.mean()
    print(
        f"nonlinearity: corr(x, residual)={np.corrcoef(x, linear_residuals)[0,1]:.4f}; "
        f"corr(x^2, residual)={np.corrcoef(x**2, linear_residuals)[0,1]:.4f}"
    )

    plt.figure(figsize=(8, 4))
    plt.scatter(x, linear_residuals, alpha=0.35, label="residual")
    grid = np.linspace(x.min(), x.max(), 100)
    plt.plot(grid, grid**2 - y.mean(), color="tab:red", label="nonlinear pattern")
    plt.axhline(0, color="0.35", linewidth=0.8)
    plt.xlabel("predictor")
    plt.ylabel("residual")
    plt.title("Zero linear correlation does not rule out nonlinear structure")
    plt.legend()
    save_figure(FIGURE_DIR, "04_residual_nonlinearity.png")


def normality_check() -> None:
    rng = np.random.default_rng(905)
    residuals = rng.standard_t(df=4, size=600) / np.sqrt(2)
    sorted_values = np.sort(residuals)
    probabilities = (np.arange(1, len(residuals) + 1) - 0.5) / len(residuals)
    normal_reference = np.array(
        [NormalDist().inv_cdf(float(probability)) for probability in probabilities]
    )
    print(
        f"distribution check: residual mean={residuals.mean():.4f}; "
        f"residual standard deviation={residuals.std():.4f}; "
        f"largest absolute residual={np.max(np.abs(residuals)):.3f}"
    )

    plt.figure(figsize=(6, 6))
    plt.scatter(normal_reference, sorted_values, s=10)
    limits = [normal_reference.min(), normal_reference.max()]
    plt.plot(limits, limits, color="tab:red")
    plt.xlabel("normal reference quantile")
    plt.ylabel("ordered residual")
    plt.title("Heavy-tailed residuals bend away from a normal reference")
    save_figure(FIGURE_DIR, "05_residual_distribution.png")


def ljung_box_shape() -> None:
    rng = np.random.default_rng(906)
    values = simulate_ar1(rng, 0.7, 260)
    residuals = rng.normal(size=260)
    dependent_acf = acf(values, 20)[1:]
    white_acf = acf(residuals, 20)[1:]
    dependent_stat = np.cumsum(260 * (dependent_acf**2) / (260 - np.arange(1, 21)))
    white_stat = np.cumsum(260 * (white_acf**2) / (260 - np.arange(1, 21)))
    print(
        f"Ljung-Box shape: Q_10 dependent={dependent_stat[9]:.3f}; "
        f"Q_10 white-noise={white_stat[9]:.3f}"
    )

    plt.figure(figsize=(8, 4))
    plt.plot(np.arange(1, 21), dependent_stat, label="dependent residuals")
    plt.plot(np.arange(1, 21), white_stat, label="white-noise residuals")
    plt.xlabel("maximum tested lag")
    plt.ylabel("cumulative Q statistic")
    plt.title("Portmanteau statistics accumulate residual autocorrelation")
    plt.legend()
    save_figure(FIGURE_DIR, "06_ljung_box_shape.png")


def structural_break() -> None:
    rng = np.random.default_rng(907)
    n = 220
    values = np.where(
        np.arange(n) < 110,
        2.0 + rng.normal(scale=0.5, size=n),
        5.0 + rng.normal(scale=0.5, size=n),
    )
    global_mean = values.mean()
    rolling_mean = np.convolve(values, np.ones(25) / 25, mode="valid")
    print(
        f"structural break: pre-break mean={values[:110].mean():.3f}; "
        f"post-break mean={values[110:].mean():.3f}; global mean={global_mean:.3f}"
    )

    plt.figure(figsize=(9, 4))
    plt.plot(values, alpha=0.5, label="series")
    plt.plot(np.arange(12, n - 12), rolling_mean, color="tab:red", label="25-point mean")
    plt.axvline(109.5, color="0.35", linestyle=":")
    plt.xlabel("t")
    plt.ylabel("value")
    plt.title("A structural break can invalidate one global mean")
    plt.legend()
    save_figure(FIGURE_DIR, "07_structural_break.png")


def validation_splits() -> None:
    n = 120
    t = np.arange(n)
    values = np.sin(2 * np.pi * t / 20)
    train_end = 80
    validation_end = 100
    print(
        f"temporal validation: train=0:{train_end}; validation={train_end}:{validation_end}; "
        f"test={validation_end}:{n}"
    )

    plt.figure(figsize=(9, 3.5))
    plt.plot(t, values, color="0.35")
    plt.axvspan(0, train_end, alpha=0.18, color="tab:blue", label="train")
    plt.axvspan(train_end, validation_end, alpha=0.18, color="tab:orange", label="validation")
    plt.axvspan(validation_end, n, alpha=0.18, color="tab:green", label="test")
    plt.xlabel("time")
    plt.ylabel("value")
    plt.title("A forecasting split preserves temporal order")
    plt.legend()
    save_figure(FIGURE_DIR, "08_temporal_validation_split.png")


def main() -> None:
    detrending()
    residual_acf()
    residual_variance()
    residual_nonlinearity()
    normality_check()
    ljung_box_shape()
    structural_break()
    validation_splits()


if __name__ == "__main__":
    main()
