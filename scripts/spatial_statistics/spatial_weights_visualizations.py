"""
Spatial weights and spatial lags teaching visualizations
========================================================

Creates the figures referenced in `spatial_weights.md`.

Dependencies:
    numpy
    matplotlib

Run:
    python scripts/spatial_statistics/spatial_weights_visualizations.py
"""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


REPO_ROOT = Path(__file__).resolve().parents[2]
FIG_DIR = REPO_ROOT / "assets" / "spatial_statistics" / "spatial_weights"
FIG_DIR.mkdir(parents=True, exist_ok=True)


def save_and_close(filename):
    path = FIG_DIR / filename
    plt.tight_layout()
    plt.savefig(path, dpi=180, bbox_inches="tight")
    plt.close()
    print(f"created: {path}")


def pairwise_distance(coords):
    coords = np.asarray(coords, dtype=float)
    delta = coords[:, None, :] - coords[None, :, :]
    return np.sqrt(np.sum(delta**2, axis=2))


def row_standardize(W):
    W = np.asarray(W, dtype=float).copy()
    sums = W.sum(axis=1)
    out = np.zeros_like(W)
    nonzero = sums > 0
    out[nonzero] = W[nonzero] / sums[nonzero, None]
    return out


def distance_band_weights(coords, threshold):
    D = pairwise_distance(coords)
    return ((D > 0) & (D <= threshold)).astype(float)


def knn_weights(coords, k=1):
    coords = np.asarray(coords, dtype=float)
    D = pairwise_distance(coords)
    np.fill_diagonal(D, np.inf)

    W = np.zeros((len(coords), len(coords)), dtype=float)
    for i in range(len(coords)):
        nbrs = np.argsort(D[i])[:k]
        W[i, nbrs] = 1.0
    return W


def union_symmetrize(W):
    return ((W + W.T) > 0).astype(float)


def mutual_symmetrize(W):
    return ((W > 0) & (W.T > 0)).astype(float)


def inverse_distance_weights(coords, alpha=1.0, epsilon=1e-9):
    D = pairwise_distance(coords)
    W = np.zeros_like(D)
    mask = D > epsilon
    W[mask] = D[mask] ** (-alpha)
    np.fill_diagonal(W, 0.0)
    return W


def rook_weights_2x2():
    return np.array([
        [0, 1, 1, 0],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [0, 1, 1, 0],
    ], dtype=float)


def queen_weights_2x2():
    W = np.ones((4, 4), dtype=float)
    np.fill_diagonal(W, 0.0)
    return W


def figure_01_weights_graph():
    coords = np.array([
        [0.0, 1.0],
        [1.0, 1.0],
        [0.0, 0.0],
        [1.0, 0.0],
    ])
    names = ["A", "B", "C", "D"]
    W = rook_weights_2x2()

    plt.figure(figsize=(6, 6))

    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            if W[i, j] > 0:
                plt.plot(
                    [coords[i, 0], coords[j, 0]],
                    [coords[i, 1], coords[j, 1]],
                    linewidth=2,
                )

    plt.scatter(coords[:, 0], coords[:, 1], s=180)

    for xy, name in zip(coords, names):
        plt.annotate(name, xy, xytext=(7, 7), textcoords="offset points")

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("A spatial weights matrix is a numerical representation of a neighbor graph")
    plt.xlim(-0.3, 1.3)
    plt.ylim(-0.3, 1.3)
    plt.gca().set_aspect("equal", adjustable="box")
    save_and_close("01_weights_graph.png")


