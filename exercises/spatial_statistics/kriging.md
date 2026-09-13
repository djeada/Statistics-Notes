# Kriging Exercises

Use this problem set with the [chapter notes](../../notes/spatial_statistics/kriging.md) and the [visualization script](../../scripts/spatial_statistics/kriging_visualizations.py).


## Exercise 1: ordinary-kriging constraint

Suppose ordinary-kriging weights are

$$
0.2,\quad0.5,\quad0.4.
$$

Are they valid with respect to the unbiasedness constraint?

If not, explain why.

---

## Exercise 2: calculate a prediction

Suppose

$$
\lambda=
\begin{bmatrix}
0.25\\
0.50\\
0.25
\end{bmatrix}
$$

and

$$
z=
\begin{bmatrix}
8\\
12\\
16
\end{bmatrix}.
$$

Calculate

$$
\hat Z(s_0)=\lambda^\top z.
$$

---

## Exercise 3: calculate kriging variance

Suppose

$$
\lambda=
\begin{bmatrix}
0.4\\
0.6
\end{bmatrix},
$$

$$
\gamma_0=
\begin{bmatrix}
1.2\\
1.8
\end{bmatrix},
$$

and

$$
\mu=0.2.
$$

Using the sign convention in this chapter, calculate

$$
\sigma_K^2
=
\lambda^\top\gamma_0+\mu.
$$

---

## Exercise 4: simple kriging

Suppose the known mean is 20.

The simple-kriging weights are

$$
0.3,\quad0.2,
$$

and the two observations are

$$
24,\quad18.
$$

Calculate the prediction using deviations from the known mean.

---

## Exercise 5: interpretation

A kriging uncertainty map shows a very low variance in one region, but cross-validation residuals in that region have strong spatial bias.

Explain why the low kriging variance does not resolve the modeling problem.

---
