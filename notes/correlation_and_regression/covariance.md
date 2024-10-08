# Covariance

Covariance is a fundamental statistical measure that quantifies the degree to which two random variables change together. It indicates the direction of the linear relationship between variables:

- A **positive covariance** implies that as one variable increases, the other tends to increase as well.
- A **negative covariance** suggests that as one variable increases, the other tends to decrease.
- A **zero covariance** indicates no linear relationship between the variables.

## Definition

The **covariance** between two random variables $X$ and $Y$ is defined as the expected value (mean) of the product of their deviations from their respective means:

$$
\text{Cov}(X, Y) = \mathbb{E}\left[ (X - \mu_X)(Y - \mu_Y) \right]
$$

Where:

- $\text{Cov}(X, Y)$ is the covariance between $X$ and $Y$.
- $\mathbb{E}$ denotes the expected value operator.
- $\mu_X = \mathbb{E}[X]$ is the mean of $X$.
- $\mu_Y = \mathbb{E}[Y]$ is the mean of $Y$.

### Alternative Expression

By expanding the definition and applying the linearity properties of expectation, covariance can also be expressed as:

$$
\text{Cov}(X, Y) = \mathbb{E}[XY] - \mathbb{E}[X] \mathbb{E}[Y]
$$

**Derivation**:

1. Start with the definition:

$$
\text{Cov}(X, Y) = \mathbb{E}\left[ (X - \mu_X)(Y - \mu_Y) \right]
$$

2. Expand the product inside the expectation:

$$
\text{Cov}(X, Y) = \mathbb{E}\left[ XY - X \mu_Y - \mu_X Y + \mu_X \mu_Y \right]
$$

3. Use the linearity of expectation:

$$
\text{Cov}(X, Y) = \mathbb{E}[XY] - \mu_Y \mathbb{E}[X] - \mu_X \mathbb{E}[Y] + \mu_X \mu_Y
$$

4. Recognize that $\mu_X = \mathbb{E}[X]$ and $\mu_Y = \mathbb{E}[Y]$:

$$
\text{Cov}(X, Y) = \mathbb{E}[XY] - \mu_Y \mu_X - \mu_X \mu_Y + \mu_X \mu_Y = \mathbb{E}[XY] - \mu_X \mu_Y
$$

Thus, we arrive at:

$$
\text{Cov}(X, Y) = \mathbb{E}[XY] - \mathbb{E}[X] \mathbb{E}[Y]
$$

### Interpretation

- **Positive Covariance ($\text{Cov}(X, Y) > 0 $)**: Indicates that $X$ and $Y$ tend to increase or decrease together.
- **Negative Covariance ($\text{Cov}(X, Y) < 0 $)**: Indicates that when $X$ increases, $Y$ tends to decrease, and vice versa.
- **Zero Covariance ($\text{Cov}(X, Y) = 0 $)**: Suggests no linear relationship between $X$ and $Y$.

**Important Note**:

- If $X$ and $Y$ are **independent**, then $\text{Cov}(X, Y) = 0 $.
- However, a covariance of zero does **not** necessarily imply independence. Variables can be uncorrelated (zero covariance) but still dependent in a non-linear way.

## Properties of Covariance

I. **Symmetry**:

$$
\text{Cov}(X, Y) = \text{Cov}(Y, X)
$$

II. **Linearity in Each Argument**:

For constants $a$ and $b$, and random variables $X$, $Y$, and $Z$:

$$
\text{Cov}(aX + bY, Z) = a \text{Cov}(X, Z) + b \text{Cov}(Y, Z)
$$

III. **Covariance with Itself (Variance Relation)**:

The covariance of a variable with itself is the variance of that variable:

$$
\text{Cov}(X, X) = \text{Var}(X)
$$

IV. **Scaling**:

If $a$ and $b$ are constants:

$$
\text{Cov}(aX, bY) = ab \text{Cov}(X, Y)
$$

V. **Addition of Constants**:

Adding a constant to a variable does not affect the covariance:

$$
\text{Cov}(X + c, Y) = \text{Cov}(X, Y)
$$

VI. **Relationship with Correlation**:

Covariance is related to the correlation coefficient $\rho_{XY}$:

$$
\rho_{XY} = \frac{\text{Cov}(X, Y)}{\sigma_X \sigma_Y}
$$

Where $\sigma_X$ and $\sigma_Y$ are the standard deviations of $X$ and $Y$, respectively.

## Sample Covariance

When working with sample data, the sample covariance between two variables $X$ and $Y$ is calculated as:

$$
s_{XY} = \text{Cov}(X, Y) = \frac{1}{n - 1} \sum_{i=1}^{n} (X_i - \bar{X})(Y_i - \bar{Y})
$$

Where:

- $n$ is the number of observations.
- $X_i$ and $Y_i$ are the $i$-th observations of variables $X$ and $Y$.
- $\bar{X}$ and $\bar{Y}$ are the sample means of $X$ and $Y$.

**Note**: The denominator $n - 1$ provides an unbiased estimate of the covariance for a sample drawn from a population.

## Example: Calculating Covariance Step by Step

Let's calculate the covariance between two variables $X$ and $Y$ using the following dataset:

| Observation ($i$) | $X_i$ | $Y_i$ |
|-----------------------|-----------|-----------|
| 1                     | 1         | 2         |
| 2                     | 2         | 4         |
| 3                     | 3         | 6         |

### Step 1: Calculate the Sample Means