def figure_02_rook_vs_queen():
    coords = np.array([
        [0.0, 1.0],
        [1.0, 1.0],
        [0.0, 0.0],
        [1.0, 0.0],
    ])
    names = ["A", "B", "C", "D"]

    # Rook links in left display; queen links in right display.
    rook = rook_weights_2x2()
    queen = queen_weights_2x2()

    left = coords.copy()
    right = coords.copy()
    right[:, 0] += 3.0

    plt.figure(figsize=(10, 5))

    for display_coords, W in [(left, rook), (right, queen)]:
        for i in range(4):
            for j in range(i + 1, 4):
                if W[i, j] > 0:
                    plt.plot(
                        [display_coords[i, 0], display_coords[j, 0]],
                        [display_coords[i, 1], display_coords[j, 1]],
                        linewidth=1.8,
                    )
        plt.scatter(display_coords[:, 0], display_coords[:, 1], s=140)

    for xy, name in zip(left, names):
        plt.annotate(name, xy, xytext=(5, 5), textcoords="offset points")
    for xy, name in zip(right, names):
        plt.annotate(name, xy, xytext=(5, 5), textcoords="offset points")

    plt.text(0.2, 1.35, "Rook: shared edges")
    plt.text(3.15, 1.35, "Queen: shared edges or vertices")
    plt.xlabel("display coordinate")
    plt.ylabel("y")
    plt.title("Rook and queen contiguity define different neighborhood graphs")
    plt.xlim(-0.4, 4.4)
    plt.ylim(-0.4, 1.7)
    plt.gca().set_aspect("equal", adjustable="box")
    save_and_close("02_rook_vs_queen.png")


def figure_03_binary_vs_row_standardized():
    W = rook_weights_2x2()
    Wr = row_standardize(W)
    x = np.array([10.0, 14.0, 8.0, 20.0])

    raw_lag = W @ x
    avg_lag = Wr @ x

    labels = ["A", "B", "C", "D"]
    xpos = np.arange(4)
    width = 0.36

    plt.figure(figsize=(8, 5))
    plt.bar(xpos - width / 2, raw_lag, width=width, label="Binary W: neighbor sum")
    plt.bar(xpos + width / 2, avg_lag, width=width, label="Row-standardized W: neighbor average")
    plt.xticks(xpos, labels)
    plt.ylabel("Spatial lag")
    plt.title("Row standardization changes the numerical meaning of the spatial lag")
    plt.legend()
    save_and_close("03_binary_vs_row_standardized.png")


def figure_04_knn_asymmetry():
    coords = np.array([
        [0.0, 0.0],
        [1.0, 0.0],
        [10.0, 0.0],
    ])
    names = ["A", "B", "C"]
    W = knn_weights(coords, k=1)

    plt.figure(figsize=(9, 3.5))
    plt.scatter(coords[:, 0], coords[:, 1], s=150)

    directed_links = [(0, 1, 0.08), (1, 0, -0.08), (2, 1, 0.08)]
    for i, j, offset in directed_links:
        start = coords[i] + np.array([0.0, offset])
        end = coords[j] + np.array([0.0, offset])
        plt.annotate(
            "",
            xy=end,
            xytext=start,
            arrowprops={"arrowstyle": "->", "linewidth": 1.8},
        )

    for xy, name in zip(coords, names):
        plt.annotate(name, xy, xytext=(0, 12), textcoords="offset points", ha="center")

    plt.xlabel("x")
    plt.yticks([])
    plt.title("Directed 1-nearest-neighbor weights can be asymmetric")
    plt.xlim(-0.8, 10.8)
    plt.ylim(-0.7, 0.8)
    save_and_close("04_knn_asymmetry.png")


def figure_05_islands_and_components():
    coords = np.array([
        [0.0, 0.0],
        [1.0, 0.4],
        [2.0, 0.0],
        [6.5, 0.2],
        [7.4, 0.8],
        [11.5, 0.0],
    ])
    threshold = 1.6
    W = distance_band_weights(coords, threshold)

    plt.figure(figsize=(10, 4))

    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            if W[i, j] > 0:
                plt.plot(
                    [coords[i, 0], coords[j, 0]],
                    [coords[i, 1], coords[j, 1]],
                    linewidth=2,
                )

    degree = W.sum(axis=1)
    plt.scatter(coords[:, 0], coords[:, 1], s=140)

    for i, xy in enumerate(coords):
        label = f"{i+1}\ndegree={int(degree[i])}"
        plt.annotate(label, xy, xytext=(5, 8), textcoords="offset points")

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("A distance rule can create disconnected components and islands")
    plt.xlim(-0.7, 12.3)
    plt.ylim(-0.6, 1.7)
    save_and_close("05_islands_and_components.png")


