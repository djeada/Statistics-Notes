## Yule-Walker Equations

The **Yule-Walker equations** are a set of linear relationships that tie the **autocovariances/autocorrelations** of a *stationary* **autoregressive (AR $p$) process** to its parameters. They are the work-horse for parameter estimation, diagnostic checking, and theoretical analysis of AR models.

### Definition

First recall the *AR $p$* model itself

$$
\boxed{%
X_t = \phi_1 X_{t-1} + \phi_2 X_{t-2} + \dots + \phi_p X_{t-p} + Z_t,
\qquad 
Z_t \stackrel{\text{i.i.d.}}{\sim} \text{WN}\bigl(0,\sigma_Z^{2}\bigr)}
$$

where $Z_t$ is white noise.
Define the autocovariance function (ACVF) and autocorrelation function (ACF) by

$$
\gamma(k)=\mathrm{Cov}(X_t,X_{t-k}),\quad
\rho(k)=\frac{\gamma(k)}{\gamma(0)},\quad
k\in\mathbb{Z}
$$

**Yule-Walker system (covariance form, including variance equation)**

$$
\boxed{%
\gamma(k)=\sum_{j=1}^{p}\phi_j \gamma(k-j)}, 
\qquad k=1,2,\dots ,p
$$

$$
\boxed{%
\gamma(0)=\sum_{j=1}^{p}\phi_j \gamma(j)+\sigma_Z^{2}} \tag{\(*\)}
$$

Dividing every equation (except $*$) by $\gamma(0)$ converts them to *autocorrelation form*—the version most frequently quoted:

$$
\boxed{%
\rho(k)=\sum_{j=1}^{p}\phi_j \rho(k-j)},
\qquad k=1,2,\dots ,p.
$$

Because $\rho(0)=1$, each equation involves only *observable* autocorrelations on the left and right sides.

### Deriving the Yule-Walker Equations

#### Assumptions

1. **Second-order stationarity** – mean and variance are constant; $\gamma(k)$ depends only on $k$.
2. **White-noise innovations** – $E[Z_t]=0,\quad \mathrm{Var}(Z_t)=\sigma_Z^2.$, and $Z_t$ is uncorrelated with $\{X_{t-k}\}_{k\ge1}$.

#### Derivation Steps

I. **Multiply by a lagged value.**

For a fixed $k\in\{1dots ,p\}$,

$$X_tX_{t-k}= \sum_{j=1}^{p} \phi_j,X_{t-j}X_{t-k}+Z_tX_{t-k}$$

II. **Take expectations.**

Using stationarity,

$$
E[X_t X_{t-k}]
= \sum_{j=1}^p \phi_j\,E[X_{t-j} X_{t-k}] + E[Z_t X_{t-k}]
$$

Because $Z_t$ is uncorrelated with past $X$’s, the final expectation vanishes for $k\ge1$.

III. **Replace expectations with autocovariances.**

$$\gamma(k)=\sum_{j=1}^{p}\phi_j,\gamma(k-j), 
\qquad k=1dots ,p$$

For $k=0$ the expectation $E[Z_tX_t]=\sigma_Z^{2}$ is non-zero, flexible equation $*$ above.

IV. **Normalize to autocorrelations.**

Divide by $\gamma(0)$ (the variance) whenever $\gamma(0)\neq0$ to obtain the autocorrelation version.

Matrix view (same equations in compact form):

Let

$$r = 
\begin{pmatrix}
\rho(1)\\
\rho(2)\\
\vdots\\
\rho(p)
\end{pmatrix}$$

known from the data.

Let

$$
R 
= \bigl[\rho(|i-j|)\bigr]_{i,j=1}^p
= \begin{pmatrix}
\rho(0)&\rho(1)&\cdots&\rho(p-1)\\
\rho(1)&\rho(0)&\cdots&\rho(p-2)\\
\vdots&\vdots&\vdots&\vdots\\
\rho(p-1)&\rho(p-2)&\cdots&\rho(0)
\end{pmatrix}$$

the Toeplitz matrix.

Finally, let

$$\phi = 
\begin{pmatrix}
\phi_1\\
\phi_2\\
\vdots\\
\phi_p
\end{pmatrix}$$

Then the Yule–Walker equations read

$$R,\phi = r$$

Solving this Toeplitz system (e.g. by Levinson–Durbin recursion) delivers the **Yule-Walker estimates** 

$$\hat{\phi}_j$$ 

and 

$$
\hat\sigma_Z^2 = \gamma(0) - \sum_{j=1}^p \hat\phi_j \gamma(j)
$$

### Example: Yule-Walker Equations for an AR(2) Process

We want to illustrate how the Yule-Walker equations connect an AR(2) model’s parameters to its (theoretical) autocovariance and autocorrelation functions.  Concretely, we will

1. **Check stationarity** of the given coefficient pair \$(\phi\_1,\phi\_2)\$ by inspecting the roots of \$1-\phi\_1z-\phi\_2z^2=0\$.
2. **Derive the first two Yule-Walker equations** and solve for \$\gamma(1)\$ and \$\gamma(2)\$.
3. **Convert to autocorrelations** \$\rho(1)\$ and \$\rho(2)\$ and comment on whether the results are admissible.
4. **Solve the homogeneous recurrence** \$\rho(k)=\phi\_1\rho(k-1)+\phi\_2\rho(k-2)\$ to obtain the closed-form \$\rho(k)\$.
5. **Contrast a non-stationary versus a stationary parameter set** so the difference is visible at a glance.

Input data — numbers we will plug in:

