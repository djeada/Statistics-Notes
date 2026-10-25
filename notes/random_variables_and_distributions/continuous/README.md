# Continuous Distributions

The continuous families here allocate probability through a density. A point has zero probability, and an interval probability is an area under the density. A density may exceed 1 without violating the probability rules: its total integral, not its maximum height, must equal 1.

Choose a family using both support and mechanism. A normal density cannot represent a strict positive boundary exactly, while a uniform density assumes much more than merely knowing two bounds.

| Situation | Starting model | Support and interpretation |
|---|---|---|
| Equal probability for equal-length subintervals of a bounded range | [Uniform](https://github.com/djeada/Statistics-Notes/blob/main/notes/random_variables_and_distributions/continuous/uniform_distribution.md) | $[a,b]$; constant density |
| An underlying probability or proportion | [Beta](https://github.com/djeada/Statistics-Notes/blob/main/notes/random_variables_and_distributions/continuous/beta_distribution.md) | $[0,1]$; flexible shape |
| Wait to the next constant-rate Poisson event | [Exponential](https://github.com/djeada/Statistics-Notes/blob/main/notes/random_variables_and_distributions/continuous/exponential_distribution.md) | Positive time; constant hazard |
| Accumulated positive waits or another suitable positive quantity | [Gamma](https://github.com/djeada/Statistics-Notes/blob/main/notes/random_variables_and_distributions/continuous/gamma_distribution.md) | Positive; shape and rate control the distribution |
| Approximately symmetric additive measurements | [Normal](https://github.com/djeada/Statistics-Notes/blob/main/notes/random_variables_and_distributions/continuous/normal_distribution.md) | Entire real line; center and scale |
| A positive quantity with a normal logarithm | [Log-normal](https://github.com/djeada/Statistics-Notes/blob/main/notes/random_variables_and_distributions/continuous/log_normal_distribution.md) | Positive; multiplicative variation |

## Relationships and parameter meanings

An exponential distribution is gamma with shape 1. A sum of independent equal-rate exponential waits is gamma with integer shape. If $Y$ is normal, then $e^Y$ is log-normal, but its original-scale mean is not simply the exponential of the log-scale mean.

The gamma formulas here use shape $\alpha$ and **rate** $\beta$. Software may instead accept **scale** $\theta=1/\beta$. In the beta distribution, $\beta$ is a second shape parameter, not a rate. A symbol's meaning and units come from the specified family and equation.

The normal distribution also approximates suitable standardized sums and sampling distributions. That does not imply that the observations being summed are normal. Student's t, chi-square, and F are developed with their inferential roles in [Sampling and Sampling Distributions](https://github.com/djeada/Statistics-Notes/tree/main/notes/sampling_and_sampling_distributions).

For each model, calculate interval probabilities from the CDF or density integral, then interpret the result in the variable's original units and experimental setting.
