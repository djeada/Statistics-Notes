# Spatial Weights and Spatial Lags Exercises

Use this problem set with the [chapter notes](../../notes/spatial_statistics/spatial_weights.md) and the [visualization script](../../scripts/spatial_statistics/spatial_weights_visualizations.py).


## Exercise 1: binary spatial lag

Let

\[
W=
\begin{bmatrix}
0&1&1\\
1&0&0\\
1&0&0
\end{bmatrix}
\]

and

\[
x=
\begin{bmatrix}
4\\
6\\
10
\end{bmatrix}.
\]

Calculate

\[
Wx.
\]

---

## Exercise 2: row standardization

Row-standardize the matrix from Exercise 1.

Then calculate the row-standardized lag.

---

## Exercise 3: distance band

Points lie at positions

\[
0,\ 2,\ 5,\ 9.
\]

Construct the binary weights matrix using

\[
d_0=3.
\]

Identify any islands.

---

## Exercise 4: inverse distance

A location has two neighbors at distances 2 km and 4 km.

Using

\[
w=d^{-1},
\]

calculate the raw weights and their row-standardized values.

---

## Exercise 5: \(k\)-NN asymmetry

Points lie at

\[
0,\ 1,\ 8.
\]

Construct directed 1-nearest-neighbor weights.

Is the matrix symmetric?

---

## Exercise 6: sensitivity

A location has rook neighbors with values 5 and 7.

Queen contiguity adds two corner neighbors with values 20 and 22.

Calculate the row-standardized spatial lag under both rules.

Explain why downstream spatial statistics may differ.

---
