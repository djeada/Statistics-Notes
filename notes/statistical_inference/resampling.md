#  Simulations in Statistical Inference

Statistical inference often involves estimating population parameters and constructing confidence intervals based on sample data. Traditional methods rely on assumptions about the sampling distribution of estimators, such as normality and known standard errors. However, these assumptions may not hold, especially with small sample sizes or complex estimators. **Simulations**, like the **Monte Carlo method** and **bootstrap techniques**, offer powerful alternatives to traditional inference by using computational methods to approximate sampling distributions and estimate standard errors.

---

## Confidence Intervals for the Population Mean

### Traditional Confidence Interval

For a population mean $\mu$, the traditional confidence interval is:

$$
\bar{x} \pm z_{\alpha/2} \cdot SE(\bar{x})
$$

- $\bar{x}$: Sample mean.
- $z_{\alpha/2}$: Critical value from the standard normal distribution corresponding to the desired confidence level $(1 - \alpha)$.
- $SE(\bar{x})$: Standard error of the sample mean, typically estimated as $\frac{s}{\sqrt{n}}$ when the population standard deviation $\sigma$ is unknown.

### Limitations of Traditional Methods

- **Normality Assumption**: Assumes that $\bar{x}$ is normally distributed, which may not be valid for small $n$ or non-normal populations.
- **Unknown Standard Error**: Difficulty arises when $SE(\hat{\theta})$ cannot be easily computed due to complex estimators or unknown population parameters.

---

## Simulations in Statistical Inference

Simulations provide a way to estimate the sampling distribution of an estimator $\hat{\theta}$ without relying on strict theoretical assumptions.

---

## The Monte Carlo Method

### Overview

The **Monte Carlo method** uses random sampling from a known distribution to approximate numerical results, particularly for estimating parameters and their variability.

### Estimating an Unknown Parameter $\theta$

- **Objective**: Estimate a population parameter $\theta$, such as the average height in the U.S.
- **Approach**:
  - **Sampling**: Draw $n$ observations $X_1, X_2, \dots, X_n$ from the population.
  - **Estimation**: Compute $\hat{\theta} = \bar{X}$, the sample mean.
  - **Law of Large Numbers**: As $n$ increases, $\hat{\theta}$ converges to $\theta$.

### Estimating the Standard Error $SE(\hat{\theta})$

- **Problem**: Analytical calculation of $SE(\hat{\theta})$ may be complex.
- **Monte Carlo Solution**:
  1. **Multiple Samples**: Draw $B$ independent samples of size $n$ from the population.
  2. **Compute Estimates**: For each sample $b$, compute $\hat{\theta}_b$.
  3. **Estimate Standard Error**:

     $$
     SE(\hat{\theta}) \approx \sqrt{\frac{1}{B - 1} \sum_{b=1}^{B} (\hat{\theta}_b - \bar{\hat{\theta}})^2}
     $$

     where $\bar{\hat{\theta}} = \frac{1}{B} \sum_{b=1}^{B} \hat{\theta}_b$.

### Advantages

- **Flexibility**: Applicable to complex estimators where analytical solutions are intractable.
- **Accuracy**: Improves with the number of simulations $B$.

---

## The Bootstrap Principle

### Motivation

- **Challenge**: Often, the population distribution is unknown, and only a single sample is available.
- **Solution**: Use the sample itself to approximate the sampling distribution of $\hat{\theta}$.

### The Plug-in Principle

- **Concept**: Replace the unknown population distribution with the empirical distribution derived from the sample.
- **Justification**: If the sample is representative, its distribution approximates the population.

### Bootstrap Procedure

1. **Original Sample**: Given data $X = \{ X_1, X_2, \dots, X_n \}$.
2. **Bootstrap Samples**:
   - Generate $B$ bootstrap samples $X^{*b}$ by sampling with replacement from $X$.
   - Each bootstrap sample $X^{*b}$ has size $n$.
3. **Compute Bootstrap Estimates**:
   - For each $X^{*b}$, compute $\hat{\theta}^*_b$.
4. **Estimate Standard Error**:

   $$
   SE_{\text{boot}}(\hat{\theta}) = \sqrt{\frac{1}{B - 1} \sum_{b=1}^{B} (\hat{\theta}^*_b - \bar{\hat{\theta}}^*)^2}
   $$

   where $\bar{\hat{\theta}}^* = \frac{1}{B} \sum_{b=1}^{B} \hat{\theta}^*_b$.

