## Yule-Walker Equations for Autoregressive Processes

The Yule-Walker equations are a set of linear equations that relate the autocorrelations of an autoregressive (AR) process to its parameters. These equations are crucial for estimating the autocorrelation function (ACF) of AR processes and solving for model parameters.

### 2. **Assumptions and Procedure**

#### 2.1 **Assumptions**

1. **Stationarity**: The AR process is assumed to be stationary. This implies that the statistical properties, including mean and variance, are time-invariant.

2. **White Noise**: The error term \( Z_t \) is assumed to be white noise with mean zero and variance \( \sigma_Z^2 \). This means \( Z_t \) is uncorrelated with any past values.

#### 2.2 **Procedure**

1. **Multiply the AR Model by \( X_{t-k} \)**: To derive the Yule-Walker equations, multiply the AR model by \( X_{t-k} \), where \( k \) is the lag.

2. **Take Expectation**: Compute the expected value of both sides of the equation.

3. **Use Covariance Definition**: Replace the expectations with autocovariances and normalize by the variance \( \gamma_0 = \sigma_X^2 \).

4. **Formulate Difference Equations**: The result will be a set of difference equations relating the autocorrelations \( \rho(k) \) at various lags.

5. **Solve for ACF**: Solve the difference equations to determine the ACF of the process.

### 3. **Example: AR(2) Process**

Consider the AR(2) process defined by:
\[ X_t = \frac{3}{1} X_{t-1} + \frac{2}{1} X_{t-2} + Z_t \]
where \( Z_t \) is white noise with mean zero and variance \( \sigma_Z^2 \).

#### 3.1 **Characteristic Polynomial**

The characteristic polynomial of the AR(2) process is:
\[ \phi(B) = 1 - \frac{3}{1}B - \frac{2}{1}B^2 \]

#### 3.2 **Roots of the Characteristic Polynomial**

To determine stationarity, solve for the roots of:
\[ \phi(B) = 1 - 3B - 2B^2 \]

The roots of the polynomial are:
\[ \lambda = \frac{-2 \pm \sqrt{76}}{2} \]

Both roots have magnitudes greater than 1, indicating that the process is stationary.

### 4. **Yule-Walker Equations for AR(2)**

To find the ACF \( \rho(k) \) for the AR(2) process:

#### 4.1 **Multiply by \( X_{t-k} \) and Take Expectation**

Multiply the AR(2) equation by \( X_{t-k} \) and take the expectation:
\[ \mathbb{E}[X_{t-k} X_t] = \frac{3}{1} \mathbb{E}[X_{t-k} X_{t-1}] + \frac{2}{1} \mathbb{E}[X_{t-k} X_{t-2}] \]

Since \( Z_t \) is white noise and uncorrelated with \( X_{t-k} \), we have:
\[ \mathbb{E}[X_{t-k} Z_t] = 0 \]

Using the definition of autocovariance \( \gamma(k) = \mathbb{E}[X_t X_{t-k}] \), we get:
\[ \gamma(k) = \frac{3}{1} \gamma(k-1) + \frac{2}{1} \gamma(k-2) \]

#### 4.2 **Express as ACF Equation**

Normalize by the variance \( \gamma_0 = \sigma_X^2 \):
\[ \rho(k) = \frac{3}{1} \rho(k-1) + \frac{2}{1} \rho(k-2) \]

This gives the Yule-Walker equation for the AR(2) process:
\[ \rho(k) = 3 \rho(k-1) + 2 \rho(k-2) \]

### 5. **Solving the Difference Equation**

Assume a solution of the form \( \rho(k) = \lambda^k \). Substituting into the Yule-Walker equation:
\[ \lambda^k = \frac{3}{1} \lambda^{k-1} + \frac{2}{1} \lambda^{k-2} \]

Dividing by \( \lambda^{k-2} \):
\[ \lambda^2 = 3 \lambda + 2 \]

#### 5.1 **Solve the Characteristic Equation**

The characteristic equation is:
\[ \lambda^2 - 3 \lambda - 2 = 0 \]

