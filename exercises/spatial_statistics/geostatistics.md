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