Compute the mean of $X$ and $Y$:

$$
\bar{X} = \frac{1}{n} \sum_{i=1}^{n} X_i = \frac{1 + 2 + 3}{3} = \frac{6}{3} = 2
$$

$$
\bar{Y} = \frac{1}{n} \sum_{i=1}^{n} Y_i = \frac{2 + 4 + 6}{3} = \frac{12}{3} = 4
$$

### Step 2: Compute the Deviations from the Mean

Calculate $(X_i - \bar{X})$ and $(Y_i - \bar{Y})$:

| $i$ | $X_i$ | $Y_i$ | $X_i - \bar{X}$ | $Y_i - \bar{Y}$ |
|---------|-----------|-----------|----------------------|----------------------|
| 1       | 1         | 2         | $1 - 2 = -1$     | $2 - 4 = -2 $     |
| 2       | 2         | 4         | $2 - 2 = 0 $      | $4 - 4 = 0 $      |
| 3       | 3         | 6         | $3 - 2 = 1$      | $6 - 4 = 2 $      |

### Step 3: Calculate the Product of Deviations

Compute $(X_i - \bar{X})(Y_i - \bar{Y})$:

| $i$ | $X_i - \bar{X}$ | $Y_i - \bar{Y}$ | $(X_i - \bar{X})(Y_i - \bar{Y})$ |
|---------|----------------------|----------------------|---------------------------------------|
| 1       | -1                   | -2                   | $(-1)(-2) = 2 $                    |
| 2       | 0                    | 0                    | $(0)(0) = 0 $                      |
| 3       | 1                    | 2                    | $(1)(2) = 2 $                      |

### Step 4: Sum the Products of Deviations

Compute the sum:

$$
\sum_{i=1}^{n} (X_i - \bar{X})(Y_i - \bar{Y}) = 2 + 0 + 2 = 4
$$

### Step 5: Calculate the Sample Covariance

Use the sample covariance formula:

$$
s_{XY} = \text{Cov}(X, Y) = \frac{1}{n - 1} \sum_{i=1}^{n} (X_i - \bar{X})(Y_i - \bar{Y})
$$

Since $n = 3 $:

$$
s_{XY} = \frac{1}{3 - 1} \times 4 = \frac{1}{2} \times 4 = 2
$$

Interpretation:

- The positive covariance of $2 $ indicates that $X$ and $Y$ tend to increase together.
- Since the data points lie perfectly on a straight line ($Y = 2X$), the covariance reflects a perfect positive linear relationship.

### Step 6: Calculate the Variances (Optional)

For completeness, calculate the variances of $X$ and $Y$:

#### Variance of $X$

$$
s_{XX} = \text{Var}(X) = \frac{1}{n - 1} \sum_{i=1}^{n} (X_i - \bar{X})^2
$$

Compute $(X_i - \bar{X})^2 $:

| $i$ | $X_i - \bar{X}$ | $(X_i - \bar{X})^2 $ |
|---------|----------------------|-------------------------|
| 1       | -1                   | $(-1)^2 = 1$        |
| 2       | 0                    | $(0)^2 = 0 $         |
| 3       | 1                    | $(1)^2 = 1$         |

Sum:

$$
\sum_{i=1}^{n} (X_i - \bar{X})^2 = 1 + 0 + 1 = 2
$$

Compute variance:

$$
s_{XX} = \frac{1}{2} \times 2 = 1
$$

#### Variance of $Y$

Similarly, compute $(Y_i - \bar{Y})^2 $:

| $i$ | $Y_i - \bar{Y}$ | $(Y_i - \bar{Y})^2 $ |
|---------|----------------------|-------------------------|
| 1       | -2                   | $(-2)^2 = 4 $        |
| 2       | 0                    | $(0)^2 = 0 $         |
| 3       | 2                    | $(2)^2 = 4 $         |

Sum:

$$
\sum_{i=1}^{n} (Y_i - \bar{Y})^2 = 4 + 0 + 4 = 8
$$

Compute variance:

$$
s_{YY} = \text{Var}(Y) = \frac{1}{2} \times 8 = 4
$$

### Step 7: Calculate the Correlation Coefficient (Optional)

The correlation coefficient $r_{XY}$ standardizes the covariance, providing a dimensionless measure of the strength and direction of the linear relationship:

$$
r_{XY} = \frac{s_{XY}}{\sqrt{s_{XX} \times s_{YY}}} = \frac{2}{\sqrt{1 \times 4}} = \frac{2}{2} = 1
$$

Interpretation:

- A correlation coefficient of $1$ indicates a perfect positive linear relationship between $X$ and $Y$.
- This makes sense since $Y = 2X$ in the dataset.

Plot:

![output(13)](https://github.com/user-attachments/assets/85baa5bd-7459-4d06-ad4c-6c514eac3899)

## Limitations of Covariance

I. **Scale Dependence**:

- Covariance values are affected by the units of measurement of the variables.
- For example, measuring height in meters vs. centimeters will change the covariance.

II. **Comparison Difficulties**:

- Because covariance is not standardized, comparing covariances across different datasets or variables with different scales is challenging.
- This is why the **correlation coefficient**, which standardizes covariance, is often used.

III. **Not a Measure of Strength**:

- The magnitude of covariance does not directly indicate the strength of the relationship.
- A large covariance could be due to large variances rather than a strong relationship.

IV. **Linear Relationships Only**:

- Covariance measures only linear relationships.
- It does not capture non-linear dependencies between variables.
