# Multivariate Time Series

Related series can carry predictive information for one another. A demand series may respond to earlier prices, while prices respond to earlier demand. Modeling each series separately ignores those cross-lag relationships. A **multivariate time-series model** writes equations for the variables jointly, allowing each variable to use the included histories of the others.

Joint modeling also distinguishes correlated shocks from delayed feedback. Two variables can move together today because their innovations share a driver, because one responds to the other's past, or because both follow a common long-run relation. These mechanisms have different equations and interpretations.

A VAR represents short-run linear lag dynamics. If the modeled levels contain unit roots, first decide whether their long-run combinations are stationary. Cointegration allows individually nonstationary series to have a stationary spread, and a VECM includes that spread as an error-correction term. Granger tests and impulse responses then ask specific predictive or dynamic questions within the chosen system; they do not supply causal identification on their own.

## Worked calculation: a cointegrating spread

Let $x_t=10$ and suppose the long-run relation is

$$
y_t=1.4x_t+u_t.
$$

If the current deviation is $u_t=0.5$, then

$$
y_t=1.4(10)+0.5=14.5.
$$

The levels can wander while the spread

$$
y_t-1.4x_t=u_t
$$

remains stable. A model using only unrestricted short-run differences would omit this error-correction term unless it were added explicitly. Differencing is an algebraic transformation; it is the omission of the lagged level relation from the model that loses the equilibrium information. A VECM keeps both:

$$
\Delta y_t=\alpha\left(y_{t-1}-1.4x_{t-1}\right)
+\text{short-run terms}+\varepsilon_t.
$$

The current spread of 0.5 is an illustration of the assumed relation, not evidence that a stationary spread exists. Establishing cointegration requires behavior across time and an appropriate model. Given a defined lagged spread, $\alpha$ determines its contribution to the next change. A negative coefficient in the $y$ equation pushes $y$ downward when the defined spread is positive; reversing the spread's sign would reverse that coefficient's interpretation.

