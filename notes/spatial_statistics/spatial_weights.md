# Spatial Weights and Spatial Lags

A spatial weights matrix converts a qualitative statement such as “these locations are neighbors” into a numerical object.

For $n$ observations, let

$$
W = [w_{ij}]
$$

with $w_{ij}$ describing the connection from location $i$ to location $j$. The diagonal is usually set to zero so an observation is not its own neighbor.

## Common Weight Constructions

### Contiguity weights

For polygons, binary weights can be defined by shared boundaries:

$$
w_{ij} =
\begin{cases}
1, & A_i \text{ and } A_j \text{ are neighbors},\\
0, & \text{otherwise}.
\end{cases}
$$

“Rook” contiguity requires a shared edge. “Queen” contiguity also allows a shared vertex.

### Distance-band weights

For coordinates,

$$
w_{ij} = \mathbf{1}(0 < d_{ij} \le d_0)
$$

connects locations within threshold $d_0$.

### $k$-nearest-neighbor weights

Each observation is connected to its $k$ closest observations. This avoids isolated observations when sampling density varies, but the resulting graph may be asymmetric unless it is explicitly symmetrized.

### Distance-decay weights

A continuous alternative is

$$
w_{ij} = d_{ij}^{-\alpha}
$$

or another decreasing function of distance. A small-distance safeguard is needed when locations can coincide.

## Row Standardization

A common transformation divides each row by its row sum:

$$
w_{ij}^{(R)}
=
\frac{w_{ij}}{\sum_j w_{ij}}.
$$

For non-isolated rows,

$$
\sum_j w_{ij}^{(R)}=1.
$$

The resulting spatial lag is then a weighted neighbor average.

Row standardization changes the numerical meaning of $W$. It is not merely a computational convenience. Binary, row-standardized, and distance-decay matrices generally produce different statistics and model coefficients.

## Spatial Lag

For observed values $x=(x_1,\ldots,x_n)^\top$, the spatial lag is

$$
Wx.
$$

At location $i$,

$$
(Wx)_i = \sum_j w_{ij}x_j.
$$

A Moran scatterplot compares centered values $z_i=x_i-\bar{x}$ with their spatial lag $(Wz)_i$.

The companion script [`spatial_weights.py`](../../scripts/spatial_statistics/spatial_weights.py) builds nearest-neighbor and distance-band weights directly with NumPy/SciPy.

## Islands and Disconnected Components

A row with

$$
\sum_j w_{ij}=0
$$

is an **island**. Row standardization is undefined for that row unless a convention is chosen.

Disconnected graph components are not automatically invalid, but they change the interpretation of global summaries and may indicate that the chosen neighborhood rule does not match the study design.

## Symmetry

Contiguity and distance-band weights are naturally symmetric if the distance relation is symmetric. Directed $k$-nearest-neighbor weights need not be.

Whether $W$ is symmetric matters for:

- eigenvalues;
- SAR model admissibility;
- some analytical variance formulas;
- interpretation of “neighbor.”

Always state how $W$ was constructed rather than referring generically to “the spatial weights.”

## Sensitivity Analysis

There is rarely one uniquely correct $W$. A useful analysis checks whether conclusions survive scientifically reasonable alternatives.

Examples:

- queen vs rook contiguity;
- $k=4$ vs $k=8$ nearest neighbors;
- several distance thresholds;
- binary vs row-standardized weights.

If the conclusion disappears under a small change in $W$, the result is highly dependent on the neighborhood definition.

Next, use $W$ to study [spatial autocorrelation](spatial_autocorrelation.md).
