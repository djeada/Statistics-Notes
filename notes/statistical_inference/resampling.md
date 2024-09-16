##  Simulations in Statistical Inference

Statistical inference often involves estimating population parameters and constructing confidence intervals based on sample data. Traditional methods rely on assumptions about the sampling distribution of estimators, such as normality and known standard errors. However, these assumptions may not hold, especially with small sample sizes or complex estimators. **Simulations**, like the **Monte Carlo method** and **bootstrap techniques**, offer powerful alternatives to traditional inference by using computational methods to approximate sampling distributions and estimate standard errors.

### Confidence Intervals for the Population Mean

#### Traditional Confidence Interval

For a population mean $\mu$, the traditional confidence interval is:

$$
\bar{x} \pm z_{\alpha/2} \cdot SE(\bar{x})
$$

where:

- $\bar{x}$: Sample mean.
- $z_{\alpha/2}$: Critical value from the standard normal distribution corresponding to the desired confidence level $(1 - \alpha)$.
- $SE(\bar{x})$: Standard error of the sample mean, typically estimated as $\frac{s}{\sqrt{n}}$ when the population standard deviation $\sigma$ is unknown.

#### Limitations of Traditional Methods

- The **normality assumption** assumes that the sample mean $\bar{x}$ is normally distributed, which may not hold for small sample sizes or non-normal populations.
- **Unknown standard error** can be problematic when $SE(\hat{\theta})$ is difficult to compute due to complex estimators or unknown population parameters.

### Simulations in Statistical Inference

Simulations provide a way to estimate the sampling distribution of an estimator $\hat{\theta}$ without relying on strict theoretical assumptions.

### The Monte Carlo Method

The **Monte Carlo method** uses random sampling from a known distribution to approximate numerical results, particularly for estimating parameters and their variability.

#### Estimating an Unknown Parameter $\theta$

- The **objective** is to estimate a population parameter $\theta$, such as the average height in the U.S.
- The **approach** involves drawing $n$ observations, denoted as $X_1, X_2, \dots, X_n$, from the population.
- To estimate, compute the sample mean **$\hat{\theta} = \bar{X}$**.
- According to the **law of large numbers**, as $n$ increases, $\hat{\theta}$ will converge to the true population parameter $\theta$.

#### Estimating the Standard Error $SE(\hat{\theta})$

- The **problem** is that calculating the standard error $SE(\hat{\theta})$ analytically can be complex.
- A **Monte Carlo solution** involves drawing multiple independent samples to estimate $SE(\hat{\theta})$.
- **Multiple samples** are drawn, with $B$ independent samples of size $n$ from the population.
- For each sample $b$, **compute estimates** $\hat{\theta}_b$.
- The **standard error** is then estimated using the formula:

$$
SE(\hat{\theta}) \approx \sqrt{\frac{1}{B - 1} \sum_{b=1}^{B} (\hat{\theta}_b - \bar{\hat{\theta}})^2}
$$

where $\bar{\hat{\theta}} = \frac{1}{B} \sum_{b=1}^{B} \hat{\theta}_b$.

#### Advantages

- The **flexibility** of this method allows it to be applied to complex estimators where analytical solutions are not feasible.
- **Accuracy** improves as the number of simulations $B$ increases.

### The Bootstrap Principle

- The **challenge** arises when the population distribution is unknown, and only a single sample is available.
- The **solution** is to use the sample itself to approximate the sampling distribution of $\hat{\theta}$.

#### The Plug-in Principle

- The **concept** involves replacing the unknown population distribution with the empirical distribution derived from the sample.
- The **justification** is that if the sample is representative, its distribution closely approximates the population.

#### Bootstrap Procedure

1. Start with the **original sample**, denoted as $X = \{ X_1, X_2, \dots, X_n \}$.
2. Generate **bootstrap samples** by sampling with replacement from $X$ to create $B$ bootstrap samples $X^{*b}$, each of size $n$.
3. For each bootstrap sample $X^{*b}$, **compute bootstrap estimates** $\hat{\theta}^*_b$.
4. Finally, **estimate the standard error** using the formula:

$$
SE_{\text{boot}}(\hat{\theta}) = \sqrt{\frac{1}{B - 1} \sum_{b=1}^{B} (\hat{\theta}^*_b - \bar{\hat{\theta}}^*)^2}
$$

where:

