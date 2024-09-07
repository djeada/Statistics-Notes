## Stationarity

1. **Intuition for (Weak) Stationary Time Series:**
   - A stationary time series is a data sequence where the statistical properties remain consistent over time. Specifically:
     - **No systematic change in mean** (i.e., no trend over time).
     - **No systematic change in variance** (i.e., constant variation across time).
     - **No periodic fluctuations** (i.e., no repeating cycles or seasonality).
   - The properties (such as mean, variance, and autocorrelation) of one section of the data are similar to those of other sections of the data.
     - This implies that the data behaves similarly at any point in time.

2. **Dealing with Non-Stationary Time Series:**
   - In practice, many time series data sets are non-stationary, meaning they may exhibit trends, changing variance, or seasonality.
   - To analyze non-stationary time series, we often apply **transformations** to make the series stationary, which is essential for many statistical modeling techniques (e.g., ARIMA models).
     - Common transformations include **differencing**, **logarithmic transformations**, or **detrending** to remove trends or stabilize variance.

### Weak Stationarity
- A **weakly stationary** (or second-order stationary) time series is a more relaxed definition of stationarity, focusing primarily on the first two moments of the distribution (mean and variance):
  - The **mean** of the series is constant over time.
  - The **variance** is constant over time (no systematic change in variance).
  - The **covariance** between values at different times depends only on the time difference (lag) between them and not the actual time itself.



### **Stationarity: Properties and Examples**

#### **1. Weak Stationarity**
A process is said to be **weakly stationary** if:
1. The mean $\mu(t)$ is constant over time.
2. The variance $\text{Var}(X_t)$ is constant over time.
3. The autocovariance $\gamma(t_1, t_2)$ depends only on the time difference $|t_1 - t_2|$.

For a weakly stationary process, the **autocorrelation** function $\rho(t)$ satisfies the property:
$$
-1 \leq \rho(t) \leq 1
$$
This is analogous to the elementary statistics result that the correlation coefficient between two random variables lies between -1 and 1.

In linear algebra terms, if you have two vectors $x$ and $y$, the inequality $|x^T y| \leq \|x\|_2 \|y\|_2$ applies, which is a similar concept to the bound on autocorrelations.

---

#### **2. Variance of a Linear Combination of Random Variables**

To explore this mathematically, consider a linear combination of two random variables $X_1$ and $X_2$, with the requirement that the variance of this combination is non-negative:
$$
V[aX_1 + bX_2] \geq 0
$$
Expanding this variance expression, we use the properties of variances and covariances:
$$
V[aX_1 + bX_2] = a^2 V[X_1] + b^2 V[X_2] + 2ab \, \text{Cov}(X_1, X_2)
$$
For a time series, with a lag of $\tau$, we substitute $X_1 = X(t)$ and $X_2 = X(t + \tau)$:
$$
V[aX(t) + bX(t + \tau)] = a^2 V[X(t)] + b^2 V[X(t + \tau)] + 2ab \, \text{Cov}(X(t), X(t + \tau)) \geq 0
$$
Assuming weak stationarity, where the variance is constant across time, we get:
$$
a^2 \sigma^2 + b^2 \sigma^2 + 2ab \, \gamma(\tau) \geq 0
$$
This gives two special cases:

- **Case 1: $a = b = 1$**:
$$
2 \sigma^2 + 2 \, \gamma(\tau) \geq 0
$$
Simplifying:
$$
\sigma^2 \geq - \gamma(\tau)
$$
So:
$$
1 \geq - \rho(\tau)
$$
Thus, $\rho(\tau) \geq -1$.

- **Case 2: $a = 1, b = -1$**:
This case can be used to show that $\rho(\tau) \leq 1$, completing the proof that:
$$
-1 \leq \rho(\tau) \leq 1
$$

---

#### **3. Stationary Models**

