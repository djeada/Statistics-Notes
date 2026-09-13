# Multivariate Time Series

## Worked calculation: a cointegrating spread

Let $x_t=10$ and suppose the long-run relation is $y_t=1.4x_t+u_t$. If the current deviation is $u_t=0.5$, then

$$
y_t=1.4(10)+0.5=14.5.
$$

The levels can wander while the spread

$$
y_t-1.4x_t=u_t
$$

remains stable. Differencing both series would model short-run changes but would discard this level relationship. A VECM keeps both:

$$
\Delta y_t=\alpha\left(y_{t-1}-1.4x_{t-1}\right)+\text{short-run terms}+\varepsilon_t.
$$

The sign and size of $\alpha$ describe how the system responds after the spread moves away from equilibrium.

![Two levels with a stable cointegrating spread](../../assets/time_series/student/17_multivariate_cointegration.png)

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

## Student guide: model the system before interpreting individual equations

Multivariate analysis is useful when variables can affect one another, share shocks, or move together in the long run. It also creates more opportunities for overfitting and interpretation errors. Begin with the data-generating and forecasting question, then decide whether a joint model adds information beyond separate univariate forecasts.

### VAR(1) mechanics with numbers

Let

$$
y_t=
\begin{bmatrix}
x_t\\
z_t
\end{bmatrix},
\qquad
y_t=
\begin{bmatrix}
0.5&0.2\\
-0.1&0.4
\end{bmatrix}
y_{t-1}+\varepsilon_t.
$$

If $y_{t-1}=(10,5)^\top$ and $\varepsilon_t=(0.3,-0.2)^\top$, then

$$
\hat y_t=
\begin{bmatrix}
0.5(10)+0.2(5)\\
-0.1(10)+0.4(5)
\end{bmatrix}
=
\begin{bmatrix}
6\\
1
\end{bmatrix},
$$

and the realized value is $(6.3,0.8)^\top$. The first equation uses the lag of both variables; the second does as well. With $k$ variables and $p$ lags, the coefficient count grows approximately as $k^2p$, before deterministic terms and covariance parameters.

### Stability

Write the VAR in lag-polynomial form:

$$
A(B)y_t=\varepsilon_t,
\qquad
A(B)=I-A_1B-\cdots-A_pB^p.
$$

Stability requires the determinant of $A(z)$ to be nonzero for $|z|\le1$. For a VAR(1), the eigenvalues of $A_1$ must lie inside the unit circle. If the largest modulus is near 1, shocks decay slowly and forecasts can be highly uncertain.

Do not infer stability from an attractive fitted plot alone. Inspect software stability roots, simulate impulse responses, and check whether the assumed model is appropriate for the transformed variables.

### Lag-order selection

Candidate lag orders can be compared with AIC, BIC, or HQIC:

$$
\operatorname{AIC}=-2\ell+2k,
\qquad
\operatorname{BIC}=-2\ell+k\log n.
$$

In a multivariate model, $k$ rises quickly. AIC may prefer a larger system than BIC. Use these criteria to narrow candidates, then inspect residual cross-correlation, stability, forecast performance, and parameter plausibility.

The lag order should also respect the sampling frequency and the response horizon. Monthly data may need lags 12 or 24 for seasonal dynamics, but adding every seasonal lag can consume degrees of freedom.

### Granger predictability

In a bivariate system, $x$ is said to Granger-predict $y$ if lagged $x$ terms improve the conditional forecast of $y$ after including the relevant lagged $y$ terms and other variables in the information set.

A restricted equation might be

$$
y_t=a+\phi y_{t-1}+u_t,
$$

while an unrestricted equation is

$$
y_t=a+\phi y_{t-1}+\gamma x_{t-1}+v_t.
$$

If the unrestricted forecast error variance is materially lower and the joint restrictions $\gamma=0$ are rejected, the past of $x$ contains incremental predictive information. This does not show that an intervention on $x$ would change $y$. Omitted variables, feedback, measurement timing, and common shocks can all create predictive precedence.

### Impulse responses

The moving-average representation

$$
y_t=\mu+\sum_{h=0}^{\infty}\Psi_h\varepsilon_{t-h}
$$

maps innovations into future outcomes. An impulse-response plot shows a column of $\Psi_h$ across horizons. The response at horizon 0 is a contemporaneous effect; later responses combine feedback through the whole system.

Reduced-form innovations can be correlated across equations. To interpret an impulse as a distinct shock, an identification scheme is required, such as:

- a recursive ordering;
- sign restrictions;
- external instruments;
- a structural economic model.

Orthogonalized impulse responses depend on variable ordering. Always state the identification assumptions and show sensitivity when they are contestable.

### Spurious regression and cointegration

Two independent random walks can both display persistent trends. Regressing one on the other may produce a high $R^2$ and apparently significant slope even when the innovations are independent. Check integration order before fitting levels relationships.

If $x_t$ and $y_t$ are both $I(1)$ but

$$
u_t=y_t-\beta x_t
$$

is stationary, they are cointegrated. For example, if $x_t=10$ and $y_t=1.4x_t+0.5$, the spread is $0.5$. The levels can wander while their deviation from the long-run relation remains bounded.

If non-stationary series are not cointegrated, a VAR in differences may be appropriate. If they are cointegrated, differencing alone loses the equilibrium term.

### VECM interpretation

A VECM can be written

$$
\Delta y_t
=\Pi y_{t-1}
\sum_{j=1}^{p-1}\Gamma_j\Delta y_{t-j}
\varepsilon_t.
$$

When $\Pi=\alpha\beta^\top$:

- $\beta^\top y_{t-1}$ contains the stationary long-run relations;
- $\alpha$ contains the speed and direction of adjustment;
- $\Gamma_j$ describes short-run lag dynamics.

For a spread of $2$, if $\alpha_x=-0.25$ and $\alpha_y=0.40$, the error-correction contributions are $\Delta x=-0.5$ and $\Delta y=0.8$ before the other terms and new shocks are included. The signs must be interpreted together with the definition of the spread.

### Deterministic terms and transformations

Decide whether the system includes:

- an intercept in the levels;
- a trend;
- seasonal deterministic terms;
- an intercept inside or outside the cointegrating relation.

These choices affect rank tests and the estimated long-run relationship. Treating a deterministic trend as stochastic integration, or omitting a needed trend, can change the conclusion.

### System workflow

1. Align all series, units, and release dates.
2. Plot levels and transformations.
3. Inspect breaks and missing observations.
4. Assess integration and cointegration.
5. Choose a small candidate lag range.
6. Fit levels VAR, differenced VAR, or VECM as justified.
7. Check stability and residual cross-dependence.
8. Use Granger tests and impulse responses only with assumptions stated.
9. Backtest joint forecasts using temporal origins.
10. Compare the system against separate univariate baselines.

### Visual companions

Run [dynamic_multivariate_visualizations.py](../../scripts/time_series/dynamic_multivariate_visualizations.py):

![VAR feedback](../../assets/time_series/dynamic_multivariate/04_var_feedback.png)

![Granger predictability](../../assets/time_series/dynamic_multivariate/05_granger_predictability.png)

![Cointegrating spread](../../assets/time_series/dynamic_multivariate/06_cointegrating_spread.png)

![VECM adjustment](../../assets/time_series/dynamic_multivariate/07_vecm_adjustment.png)

![Impulse response](../../assets/time_series/dynamic_multivariate/08_impulse_response.png)

The companion script [`var_and_cointegration.py`](../../scripts/time_series/var_and_cointegration.py) simulates cointegrated series and fits both a VAR on differences and a VECM.
