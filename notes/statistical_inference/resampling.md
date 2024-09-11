
#### Simulations in Statistical Inference

- **Confidence Interval for Population Mean**: 
    \[
    \bar{x} \pm z \cdot SE(\bar{x})
    \]
    The confidence interval assumes the sample mean \( \bar{x} \) follows a normal distribution, but what if this assumption doesn’t hold? What if we cannot compute the standard error (SE) of an estimator \( \hat{\theta} \) for a population parameter \( \theta \)? Simulations, such as the Monte Carlo method, provide a solution to these challenges.

#### The Monte Carlo Method
- **Problem**: We often want to estimate an unknown parameter \( \theta \) of a population (e.g., the average height of all people in the US).
  
- **Monte Carlo Approach**: 
    - Sample \( n \) observations from the population, compute the sample mean \( \hat{\theta} \), and use it as an estimate for \( \theta \).
    - Even for moderate sample sizes, \( \hat{\theta} \) approximates \( \theta \) quite well due to the *Law of Large Numbers*.

- **Generalization**: The Monte Carlo method applies to more complex estimators and can also be used to compute the standard error \( SE(\hat{\theta}) \) by generating multiple random samples:
    1. Draw many samples (e.g., 1,000) of size \( n \).
    2. Compute \( \hat{\theta} \) for each sample.
    3. Estimate the standard error by the standard deviation of these estimates.

#### The Bootstrap Principle

- **Bootstrap Idea**: When the population is not accessible, and we have only one sample, we simulate data from the sample itself, applying the *plug-in principle*.
    - **Plug-in Principle**: If the sample histogram is close to the population histogram, the sample mean \( \hat{\theta} \) will be close to the population mean \( \theta \).

- **Bootstrap Steps**:
    1. Draw \( B \) bootstrap samples (e.g., 1,000) from the original sample with replacement.
    2. Compute \( \hat{\theta}^* \) for each bootstrap sample.
    3. Estimate quantities of interest, such as the standard error \( SE(\hat{\theta}) \), using the distribution of the bootstrap estimates.

#### Bootstrap Confidence Intervals

- **Normal Approximation Confidence Interval**:
    - If the sampling distribution of \( \hat{\theta} \) is approximately normal:
    \[
    \left[ \hat{\theta} - z_{\alpha/2} \cdot SE(\hat{\theta}), \hat{\theta} + z_{\alpha/2} \cdot SE(\hat{\theta}) \right]
    \]
    where \( SE(\hat{\theta}) \) is estimated by the bootstrap.

- **Bootstrap Percentile Interval**:
    - When the sampling distribution of \( \hat{\theta} \) is not normal, estimate it from the distribution of the bootstrap estimates:
    \[
    \left[ \hat{\theta}_{(\alpha/2)}, \hat{\theta}_{(1-\alpha/2)} \right]
    \]
    where \( \hat{\theta}_{(\alpha/2)} \) is the \( \alpha/2 \) percentile of the bootstrap estimates.

- **Bootstrap Pivotal Interval**:
    - A more accurate interval, based on \( \hat{\theta} - \theta \), is given by:
    \[
    \left[ 2\hat{\theta} - \hat{\theta}_{(1-\alpha/2)}, 2\hat{\theta} - \hat{\theta}_{(\alpha/2)} \right]
    \]

#### Bootstrapping for Regression

- **Simple Linear Regression**: Suppose we have data \( (X_1, Y_1), \dots, (X_n, Y_n) \) from the model:
    \[
    Y_i = a + b X_i + e_i
    \]
    where \( e_i \) are random errors.
    
- **Bootstrap Approach**:
    1. Compute the residuals \( \hat{e}_i = Y_i - \hat{a} - \hat{b}X_i \).
    2. Resample from these residuals to create new bootstrapped responses:
       \[
       Y_i^* = \hat{a} + \hat{b}X_i + e_i^*
       \]
    3. Use these bootstrapped samples to estimate the regression coefficients \( \hat{a}^* \) and \( \hat{b}^* \), and compute their standard errors or confidence intervals.