$$\bar{\hat{\theta}}^* = \frac{1}{B} \sum_{b=1}^{B} \hat{\theta}^*_b$$

### Bootstrap Confidence Intervals

Bootstrapping allows construction of confidence intervals without relying on normality or known standard errors.

#### 1. Normal Approximation Interval

- The **assumption** is that the sampling distribution of $\hat{\theta}$ is approximately normal.
- The **interval** is calculated as:

$$
\left[ \hat{\theta} - z_{\alpha/2} \cdot SE_{\text{boot}}(\hat{\theta}), \quad \hat{\theta} + z_{\alpha/2} \cdot SE_{\text{boot}}(\hat{\theta}) \right]
$$

This approach is appropriate for symmetric distributions and large sample sizes.

#### 2. Bootstrap Percentile Interval

- The **concept** of this interval relies on using percentiles from the bootstrap distribution.
- The **interval** is given by:

$$
\left[ \hat{\theta}_{(\alpha/2)}, \quad \hat{\theta}_{(1 - \alpha/2)} \right]
$$

- Here, $\hat{\theta}_{(\alpha/2)}$ represents the $100 \times (\alpha/2)$th percentile of $\hat{\theta}^*_b$.
- This method does not assume the distribution is normal.

#### 3. Bootstrap Pivotal Interval

- This method **adjusts for bias** by centering the interval around $\hat{\theta}$.
- The **interval** is calculated as:

$$
\left[ 2\hat{\theta} - \hat{\theta}_{(1 - \alpha/2)}, \quad 2\hat{\theta} - \hat{\theta}_{(\alpha/2)} \right]
$$

This interval is more accurate for skewed distributions.

### Bootstrapping for Regression

Bootstrapping can estimate the variability of regression coefficients when traditional assumptions (like normality of errors) may not hold.

#### Simple Linear Regression Model

$$
Y_i = a + b X_i + e_i, \quad i = 1, 2, \dots, n
$$

- $Y_i$: Response variable.
- $X_i$: Predictor variable.
- $a$, $b$: Regression coefficients.
- $e_i$: Error terms, assumed to be independent with mean zero.

#### 1. Residual Resampling

- The first step is to **fit the original model** and obtain estimates for $\hat{a}$ and $\hat{b}$.
- Next, **compute the residuals** as $\hat{e}_i = Y_i - \hat{a} - \hat{b} X_i$.
- Optionally, **center the residuals** to ensure they have a mean of zero.
- Then, **bootstrap samples** are created by resampling residuals $\hat{e}_i^*$ with replacement, and generating new responses as $Y_i^* = \hat{a} + \hat{b} X_i + \hat{e}_i^*$.
- **Refit the model** using the new responses to compute $\hat{a}^*$ and $\hat{b}^*$.
- **Repeat this process** for $B$ bootstrap samples to obtain a reliable estimate.
- Finally, **estimate the variability** by using the distribution of $\hat{b}^*$ to calculate $SE(\hat{b})$.
- This method assumes that the **error terms $e_i$** are identically distributed.

#### 2. Case Resampling (Pairs Method)

- Begin by **bootstrapping samples** by resampling $(X_i, Y_i)$ pairs with replacement.
- **Refit the model** for each sample to calculate $\hat{a}^*$ and $\hat{b}^*$.
- **Repeat this process** for $B$ bootstrap samples.
- **Estimate the variability** by analyzing the distribution of $\hat{b}^*$ from the bootstrap results.
- An advantage of this method is that it captures the variability in both **$X$ and $Y$**.

#### 3. Wild Bootstrap

- The **purpose** of the wild bootstrap is to handle heteroscedasticity, where the variance of errors is not constant.
- The **method** involves multiplying residuals by random variables $\eta_i$ that have a mean of zero and variance of one.
- New responses are then generated as $Y_i^* = \hat{a} + \hat{b} X_i + \hat{e}_i \eta_i$ to account for this variability.

### Practical Considerations

#### Number of Bootstrap Samples $B$

- There is a **trade-off** between precision and computation: using a larger $B$ provides more precise estimates but increases computational demands.
- It is generally **recommended** to use at least $B = 1,000$ when calculating confidence intervals.

#### Assumptions and Limitations

- The **bootstrap method** relies on the sample being representative of the population for accurate results.
- **Independence of observations** is crucial, as the bootstrap assumes that each observation is independent of the others.
- **Sample size** can affect reliability, with the bootstrap being less dependable when dealing with very small samples.
