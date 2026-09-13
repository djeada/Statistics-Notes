"""State-space filtering and frequency-domain visualizations."""

import matplotlib.pyplot as plt
import numpy as np

from student_plot_utils import (
    acf,
    kalman_filter,
    output_dir,
    save_figure,
    simulate_local_level,
)


FIGURE_DIR = output_dir("state_space_frequency")


def local_level() -> None:
    rng = np.random.default_rng(701)
    state, observations = simulate_local_level(
        rng, n=220, process_variance=0.10, measurement_variance=1.0
    )
    filtered, gains, _ = kalman_filter(observations, 0.10, 1.0)
    print(
        f"local level: observation RMSE={np.sqrt(np.mean((observations-state)**2)):.4f}; "
        f"filtered RMSE={np.sqrt(np.mean((filtered-state)**2)):.4f}; "
        f"first/last gain={gains[0]:.4f}/{gains[-1]:.4f}"
    )

    plt.figure(figsize=(9, 4))
    plt.plot(observations, color="0.65", label="observations")
    plt.plot(state, color="black", label="latent state")
    plt.plot(filtered, color="tab:blue", linewidth=2, label="filtered level")
    plt.xlabel("t")
    plt.ylabel("value")
    plt.title("A local-level state-space model")
    plt.legend()
    save_figure(FIGURE_DIR, "01_local_level_filter.png")


def kalman_gain() -> None:
    measurement_variances = np.logspace(-2, 2, 80)
    process_variance = 0.2
    gains = []
    for measurement_variance in measurement_variances:
        predicted_variance = 1.0 + process_variance
        gains.append(predicted_variance / (predicted_variance + measurement_variance))
    print(
        f"Kalman gain: R=0.01 gives {gains[0]:.4f}; "
        f"R=100 gives {gains[-1]:.4f}"
    )

    plt.figure(figsize=(8, 4))
    plt.semilogx(measurement_variances, gains)
    plt.xlabel("measurement variance R")
    plt.ylabel("Kalman gain")
    plt.title("Noisier measurements receive less weight")
    save_figure(FIGURE_DIR, "02_kalman_gain.png")


def missing_observations() -> None:
    rng = np.random.default_rng(702)
    state, observations = simulate_local_level(
        rng, n=180, process_variance=0.12, measurement_variance=0.8
    )
    missing = np.arange(70, 91)
    observations_with_missing = observations.copy()
    observations_with_missing[missing] = np.nan
    filtered, gains, variances = kalman_filter(
        observations_with_missing, 0.12, 0.8
    )
    print(
        f"missing observations: variance before gap={variances[69]:.4f}; "
        f"variance at gap end={variances[90]:.4f}; "
        f"gain at gap end={gains[90]:.4f}"
    )

    plt.figure(figsize=(9, 4))
    plt.plot(state, color="black", label="latent state")
    plt.scatter(np.arange(len(observations)), observations_with_missing, s=12, label="observed")
    plt.plot(filtered, color="tab:blue", label="filtered state")
    plt.axvspan(missing[0], missing[-1], color="tab:orange", alpha=0.18, label="missing block")
    plt.xlabel("t")
    plt.ylabel("value")
    plt.title("Prediction continues when a measurement is missing")
    plt.legend()
    save_figure(FIGURE_DIR, "03_missing_observations.png")


def filtering_and_smoothing() -> None:
    rng = np.random.default_rng(703)
    state, observations = simulate_local_level(
        rng, n=200, process_variance=0.05, measurement_variance=1.2
    )
    filtered, _, _ = kalman_filter(observations, 0.05, 1.2)
    smoothed = np.convolve(filtered, np.ones(9) / 9, mode="same")
    print(
        f"filtering/smoothing: filtered RMSE={np.sqrt(np.mean((filtered-state)**2)):.4f}; "
        f"smoothed interior RMSE={np.sqrt(np.mean((smoothed[4:-4]-state[4:-4])**2)):.4f}"
    )

    plt.figure(figsize=(9, 4))
    plt.plot(state, color="black", label="latent state")
    plt.plot(observations, color="0.75", label="observations")
    plt.plot(filtered, color="tab:blue", label="filter: data through t")
    plt.plot(smoothed, color="tab:red", label="retrospective smoother")
    plt.xlabel("t")
    plt.ylabel("value")
    plt.title("Filtering is real-time; smoothing uses later observations")
    plt.legend()
    save_figure(FIGURE_DIR, "04_filtering_vs_smoothing.png")


