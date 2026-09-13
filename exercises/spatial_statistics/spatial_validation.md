# Spatial Validation Exercises

Use this problem set with the [chapter notes](../../notes/spatial_statistics/spatial_validation.md) and the [visualization script](../../scripts/spatial_statistics/spatial_validation_visualizations.py).


## Exercise 1: RMSE

Observed values are

\[
5,\ 7,\ 8,\ 10
\]

and predictions are

\[
6,\ 6,\ 9,\ 11.
\]

Calculate RMSE.

---

## Exercise 2: nearest-training distance

A test point is at coordinate

\[
(4,3).
\]

Training points are

\[
(0,0),\ (4,0),\ (10,3).
\]

Calculate the nearest Euclidean training distance.

---

## Exercise 3: buffer

A test block has three nearby training observations at distances

\[
0.8,\ 1.4,\ 2.7\text{ km}.
\]

Which remain if the buffer is

\[
b=1.5\text{ km}?
\]

---

## Exercise 4: fold interpretation

Random CV gives RMSE 0.9.

Leave-region-out CV gives RMSE 2.4.

Give a scientifically reasonable explanation without saying one result must be wrong.

---

## Exercise 5: leakage

Explain why fitting a spatial interpolator for a predictor using all observations before cross-validation can leak information.

---

## Exercise 6: unsupported extrapolation

Training elevations range from 100 to 900 m.

Deployment will occur above 1800 m.

Explain why spatial block CV within the original dataset cannot fully validate this deployment.

---
