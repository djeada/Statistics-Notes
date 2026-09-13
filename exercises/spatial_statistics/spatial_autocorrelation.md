# Spatial Autocorrelation Exercises

Use this problem set with the [chapter notes](../../notes/spatial_statistics/spatial_autocorrelation.md) and the [visualization script](../../scripts/spatial_statistics/spatial_autocorrelation_visualizations.py).


## Exercise 1: centering

For

\[
x=(4,5,9,10),
\]

calculate:

1. \(\bar x\);
2. all centered values \(z_i\);
3. \(\sum_i z_i^2\).

---

## Exercise 2: spatial lag

Suppose a location has two neighbors with centered values

\[
-3
\quad\text{and}\quad
1.
\]

With equal row-standardized weights, calculate its spatial lag.

---

## Exercise 3: Moran numerator

Suppose

\[
z=
\begin{bmatrix}
-2\\
-1\\
1\\
2
\end{bmatrix}
\]

and

\[
Wz=
\begin{bmatrix}
-1\\
-0.5\\
0.5\\
1
\end{bmatrix}.
\]

Calculate

\[
z^\top Wz.
\]

Does the sign suggest positive or negative association?

---

## Exercise 4: null expectation

For

\[
n=25,
\]

calculate

\[
E[I]=-\frac1{n-1}.
\]

---

## Exercise 5: permutation p-value

Suppose

\[
M=499
\]

permutations are used and

\[
R=4
\]

are at least as large as the observed statistic.

Calculate the one-sided pseudo-\(p\) value.

---

## Exercise 6: multiple testing

Suppose 200 local tests are performed at unadjusted

\[
\alpha=0.05.
\]

Under the simple independent-null heuristic, how many false positives would be expected on average?

Why is this only a heuristic in spatial data?

---
