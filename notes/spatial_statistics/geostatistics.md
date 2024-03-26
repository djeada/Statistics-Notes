## Advanced Geostatistics

Geostatistics is a branch of applied statistics focusing on spatial and spatiotemporal data analysis, integral in fields like earth sciences, hydrology, ecology, and environmental sciences. It deals with the modeling, prediction, and interpolation of geographically indexed data.

### Fundamental Concepts in Geostatistics

Geostatistics revolves around several critical mathematical and statistical concepts:

1. **Spatial Autocorrelation**: This concept refers to the correlation of a variable with itself across space. According to Tobler's First Law of Geography, "everything is related to everything else, but near things are more related than distant things." Mathematically, spatial autocorrelation is typically assessed through Moran's I or Geary's C statistics.

2. **Variogram and Covariogram**: Central tools in geostatistics, variograms (and their counterparts, covariograms) provide insights into the spatial correlation of data. They are functions describing the degree of spatial dependence of a spatial random field or stochastic process. The variogram, for instance, is given by:

$$
\gamma(h) = \frac{1}{2}Var(Z(x) - Z(x+h))
$$

where $\gamma(h)$ is the semivariance at lag $h$, and $Z(x)$ is the value of the geospatial variable at location $x$.

4. **Kriging**: Kriging is a set of advanced geostatistical techniques used for spatial interpolation. It is essentially a method of best linear unbiased prediction (BLUP) for random fields. The key concept behind Kriging is to interpolate the values of a random field at unsampled locations based on the spatial covariance structure derived from sampled data.

### Types of Kriging and Their Mathematical Foundations

Kriging methods are diverse, each suited to different types of data and assumptions:

I. **Simple Kriging**: This form is used when the mean of the random field is known and constant. The Kriging predictor is linear and unbiased, minimizing the mean squared error.

$$
Z^*(x_0) = \mu + \sum_{i=1}^n \lambda_i (Z(x_i) - \mu)
$$

Here, $Z^*(x_0)$ is the estimated value at location $x_0$, $\mu$ is the known mean, $Z(x_i)$ are the observed values at known locations $x_i$, and $\lambda_i$ are the weights calculated based on the variogram.

II. **Ordinary Kriging**: The most common form, it assumes an unknown but constant mean and uses local averages to estimate it.

$$
Z^*(x_0) = \sum_{i=1}^n \lambda_i Z(x_i) 
$$

Subject to the unbiasedness constraint: $\sum_{i=1}^n \lambda_i = 1$. In this case, the weights $\lambda_i$ are determined based on the variogram and the constraint ensures that the estimator is unbiased when the mean is unknown.

III. **Universal Kriging**: Here, the mean is modeled as a known function (e.g., a polynomial) of spatial coordinates. It is useful for dealing with trends over space.

$$
Z^*(x_0) = \sum_{i=1}^n \lambda_i Z(x_i) + \sum_{j=1}^m \beta_j f_j(x_0)
$$

$f_j(x_0)$ are known deterministic functions of the spatial coordinates (e.g., polynomials), and $\beta_j$ are coefficients to be estimated. The first sum is similar to ordinary kriging, estimating the variable based on spatial autocorrelation. The second sum accounts for the deterministic trend over space.

### Applications

Geostatistics finds application in various fields:

- **Natural Resource Exploration**: Identifying and estimating the distribution of oil, gas, and mineral resources.
- **Environmental Monitoring**: Studying and predicting pollution patterns, ecological distributions, etc.
- **Public Health**: Analyzing the spread of diseases and planning healthcare services based on spatial data.

### Example: Soil pH Prediction

Consider a scenario where soil pH levels are sampled at specific locations in a field. The task is to predict pH levels at unsampled locations.

1. **Data Representation**: The sampled data points are plotted spatially, with soil pH values as attributes.
2. **Variogram Analysis**: A variogram is calculated to understand how pH values correlate over distance.
3. **Kriging Application**: Employing an appropriate Kriging method, predictions for unsampled locations are made using a weighted average of the sampled values. The weights are derived from the variogram, ensuring optimal, unbiased spatial prediction.

![Soil pH level](https://github.com/djeada/Statistics-Notes/assets/37275728/d2e73c01-0891-48a9-9adb-186ff40e95a7)
