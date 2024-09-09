## Yule-Walker Equations

The **Yule-Walker equations** are a set of linear equations that relate the autocorrelations of an **autoregressive (AR) process** to its parameters. These equations are crucial for estimating the parameters of AR models and for understanding the autocorrelation structure of the process.

### Yule-Walker Equations: Definition

The Yule-Walker equations provide a way to estimate the **parameters of an AR(p) process** by relating them to the **autocorrelations** of the process. The key idea is to derive a system of equations that link the parameters $\phi_1, \phi_2, \dots, \phi_p$ with the autocorrelation function (ACF) at different lags $k$.

For an AR(p) process, the Yule-Walker equations are:

$$
\rho(k) = \phi_1 \rho(k-1) + \phi_2 \rho(k-2) + \dots + \phi_p \rho(k-p) \quad \text{for } k = 1, 2, \dots, p
$$

Where:

- $\rho(k)$ is the autocorrelation at lag $k$.
- $\rho(0) = 1$, since the autocorrelation at lag 0 is always 1.

These equations can be used to estimate the parameters $\phi_1, \phi_2, \dots, \phi_p$ of the AR process from the sample autocorrelations.

---

### Deriving the Yule-Walker Equations

#### Assumptions

1. **Stationarity**: The AR process is assumed to be stationary, meaning the mean and variance of the process do not change over time, and the autocovariance function depends only on the lag, not the time.
2. **White Noise**: The error term $Z_t$ is white noise with zero mean and constant variance $\sigma_Z^2$, meaning $Z_t$ is uncorrelated with past values of the process.

#### Derivation Steps

1. **Multiply the AR(p) model by $X_{t-k}$** for a given lag $k$:

$$
X_t = \phi_1 X_{t-1} + \phi_2 X_{t-2} + \dots + \phi_p X_{t-p} + Z_t
$$

Multiply both sides by $X_{t-k}$ for $k = 1, 2, \dots, p$.

2. **Take the expectation** of both sides: Use the definition of the **autocovariance function** $\gamma(k) = E[X_t X_{t-k}]$, and replace the expectations accordingly. Since the white noise $Z_t$ is uncorrelated with $X_{t-k}$, the expected value of $Z_t X_{t-k}$ is zero for all $k \geq 1$.

3. **Use covariance definitions**: Express the expectations as autocovariances $\gamma(k)$ and normalize by $\gamma(0)$, which is the variance of the process, to convert them into autocorrelations $\rho(k)$.

4. **Formulate the Yule-Walker equations**: You will end up with a system of linear equations that relate the autocorrelations at different lags $\rho(1), \rho(2), \dots, \rho(p)$ to the AR model parameters $\phi_1, \phi_2, \dots, \phi_p$.

---

### Example: Yule-Walker Equations for an AR(2) Process

Consider the AR(2) process:

$$
X_t = 3 X_{t-1} + 2 X_{t-2} + Z_t
$$

Where $Z_t$ is white noise with variance $\sigma_Z^2$.

#### Deriving the Yule-Walker Equations

1. **Multiply by $X_{t-1}$** and take the expectation:

$$
E[X_t X_{t-1}] = 3 E[X_{t-1}^2] + 2 E[X_{t-2} X_{t-1}]
$$

Using $\gamma(1) = E[X_t X_{t-1}]$ and $\gamma(0) = E[X_{t-1}^2]$, we get:

$$
\gamma(1) = 3 \gamma(0) + 2 \gamma(1)
$$

2. **Multiply by $X_{t-2}$** and take the expectation:

$$
E[X_t X_{t-2}] = 3 E[X_{t-1} X_{t-2}] + 2 E[X_{t-2}^2]
$$

Using $\gamma(2) = E[X_t X_{t-2}]$, we get:

$$
\gamma(2) = 3 \gamma(1) + 2 \gamma(0)
$$

3. **Express the autocovariances as autocorrelations**: Normalize by the variance $\gamma(0)$, to convert autocovariances into autocorrelations $\rho(k)$:

$$
\rho(1) = \frac{3}{1 + 2} = \frac{3}{3} = 1, \quad \rho(2) = \frac{3 \cdot 1 + 2}{\gamma(0)}
$$

---

### Solving the Difference Equations for AR(2)

To solve the Yule-Walker equations for the AR(2) process, we assume a solution of the form $\rho(k) = \lambda^k$. Substituting into the equation:

$$
\lambda^2 = 3 \lambda + 2
$$

The characteristic equation is:

$$
\lambda^2 - 3 \lambda - 2 = 0
$$

Solving the quadratic equation:

$$
\lambda = \frac{3 \pm \sqrt{9 + 8}}{2} = \frac{3 \pm \sqrt{17}}{2}
$$

Thus, the roots are:

$$
\lambda_1 = \frac{3 + \sqrt{17}}{2}, \quad \lambda_2 = \frac{3 - \sqrt{17}}{2}
$$

The general solution for the autocorrelation function $\rho(k)$ is:

$$
\rho(k) = c_1 \lambda_1^k + c_2 \lambda_2^k
$$

---

### Finding Coefficients $c_1$ and $c_2$

#### Use $\rho(0) = 1$

At $k = 0$, we know $\rho(0) = 1$. This gives the equation:

$$
c_1 + c_2 = 1
$$

#### Use $\rho(1)$

At $k = 1$, we use the relationship $\rho(1) = 3 \rho(0) + 2 \rho(1)$ to find:

$$
\rho(1) = 3 \cdot 1 + 2 \cdot \rho(1)
$$

Solving this, we get:

$$
\rho(1) = \frac{3}{2}
$$

Substituting into the general solution:

$$
c_1 \lambda_1 + c_2 \lambda_2 = \frac{3}{2}
$$

Solving the system of equations:

$$
\begin{aligned}
c_1 + c_2 &= 1 \\
c_1 \lambda_1 + c_2 \lambda_2 &= \frac{3}{2}
\end{aligned}
$$

This gives the values for $c_1$ and $c_2$, which can then be substituted back into the general solution for $\rho(k)$.

### **7. Matrix Form of Yule-Walker Equations for AR(p)**

For an AR(p) process, the Yule-Walker equations can be written in **matrix form**. Define:

- $\mathbf{r} = \begin{bmatrix} \rho(1) \\ \rho(2) \\ \vdots \\ \rho(p) \end{bmatrix}$ as the vector of autocorrelations.
- $\mathbf{\phi} = \begin{bmatrix} \phi_1 \\ \phi_2 \\ \vdots \\ \phi_p \end{bmatrix}$ as the vector of AR coefficients.

The **autocorrelation matrix** $R$ is a Toeplitz matrix:

$$
R = \begin{bmatrix}
1 & \rho(1) & \rho(2) & \dots & \rho(p-1) \\
\rho(1) & 1 & \rho(1) & \dots & \rho(p-2) \\
\rho(2) & \rho(1) & 1 & \dots & \rho(p-3) \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
\rho(p-1) & \rho(p-2) & \rho(p-3) & \dots & 1
\end{bmatrix}
$$

The Yule-Walker equations are then written as:

$$
R \mathbf{\phi} = \mathbf{r}
$$

To solve for the AR coefficients $\mathbf{\phi}$:

$$
\mathbf{\phi} = R^{-1} \mathbf{r}
$$
