# Spatial Regression Exercises

Use this problem set with the [chapter notes](../../notes/spatial_statistics/spatial_regression.md) and the [visualization script](../../scripts/spatial_statistics/spatial_regression_visualizations.py).


## Exercise 1: OLS point estimate

Let

\[
X=
\begin{bmatrix}
1&0\\
1&1\\
1&2
\end{bmatrix}
\]

and

\[
y=
\begin{bmatrix}
2\\
3\\
6
\end{bmatrix}.
\]

Calculate the OLS intercept and slope.

---

## Exercise 2: covariance interpretation

Suppose

\[
\Sigma_{ij}
=
3e^{-d_{ij}/4}
\]

for \(i\neq j\).

Calculate the covariance for locations 4 units apart.

---

## Exercise 3: whitening

If

\[
LL^\top=\Sigma,
\]

what transformed outcome and design matrix are used to express GLS as OLS?

---

## Exercise 4: spatial error interpretation

Explain why

\[
u=\lambda Wu+\varepsilon
\]

does not imply that neighboring observed outcomes directly cause one another.

---

## Exercise 5: SAR multiplier

Suppose

\[
\rho=0.
\]

What is

\[
(I-\rho W)^{-1}?
\]

What does the SAR model reduce to?

---

## Exercise 6: direct and indirect effects

Suppose the first column of an SAR impact matrix is

\[
\begin{bmatrix}
1.8\\
0.4\\
0.1
\end{bmatrix}.
\]

If predictor \(x_1\) increases by one unit, interpret all three numbers.

---
