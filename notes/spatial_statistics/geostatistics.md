# Geostatistics

Geostatistics is a branch of statistics devoted to the analysis and interpretation of spatial or spatiotemporal datasets. This field finds applications in geology, hydrology, environmental science, agriculture, meteorology, and many other areas where data vary across space. The techniques of geostatistics allow us to model spatial correlations, predict values at locations where measurements are unavailable, and quantify the uncertainty inherent in these predictions. The discussion below introduces the important ideas, mathematical tools, and practical applications of geostatistics, all while using clear formulas, diagrams, and examples to make the concepts accessible.

## Important Concepts in Geostatistics

The core of geostatistics rests on understanding spatial relationships and dependencies. This involves grasping how nearby observations influence one another and how their variability changes with distance. The field is built on several key concepts: spatial autocorrelation, variogram and covariance functions, and interpolation methods such as kriging.

### Spatial Autocorrelation

Spatial autocorrelation examines how a variable correlates with itself through space. The underlying idea is that points close to one another tend to have similar values. This principle is encapsulated in Tobler’s First Law of Geography, which asserts that “everything is related to everything else, but near things are more related than distant things.” In geostatistics, measures such as Moran’s I and Geary’s C help quantify this dependence. For instance, Moran’s I is defined as

$$I = \frac{n}{W} \frac{\sum_{i=1}^{n}\sum_{j=1}^{n} w_{ij}(Z_i - \bar{Z})(Z_j - \bar{Z})}{\sum_{i=1}^{n}(Z_i - \bar{Z})^2}$$

where $n$ is the number of observations, $Z_i$ and $Z_j$ are the values at locations $i$ and $j$, $\bar{Z}$ is the mean value, $w_{ij}$ represents spatial weights between locations, and $W = \sum_{i=1}^{n}\sum_{j=1}^{n} w_{ij}$. Geary’s C, on the other hand, emphasizes local spatial autocorrelation with the formula

$$C = \frac{(n - 1)}{2W} \frac{\sum_{i=1}^{n}\sum_{j=1}^{n} w_{ij}(Z_i - Z_j)^2}{\sum_{i=1}^{n}(Z_i - \bar{Z})^2}$$

These formulas provide a quantitative way to assess whether the spatial distribution of values is clustered, dispersed, or random.

### Variogram and Covariance Function

A variogram is a important tool that describes how the average difference between paired observations changes with distance. It is defined as

$$
\gamma(h) = \frac{1}{2} \mathrm{Var}[Z(x) - Z(x+h)] = \frac{1}{2}\, \mathbb{E}\bigl[(Z(x)-Z(x+h))^2\bigr]
$$

with $h$ representing the lag distance between two locations and $Z(x)$ being the value at location $x$. Complementing the variogram is the covariance function, which measures the degree to which values at two locations vary together:

$$
C(h) = \mathrm{Cov}[Z(x), Z(x+h)] = \mathbb{E}\bigl[(Z(x)-\mu)(Z(x+h)-\mu)\bigr]
$$

where $\mu$ is the mean of $Z$. The variogram and covariance function are closely linked by the relation

$$\gamma(h) = C(0) - C(h)$$

with $C(0)$ representing the variance of the variable.

A visual representation of a typical variogram helps illustrate these ideas. Imagine a simple ASCII diagram where the vertical axis represents the variogram value and the horizontal axis is the distance $h$:

```
   Variogram (γ)
      ^
      |          o  o  o
      |        o
      |      o
      |    o
      |  o
      |o
      +-----------------> Distance (h)
```

This diagram shows that as the lag distance increases, the variogram value increases until it reaches a plateau. Three key parameters describe a variogram model:

- The nugget ($c_0$) reflects measurement error or microscale variation.
- The sill ($c_0 + c$) is the plateau where the variogram levels off, indicating the total variance.
- The range ($a$) is the distance at which the sill is reached, beyond which spatial correlation is minimal.

Common variogram models include the spherical model,

$$\gamma(h) = c_0 + c \left[ \frac{3h}{2a} - \frac{1}{2} \left( \frac{h}{a} \right)^3 \right] \quad \text{for } 0 \leq h \leq a$$

the exponential model,

$$\gamma(h) = c_0 + c \left[ 1 - e^{-h/a} \right]$$

and the Gaussian model,

$$\gamma(h) = c_0 + c \left[ 1 - e^{-(h/a)^2} \right]$$

Each model offers a different way to capture the spatial dependence observed in the data.

### Kriging

Kriging is a powerful geostatistical interpolation technique that provides the best linear unbiased prediction (BLUP) for unsampled locations. It relies on the spatial autocorrelation captured by the variogram to weight nearby observations optimally.

The general kriging estimator is expressed as

$$Z^*(x_0) = \sum_{i=1}^{n} \lambda_i Z(x_i)$$

where $Z^*(x_0)$ is the predicted value at the location $x_0$, $Z(x_i)$ are the observed values, and $\lambda_i$ are the weights determined through optimization. The goal is to minimize the estimation variance

$$
\mathrm{Var}[Z^*(x_0) - Z(x_0)]
$$

subject to the unbiasedness constraint

$$\sum_{i=1}^{n} \lambda_i = 1$$

This requirement leads to a system of linear equations derived from the variogram model that must be solved to obtain the weights.

#### Types of Kriging

Different forms of kriging are available depending on the assumptions made about the data’s mean and trend. In simple kriging, the mean $\mu$ of the random field is assumed known and constant. The estimator takes the form

