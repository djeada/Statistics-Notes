# Spatial Autocorrelation

**Spatial autocorrelation** refers to the correlation of a variable with itself through space. It measures the degree to which similar or dissimilar values of a variable are clustered or dispersed in a geographical area. This concept is rooted in **Tobler's First Law of Geography**:

> "Everything is related to everything else, but near things are more related than distant things."

Understanding spatial autocorrelation is fundamental in spatial analysis, geography, environmental science, and many other fields dealing with spatial data.

---

## Types of Spatial Autocorrelation

Spatial autocorrelation can be classified into three types:

### 1. Positive Spatial Autocorrelation

- **Definition**: Occurs when similar values cluster together in space.
- **Implication**: High values are surrounded by high values, and low values are surrounded by low values.
- **Examples**:
- Elevation levels in a mountainous region.
- Temperature distributions where warmer areas are adjacent to other warm areas.

### 2. Negative Spatial Autocorrelation

- **Definition**: Occurs when dissimilar values are adjacent.
- **Implication**: High values are near low values, creating a checkerboard pattern.
- **Examples**:
- Agricultural land alternating with urban areas.
- Predatory and prey species distributions in an ecosystem.

### 3. Zero Spatial Autocorrelation

- **Definition**: No apparent spatial pattern; values are randomly distributed in space.
- **Implication**: Location does not influence attribute similarity.

---

## Measures of Spatial Autocorrelation

Several statistical measures quantify the degree of spatial autocorrelation:

### 1. Moran's I

#### Definition

- A global measure of spatial autocorrelation.
- Values range from **-1** (perfect dispersion) to **+1** (perfect correlation).
- A value of **0** indicates a random spatial pattern.

#### Formula

$$
I = \frac{n}{W} \cdot \frac{\sum_{i=1}^{n} \sum_{j=1}^{n} w_{ij} (x_i - \bar{x})(x_j - \bar{x})}{\sum_{i=1}^{n} (x_i - \bar{x})^2}
$$

- $n$: Number of spatial units.
- $x_i$: Value at location $i$.
- $\bar{x}$: Mean of the variable.
- $w_{ij}$: Spatial weight between locations $i$ and $j$.
- $W$: Sum of all spatial weights ($W = \sum_{i=1}^{n} \sum_{j=1}^{n} w_{ij}$).

#### Interpretation

- **$I > 0$**: Positive spatial autocorrelation (clustering of similar values).
- **$I < 0$**: Negative spatial autocorrelation (clustering of dissimilar values).
- **$I = 0$**: No spatial autocorrelation (random distribution).

### 2. Geary's C

#### Definition

- A global measure sensitive to local spatial autocorrelation.
- Values range from **0** (perfect positive autocorrelation) to **2** (perfect negative autocorrelation).
- A value of **1** indicates no spatial autocorrelation.

#### Formula

$$
C = \frac{(n - 1)}{2W} \cdot \frac{\sum_{i=1}^{n} \sum_{j=1}^{n} w_{ij} (x_i - x_j)^2}{\sum_{i=1}^{n} (x_i - \bar{x})^2}
$$

#### Interpretation

- **$C < 1$**: Positive spatial autocorrelation.
- **$C > 1$**: Negative spatial autocorrelation.
- **$C = 1$**: Random spatial pattern.

### 3. Local Indicators of Spatial Association (LISA)

#### Definition

- Measures local spatial autocorrelation.
- Identifies clusters (hot spots and cold spots) and spatial outliers.
- Provides a statistic for each location.

#### Example: Local Moran's I

$$
I_i = (x_i - \bar{x}) \cdot \sum_{j} w_{ij} (x_j - \bar{x})
$$

- $I_i$: Local Moran's I at location $i$.

#### Interpretation

- **High-High Clusters (Hot Spots)**: Locations where high values are surrounded by high values.
- **Low-Low Clusters (Cold Spots)**: Locations where low values are surrounded by low values.
- **High-Low Outliers**: High value surrounded by low values.
- **Low-High Outliers**: Low value surrounded by high values.

---

## Applications of Spatial Autocorrelation

Understanding spatial autocorrelation is essential in various fields:

### Geography and Cartography

- **Mapping Spatial Patterns**: Identifying regions with similar attributes.
- **Spatial Interpolation**: Estimating values at unmeasured locations based on nearby measured values.

### Epidemiology

