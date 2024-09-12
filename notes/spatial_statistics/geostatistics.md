# Geostatistics

Geostatistics is a branch of statistics that focuses on the analysis and interpretation of spatial or spatiotemporal datasets. It is widely used in fields such as geology, hydrology, environmental science, agriculture, and meteorology. Geostatistics provides tools for modeling spatial correlation, predicting values at unsampled locations, and quantifying the uncertainty associated with these predictions.

## Fundamental Concepts in Geostatistics

Geostatistics is built upon several key mathematical and statistical concepts essential for understanding and modeling spatial data.

### 1. Spatial Autocorrelation

**Spatial autocorrelation** refers to the correlation of a variable with itself across space. It quantifies the degree to which observations at spatial locations are similar to one another. According to Tobler's First Law of Geography:

> "Everything is related to everything else, but near things are more related than distant things."

Mathematically, spatial autocorrelation is assessed through statistics like **Moran's I** and **Geary's C**.

- **Moran's I** measures global spatial autocorrelation:

  $$
  I = \frac{n}{W} \frac{\sum_{i=1}^{n}\sum_{j=1}^{n} w_{ij}(Z_i - \bar{Z})(Z_j - \bar{Z})}{\sum_{i=1}^{n}(Z_i - \bar{Z})^2}
  $$

  Where:
  - $n $ is the number of observations.
  - $Z_i $ and $Z_j $ are the values at locations $i $ and $j $.
  - $\bar{Z} $ is the mean of $Z $.
  - $w_{ij} $ is the spatial weight between locations $i $ and $j $.
  - $W = \sum_{i=1}^{n}\sum_{j=1}^{n} w_{ij} $.

- **Geary's C** focuses on local spatial autocorrelation:

  $$
  C = \frac{(n - 1)}{2W} \frac{\sum_{i=1}^{n}\sum_{j=1}^{n} w_{ij}(Z_i - Z_j)^2}{\sum_{i=1}^{n}(Z_i - \bar{Z})^2}
  $$

Values of Moran's I range from -1 (perfect dispersion) to +1 (perfect correlation), with 0 indicating random spatial patterns.

### 2. Variogram and Covariance Function

The **variogram** and **covariance function** are fundamental tools used to quantify spatial dependence in geostatistics.

- **Variogram ($\gamma(h) $)**: Describes how the average difference between values changes with distance. It is defined as:

  $$
  \gamma(h) = \frac{1}{2} \operatorname{Var}[Z(x) - Z(x + h)] = \frac{1}{2} \mathbb{E}[(Z(x) - Z(x + h))^2]
  $$

  Where:
  - $h $ is the lag distance between two locations.
  - $Z(x) $ is the value at location $x $.

- **Covariance Function ($C(h) $)**: Describes how the covariance between values changes with distance:

  $$
  C(h) = \operatorname{Cov}[Z(x), Z(x + h)] = \mathbb{E}[(Z(x) - \mu)(Z(x + h) - \mu)]
  $$

The relationship between the variogram and covariance function is:

$$
\gamma(h) = C(0) - C(h)
$$

Where $C(0) $ is the variance of $Z $.

#### Variogram Parameters

- **Nugget ($c_0 $)**: Represents measurement error or microscale variation at distances smaller than the sampling interval. It is the variogram value as $h $ approaches zero.

- **Sill ($c_0 + c $)**: The plateau of the variogram, representing the total variance where spatial dependence levels off.

- **Range ($a $)**: The distance at which the variogram reaches the sill. Beyond this distance, spatial correlation becomes negligible.

#### Variogram Models

Common theoretical variogram models include:

- **Spherical Model**:

  $$
  \gamma(h) = c_0 + c \left[ \frac{3h}{2a} - \frac{1}{2} \left( \frac{h}{a} \right)^3 \right], \quad 0 \leq h \leq a
  $$

- **Exponential Model**:

  $$
  \gamma(h) = c_0 + c \left[ 1 - e^{-h/a} \right]
  $$

- **Gaussian Model**:

  $$
  \gamma(h) = c_0 + c \left[ 1 - e^{-(h/a)^2} \right]
  $$

### 3. Kriging

**Kriging** is a geostatistical interpolation technique that provides the best linear unbiased prediction (BLUP) for spatial data. It leverages the spatial autocorrelation quantified by the variogram to estimate values at unsampled locations.

#### Kriging Estimator

