"""
Spatial validation teaching visualizations
===========================================

Creates the figures used in `spatial_validation.md`.

Dependencies:
    numpy
    matplotlib

Run:
    python scripts/spatial_statistics/spatial_validation_visualizations.py

The prediction method used here is deliberately simple inverse-distance
weighting (IDW). Its purpose is to make the effect of validation geometry
easy to see, not to recommend IDW as a universal spatial model.
"""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


REPO_ROOT = Path(__file__).resolve().parents[2]
FIG_DIR = REPO_ROOT / "assets" / "spatial_statistics" / "spatial_validation"
FIG_DIR.mkdir(parents=True, exist_ok=True)


def save_and_close(filename):
    path = FIG_DIR / filename
    plt.tight_layout()
    plt.savefig(path, dpi=180, bbox_inches="tight")
    plt.close()
    print(f"created: {path}")


def generate_dataset(seed=12, n=320):
    rng = np.random.default_rng(seed)
    coords = rng.uniform(0.0, 20.0, size=(n, 2))
    x = coords[:, 0]
    y = coords[:, 1]

    response = (
        8.0
        + 2.3 * np.sin(x / 2.6)
        + 1.9 * np.cos(y / 3.4)
        + 1.2 * np.sin((x + y) / 4.2)
        + rng.normal(0.0, 0.45, size=n)
    )
    return coords, response


def pairwise_distance(a, b):
    delta = a[:, None, :] - b[None, :, :]
    return np.sqrt(np.sum(delta**2, axis=2))


def idw_predict(train_coords, train_y, test_coords, k=8, power=2.0):
    D = pairwise_distance(test_coords, train_coords)
    predictions = np.empty(len(test_coords), dtype=float)

    for i in range(len(test_coords)):
        order = np.argsort(D[i])
        use = order[: min(k, len(order))]
        d = D[i, use]

        if np.any(d < 1e-12):
            predictions[i] = train_y[use[np.argmin(d)]]
            continue

        w = 1.0 / (d**power + 1e-12)
        predictions[i] = np.sum(w * train_y[use]) / np.sum(w)

    return predictions


def rmse(y, pred):
    return np.sqrt(np.mean((y - pred) ** 2))


def nearest_training_distance(train_coords, test_coords):
    D = pairwise_distance(test_coords, train_coords)
    return D.min(axis=1)


def random_folds(n, n_folds=5, seed=100):
    rng = np.random.default_rng(seed)
    ids = np.arange(n)
    rng.shuffle(ids)
    return np.array_split(ids, n_folds)


def vertical_block_folds(coords, n_blocks=5):
    x = coords[:, 0]
    edges = np.linspace(x.min(), x.max() + 1e-9, n_blocks + 1)
    folds = []
    for i in range(n_blocks):
        use = np.where((x >= edges[i]) & (x < edges[i + 1]))[0]
        folds.append(use)
    return folds


def buffered_train_indices(coords, test_idx, buffer_distance):
    all_idx = np.arange(len(coords))
    test_mask = np.zeros(len(coords), dtype=bool)
    test_mask[test_idx] = True

    candidate_train = all_idx[~test_mask]

    if buffer_distance <= 0:
        return candidate_train

    D = pairwise_distance(coords[candidate_train], coords[test_idx])
    min_to_test = D.min(axis=1)
    return candidate_train[min_to_test >= buffer_distance]