def figure_06_neighbor_count():
    rng = np.random.default_rng(21)
    coords = rng.uniform(0.0, 10.0, size=(70, 2))
    thresholds = np.linspace(0.8, 4.5, 30)

    mean_degree = []
    island_count = []

    for threshold in thresholds:
        W = distance_band_weights(coords, threshold)
        degree = W.sum(axis=1)
        mean_degree.append(degree.mean())
        island_count.append(np.sum(degree == 0))

    plt.figure(figsize=(8, 5))
    plt.plot(thresholds, mean_degree, "o-", label="Mean neighbor count")
    plt.plot(thresholds, island_count, "o-", label="Number of islands")
    plt.xlabel("Distance threshold")
    plt.ylabel("Count")
    plt.title("Increasing the distance threshold changes graph density and connectivity")
    plt.legend()
    save_and_close("06_neighbor_count.png")


def figure_07_weights_sensitivity():
    coords = np.array([
        [0.0, 1.0],
        [1.0, 1.0],
        [0.0, 0.0],
        [1.0, 0.0],
    ])
    x = np.array([10.0, 14.0, 8.0, 20.0])

    rook = row_standardize(rook_weights_2x2())
    queen = row_standardize(queen_weights_2x2())
    inv = row_standardize(inverse_distance_weights(coords, alpha=1.0))

    lag_rook = rook @ x
    lag_queen = queen @ x
    lag_inv = inv @ x

    xpos = np.arange(4)
    width = 0.24

    plt.figure(figsize=(9, 5))
    plt.bar(xpos - width, lag_rook, width=width, label="Rook")
    plt.bar(xpos, lag_queen, width=width, label="Queen")
    plt.bar(xpos + width, lag_inv, width=width, label="Inverse distance")
    plt.xticks(xpos, ["A", "B", "C", "D"])
    plt.ylabel("Row-standardized spatial lag")
    plt.title("The same observations can have different lags under different W")
    plt.legend()
    save_and_close("07_weights_sensitivity.png")


def figure_08_distance_decay():
    distances = np.linspace(0.25, 10.0, 250)

    plt.figure(figsize=(8, 5))
    for alpha in [0.5, 1.0, 2.0]:
        weights = distances ** (-alpha)
        plt.plot(distances, weights, label=rf"$\alpha={alpha}$")

    plt.xlabel("Distance")
    plt.ylabel(r"Raw weight $d^{-\alpha}$")
    plt.title("The distance-decay exponent controls how quickly influence decreases")
    plt.legend()
    save_and_close("08_distance_decay.png")


def print_worked_examples():
    print("WORKED SPATIAL WEIGHTS EXAMPLES")
    print("--------------------------------")

    W = rook_weights_2x2()
    Wr = row_standardize(W)
    x = np.array([10.0, 14.0, 8.0, 20.0])

    print("Binary rook W:")
    print(W)
    print("\nRow-standardized rook W:")
    print(Wr)
    print("\nx =", x)
    print("Binary lag W x =", W @ x)
    print("Row-standardized lag W_R x =", Wr @ x)

    z = x - x.mean()
    print("\nmean(x) =", x.mean())
    print("z =", z)
    print("Centered spatial lag W_R z =", Wr @ z)

    coords_line = np.array([
        [0.0, 0.0],
        [1.0, 0.0],
        [3.0, 0.0],
        [7.0, 0.0],
    ])
    Wd = distance_band_weights(coords_line, threshold=2.5)
    print("\nDistance-band W for points 0,1,3,7 with threshold 2.5:")
    print(Wd)
    print("degrees =", Wd.sum(axis=1))

    coords_knn = np.array([
        [0.0, 0.0],
        [1.0, 0.0],
        [10.0, 0.0],
    ])
    Wk = knn_weights(coords_knn, k=1)
    print("\nDirected 1-NN W for points 0,1,10:")
    print(Wk)
    print("Symmetric?", np.allclose(Wk, Wk.T))

    raw = np.array([1.0, 0.5])
    std = raw / raw.sum()
    lag = std @ np.array([12.0, 6.0])
    print("\nInverse-distance example raw weights =", raw)
    print("Standardized weights =", std)
    print("Weighted lag =", lag)


def main():
    print_worked_examples()
    figure_01_weights_graph()
    figure_02_rook_vs_queen()
    figure_03_binary_vs_row_standardized()
    figure_04_knn_asymmetry()
    figure_05_islands_and_components()
    figure_06_neighbor_count()
    figure_07_weights_sensitivity()
    figure_08_distance_decay()
    print(f"\nAll figures are in: {FIG_DIR}")


if __name__ == "__main__":
    main()
