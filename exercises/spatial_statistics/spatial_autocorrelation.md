# Spatial Autocorrelation Exercises

Use this problem set with the [chapter notes](../../notes/spatial_statistics/spatial_autocorrelation.md) and the [visualization script](../../scripts/spatial_statistics/spatial_autocorrelation_visualizations.py).


## Exercise 1: centering

For

$$
x=(4,5,9,10),
$$

calculate:

1. $\bar x$;
2. all centered values $z_i$;
3. $\sum_i z_i^2$.

---

## Exercise 2: spatial lag

Suppose a location has two neighbors with centered values

$$
-3
\quad\text{and}\quad
1.
$$

With equal row-standardized weights, calculate its spatial lag.

---

## Exercise 3: Moran numerator

Suppose

$$
z=
\begin{bmatrix}
-2\\
-1\\
1\\
2
\end{bmatrix}
$$

and

$$
Wz=
\begin{bmatrix}
-1\\
-0.5\\
0.5\\
1
\end{bmatrix}.
$$

Calculate

$$
z^\top Wz.
$$

Does the sign suggest positive or negative association?

---

## Exercise 4: null expectation

For

$$
n=25,
$$

calculate

$$
E[I]=-\frac1{n-1}.
$$

---

## Exercise 5: permutation p-value

Suppose

$$
M=499
$$

permutations are used and

$$
R=4
$$

are at least as large as the observed statistic.

Calculate the one-sided pseudo-$p$ value.

---

## Exercise 6: multiple testing

Suppose 200 local tests are performed at unadjusted

$$
\alpha=0.05.
$$

Under the simple independent-null heuristic, how many false positives would be expected on average?

Why is this only a heuristic in spatial data?

---

## Worked solutions

### Solution 1

1. $\bar x=\dfrac{4+5+9+10}{4}=\dfrac{28}{4}=7$.
2. $z=(4-7,\ 5-7,\ 9-7,\ 10-7)=(-3,\ -2,\ 2,\ 3)$. Check: the centered values sum to 0.
3. $\sum_i z_i^2=9+4+4+9=26$.

### Solution 2

With two neighbors, each weight is $1/2$:

$$
(Wz)_i=\tfrac12(-3)+\tfrac12(1)=\frac{-3+1}{2}=-1.
$$

The neighborhood average is below the global mean, so a location with $z_i<0$ here would be low-low, and one with $z_i>0$ would be high-low.

### Solution 3

Multiply componentwise and add:

$$
z^\top Wz=(-2)(-1)+(-1)(-0.5)+(1)(0.5)+(2)(1)=2+0.5+0.5+2=5.
$$

The sign is positive: every location has the same sign as its neighborhood lag, so the pattern suggests positive spatial association. For scale, $z^\top z=4+1+1+4=10$, so the ratio $z^\top Wz/z^\top z=0.5$ (this equals Moran's $I$ if $n/S_0=1$).

### Solution 4

$$
E[I]=-\frac{1}{25-1}=-\frac1{24}\approx-0.0417.
$$

### Solution 5

$$
p=\frac{R+1}{M+1}=\frac{4+1}{499+1}=\frac{5}{500}=0.01.
$$

The smallest attainable value with $M=499$ is $1/500=0.002$.

### Solution 6

Expected false positives $=200\times0.05=10$.

This is only a heuristic because (i) neighboring local statistics share observations and neighbors, so the tests are dependent and the number of false positives has a larger variance and a different distribution than a binomial; (ii) permutation $p$-values for local statistics are conditional and not exactly uniform under the null; (iii) the null is rarely true everywhere. Adjusting with Benjamini-Hochberg or Bonferroni, or treating the map as exploratory, addresses the issue.