def periodogram() -> None:
    rng = np.random.default_rng(704)
    n = 240
    t = np.arange(n)
    values = 1.8 * np.sin(2 * np.pi * t / 12) + 0.8 * np.sin(
        2 * np.pi * t / 30
    ) + rng.normal(scale=0.7, size=n)
    frequencies = np.fft.rfftfreq(n)
    power = np.abs(np.fft.rfft(values - values.mean())) ** 2 / n
    positive = frequencies > 0
    peak = np.argmax(power[positive])
    peak_frequency = frequencies[positive][peak]
    print(
        f"periodogram: peak frequency={peak_frequency:.5f}; "
        f"period={1/peak_frequency:.3f}; frequency resolution={1/n:.5f}"
    )

    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    axes[0].plot(values)
    axes[0].set_title("signal with two periodic components")
    axes[0].set_xlabel("t")
    axes[1].plot(frequencies[positive], power[positive])
    axes[1].axvline(peak_frequency, color="tab:red", linestyle="--")
    axes[1].set_title("periodogram")
    axes[1].set_xlabel("cycles per observation")
    axes[1].set_ylabel("power")
    save_figure(FIGURE_DIR, "05_periodogram.png")


def leakage_and_windowing() -> None:
    n = 100
    t = np.arange(n)
    frequency = 0.137
    signal = np.sin(2 * np.pi * frequency * t)
    window = 0.5 - 0.5 * np.cos(2 * np.pi * t / (n - 1))
    raw_power = np.abs(np.fft.rfft(signal)) ** 2
    windowed_power = np.abs(np.fft.rfft(signal * window)) ** 2
    frequencies = np.fft.rfftfreq(n)
    print(
        f"leakage: signal frequency={frequency:.3f}; "
        f"raw peak={frequencies[np.argmax(raw_power)]:.3f}; "
        f"windowed peak={frequencies[np.argmax(windowed_power)]:.3f}"
    )

    plt.figure(figsize=(9, 4))
    plt.plot(frequencies[1:], raw_power[1:] / raw_power[1:].max(), label="rectangular window")
    plt.plot(
        frequencies[1:],
        windowed_power[1:] / windowed_power[1:].max(),
        label="cosine taper",
    )
    plt.xlabel("frequency")
    plt.ylabel("scaled power")
    plt.title("Windowing changes leakage and peak width")
    plt.legend()
    save_figure(FIGURE_DIR, "06_spectral_leakage_windowing.png")


def aliasing() -> None:
    fine_t = np.linspace(0, 10, 2000)
    high_frequency = 0.65
    fine_signal = np.sin(2 * np.pi * high_frequency * fine_t)
    sample_t = np.arange(0, 10.01, 0.5)
    sampled = np.sin(2 * np.pi * high_frequency * sample_t)
    alias_frequency = abs(high_frequency - round(high_frequency))
    print(
        f"aliasing: original frequency={high_frequency:.2f}; "
        f"sampling interval=0.5; apparent alias frequency={alias_frequency:.2f}"
    )

    plt.figure(figsize=(9, 4))
    plt.plot(fine_t, fine_signal, color="0.7", label="continuous signal")
    plt.scatter(sample_t, sampled, color="tab:red", s=18, label="sampled values")
    plt.xlabel("time")
    plt.ylabel("value")
    plt.title("Sampling above the Nyquist limit produces an alias")
    plt.legend()
    save_figure(FIGURE_DIR, "07_aliasing.png")


def coherence_like_comparison() -> None:
    rng = np.random.default_rng(705)
    n = 240
    t = np.arange(n)
    shared = np.sin(2 * np.pi * t / 15)
    first = shared + rng.normal(scale=0.7, size=n)
    second = 0.8 * shared + rng.normal(scale=0.7, size=n)
    first_power = np.abs(np.fft.rfft(first - first.mean())) ** 2
    second_power = np.abs(np.fft.rfft(second - second.mean())) ** 2
    cross = np.fft.rfft(first - first.mean()) * np.conjugate(
        np.fft.rfft(second - second.mean())
    )
    coherence = np.abs(cross) ** 2 / (first_power * second_power)
    frequencies = np.fft.rfftfreq(n)
    print(
        f"frequency relationship: largest coherence frequency="
        f"{frequencies[1 + np.argmax(coherence[1:])]:.5f}"
    )

    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    axes[0].plot(first, label="series 1")
    axes[0].plot(second, label="series 2")
    axes[0].set_title("Two series with a shared cycle")
    axes[0].legend()
    axes[1].plot(frequencies[1:], coherence[1:])
    axes[1].set_ylim(0, 1.05)
    axes[1].set_title("Frequency-specific squared coherence")
    axes[1].set_xlabel("frequency")
    axes[1].set_ylabel("coherence")
    save_figure(FIGURE_DIR, "08_frequency_relationship.png")


def main() -> None:
    local_level()
    kalman_gain()
    missing_observations()
    filtering_and_smoothing()
    periodogram()
    leakage_and_windowing()
    aliasing()
    coherence_like_comparison()


if __name__ == "__main__":
    main()
