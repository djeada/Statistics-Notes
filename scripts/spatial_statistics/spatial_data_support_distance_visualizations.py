"""
Spatial data, support, and distance teaching visualizations
===========================================================

Creates the figures used in `spatial_data_and_distance.md`.

Dependencies:
    numpy
    matplotlib

Run:
    python scripts/spatial_statistics/spatial_data_support_distance_visualizations.py
"""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


REPO_ROOT = Path(__file__).resolve().parents[2]
FIG_DIR = REPO_ROOT / "assets" / "spatial_statistics" / "data_support_distance"
FIG_DIR.mkdir(parents=True, exist_ok=True)


def save_and_close(filename):
    path = FIG_DIR / filename
    plt.tight_layout()
    plt.savefig(path, dpi=180, bbox_inches="tight")
    plt.close()
    print(f"created: {path}")


def haversine_km(lat1, lon1, lat2, lon2, radius_km=6371.0):
    """
    Great-circle distance using the haversine formula.
    Input angles are in degrees.
    """
    phi1 = np.deg2rad(lat1)
    phi2 = np.deg2rad(lat2)
    dphi = np.deg2rad(lat2 - lat1)
    dlambda = np.deg2rad(lon2 - lon1)

    a = (
        np.sin(dphi / 2.0) ** 2
        + np.cos(phi1) * np.cos(phi2) * np.sin(dlambda / 2.0) ** 2
    )

    c = 2.0 * np.arctan2(np.sqrt(a), np.sqrt(1.0 - a))
    return radius_km * c


def block_average(field, block_size):
    """Average a 2D array over non-overlapping square blocks."""
    ny, nx = field.shape

    if ny % block_size != 0 or nx % block_size != 0:
        raise ValueError("Field dimensions must be divisible by block_size.")

    reshaped = field.reshape(
        ny // block_size,
        block_size,
        nx // block_size,
        block_size,
    )
    return reshaped.mean(axis=(1, 3))


def figure_01_spatial_data_objects():
    rng = np.random.default_rng(12)

    # Three examples displayed side by side in one axes.
    plt.figure(figsize=(13, 4.8))

    # Areal cells.
    for ix in range(3):
        for iy in range(3):
            x0 = ix
            y0 = iy
            value = 2 + ix + 2 * iy
            plt.gca().add_patch(
                plt.Rectangle((x0, y0), 1, 1, fill=False)
            )
            plt.text(x0 + 0.5, y0 + 0.5, f"{value}", ha="center", va="center")

    plt.text(0.35, 3.25, "Areal/lattice data")

    # Point referenced.
    offset = 5.0
    xy = rng.uniform([offset, 0.2], [offset + 3.0, 2.8], size=(10, 2))
    vals = 5 + 0.6 * xy[:, 0] + rng.normal(0, 0.3, len(xy))
    sc = plt.scatter(xy[:, 0], xy[:, 1], c=vals, s=90)
    plt.text(offset + 0.2, 3.25, "Point-referenced values")

    # Point pattern.
    offset2 = 10.0
    pp = rng.uniform([offset2, 0.2], [offset2 + 3.0, 2.8], size=(18, 2))
    plt.scatter(pp[:, 0], pp[:, 1], s=55)
    plt.text(offset2 + 0.45, 3.25, "Point pattern")

    plt.axvline(4.0, linestyle=":")
    plt.axvline(9.0, linestyle=":")
    plt.xlim(-0.2, 13.3)
    plt.ylim(-0.2, 3.7)
    plt.xlabel("display coordinate")
    plt.ylabel("display coordinate")
    plt.title("Three spatial data objects can require different statistical models")
    save_and_close("01_spatial_data_objects.png")


def figure_02_longitude_distance_by_latitude():
    lat = np.linspace(0, 80, 200)

    # Approximate physical length of one degree longitude.
    km = 111.2 * np.cos(np.deg2rad(lat))

    plt.figure(figsize=(7, 5))
    plt.plot(lat, km)
    plt.xlabel("Latitude (degrees)")
    plt.ylabel("Approximate km per degree of longitude")
    plt.title("One degree of longitude shrinks physically toward the poles")
    save_and_close("02_longitude_distance_by_latitude.png")