![Two levels with a stable cointegrating spread](https://raw.githubusercontent.com/djeada/Statistics-Notes/main/assets/time_series/student/17_multivariate_cointegration.png)

The figure shows two non-stationary levels moving together while their spread remains bounded. Cointegration is about this stable combination, not about the individual levels being stationary.

## Why model several series jointly?

Multivariate time-series methods model several variables jointly so that feedback, shared shocks, cross-predictability, and long-run relationships can be represented within one system. This joint specification uses both within-series histories and cross-series lag information; it also requires checking residual dependence across equations.

## Vector Autoregression

For a $k$-dimensional vector $y_t$, a VAR($p$) model is

$$
y_t=c+A_1y_{t-1}+\cdots+A_py_{t-p}+\varepsilon_t.
$$

Each VAR equation includes the same lagged information set, but its coefficients can differ. With $k$ variables and $p$ consecutive lags, the lag coefficients alone number $k^2p$. A modest increase in either system size or order can therefore use substantial estimation freedom. Include variables and lags that address the forecasting question, then check whether the added cross-history actually improves predictions beyond separate univariate baselines.

![VAR feedback](https://raw.githubusercontent.com/djeada/Statistics-Notes/main/assets/time_series/dynamic_multivariate/04_var_feedback.png)

A lagged cross-effect appears as a coefficient connecting one variable's past value to another variable's next equation. This is distinct from contemporaneous covariance between the innovations. Estimating the equations jointly describes both, but a reduced-form VAR still needs additional assumptions to interpret a contemporaneous innovation as a separately identified economic or physical shock.

Lag order can be compared with AIC, BIC, or HQIC, but residual diagnostics, stability, and forecast performance should also be checked.

## Granger Predictability

Variable $x$ **Granger-predicts** $y$ if adding the past of $x$ improves prediction of $y$ relative to the specified information set without it. In a linear VAR this can be assessed through restrictions on the relevant lag coefficients, alongside forecast performance. The conclusion depends on which other variables and lags are included: a missing common driver can make $x$ appear informative without establishing that intervening on $x$ changes $y$.

![Granger predictability](https://raw.githubusercontent.com/djeada/Statistics-Notes/main/assets/time_series/dynamic_multivariate/05_granger_predictability.png)

The visual compares prediction with and without the additional lagged series. The relevant question is whether including the history of $x$ improves the conditional forecast of $y$ beyond the information already in the model.

Impulse-response functions trace how shocks propagate through a VAR. Their interpretation depends on how the shocks are defined. Reduced-form responses describe the fitted innovation system; structural interpretations need additional identifying assumptions. For example, recursive orthogonalization can make the reported response depend on the ordering of the variables.

![Impulse response](https://raw.githubusercontent.com/djeada/Statistics-Notes/main/assets/time_series/dynamic_multivariate/08_impulse_response.png)

The impulse-response figure connects a one-time identified shock to its model-implied effects across future horizons. Those responses are not uniquely structural until the shock-identification assumptions are specified.

## Nonstationarity and Cointegration

Independent random walks can produce spurious regression in levels. If integrated variables are not cointegrated, a model in differences is often more appropriate. If they are cointegrated, a model containing only short-run differences omits the lagged equilibrium error; a VECM retains it explicitly.

Two or more $I(1)$ variables are cointegrated when a nontrivial linear combination is stationary. A cointegrated VAR can be written as a vector error-correction model (VECM):

$$
\Delta y_t
=\Pi y_{t-1}
+\Gamma_1\Delta y_{t-1}
+\cdots
+\Gamma_{p-1}\Delta y_{t-p+1}
+\varepsilon_t.
$$

When

$$
\Pi=\alpha\beta^\top,
$$

the columns of $\beta$ describe cointegrating relations and $\alpha$ describes how each equation adjusts to deviations from those relations.

![Cointegrating spread](https://raw.githubusercontent.com/djeada/Statistics-Notes/main/assets/time_series/dynamic_multivariate/06_cointegrating_spread.png)

The spread figure shows the stationary combination that is preserved by the VECM rather than discarded through differencing.

![VECM adjustment](https://raw.githubusercontent.com/djeada/Statistics-Notes/main/assets/time_series/dynamic_multivariate/07_vecm_adjustment.png)

The adjustment figure shows how disequilibrium at one time point can feed into later changes. The direction of adjustment depends on both the definition of the spread and the signs of the loading coefficients.

A practical workflow is to inspect transformations and stationarity, decide among a levels VAR, differenced VAR, or VECM, choose a parsimonious lag order, fit and diagnose the system, and evaluate forecasts with rolling or expanding origins.

## Stability, predictive restrictions, and equilibrium adjustment

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
\end{bmatrix}y_{t-1}+\varepsilon_t.
$$

If $y_{t-1}=(10,5)^\top$ and $\varepsilon_t=(0.3,-0.2)^\top$, the conditional mean is

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

and the realized value is $(6.3,0.8)^\top$. Each equation uses lagged information from both variables. With $k$ variables and $p$ lags, the lag-coefficient count grows approximately as $k^2p$, before deterministic terms and covariance parameters are included.

### Stability

Write the VAR in lag-polynomial form:

$$
A(B)y_t=\varepsilon_t,
\qquad
A(B)=I-A_1B-\cdots-A_pB^p.
$$

Stability requires

$$
\det A(z)\ne0
\quad\text{for }|z|\le1.
$$

For VAR(1), repeated prediction involves powers of $A_1$. Eigenvalues inside the unit circle make those powers decay, so the effect of a starting deviation or isolated shock eventually fades. An eigenvalue near the boundary gives slow decay. For higher orders, apply the same idea to the companion form, or equivalently inspect the zeros of the lag-polynomial determinant. Keep the eigenvalue and lag-root conventions distinct.

Do not infer stability from a fitted plot alone. Inspect the model roots or eigenvalues and verify that the stationarity assumption matches the variables being modeled.

### Lag-order selection

Candidate lag orders can be compared with information criteria such as

$$
\mathrm{AIC}=-2\ell+2m,
\qquad
\mathrm{BIC}=-2\ell+m\log n.
$$

Here $\ell$ is the maximized log-likelihood and $m$ is the number of estimated parameters under the software's convention. In a multivariate system that count rises quickly, so AIC can favor substantially larger systems than BIC.

Use information criteria to narrow the candidate set, then inspect residual cross-correlation, stability, parameter plausibility, and forecast performance. The lag range should also reflect the sampling frequency and relevant response horizon.

### Granger predictability

In a bivariate system, a restricted equation might be

$$
y_t=a+\phi y_{t-1}+u_t,
$$

while an unrestricted equation adds a lag of $x$:

$$
y_t=a+\phi y_{t-1}+\gamma x_{t-1}+v_t.
$$

If including lagged $x$ materially improves prediction and the relevant restrictions such as $\gamma=0$ are rejected, the past of $x$ contains incremental predictive information for $y$ within the specified information set.

That conclusion is not automatically causal. Omitted variables, common shocks, feedback, and measurement timing can all create predictive precedence without identifying the effect of an intervention.

### Impulse responses

A stable VAR has a moving-average representation of the form

$$
y_t=\mu+\sum_{h=0}^{\infty}\Psi_h\varepsilon_{t-h}.
$$

A reduced-form response follows a specified innovation through the system's matrix recursion. At horizon 0 the contemporaneous mapping applies; at later horizons, feedback across all equations propagates it. If innovations are correlated, changing one component while fixing the others is a particular statistical experiment, not automatically an isolated structural intervention. Report the shock definition together with the response plot.

Reduced-form innovations can be correlated across equations, so a separate identification scheme is needed before an innovation can be interpreted as a distinct structural shock. Common approaches include recursive orderings, sign restrictions, external instruments, and structural models. Report the identifying assumptions and test sensitivity when they are contestable.

### Spurious regression and cointegration

Persistent levels can produce an apparently strong regression even when their new shocks are independent. In that setting the usual stationary regression interpretation is unreliable. Cointegration asks a more specific question: does a particular linear combination remove the stochastic trends and leave a stationary error? High correlation in levels is not sufficient, and merely observing that two curves move together does not answer the integration question.

If $x_t$ and $y_t$ are both $I(1)$ but

$$
u_t=y_t-\beta x_t
$$

is stationary, the variables are cointegrated. For $x_t=10$ and $y_t=1.4x_t+0.5$, the spread is $0.5$. The levels can move widely while their deviation from the long-run relation remains stable.

If integrated variables are not cointegrated, a VAR in differences may be appropriate. If they are cointegrated, include the lagged cointegrating relation as well as short-run changes; this is the role of the error-correction term in a VECM.

### VECM interpretation

A VECM can be written

$$
\Delta y_t
=\Pi y_{t-1}
+\sum_{j=1}^{p-1}\Gamma_j\Delta y_{t-j}
+\varepsilon_t.
$$

When $\Pi=\alpha\beta^\top$:

- $\beta^\top y_{t-1}$ contains the stationary long-run relations;
- $\alpha$ contains the speed and direction of adjustment;
- $\Gamma_j$ describes short-run lag dynamics.

With a lagged spread of 2, loading coefficients $-0.25$ and $0.40$ contribute $-0.5$ and $0.8$ to the two next-period changes. Those are contributions, not the full changes: short-run lag terms and new shocks also enter. Whether the combined movement reduces the disequilibrium depends on how the spread is defined. Interpret the loading vector together with the cointegrating vector rather than naming a coefficient a “speed of adjustment” in isolation.

### Deterministic terms and transformations

An intercept in the differenced equations, an intercept inside the cointegrating relation, and a deterministic trend imply different long-run behavior. Seasonal deterministic terms can also explain patterns that would otherwise appear as lag dependence. State where these terms enter before estimating cointegration rank or interpreting equilibrium. The algebraic label VECM does not determine those choices.

Treating a deterministic trend as stochastic integration, or omitting a needed deterministic term, can change the model conclusion substantially.

### System workflow

1. Align all series, units, and release dates.
2. Plot levels and relevant transformations.
3. Inspect breaks and missing observations.
4. Assess integration and cointegration.
5. Choose a small candidate lag range.
6. Fit a levels VAR, differenced VAR, or VECM as justified.
7. Check stability and residual cross-dependence.
8. Use Granger tests and impulse responses only with assumptions stated.
9. Backtest joint forecasts using temporal origins.
10. Compare the system against separate univariate baselines.

## Formula reference

| Model / quantity | General formula | Notes / special case |
|---|---|---|
| Vector mean | $\mu_t=E[y_t]$ | $y_t$ is a $k\times1$ vector. |
| Cross-covariance matrix | $\Gamma(h)=\mathrm{Cov}(y_t,y_{t-h})$ | Entries contain own- and cross-lag covariances. |
| VAR($p$) | $y_t=c+A_1y_{t-1}+\cdots+A_py_{t-p}+\varepsilon_t$ | Each equation may use lagged values of every series. |
| VAR lag polynomial | $A(B)=I-A_1B-\cdots-A_pB^p$ | VAR is $A(B)y_t=c+\varepsilon_t$. |
| VAR stability | $\det A(z)\ne0$ for $\lvert z\rvert\le1$ | For VAR(1), all eigenvalues of $A_1$ must have modulus below 1. |
| VAR(1) long-run mean | $\mu=(I-A_1)^{-1}c$ | Requires a stable VAR(1). |
| VMA representation | $y_t=\mu+\sum_{h=0}^{\infty}\Psi_h\varepsilon_{t-h}$ | For VAR(1), $\Psi_h=A_1^h$. |
| Impulse response | $\Psi_h$ | Column $j$ gives the response at horizon $h$ to a specified innovation/shock $j$. |
| Granger restriction | $H_0:A_{1,yx}=\cdots=A_{p,yx}=0$ | Tests whether past $x$ adds predictive information for $y$. |
| Cointegration | $\beta^\top y_t\sim I(0)$ while components of $y_t$ are $I(1)$ | $\beta$ contains long-run equilibrium relations. |
| VECM | $\Delta y_t=\Pi y_{t-1}+\sum_{j=1}^{p-1}\Gamma_j\Delta y_{t-j}+\varepsilon_t$ | Reparameterization of a cointegrated VAR. |
| Cointegration factorization | $\Pi=\alpha\beta^\top$ | $\beta$: long-run relations; $\alpha$: adjustment speeds. |
| Forecast recursion | $\hat y_{t+h\mid t}=c+\sum_{j=1}^{p}A_j\hat y_{t+h-j\mid t}$ | Use observed values when the lag index is at or before $t$. |
