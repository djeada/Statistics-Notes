# Yule-Walker Equations

The Yule-Walker equations connect an autoregressive model's coefficients to its autocovariances and autocorrelations. They translate a recursion written in terms of lagged observations into a set of moment relationships that can be studied theoretically or estimated from data.

For a stationary AR process, this link works in both directions: known coefficients determine the ACF recursion, while estimated autocovariances can be used to solve for the coefficients. The equations are therefore useful for understanding AR dependence, estimating parameters, and checking whether an implied correlation pattern is compatible with stationarity.

## Formula reference

| Quantity / case | General formula | Notes / special case |
|---|---|---|
| AR($p$) | $X_t-\mu=\sum_{j=1}^{p}\phi_j(X_{t-j}-\mu)+\varepsilon_t$ | Yule-Walker applies to a stationary AR process. |
| Covariance recursion | $\gamma(k)=\sum_{j=1}^{p}\phi_j\gamma(k-j)$ | For $k\ge1$, using $\gamma(-h)=\gamma(h)$. |
| Correlation recursion | $\rho(k)=\sum_{j=1}^{p}\phi_j\rho(k-j)$ | Divide the covariance equations by $\gamma(0)$. |
| Zero-lag equation | $\gamma(0)=\sum_{j=1}^{p}\phi_j\gamma(j)+\sigma_\varepsilon^2$ | Determines innovation variance once the AR coefficients are known. |
| Matrix form | $\Gamma_p\boldsymbol\phi=\boldsymbol\gamma_p$ | $\Gamma_p$ is the Toeplitz matrix with entries $\gamma(\lvert i-j\rvert)$. |
| Correlation matrix form | $R_p\boldsymbol\phi=\mathbf r_p$ | $R_{ij}=\rho(\lvert i-j\rvert)$ and $\mathbf r_p=(\rho_1,\ldots,\rho_p)^\top$. |
| Yule-Walker estimate | $\hat{\boldsymbol\phi}=\hat\Gamma_p^{-1}\hat{\boldsymbol\gamma}_p$ | In practice solve the Toeplitz system rather than explicitly inverting. |
| Innovation variance | $\hat\sigma_\varepsilon^2=\hat\gamma(0)-\sum_{j=1}^{p}\hat\phi_j\hat\gamma(j)$ | Equivalent to $\hat\gamma(0)(1-\hat{\boldsymbol\phi}^{\top}\hat{\mathbf r}_p)$. |
| AR(1) | $\rho(k)=\phi^{\lvert k\rvert}$ | Hence $\phi=\rho(1)$ and $\sigma_\varepsilon^2=\gamma(0)(1-\phi^2)$. |
| AR(2), lag 1 | $\rho_1=\phi_1+\phi_2\rho_1$ | Thus $\rho_1=\phi_1/(1-\phi_2)$. |
| AR(2), later lags | $\rho_k=\phi_1\rho_{k-1}+\phi_2\rho_{k-2}$ | Produces geometric or damped-oscillatory decay for a stable model. |

## Worked calculation: AR(2) autocorrelations

For an AR(2) with $\phi_1=0.6$ and $\phi_2=-0.2$, the first two Yule-Walker equations give

$$
\rho_1=\phi_1+\phi_2\rho_1
\quad\Longrightarrow\quad
\rho_1=\frac{0.6}{1-(-0.2)}=0.5,
$$

and

$$
\rho_2=\phi_1\rho_1+\phi_2
=0.6(0.5)-0.2=0.1.
$$

For later lags, use the recursion

$$
\rho_h=0.6\rho_{h-1}-0.2\rho_{h-2}.
$$

For example, $\rho_3=0.6(0.1)-0.2(0.5)=-0.04$. The equations turn AR coefficients into restrictions on the autocorrelation pattern that can be compared with a sample ACF.

