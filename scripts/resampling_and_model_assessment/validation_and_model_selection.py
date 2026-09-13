"""Cross-validation for model selection with a final untouched test set."""

import numpy as np
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import KFold, cross_val_score, train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

rng = np.random.default_rng(8)
x = rng.uniform(-3.0, 3.0, size=300)
y = 1.0 + 0.8 * x - 0.5 * x**2 + rng.normal(scale=1.2, size=x.size)
X = x[:, None]

X_dev, X_test, y_dev, y_test = train_test_split(
    X, y, test_size=0.25, random_state=17
)

cv = KFold(n_splits=5, shuffle=True, random_state=19)
scores = {}

for degree in range(1, 7):
    model = make_pipeline(
        PolynomialFeatures(degree=degree, include_bias=False),
        StandardScaler(),
        Ridge(alpha=1.0),
    )
    fold_mse = -cross_val_score(
        model, X_dev, y_dev, cv=cv, scoring="neg_mean_squared_error"
    )
    scores[degree] = fold_mse.mean()

best_degree = min(scores, key=scores.get)
final_model = make_pipeline(
    PolynomialFeatures(degree=best_degree, include_bias=False),
    StandardScaler(),
    Ridge(alpha=1.0),
)
final_model.fit(X_dev, y_dev)
test_prediction = final_model.predict(X_test)

print("Mean cross-validation MSE by polynomial degree:")
for degree, mse in scores.items():
    print(f"degree={degree}: {mse:.3f}")
print(f"\nSelected degree: {best_degree}")
print(f"Untouched test MSE: {mean_squared_error(y_test, test_prediction):.3f}")
