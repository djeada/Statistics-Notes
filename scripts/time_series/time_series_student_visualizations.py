"""Generate worked time-series figures and print the numerical checkpoints.

The existing time-series unit already contains several figures.  This script
adds a small, reproducible set of figures for the worked explanations in the
student notes.  It uses only NumPy and Matplotlib so that the calculations are
visible rather than hidden inside a model-fitting library.

Run from the repository root with:

    python scripts/time_series/time_series_student_visualizations.py

Figures are written to assets/time_series/student.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


REPO_ROOT = Path(__file__).resolve().parents[2]
FIGURE_DIR = REPO_ROOT / "assets" / "time_series" / "student"
FIGURE_DIR.mkdir(parents=True, exist_ok=True)


def save_figure(name: str) -> None:
    path = FIGURE_DIR / name
    plt.tight_layout()
    plt.savefig(path, dpi=180, bbox_inches="tight")
    plt.close()
    print(f"created {path.relative_to(REPO_ROOT)}")


def acf(values: np.ndarray, max_lag: int) -> np.ndarray:
    centered = np.asarray(values, dtype=float) - np.mean(values)
    denominator = np.dot(centered, centered)
    result = np.empty(max_lag + 1)
    result[0] = 1.0
    for lag in range(1, max_lag + 1):
        result[lag] = np.dot(centered[:-lag], centered[lag:]) / denominator
    return result


def pacf_from_acf(acf_values: np.ndarray) -> np.ndarray:
    """Levinson-style recursion from an autocorrelation sequence."""
    max_lag = len(acf_values) - 1
    coefficients = np.zeros((max_lag + 1, max_lag + 1))
    partial = np.zeros(max_lag + 1)
    partial[0] = 1.0
    for order in range(1, max_lag + 1):
        numerator = acf_values[order]
        denominator = 1.0
        for j in range(1, order):
            numerator -= coefficients[order - 1, j] * acf_values[order - j]
            denominator -= coefficients[order - 1, j] * acf_values[j]
        coefficients[order, order] = numerator / denominator
        for j in range(1, order):
            coefficients[order, j] = (
                coefficients[order - 1, j]
                - coefficients[order, order] * coefficients[order - 1, order - j]
            )
        partial[order] = coefficients[order, order]
    return partial


def stem(ax: plt.Axes, values: np.ndarray, title: str, color: str = "tab:blue") -> None:
    lags = np.arange(len(values))
    ax.stem(lags, values, linefmt=color, markerfmt="o", basefmt=" ")
    ax.axhline(0, color="0.35", linewidth=0.8)
    ax.set_title(title)
    ax.set_xlabel("Lag")


def simulate_ar1(rng: np.random.Generator, phi: float, n: int = 240) -> np.ndarray:
    values = np.zeros(n)
    shocks = rng.normal(size=n)
    for t in range(1, n):
        values[t] = phi * values[t - 1] + shocks[t]
    return values


def simulate_ar2(
    rng: np.random.Generator,
    phi1: float = 0.65,
    phi2: float = -0.25,
    n: int = 300,
) -> np.ndarray:
    values = np.zeros(n)
    shocks = rng.normal(size=n)
    for t in range(2, n):
        values[t] = phi1 * values[t - 1] + phi2 * values[t - 2] + shocks[t]
    return values


def simulate_ma1(rng: np.random.Generator, theta: float = 0.7, n: int = 240) -> np.ndarray:
    shocks = rng.normal(size=n + 1)
    return shocks[1:] + theta * shocks[:-1]


def figure_series() -> None:
    ratio = 0.5
    terms = ratio ** np.arange(11)
    partial = np.cumsum(terms)
    finite_sum = partial[-1]
    infinite_sum = 1 / (1 - ratio)
    print(f"series: sum_(j=0)^10 0.5^j = {finite_sum:.6f}; limit = {infinite_sum:.6f}")

    plt.figure(figsize=(7, 4))
    plt.plot(np.arange(11), partial, marker="o", label="partial sum")
    plt.axhline(infinite_sum, color="tab:red", linestyle="--", label="limit = 2")
    plt.xlabel("Number of terms minus one")
    plt.ylabel("Partial sum")
    plt.title("A geometric series approaches its limit")
    plt.legend()
    save_figure("01_series_partial_sums.png")


def figure_difference_equations() -> None:
    n = 30
    values = np.zeros(n)
    values[0] = 10
    for t in range(1, n):
        values[t] = 0.7 * values[t - 1] + 2
    equilibrium = 2 / (1 - 0.7)
    print(
        "difference equation: x_1 = "
        f"{values[1]:.3f}, x_10 = {values[10]:.3f}, equilibrium = {equilibrium:.3f}"
    )

    plt.figure(figsize=(7, 4))
    plt.plot(values, marker="o", label="x_t")
    plt.axhline(equilibrium, color="tab:red", linestyle="--", label="equilibrium")
    plt.xlabel("t")
    plt.ylabel("x_t")
    plt.title(r"Recursive equation $x_t=0.7x_{t-1}+2$")
    plt.legend()
    save_figure("02_difference_equation.png")


def figure_moments() -> None:
    rng = np.random.default_rng(12)
    n = 240
    low_variance = 10 + rng.normal(scale=0.5, size=n)
    high_variance = 10 + rng.normal(scale=2.0, size=n)
    print(
        "moments: low-variance sample mean/variance = "
        f"{low_variance.mean():.3f}/{low_variance.var(ddof=1):.3f}; "
        "high-variance = "
        f"{high_variance.mean():.3f}/{high_variance.var(ddof=1):.3f}"
    )

    plt.figure(figsize=(8, 4))
    plt.plot(low_variance, label="variance = 0.25")
    plt.plot(high_variance, alpha=0.65, label="variance = 4")
    plt.axhline(10, color="0.25", linestyle="--", linewidth=1)
    plt.xlabel("t")
    plt.ylabel("value")
    plt.title("Equal means do not imply equal time-series behavior")
    plt.legend()
    save_figure("03_moments_mean_and_variance.png")


def figure_white_noise_and_random_walk() -> None:
    rng = np.random.default_rng(21)
    n = 220
    noise = rng.normal(size=n)
    walk = np.cumsum(noise)
    print(
        "white noise/random walk: theoretical Var(e_t) = 1; "
        f"Var(sum of first 100 shocks) = 100"
    )

    fig, axes = plt.subplots(2, 1, figsize=(8, 6), sharex=True)
    axes[0].plot(noise, color="tab:blue")
    axes[0].set_title("White noise: shocks do not accumulate")
    axes[0].set_ylabel("epsilon_t")
    axes[1].plot(walk, color="tab:orange")
    axes[1].set_title("Random walk: the same shocks accumulate")
    axes[1].set_xlabel("t")
    axes[1].set_ylabel("X_t")
    save_figure("04_white_noise_and_random_walk.png")


def figure_autocovariance() -> None:
    rng = np.random.default_rng(31)
    phi = 0.7
    values = simulate_ar1(rng, phi)
    estimated = np.var(values) * acf(values, 15)
    theoretical_gamma0 = 1 / (1 - phi**2)
    theoretical_gamma1 = phi * theoretical_gamma0
    print(
        "AR(1) autocovariance: theoretical gamma_0 = "
        f"{theoretical_gamma0:.6f}, gamma_1 = {theoretical_gamma1:.6f}"
    )

    lags = np.arange(16)
    theoretical = theoretical_gamma0 * phi**lags
    plt.figure(figsize=(8, 4))
    plt.stem(lags, estimated, linefmt="tab:blue", markerfmt="o", basefmt=" ", label="sample")
    plt.plot(lags, theoretical, color="tab:red", linestyle="--", label="theory")
    plt.xlabel("Lag")
    plt.ylabel("autocovariance")
    plt.title("Autocovariance of a stationary AR(1)")
    plt.legend()
    save_figure("05_autocovariance_ar1.png")


def figure_ar_ma_identification() -> None:
    rng = np.random.default_rng(41)
    ar_values = simulate_ar1(rng, 0.75)
    ma_values = simulate_ma1(rng, 0.75)
    ar_acf = acf(ar_values, 18)
    ma_acf = acf(ma_values, 18)
    print(
        "identification: AR(1) theoretical rho_1 = 0.75; "
        f"MA(1) theoretical rho_1 = {0.75 / (1 + 0.75**2):.6f}"
    )

    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    stem(axes[0], ar_acf, "AR(1): ACF tails off")
    stem(axes[1], ma_acf, "MA(1): ACF cuts off after lag 1", "tab:orange")
    save_figure("06_ar_ma_identification.png")


def figure_backward_shift() -> None:
    values = np.array([8.0, 10.0, 13.0, 12.0, 15.0])
    first_difference = values[1:] - values[:-1]
    print(
        "backshift: at t=5, B y_5 = "
        f"{values[-2]:.1f} and (1-B)y_5 = {first_difference[-1]:.1f}"
    )

    fig, axes = plt.subplots(1, 2, figsize=(9, 4))
    axes[0].plot(np.arange(1, 6), values, marker="o")
    axes[0].set_title("Original y_t")
    axes[0].set_xlabel("t")
    axes[1].bar(np.arange(2, 6), first_difference, color="tab:orange")
    axes[1].axhline(0, color="0.35", linewidth=0.8)
    axes[1].set_title("First difference (1 - B)y_t")
    axes[1].set_xlabel("t")
    save_figure("07_backward_shift_difference.png")


def figure_invertibility() -> None:
    theta_values = [0.5, 2.0]
    horizon = np.arange(12)
    fig, axes = plt.subplots(1, 2, figsize=(9, 4), sharey=True)
    for ax, theta in zip(axes, theta_values):
        inverse_weights = (-theta) ** horizon
        ax.stem(horizon, inverse_weights, basefmt=" ")
        ax.set_title(f"MA(1) theta = {theta}")
        ax.set_xlabel("lag in inverse")
        ax.set_ylim(-6, 6)
        print(
            f"invertibility: theta={theta:.1f}, root of 1+theta B = {-1/theta:.3f}, "
            f"first inverse weights={inverse_weights[:4]}"
        )
    axes[0].set_ylabel("inverse-filter weight")
    save_figure("08_invertibility_inverse_weights.png")


def figure_yule_walker() -> None:
    phi1, phi2 = 0.6, -0.2
    rho1 = phi1 / (1 - phi2)
    rho2 = phi1 * rho1 + phi2
    print(f"Yule-Walker: rho_1 = {rho1:.6f}, rho_2 = {rho2:.6f}")

    lags = np.arange(13)
    rho = np.zeros(len(lags))
    rho[0] = 1
    rho[1] = rho1
    rho[2] = rho2
    for lag in range(3, len(lags)):
        rho[lag] = phi1 * rho[lag - 1] + phi2 * rho[lag - 2]
    plt.figure(figsize=(8, 4))
    stem(plt.gca(), rho, "Yule-Walker recursion for an AR(2)")
    save_figure("09_yule_walker_ar2.png")


def figure_stationarity_and_random_walk() -> None:
    rng = np.random.default_rng(51)
    n = 150
    paths = {
        "stationary AR(1), phi=0.7": simulate_ar1(rng, 0.7, n),
        "unit root, phi=1": np.cumsum(rng.normal(size=n)),
        "explosive AR(1), phi=1.03": simulate_ar1(rng, 1.03, n),
    }
    print("stationarity: |phi| < 1 is the AR(1) stability condition")
    plt.figure(figsize=(9, 4))
    for label, values in paths.items():
        plt.plot(values, label=label)
    plt.xlabel("t")
    plt.ylabel("value")
    plt.title("Three AR(1)-type behaviors")
    plt.legend()
    save_figure("10_stationarity_cases.png")


def figure_acf_pacf() -> None:
    rng = np.random.default_rng(61)
    values = simulate_ar2(rng)
    acf_values = acf(values, 18)
    pacf_values = pacf_from_acf(acf_values)
    print(
        f"ACF/PACF: sample rho_1 = {acf_values[1]:.3f}; "
        f"sample PACF_1 = {pacf_values[1]:.3f}; PACF_2 = {pacf_values[2]:.3f}"
    )

    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    stem(axes[0], acf_values, "AR(2) sample ACF")
    stem(axes[1], pacf_values, "AR(2) sample PACF", "tab:green")
    save_figure("11_acf_pacf_ar2.png")


def figure_arima_and_seasonality() -> None:
    rng = np.random.default_rng(71)
    n = 180
    t = np.arange(n)
    integrated = np.cumsum(rng.normal(scale=0.7, size=n))
    differenced = np.diff(integrated)
    seasonal = 10 + 0.03 * t + 2 * np.sin(2 * np.pi * t / 12) + rng.normal(
        scale=0.5, size=n
    )
    seasonal_difference = seasonal[12:] - seasonal[:-12]
    print(
        "differencing: first difference has length "
        f"{len(differenced)}; seasonal difference has length {len(seasonal_difference)}"
    )

    fig, axes = plt.subplots(2, 2, figsize=(10, 6))
    axes[0, 0].plot(integrated)
    axes[0, 0].set_title("Integrated series")
    axes[0, 1].plot(differenced)
    axes[0, 1].set_title("First difference")
    axes[1, 0].plot(seasonal)
    axes[1, 0].set_title("Trend plus period-12 seasonality")
    axes[1, 1].plot(seasonal_difference)
    axes[1, 1].set_title("Seasonal difference, lag 12")
    save_figure("12_arima_and_seasonal_differencing.png")


def figure_modeling_diagnostics() -> None:
    rng = np.random.default_rng(81)
    values = simulate_ar1(rng, 0.8)
    residuals = values[1:] - 0.8 * values[:-1]
    residual_acf = acf(residuals, 16)
    print(
        "model diagnostics: residual mean = "
        f"{residuals.mean():.4f}; residual lag-1 ACF = {residual_acf[1]:.4f}"
    )

    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    axes[0].plot(values, label="observed")
    axes[0].plot(np.arange(1, len(values)), 0.8 * values[:-1], label="one-step mean")
    axes[0].set_title("AR(1) conditional mean")
    axes[0].legend()
    stem(axes[1], residual_acf, "Residual ACF")
    save_figure("13_modeling_residual_diagnostics.png")


def figure_forecasting() -> None:
    rng = np.random.default_rng(91)
    values = simulate_ar1(rng, 0.8, 150)
    origin = 120
    history = values[:origin]
    horizons = np.arange(1, 21)
    ar_forecast = history[-1] * 0.8**horizons
    naive_forecast = np.repeat(history[-1], len(horizons))
    interval = 1.96 * np.sqrt((1 - 0.8 ** (2 * horizons)) / (1 - 0.8**2))
    actual = values[origin : origin + len(horizons)]
    print(
        "forecasting: one-step AR forecast = "
        f"{ar_forecast[0]:.3f}; h=20 forecast = {ar_forecast[-1]:.3f}; "
        f"observed h=1 = {actual[0]:.3f}"
    )

    future = np.arange(origin, origin + len(horizons))
    plt.figure(figsize=(9, 4))
    plt.plot(np.arange(origin), history, color="0.35", label="history")
    plt.plot(future, actual, color="black", label="future observations")
    plt.plot(future, ar_forecast, color="tab:blue", label="AR forecast")
    plt.plot(future, naive_forecast, color="tab:orange", linestyle="--", label="naive")
    plt.fill_between(
        future,
        ar_forecast - interval,
        ar_forecast + interval,
        color="tab:blue",
        alpha=0.16,
        label="approx. 95% interval",
    )
    plt.axvline(origin - 0.5, color="0.5", linestyle=":")
    plt.xlabel("t")
    plt.ylabel("value")
    plt.title("Forecasts diverge as the horizon grows")
    plt.legend(ncol=2)
    save_figure("14_forecasting_intervals.png")


def figure_forecast_evaluation() -> None:
    rng = np.random.default_rng(101)
    values = simulate_ar1(rng, 0.75, 180)
    origins = np.arange(80, 170)
    actual = values[origins]
    naive = values[origins - 1]
    ar_forecast = 0.75 * values[origins - 1]
    naive_mae = np.mean(np.abs(actual - naive))
    ar_mae = np.mean(np.abs(actual - ar_forecast))
    print(
        f"backtesting: naive MAE = {naive_mae:.4f}; "
        f"AR(1) MAE = {ar_mae:.4f}; MASE scale = {np.mean(np.abs(np.diff(values[:80]))):.4f}"
    )

    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    axes[0].plot(origins, actual, label="actual")
    axes[0].plot(origins, naive, label="naive")
    axes[0].plot(origins, ar_forecast, label="AR(1)")
    axes[0].set_title("One-step forecasts at rolling origins")
    axes[0].set_xlabel("forecast origin")
    axes[0].legend()
    errors = [actual - naive, actual - ar_forecast]
    axes[1].boxplot(errors)
    axes[1].set_xticks([1, 2], ["naive", "AR(1)"])
    axes[1].axhline(0, color="0.35", linewidth=0.8)
    axes[1].set_title("Forecast-error distributions")
    axes[1].set_ylabel("error")
    save_figure("15_forecast_backtesting.png")


def figure_dynamic_regression() -> None:
    rng = np.random.default_rng(111)
    n = 180
    x = rng.normal(size=n)
    error = np.zeros(n)
    for t in range(1, n):
        error[t] = 0.75 * error[t - 1] + rng.normal(scale=0.8)
    y = 1.5 + 2.0 * x + error
    beta_ols = np.polyfit(x, y, 1)
    residuals = y - (beta_ols[0] * x + beta_ols[1])
    print(
        f"dynamic regression: OLS slope = {beta_ols[0]:.4f}; "
        f"residual lag-1 ACF = {acf(residuals, 1)[1]:.4f}"
    )

    order = np.argsort(x)
    plt.figure(figsize=(8, 4))
    plt.scatter(x, y, alpha=0.45, label="observations")
    plt.plot(x[order], (beta_ols[0] * x + beta_ols[1])[order], color="tab:red", label="OLS mean")
    plt.xlabel("external predictor x_t")
    plt.ylabel("target y_t")
    plt.title("A useful predictor can coexist with dynamic errors")
    plt.legend()
    save_figure("16_dynamic_regression.png")


def figure_multivariate() -> None:
    rng = np.random.default_rng(121)
    n = 220
    x = np.cumsum(rng.normal(scale=0.6, size=n))
    spread = simulate_ar1(rng, 0.65, n) * 0.5
    y = 1.4 * x + spread
    print(
        f"cointegration example: level correlation = {np.corrcoef(x, y)[0, 1]:.4f}; "
        f"spread lag-1 ACF = {acf(spread, 1)[1]:.4f}"
    )

    fig, axes = plt.subplots(2, 1, figsize=(8, 6), sharex=True)
    axes[0].plot(x, label="x_t")
    axes[0].plot(y, label="y_t")
    axes[0].set_title("Two non-stationary series with a stable spread")
    axes[0].legend()
    axes[1].plot(y - 1.4 * x, color="tab:orange")
    axes[1].axhline(0, color="0.35", linewidth=0.8)
    axes[1].set_title("Cointegrating residual y_t - 1.4 x_t")
    axes[1].set_xlabel("t")
    save_figure("17_multivariate_cointegration.png")


def figure_state_space() -> None:
    rng = np.random.default_rng(131)
    n = 180
    process_variance = 0.12
    measurement_variance = 1.0
    state = np.zeros(n)
    state[0] = 4.0
    state[1:] = state[0] + np.cumsum(
        rng.normal(scale=np.sqrt(process_variance), size=n - 1)
    )
    observations = state + rng.normal(scale=np.sqrt(measurement_variance), size=n)
    filtered = np.zeros(n)
    a, variance = 0.0, 1.0
    first_gain = None
    last_gain = None
    for t, observation in enumerate(observations):
        predicted_variance = variance + process_variance
        gain = predicted_variance / (predicted_variance + measurement_variance)
        a = a + gain * (observation - a)
        variance = (1 - gain) * predicted_variance
        filtered[t] = a
        first_gain = gain if first_gain is None else first_gain
        last_gain = gain
    print(
        f"state space: first Kalman gain = {first_gain:.4f}; "
        f"last Kalman gain = {last_gain:.4f}; "
        f"observation RMSE = {np.sqrt(np.mean((observations-state)**2)):.4f}; "
        f"filtered RMSE = {np.sqrt(np.mean((filtered-state)**2)):.4f}"
    )

    plt.figure(figsize=(9, 4))
    plt.plot(observations, color="0.65", label="observations")
    plt.plot(state, color="black", linewidth=1.5, label="latent state")
    plt.plot(filtered, color="tab:blue", linewidth=2, label="filtered state")
    plt.xlabel("t")
    plt.ylabel("value")
    plt.title("Local-level state-space model")
    plt.legend()
    save_figure("18_state_space_filter.png")


def figure_frequency_domain() -> None:
    rng = np.random.default_rng(141)
    n = 240
    t = np.arange(n)
    period = 12
    values = 1.8 * np.sin(2 * np.pi * t / period) + rng.normal(scale=0.8, size=n)
    centered = values - values.mean()
    frequencies = np.fft.rfftfreq(n)
    power = np.abs(np.fft.rfft(centered)) ** 2 / n
    positive = frequencies > 0
    peak_index = np.argmax(power[positive])
    peak_frequency = frequencies[positive][peak_index]
    print(
        f"frequency domain: peak frequency = {peak_frequency:.5f}; "
        f"estimated period = {1/peak_frequency:.3f}; Nyquist = 0.5"
    )

    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    axes[0].plot(values)
    axes[0].set_title("Signal with a period-12 component")
    axes[0].set_xlabel("t")
    axes[1].plot(frequencies[positive], power[positive])
    axes[1].axvline(peak_frequency, color="tab:red", linestyle="--")
    axes[1].set_title("Periodogram")
    axes[1].set_xlabel("cycles per observation")
    axes[1].set_ylabel("power")
    save_figure("19_frequency_periodogram.png")


def figure_financial_volatility() -> None:
    rng = np.random.default_rng(151)
    n = 240
    returns = np.zeros(n)
    variance = np.zeros(n)
    variance[0] = 0.2
    for t in range(1, n):
        variance[t] = 0.03 + 0.18 * returns[t - 1] ** 2 + 0.75 * variance[t - 1]
        returns[t] = rng.normal(scale=np.sqrt(variance[t]))
    squared_acf = acf(returns**2, 12)
    print(
        f"volatility: return ACF_1 = {acf(returns, 1)[1]:.4f}; "
        f"squared-return ACF_1 = {squared_acf[1]:.4f}"
    )

    fig, axes = plt.subplots(2, 1, figsize=(8, 6), sharex=True)
    axes[0].plot(returns, color="tab:blue")
    axes[0].set_title("Returns")
    axes[1].plot(returns**2, color="tab:orange")
    axes[1].set_title("Squared returns reveal volatility clustering")
    axes[1].set_xlabel("t")
    save_figure("20_financial_volatility.png")


def main() -> None:
    figure_series()
    figure_difference_equations()
    figure_moments()
    figure_white_noise_and_random_walk()
    figure_autocovariance()
    figure_ar_ma_identification()
    figure_backward_shift()
    figure_invertibility()
    figure_yule_walker()
    figure_stationarity_and_random_walk()
    figure_acf_pacf()
    figure_arima_and_seasonality()
    figure_modeling_diagnostics()
    figure_forecasting()
    figure_forecast_evaluation()
    figure_dynamic_regression()
    figure_multivariate()
    figure_state_space()
    figure_frequency_domain()
    figure_financial_volatility()


if __name__ == "__main__":
    main()