![Yule-Walker recursion for an AR(2)](https://raw.githubusercontent.com/djeada/Statistics-Notes/refs/heads/main/assets/time_series/student/09_yule_walker_ar2.png)

The **Yule-Walker equations** are linear relationships connecting the autocovariances or autocorrelations of a stationary autoregressive process to its AR coefficients. They provide a direct link between a model written in terms of lagged values and the second-order dependence visible in its ACF.

### Definition

Consider a zero-mean stationary AR($p$) process

$$
X_t=\phi_1X_{t-1}+\phi_2X_{t-2}+\dots+\phi_pX_{t-p}+Z_t,
$$

where $Z_t$ is white noise with

$$
E(Z_t)=0,
\qquad
\mathrm{Var}(Z_t)=\sigma_Z^2,
$$

and is uncorrelated with past values of the process.

Define the autocovariance function (ACVF) and autocorrelation function (ACF) by

$$
\gamma(k)=\mathrm{Cov}(X_t,X_{t-k}),
\qquad
\rho(k)=\frac{\gamma(k)}{\gamma(0)},
\qquad
k\in\mathbb Z.
$$

The covariance form of the Yule-Walker equations is

$$
\gamma(k)=\sum_{j=1}^{p}\phi_j\gamma(k-j),
\qquad k=1,2,\dots,p,
$$

with the variance equation

$$
\gamma(0)=\sum_{j=1}^{p}\phi_j\gamma(j)+\sigma_Z^2.
$$

Dividing the first set of equations by $\gamma(0)$ gives the autocorrelation form

$$
\rho(k)=\sum_{j=1}^{p}\phi_j\rho(k-j),
\qquad k=1,2,\dots,p.
$$

Because $\rho(0)=1$, these equations relate the AR coefficients directly to the autocorrelation sequence. In estimation, the theoretical autocorrelations are replaced by sample estimates.

### Deriving the Yule-Walker Equations

#### Assumptions

The derivation uses two main conditions:

1. **Second-order stationarity:** the mean and variance are constant, and $\gamma(k)$ depends only on the lag $k$.
2. **White-noise innovations:** $E(Z_t)=0$, $\mathrm{Var}(Z_t)=\sigma_Z^2$, and $Z_t$ is uncorrelated with $X_{t-k}$ for $k\ge1$.

#### Derivation Steps

For a fixed $k\in\{1,2,\ldots,p\}$, multiply the AR equation by $X_{t-k}$:

$$
X_tX_{t-k}
=\sum_{j=1}^{p}\phi_jX_{t-j}X_{t-k}+Z_tX_{t-k}.
$$

Taking expectations gives

$$
E(X_tX_{t-k})
=\sum_{j=1}^{p}\phi_jE(X_{t-j}X_{t-k})+E(Z_tX_{t-k}).
$$

For the zero-mean process used here, these expectations are covariances. Because the innovation is uncorrelated with past values, the final term is zero for $k\ge1$. Therefore,

$$
\gamma(k)=\sum_{j=1}^{p}\phi_j\gamma(k-j),
\qquad k=1,2,\ldots,p.
$$

At $k=0$, the innovation appears inside $X_t$, so $E(Z_tX_t)=\sigma_Z^2$. This gives

$$
\gamma(0)=\sum_{j=1}^{p}\phi_j\gamma(j)+\sigma_Z^2.
$$

Finally, dividing the lag equations by $\gamma(0)$ produces the autocorrelation form.

The same equations can be written compactly in matrix form. Let

$$
r=
\begin{pmatrix}
\rho(1)\\
\rho(2)\\
\vdots\\
\rho(p)
\end{pmatrix},
$$

and define the Toeplitz matrix

$$
R=
\bigl[\rho(|i-j|)\bigr]_{i,j=1}^{p}
=
\begin{pmatrix}
\rho(0)&\rho(1)&\cdots&\rho(p-1)\\
\rho(1)&\rho(0)&\cdots&\rho(p-2)\\
\vdots&\vdots&\ddots&\vdots\\
\rho(p-1)&\rho(p-2)&\cdots&\rho(0)
\end{pmatrix}.
$$

With

$$
\phi=
\begin{pmatrix}
\phi_1\\
\phi_2\\
\vdots\\
\phi_p
\end{pmatrix},
$$

the Yule-Walker system is

$$
R\phi=r.
$$

Replacing the theoretical autocorrelations by sample estimates and solving this system gives the Yule-Walker coefficient estimates. The innovation variance can then be estimated from

$$
\hat\sigma_Z^2
=\hat\gamma(0)-\sum_{j=1}^{p}\hat\phi_j\hat\gamma(j).
$$

### Example: Yule-Walker Equations for an AR(2) Process

This example deliberately contrasts an invalid non-stationary coefficient pair with a stationary alternative. The purpose is to show both how the equations are applied and why their results must still satisfy the basic constraints of an autocorrelation function.

The two parameter sets are:

| Symbol | Description | Non-stationary run | Stationary check |
|---|---|---:|---:|
| $\phi_1$ | AR coefficient on lag 1 | $3$ | $0.3$ |
| $\phi_2$ | AR coefficient on lag 2 | $2$ | $0.2$ |
| $\sigma_Z^2$ | Innovation variance | kept symbolic | same |

For a stationary AR(2), the roots of the AR polynomial

$$
1-\phi_1z-\phi_2z^2=0
$$

must lie outside the unit circle. With $\phi_1=3$ and $\phi_2=2$, one root lies inside the unit circle, so the model is not stationary and a valid stationary ACF does not exist. The algebra below is still useful because it shows how the failure appears in the implied correlations.

#### Write down the model

For the non-stationary parameter set,

$$
X_t=3X_{t-1}+2X_{t-2}+Z_t,
$$

where $Z_t$ is white noise with variance $\sigma_Z^2$.

#### Derive the Yule-Walker equations

At lag 1,

$$
\gamma(1)=3\gamma(0)+2\gamma(1),
$$

so

$$
(1-2)\gamma(1)=3\gamma(0)
\quad\Longrightarrow\quad
\gamma(1)=-3\gamma(0).
$$

At lag 2,

$$
\gamma(2)=3\gamma(1)+2\gamma(0),
$$

which gives

$$
\gamma(2)=3[-3\gamma(0)]+2\gamma(0)=-7\gamma(0).
$$

#### Convert to autocorrelations

Dividing by $\gamma(0)$ gives

$$
\rho(1)=-3,
\qquad
\rho(2)=-7.
$$

An autocorrelation must lie between $-1$ and $1$, so these values are impossible for a stationary covariance process. The contradiction is another indication that the coefficient pair $(3,2)$ does not define a stationary AR(2).

#### Solve the homogeneous difference equation

The corresponding AR(2) recursion is

$$
\rho(k)=3\rho(k-1)+2\rho(k-2),
\qquad k\ge2.
$$

Trying $\rho(k)=\lambda^k$ gives

$$
\lambda^2-3\lambda-2=0,
$$

with roots

$$
\lambda_{1,2}=\frac{3\pm\sqrt{17}}{2},
$$

or approximately $3.5616$ and $-0.5616$. Hence

$$
\rho(k)=c_1\lambda_1^k+c_2\lambda_2^k.
$$

#### Determine $c_1$ and $c_2$

Using $\rho(0)=1$ and the algebraic value $\rho(1)=-3$ gives

$$
c_1+c_2=1
$$

and

$$
c_1\lambda_1+c_2\lambda_2=-3.
$$

Therefore,

$$
c_1=\frac{-3-\lambda_2}{\lambda_1-\lambda_2},
\qquad
c_2=1-c_1.
$$

Numerically, $c_1\approx-0.592$ and $c_2\approx1.592$. These constants satisfy the formal recursion, but the term involving $|\lambda_1|>1$ grows rather than decays, so the sequence cannot be a stationary ACF.

#### Quick check: a stationary alternative

Now take $\phi_1=0.3$ and $\phi_2=0.2$. The Yule-Walker equations give

$$
\rho(1)=\frac{0.3}{1-0.2}=0.375,
$$

and

$$
\rho(2)=0.3\rho(1)+0.2=0.3125.
$$

For this parameter set, the roots of the AR polynomial in $z$ lie outside the unit circle. Equivalently, the roots governing the homogeneous recursion in powers of $\lambda$ lie inside the unit circle, so the autocorrelation sequence decays rather than diverges.

#### Matrix form

For a general AR($p$), collect the autocorrelations into

$$
\mathbf r=
\begin{bmatrix}
\rho(1)\\
\rho(2)\\
\vdots\\
\rho(p)
\end{bmatrix}
$$

and form

$$
R=
\begin{bmatrix}
1&\rho(1)&\rho(2)&\dots&\rho(p-1)\\
\rho(1)&1&\rho(1)&\dots&\rho(p-2)\\
\vdots&\vdots&\ddots&\ddots&\vdots\\
\rho(p-1)&\rho(p-2)&\dots&\rho(1)&1
\end{bmatrix}.
$$

Then

$$
R\boldsymbol\phi=\mathbf r.
$$

When $R$ is nonsingular,

$$
\boldsymbol\phi=R^{-1}\mathbf r.
$$

In practice, numerical solvers exploit the Toeplitz structure rather than forming the inverse explicitly.

## Student guide: solve the equations and check the result

For a zero-mean stationary AR($p$), the autocovariances satisfy the AR recursion at sufficiently large lags:

$$
\gamma(k)=\phi_1\gamma(k-1)+\cdots+\phi_p\gamma(k-p).
$$

The first $p$ lags supply the boundary equations needed to determine the coefficients. Dividing by $\gamma(0)$ gives the corresponding relations for autocorrelations.

### AR(2) by hand

For $\phi_1=0.6$ and $\phi_2=-0.2$,

$$
\rho_1=\phi_1+\phi_2\rho_1,
$$

so

$$
\rho_1=\frac{0.6}{1.2}=0.5.
$$

The next equation is

$$
\rho_2=\phi_1\rho_1+\phi_2
=0.6(0.5)-0.2=0.1.
$$

At lag 3,

$$
\rho_3=0.6(0.1)-0.2(0.5)=-0.04.
$$

The recursion then continues. A sample ACF will not equal these population values exactly, but its pattern should be broadly compatible with the fitted AR coefficients.

![Yule-Walker recursion](https://raw.githubusercontent.com/djeada/Statistics-Notes/refs/heads/main/assets/time_series/dependence/07_yule_walker_recursion.png)

The figure shows how each new autocorrelation is generated from earlier lags. For a stable AR model, the recursion produces a sequence that decays rather than growing without bound.

### Matrix form

For AR(2), define

$$
R=
\begin{bmatrix}
1&\rho_1\\
\rho_1&1
\end{bmatrix},
\qquad
r=
\begin{bmatrix}
\rho_1\\
\rho_2
\end{bmatrix}.
$$

Then the coefficient vector solves

$$
R
\begin{bmatrix}
\phi_1\\
\phi_2
\end{bmatrix}
=
\begin{bmatrix}
\rho_1\\
\rho_2
\end{bmatrix}.
$$

When estimated autocorrelations replace the population values, the solution is affected by sampling noise. At high orders, the Toeplitz matrix can also become poorly conditioned, which makes the coefficient estimates unstable.

### Innovation variance

After estimating $\boldsymbol\phi$, the innovation variance follows from the zero-lag equation:

$$
\sigma_\varepsilon^2
=\gamma(0)\left(1-\sum_{j=1}^{p}\phi_j\rho_j\right).
$$

For an AR(1) with $\phi=0.7$ and $\gamma(0)=1/(1-0.7^2)=1.9608$,

$$
\sigma_\varepsilon^2
=1.9608(1-0.7^2)=1.
$$

This recovers the innovation variance used to define the process and provides a useful check on the moment calculations.

### When not to use Yule-Walker blindly

Yule-Walker equations assume a stationary AR structure. They are not, by themselves, a solution for an untransformed random walk, an MA model with latent shocks, a strongly trending series, a process with time-varying coefficients, or a series dominated by a structural break.

Use the equations as a transparent estimator or theoretical relationship, then check stationarity, compare with other estimation methods when appropriate, and examine residual diagnostics before accepting the model.