- **Disease Spread**: Analyzing how diseases propagate through space.
- **Health Resource Allocation**: Planning based on regional health data.

### Urban Planning

- **Land Use Analysis**: Understanding the distribution of residential, commercial, and industrial areas.
- **Transportation Networks**: Optimizing routes and infrastructure based on spatial patterns.

### Environmental Science

- **Biodiversity Studies**: Mapping species distributions to identify areas of high diversity.
- **Pollution Monitoring**: Identifying areas with high levels of contamination.

---

## Example: Spatial Autocorrelation in Tree Heights

### Scenario

Suppose we are studying the distribution of a certain species of tree across a national park. Each tree is a point in space, and the attribute of interest is the **tree's height**.

### Observations

- **Positive Spatial Autocorrelation**: Tall trees tend to be near other tall trees, and short trees tend to be near other short trees.
- **Possible Reasons**:
- **Soil Quality**: Areas with richer soil nutrients support taller trees.
- **Microclimate Conditions**: Regions with optimal sunlight and moisture.
- **Seed Dispersal Patterns**: Limited dispersal range leading to clusters of similar-aged trees.

### Visual Representation

![Spatial Autocorrelation of Tree Heights](https://github.com/user-attachments/assets/3ef9948c-f28f-4b31-aeb9-c5f26788a9ed)

*Figure: A map illustrating the spatial distribution of tree heights in a national park. Clusters of tall trees (depicted with larger symbols) and clusters of short trees (depicted with smaller symbols) are evident.*

### Quantifying with Moran's I

To quantify the spatial autocorrelation of tree heights, we can calculate **Moran's I**:

1. **Compute the Mean Tree Height ($\bar{x}$)**:

$$
\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i
$$

2. **Construct the Spatial Weights Matrix ($w_{ij}$)**:

- Define the spatial relationships (e.g., adjacency, distance-based weights).
- Commonly, $w_{ij} = 1$ if locations $i$ and $j$ are neighbors; otherwise, $w_{ij} = 0$.

3. **Calculate Moran's I** using the formula provided earlier.

4. **Interpret the Result**:

- If $I$ is significantly greater than 0, there is evidence of positive spatial autocorrelation among tree heights.

### Identifying Hot Spots and Cold Spots with LISA

Using **Local Indicators of Spatial Association (LISA)**, specifically Local Moran's I:

- **Hot Spots**:

- Areas where tall trees are significantly clustered.
- Indicates regions with favorable growth conditions.

- **Cold Spots**:

- Areas where short trees are significantly clustered.
- May suggest poor soil quality or environmental stress.

---

## Mathematical Rigor in Spatial Autocorrelation

### Spatial Weights Matrix ($w_{ij}$)

- **Definition**: Defines the spatial relationship between locations $i$ and $j$.
- **Construction Methods**:
- **Contiguity-Based Weights**: $w_{ij} = 1$ if $i$ and $j$ share a border; else $0$.
- **Distance-Based Weights**:

$$
w_{ij} = \frac{1}{d_{ij}^\beta}
$$

- $d_{ij}$: Distance between $i$ and $j$.
- $\beta$: Distance decay parameter.

### Statistical Significance Testing

- **Null Hypothesis ($H_0$)**: No spatial autocorrelation exists (random spatial pattern).
- **Alternative Hypothesis ($H_1$)**: Spatial autocorrelation exists.

#### Steps

1. **Compute Expected Value of Moran's I ($E[I]$)**:

$$
E[I] = -\frac{1}{n - 1}
$$

2. **Compute Variance of Moran's I ($\text{Var}[I]$)** (complex formula involving weights).

3. **Calculate Z-Score**:

$$
Z = \frac{I_{\text{observed}} - E[I]}{\sqrt{\text{Var}[I]}}
$$

4. **Determine P-Value**:

- Based on the Z-score and standard normal distribution.
- If the p-value is less than the significance level (e.g., 0.05), reject $H_0$.

---

## Assumptions and Limitations

### Assumptions

1. **Stationarity**: Statistical properties are constant over space.
2. **Isotropy**: Spatial autocorrelation is the same in all directions.
3. **Independence**: Observations are independent, given the spatial structure.

### Limitations

- **Edge Effects**: Problems arising at the boundaries of the study area.
- **Scale Dependency**: Results may vary with the spatial scale of analysis.
- **Modifiable Areal Unit Problem (MAUP)**: Statistical results can change based on how spatial units are defined.
