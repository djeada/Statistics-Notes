# Spatial Autocorrelation

Spatial autocorrelation asks whether values attached to locations show a systematic spatial pattern. The idea is:

> Are neighboring locations more similar, or more dissimilar, than we would expect under a stated reference mechanism?

Examples include:

- neighboring districts with similar unemployment rates;
- nearby counties with similar disease incidence;
- adjacent raster cells with similar temperature;
- neighboring census tracts with similar house prices;
- nearby monitoring sites with similar pollution levels.

Spatial autocorrelation is not a property of the values alone. Its interpretation depends on:

1. the observed values;
2. the spatial weights matrix $W$;
3. the null/reference mechanism used for inference.

The same dataset can produce different results when “neighbor” is defined differently.

## Description and Inference Use Different Ingredients

A statistic describes the alignment between observed values and a specified neighborhood graph. Its reference distribution adds a probability model for judging that alignment. Global Moran's I uses products of centered neighboring values; Geary's C uses squared differences. Both summarize a whole map and can conceal local variation.

A local statistic can identify high-high, low-low, or contrasting configurations, but a quadrant label is descriptive until it is compared with a justified null distribution. Testing many locations introduces multiplicity, and testing several neighborhood definitions introduces another selection step. Broad spatial trends can also create apparent association among raw values. The worked examples therefore keep the arithmetic, the null mechanism, and the scientific interpretation separate. A significant result establishes a departure from that reference mechanism; identifying residual dependence, stationarity, or a causal process requires further modeling.

## What is spatial autocorrelation?

Suppose a variable $x_i$ is observed at each of $n$ spatial locations. For example:

| Location | Value |
|---|---:|
| A | 2 |
| B | 3 |
| C | 4 |
| D | 8 |
| E | 9 |

If nearby locations tend to have similar values, this is called **positive spatial autocorrelation**. Examples:

- high values beside high values;
- low values beside low values.

If nearby locations tend to have contrasting values, this is called **negative spatial autocorrelation**. Examples:

- high values beside low values;
- low values beside high values.

If the observed arrangement is not distinguishable from the chosen null mechanism, there is little evidence of spatial autocorrelation under that null.

## Spatial autocorrelation requires a definition of neighborhood

Before calculating Moran's $I$, Geary's $C$, or a local statistic, we must define which locations are spatially connected. These connections are encoded in the **spatial weights matrix**

$$
W=(w_{ij}).
$$

The entry $w_{ij}$ describes how strongly location $j$ contributes to the neighborhood of location $i$. A common binary definition is

$$
w_{ij} =
\begin{cases}
1, & \text{if }i\text{ and }j\text{ are neighbors},\\
0, & \text{otherwise}.
\end{cases}
$$

Usually,

$$
w_{ii}=0,
$$

because a location is not treated as its own neighbor.

