# Regression

Regression models a response conditional on one or more predictors. The target can be a numerical conditional mean, such as expected sales at a given price, or a conditional probability, such as the probability of purchase. Choosing the response and predictors gives the model a direction that correlation alone does not have.

## Mean structure and unexplained variation

A linear regression writes the response as a systematic component plus an error. Least squares chooses coefficients that minimize squared residuals in the observed data. The model errors are unobserved deviations from the population mean; residuals are fitted deviations and inherit constraints from the fitting procedure.

With several predictors, each coefficient describes an association conditional on the other included predictors. The interpretation depends on coding, units, interactions, and whether the data contain comparable observations at the predictor combinations being discussed. Multicollinearity can make individual coefficients unstable even when fitted values are reasonably stable.

## Comparing models and predicting outcomes

ANOVA represents group differences with indicator predictors and compares nested mean models through sums of squares. Logistic regression uses a linear predictor for log odds, which keeps fitted probabilities between zero and one. Its coefficients act multiplicatively on odds rather than additively on probability.

Standard errors and hypothesis tests describe uncertainty under a model; residual plots help assess mean and variance assumptions; held-out evaluation assesses prediction on new data. These are related tasks with different targets. Strong training fit does not establish good future prediction, and a statistically precise coefficient does not establish a causal effect. Causal conclusions require a suitable design or assumptions about treatment assignment, confounding, and selection in addition to the regression equation.
