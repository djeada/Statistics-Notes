## Autoregressive Moving Average (ARMA) Models

ARMA models combine autoregressive (AR) and moving average (MA) components to model time series data exhibiting both autocorrelation and serial dependence.

### Mathematical Definition of ARMA Models

An **ARMA(\( p, q \))** model is defined by:

\[
X_t = c + \sum_{i=1}^{p} \phi_i X_{t-i} + \epsilon_t + \sum_{j=1}^{q} \theta_j \epsilon_{t-j}
\]

or, equivalently, using the backshift operator \( B \):

\[
\phi(B) X_t = c + \theta(B) \epsilon_t
\]

where:

- \( \phi(B) = 1 - \phi_1 B - \phi_2 B^2 - \dots - \phi_p B^p \)
- \( \theta(B) = 1 + \theta_1 B + \theta_2 B^2 + \dots + \theta_q B^q \)

### Key Concepts

#### Stationarity of AR Processes

An AR(\( p \)) process is **stationary** if all the roots of the characteristic polynomial \( \phi(B) = 0 \) lie outside the unit circle in the complex plane. This condition ensures that the time series has a constant mean and variance over time.

#### Invertibility of MA Processes

An MA(\( q \)) process is **invertible** if all the roots of \( \theta(B) = 0 \) lie outside the unit circle. Invertibility allows the MA process to be expressed as an infinite AR process, ensuring a unique representation and facilitating parameter estimation.

#### Infinite Order Representations

- **AR(∞) Representation of MA Processes**:

  An MA process can be expressed as an infinite-order AR process:

  \[
  X_t = \sum_{k=1}^{\infty} \pi_k X_{t-k} + \epsilon_t
  \]

- **MA(∞) Representation of AR Processes**:

  An AR process can be expressed as an infinite-order MA process:

  \[
  X_t = \sum_{k=0}^{\infty} \psi_k \epsilon_{t-k}
  \]

### Example: ARMA(1,1) Process

Consider the ARMA(1,1) model:

\[
X_t = \phi X_{t-1} + \epsilon_t + \theta \epsilon_{t-1}
\]

Let \( \phi = 0.7 \), \( \theta = 0.2 \), and \( \epsilon_t \) is white noise.

#### Simulation

To analyze this process, we simulate a large number of observations using statistical software (e.g., R or Python) to approximate its properties.

```r
set.seed(500)
data <- arima.sim(n = 1e6, list(ar = 0.7, ma = 0.2))
```

#### Converting ARMA to Infinite Order Processes

- **AR(∞) Representation**:

  \[
  \begin{align*}
  (1 - \phi B) X_t &= (1 + \theta B) \epsilon_t \\
  X_t &= (1 - \phi B)^{-1} (1 + \theta B) \epsilon_t \\
  X_t &= [1 + \phi B + \phi^2 B^2 + \dots] (1 + \theta B) \epsilon_t \\
  \end{align*}
  \]

  Multiplying the series:

  \[
  X_t = [1 + (\phi + \theta) B + (\phi^2 + \phi \theta) B^2 + \dots] \epsilon_t
  \]

- **MA(∞) Representation**:

  \[
  X_t = \frac{1 + \theta B}{1 - \phi B} \epsilon_t = [1 + \psi_1 B + \psi_2 B^2 + \dots] \epsilon_t
  \]

  Calculating \( \psi \) coefficients:

  \[
  \psi_k = \phi^k + \theta \phi^{k-1}
  \]

#### Theoretical Autocorrelations

The autocorrelation function (ACF) for an ARMA(1,1) process is:

\[
\rho_k = \phi^k \left( \frac{1 + \phi \theta}{1 + 2 \phi \theta + \theta^2} \right)
\]

Calculations:

\[
\begin{align*}
\rho_1 &= 0.7 \left( \frac{1 + 0.7 \times 0.2}{1 + 2 \times 0.7 \times 0.2 + 0.2^2} \right) \approx 0.777 \\
\rho_2 &= 0.7 \times \rho_1 \approx 0.544 \\
\rho_3 &= 0.7 \times \rho_2 \approx 0.381 \\
\end{align*}
\]

#### Results and Interpretation

- **Empirical ACF**: The autocorrelations computed from the simulated data closely match the theoretical values, validating the model.
- **Model Behavior**: The ARMA(1,1) model captures both the short-term dependencies (MA component) and the longer-term autocorrelation (AR component).
