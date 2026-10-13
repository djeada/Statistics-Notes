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

## Worked solutions

### Exercise 1

Each entry of $Wx$ is the sum of the neighbor values in that row.

- Row 1 has neighbors 2 and 3: $1(6)+1(10)=16$.
- Row 2 has neighbor 1: $1(4)=4$.
- Row 3 has neighbor 1: $1(4)=4$.

$$
Wx=
\begin{bmatrix}16\\4\\4\end{bmatrix}.
$$

These are neighbor sums, not averages.

### Exercise 2

Row sums are $s=(2,1,1)$. Divide each row by its sum:

$$
W^{(R)}=
\begin{bmatrix}
0&1/2&1/2\\
1&0&0\\
1&0&0
\end{bmatrix}.
$$

The lag is

- row 1: $\tfrac12(6)+\tfrac12(10)=8$;
- row 2: $1(4)=4$;
- row 3: $1(4)=4$.

$$
W^{(R)}x=
\begin{bmatrix}8\\4\\4\end{bmatrix}.
$$

Row 1 is now the neighbor mean (8) rather than the sum (16). Note that $W^{(R)}$ is no longer symmetric even though $W$ was.

### Exercise 3

Label the points $A=0,B=2,C=5,D=9$ and compute the pairwise distances:

| pair | distance | $\le 3$? |
|---|---|---|
| A-B | 2 | yes |
| A-C | 5 | no |
| A-D | 9 | no |
| B-C | 3 | yes (boundary included) |
| B-D | 7 | no |
| C-D | 4 | no |

$$
W=
\begin{bmatrix}
0&1&0&0\\
1&0&1&0\\
0&1&0&0\\
0&0&0&0
\end{bmatrix}.
$$

Row 4 sums to 0, so D (position 9) is an **island**. The B-C link exists only because the rule is $d\le d_0$; with a strict inequality it would vanish and C would become a second island.

### Exercise 4

Raw weights are $w=d^{-1}$:

$$
w_1=\frac12=0.5,
\qquad
w_2=\frac14=0.25.
$$

The row sum is $0.75$, so

$$
w_1^{(R)}=\frac{0.5}{0.75}=\frac23,
\qquad
w_2^{(R)}=\frac{0.25}{0.75}=\frac13.
$$

The neighbor at 2 km gets twice the weight of the neighbor at 4 km, because halving the distance doubles $d^{-1}$.

### Exercise 5

Label the points $A=0,B=1,C=8$.

- A's nearest neighbor is B (distance 1 versus 8).
- B's nearest neighbor is A (distance 1 versus 7).
- C's nearest neighbor is B (distance 7 versus 8).

$$
W=
\begin{bmatrix}
0&1&0\\
1&0&0\\
0&1&0
\end{bmatrix}.
$$

Since $w_{CB}=1$ but $w_{BC}=0$, $W\neq W^\top$: the matrix is **not symmetric**. The union rule would add $w_{BC}=1$; the mutual rule would drop $w_{CB}$ (leaving C an island).

### Exercise 6

Rook rule, neighbors 5 and 7, each with weight $1/2$:

$$
\frac{5+7}{2}=6.
$$

Queen rule, four neighbors each with weight $1/4$:

$$
\frac{5+7+20+22}{4}=\frac{54}{4}=13.5.
$$

The lag more than doubles because the two corner neighbors are much larger than the edge neighbors. Moran's $I$, local statistics and any SAR/SEM coefficients use $Wz$ or $W$ directly, so they inherit this change: a location that looks like a low-value cell surrounded by medium values under rook can look like a low cell surrounded by high values under queen. Results should therefore be reported for both definitions.