![Spatial weights network](https://raw.githubusercontent.com/djeada/Statistics-Notes/refs/heads/main/assets/spatial_statistics/spatial_autocorrelation/01_spatial_weights.png)

## Common ways to define spatial weights

There is no universally correct $W$. Common choices include:

- adjacency: regions sharing a border are neighbors;
- distance threshold: locations within a chosen distance are neighbors;
- $k$-nearest neighbors: every location is linked to its $k$ closest observations;
- inverse distance: closer observations receive larger weights;
- network-based distance: connection follows roads, rivers, or another network.

The scientific interpretation changes with the choice of weights. For example, “neighbor” could mean:

- adjacent county;
- within 5 km;
- five nearest monitoring sites;
- connected along a river channel.

The weights matrix is therefore part of the model specification, not a technical afterthought.

## Row-standardization

A common transformation makes every non-isolated row of $W$ sum to 1. If location $i$ has $k_i$ equally weighted neighbors, then each receives weight $\frac{1}{k_i}$. For example, if a location has two neighbors,

$$
w_{ij}=\frac12
$$

for each neighbor. The row-standardized spatial lag

$$
(Wz)_i =
\sum_j w_{ij}z_j
$$

then becomes the weighted average of neighboring centered values.

### Why row-standardize?

It gives a simple interpretation:

> the spatial lag is the average centered value in the neighborhood.

Row-standardization is a modeling choice; other normalizations are possible.

## Global Moran's I

Define centered observations

$$
z_i=x_i-\bar x,
$$

where

$$
\bar x =
\frac1n\sum_i x_i.
$$

Also define

$$
S_0 =
\sum_i\sum_jw_{ij}.
$$

Global Moran's $I$ is

$$
\boxed{
I =
\frac{n}{S_0}
\frac{
\sum_i\sum_jw_{ij}z_i z_j
}{
\sum_i z_i^2
}
}.
$$

### What is being calculated?

The numerator

$$
\sum_i\sum_jw_{ij}z_i z_j
$$

adds weighted products of centered values for spatially connected observations. If neighboring values have the same sign:

$$
(+)(+)>0
$$

or

$$
(-)(-)>0,
$$

they add positive contributions. If neighboring values have opposite signs:

$$
(+)(-)<0,
$$

they add negative contributions. Moran's $I$ therefore compares neighboring similarity with the overall variation in the data.

## Fully worked Moran's I example

Consider five locations arranged in a line:

$$
A-B-C-D-E.
$$

The observed values are

$$
x=
\begin{bmatrix}
2\\
3\\
4\\
8\\
9
\end{bmatrix}.
$$

We use row-standardized first-order neighbors. Thus:

- A has neighbor B;
- B has neighbors A and C;
- C has neighbors B and D;
- D has neighbors C and E;
- E has neighbor D.

The weights matrix is

$$
W=
\begin{bmatrix}
0 & 1 & 0 & 0 & 0\\
1/2 & 0 & 1/2 & 0 & 0\\
0 & 1/2 & 0 & 1/2 & 0\\
0 & 0 & 1/2 & 0 & 1/2\\
0 & 0 & 0 & 1 & 0
\end{bmatrix}.
$$

Because every row sums to 1,

$$
S_0=5.
$$

### Calculate the mean

$$
\bar x =
\frac{2+3+4+8+9}{5} =
\frac{26}{5} =
5.2.
$$

### Center the values

$$
z_i=x_i-\bar x.
$$

Therefore

$$
z=
\begin{bmatrix}
2-5.2\\
3-5.2\\
4-5.2\\
8-5.2\\
9-5.2
\end{bmatrix} =
\begin{bmatrix}
-3.2\\
-2.2\\
-1.2\\
2.8\\
3.8
\end{bmatrix}.
$$

Low-valued locations have negative deviations, while high-valued locations have positive deviations.

### Calculate the denominator

The denominator is

$$
\sum_i z_i^2.
$$

Substitute:

$$
(-3.2)^2+(-2.2)^2+(-1.2)^2+(2.8)^2+(3.8)^2.
$$

Calculate each square:

$$
10.24+4.84+1.44+7.84+14.44.
$$

Therefore

$$
\sum_i z_i^2 =
38.80.
$$

### Calculate the spatial lag $Wz$

For A:

$$
(Wz)_A=z_B=-2.2.
$$

For B:

$$
(Wz)_B =
\frac12z_A+\frac12z_C =
\frac12(-3.2)+\frac12(-1.2) =-2.2.
$$

For C:

$$
(Wz)_C =
\frac12z_B+\frac12z_D =
\frac12(-2.2)+\frac12(2.8) =0.3.
$$

For D:

$$
(Wz)_D =
\frac12z_C+\frac12z_E =
\frac12(-1.2)+\frac12(3.8) =1.3.
$$

For E:

$$
(Wz)_E=z_D=2.8.
$$

Thus

$$
Wz =
\begin{bmatrix}
-2.2\\
-2.2\\
0.3\\
1.3\\
2.8
\end{bmatrix}.
$$

### Calculate the Moran numerator

In matrix form (for any $W$),

$$
\sum_i\sum_jw_{ij}z_i z_j =
z^\top Wz.
$$

Calculate

$$
z^\top Wz =
(-3.2)(-2.2)
+
(-2.2)(-2.2)
+
(-1.2)(0.3)
+
(2.8)(1.3)
+
(3.8)(2.8).
$$

The terms are

$$
7.04+4.84-0.36+3.64+10.64.
$$

Therefore

$$
z^\top Wz =
25.80.
$$

### Calculate Moran's I

The formula is

$$
I =
\frac{n}{S_0}
\frac{z^\top Wz}{z^\top z}.
$$

Here

$$
n=5,\qquad S_0=5,
$$

so

$$
\frac{n}{S_0}=1.
$$

Therefore

$$
I =
\frac{25.80}{38.80}
$$

$$
\boxed{
I\approx0.665
}.
$$

#### Interpretation

The statistic is positive because connected locations tend to have deviations with the same sign. The sequence $2,3,4,8,9$ places relatively low values beside low values and relatively high values beside high values. For this weights matrix, the arrangement produces positive spatial autocorrelation.

## Moran's I is not an ordinary Pearson correlation

It is tempting to think:

$$
-1\le I\le1.
$$

That is not generally true. The attainable range of Moran's $I$ depends on the spatial weights structure. Let $M=I_n-\mathbf1\mathbf1^\top/n$ be the centering matrix. For symmetric $W$, the sharp bounds are $n/S_0$ times the minimum and maximum eigenvalues of $MWM$ restricted to the mean-zero subspace. The restriction matters because centering adds a constant-vector eigenvalue of zero that is not an available centered-data direction. For asymmetric weights, replace $W$ by $(W+W^\top)/2$ in the quadratic form, since its skew-symmetric part contributes zero. These bounds need not coincide with $[-1,1]$.

Moran's $I$ is a spatial quadratic-form statistic, not an ordinary Pearson correlation between two independent variables. Therefore values should be interpreted relative to:

- the chosen $W$;
- the null distribution;
- permutation or analytic reference values.

## The finite-sample null expectation

Under the common randomization null in which the observed values are exchangeable over the fixed locations,

$$
\boxed{
E[I] =
-\frac{1}{n-1}
}.
$$

For

$$
n=5,
$$

the expected value is

$$
E[I] =
-\frac{1}{4} =
-0.25.
$$

Under this finite-sample null, the expected value under “no spatial association” is therefore not exactly zero. The negative expectation follows from centering and sampling without replacement. Write $Q=\sum_i z_i^2>0$. Across random assignments, each squared value has expectation $Q/n$. For distinct locations $i\ne j$, the expected product is $-Q/[n(n-1)]$, because the centered values sum to zero. With fixed zero-diagonal weights, summing these products gives expected numerator $-S_0Q/[n(n-1)]$. Dividing by the fixed denominator $Q$ and multiplying by $n/S_0$ yields $-1/(n-1)$. The result assumes $S_0\ne0$, nonconstant values, and the stated randomization scheme. For large $n$,

$$
-\frac{1}{n-1}
$$

approaches zero.

### What is the randomization null?

The randomization null says:

> Keep the locations and spatial weights matrix fixed, but imagine that the observed values could have been assigned to those locations in any exchangeable ordering.

For the five values $2,3,4,8,9$, one possible permutation is $8,2,9,3,4$. Another is $4,9,2,8,3$. For every permutation, calculate Moran's $I$. The collection of permuted statistics forms the reference distribution under exchangeability.

![Permutation reference distribution](https://raw.githubusercontent.com/djeada/Statistics-Notes/refs/heads/main/assets/spatial_statistics/spatial_autocorrelation/04_permutation_distribution.png)

### Monte Carlo permutation inference

If every possible permutation is impractical, draw $M$ random permutations. For a positive-autocorrelation alternative, let $R$ be the number of permuted statistics at least as large as the observed statistic. Then a common Monte Carlo pseudo-$p$ value is

$$
\boxed{
p =
\frac{R+1}{M+1}
}.
$$

#### Numerical example

Suppose

$$
M=999
$$

permutations are performed. Assume only

$$
R=8
$$

permuted statistics are at least as large as the observed statistic. Then

$$
p =
\frac{8+1}{999+1} =
\frac9{1000}
$$

$$
\boxed{
p=0.009
}.
$$

This provides evidence against the chosen exchangeability null in the positive-autocorrelation direction. It does not establish a causal spatial mechanism.

### Why add 1 to numerator and denominator?

The correction

$$
\frac{R+1}{M+1}
$$

includes the observed arrangement as one member of the reference set. It also prevents reporting a Monte Carlo $p$-value of exactly zero merely because none of a finite number of simulations was more extreme. With

$$
M=999,
$$

the smallest possible pseudo-$p$ value is

$$
\frac1{1000}=0.001.
$$

### One-sided versus two-sided alternatives

The meaning of “at least as extreme” must be defined before inference. Possible alternatives include:

#### Positive spatial autocorrelation

Count permuted values satisfying

$$
I_{\text{perm}}\ge I_{\text{obs}}.
$$

#### Negative spatial autocorrelation

Count

$$
I_{\text{perm}}\le I_{\text{obs}}.
$$

#### Two-sided departure

Use a clearly stated two-sided extremeness rule, usually relative to the null center. Do not calculate a one-sided test and then describe it as two-sided.

## Geary's C

Geary's $C$ emphasizes squared differences between neighboring observations. A common form is

$$
\boxed{
C =
\frac{n-1}{2S_0}
\frac{
\sum_i\sum_jw_{ij}(x_i-x_j)^2
}{
\sum_i(x_i-\bar x)^2
}
}.
$$

Under a common null reference:

- $C\approx1$: little spatial autocorrelation;
- $C<1$: positive spatial autocorrelation;
- $C>1$: negative spatial autocorrelation.

Note that this direction is opposite to the usual interpretation of Moran's $I$. For Moran:

- larger positive values suggest positive association.

For Geary:

- values below 1 suggest positive association.

### Worked Geary's C example

Use the same five observations and row-standardized weights. We already calculated

$$
\sum_i(x_i-\bar x)^2=38.8.
$$

For the chosen $W$, row by row (A to E), the weighted squared differences are
$1,\ 1,\ 8.5,\ 8.5,\ 1$, so

$$
\sum_i\sum_jw_{ij}(x_i-x_j)^2 =
20.0.
$$

Also,

$$
n=5,
\qquad
S_0=5.
$$

Therefore

$$
C =
\frac{5-1}{2(5)}
\frac{20.0}{38.8}.
$$

First,

$$
\frac4{10}=0.4.
$$

Then

$$
\frac{20}{38.8}
\approx0.5155.
$$

Thus

$$
C
\approx
0.4(0.5155)
$$

$$
\boxed{
C\approx0.206
}.
$$

Because this is well below 1, it indicates positive spatial autocorrelation for this example.

### Moran and Geary measure related but different features

Moran's $I$ uses cross-products: $z_i z_j$. Geary's $C$ uses squared differences:

$$
(x_i-x_j)^2.
$$

Therefore they respond differently to local contrasts and extreme values. Moran's $I$ is often interpreted as a broad global association measure. Geary's $C$ can be more sensitive to local neighbor-to-neighbor differences. Neither statistic is universally better.

![Moran and Geary comparison](https://raw.githubusercontent.com/djeada/Statistics-Notes/refs/heads/main/assets/spatial_statistics/spatial_autocorrelation/05_moran_geary_sensitivity.png)

## The spatial lag

For centered values,

$$
(Wz)_i =
\sum_jw_{ij}z_j
$$

is called the **spatial lag**. With row-standardized weights, it is a weighted neighborhood average. A positive spatial lag means the neighborhood tends to be above the global mean. A negative spatial lag means the neighborhood tends to be below the global mean. This interpretation leads naturally to the Moran scatterplot.

## Moran scatterplot

A Moran scatterplot places $z_i$ on the horizontal axis and $(Wz)_i$ on the vertical axis. The four quadrants have standard interpretations.

### High-high

$$
z_i>0,
\qquad
(Wz)_i>0.
$$

A high-valued location is surrounded by high-valued neighbors.

### Low-low

$$
z_i<0,
\qquad
(Wz)_i<0.
$$

A low-valued location is surrounded by low-valued neighbors.

### High-low

$$
z_i>0,
\qquad
(Wz)_i<0.
$$

A high-valued location is surrounded by low-valued neighbors.

### Low-high

$$
z_i<0,
\qquad
(Wz)_i>0.
$$

A low-valued location is surrounded by high-valued neighbors.

![Moran scatterplot](https://raw.githubusercontent.com/djeada/Statistics-Notes/refs/heads/main/assets/spatial_statistics/spatial_autocorrelation/03_moran_scatterplot.png)

The least-squares slope through the origin of $(Wz)_i$ on $z_i$ is $z^\top Wz/z^\top z$. It equals Moran's $I$ when $S_0=n$, as for row-standardized weights with no islands. If some rows remain zero, or another normalization is used, the factor $n/S_0$ must still be applied. The scatterplot slope is a regression summary of these constructed values, not a Pearson correlation between two independently sampled vectors. The scatterplot is a diagnostic display, not a substitute for formal inference.

## Local Moran statistics

A global statistic can hide important local patterns. One common local Moran form is

$$
I_i =
\frac{z_i}{m_2}
\sum_jw_{ij}z_j,
$$

where

$$
m_2 =
\frac1n\sum_i z_i^2.
$$

Equivalently,

$$
I_i =
\frac{z_i(Wz)_i}{m_2}.
$$

With this normalization, summing local statistics gives $\sum_i I_i=S_0I$. If every row sums to one and there are no islands, then $S_0=n$, and their average equals global Moran's $I$. Software that uses a divisor $n-1$ or another normalization can report different local magnitudes, so compare formulas before comparing numerical outputs.

### What is being calculated?

The statistic multiplies:

1. the centered value at location $i$;
2. the average centered value in its neighborhood.

If both have the same sign, $I_i$ tends to be positive. If they have opposite signs, $I_i$ tends to be negative.

### Worked local Moran example

From the five-location example,

$$
\sum_i z_i^2=38.8.
$$

Therefore

$$
m_2 =
\frac{38.8}{5} =
7.76.
$$

For location A,

$$
z_A=-3.2
$$

and

$$
(Wz)_A=-2.2.
$$

Therefore

$$
I_A =
\frac{(-3.2)(-2.2)}{7.76} =
\frac{7.04}{7.76}
$$

$$
\boxed{
I_A\approx0.907
}.
$$

Both terms are negative, so A is a **low-low** location. For location D,

$$
z_D=2.8
$$

and

$$
(Wz)_D=1.3.
$$

Therefore

$$
I_D =
\frac{(2.8)(1.3)}{7.76}
$$

$$
\approx0.469.
$$

Both are positive, so D is a **high-high** location.

### A local category is not automatically significant

A location can fall in an HH quadrant without being statistically unusual under the chosen null. The category only describes the signs of: $z_i$ and $(Wz)_i$. Statistical significance requires a reference distribution for the local statistic. A common approach uses conditional or unconditional permutations, depending on the local statistic and software implementation.

A conditional local randomization may hold the focal value fixed while rearranging the remaining values among possible neighbors. An unconditional permutation moves all values. Those reference mechanisms answer different questions and can have different null moments. The global expectation $-1/(n-1)$ should not be copied automatically to every local implementation. Always document the exact inferential procedure.

### Local Moran maps

A local map can display categories such as:

- HH: high surrounded by high;
- LL: low surrounded by low;
- HL: high surrounded by low;
- LH: low surrounded by high.

![Local Moran categories](https://raw.githubusercontent.com/djeada/Statistics-Notes/refs/heads/main/assets/spatial_statistics/spatial_autocorrelation/06_local_moran_categories.png)

HH and LL are often called local clusters. HL and LH are often called spatial outliers. These labels describe spatial configuration; they do not establish a physical mechanism.

## Multiple testing

If a local statistic is tested at every location, many hypothesis tests are being performed. Suppose there are

$$
m=100
$$

locations and every null hypothesis is true. If each is tested at

$$
\alpha=0.05,
$$

then, if every true-null test has rejection probability exactly 0.05, the expected number of false positives is

$$
100(0.05)=5.
$$

Linearity of expectation gives this count without requiring independence. Dependence affects the distribution of the number of false positives and the chance of at least one, while conservative tests can reduce the expectation below five. The core problem remains:

> a map of unadjusted $p<0.05$ locations will usually contain false discoveries.

### Responses to multiple testing

Possible strategies include:

- false-discovery-rate control;
- family-wise error adjustments;
- simulation-based global procedures;
- treating local maps as exploratory rather than confirmatory.

One widely used method is the Benjamini-Hochberg false-discovery-rate procedure. This goal differs from Bonferroni-style family-wise error control. FDR procedures tolerate some false discoveries while controlling their expected proportion under specified assumptions. For standard Benjamini-Hochberg control, those assumptions include independence or a suitable positive regression dependence condition for the null p-values; spatial proximity alone does not establish it. Bonferroni and Holm control family-wise error for valid p-values under arbitrary dependence. The desired error criterion and the calibration of the individual local tests both need to match the claim being mapped.

## First-order trend can mimic spatial dependence

Suppose

$$
X(s) =
m(s)+\varepsilon(s),
$$

where $m(s)$ changes smoothly over space. Nearby locations will often have similar $m(s)$. Therefore the raw observations can show positive Moran's $I$ even if $\varepsilon(s)$ is spatially independent. This is analogous to trend confounding in geostatistics.

![Trend-induced spatial autocorrelation](https://raw.githubusercontent.com/djeada/Statistics-Notes/refs/heads/main/assets/spatial_statistics/spatial_autocorrelation/07_trend_vs_residual.png)

### Numerical trend example

Suppose observations lie along a line at

$$
x=0,1,2,3,4.
$$

Let

$$
X(x)=5+2x+\varepsilon(x),
$$

with small independent residuals. Ignoring the trend produces values that increase smoothly across space. Neighbors therefore look similar. If we fit the mean

$$
m(x)=5+2x
$$

and define residuals

$$
e(x)=X(x)-m(x),
$$

the residual Moran statistic may be near its null reference. For example, with the five-point line and weights above, the noise-free values $5,7,9,11,13$ give $z=(-4,-2,0,2,4)$, $Wz=(-2,-2,0,2,2)$, $z^\top Wz=24$, $\sum z_i^2=40$, so $I=0.6$, even though there is no residual dependence at all. Note that the null expectation $-1/(n-1)$ applies to raw values under exchangeability; for regression residuals the null mean and variance of $I$ depend on the design matrix and $W$. In this example, the spatial association in the raw values is primarily first-order structure rather than residual dependence.

### Why detrending changes the scientific question

A Moran statistic on raw values asks:

> Are the observed values spatially arranged?

A Moran statistic on regression residuals asks:

> After accounting for the modeled covariates or trend, does spatial pattern remain?

These are different scientific questions. Neither is automatically preferable; the appropriate choice depends on the scientific objective.

## Sensitivity to the spatial weights matrix

Suppose a dataset contains a cluster at a spatial scale of about 2 km. A weights matrix connecting only observations within 500 m may miss much of that structure. A weights matrix connecting everything within 10 km may dilute it. Moran's $I$ is therefore partly scale-dependent through $W$.

![Weights-scale sensitivity](https://raw.githubusercontent.com/djeada/Statistics-Notes/refs/heads/main/assets/spatial_statistics/spatial_autocorrelation/08_weights_scale_sensitivity.png)

A good analysis should justify the spatial scale scientifically or examine sensitivity across plausible choices. Do not search many weight matrices and report only the one producing the smallest $p$-value without acknowledging that model-selection step.

## Isolated observations

Some weights definitions can produce locations with no neighbors. These are sometimes called **islands**. For a row-standardized matrix, a row with no neighbors cannot be standardized in the ordinary way. Possible responses include:

- increase the distance threshold;
- use $k$-nearest neighbors;
- define a special rule for islands;
- remove them only with strong justification.

How islands are handled can affect both global and local statistics.

## Permutation inference does not prove stationarity

A significant permutation test tells us that the observed arrangement is unusual under the stated exchangeability null. It does not show that:

- the process is stationary;
- the weights matrix is scientifically correct;
- the effect is causal;
- the residual distribution is Gaussian;
- a spatial regression model is correctly specified.

Inference is always relative to the stated reference mechanism.

## What Moran's I does not tell you

A significant Moran statistic does not identify:

- the physical mechanism generating the pattern;
- the correct spatial scale;
- whether a covariate effect is causal;
- whether a geostatistical covariance model is valid;
- whether a point pattern is clustered;
- whether spatial prediction will be accurate.

These require separate models and diagnostics.

## Spatial autocorrelation versus point-process clustering

These concepts are distinct but easy to confuse.

### Spatial autocorrelation

Values are attached to known locations. Example:

$$
\text{county}\rightarrow\text{unemployment rate}.
$$

Question:

> Are neighboring values similar?

### Point-process clustering

The event locations themselves are random. Example:

$$
\text{locations of burglaries}.
$$

Question:

> Are events arranged more densely or regularly than expected?

Moran's $I$ is not a generic test of point-pattern clustering.

## A complete workflow

A practical spatial-autocorrelation analysis can follow this sequence.

### Map the observations

Look for:

- trend;
- regional differences;
- outliers;
- missing areas;
- boundaries.

### Define the scientific neighborhood

Construct $W$ from:

- adjacency;
- distance;
- nearest neighbors;
- a network;
- another justified relationship.

### Inspect the weights

Check:

- number of neighbors per location;
- islands;
- symmetry/asymmetry;
- row-standardization.

### Calculate a global statistic

For example:

- Moran's $I$;
- Geary's $C$.

### Define the null hypothesis

State exactly what is being randomized or assumed.

### Perform inference

Use:

- permutation inference;
- an appropriate analytic reference distribution;
- another justified procedure.

### Investigate first-order structure

Ask whether:

- trend;
- omitted covariates;
- regional means

explain the apparent dependence.

### Inspect local structure if scientifically useful

Calculate local statistics and correct or qualify for multiple testing.

### Perform sensitivity analysis

Check whether conclusions depend strongly on plausible choices of $W$.

### Move to a model if needed

Significant spatial autocorrelation is often a diagnostic that a spatial regression, geostatistical, or other explicit spatial model may be needed.

## Common mistakes

### Interpreting Moran's I without stating the weights

The statistic has no complete meaning without $W$.

### Treating Moran's I as an ordinary correlation bounded by $[-1,1]$

Its attainable range depends on the weights structure.

### Assuming the null expectation is exactly zero

Under common randomization,

$$
E[I]=-\frac1{n-1}.
$$

### Interpreting a significant test as proof of causality

It only rejects or challenges the stated reference mechanism.

### Ignoring a large-scale trend

A trend can create strong raw spatial autocorrelation.

### Treating HH and LL labels as automatically significant

Quadrant membership is descriptive.

### Mapping many unadjusted local tests

This creates a multiple-testing problem.

### Trying many weights matrices and reporting only the strongest result

That introduces unreported model-selection uncertainty.

### Using Moran's I to answer a point-process question

Point-pattern clustering requires point-process methods.

## Compact worked interpretation

Suppose a study has

$$
n=50
$$

regions. A row-standardized adjacency matrix is used. The observed statistic is

$$
I=0.31.
$$

Under randomization,

$$
E[I] =
-\frac1{49}
\approx-0.0204.
$$

A permutation test using $999$ permutations gives

$$
p=0.004
$$

for the positive-autocorrelation alternative. A careful interpretation is:

> Values in neighboring regions are more similar than expected under the specified exchangeability/randomization null for this adjacency matrix.

A careless interpretation would be:

> Geography causes the outcome.

The second statement is not established by Moran's $I$.

## Connecting a Pattern Summary to an Explanation

Center the values, calculate their spatial lag using a justified W, and inspect how neighboring products or differences contribute to a global statistic. Next specify the reference mechanism and the direction of the alternative. The observed value, its null expectation, and its permutation tail probability play different roles: the first describes the map, the second supplies a comparison center, and the third quantifies extremeness under a model.

If broad trends or covariates explain the raw arrangement, a residual analysis asks whether structure remains after that explanation. Its reference distribution must account for fitting. Local analysis can then investigate where patterns occur, with a stated normalization and multiple-testing strategy. Finally, use an explicit spatial model when the goal is prediction, parameter interpretation, or a mechanism of dependence. A significant global statistic is evidence relevant to those next questions, but it does not choose their answers by itself.

## Questions students should be able to answer

1. Why must a spatial weights matrix be defined before Moran's $I$ can be interpreted?
2. What does row-standardization do?
3. What does the product $z_i z_j$ tell us for two neighbors?
4. Why do same-sign deviations contribute positively to Moran's numerator?
5. Why is Moran's $I$ not generally bounded by $-1$ and $1$?
6. Under the randomization null, what is $E[I]$?
7. What exactly is permuted in a Moran permutation test?
8. Why is $(R+1)/(M+1)$ used?
9. How does Geary's $C$ differ mathematically from Moran's $I$?
10. What do HH, LL, HL, and LH mean?
11. Why is a local quadrant label not automatically statistically significant?
12. Why do many local tests create a multiple-testing problem?
13. How can a smooth mean trend generate positive raw Moran's $I$?
14. Why can the result change when $W$ changes?
15. What can a significant Moran statistic not establish?

## Practice

Use the companion [spatial autocorrelation exercises](https://github.com/djeada/Statistics-Notes/blob/main/exercises/spatial_statistics/spatial_autocorrelation.md).
