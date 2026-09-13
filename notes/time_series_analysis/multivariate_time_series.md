# Multivariate Time Series

Multivariate time-series methods model several variables jointly. The goal is to represent feedback, shared dynamics, and long-run relationships that cannot be captured by separate univariate models.

## Vector Autoregression

For a $k$-dimensional vector $y_t$, a VAR$(p)$ model is

$$
y_t = c + A_1 y_{t-1}+\cdots+A_p y_{t-p}+\varepsilon_t,
$$

where each $A_i$ is a $k\times k$ coefficient matrix. Every variable can depend on lags of every variable in the system.

A VAR is the multivariate analogue of an autoregression. The number of parameters grows quickly with the number of variables and lags, so parsimony matters.

## Stability and Lag Order

For a standard VAR in levels, stability requires the roots of the associated characteristic polynomial to lie outside the unit circle. In practice, inspect stability diagnostics supplied by the software.

Lag order can be compared with AIC, BIC, or HQIC, but residual diagnostics and forecasting performance should also be checked.

## Granger Predictability

Variable $x$ is said to **Granger-cause** $y$ if past values of $x$ improve prediction of $y$ after accounting for the included past information.

This is a statement about incremental predictive content, not intervention or structural causality. A third variable, common trend, or feedback system can generate Granger predictability without a causal effect in the scientific sense.

## Impulse Responses

An impulse-response function traces how a shock to one innovation propagates through the VAR over future periods. Interpretation depends on how contemporaneous shocks are identified. Orthogonalized impulse responses, for example, depend on variable ordering unless stronger identifying assumptions are supplied.

## Non-Stationary Variables and Spurious Regression

Independent random walks can produce apparently strong regression relationships. Before fitting a VAR in levels, determine whether the variables are stationary, integrated, or cointegrated.

If integrated variables are not cointegrated, modeling differences is often appropriate. If they are cointegrated, differencing alone throws away the long-run equilibrium relationship.

## Cointegration

Two or more $I(1)$ variables are cointegrated if some linear combination is stationary. For two variables,

$$
z_t = y_t - \beta x_t
$$

may be stationary even when $x_t$ and $y_t$ are individually non-stationary. Cointegration represents a stable long-run relationship with short-run deviations.

Common approaches include the Engle-Granger procedure for simple settings and Johansen tests for multivariate systems with potentially multiple cointegrating relationships.

## Vector Error-Correction Model

A cointegrated VAR can be written as a VECM:

$$
\Delta y_t = \Pi y_{t-1} + \Gamma_1\Delta y_{t-1}+\cdots+\Gamma_{p-1}\Delta y_{t-p+1}+\varepsilon_t.
$$

When $\Pi=\alpha\beta^\top$, the columns of $\beta$ describe cointegrating relationships and $\alpha$ describes how variables adjust when the system moves away from long-run equilibrium.

## Workflow

1. Plot all variables and check alignment/frequency.
2. Examine transformations, structural breaks, and stationarity.
3. Decide whether a VAR in levels, VAR in differences, or VECM matches the integration structure.
4. Choose a parsimonious lag order.
5. Fit the model and check residual serial correlation and stability.
6. Use Granger tests, impulse responses, or variance decompositions only with their assumptions clearly stated.
7. Evaluate forecasts with rolling or expanding origins.

The companion script `scripts/time_series_analysis/var_and_cointegration.py` simulates cointegrated series and fits both a VAR on differences and a VECM.
