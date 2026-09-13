# Continuous Distributions

Choose a continuous distribution by considering support, shape, and the data-generating mechanism rather than by matching a familiar name.

| Situation | Useful starting model | Support / role |
|---|---|---|
| Roughly equal density over a bounded interval | [Uniform](uniform_distribution.md) | $[a,b]$ |
| Probability or proportion on the unit interval | [Beta](beta_distribution.md) | $[0,1]$ |
| Waiting time to the next constant-rate Poisson event | [Exponential](exponential_distribution.md) | positive |
| Positive waiting-time/size variable with flexible shape | [Gamma](gamma_distribution.md) | positive |
| Symmetric bell-shaped measurement model | [Normal](normal_distribution.md) | real line |
| Positive variable whose logarithm is normal | [Log-normal](log_normal_distribution.md) | positive |

## Important Relationships

- The exponential distribution is a gamma special case with shape $1$ under compatible parameterizations.
- If $Y$ is normal, then $X=e^Y$ is log-normal.
- The normal distribution is especially important because standardized sums and many sampling distributions become approximately normal under suitable conditions.

Student's t, chi-square, and F are covered in **[Sampling & Sampling Distributions](../../sampling_and_sampling_distributions/README.md)**, where their inferential roles and degrees-of-freedom parameters have context.

## Parameterization Warning

The **gamma** note uses shape $\alpha$ and **rate** $\beta$. Many software libraries expose a scale parameter instead, equal to $1/\beta$. Always translate parameterizations before comparing formulas.

A density value is not a point probability. For an absolutely continuous random variable, probabilities are obtained by integrating the density over intervals.
