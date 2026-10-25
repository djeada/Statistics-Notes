# Statistics Notes

Statistical analysis connects a question about the world to observations and then to a conclusion with a stated uncertainty. The calculation is only one part of that connection. A numerical answer is useful when the population, sampling process, measured variables, and assumptions describe the question we actually want to answer.

## From observations to a probability model

A dataset records values for observational units. Descriptive statistics organize those values through frequencies, plots, measures of center, and measures of spread. A mean describes an arithmetic average; a median describes a middle position. Choosing between them requires a purpose, rather than a rule that one summary is always better.

Probability supplies a model for uncertainty. Events describe sets of possible outcomes, and random variables attach numbers to those outcomes. A population distribution describes an individual observation. A joint distribution describes several variables together, including how the behavior of one changes when another is known. Covariance and correlation summarize particular aspects of that joint behavior, while leaving much of the dependence unspecified.

## From a sample to an unknown parameter

A sample statistic is also a random variable before the sample is observed. Repeating a sampling process would produce different means, proportions, variances, or regression coefficients. Their sampling distributions explain why an estimate can differ from the population parameter even when the data collection and calculations are sound.

The standard deviation of this repeated-sample distribution is a standard error. It measures uncertainty in a statistic, whereas the standard deviation of the raw data measures variation among observations. Larger samples can reduce the first quantity without reducing the second. Neither quantity measures systematic bias caused by a poorly chosen sample or a misspecified model.

Estimation, confidence intervals, and hypothesis tests use this sampling behavior for different purposes. Estimation supplies a value; an interval describes uncertainty through a procedure with a coverage property; a test compares a statistic with its behavior under a specified null model. Student's t, chi-square, and F distributions arise as reference distributions for such statistics under particular assumptions.

## From a fitted relationship to a useful prediction

Regression models a response conditional on predictors. Linear regression describes a conditional mean; logistic regression describes a conditional probability for a binary outcome. Model coefficients summarize associations under the chosen specification. A causal interpretation also requires a study design or assumptions that address confounding and selection.

Good fit on the data used for estimation does not establish predictive accuracy on new observations. Resampling and validation address separate questions: a bootstrap can approximate estimator uncertainty, a permutation test can construct a null distribution, and held-out evaluation can assess prediction. Preprocessing and model selection belong inside the training process so that the evaluation data remain informative about generalization.

## Dependence changes the analysis

Observations close in time or space often share information. Time-series models represent serial dependence and forecast from an information set available at a forecast origin. Spatial models represent neighborhood structure, covariance across locations, or random event locations. In both settings, uncertainty calculations and validation must account for how observations depend on one another.

Bayesian inference adds an explicit probability distribution for unknown parameters and updates it using the likelihood. Frequentist inference evaluates procedures through their sampling behavior. Both require defensible models, careful data collection, and interpretations matched to the quantity being estimated.
