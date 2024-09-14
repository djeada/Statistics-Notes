## Invertibility in Time Series Models

In time series modeling, **invertibility** is the property of a model that allows the innovation process (also called the noise or disturbance process) to be expressed as a function of the observed series and its past values. This is particularly relevant for **Moving Average (MA)** models.

### Intuition Behind Invertibility

Invertibility ensures that a **Moving Average (MA)** model, which expresses the current value of a series as a linear combination of white noise terms, can be transformed into an **Autoregressive (AR)** form. This is crucial because it allows us to use observed data to infer the underlying white noise, making the model estimable and stable.

An **invertible model** ensures a unique relationship between the observed values of the time series and the underlying innovations. Without invertibility, the same time series could be explained by multiple different models, which makes interpretation and prediction difficult.

### Mathematical Definition of Invertibility

Formally, a process $\{X_t\}$ is said to be **invertible** if the white noise sequence $\{Z_t\}$ can be expressed as a convergent infinite sum of past observations $\{X_t\}$:

$$
Z_t = \sum_{k=0}^{\infty} \pi_k X_{t-k}
$$

where the series $\sum_{k=0}^{\infty} |\pi_k|$ converges.

### Why is Invertibility Important?

Invertibility is essential for practical purposes because:

- It ensures that the noise (or shock) sequence $Z_t$ can be uniquely recovered from the observed data.
- It prevents model ambiguity by ensuring a one-to-one correspondence between the observed series and the underlying noise.
- It is necessary for model estimation, as non-invertible models may lead to poor or misleading parameter estimates.
  
Invertibility also allows the series to be expressed in an **AR(∞)** (AutoRegressive process of infinite order) form, which helps in analysis and forecasting.

### General Conditions for Invertibility

For a **Moving Average (MA)** process to be invertible, the parameters associated with the lagged noise terms must satisfy certain conditions. Specifically, for an MA process of order $q$:

$$
X_t = Z_t + \theta_1 Z_{t-1} + \theta_2 Z_{t-2} + \dots + \theta_q Z_{t-q}
$$

the model is invertible if and only if the roots of the associated characteristic equation lie outside the unit circle in the complex plane. The characteristic equation is:

$$
1 + \theta_1 z + \theta_2 z^2 + \dots + \theta_q z^q = 0
$$

### Example: MA(1) Process

Now let's apply the concept of invertibility to a specific case, the **Moving Average (MA(1))** process.

Consider an **MA(1)** process:

$$
X_t = Z_t + \beta Z_{t-1}
$$

where $Z_t$ is white noise with mean 0 and variance $\sigma_Z^2$, and $\beta$ is a constant. To determine the invertibility of this model, we need to express $Z_t$ in terms of $X_t$ and its past values.

#### Inversion Using Backward Substitution

We can express $Z_t$ in terms of $X_t$ and its lagged values by backward substitution. Starting from:

$$
Z_t = X_t - \beta Z_{t-1}
$$

Now substitute $Z_{t-1}$ from the same equation:

$$
Z_t = X_t - \beta \left( X_{t-1} - \beta Z_{t-2} \right) = X_t - \beta X_{t-1} + \beta^2 Z_{t-2}
$$

Continuing this process:

$$
Z_t = X_t - \beta X_{t-1} + \beta^2 X_{t-2} - \beta^3 X_{t-3} + \dots
$$

This shows that the **MA(1)** process can be written as an infinite autoregressive process:

$$
Z_t = \sum_{k=0}^{\infty} (-\beta)^k X_{t-k}
$$

This series converges if $|\beta| < 1$. Therefore, the MA(1) process is **invertible** if $|\beta| < 1$.

#### Inversion Using the Backward Shift Operator

Alternatively, we can use the **backward shift operator** to invert the MA(1) process.

Given:

$$
X_t = (1 + \beta B) Z_t
$$

where $B$ is the backward shift operator (i.e., $B Z_t = Z_{t-1}$), we aim to find $Z_t$ in terms of $X_t$ by inverting the operator $1 + \beta B$:

$$
Z_t = (1 + \beta B)^{-1} X_t
$$

The inverse of $1 + \beta B$ can be expanded as a power series:

$$
(1 + \beta B)^{-1} = 1 - \beta B + \beta^2 B^2 - \beta^3 B^3 + \dots
$$

Thus, applying this operator to $X_t$, we get:

$$
Z_t = X_t - \beta X_{t-1} + \beta^2 X_{t-2} - \beta^3 X_{t-3} + \dots
$$

This is the same result obtained by backward substitution. Again, the series converges if $|\beta| < 1$, confirming that the MA(1) process is invertible under this condition.

### Example: MA(2) Process

Consider an **MA(2)** process:

