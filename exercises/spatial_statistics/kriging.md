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

## Worked solutions

### Solution 1: ordinary-kriging constraint

$$
0.2+0.5+0.4=1.1\ne1.
$$

The weights are not valid. With $E[Z(s_i)]=m$ we get $E[\hat Z(s_0)]=m\sum_i\lambda_i=1.1\,m$, so the predictor is biased by $0.1\,m$ for any nonzero mean. A valid set would be, for example, $0.2,\,0.5,\,0.3$.

### Solution 2: prediction

$$
\hat Z(s_0)=0.25(8)+0.50(12)+0.25(16)=2+6+4=12.
$$

The weights sum to 1, so this is a valid ordinary-kriging combination.

### Solution 3: kriging variance

$$
\lambda^\top\gamma_0=0.4(1.2)+0.6(1.8)=0.48+1.08=1.56,
$$

$$
\sigma_K^2=1.56+0.2=1.76.
$$

(The standard deviation is $\sqrt{1.76}\approx1.327$.)

### Solution 4: simple kriging

Deviations from the known mean: $24-20=4$ and $18-20=-2$.

$$
\hat Z(s_0)=20+0.3(4)+0.2(-2)=20+1.2-0.4=20.8.
$$

The weights sum to $0.5$, which is allowed: the remaining weight $0.5$ is implicitly placed on the known mean.

### Solution 5: interpretation (model answer)

Kriging variance is computed conditional on the assumed model and depends only on the sampling geometry and the covariance parameters, not on the observed values. A low variance means the model is confident, not that it is right. Spatially structured cross-validation bias means the mean model or covariance model is wrong there (an unmodeled trend, nonstationarity, a boundary, wrong range or nugget). The remedy is to revise the model (trend terms, anisotropy, local fitting) and check that standardized errors are centered near 0 with RMSSE near 1.