Solving this quadratic equation yields:
\[ \lambda = \frac{3 \pm \sqrt{13}}{2} \]

The roots are:
\[ \lambda_1 = \frac{3 + \sqrt{13}}{2}, \quad \lambda_2 = \frac{3 - \sqrt{13}}{2} \]

#### 5.2 **General Solution for \( \rho(k) \)**

The general solution for \( \rho(k) \) is:
\[ \rho(k) = c_1 \lambda_1^k + c_2 \lambda_2^k \]

### 6. **Determine Coefficients \( c_1 \) and \( c_2 \)**

#### 6.1 **Use \( \rho(0) = 1 \)**

At \( k = 0 \):
\[ \rho(0) = c_1 + c_2 = 1 \]

#### 6.2 **Use \( \rho(1) \)**

At \( k = 1 \):
\[ \rho(1) = 3 \rho(0) + 2 \rho(-1) \]

Since \( \rho(k) = \rho(-k) \):
\[ \rho(1) = 3 \cdot 1 + 2 \cdot \rho(1) \]
\[ \rho(1) = \frac{3}{2} \]

Substitute into the general solution:
\[ \rho(1) = c_1 \lambda_1 + c_2 \lambda_2 = \frac{3}{2} \]

#### 6.3 **Solve the System of Equations**

We solve:
\[ c_1 + c_2 = 1 \]
\[ c_1 \lambda_1 + c_2 \lambda_2 = \frac{3}{2} \]

Substituting the values of \( \lambda_1 \) and \( \lambda_2 \):
\[ c_1 = \frac{4 + \sqrt{13}}{8}, \quad c_2 = \frac{4 - \sqrt{13}}{8} \]

### 7. **Autocorrelation Function (ACF) for AR(2) Process**

The ACF \( \rho(k) \) is given by:
\[ \rho(k) = \frac{4 + \sqrt{13}}{8} \left(\frac{3 + \sqrt{13}}{2}\right)^k + \frac{4 - \sqrt{13}}{8} \left(\frac{3 - \sqrt{13}}{2}\right)^k \]

This formula describes the autocorrelation function of the AR(2) process based on the derived coefficients and characteristic roots.


## Yule-Walker Equations in Matrix Form for AR(p) Processes

### 1. **Autoregressive (AR) Process Definition**

An AR(p) process is defined by:
\[ X_t = \phi_0 + \phi_1 X_{t-1} + \phi_2 X_{t-2} + \cdots + \phi_p X_{t-p} + Z_t \]
where:
- \( Z_t \sim \text{Normal}(0, \sigma_Z^2) \) represents white noise with zero mean and variance \( \sigma_Z^2 \).

For simplicity, assume the process is centered (i.e., \( \phi_0 = 0 \)):
\[ X_t = \phi_1 X_{t-1} + \phi_2 X_{t-2} + \cdots + \phi_p X_{t-p} + Z_t \]

### 2. **Autocorrelation Function (ACF) and Yule-Walker Equations**

The autocorrelation function \( \rho_k \) of an AR(p) process is given by:
\[ \rho_k = \phi_1 \rho_{k-1} + \phi_2 \rho_{k-2} + \cdots + \phi_p \rho_{k-p} \]
where:
- \( \rho_0 = 1 \) (by definition of autocorrelation at lag 0).
- For negative lags, \( \rho_{-k} = \rho_k \) due to the property of autocorrelation functions being symmetric.

#### 2.1 **Deriving Yule-Walker Equations**

For \( k = 1, 2, \ldots, p \), the Yule-Walker equations are:
- For \( k = 1 \):
\[ \rho_1 = \phi_1 \rho_0 + \phi_2 \rho_{-1} + \cdots + \phi_p \rho_{1-p} \]
Since \( \rho_{-1} = \rho_1 \) and \( \rho_{1-p} = \rho_{p-1} \):
\[ \rho_1 = \phi_1 \cdot 1 + \phi_2 \rho_1 + \cdots + \phi_p \rho_{p-1} \]
- For \( k = 2 \):
\[ \rho_2 = \phi_1 \rho_1 + \phi_2 \rho_0 + \cdots + \phi_p \rho_{2-p} \]
- For \( k = 3 \):
\[ \rho_3 = \phi_1 \rho_2 + \phi_2 \rho_1 + \cdots + \phi_p \rho_{3-p} \]
- Continuing similarly up to \( k = p \):
\[ \rho_p = \phi_1 \rho_{p-1} + \phi_2 \rho_{p-2} + \cdots + \phi_p \rho_0 \]

