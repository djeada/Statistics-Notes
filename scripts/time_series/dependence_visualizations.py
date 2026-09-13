"""Dependence, ARMA identification, and diagnostic visualizations."""

import matplotlib.pyplot as plt
import numpy as np

from student_plot_utils import (
    acf,
    output_dir,
    pacf_from_acf,
    simulate_ar1,
    simulate_ar2,
    simulate_ma1,
    save_figure,
    stem,
)


FIGURE_DIR = output_dir("dependence")


def covariance_geometry() -> None:
    x = np.array([1.0, 2.0, 4.0, 3.0])
    centered = x - x.mean()
    gamma0 = np.dot(centered, centered) / len(x)
    gamma1 = np.dot(centered[:-1], centered[1:]) / len(x)
    print(
        f"autocovariance: mean={x.mean():.2f}, gamma_0={gamma0:.4f}, "
        f"gamma_1={gamma1:.4f}, rho_1={gamma1/gamma0:.4f}"
    )

    fig, axes = plt.subplots(1, 2, figsize=(9, 4))
    axes[0].plot(np.arange(1, 5), x, marker="o")
    axes[0].axhline(x.mean(), color="tab:red", linestyle="--", label="mean")
    axes[0].set_title("Observed values")
    axes[0].set_xlabel("t")
    axes[0].legend()
    axes[1].scatter(centered[:-1], centered[1:], s=80)
    axes[1].axhline(0, color="0.4", linewidth=0.8)
    axes[1].axvline(0, color="0.4", linewidth=0.8)
    axes[1].set_xlabel("z_t")
    axes[1].set_ylabel("z_(t+1)")
    axes[1].set_title("Lagged centered pairs")
    save_figure(FIGURE_DIR, "01_autocovariance_geometry.png")


def acf_pacf_ar2() -> None:
    rng = np.random.default_rng(302)
    values = simulate_ar2(rng, phi1=0.6, phi2=-0.2, n=500)
    acf_values = acf(values, 24)
    pacf_values = pacf_from_acf(acf_values)
    print(
        f"AR(2) sample: rho_1={acf_values[1]:.4f}, "
        f"rho_2={acf_values[2]:.4f}, PACF_1={pacf_values[1]:.4f}, "
        f"PACF_2={pacf_values[2]:.4f}"
    )

    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    stem(axes[0], acf_values, "AR(2) ACF")
    stem(axes[1], pacf_values, "AR(2) PACF", "tab:green")
    save_figure(FIGURE_DIR, "02_acf_pacf_identification.png")


def ar_persistence() -> None:
    rng = np.random.default_rng(303)
    n = 160
    values = {
        "phi=0.2": simulate_ar1(rng, 0.2, n),
        "phi=0.7": simulate_ar1(rng, 0.7, n),
        "phi=-0.7": simulate_ar1(rng, -0.7, n),
    }
    print("AR persistence: theoretical rho(1) values are 0.2, 0.7, and -0.7")

    plt.figure(figsize=(9, 4))
    for label, series in values.items():
        plt.plot(series, label=label)
    plt.xlabel("t")
    plt.ylabel("value")
    plt.title("Positive and negative autoregressive dependence")
    plt.legend()
    save_figure(FIGURE_DIR, "03_ar_persistence.png")


def ma_shock_duration() -> None:
    n = 20
    impulse = np.zeros(n)
    impulse[0] = 1.0
    theta = 0.7
    ma1 = impulse.copy()
    ma1[1] = theta
    ma2 = impulse.copy()
    ma2[1:3] = [0.7, -0.35]
    print(
        f"MA impulse response: MA(1) weights={ma1[:4]}, "
        f"MA(2) weights={ma2[:4]}"
    )

    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    axes[0].stem(np.arange(n), ma1, basefmt=" ")
    axes[0].set_title("One shock in an MA(1)")
    axes[1].stem(np.arange(n), ma2, basefmt=" ")
    axes[1].set_title("One shock in an MA(2)")
    for ax in axes:
        ax.set_xlabel("lag")
        ax.set_ylabel("response")
    save_figure(FIGURE_DIR, "04_ma_shock_duration.png")


