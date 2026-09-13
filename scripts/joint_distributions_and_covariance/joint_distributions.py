"""Joint, marginal, and conditional distributions with covariance and correlation."""

import numpy as np

joint = np.array([[0.10, 0.15, 0.05], [0.10, 0.20, 0.40]], dtype=float)
x_values = np.array([0.0, 1.0])
y_values = np.array([0.0, 1.0, 2.0])

px = joint.sum(axis=1)
py = joint.sum(axis=0)

ex = np.sum(x_values * px)
ey = np.sum(y_values * py)
exy = np.sum(joint * x_values[:, None] * y_values[None, :])

var_x = np.sum((x_values - ex) ** 2 * px)
var_y = np.sum((y_values - ey) ** 2 * py)
cov_xy = exy - ex * ey
corr_xy = cov_xy / np.sqrt(var_x * var_y)

conditional_y_given_x1 = joint[1] / px[1]
independence_gap = np.max(np.abs(joint - np.outer(px, py)))

print("P(X):", px)
print("P(Y):", py)
print("P(Y | X=1):", conditional_y_given_x1)
print(f"E[X]={ex:.3f}, E[Y]={ey:.3f}")
print(f"Cov(X,Y)={cov_xy:.3f}, Corr(X,Y)={corr_xy:.3f}")
print(f"Maximum |p(x,y)-p(x)p(y)| = {independence_gap:.3f}")