def evaluate_folds(coords, y, folds, buffer_distance=0.0, k=8):
    fold_rmse = []
    fold_nearest = []
    fold_sizes = []

    all_idx = np.arange(len(coords))

    for test_idx in folds:
        test_idx = np.asarray(test_idx, dtype=int)
        if len(test_idx) == 0:
            continue

        if buffer_distance > 0:
            train_idx = buffered_train_indices(coords, test_idx, buffer_distance)
        else:
            mask = np.ones(len(coords), dtype=bool)
            mask[test_idx] = False
            train_idx = all_idx[mask]

        if len(train_idx) < max(3, k):
            continue

        pred = idw_predict(
            coords[train_idx],
            y[train_idx],
            coords[test_idx],
            k=k,
        )

        fold_rmse.append(rmse(y[test_idx], pred))
        fold_nearest.extend(
            nearest_training_distance(
                coords[train_idx],
                coords[test_idx],
            )
        )
        fold_sizes.append((len(train_idx), len(test_idx)))

    return (
        np.asarray(fold_rmse),
        np.asarray(fold_nearest),
        fold_sizes,
    )


def figure_01_random_vs_spatial_split():
    coords, _ = generate_dataset(seed=12, n=230)
    rng = np.random.default_rng(11)

    # Random holdout: 20% scattered.
    random_test = rng.choice(len(coords), size=46, replace=False)
    random_mask = np.zeros(len(coords), dtype=bool)
    random_mask[random_test] = True

    # Spatial holdout: rightmost strip.
    spatial_mask = coords[:, 0] >= 16.0

    # Show both as two vertically offset copies in one axes.
    c1 = coords.copy()
    c2 = coords.copy()
    c2[:, 1] += 24.0

    plt.figure(figsize=(9, 9))
    plt.scatter(
        c1[~random_mask, 0],
        c1[~random_mask, 1],
        s=30,
        label="Training",
    )
    plt.scatter(
        c1[random_mask, 0],
        c1[random_mask, 1],
        s=65,
        marker="x",
        label="Random test",
    )

    plt.scatter(
        c2[~spatial_mask, 0],
        c2[~spatial_mask, 1],
        s=30,
    )
    plt.scatter(
        c2[spatial_mask, 0],
        c2[spatial_mask, 1],
        s=65,
        marker="^",
        label="Spatial test region",
    )

    plt.text(0.2, 20.6, "Random holdout")
    plt.text(0.2, 44.6, "Contiguous spatial holdout")
    plt.xlabel("x")
    plt.ylabel("display coordinate")
    plt.title("Random and spatial holdouts represent different prediction tasks")
    plt.legend()
    save_and_close("01_random_vs_spatial_split.png")


def figure_02_nearest_training_distance():
    coords, y = generate_dataset(seed=16, n=320)

    random = random_folds(len(coords), n_folds=5, seed=5)
    blocks = vertical_block_folds(coords, n_blocks=5)

    _, d_random, _ = evaluate_folds(coords, y, random, buffer_distance=0.0)
    _, d_block, _ = evaluate_folds(coords, y, blocks, buffer_distance=0.0)
    _, d_buffer, _ = evaluate_folds(coords, y, blocks, buffer_distance=1.5)

    data = [d_random, d_block, d_buffer]

    plt.figure(figsize=(8, 5))
    plt.boxplot(
        data,
        labels=["Random", "Spatial blocks", "Buffered blocks"],
        showfliers=False,
    )
    plt.ylabel("Nearest training distance")
    plt.title("Validation schemes create very different train-test separation")
    save_and_close("02_nearest_training_distance.png")


def figure_03_validation_rmse():
    coords, y = generate_dataset(seed=18, n=340)

    random = random_folds(len(coords), n_folds=5, seed=13)
    blocks = vertical_block_folds(coords, n_blocks=5)

    r_random, _, _ = evaluate_folds(coords, y, random, 0.0)
    r_block, _, _ = evaluate_folds(coords, y, blocks, 0.0)
    r_buffer, _, _ = evaluate_folds(coords, y, blocks, 1.5)

    means = [
        np.mean(r_random),
        np.mean(r_block),
        np.mean(r_buffer),
    ]

    labels = ["Random", "Spatial blocks", "Buffered blocks"]

    plt.figure(figsize=(8, 5))
    plt.bar(labels, means)
    plt.ylabel("Mean fold RMSE")
    plt.title("The same spatial predictor looks weaker as validation becomes more separated")

    for i, value in enumerate(means):
        plt.text(i, value + 0.03, f"{value:.2f}", ha="center")

    save_and_close("03_validation_rmse.png")

    print("\nVALIDATION RMSE COMPARISON")
    print("Random CV mean RMSE =", np.mean(r_random))
    print("Block CV mean RMSE  =", np.mean(r_block))
    print("Buffered mean RMSE  =", np.mean(r_buffer))


