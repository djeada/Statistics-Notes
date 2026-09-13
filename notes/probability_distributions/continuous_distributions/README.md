# Continuous Distributions

Choose a continuous distribution by thinking first about support, shape, and the data-generating mechanism rather than by matching a familiar name.

## Family Map

| Situation | Useful starting model | Support / role |
|---|---|---|
| Roughly equal density over a bounded interval | [Uniform](uniform_distribution.md) | $[a,b]$ |
| Probability or proportion on the unit interval | [Beta](beta_distribution.md) | $[0,1]$ |
| Waiting time to the next constant-rate Poisson event | [Exponential](exponential_distribution.md) | positive |
| Waiting time / positive quantity with flexible shape | [Gamma](gamma_distribution.md) | positive |
| Symmetric bell-shaped measurement or sampling model | [Normal](normal_distribution.md) | real line |
| Positive variable whose logarithm is normal | [Log-normal](log_normal_distribution.md) | positive |
| Standardized mean with estimated variance | [Student's t](student_t_distribution.md) | real line; inference |
| Sum of squared independent standard normals | [Chi-square](chi_square_distribution.md) | nonnegative; inference |
| Ratio of scaled independent chi-square variables | [F](f_distribution.md) | nonnegative; inference |

## Important Relationships

- The exponential distribution is a gamma special case with shape $1$ under compatible parameterizations.
- If $Y$ is normal, then $X=e^Y$ is log-normal.
- For normal-sample theory, t, chi-square, and F distributions form a connected family of reference distributions used for means, variances, ANOVA, and regression.

## Parameterization Warning

The **gamma** note uses shape $\alpha$ and **rate** $\beta$. Many software libraries expose a scale parameter instead, equal to $1/\beta$. Always translate parameterizations before comparing formulas.

A continuous density value is not a point probability. Probabilities come from integrating the density over intervals.