The kriging estimator for a location $x_0 $ is a weighted sum of the observed values:

$$
Z^*(x_0) = \sum_{i=1}^{n} \lambda_i Z(x_i)
$$

Where:

- $Z^*(x_0) $ is the predicted value at location $x_0 $.
- $Z(x_i) $ are observed values at locations $x_i $.
- $\lambda_i $ are the weights assigned to each observation.

#### Kriging Weights Determination

Weights $\lambda_i $ are calculated by minimizing the estimation variance $\operatorname{Var}[Z^*(x_0) - Z(x_0)] $ subject to the unbiasedness condition $\sum_{i=1}^{n} \lambda_i = 1 $. This involves solving a system of linear equations derived from the variogram model.

## Types of Kriging and Their Mathematical Foundations

Different kriging methods are tailored to specific data characteristics and assumptions about the spatial process.

### I. Simple Kriging

- **Assumptions**:
  - The mean $\mu $ of the random field is known and constant across the study area.

- **Estimator**:

  $$
  Z^*(x_0) = \mu + \sum_{i=1}^{n} \lambda_i [Z(x_i) - \mu]
  $$

- **Kriging Equations**:

  $$
  \sum_{j=1}^{n} \lambda_j C(x_i - x_j) = C(x_i - x_0), \quad i = 1, 2, \dots, n
  $$

### II. Ordinary Kriging

- **Assumptions**:
  - The mean $\mu $ is unknown but constant within the local neighborhood.

- **Estimator**:

  $$
  Z^*(x_0) = \sum_{i=1}^{n} \lambda_i Z(x_i)
  $$

- **Constraints**:

  $$
  \sum_{i=1}^{n} \lambda_i = 1
  $$

- **Kriging System**:

  $$
  \begin{cases}
  \sum_{j=1}^{n} \lambda_j \gamma(x_i - x_j) + \mu = \gamma(x_i - x_0), & i = 1, \dots, n \\
  \sum_{j=1}^{n} \lambda_j = 1
  \end{cases}
  $$

  Where $\mu $ is a Lagrange multiplier ensuring the unbiasedness constraint.

### III. Universal Kriging

- **Assumptions**:
  - The mean $\mu(x) $ is an unknown deterministic function of the spatial coordinates, often modeled using a polynomial.

- **Estimator**:

  $$
  Z^*(x_0) = \sum_{i=1}^{n} \lambda_i Z(x_i)
  $$

- **Trend Model**:

  $$
  \mu(x) = \sum_{k=1}^{m} \beta_k f_k(x)
  $$

  Where:
  - $f_k(x) $ are known basis functions (e.g., polynomials).
  - $\beta_k $ are coefficients to be estimated.

- **Constraints**:

  $$
  \sum_{i=1}^{n} \lambda_i f_k(x_i) = f_k(x_0), \quad k = 1, \dots, m
  $$

- **Kriging System**:

  $$
  \begin{cases}
  \sum_{j=1}^{n} \lambda_j \gamma(x_i - x_j) + \sum_{k=1}^{m} \mu_k f_k(x_i) = \gamma(x_i - x_0), & i = 1, \dots, n \\
  \sum_{j=1}^{n} \lambda_j f_k(x_j) = f_k(x_0), & k = 1, \dots, m
  \end{cases}
  $$

  Where $\mu_k $ are Lagrange multipliers.

## Applications of Geostatistics

Geostatistics is applied in various fields to analyze spatial data and make informed decisions.

### 1. Natural Resource Exploration

- **Mining**: Estimating mineral reserves and ore grades.
- **Oil and Gas**: Modeling reservoir properties like porosity and permeability.

### 2. Environmental Monitoring

- **Pollution Assessment**: Mapping contaminant concentrations in soil, water, or air.
- **Ecology**: Studying species distribution and habitat suitability.

### 3. Public Health

- **Epidemiology**: Analyzing disease spread patterns and identifying hotspots.
- **Resource Allocation**: Planning healthcare services based on spatial demand.

### 4. Agriculture

- **Soil Analysis**: Mapping soil properties for precision farming.
- **Yield Prediction**: Estimating crop yields based on spatial variables.

## Example: Soil pH Prediction Using Kriging

Consider a scenario where soil pH levels are sampled at specific locations within an agricultural field. The objective is to predict soil pH at unsampled locations to inform lime application strategies.

### Step 1: Data Representation

