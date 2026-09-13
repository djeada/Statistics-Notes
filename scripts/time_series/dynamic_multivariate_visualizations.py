"""Dynamic regression and multivariate time-series visualizations."""

import matplotlib.pyplot as plt
import numpy as np

from student_plot_utils import acf, output_dir, save_figure, simulate_ar1


FIGURE_DIR = output_dir("dynamic_multivariate")


def dynamic_regression() -> None:
    rng = np.random.default_rng(601)
    n = 220
    x = rng.normal(size=n)
    errors = simulate_ar1(rng, 0.75, n, innovation_scale=0.8)
    y = 2.0 + 1.5 * x + errors
    slope, intercept = np.polyfit(x, y, 1)
    residuals = y - (intercept + slope * x)
    print(
        f"dynamic regression: true slope=1.5; OLS slope={slope:.4f}; "
        f"residual ACF_1={acf(residuals, 1)[1]:.4f}"
    )

    order = np.argsort(x)
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    axes[0].scatter(x, y, alpha=0.45)
    axes[0].plot(x[order], (intercept + slope * x)[order], color="tab:red")
    axes[0].set_title("Regression mean")
    axes[0].set_xlabel("x_t")
    axes[0].set_ylabel("y_t")
    axes[1].plot(residuals)
    axes[1].set_title("Autocorrelated residuals")
    axes[1].set_xlabel("t")
    save_figure(FIGURE_DIR, "01_dynamic_regression_errors.png")


def distributed_lag() -> None:
    rng = np.random.default_rng(602)
    n = 180
    x = rng.normal(size=n)
    response = np.zeros(n)
    weights = np.array([1.0, 0.6, 0.25])
    for t in range(2, n):
        response[t] = (
            weights[0] * x[t]
            + weights[1] * x[t - 1]
            + weights[2] * x[t - 2]
            + rng.normal(scale=0.5)
        )
    print(
        f"distributed lag weights={weights}; total contemporaneous-plus-lag effect="
        f"{weights.sum():.2f}"
    )

    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    axes[0].stem(np.arange(3), weights, basefmt=" ")
    axes[0].set_xticks([0, 1, 2], ["x_t", "x_(t-1)", "x_(t-2)"])
    axes[0].set_title("Distributed-lag coefficients")
    axes[1].plot(x, label="predictor")
    axes[1].plot(response, label="response")
    axes[1].set_title("Delayed predictor response")
    axes[1].legend()
    save_figure(FIGURE_DIR, "02_distributed_lag.png")


def future_predictor_availability() -> None:
    t = np.arange(80)
    known_calendar = (t % 7 == 0).astype(float)
    realized_weather = 10 + 4 * np.sin(2 * np.pi * t / 30)
    forecast_weather = realized_weather.copy()
    forecast_weather[50:] = realized_weather[49]
    print(
        "future predictors: calendar values are known at the origin; "
        f"weather value at t=60 realized={realized_weather[60]:.2f}, "
        f"available forecast={forecast_weather[60]:.2f}"
    )

    plt.figure(figsize=(9, 4))
    plt.plot(t, realized_weather, label="realized weather")
    plt.plot(t[50:], forecast_weather[50:], linestyle="--", label="available forecast")
    plt.scatter(
        t[known_calendar == 1],
        np.full(int(np.sum(known_calendar)), 9.5),
        label="known calendar event",
    )
    plt.axvline(50, color="0.4", linestyle=":")
    plt.text(51, 13.5, "forecast origin")
    plt.xlabel("t")
    plt.ylabel("predictor")
    plt.title("Realized future predictors can leak into evaluation")
    plt.legend()
    save_figure(FIGURE_DIR, "03_future_predictor_availability.png")


def var_feedback() -> None:
    rng = np.random.default_rng(603)
    n = 180
    x = np.zeros(n)
    y = np.zeros(n)
    shocks = rng.normal(scale=0.6, size=(2, n))
    for t in range(1, n):
        x[t] = 0.65 * x[t - 1] + 0.20 * y[t - 1] + shocks[0, t]
        y[t] = -0.15 * x[t - 1] + 0.55 * y[t - 1] + shocks[1, t]
    print(
        f"VAR feedback: x_1={x[1]:.3f}, y_1={y[1]:.3f}; "
        f"corr(x_t,y_(t-1))={np.corrcoef(x[1:], y[:-1])[0,1]:.4f}"
    )

    fig, axes = plt.subplots(2, 1, figsize=(9, 6), sharex=True)
    axes[0].plot(x, label="x_t")
    axes[0].plot(y, label="y_t")
    axes[0].set_title("A VAR allows feedback between series")
    axes[0].legend()
    axes[1].scatter(x[:-1], y[1:], s=12, alpha=0.5)
    axes[1].set_xlabel("x_(t-1)")
    axes[1].set_ylabel("y_t")
    axes[1].set_title("A lagged cross-variable relationship")
    save_figure(FIGURE_DIR, "04_var_feedback.png")