$$
X_t = Z_t + \theta_1 Z_{t-1} + \theta_2 Z_{t-2}
$$

The characteristic equation for this process is:

$$
1 + \theta_1 z + \theta_2 z^2 = 0
$$

For invertibility, the roots of this equation must lie outside the unit circle. Suppose $\theta_1 = 0.5$ and $\theta_2 = 0.3$. The characteristic equation becomes:

$$
1 + 0.5 z + 0.3 z^2 = 0
$$

Solving this quadratic equation:

$$
z = \frac{-0.5 \pm \sqrt{0.5^2 - 4 \cdot 0.3 \cdot 1}}{2 \cdot 0.3} = \frac{-0.5 \pm \sqrt{0.25 - 1.2}}{0.6}
$$

$$
z = \frac{-0.5 \pm \sqrt{-0.95}}{0.6}
$$

Since the discriminant is negative, the roots are complex numbers. The modulus of these complex roots must be greater than 1 for the process to be invertible. If the modulus of the roots is less than 1, the process is not invertible.

### Convergence of the Series in MA Models

When working with **Moving Average (MA)** models, it's important to ensure that the infinite series we obtain when trying to express the noise term $Z_t$ as a function of past observations $X_t$ converges. This is crucial because we want to guarantee that the process remains stable and well-defined over time.

#### Understanding Mean-Square Convergence

In time series analysis, when we express $Z_t$ (the white noise term) as an infinite sum of past values of the observed series $X_t$, we need this sum to **converge in the mean-square sense**. This type of convergence is important because it means that, as we include more and more past terms, the series approaches a stable value in terms of the average squared deviation from the true value of the noise term $Z_t$.

In the context of an MA(1) model, this means we can write:

$$
Z_t = X_t - \beta X_{t-1} + \beta^2 X_{t-2} - \beta^3 X_{t-3} + \dots
$$

This representation involves an **infinite series** of lagged values of $X_t$, where each term is weighted by increasing powers of $\beta$. For this series to be **stable** and **convergent**, the terms $\beta^n$ must decay as $n \to \infty$, meaning that as we go further back in time (larger lags), the influence of past values should diminish.

#### Condition for Convergence: $|\beta| < 1$

For the series to converge in the mean-square sense, the absolute value of $\beta$ must be **less than 1**. This condition ensures that the powers of $\beta$ become progressively smaller as $n$ increases, which in turn guarantees that the terms in the infinite sum $\beta^n X_{t-n}$ shrink in magnitude. If $|\beta| \geq 1$, the terms would grow or remain constant, and the series would fail to converge, leading to instability in the model.

Let’s break it down:

- **If $|\beta| < 1$:** Each successive term $\beta^n$ becomes smaller and smaller as $n$ increases, causing the series to converge to a finite value.
- **If $|\beta| = 1$:** The terms do not decay, and the series either oscillates (if $\beta = -1$) or remains constant (if $\beta = 1$).
- **If $|\beta| > 1$:** The terms $\beta^n$ grow larger as $n$ increases, causing the series to diverge.

Therefore, the necessary condition for the **convergence of the series** in an MA(1) process is:

$$
|\beta| < 1
$$

This ensures that the MA(1) model is **invertible**, meaning we can express the white noise $Z_t$ as a finite sum of past values of $X_t$.

#### Generalization to Higher-Order MA Models

The concept of convergence extends to higher-order MA models as well. For an MA(q) model:

$$
X_t = Z_t + \theta_1 Z_{t-1} + \theta_2 Z_{t-2} + \dots + \theta_q Z_{t-q}
$$

We can express the noise $Z_t$ as an infinite sum of past values of $X_t$ using a similar process. The condition for convergence in this case is that the **roots** of the characteristic polynomial:

$$
1 + \theta_1 z + \theta_2 z^2 + \dots + \theta_q z^q = 0
$$

must lie **outside the unit circle** in the complex plane. This ensures that the coefficients of the lagged terms (analogous to powers of $\beta$ in MA(1)) decay as we go further back in time, leading to a convergent series.

#### Example: MA(1) Process

For an MA(1) process:

$$
X_t = Z_t + \beta Z_{t-1}
$$

Using backward substitution, we express $Z_t$ as an infinite series:

$$
Z_t = X_t - \beta X_{t-1} + \beta^2 X_{t-2} - \beta^3 X_{t-3} + \dots
$$

The condition for this series to converge is:

$$
|\beta| < 1
$$

This ensures that the terms $\beta^n$ decay as $n \to \infty$, leading to convergence of the series. In practical terms, if $|\beta|$ is too large, the influence of past values remains strong, and the infinite series becomes unstable and non-convergent.

Thus, for any MA process, ensuring that the absolute values of the coefficients of the lagged noise terms are **less than 1** is a key requirement for convergence and invertibility.
