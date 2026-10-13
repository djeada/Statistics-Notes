# Geostatistics Exercises

Use this problem set with the [chapter notes](../../notes/spatial_statistics/geostatistics.md) and the [visualization script](../../scripts/spatial_statistics/geostatistics_visualizations.py).


## Exercise 1: empirical semivariance

Using points

| Point | Coordinate | Value |
|---|---|---:|
| A | $(0,0)$ | 3 |
| B | $(1,0)$ | 5 |
| C | $(0,1)$ | 4 |
| D | $(1,1)$ | 8 |

calculate $\hat\gamma(1)$ using all pairs exactly 1 unit apart.

## Exercise 2: exponential model

For

$$
\gamma(h)
=
0.3+2.7(1-e^{-h/15}),
$$

calculate:

1. the nugget;
2. the partial sill;
3. the sill;
4. $\gamma(15)$;
5. the approximate practical range.

## Exercise 3: trend

Suppose

$$
m(x,y)=5+0.4x-0.2y.
$$

At location $(10,5)$, the observed value is 8.5.

Calculate the fitted mean and residual.

## Exercise 4: interpretation

An empirical variogram rises continuously across the entire observed distance range and never levels off.

Give at least three possible explanations.

---

## Worked solutions

### Solution 1: empirical semivariance

Pairs exactly 1 unit apart (horizontal or vertical neighbours): A-B, A-C, B-D, C-D. The diagonals A-D and B-C are $\sqrt2$ apart and are excluded, so $|N(1)|=4$.

| Pair | Difference | Squared |
|---|---:|---:|
| A-B | $3-5=-2$ | 4 |
| A-C | $3-4=-1$ | 1 |
| B-D | $5-8=-3$ | 9 |
| C-D | $4-8=-4$ | 16 |

Sum of squares: $4+1+9+16=30$.

$$
\hat\gamma(1)=\frac{30}{2\cdot4}=\frac{30}{8}=3.75.
$$

The mean squared difference is $30/4=7.5$; the semivariance is half of it.

### Solution 2: exponential model

$\gamma(h)=c_0+c(1-e^{-h/a})$ with $c_0=0.3$, $c=2.7$, $a=15$.

1. Nugget: $c_0=0.3$.
2. Partial sill: $c=2.7$.
3. Sill: $c_0+c=0.3+2.7=3.0$.
4. $\gamma(15)=0.3+2.7(1-e^{-1})=0.3+2.7(0.6321)=0.3+1.7067=2.0067\approx2.007$.
5. Practical range $\approx3a=45$, where $\gamma(45)=0.3+2.7(1-e^{-3})=0.3+2.7(0.9502)\approx2.866$, i.e. 95% of the partial sill.

### Solution 3: trend

$$
m(10,5)=5+0.4(10)-0.2(5)=5+4-1=8.
$$

Residual: $\varepsilon=8.5-8=0.5$.

### Solution 4: interpretation (model answer)

Any three of the following:

- an unmodeled large-scale trend (the variogram then grows with $h$ because distant points differ systematically);
- nonstationarity, such as boundaries, zones, or a changing variance;
- the study region is too small to reach the range, so the sill lies beyond the largest lag;
- a model with no sill (e.g. a power or intrinsic/linear variogram, as for Brownian-like fields);
- outliers inflating squared differences at all large lags;
- strong anisotropy mixed into an omnidirectional variogram.

The practical response is to map the data, regress on coordinates or covariates, and re-compute the variogram of the residuals.