$$Z^*(x_0) = \mu + \sum_{i=1}^{n} \lambda_i [Z(x_i) - \mu]$$

with the kriging equations given by

$$\sum_{j=1}^{n} \lambda_j C(x_i - x_j) = C(x_i - x_0), \quad i = 1, 2, dots, n$$

When the mean is unknown but assumed constant locally, ordinary kriging is used. Its estimator is

$$Z^*(x_0) = \sum_{i=1}^{n} \lambda_i Z(x_i)$$

with the constraint

$$\sum_{i=1}^{n} \lambda_i = 1$$

The corresponding kriging system becomes

$$\begin{cases}
\sum_{j=1}^{n} \lambda_j \gamma(x_i - x_j) + \mu = \gamma(x_i - x_0), & i = 1, dots, n \\
\sum_{j=1}^{n} \lambda_j = 1,
\end{cases}$$

where $\mu$ is a Lagrange multiplier making sure unbiasedness. In cases where the mean exhibits a trend across the study area, universal kriging is applied. The mean is modeled as a deterministic function,

$$\mu(x) = \sum_{k=1}^{m} \beta_k f_k(x)$$

and the estimator is still

$$Z^*(x_0) = \sum_{i=1}^{n} \lambda_i Z(x_i)$$

The weights are then obtained by solving the kriging system with constraints that account for the trend functions:

$$\begin{cases}
\sum_{j=1}^{n} \lambda_j \gamma(x_i - x_j) + \sum_{k=1}^{m} \mu_k f_k(x_i) = \gamma(x_i - x_0), & i = 1, dots, n \\
\sum_{j=1}^{n} \lambda_j f_k(x_j) = f_k(x_0), & k = 1, dots, m,
\end{cases}$$

where the $\mu_k$ are Lagrange multipliers for the trend constraints.

## Applications of Geostatistics

Geostatistical methods are versatile tools that support decision making in many fields. In natural resource exploration, geostatistics assists in estimating mineral reserves and modeling reservoir properties such as porosity and permeability. Environmental monitoring applications include mapping pollution levels in soil, water, or air, as well as studying species distributions for ecological research. Public health initiatives benefit from geostatistics through analyses of disease spread and optimal resource allocation. In agriculture, soil analysis and crop yield prediction are enhanced by spatial predictions and uncertainty quantification.

## Example: Soil pH Prediction Using Kriging

Imagine a scenario where soil pH is sampled at various locations within an agricultural field. The goal is to predict pH at unsampled locations, which can help inform lime application strategies and improve crop management. Data are first collected by measuring pH at $n$ distinct locations $x_i$, and the data are visualized on a map to reveal any spatial patterns.

The next step involves computing an experimental variogram, which can be calculated as

$$\gamma(h) = \frac{1}{2N(h)} \sum_{i=1}^{N(h)} [Z(x_i) - Z(x_i + h)]^2$$

where $N(h)$ is the number of pairs of points separated by lag distance $h$. By plotting $\gamma(h)$ versus $h$, one can observe how the spatial variability increases with distance. A theoretical variogram model, such as the spherical model, is then fitted to the experimental data by estimating parameters like the nugget ($c_0$), sill ($c_0 + c$), and range ($a$).

Once the variogram model is set up, the kriging system is set up. In the case of ordinary kriging, the system to be solved is

$$\begin{cases}
\sum_{j=1}^{n} \lambda_j \gamma(x_i - x_j) + \mu = \gamma(x_i - x_0), & i = 1, dots, n \\
\sum_{j=1}^{n} \lambda_j = 1,
\end{cases}$$

where $\mu$ is the Lagrange multiplier. Solving this system yields the weights $\lambda_i$ used in the kriging estimator

$$Z^*(x_0) = \sum_{i=1}^{n} \lambda_i Z(x_i)$$

The uncertainty associated with the prediction is quantified by the kriging variance

$$\sigma_K^2 = \gamma(0) - \sum_{i=1}^{n} \lambda_i \gamma(x_i - x_0) - \mu$$

The final step involves applying the kriging prediction across a grid that covers the study area, thus generating a continuous prediction map for soil pH. An example of such a map is shown below:

![soil_ph_map](https://github.com/user-attachments/assets/04e2c8d8-c966-4b2b-a69f-5829d3ba2201)

This map not only displays predicted soil pH values but can also be complemented with an uncertainty map that highlights areas where prediction variance is high.

## Important Considerations

When functioning with geostatistical methods, it is necessary to be aware of certain assumptions and limitations. The assumption of stationarity implies that statistical properties such as the mean and variance remain constant over space or vary in a predictable manner. Researchers must also consider whether the spatial correlation is isotropic—uniform in all directions—or anisotropic, which might require directional variogram analysis.

The quality and design of the sampling campaign are also important. Outliers or errors in the data can distort variogram estimation and affect kriging results, while the spatial arrangement and density of sampling locations influence the reliability of predictions. Additionally, geostatistical methods, particularly kriging, can be computationally demanding when applied to large datasets.

## Software for Geostatistical Analysis

A range of software packages and libraries help geostatistical modeling and kriging. In the realm of proprietary software, ArcGIS Geostatistical Analyst is widely used. Open-source tools in R, such as the packages `gstat`, `geoR`, and `sp`, offer strong geostatistical capabilities. Python users may explore libraries like `PyKrige`, `GeostatsPy`, or `GSTools`, while specialized platforms like SGeMS (Stanford Geostatistical Modeling Software) provide dedicated environments for geostatistical analysis.