def width_based_folds(coords, block_width):
    x = coords[:, 0]
    xmin = x.min()
    xmax = x.max()
    edges = np.arange(xmin, xmax + block_width, block_width)

    if edges[-1] <= xmax:
        edges = np.append(edges, edges[-1] + block_width)

    folds = []
    for i in range(len(edges) - 1):
        idx = np.where((x >= edges[i]) & (x < edges[i + 1]))[0]
        if len(idx) >= 8:
            folds.append(idx)
    return folds


def figure_04_block_size_sensitivity():
    coords, y = generate_dataset(seed=22, n=420)
    widths = np.array([1.5, 2.5, 4.0, 5.0])
    scores = []
    distances = []

    for width in widths:
        folds = width_based_folds(coords, width)
        r, d, _ = evaluate_folds(coords, y, folds, 0.0, k=8)
        scores.append(np.mean(r))
        distances.append(np.median(d))

    plt.figure(figsize=(8, 5))
    plt.plot(widths, scores, "o-", label="Mean RMSE")
    plt.xlabel("Vertical block width")
    plt.ylabel("Mean fold RMSE")
    plt.title("Block size changes the spatial separation and estimated transfer error")
    plt.legend()
    save_and_close("04_block_size_sensitivity.png")

    print("\nBLOCK SIZE SENSITIVITY")
    for w, r, d in zip(widths, scores, distances):
        print(f"width={w:.1f}, mean RMSE={r:.3f}, median distance={d:.3f}")


def figure_05_buffer_geometry():
    coords, _ = generate_dataset(seed=25, n=260)

    test = np.where((coords[:, 0] >= 8.0) & (coords[:, 0] <= 12.0))[0]
    buffer_distance = 1.7
    train = buffered_train_indices(coords, test, buffer_distance)

    all_idx = np.arange(len(coords))
    is_test = np.zeros(len(coords), dtype=bool)
    is_test[test] = True
    is_train = np.zeros(len(coords), dtype=bool)
    is_train[train] = True
    removed = ~(is_test | is_train)

    plt.figure(figsize=(8, 6))
    plt.scatter(
        coords[is_train, 0],
        coords[is_train, 1],
        s=35,
        label="Retained training",
    )
    plt.scatter(
        coords[removed, 0],
        coords[removed, 1],
        s=60,
        marker="x",
        label="Removed by buffer",
    )
    plt.scatter(
        coords[is_test, 0],
        coords[is_test, 1],
        s=60,
        marker="^",
        label="Test block",
    )
    plt.axvline(8.0 - buffer_distance, linestyle=":")
    plt.axvline(12.0 + buffer_distance, linestyle=":")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Buffered validation removes training observations near the test region")
    plt.legend()
    save_and_close("05_buffer_geometry.png")