def figure_03_spatial_support():
    plt.figure(figsize=(11, 5))

    # Point support.
    plt.scatter([1.0], [2.0], s=140)
    plt.text(0.3, 3.5, "Point support")
    plt.annotate("sensor", (1.0, 2.0), xytext=(1.3, 2.4))

    # Pixel support.
    plt.gca().add_patch(
        plt.Rectangle((4.0, 1.0), 2.0, 2.0, fill=False, linewidth=2)
    )
    plt.text(4.15, 3.5, "Pixel/area support")
    plt.text(5.0, 2.0, "average", ha="center", va="center")

    # Polygon support.
    polygon = np.array([
        [8.2, 1.0],
        [10.4, 1.3],
        [10.7, 2.9],
        [9.3, 3.3],
        [7.8, 2.4],
        [8.2, 1.0],
    ])
    plt.plot(polygon[:, 0], polygon[:, 1], linewidth=2)
    plt.text(8.2, 3.7, "Polygon support")
    plt.text(9.25, 2.2, "regional\nsummary", ha="center", va="center")

    plt.xlim(-0.3, 11.2)
    plt.ylim(0.3, 4.2)
    plt.xlabel("display coordinate")
    plt.ylabel("display coordinate")
    plt.title("The same coordinate can refer to measurements with different spatial support")
    save_and_close("03_spatial_support.png")


def generate_fine_field(seed=33, n=40):
    rng = np.random.default_rng(seed)

    x = np.linspace(0, 4 * np.pi, n)
    y = np.linspace(0, 4 * np.pi, n)
    xx, yy = np.meshgrid(x, y)

    field = (
        3.0
        + 1.8 * np.sin(xx)
        + 1.3 * np.cos(yy)
        + 0.8 * np.sin(0.5 * xx + 0.8 * yy)
        + rng.normal(0, 0.9, size=(n, n))
    )
    return field


def figure_04_support_and_aggregation():
    field = generate_fine_field(seed=33, n=40)
    agg = block_average(field, 5)

    # Display fine values as a line and block means as a line using one row slice.
    fine_slice = field[20, :]
    expanded_agg = np.repeat(agg[4, :], 5)

    plt.figure(figsize=(9, 5))
    plt.plot(np.arange(len(fine_slice)), fine_slice, label="Fine support")
    plt.plot(np.arange(len(expanded_agg)), expanded_agg, linewidth=2, label="5-cell block averages")
    plt.xlabel("Fine-scale position")
    plt.ylabel("Value")
    plt.title("Larger support smooths fine-scale variation")
    plt.legend()
    save_and_close("04_support_and_aggregation.png")


def figure_05_maup_scale():
    field = generate_fine_field(seed=41, n=40)

    # Show averages for increasing block support as a variance curve.
    block_sizes = np.array([1, 2, 4, 5, 8, 10])
    variances = []

    for b in block_sizes:
        agg = block_average(field, int(b))
        variances.append(np.var(agg))

    plt.figure(figsize=(8, 5))
    plt.plot(block_sizes, variances, "o-")
    plt.xlabel("Aggregation block width (fine cells)")
    plt.ylabel("Variance of aggregated values")
    plt.title("MAUP scale effect: aggregation changes the distribution of areal values")
    save_and_close("05_maup_scale.png")


def figure_06_maup_zoning():
    # Fine values in a 4x4 field.
    field = np.array([
        [1, 2, 8, 9],
        [2, 3, 9, 10],
        [4, 5, 11, 12],
        [5, 6, 12, 13],
    ], dtype=float)

    # Zoning 1: vertical halves.
    zone1 = np.zeros_like(field, dtype=int)
    zone1[:, :2] = 0
    zone1[:, 2:] = 1

    # Zoning 2: diagonal/checker-like partition while retaining two zones.
    zone2 = np.indices(field.shape).sum(axis=0) % 2

    means1 = [field[zone1 == z].mean() for z in [0, 1]]
    means2 = [field[zone2 == z].mean() for z in [0, 1]]

    positions = np.array([0, 1])

    plt.figure(figsize=(8, 5))
    width = 0.34
    plt.bar(positions - width / 2, means1, width=width, label="Zoning scheme 1")
    plt.bar(positions + width / 2, means2, width=width, label="Zoning scheme 2")
    plt.xticks(positions, ["Region 1", "Region 2"])
    plt.ylabel("Regional mean")
    plt.title("MAUP zoning effect: boundaries change the regional summaries")
    plt.legend()
    save_and_close("06_maup_zoning.png")


