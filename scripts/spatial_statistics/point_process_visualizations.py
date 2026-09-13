"""
Point-process teaching visualizations
=====================================

This script creates the figures referenced in `point_processes.md`.

Dependencies:
    numpy
    matplotlib

Run:
    python scripts/spatial_statistics/point_process_visualizations.py

The implementations are deliberately explicit and educational rather than
optimized for very large point patterns.
"""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


REPO_ROOT = Path(__file__).resolve().parents[2]
FIG_DIR = REPO_ROOT / "assets" / "spatial_statistics" / "point_processes"
FIG_DIR.mkdir(parents=True, exist_ok=True)

WINDOW = (0.0, 10.0, 0.0, 10.0)
WINDOW_AREA = 100.0


def save_and_close(filename):
    path = FIG_DIR / filename
    plt.tight_layout()
    plt.savefig(path, dpi=180, bbox_inches="tight")
    plt.close()
    print(f"created: {path}")


def simulate_homogeneous_poisson(rng, intensity, window=WINDOW):
    """Simulate a full homogeneous Poisson process in a rectangle."""
    xmin, xmax, ymin, ymax = window
    area = (xmax - xmin) * (ymax - ymin)

    n = rng.poisson(intensity * area)
    x = rng.uniform(xmin, xmax, size=n)
    y = rng.uniform(ymin, ymax, size=n)
    return np.column_stack([x, y])


def simulate_fixed_count_uniform(rng, n, window=WINDOW):
    """Simulate n uniform points: Poisson process conditional on N(W)=n."""
    xmin, xmax, ymin, ymax = window
    x = rng.uniform(xmin, xmax, size=n)
    y = rng.uniform(ymin, ymax, size=n)
    return np.column_stack([x, y])


def simulate_inhomogeneous_x_gradient(rng, n, window=WINDOW):
    """
    Simulate a simple x-gradient intensity pattern by inverse-transform sampling.

    Density in x is proportional to 0.35 + 0.13*x over [0,10].
    y remains uniform.
    """
    xmin, xmax, ymin, ymax = window

    # Rejection sampling keeps the code transparent.
    points = []
    max_weight = 0.35 + 0.13 * xmax

    while len(points) < n:
        x = rng.uniform(xmin, xmax)
        y = rng.uniform(ymin, ymax)
        weight = 0.35 + 0.13 * x

        if rng.uniform(0.0, max_weight) <= weight:
            points.append((x, y))

    return np.asarray(points)


def simulate_thomas_like(rng,
                         parent_intensity=0.055,
                         mean_offspring=8.0,
                         cluster_sd=0.45,
                         window=WINDOW):
    """
    Simulate a Thomas-like cluster process.

    Parents are simulated in an expanded region so that offspring from parents
    just outside the observation window may still enter the window.
    """
    xmin, xmax, ymin, ymax = window
    margin = 3.0 * cluster_sd
    expanded = (
        xmin - margin,
        xmax + margin,
        ymin - margin,
        ymax + margin,
    )

    parents = simulate_homogeneous_poisson(
        rng,
        parent_intensity,
        expanded,
    )

    offspring = []

    for parent in parents:
        k = rng.poisson(mean_offspring)
        if k == 0:
            continue

        children = parent + rng.normal(
            loc=0.0,
            scale=cluster_sd,
            size=(k, 2),
        )

        inside = (
            (children[:, 0] >= xmin)
            & (children[:, 0] <= xmax)
            & (children[:, 1] >= ymin)
            & (children[:, 1] <= ymax)
        )

        offspring.extend(children[inside])

    if not offspring:
        return np.empty((0, 2))

    return np.asarray(offspring)


def simulate_sequential_inhibition(rng,
                                   n=55,
                                   hard_core=0.75,
                                   max_attempts=300000,
                                   window=WINDOW):
    """
    Simple sequential inhibition pattern.

    This is an educational hard-core-like construction, not a general sampler
    for every Gibbs hard-core model.
    """
    xmin, xmax, ymin, ymax = window
    points = []

    attempts = 0
    while len(points) < n and attempts < max_attempts:
        attempts += 1
        candidate = np.array([
            rng.uniform(xmin, xmax),
            rng.uniform(ymin, ymax),
        ])

        if not points:
            points.append(candidate)
            continue

        arr = np.asarray(points)
        distances = np.sqrt(np.sum((arr - candidate) ** 2, axis=1))

        if np.all(distances >= hard_core):
            points.append(candidate)

    return np.asarray(points)


