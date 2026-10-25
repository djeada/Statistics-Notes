# Random Variables and Distributions

A random variable turns an experiment into a numerical quantity. Its distribution describes which values are possible and how probability is allocated to them. Choosing a model therefore begins with the quantity being measured or counted, not with a familiar curve: a success count in ten trials, a trial number at first success, and a continuous waiting time are different random variables.

The foundational notes develop three complementary descriptions:

| Topic | Main question |
|---|---|
| [Introduction to distributions](https://github.com/djeada/Statistics-Notes/blob/main/notes/random_variables_and_distributions/introduction_to_distributions.md) | How do supports, probability masses, densities, and CDFs describe events? |
| [Statistical moments](https://github.com/djeada/Statistics-Notes/blob/main/notes/random_variables_and_distributions/statistical_moments.md) | How do weighted powers summarize location, spread, and shape, and when can an MGF generate them? |
| [Normal curves and z-scores](https://github.com/djeada/Statistics-Notes/blob/main/notes/random_variables_and_distributions/normal_curve_and_z_score.md) | How are measurements converted to standard-deviation units and then to normal probabilities or percentiles? |

## Distribution families and their mechanisms

The discrete families are binomial, geometric, negative binomial, and Poisson. Binomial fixes the number of independent trials and counts successes. Geometric and negative binomial fix a target number of successes and count the trials required. Poisson counts events over a specified exposure rather than over a fixed number of Bernoulli trials.

The continuous families are uniform, beta, exponential, gamma, normal, and log-normal. Their supports and mechanisms differ: bounded randomization, uncertain proportions, constant-rate waiting, accumulated positive durations, additive symmetric variation, and multiplicative positive variation respectively. A plausible support is necessary, but does not by itself determine the distribution.

## Values, moments, and model assumptions

A PMF gives point probabilities; a density gives probabilities only after integration. A CDF gives $P(X\le x)$ in either case, making it useful for translating event wording precisely. Means and variances summarize a distribution but do not determine all its probabilities. Two models can share a mean and still imply different tails, supports, and generating mechanisms.

Parameter definitions are part of the model. Gamma rate and scale are reciprocals, and negative binomial total trials differ from failures before stopping. Translate these conventions before comparing formulas or software output.

## Connections to other statistical questions

A univariate distribution describes one quantity. Modeling several quantities together requires joint distributions to define marginal and conditional laws, independence, covariance, and correlation; these are developed in [Joint Distributions and Covariance](https://github.com/djeada/Statistics-Notes/tree/main/notes/joint_distributions_and_covariance).

Student's t, chi-square, and F distributions are treated in [Sampling and Sampling Distributions](https://github.com/djeada/Statistics-Notes/tree/main/notes/sampling_and_sampling_distributions), where their degrees of freedom and roles as distributions of sample statistics have context. A distribution of individual observations and a distribution of an estimator across samples answer different questions even when both are displayed as curves.
