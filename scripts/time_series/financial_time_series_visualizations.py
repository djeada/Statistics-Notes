"""Financial-return and conditional-volatility visualizations."""

import matplotlib.pyplot as plt
import numpy as np

from student_plot_utils import acf, output_dir, save_figure


FIGURE_DIR = output_dir("financial")


def prices_and_returns() -> None:
    rng = np.random.default_rng(801)
    n = 220
    returns = rng.normal(loc=0.001, scale=0.02, size=n)
    prices = 100 * np.exp(np.cumsum(returns))
    log_returns = np.diff(np.log(prices))
    print(
        f"returns: price_0={prices[0]:.2f}; price_1={prices[1]:.2f}; "
        f"log return_1={log_returns[0]:.5f}; return mean={log_returns.mean():.5f}"
    )

    fig, axes = plt.subplots(2, 1, figsize=(9, 6), sharex=True)
    axes[0].plot(prices)
    axes[0].set_title("Price level")
    axes[1].plot(log_returns, color="tab:orange")
    axes[1].axhline(0, color="0.35", linewidth=0.8)
    axes[1].set_title("Log returns")
    axes[1].set_xlabel("t")
    save_figure(FIGURE_DIR, "01_prices_and_returns.png")


def arch_process() -> None:
    rng = np.random.default_rng(802)
    n = 260
    alpha0, alpha1 = 0.02, 0.35
    variance = np.zeros(n)
    returns = np.zeros(n)
    variance[0] = alpha0 / (1 - alpha1)
    for t in range(1, n):
        variance[t] = alpha0 + alpha1 * returns[t - 1] ** 2
        returns[t] = rng.normal(scale=np.sqrt(variance[t]))
    print(
        f"ARCH(1): alpha0={alpha0}; alpha1={alpha1}; "
        f"variance at t=100={variance[100]:.5f}"
    )

    fig, axes = plt.subplots(2, 1, figsize=(9, 6), sharex=True)
    axes[0].plot(returns)
    axes[0].set_title("ARCH-style returns")
    axes[1].plot(variance, color="tab:red")
    axes[1].set_title("Variance reacts to the previous squared return")
    axes[1].set_xlabel("t")
    save_figure(FIGURE_DIR, "02_arch_variance.png")


def garch_persistence() -> None:
    rng = np.random.default_rng(803)
    n = 260
    alpha0, alpha1, beta1 = 0.01, 0.10, 0.85
    variance = np.zeros(n)
    returns = np.zeros(n)
    variance[0] = alpha0 / (1 - alpha1 - beta1)
    for t in range(1, n):
        variance[t] = (
            alpha0 + alpha1 * returns[t - 1] ** 2 + beta1 * variance[t - 1]
        )
        returns[t] = rng.normal(scale=np.sqrt(variance[t]))
    persistence = alpha1 + beta1
    print(
        f"GARCH(1,1): alpha+beta={persistence:.2f}; "
        f"long-run variance={alpha0/(1-persistence):.4f}"
    )

    fig, axes = plt.subplots(2, 1, figsize=(9, 6), sharex=True)
    axes[0].plot(returns)
    axes[0].set_title("GARCH(1,1)-style returns")
    axes[1].plot(np.sqrt(variance), color="tab:red")
    axes[1].set_title("Persistent conditional standard deviation")
    axes[1].set_xlabel("t")
    save_figure(FIGURE_DIR, "03_garch_persistence.png")


def squared_return_dependence() -> None:
    rng = np.random.default_rng(804)
    n = 320
    alpha0, alpha1, beta1 = 0.01, 0.12, 0.82
    variance = np.zeros(n)
    returns = np.zeros(n)
    variance[0] = alpha0 / (1 - alpha1 - beta1)
    for t in range(1, n):
        variance[t] = alpha0 + alpha1 * returns[t - 1] ** 2 + beta1 * variance[t - 1]
        returns[t] = rng.normal(scale=np.sqrt(variance[t]))
    return_acf = acf(returns, 18)
    square_acf = acf(returns**2, 18)
    print(
        f"volatility dependence: return ACF_1={return_acf[1]:.4f}; "
        f"squared-return ACF_1={square_acf[1]:.4f}"
    )

    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    axes[0].stem(np.arange(len(return_acf)), return_acf, basefmt=" ")
    axes[0].set_title("ACF of returns")
    axes[1].stem(np.arange(len(square_acf)), square_acf, basefmt=" ")
    axes[1].set_title("ACF of squared returns")
    for ax in axes:
        ax.set_xlabel("lag")
        ax.set_ylabel("ACF")
    save_figure(FIGURE_DIR, "04_returns_vs_squared_returns.png")


