# Multivariate Time Series

Multivariate time-series methods model several variables jointly to represent feedback, shared dynamics, and long-run relationships.

## Vector Autoregression

For a $k$-dimensional vector $y_t$, a VAR$(p)$ model is

$$
y_t=c+A_1y_{t-1}+\cdots+A_py_{t-p}+\varepsilon_t.
$$

Every variable can depend on lags of every variable. Parameter counts therefore grow quickly, so parsimony matters. Lag order can be compared with AIC, BIC, or HQIC, but residual diagnostics and forecasting performance should also be checked.

## Granger Predictability

Variable $x$ **Granger-causes** $y$ when past values of $x$ improve prediction of $y$ after accounting for the included past information. This is a statement about incremental predictive content, not intervention or structural causality.

Impulse-response functions trace how shocks propagate through a VAR. Their interpretation depends on how contemporaneous shocks are identified; orthogonalized responses can depend on variable ordering.

## Nonstationarity and Cointegration

Independent random walks can produce spurious regression. If integrated variables are not cointegrated, modeling differences is often appropriate. If they are cointegrated, differencing alone discards the long-run relationship.

Two or more $I(1)$ variables are cointegrated when a linear combination is stationary. A cointegrated VAR can be written as a VECM:

$$
\Delta y_t=\Pi y_{t-1}+\Gamma_1\Delta y_{t-1}+\cdots+\Gamma_{p-1}\Delta y_{t-p+1}+\varepsilon_t.
$$

When $\Pi=\alpha\beta^\top$, the columns of $\beta$ describe cointegrating relationships and $\alpha$ describes adjustment back toward long-run equilibrium.

A practical workflow is: inspect transformations and stationarity, decide among levels/differences/VECM, choose a parsimonious lag order, fit and diagnose, then evaluate forecasts with rolling or expanding origins.

The companion script [`var_and_cointegration.py`](../../scripts/time_series/var_and_cointegration.py) simulates cointegrated series and fits both a VAR on differences and a VECM.