def backshift_operations() -> None:
    values = np.array([8.0, 10.0, 13.0, 12.0, 15.0])
    first = np.diff(values)
    second = np.diff(values, n=2)
    print(
        f"backshift: y_5={values[-1]:.1f}, By_5={values[-2]:.1f}, "
        f"(1-B)y_5={first[-1]:.1f}, (1-B)^2y_5={second[-1]:.1f}"
    )

    fig, axes = plt.subplots(1, 3, figsize=(11, 3.5))
    axes[0].plot(np.arange(1, 6), values, marker="o")
    axes[0].set_title("y_t")
    axes[1].bar(np.arange(2, 6), first, color="tab:orange")
    axes[1].set_title("(1-B)y_t")
    axes[2].bar(np.arange(3, 6), second, color="tab:green")
    axes[2].set_title("(1-B)^2 y_t")
    for ax in axes:
        ax.axhline(0, color="0.35", linewidth=0.8)
        ax.set_xlabel("t")
    save_figure(FIGURE_DIR, "05_backshift_differences.png")


def invertibility() -> None:
    lags = np.arange(12)
    inverse_stable = (-0.5) ** lags
    inverse_unstable = (-2.0) ** lags
    print(
        f"invertibility: stable inverse first weights={inverse_stable[:5]}; "
        f"non-invertible first weights={inverse_unstable[:5]}"
    )

    fig, axes = plt.subplots(1, 2, figsize=(10, 4), sharey=True)
    axes[0].stem(lags, inverse_stable, basefmt=" ")
    axes[0].set_title("theta=0.5: decaying inverse")
    axes[1].stem(lags, inverse_unstable, basefmt=" ")
    axes[1].set_title("theta=2: exploding inverse")
    for ax in axes:
        ax.set_xlabel("inverse-filter lag")
    axes[0].set_ylabel("weight")
    save_figure(FIGURE_DIR, "06_invertibility.png")


def yule_walker() -> None:
    phi1, phi2 = 0.6, -0.2
    rho = np.zeros(15)
    rho[0] = 1.0
    rho[1] = phi1 / (1 - phi2)
    rho[2] = phi1 * rho[1] + phi2
    for lag in range(3, len(rho)):
        rho[lag] = phi1 * rho[lag - 1] + phi2 * rho[lag - 2]
    print(
        f"Yule-Walker: rho_1={rho[1]:.4f}, rho_2={rho[2]:.4f}, "
        f"rho_3={rho[3]:.4f}, rho_4={rho[4]:.4f}"
    )

    plt.figure(figsize=(8, 4))
    stem(plt.gca(), rho, "AR(2) autocorrelation from Yule-Walker equations")
    save_figure(FIGURE_DIR, "07_yule_walker_recursion.png")


def randomness_and_residuals() -> None:
    rng = np.random.default_rng(304)
    white = rng.normal(size=220)
    dependent = simulate_ar1(rng, 0.75, 220)
    white_acf = acf(white, 18)
    dependent_acf = acf(dependent, 18)
    print(
        f"randomness diagnostics: white-noise lag-1 ACF={white_acf[1]:.4f}; "
        f"dependent lag-1 ACF={dependent_acf[1]:.4f}"
    )

    fig, axes = plt.subplots(2, 2, figsize=(10, 6))
    axes[0, 0].plot(white)
    axes[0, 0].set_title("white-noise residuals")
    axes[0, 1].plot(dependent)
    axes[0, 1].set_title("residuals with dependence")
    stem(axes[1, 0], white_acf, "white-noise ACF")
    stem(axes[1, 1], dependent_acf, "dependent ACF", "tab:red")
    save_figure(FIGURE_DIR, "08_randomness_residual_diagnostics.png")


def main() -> None:
    covariance_geometry()
    acf_pacf_ar2()
    ar_persistence()
    ma_shock_duration()
    backshift_operations()
    invertibility()
    yule_walker()
    randomness_and_residuals()


if __name__ == "__main__":
    main()