##### **White Noise**
White noise is a simple example of a weakly stationary process. Suppose $X_t$ are i.i.d. random variables drawn from a normal distribution:
$$
X_t \sim \mathcal{N}(\mu, \sigma^2)
$$
The mean function $\mu(t)$ is constant:
$$
\mu(t) = \mu
$$
The autocovariance function $\gamma(t_1, t_2)$ is:
$$
\gamma(t_1, t_2) = 
\begin{cases} 
0 & t_1 \neq t_2 \\
\sigma^2 & t_1 = t_2
\end{cases}
$$
The autocorrelation function $\rho(t_1, t_2)$ is:
$$
\rho(t_1, t_2) = 
\begin{cases} 
0 & t_1 \neq t_2 \\
1 & t_1 = t_2
\end{cases}
$$
Thus, white noise is weakly stationary and can even be shown to be strictly stationary.

---

##### **Random Walk**
A **random walk** is not weakly stationary. Consider a random walk with i.i.d. steps $Z_t$ such that $E[Z_t] = \mu$ and $\text{Var}(Z_t) = \sigma^2$. The random walk is given by:
$$
X_t = X_{t-1} + Z_t = \sum_{i=1}^{t} Z_i
$$
- The **mean** of the random walk is:
$$
E[X_t] = \sum_{i=1}^{t} E[Z_i] = t \cdot \mu
$$
- The **variance** of the random walk is:
$$
\text{Var}(X_t) = \sum_{i=1}^{t} \text{Var}(Z_i) = t \cdot \sigma^2
$$
Thus, the variance increases with time, indicating that the random walk is not stationary.

---

##### **Moving Average Processes (MA(q))**
In a **moving average process** of order $q$, $X_t$ is a linear combination of white noise terms from the present and past $q$ periods:
$$
X_t = \beta_0 Z_t + \beta_1 Z_{t-1} + \dots + \beta_q Z_{t-q}
$$
Where $Z_t \sim \mathcal{N}(0, \sigma^2_Z)$ and are i.i.d. random variables.

- The **mean** of $X_t$ is:
$$
E[X_t] = \beta_0 E[Z_t] + \beta_1 E[Z_{t-1}] + \dots + \beta_q E[Z_{t-q}] = 0
$$
- The **variance** of $X_t$ is:
$$
\text{Var}(X_t) = \beta_0^2 \text{Var}(Z_t) + \beta_1^2 \text{Var}(Z_{t-1}) + \dots + \beta_q^2 \text{Var}(Z_{t-q}) = \sigma_Z^2 \sum_{i=0}^{q} \beta_i^2
$$
- The **autocovariance** of $X_t$ and $X_{t+k}$ is:
$$
\text{Cov}(X_t, X_{t+k}) = 
\begin{cases} 
0 & k > q \\
\sigma_Z^2 \sum_{i=0}^{q-k} \beta_i \beta_{i+k} & k \leq q
\end{cases}
$$
Since the autocovariance function depends only on the lag $k$, the moving average process is weakly stationary.

- The **autocorrelation function** $\rho(k)$ is:
$$
\rho(k) = \frac{\gamma(k)}{\gamma(0)} = \frac{\sum_{i=0}^{q-k} \beta_i \beta_{i+k}}{\sum_{i=0}^{q} \beta_i^2}
$$


### **Stationarity: Intuition and Definition**

---

#### **1. Stochastic Processes**
A **stochastic process** is essentially a random process that generates a sequence of random variables over time. Stochastic processes can be either **discrete** or **continuous**:

- A **discrete stochastic process** is a family of random variables $\{X_t \}$ indexed by discrete time steps $t$. An example could be the daily high temperatures in Melbourne.
  
- A **continuous stochastic process**, such as the **Wiener process** (Brownian motion), is indexed by a continuous variable $t$, where $X(t)$ describes the position of a particle as it floats on a liquid surface.

---

#### **2. Ensembles and Realizations**
In the context of stochastic processes:
- A **realization** is a single observed trajectory of a stochastic process. For example, one observed time series of stock prices over time is a realization of a stochastic process.
  
- The **ensemble** is the set of all possible realizations (trajectories) of the process.

In practice, we usually observe only one realization, and we have to infer the properties of the underlying stochastic process from this single observation.

---

#### **3. Mean, Variance, and Autocovariance Functions**
When analyzing stochastic processes, we summarize the behavior using:
- **Mean function** $\mu(t) = E[X(t)]$: the expected value of the random variables at time $t$.
  
- **Variance function** $\sigma^2(t) = V[X(t)]$: the variance of the random variable at time $t$.

