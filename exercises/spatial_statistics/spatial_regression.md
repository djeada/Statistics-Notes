# Spatial Regression Exercises

Use this problem set with the [chapter notes](../../notes/spatial_statistics/spatial_regression.md) and the [visualization script](../../scripts/spatial_statistics/spatial_regression_visualizations.py).


## Exercise 1: OLS point estimate

Let

$$
X=
\begin{bmatrix}
1&0\\
1&1\\
1&2
\end{bmatrix}
$$

and

$$
y=
\begin{bmatrix}
2\\
3\\
6
\end{bmatrix}.
$$

Calculate the OLS intercept and slope.

---

## Exercise 2: covariance interpretation

Suppose

$$
\Sigma_{ij}
=
3e^{-d_{ij}/4}
$$

for $i\neq j$.

Calculate the covariance for locations 4 units apart.

---

## Exercise 3: whitening

If

$$
LL^\top=\Sigma,
$$

what transformed outcome and design matrix are used to express GLS as OLS?

---

## Exercise 4: spatial error interpretation

Explain why

$$
u=\lambda Wu+\varepsilon
$$

does not imply that neighboring observed outcomes directly cause one another.

---

## Exercise 5: SAR multiplier

Suppose

$$
\rho=0.
$$

What is

$$
(I-\rho W)^{-1}?
$$

What does the SAR model reduce to?

---

## Exercise 6: direct and indirect effects

Suppose the first column of an SAR impact matrix is

$$
\begin{bmatrix}
1.8\\
0.4\\
0.1
\end{bmatrix}.
$$

If predictor $x_1$ increases by one unit, interpret all three numbers.

---

## Worked solutions

### Solution 1

$$
X^\top X=\begin{bmatrix}3&3\\3&5\end{bmatrix},\qquad
X^\top y=\begin{bmatrix}2+3+6\\0\cdot2+1\cdot3+2\cdot6\end{bmatrix}=\begin{bmatrix}11\\15\end{bmatrix}.
$$

The determinant is $3\cdot5-3\cdot3=6$, so

$$
(X^\top X)^{-1}=\frac16\begin{bmatrix}5&-3\\-3&3\end{bmatrix},\qquad
\hat\beta=\frac16\begin{bmatrix}5\cdot11-3\cdot15\\-3\cdot11+3\cdot15\end{bmatrix}
=\frac16\begin{bmatrix}10\\12\end{bmatrix}.
$$

The intercept is $10/6\approx1.667$ and the slope is $2$.

Check: fitted values are $1.667,\ 3.667,\ 5.667$, residuals are $0.333,\ -0.667,\ 0.333$; they sum to 0 and are orthogonal to $x=(0,1,2)$ ($0-0.667+0.667=0$).

### Solution 2

$$
\Sigma_{ij}=3e^{-4/4}=3e^{-1}\approx3(0.3679)=1.104.
$$

Locations 4 units apart (equal to the scale $a=4$) retain a fraction $e^{-1}\approx0.368$ of the spatial variance $3$.

### Solution 3

Take any factor with $LL^\top=\Sigma$ (e.g. Cholesky) and set

$$
y^*=L^{-1}y,\qquad X^*=L^{-1}X.
$$

Then $\mathrm{Cov}(\varepsilon^*)=L^{-1}\Sigma L^{-\top}=L^{-1}LL^\top L^{-\top}=I$, and OLS on $(y^*,X^*)$ gives

$$
(X^{*\top}X^*)^{-1}X^{*\top}y^*=(X^\top\Sigma^{-1}X)^{-1}X^\top\Sigma^{-1}y,
$$

because $X^{*\top}X^*=X^\top L^{-\top}L^{-1}X=X^\top\Sigma^{-1}X$ (and similarly for $X^{*\top}y^*$).

### Solution 4

In $u=\lambda Wu+\varepsilon$ the spatial dependence is in the unobserved disturbance, $u=(I-\lambda W)^{-1}\varepsilon$. A shock $\varepsilon_A$ leaks into neighbors' disturbances, but the mean $X\beta$ of each outcome does not contain neighbors' $y$ values. Example with the chain $A-B-C$, $\lambda=0.4$, row-standardized $W$ and $\varepsilon=(1,0,0)^\top$: $u\approx(1.095,\ 0.238,\ 0.095)^\top$. B and C have correlated disturbances because of shared unmodeled factors (omitted variables, common measurement process), not because $y_A$ enters the equation for $y_B$. Changing $x_A$ would not move $E[y_B]$.

### Solution 5

With $\rho=0$,

$$
(I-0\cdot W)^{-1}=I.
$$

The model becomes $y=X\beta+\varepsilon$, ordinary regression with no spatial spillover; all indirect effects are zero and impacts equal $\beta$ times the identity.

### Solution 6

The first column gives $\partial E[y_i]/\partial x_1$ for each location $i$ (with $x_1$ the predictor at location 1):

- location 1 (direct effect): $E[y_1]$ rises by about $1.8$, including feedback through neighbors;
- location 2 (indirect/spillover): $E[y_2]$ rises by about $0.4$ although $x_2$ did not change;
- location 3 (indirect, two steps away): $E[y_3]$ rises by about $0.1$.

The spillover decays with network distance. The total effect of the change on the whole system is $1.8+0.4+0.1=2.3$ outcome units.
