## Autocovariance function

### **1. Random Variables (r.v.)**

A **random variable (r.v.)** is a mapping from a set of outcomes in a probability space to a set of real numbers. We can distinguish between:

- **Discrete random variables**: These take on countable values. For example, let:
  \[
  X = \{45, 36, 27, \dots\}
  \]

- **Continuous random variables**: These take on any value in a continuous range. For instance:
  \[
  Y \in (10, 60)
  \]

- **Realization**: A realization is a specific observed value of a random variable. For instance:
  \[
  X = 20 \quad \text{and} \quad Y = 30.29
  \]

### **2. Covariance**

- The **covariance** between two random variables \( X \) and \( Y \) measures the linear relationship between them. It is defined as:
  \[
  \text{Cov}(X, Y) = E\left[(X - \mu_X)(Y - \mu_Y)\right]
  \]
  Where:
  - \( \mu_X = E[X] \) is the mean of \( X \).
  - \( \mu_Y = E[Y] \) is the mean of \( Y \).
  - \( E[\cdot] \) denotes the expectation operator.

- The covariance is symmetric:
  \[
  \text{Cov}(X, Y) = \text{Cov}(Y, X)
  \]
  
  **Interpretation**:
  - If \( \text{Cov}(X, Y) > 0 \), \( X \) and \( Y \) increase together.
  - If \( \text{Cov}(X, Y) < 0 \), when \( X \) increases, \( Y \) tends to decrease.
  - If \( \text{Cov}(X, Y) = 0 \), there is no linear dependence between \( X \) and \( Y \).

### **3. Stochastic Processes**

- A **stochastic process** is a collection of random variables indexed by time, denoted as:
  \[
  \{X_t : t \in T\}
  \]
  where \( T \) is the index set (often time or space).

- Each \( X_t \) follows a certain distribution with a mean \( \mu \) and variance \( \sigma^2 \):
  \[
  X_t \sim \text{Distribution}(\mu, \sigma^2)
  \]

- **Example**:
  A time series is a realization of a stochastic process. Consider the following realizations:
  \[
  X_1, X_2, X_3, \dots
  \]
  Realized as:
  \[
  30, 29, 57, \dots
  \]

### **4. Autocovariance Function**

- The **autocovariance function** measures the covariance between two values of the time series at different times \( s \) and \( t \):
  \[
  \gamma(s, t) = \text{Cov}(X_s, X_t) = E\left[(X_s - \mu_s)(X_t - \mu_t)\right]
  \]
  
  Where:
  - \( X_s \) and \( X_t \) are the values of the time series at times \( s \) and \( t \), respectively.
  - \( \mu_s \) and \( \mu_t \) are the means at times \( s \) and \( t \).

- **Variance** as a special case:
  When \( s = t \), the autocovariance function simplifies to the variance of the series at time \( t \):
  \[
  \gamma(t, t) = E\left[(X_t - \mu_t)^2\right] = \text{Var}(X_t) = \sigma_t^2
  \]

### **5. Lagged Autocovariance**

- The **lagged autocovariance function** measures the covariance between values of the series at times \( t \) and \( t+k \), where \( k \) is the lag:
  \[
  \gamma_k = \gamma(t, t+k) = E\left[(X_t - \mu)(X_{t+k} - \mu)\right]
  \]
  For a **stationary process**, the autocovariance function depends only on the lag \( k \), not the specific times \( t \) and \( t+k \):
  \[
  \gamma_k \approx c_k
  \]
  
  This implies that the autocovariance function remains constant for different time points, provided the lag \( k \) is the same.