def pairwise_distances(points):
    """Full pairwise Euclidean distance matrix."""
    delta = points[:, None, :] - points[None, :, :]
    return np.sqrt(np.sum(delta**2, axis=2))


def nearest_neighbor_distances(points):
    """Nearest-other-event distance for every event."""
    D = pairwise_distances(points)
    np.fill_diagonal(D, np.inf)
    return D.min(axis=1)


def empirical_G(points, radii):
    """Empirical nearest-neighbor distribution G(r)."""
    nn = nearest_neighbor_distances(points)
    return np.array([(nn <= r).mean() for r in radii])


def naive_K(points, radii, area=WINDOW_AREA):
    """
    Naive Ripley's K estimator without edge correction.

    K_hat(r) = A / [n(n-1)] * sum_i sum_{j != i} I(d_ij <= r)
    """
    n = len(points)
    D = pairwise_distances(points)
    np.fill_diagonal(D, np.inf)

    out = []
    for r in radii:
        ordered_pairs = np.sum(D <= r)
        out.append(area * ordered_pairs / (n * (n - 1)))

    return np.asarray(out)


def border_K(points, radii, window=WINDOW):
    """
    Simple border-corrected K estimate.

    For each radius r, only points at least r from every boundary are used
    as focal points. Their neighbors may lie anywhere inside the window.
    """
    xmin, xmax, ymin, ymax = window
    area = (xmax - xmin) * (ymax - ymin)
    n = len(points)
    intensity_hat = n / area

    D = pairwise_distances(points)
    np.fill_diagonal(D, np.inf)

    results = []

    for r in radii:
        border_distance = np.minimum.reduce([
            points[:, 0] - xmin,
            xmax - points[:, 0],
            points[:, 1] - ymin,
            ymax - points[:, 1],
        ])

        focal = border_distance >= r
        n_focal = int(focal.sum())

        if n_focal < 2:
            results.append(np.nan)
            continue

        neighbor_counts = np.sum(D[focal, :] <= r, axis=1)

        # Average count around retained focal points, divided by estimated
        # intensity, directly following the definition of K.
        K_hat = neighbor_counts.mean() / intensity_hat
        results.append(K_hat)

    return np.asarray(results)


def L_minus_r(K, radii):
    """Transform K to L(r)-r."""
    return np.sqrt(K / np.pi) - radii


def figure_01_point_pattern_basics():
    rng = np.random.default_rng(10)
    points = simulate_fixed_count_uniform(rng, 32)

    plt.figure(figsize=(6, 6))
    plt.scatter(points[:, 0], points[:, 1], s=65)
    plt.xlim(0, 10)
    plt.ylim(0, 10)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Point-process data: the event locations are the observations")
    plt.gca().set_aspect("equal", adjustable="box")

    # Study subregion B = [0,4] x [0,3].
    plt.plot([0, 4, 4, 0, 0], [0, 0, 3, 3, 0], linestyle="--")
    plt.annotate("Example counting region B", (0.35, 2.55))
    save_and_close("01_point_pattern_basics.png")


def figure_02_intensity_vs_interaction():
    """
    Overlay two patterns in separated halves of one figure:
    left = inhomogeneous independent pattern
    right = clustered interaction-like pattern.

    Keeping one axes avoids subplot complexity while emphasizing the visual
    similarity of "clusters" created by different mechanisms.
    """
    rng = np.random.default_rng(21)

    inhom = simulate_inhomogeneous_x_gradient(rng, 85)
    cluster = simulate_thomas_like(
        rng,
        parent_intensity=0.05,
        mean_offspring=7.0,
        cluster_sd=0.42,
    )

    # Place the second pattern to the right by 12 units.
    cluster_shifted = cluster.copy()
    cluster_shifted[:, 0] += 12.0

    plt.figure(figsize=(12, 5))
    plt.scatter(inhom[:, 0], inhom[:, 1], s=40, label="Inhomogeneous intensity")
    plt.scatter(
        cluster_shifted[:, 0],
        cluster_shifted[:, 1],
        s=40,
        label="Cluster process",
    )

    plt.plot([11, 11], [0, 10], linestyle=":")
    plt.text(2.2, 10.35, "Independent events, varying intensity")
    plt.text(14.1, 10.35, "Local offspring clusters")
    plt.xlim(0, 22)
    plt.ylim(0, 11)
    plt.xlabel("display coordinate")
    plt.ylabel("y")
    plt.title("Similar-looking clusters can arise from different mechanisms")
    plt.legend()
    save_and_close("02_intensity_vs_interaction.png")


