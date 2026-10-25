# Estimation

Estimation uses observed data to learn the value of an unknown population or model parameter. The parameter could be a mean, a success probability, a variance, or a regression coefficient. An estimator is a rule applied to a possible sample; an estimate is the number obtained from the sample that was actually collected.

## How an estimator is evaluated

Different samples produce different estimates. Bias measures the difference between an estimator's repeated-sample average and the target parameter. Variance measures its repeated-sample spread. Mean-squared error combines both because an estimator can miss its target through a systematic displacement or through random variability.

Unbiasedness alone does not guarantee a useful estimate. An estimator centered exactly on the target can vary too widely to guide a decision. Conversely, an estimator with modest bias can have lower mean-squared error when its variance is sufficiently smaller. Consistency addresses a different question: whether estimates concentrate around the target as the amount of information grows.

## Constructing an estimate

The method of moments matches empirical summaries to their model expectations. Maximum likelihood searches for parameter values under which the observed data have the greatest joint probability mass or density. These procedures can agree, as they do for the Bernoulli success proportion, or yield different estimates with different finite-sample properties.

A point estimate does not quantify its own uncertainty. Its standard error, an interval estimate, or a posterior distribution adds information about precision under stated assumptions. Two datasets can yield the same sample mean while supporting very different levels of confidence in that value. The quality of estimation therefore depends on the model and sampling process as well as the formula used to compute the estimate.