### 3. **Matrix Form of Yule-Walker Equations**

To express the Yule-Walker equations in matrix form, define:
- \( \mathbf{r} = \begin{bmatrix} \rho_1 \\ \rho_2 \\ \vdots \\ \rho_p \end{bmatrix} \) as the vector of autocorrelations.
- \( \mathbf{\phi} = \begin{bmatrix} \phi_1 \\ \phi_2 \\ \vdots \\ \phi_p \end{bmatrix} \) as the vector of AR coefficients.

Construct the autocorrelation matrix \( R \) (also known as the Toeplitz matrix) as:
\[ R = \begin{bmatrix}
1 & \rho_1 & \rho_2 & \cdots & \rho_{p-1} \\
\rho_1 & 1 & \rho_1 & \cdots & \rho_{p-2} \\
\rho_2 & \rho_1 & 1 & \cdots & \rho_{p-3} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
\rho_{p-1} & \rho_{p-2} & \rho_{p-3} & \cdots & 1
\end{bmatrix} \]

Then, the Yule-Walker equations can be written in matrix form:
\[ \mathbf{r} = R \mathbf{\phi} \]

To solve for \( \mathbf{\phi} \):
\[ \mathbf{\phi} = R^{-1} \mathbf{r} \]

### 4. **Properties of the Matrix \( R \)**

- **Symmetry**: The matrix \( R \) is symmetric, i.e., \( R_{ij} = R_{ji} \).
- **Positive Semidefiniteness**: \( R \) is positive semidefinite, which ensures that all its eigenvalues are nonnegative.
- **Invertibility**: Since \( R \) is positive semidefinite, it is invertible if it is positive definite (i.e., all eigenvalues are strictly positive).

### 5. **Applications and Examples**

#### 5.1 **Example – AR(2) Process**

For an AR(2) process:
\[ X_t = \phi_1 X_{t-1} + \phi_2 X_{t-2} + Z_t \]

The autocorrelation matrix \( R \) is:
\[ R = \begin{bmatrix}
1 & \rho_1 \\
\rho_1 & 1
\end{bmatrix} \]

To find the coefficients \( \phi_1 \) and \( \phi_2 \):
\[ \begin{bmatrix}
\rho_1 \\
\rho_2
\end{bmatrix}
=
\begin{bmatrix}
1 & \rho_1 \\
\rho_1 & 1
\end{bmatrix}
\begin{bmatrix}
\phi_1 \\
\phi_2
\end{bmatrix} \]

#### 5.2 **Example – AR(3) Process**

For an AR(3) process:
\[ X_t = \phi_1 X_{t-1} + \phi_2 X_{t-2} + \phi_3 X_{t-3} + Z_t \]

The autocorrelation matrix \( R \) is:
\[ R = \begin{bmatrix}
1 & \rho_1 & \rho_2 \\
\rho_1 & 1 & \rho_1 \\
\rho_2 & \rho_1 & 1
\end{bmatrix} \]

To find the coefficients \( \phi_1 \), \( \phi_2 \), and \( \phi_3 \):
\[ \begin{bmatrix}
\rho_1 \\
\rho_2 \\
\rho_3
\end{bmatrix}
=
\begin{bmatrix}
1 & \rho_1 & \rho_2 \\
\rho_1 & 1 & \rho_1 \\
\rho_2 & \rho_1 & 1
\end{bmatrix}
\begin{bmatrix}
\phi_1 \\
\phi_2 \\
\phi_3
\end{bmatrix} \]