| Symbol            | Description             | Non-stationary run                                                         | Stationary check |
| ----------------- | ----------------------- | -------------------------------------------------------------------------- | ---------------- |
| \$\phi\_1\$       | AR coefficient on lag 1 | \$3\$                                                                      | \$0.3\$          |
| \$\phi\_2\$       | AR coefficient on lag 2 | \$2\$                                                                      | \$0.2\$          |
| \$\sigma\_Z^{2}\$ | Innovation variance     | kept symbolic (you can set \$\sigma\_Z^{2}=1\$ without loss of generality) | same             |

*Everything beyond this point uses these inputs unless stated otherwise.*

> **Warning on stationarity.**
> For an AR(2) model the coefficients must satisfy $1-\phi_1 z-\phi_2 z^{2}=0$ having both roots $|z|>1$ to be *stationary*.
> With $\phi_1=3,\phi_2=2$ **one root lies inside the unit circle**, so the model is *non-stationary* and its theoretical autocorrelation function (ACF) does not exist in the usual sense.
> We nevertheless go through the algebra to illustrate the mechanics of the Yule-Walker equations; the arithmetic is still correct even though the result is not a valid ACF.

#### Write down the model

$$
\boxed{%
X_t = 3X_{t-1} + 2X_{t-2} + Z_t}, 
\qquad 
Z_t\stackrel{\text{i.i.d.}}{\sim}\text{WN}\bigl(0,\sigma_Z^{2}\bigr).
$$

#### Derive the Yule-Walker equations

**(k = 1)**

$$
\boxed{%
\gamma(1)=3\gamma(0)+2\gamma(1)}
\quad\Longrightarrow\quad
(1-2)\gamma(1)=3\gamma(0)
\quad\Longrightarrow\quad
\boxed{\gamma(1)=-3\gamma(0)}.
$$

**(k = 2)**

$$
\boxed{%
\gamma(2)=3\gamma(1)+2\gamma(0)}
\quad\Longrightarrow\quad
\gamma(2)=3(-3\gamma(0))+2\gamma(0)
= -9\gamma(0)+2\gamma(0)
= \boxed{-7\gamma(0)}.
$$

#### Convert to autocorrelations

$$
\boxed{\rho(1)=\dfrac{\gamma(1)}{\gamma(0)}=-3},
\qquad
\boxed{\rho(2)=\dfrac{\gamma(2)}{\gamma(0)}=-7}.
$$

Because $|\rho(1)|>1$ (and similarly for $\rho(2)$), this confirms the earlier warning: the parameter pair $(3,2)$ produces a non-stationary AR(2) and hence impossible ACF values.

#### Solve the homogeneous difference equation

The Yule-Walker recursion for an AR(2) can be written as

$$
\boxed{\rho(k)=3\rho(k-1)+2\rho(k-2)}, \qquad k\ge2.
$$

Assume a solution $\rho(k)=\lambda^{k}$. Substituting gives

$$
\lambda^{2}=3\lambda+2
\quad\Longrightarrow\quad
\boxed{\lambda^{2}-3\lambda-2=0}.
$$

Solving the quadratic,

$$
\boxed{\lambda_{1,2}= \dfrac{3\pm\sqrt{17}}{2}}
\quad\bigl(\lambda_{1}\approx3.5616,\lambda_{2}\approx-0.5616\bigr).
$$

Hence the general form is

$$
\boxed{\rho(k)=c_{1}\lambda_{1}^{k}+c_{2}\lambda_{2}^{k}}.
$$

#### Determine $c_{1}$ and $c_{2}$

Using $\rho(0)=1$:

$$
\boxed{c_{1}+c_{2}=1}.
$$

Using the previously derived $\rho(1)=-3$:

$$
\boxed{c_{1}\lambda_{1}+c_{2}\lambda_{2}=-3}.
$$

Solving the two-equation system gives

$$
\boxed{%
c_{1}= \frac{-3-\lambda_{2}}{\lambda_{1}-\lambda_{2}},
\qquad
c_{2}=1-c_{1}
}.
$$

(Substituting numerical values, $c_{1}\approx-0.592,c_{2}\approx1.592$.)

Although these constants satisfy the recursion, the resulting $\rho(k)$ diverges because $|\lambda_{1}|>1$; again, the process is not stationary.

#### Quick check: a stationary alternative

For comparison, if we instead chose $\phi_1=0.3,\phi_2=0.2$ (both roots outside the unit circle), the same steps would yield

$$
\rho(1)=\frac{0.3}{1-0.2}=0.375,
\qquad
\rho(2)=0.3\rho(1)+0.2=0.3125,
$$

and the characteristic roots would both have magnitude $<1$, giving a decaying, admissible ACF.

#### Matrix form 

Vector of autocorrelations

$$
\mathbf{r}=
\begin{bmatrix}
\rho(1)\\\rho(2)\\\vdots\\\rho(p)
\end{bmatrix}, 
\qquad
\text{Toeplitz matrix }
R=
\begin{bmatrix}
1 & \rho(1) & \rho(2) & \dots & \rho(p-1)\\
\rho(1) & 1 & \rho(1) & \dots & \rho(p-2)\\
\vdots & \vdots & \vdots & \ddots & \vdots\\
\rho(p-1) & \rho(p-2) & \rho(p-3) & \dots & 1
\end{bmatrix}.
$$

$$
\boxed{R\boldsymbol{\phi}= \mathbf{r}},
\qquad
\boxed{\boldsymbol{\phi}=R^{-1}\mathbf{r}}.
$$
