"""Coordinate systems, distance, and spatial support.

This example intentionally avoids GIS-specific dependencies. It shows why raw
longitude/latitude degrees should not be treated as Euclidean coordinates and
why the spatial support of an observation matters.
"""

from __future__ import annotations

import numpy as np

EARTH_RADIUS_KM = 6371.0088


def haversine_km(lon1, lat1, lon2, lat2):
    """Great-circle distance in kilometers for longitude/latitude in degrees."""
    lon1, lat1, lon2, lat2 = np.radians([lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = np.sin(dlat / 2.0) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2.0) ** 2
    return 2.0 * EARTH_RADIUS_KM * np.arcsin(np.sqrt(a))


def aggregate_to_blocks(values, block_size):
    """Average a one-dimensional signal over non-overlapping blocks."""
    values = np.asarray(values, dtype=float)
    n_complete = len(values) // block_size
    trimmed = values[: n_complete * block_size]
    return trimmed.reshape(n_complete, block_size).mean(axis=1)


def main():
    # Leipzig and Berlin: Euclidean distance in degrees is not a physical distance.
    leipzig = (12.3731, 51.3397)
    berlin = (13.4050, 52.5200)

    degree_distance = np.linalg.norm(np.subtract(leipzig, berlin))
    physical_distance = haversine_km(*leipzig, *berlin)

    print(f"Euclidean distance in degree space: {degree_distance:.3f} degrees")
    print(f"Great-circle distance:              {physical_distance:.1f} km")

    # Same underlying fine-scale signal, different observation support.
    x = np.linspace(0.0, 1.0, 24, endpoint=False)
    fine = np.sin(4 * np.pi * x) + 0.35 * np.cos(10 * np.pi * x)

    for block_size in (2, 4, 6):
        coarse = aggregate_to_blocks(fine, block_size)
        print(
            f"Block size {block_size:>2}: "
            f"n={len(coarse):>2}, variance={np.var(coarse, ddof=1):.3f}"
        )


if __name__ == "__main__":
    main()