def figure_03_poisson_count_vs_fixed_count():
    rng = np.random.default_rng(44)
    intensity = 0.55

    counts = np.array([
        len(simulate_homogeneous_poisson(rng, intensity))
        for _ in range(1000)
    ])

    fixed_n = int(round(intensity * WINDOW_AREA))

    plt.figure(figsize=(8, 5))
    bins = np.arange(counts.min() - 0.5, counts.max() + 1.5, 1.0)
    plt.hist(counts, bins=bins, alpha=0.7, label="Unconditional Poisson counts")
    plt.axvline(
        fixed_n,
        linestyle="--",
        linewidth=2,
        label=f"Fixed-count simulation: N(W)={fixed_n}",
    )
    plt.xlabel("Number of events in W")
    plt.ylabel("Frequency across 1000 simulations")
    plt.title("A full Poisson process randomizes the count; fixed-count CSR does not")
    plt.legend()
    save_and_close("03_poisson_count_vs_fixed_count.png")


def figure_04_nearest_neighbor_G():
    rng = np.random.default_rng(62)
    intensity = 0.7
    points = simulate_homogeneous_poisson(rng, intensity)

    radii = np.linspace(0.0, 2.2, 180)
    empirical = empirical_G(points, radii)
    theoretical = 1.0 - np.exp(-intensity * np.pi * radii**2)

    plt.figure(figsize=(7, 5))
    plt.plot(radii, theoretical, label="Theoretical CSR G(r)")
    plt.plot(radii, empirical, label="Empirical G(r)")
    plt.xlabel("r")
    plt.ylabel("G(r)")
    plt.title("Nearest-neighbor distribution under homogeneous CSR")
    plt.ylim(0, 1.02)
    plt.legend()
    save_and_close("04_nearest_neighbor_G.png")


def figure_05_edge_effect():
    point = np.array([1.0, 5.0])
    r = 2.6

    theta = np.linspace(0, 2 * np.pi, 400)
    circle_x = point[0] + r * np.cos(theta)
    circle_y = point[1] + r * np.sin(theta)

    plt.figure(figsize=(6, 6))
    plt.plot([0, 10, 10, 0, 0], [0, 0, 10, 10, 0])
    plt.plot(circle_x, circle_y, linestyle="--", label="radius-r neighborhood")
    plt.scatter([point[0]], [point[1]], s=120, label="Focal event")
    plt.fill_betweenx(
        np.linspace(point[1] - r, point[1] + r, 200),
        -1.6,
        0,
        alpha=0.25,
        label="Unobserved outside window",
    )
    plt.xlim(-2, 10.5)
    plt.ylim(0, 10)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Near an edge, part of the event's neighborhood is unobserved")
    plt.legend(loc="upper right")
    plt.gca().set_aspect("equal", adjustable="box")
    save_and_close("05_edge_effect.png")


def figure_06_monte_carlo_envelope():
    rng = np.random.default_rng(77)

    # Make the observed pattern clustered.
    observed = simulate_thomas_like(
        rng,
        parent_intensity=0.06,
        mean_offspring=7.0,
        cluster_sd=0.50,
    )

    n_obs = len(observed)
    radii = np.linspace(0.15, 2.2, 28)

    observed_K = border_K(observed, radii)
    observed_L = L_minus_r(observed_K, radii)

    # Conditional CSR simulations preserve observed n.
    simulations = []
    for _ in range(199):
        sim = simulate_fixed_count_uniform(rng, n_obs)
        K = border_K(sim, radii)
        simulations.append(L_minus_r(K, radii))

    simulations = np.asarray(simulations)

    lower = np.nanquantile(simulations, 0.025, axis=0)
    upper = np.nanquantile(simulations, 0.975, axis=0)

    plt.figure(figsize=(8, 5))
    plt.fill_between(
        radii,
        lower,
        upper,
        alpha=0.25,
        label="95% pointwise CSR envelope",
    )
    plt.plot(radii, observed_L, linewidth=2, label="Observed L(r)-r")
    plt.axhline(0.0, linestyle=":", label="CSR reference")
    plt.xlabel("r")
    plt.ylabel("L(r) - r")
    plt.title("Monte Carlo envelope: exploratory evidence across spatial scales")
    plt.legend()
    save_and_close("06_monte_carlo_envelope.png")

    print("\nMONTE CARLO ENVELOPE")
    print("Observed number of events:", n_obs)
    print("Simulations:", len(simulations))