- **Sampling**: Soil pH is measured at $n $ locations $x_i $.
- **Visualization**: Plot the sampled data on a map to observe spatial patterns.

### Step 2: Variogram Analysis

- **Compute Experimental Variogram**:

  $$
  \gamma(h) = \frac{1}{2N(h)} \sum_{i=1}^{N(h)} [Z(x_i) - Z(x_i + h)]^2
  $$

  Where:
  - $N(h) $ is the number of data pairs at lag $h $.
  - $Z(x_i) $ is the pH value at location $x_i $.

- **Plot Variogram**: Graph $\gamma(h) $ versus lag distance $h $.

- **Fit Theoretical Variogram Model**: Choose a model (e.g., spherical) that best fits the experimental variogram.

  - **Estimate Parameters**:
    - **Nugget ($c_0 $)**: From the variogram intercept.
    - **Sill ($c_0 + c $)**: From the variogram plateau.
    - **Range ($a $)**: From the distance where the sill is reached.

### Step 3: Kriging Application

- **Set Up Kriging System**:

  For **Ordinary Kriging**, solve the system:

  $$
  \begin{cases}
  \sum_{j=1}^{n} \lambda_j \gamma(x_i - x_j) + \mu = \gamma(x_i - x_0), & i = 1, \dots, n \\
  \sum_{j=1}^{n} \lambda_j = 1
  \end{cases}
  $$

- **Solve for Weights ($\lambda_i $) and Lagrange Multiplier ($\mu $)**: Use matrix methods or computational software.

- **Predict Soil pH at Unsampled Location $x_0 $**:

  $$
  Z^*(x_0) = \sum_{i=1}^{n} \lambda_i Z(x_i)
  $$

- **Compute Kriging Variance ($\sigma_K^2 $)**:

  $$
  \sigma_K^2 = \gamma(0) - \sum_{i=1}^{n} \lambda_i \gamma(x_i - x_0) - \mu
  $$

  This provides a measure of the uncertainty associated with the prediction.

### Step 4: Generate Prediction Maps

- **Interpolation**: Apply kriging across a grid covering the study area to predict soil pH at all locations.

- **Visualization**: Create contour maps or surface plots of predicted soil pH values.

- **Uncertainty Mapping**: Map kriging variance to identify areas with higher prediction uncertainty.

![Soil pH Level Map](https://github.com/djeada/Statistics-Notes/assets/37275728/d2e73c01-0891-48a9-9adb-186ff40e95a7)

### Step 5: Validation

- **Cross-Validation**:

  - Temporarily remove each data point.
  - Predict its value using the remaining data.
  - Compare predicted values with actual measurements.

- **Error Metrics**:

  - **Mean Error (ME)**:

    $$
    \text{ME} = \frac{1}{n} \sum_{i=1}^{n} [Z(x_i) - Z^*_{-i}(x_i)]
    $$

    Where $Z^*_{-i}(x_i) $ is the predicted value without the $i $-th data point.

  - **Root Mean Square Error (RMSE)**:

    $$
    \text{RMSE} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} [Z(x_i) - Z^*_{-i}(x_i)]^2}
    $$

- **Assessment**: Evaluate the model's predictive performance and adjust variogram parameters if necessary.

## Important Considerations

### Assumptions

- **Stationarity**: Assumes that statistical properties (mean, variance) are constant over space or vary in a predictable way.

- **Isotropy vs. Anisotropy**:

  - **Isotropy**: Spatial correlation is the same in all directions.
  - **Anisotropy**: Spatial correlation varies with direction; may require directional variogram analysis.

### Limitations

- **Data Quality**: Outliers or errors in data can significantly affect variogram estimation and kriging results.

- **Sampling Design**: The spatial arrangement and density of sampling locations impact the reliability of spatial predictions.

- **Computational Complexity**: Kriging can be computationally intensive for large datasets.

### Model Selection

- **Variogram Model Fit**: Choosing an appropriate variogram model is crucial for accurate predictions.

- **Trend Modeling**: For data with significant trends, consider using Universal Kriging or detrending the data.

## Software for Geostatistical Analysis

Several software packages facilitate geostatistical modeling and kriging:

- **ArcGIS Geostatistical Analyst**
- **R Packages**:
  - `gstat`
  - `geoR`
  - `sp`
- **Python Libraries**:
  - `PyKrige`
  - `GeostatsPy`
- **SGeMS (Stanford Geostatistical Modeling Software)**
- **GSTools**