def granger_predictability() -> None:
    rng = np.random.default_rng(604)
    n = 220
    x = rng.normal(size=n)
    y = np.zeros(n)
    for t in range(1, n):
        y[t] = 0.65 * y[t - 1] + 0.45 * x[t - 1] + rng.normal(scale=0.8)
    unrestricted = 0.65 * y[:-1] + 0.45 * x[:-1]
    restricted = 0.65 * y[:-1]
    unrestricted_error = y[1:] - unrestricted
    restricted_error = y[1:] - restricted
    print(
        f"Granger illustration: restricted MSE={np.mean(restricted_error**2):.4f}; "
        f"unrestricted MSE={np.mean(unrestricted_error**2):.4f}"
    )

    plt.figure(figsize=(9, 4))
    plt.plot(y, label="target y_t")
    plt.plot(x, alpha=0.65, label="predictor x_t")
    plt.title("Past x improves prediction of y in the simulated system")
    plt.xlabel("t")
    plt.ylabel("value")
    plt.legend()
    save_figure(FIGURE_DIR, "05_granger_predictability.png")


def cointegration() -> None:
    rng = np.random.default_rng(605)
    n = 240
    x = np.cumsum(rng.normal(scale=0.7, size=n))
    spread = simulate_ar1(rng, 0.7, n, innovation_scale=0.35)
    y = 1.4 * x + spread
    print(
        f"cointegration: corr(levels)={np.corrcoef(x,y)[0,1]:.4f}; "
        f"std(x)={x.std():.3f}; std(spread)={spread.std():.3f}"
    )

    fig, axes = plt.subplots(2, 1, figsize=(9, 6), sharex=True)
    axes[0].plot(x, label="x_t")
    axes[0].plot(y, label="y_t")
    axes[0].set_title("Non-stationary levels")
    axes[0].legend()
    axes[1].plot(y - 1.4 * x, color="tab:orange")
    axes[1].axhline(0, color="0.35", linewidth=0.8)
    axes[1].set_title("Stationary-looking cointegrating spread")
    axes[1].set_xlabel("t")
    save_figure(FIGURE_DIR, "06_cointegrating_spread.png")


def vecm_adjustment() -> None:
    deviations = np.linspace(-4, 4, 100)
    alpha_x = -0.25
    alpha_y = 0.40
    adjustment_x = alpha_x * deviations
    adjustment_y = alpha_y * deviations
    print(
        f"VECM adjustment: spread=2 gives delta_x={alpha_x*2:.2f}, "
        f"delta_y={alpha_y*2:.2f}"
    )

    plt.figure(figsize=(8, 4))
    plt.plot(deviations, adjustment_x, label="Delta x")
    plt.plot(deviations, adjustment_y, label="Delta y")
    plt.axhline(0, color="0.35", linewidth=0.8)
    plt.axvline(0, color="0.35", linewidth=0.8)
    plt.xlabel("lagged spread")
    plt.ylabel("error-correction contribution")
    plt.title("Adjustment coefficients determine return toward equilibrium")
    plt.legend()
    save_figure(FIGURE_DIR, "07_vecm_adjustment.png")


def impulse_response() -> None:
    horizon = np.arange(13)
    response_x = 0.75**horizon
    response_y = np.zeros_like(horizon, dtype=float)
    for t in range(1, len(horizon)):
        response_y[t] = 0.25 * response_x[t - 1] + 0.55 * response_y[t - 1]
    print(
        f"impulse response: x response at h=0,1,4="
        f"{response_x[0]:.2f},{response_x[1]:.2f},{response_x[4]:.2f}; "
        f"y response at h=4={response_y[4]:.4f}"
    )

    plt.figure(figsize=(8, 4))
    plt.stem(horizon, response_x, linefmt="tab:blue", markerfmt="o", basefmt=" ", label="x")
    plt.stem(horizon, response_y, linefmt="tab:orange", markerfmt="o", basefmt=" ", label="y")
    plt.xlabel("horizon")
    plt.ylabel("response")
    plt.title("Impulse responses depend on the dynamic system and identification")
    plt.legend()
    save_figure(FIGURE_DIR, "08_impulse_response.png")


def main() -> None:
    dynamic_regression()
    distributed_lag()
    future_predictor_availability()
    var_feedback()
    granger_predictability()
    cointegration()
    vecm_adjustment()
    impulse_response()


if __name__ == "__main__":
    main()