def figure_07_process_types():
    rng = np.random.default_rng(88)

    csr = simulate_fixed_count_uniform(rng, 55)
    cluster = simulate_thomas_like(
        rng,
        parent_intensity=0.055,
        mean_offspring=7.5,
        cluster_sd=0.45,
    )
    inhibit = simulate_sequential_inhibition(
        rng,
        n=55,
        hard_core=0.72,
    )

    # Display three windows side by side in one axes.
    cluster_shift = cluster.copy()
    cluster_shift[:, 0] += 12.0

    inhibit_shift = inhibit.copy()
    inhibit_shift[:, 0] += 24.0

    plt.figure(figsize=(15, 5))
    plt.scatter(csr[:, 0], csr[:, 1], s=35, label="CSR")
    plt.scatter(cluster_shift[:, 0], cluster_shift[:, 1], s=35, label="Clustered")
    plt.scatter(inhibit_shift[:, 0], inhibit_shift[:, 1], s=35, label="Inhibited")

    plt.plot([11, 11], [0, 10], linestyle=":")
    plt.plot([23, 23], [0, 10], linestyle=":")
    plt.text(3.5, 10.3, "CSR")
    plt.text(14.4, 10.3, "Cluster process")
    plt.text(26.3, 10.3, "Sequential inhibition")

    plt.xlim(0, 34)
    plt.ylim(0, 11)
    plt.xlabel("display coordinate")
    plt.ylabel("y")
    plt.title("Different interaction structures produce different spacing patterns")
    plt.legend()
    save_and_close("07_process_types.png")


def figure_08_marked_pattern():
    rng = np.random.default_rng(99)
    points = simulate_fixed_count_uniform(rng, 65)

    # Categorical marks A/B/C with fixed probabilities.
    mark_codes = rng.choice([0, 1, 2], size=len(points), p=[0.45, 0.35, 0.20])
    labels = ["Mark A", "Mark B", "Mark C"]
    markers = ["o", "s", "^"]

    plt.figure(figsize=(6.5, 6))

    for code, label, marker in zip([0, 1, 2], labels, markers):
        use = mark_codes == code
        plt.scatter(
            points[use, 0],
            points[use, 1],
            s=65,
            marker=marker,
            label=label,
        )

    plt.xlim(0, 10)
    plt.ylim(0, 10)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Marked point process: each event carries an additional attribute")
    plt.legend()
    plt.gca().set_aspect("equal", adjustable="box")
    save_and_close("08_marked_pattern.png")


def print_numerical_examples():
    print("NUMERICAL CHECKS")
    print("----------------")

    # Expected count
    lam = 0.2
    area = 12.0
    expected = lam * area
    print("E[N(B)] with lambda=0.2 and area=12 =", expected)

    # Exact Poisson probability
    p3 = np.exp(-expected) * expected**3 / 6.0
    print("P(N=3) when mean=2.4 =", round(p3, 6))

    # G(2)
    lam_g = 0.08
    r = 2.0
    G = 1.0 - np.exp(-lam_g * np.pi * r**2)
    print("G(2) when lambda=0.08 =", round(G, 6))

    # Worked K example
    A = 100.0
    n = 5
    ordered_pairs = 6
    Khat = A * ordered_pairs / (n * (n - 1))
    Kcsr = np.pi * 3.0**2
    print("Khat(3) =", Khat)
    print("K_CSR(3) =", round(Kcsr, 6))


def main():
    print_numerical_examples()
    figure_01_point_pattern_basics()
    figure_02_intensity_vs_interaction()
    figure_03_poisson_count_vs_fixed_count()
    figure_04_nearest_neighbor_G()
    figure_05_edge_effect()
    figure_06_monte_carlo_envelope()
    figure_07_process_types()
    figure_08_marked_pattern()
    print(f"\nAll figures are in: {FIG_DIR}")


if __name__ == "__main__":
    main()