def figure_07_distance_metrics():
    A = np.array([0.0, 0.0])
    B = np.array([3.0, 4.0])
    C1 = np.array([0.0, 4.0])
    C2 = np.array([0.0, 5.0])

    # Euclidean direct path A-B = 5.
    # Network path A-C2-B: 5 + sqrt(10) ≈ 8.162.
    network_path = np.vstack([A, C2, B])

    plt.figure(figsize=(7, 6))
    plt.plot([A[0], B[0]], [A[1], B[1]], linestyle="--", label="Euclidean straight line")
    plt.plot(network_path[:, 0], network_path[:, 1], linewidth=2, label="Constrained network path")
    plt.scatter([A[0], B[0], C2[0]], [A[1], B[1], C2[1]], s=110)

    plt.annotate("A", A, xytext=(-12, -14), textcoords="offset points")
    plt.annotate("B", B, xytext=(8, 5), textcoords="offset points")
    plt.annotate("network junction", C2, xytext=(8, 5), textcoords="offset points")

    direct = np.linalg.norm(B - A)
    network = np.linalg.norm(C2 - A) + np.linalg.norm(B - C2)

    plt.text(
        1.2,
        2.2,
        f"Euclidean = {direct:.2f}\nNetwork = {network:.2f}",
    )

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("The shortest scientific path need not be the straight-line path")
    plt.legend()
    plt.gca().set_aspect("equal", adjustable="box")
    save_and_close("07_distance_metrics.png")


def figure_08_boundary_effect():
    window = np.array([
        [0, 0],
        [10, 0],
        [10, 10],
        [0, 10],
        [0, 0],
    ], dtype=float)

    interior = np.array([6.0, 5.0])
    edge = np.array([0.9, 5.0])
    r = 2.2

    theta = np.linspace(0, 2 * np.pi, 300)

    plt.figure(figsize=(7, 6))
    plt.plot(window[:, 0], window[:, 1], linewidth=2)

    for point, label in [(interior, "interior"), (edge, "edge")]:
        cx = point[0] + r * np.cos(theta)
        cy = point[1] + r * np.sin(theta)
        plt.plot(cx, cy, linestyle="--")
        plt.scatter([point[0]], [point[1]], s=100)
        plt.annotate(label, point, xytext=(7, 7), textcoords="offset points")

    plt.xlim(-2.0, 10.5)
    plt.ylim(0, 10)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("An edge location has part of its neighborhood outside the observed domain")
    plt.gca().set_aspect("equal", adjustable="box")
    save_and_close("08_boundary_effect.png")


def print_numerical_examples():
    print("NUMERICAL CHECKS")
    print("----------------")

    # Haversine examples.
    d_equator = haversine_km(0.0, 0.0, 0.0, 1.0)
    d_60 = haversine_km(60.0, 0.0, 60.0, 1.0)

    print("1 degree longitude at equator =", round(d_equator, 3), "km")
    print("1 degree longitude at 60N     =", round(d_60, 3), "km")

    # Projected 3-4-5 example.
    p1 = np.array([500000.0, 5700000.0])
    p2 = np.array([500300.0, 5700400.0])
    print("Projected Euclidean distance =", np.linalg.norm(p2 - p1), "m")

    # Area-weighted example.
    weighted = 0.7 * 10 + 0.3 * 20
    print("Area-weighted mean =", weighted)

    # Exercise-like example.
    p3 = np.array([1200.0, 3400.0])
    p4 = np.array([1500.0, 3800.0])
    print("Exercise projected distance =", np.linalg.norm(p4 - p3), "m")


def main():
    print_numerical_examples()
    figure_01_spatial_data_objects()
    figure_02_longitude_distance_by_latitude()
    figure_03_spatial_support()
    figure_04_support_and_aggregation()
    figure_05_maup_scale()
    figure_06_maup_zoning()
    figure_07_distance_metrics()
    figure_08_boundary_effect()
    print(f"\nAll figures are in: {FIG_DIR}")


if __name__ == "__main__":
    main()