- **Autocovariance function** $\gamma(t_1, t_2)$:
  $$
  \gamma(t_1, t_2) = E[(X(t_1) - \mu(t_1))(X(t_2) - \mu(t_2))]
  $$
  This function measures how the values of the process at times $t_1$ and $t_2$ are related.

---

#### **4. Strict Stationarity**
A process is **strictly stationary** if the joint distribution of $X(t_1), X(t_2), \dots, X(t_k)$ is the same as the joint distribution of $X(t_1 + \tau), X(t_2 + \tau), \dots, X(t_k + \tau)$ for any time shift $\tau$.

- This implies that all random variables $X(t)$ have the same distribution (i.e., identically distributed).
- In a strictly stationary process, the **mean** and **variance** functions are constant:
  $$
  \mu(t) = \mu, \quad \sigma^2(t) = \sigma^2
  $$
- The **autocovariance** function depends only on the lag $\tau = t_2 - t_1$, so we can write:
  $$
  \gamma(t_1, t_2) = \gamma(\tau)
  $$
  The process is invariant to shifts in time, and the behavior of the process depends only on the distance between time points.

#### **Example of Strict Stationarity**
Consider a time series $Y_i = \beta_0 + \beta_1 x_i + \epsilon_i$, where $\epsilon_i$ are i.i.d. random errors. A time series with a trend (where $\beta_1 \neq 0$) is not stationary, because the mean function changes over time, and the process does not remain identical when shifted in time.

---

#### **5. Weak (Second-Order) Stationarity**
A weaker form of stationarity, called **weak stationarity** or **second-order stationarity**, imposes less restrictive conditions. A process is weakly stationary if:
- The **mean function** is constant: $\mu(t) = \mu$.
- The **autocovariance function** depends only on the time difference (lag) $\tau$:
  $$
  \gamma(t_1, t_2) = \gamma(\tau)
  $$
  - For $\tau = 0$, the autocovariance becomes the variance:
    $$
    \gamma(0) = E[(X(t) - \mu)^2] = \sigma^2
    $$
  
Weak stationarity focuses on the first two moments (mean and variance) and the autocovariance, ignoring higher-order moments, which is why it is a weaker condition than strict stationarity.

---

#### **6. Intuition of Stationarity in Practice**
Stationarity allows us to "pool" our data and make inferences about the overall process from a single realization. In practice, we often work with weakly stationary processes, which simplify the analysis by ensuring that the statistical properties of the process do not change over time.

Stationary processes are particularly useful for prediction and modeling, as their future behavior is easier to estimate when the past and present exhibit the same statistical characteristics.



#### **1. Weak Stationarity and Autocorrelation Bounds**

For a **weakly stationary process**, the autocorrelation function $\rho(\tau)$ (the correlation between two points in the process separated by lag $\tau$) must satisfy the condition:
$$
-1 \leq \rho(\tau) \leq 1
$$
This is similar to the result from elementary statistics, where the correlation between two random variables is bounded by -1 and 1. This is also analogous to the linear algebra result $|x^T y| \leq \|x\|_2 \|y\|_2$.

To understand this better, we can use the following reasoning. We know that variances are non-negative, so consider a linear combination of two random variables $X_1$ and $X_2$. The variance of this combination must satisfy:
$$
V[a X_1 + b X_2] \geq 0
$$
Now, for time series data, let’s generalize this to a lag $\tau$ between two time points:
$$
V[a X(t) + b X(t + \tau)] \geq 0
$$
Using the well-known properties of variance and covariance:
$$
V[X + Y] = V[X] + V[Y] + 2 \, \text{Cov}(X, Y)
$$
and
$$
V[a X] = a^2 V[X]
$$
we can expand the variance of the linear combination as:
$$
V[a X(t) + b X(t + \tau)] = a^2 V[X(t)] + b^2 V[X(t + \tau)] + 2 a b \, \text{Cov}(X(t), X(t + \tau))
$$
For a weakly stationary process, the variances are constant over time, so we replace $V[X(t)]$ and $V[X(t + \tau)]$ with $\sigma^2$:
$$
a^2 \sigma^2 + b^2 \sigma^2 + 2 a b \, \text{Cov}(X(t), X(t + \tau)) \geq 0
$$
This inequality holds for any values of $a$ and $b$. Let’s consider two specific cases:

- **Case 1: $a = b = 1$**:
  $$
  2 \sigma^2 + 2 \, \text{Cov}(X(t), X(t + \tau)) \geq 0
  $$
  Simplifying, we get:
  $$
  \sigma^2 \geq - \text{Cov}(X(t), X(t + \tau))
  $$
  Dividing both sides by $\sigma^2$, we obtain:
  $$
  1 \geq - \rho(\tau)
  $$
  Hence, $\rho(\tau) \geq -1$.

- **Case 2: $a = 1, b = -1$**:
  Using this case, one can similarly show that $\rho(\tau) \leq 1$, completing the bound:
  $$
  -1 \leq \rho(\tau) \leq 1
  $$

---

#### **2. Stationary Models**

##### **White Noise**
White noise is a classic example of a weakly stationary process. Consider a sequence of independent, identically distributed (i.i.d.) random variables $X_t \sim \mathcal{N}(\mu, \sigma^2)$. For white noise:
- The **mean function** $\mu(t)$ is constant:
  $$
  \mu(t) = \mu
  $$
- The **autocovariance function** $\gamma(t_1, t_2)$ is:
  $$
  \gamma(t_1, t_2) = 
  \begin{cases}
  0 & \text{if } t_1 \neq t_2 \\
  \sigma^2 & \text{if } t_1 = t_2
  \end{cases}
  $$
- The **autocorrelation function** $\rho(t_1, t_2)$ is:
  $$
  \rho(t_1, t_2) = 
  \begin{cases}
  0 & \text{if } t_1 \neq t_2 \\
  1 & \text{if } t_1 = t_2
  \end{cases}
  $$
White noise is weakly stationary because its mean and variance are constant, and its autocovariance depends only on the lag between time points.

---

##### **Random Walk**
A **random walk** is not stationary. Consider a random walk $X_t$ where $X_t = X_{t-1} + Z_t$, with i.i.d. increments $Z_t \sim \mathcal{N}(\mu, \sigma^2)$. 
- The **mean** of the random walk grows linearly with time:
  $$
  E[X_t] = t \cdot \mu
  $$
- The **variance** of the random walk increases linearly with time:
  $$
  V[X_t] = t \cdot \sigma^2
  $$
Thus, the random walk is not stationary because its mean and variance are time-dependent.

---

##### **Moving Average Process (MA(q))**
A **Moving Average process** of order $q$, denoted $\text{MA}(q)$, is given by:
$$
X_t = \beta_0 Z_t + \beta_1 Z_{t-1} + \dots + \beta_q Z_{t-q}
$$
where $Z_t \sim \mathcal{N}(0, \sigma_Z^2)$ are i.i.d. white noise terms. For the MA(q) process:
- The **mean** of $X_t$ is zero:
  $$
  E[X_t] = 0
  $$
- The **variance** of $X_t$ is constant:
  $$
  V[X_t] = \sigma_Z^2 \sum_{i=0}^{q} \beta_i^2
  $$
- The **autocovariance** at lag $k$ is:
  $$
  \gamma(k) = 
  \begin{cases}
  \sigma_Z^2 \sum_{i=0}^{q-k} \beta_i \beta_{i+k} & \text{if } k \leq q \\
  0 & \text{if } k > q
  \end{cases}
  $$
The MA(q) process is weakly stationary because its mean and variance are constant, and the autocovariance depends only on the lag.

---

#### **3. Autocorrelation Function of the MA(q) Process**

The **autocorrelation function** $\rho(k)$ for the MA(q) process is obtained by normalizing the autocovariance function by the variance:
$$
\rho(k) = \frac{\gamma(k)}{\gamma(0)}
$$
Since $\gamma(0) = \sigma_Z^2 \sum_{i=0}^{q} \beta_i^2$, the autocorrelation function is:
$$
\rho(k) = \frac{\sum_{i=0}^{q-k} \beta_i \beta_{i+k}}{\sum_{i=0}^{q} \beta_i^2}
$$
For $k > q$, the autocorrelation $\rho(k) = 0$, as the process has no memory beyond $q$ time steps.