def shock_response() -> None:
    alpha0, alpha1, beta1 = 0.01, 0.10, 0.85
    baseline = alpha0 / (1 - alpha1 - beta1)
    shock = np.zeros(25)
    shock[0] = 0.25
    variance = np.zeros(25)
    variance[0] = alpha0 + alpha1 * shock[0] ** 2 + beta1 * baseline
    for t in range(1, len(variance)):
        variance[t] = alpha0 + beta1 * variance[t - 1]
    print(
        f"shock response: baseline variance={baseline:.4f}; "
        f"variance after shock={variance[0]:.4f}; "
        f"variance after 10 periods={variance[10]:.4f}"
    )

    plt.figure(figsize=(8, 4))
    plt.plot(np.sqrt(variance), marker="o", label="conditional sd")
    plt.axhline(np.sqrt(baseline), color="tab:red", linestyle="--", label="long-run sd")
    plt.xlabel("period after shock")
    plt.ylabel("standard deviation")
    plt.title("A volatility shock decays gradually in a persistent GARCH model")
    plt.legend()
    save_figure(FIGURE_DIR, "05_volatility_shock_response.png")


def leverage_effect() -> None:
    alpha0, alpha, gamma, beta = 0.01, 0.08, 0.12, 0.82
    previous_variance = 0.04
    positive = alpha0 + alpha * 0.16 + beta * previous_variance
    negative = alpha0 + (alpha + gamma) * 0.16 + beta * previous_variance
    print(
        f"leverage illustration: positive-shock variance={positive:.4f}; "
        f"negative-shock variance={negative:.4f}"
    )

    plt.figure(figsize=(8, 4))
    shocks = np.linspace(-0.5, 0.5, 120)
    variance = alpha0 + alpha * shocks**2 + beta * previous_variance
    negative_extra = gamma * shocks**2 * (shocks < 0)
    plt.plot(shocks, variance, label="symmetric response")
    plt.plot(shocks, variance + negative_extra, label="leverage response")
    plt.axvline(0, color="0.35", linewidth=0.8)
    plt.xlabel("previous return shock")
    plt.ylabel("next conditional variance")
    plt.title("Asymmetric volatility responses")
    plt.legend()
    save_figure(FIGURE_DIR, "06_leverage_effect.png")


def heavy_tails() -> None:
    rng = np.random.default_rng(805)
    normal = rng.normal(size=5000)
    heavy = rng.standard_t(df=4, size=5000) / np.sqrt(2)
    print(
        f"heavy tails: normal |x|>3 proportion={np.mean(np.abs(normal)>3):.4f}; "
        f"t_4 |x|>3 proportion={np.mean(np.abs(heavy)>3):.4f}"
    )

    plt.figure(figsize=(8, 4))
    plt.hist(normal, bins=70, density=True, alpha=0.55, label="normal")
    plt.hist(heavy, bins=70, density=True, alpha=0.55, label="scaled t(4)")
    plt.xlim(-6, 6)
    plt.xlabel("standardized return")
    plt.ylabel("density")
    plt.title("Heavy tails change the probability of extreme returns")
    plt.legend()
    save_figure(FIGURE_DIR, "07_heavy_tails.png")


def price_scale_and_log_scale() -> None:
    rng = np.random.default_rng(806)
    n = 160
    log_returns = rng.normal(loc=0.003, scale=0.025, size=n)
    log_price = np.log(100) + np.cumsum(log_returns)
    price = np.exp(log_price)
    print(
        f"scales: arithmetic change first/last={price[1]-price[0]:.4f}/"
        f"{price[-1]-price[-2]:.4f}; log-return mean={log_returns.mean():.5f}"
    )

    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    axes[0].plot(price)
    axes[0].set_title("Price scale")
    axes[1].plot(log_price)
    axes[1].set_title("Log-price scale")
    axes[0].set_xlabel("t")
    axes[1].set_xlabel("t")
    save_figure(FIGURE_DIR, "08_price_and_log_price.png")


def main() -> None:
    prices_and_returns()
    arch_process()
    garch_persistence()
    squared_return_dependence()
    shock_response()
    leverage_effect()
    heavy_tails()
    price_scale_and_log_scale()


if __name__ == "__main__":
    main()
