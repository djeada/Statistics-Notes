"""Compare random and spatial-block cross-validation on spatially dependent data."""

import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GroupKFold, KFold, cross_val_score

rng = np.random.default_rng(5)
n = 500
coordinates = rng.uniform(0.0, 1.0, size=(n, 2))
x_coord = coordinates[:, 0]
y_coord = coordinates[:, 1]

target = (
    np.sin(3 * np.pi * x_coord)
    + np.cos(3 * np.pi * y_coord)
    + 0.5 * np.sin(5 * np.pi * (x_coord + y_coord))
    + rng.normal(scale=0.20, size=n)
)

model = RandomForestRegressor(
    n_estimators=150,
    min_samples_leaf=3,
    random_state=11,
    n_jobs=1,
)

random_cv = KFold(n_splits=5, shuffle=True, random_state=13)
random_rmse = np.sqrt(
    -cross_val_score(
        model,
        coordinates,
        target,
        cv=random_cv,
        scoring="neg_mean_squared_error",
    )
)

groups = np.minimum((x_coord * 5).astype(int), 4)
block_cv = GroupKFold(n_splits=5)
block_rmse = np.sqrt(
    -cross_val_score(
        model,
        coordinates,
        target,
        cv=block_cv,
        groups=groups,
        scoring="neg_mean_squared_error",
    )
)

print(f"Random-CV RMSE: {random_rmse.mean():.3f} ± {random_rmse.std(ddof=1):.3f}")
print(f"Block-CV  RMSE: {block_rmse.mean():.3f} ± {block_rmse.std(ddof=1):.3f}")