---

## Bootstrap Confidence Intervals

Bootstrapping allows construction of confidence intervals without relying on normality or known standard errors.

### 1. Normal Approximation Interval

- **Assumption**: The sampling distribution of $\hat{\theta}$ is approximately normal.
- **Interval**:

  $$
  \left[ \hat{\theta} - z_{\alpha/2} \cdot SE_{\text{boot}}(\hat{\theta}), \quad \hat{\theta} + z_{\alpha/2} \cdot SE_{\text{boot}}(\hat{\theta}) \right]
  $$

- **When to Use**: Appropriate for symmetric distributions and large sample sizes.

### 2. Bootstrap Percentile Interval

- **Concept**: Uses percentiles from the bootstrap distribution.
- **Interval**:

  $$
  \left[ \hat{\theta}_{(\alpha/2)}, \quad \hat{\theta}_{(1 - \alpha/2)} \right]
  $$

- $\hat{\theta}_{(\alpha/2)}$: The $100 \times (\alpha/2)\)th percentile of $\hat{\theta}^*_b$.
- **Advantages**: Does not assume normality.

### 3. Bootstrap Pivotal Interval

- **Adjusts for Bias**: Centers the interval around $\hat{\theta}$.
- **Interval**:

  $$
  \left[ 2\hat{\theta} - \hat{\theta}_{(1 - \alpha/2)}, \quad 2\hat{\theta} - \hat{\theta}_{(\alpha/2)} \right]
  $$

- **Benefit**: More accurate for skewed distributions.

---

## Bootstrapping for Regression

Bootstrapping can estimate the variability of regression coefficients when traditional assumptions (like normality of errors) may not hold.

### Simple Linear Regression Model

$$
Y_i = a + b X_i + e_i, \quad i = 1, 2, \dots, n
$$

- $Y_i$: Response variable.
- $X_i$: Predictor variable.
- $a$, $b$: Regression coefficients.
- $e_i$: Error terms, assumed to be independent with mean zero.

### Bootstrap Approaches

#### 1. Residual Resampling

- **Steps**:
  1. **Fit Original Model**: Obtain estimates $\hat{a}$ and $\hat{b}$.
  2. **Compute Residuals**: $\hat{e}_i = Y_i - \hat{a} - \hat{b} X_i$.
  3. **Center Residuals**: Optional step to ensure mean zero.
  4. **Bootstrap Samples**:
     - Resample residuals $\hat{e}_i^*$ with replacement.
     - Generate new responses: $Y_i^* = \hat{a} + \hat{b} X_i + \hat{e}_i^*$.
  5. **Refit Model**: Compute $\hat{a}^*$ and $\hat{b}^*$ from $Y_i^*$.
  6. **Repeat**: For $B$ bootstrap samples.
  7. **Estimate Variability**: Use $\hat{b}^*$ to estimate $SE(\hat{b})$.

- **Assumption**: Error terms $e_i$ are identically distributed.

#### 2. Case Resampling (Pairs Method)

- **Steps**:
  1. **Bootstrap Samples**: Resample $(X_i, Y_i)$ pairs with replacement.
  2. **Refit Model**: Compute $\hat{a}^*$ and $\hat{b}^*$ for each sample.
  3. **Repeat**: For $B$ bootstrap samples.
  4. **Estimate Variability**: Analyze distribution of $\hat{b}^*$.

- **Advantage**: Captures variability in both $X$ and $Y$.

#### 3. Wild Bootstrap

- **Purpose**: Handles heteroscedasticity (non-constant variance of errors).
- **Method**:
  - Multiply residuals by random variables $\eta_i$ with mean zero and variance one.
  - Generate new responses: $Y_i^* = \hat{a} + \hat{b} X_i + \hat{e}_i \eta_i$.

---

## Practical Considerations

### Number of Bootstrap Samples $B$

- **Trade-off**: Larger $B$ yields more precise estimates but requires more computation.
- **Recommendation**: Use at least $B = 1,000$ for confidence intervals.

### Assumptions and Limitations

- **Representative Sample**: Bootstrap relies on the sample adequately representing the population.
- **Independence**: Observations should be independent.
- **Sample Size**: Bootstrap may be less reliable with very small samples.