def figure_06_spatial_leakage():
    """
    Visual teaching example of a test point whose outcome would leak into a
    training neighborhood feature if neighborhoods were computed globally.
    """
    coords = np.array([
        [1.0, 1.0],
        [2.0, 1.4],
        [2.8, 2.0],
        [3.5, 1.2],
        [4.2, 2.1],
        [5.0, 1.5],
    ])

    test_idx = 3
    train_idx = np.array([0, 1, 2, 4, 5])

    plt.figure(figsize=(8, 5))
    plt.scatter(
        coords[train_idx, 0],
        coords[train_idx, 1],
        s=110,
        label="Training observations",
    )
    plt.scatter(
        [coords[test_idx, 0]],
        [coords[test_idx, 1]],
        s=180,
        marker="x",
        label="Held-out test observation",
    )

    # Connect the held-out point to nearby training rows whose globally computed
    # neighborhood features could include its outcome.
    for i in [2, 4]:
        plt.plot(
            [coords[test_idx, 0], coords[i, 0]],
            [coords[test_idx, 1], coords[i, 1]],
            linestyle="--",
        )

    plt.text(
        2.55,
        2.45,
        "If neighborhood features are computed\nbefore splitting, the held-out outcome\ncan enter training features.",
    )
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Spatial leakage can occur during feature construction")
    plt.legend()
    save_and_close("06_spatial_leakage.png")


def figure_07_loo_vs_region_transfer():
    coords, y = generate_dataset(seed=31, n=300)

    # Approximate LOO using a random subset of singleton test points.
    rng = np.random.default_rng(31)
    loo_points = rng.choice(len(coords), size=80, replace=False)
    loo_errors = []

    all_idx = np.arange(len(coords))
    for test_i in loo_points:
        train_idx = all_idx[all_idx != test_i]
        pred = idw_predict(
            coords[train_idx],
            y[train_idx],
            coords[[test_i]],
            k=8,
        )[0]
        loo_errors.append(abs(y[test_i] - pred))

    # Region transfer: rightmost 20%.
    test_region = np.where(coords[:, 0] >= np.quantile(coords[:, 0], 0.8))[0]
    train_region = np.where(coords[:, 0] < np.quantile(coords[:, 0], 0.8))[0]

    pred_region = idw_predict(
        coords[train_region],
        y[train_region],
        coords[test_region],
        k=8,
    )
    region_errors = np.abs(y[test_region] - pred_region)

    plt.figure(figsize=(8, 5))
    plt.boxplot(
        [loo_errors, region_errors],
        labels=["Leave-one-out-like", "Held-out region"],
        showfliers=False,
    )
    plt.ylabel("Absolute prediction error")
    plt.title("Local interpolation can look much easier than geographic transfer")
    save_and_close("07_loo_vs_region_transfer.png")


def figure_08_fold_level_variability():
    coords, y = generate_dataset(seed=42, n=360)
    blocks = vertical_block_folds(coords, n_blocks=6)

    fold_rmse, _, _ = evaluate_folds(coords, y, blocks, buffer_distance=0.7)

    labels = [f"Block {i+1}" for i in range(len(fold_rmse))]

    plt.figure(figsize=(9, 5))
    plt.bar(labels, fold_rmse)
    plt.axhline(
        np.mean(fold_rmse),
        linestyle="--",
        label=f"Mean = {np.mean(fold_rmse):.2f}",
    )
    plt.ylabel("RMSE")
    plt.title("A single mean can hide large geographic differences in performance")
    plt.legend()
    save_and_close("08_fold_level_variability.png")


def print_worked_rmse():
    observed = np.array([10.0, 12.0, 14.0, 16.0])
    predicted = np.array([11.0, 11.0, 13.0, 18.0])
    errors = observed - predicted
    squared = errors**2
    value = rmse(observed, predicted)

    print("WORKED RMSE EXAMPLE")
    print("-------------------")
    print("observed =", observed)
    print("predicted =", predicted)
    print("errors =", errors)
    print("squared errors =", squared)
    print("mean squared error =", squared.mean())
    print("RMSE =", value)


def main():
    print_worked_rmse()
    figure_01_random_vs_spatial_split()
    figure_02_nearest_training_distance()
    figure_03_validation_rmse()
    figure_04_block_size_sensitivity()
    figure_05_buffer_geometry()
    figure_06_spatial_leakage()
    figure_07_loo_vs_region_transfer()
    figure_08_fold_level_variability()
    print(f"\nAll figures are in: {FIG_DIR}")


if __name__ == "__main__":
    main()
