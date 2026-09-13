"""Compare random, blocked, and buffered spatial validation."""

from __future__ import annotations

import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import KFold


def simulate_spatial_prediction_problem(n=600, seed=5):
    rng = np.random.default_rng(seed)
    coordinates = rng.uniform(0.0, 1.0, size=(n, 2))
    x, y = coordinates[:, 0], coordinates[:, 1]

    target = (
        np.sin(3 * np.pi * x)
        + np.cos(3 * np.pi * y)
        + 0.6 * np.sin(4 * np.pi * (x + y))
        + rng.normal(scale=0.18, size=n)
    )
    return coordinates, target


def stripe_splits(coordinates, n_splits=5, buffer=0.0):
    """Contiguous x-stripe test regions with optional exclusion buffer."""
    x = coordinates[:, 0]
    edges = np.linspace(0.0, 1.0, n_splits + 1)

    for fold in range(n_splits):
        left, right = edges[fold], edges[fold + 1]
        if fold == n_splits - 1:
            test = (x >= left) & (x <= right)
        else:
            test = (x >= left) & (x < right)

        train = ~test
        if buffer > 0:
            train &= (x < left - buffer) | (x > right + buffer)

        yield np.flatnonzero(train), np.flatnonzero(test)


def evaluate_splits(model_factory, coordinates, target, splits):
    scores = []
    for train_idx, test_idx in splits:
        model = model_factory()
        model.fit(coordinates[train_idx], target[train_idx])
        prediction = model.predict(coordinates[test_idx])
        scores.append(
            np.sqrt(mean_squared_error(target[test_idx], prediction))
        )
    return np.asarray(scores)


def main():
    coordinates, target = simulate_spatial_prediction_problem()

    def model_factory():
        return RandomForestRegressor(
            n_estimators=180,
            min_samples_leaf=3,
            random_state=11,
            n_jobs=1,
        )

    random_cv = KFold(n_splits=5, shuffle=True, random_state=13)
    random_scores = evaluate_splits(
        model_factory, coordinates, target, random_cv.split(coordinates)
    )
    blocked_scores = evaluate_splits(
        model_factory, coordinates, target, stripe_splits(coordinates, buffer=0.0)
    )
    buffered_scores = evaluate_splits(
        model_factory, coordinates, target, stripe_splits(coordinates, buffer=0.04)
    )

    for name, scores in [
        ("Random folds", random_scores),
        ("Spatial blocks", blocked_scores),
        ("Buffered blocks", buffered_scores),
    ]:
        print(
            f"{name:16s} RMSE = {scores.mean():.3f} "
            f"± {scores.std(ddof=1):.3f}"
        )


if __name__ == "__main__":
    main()
