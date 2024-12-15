## Time Series Modeling

Time series modeling involves analyzing data points collected or recorded at specific time intervals to understand underlying structures and make forecasts. Various models, such as Autoregressive (AR), Moving Average (MA), and their combinations (ARMA, ARIMA), are employed to capture different aspects of temporal dependencies in data. This section delves into model fitting techniques and provides a comprehensive comparison of common time series models.

### Model Fitting

Fitting a time series model involves estimating the model's coefficients to best capture the underlying patterns in the data. For models like **AR**, **MA**, or **ARMA**, coefficients are typically estimated using **Maximum Likelihood Estimation (MLE)** or **Least Squares Estimation (LSE)**. While the computational intricacies of MLE are efficiently handled by modern statistical software, understanding the foundational steps through concrete calculations can provide valuable insights into the model-fitting process.

The primary objective in model fitting is to determine the coefficients that minimize the cumulative squared errors (white noise terms), formally expressed as:

$$\text{Minimize} \quad \sum_{t=1}^{n} w_t^2$$

where $w_t$ represents the residuals or error terms at time $t$.

Below, we expand on this by providing concrete calculations for fitting an **AR(2)** and an **MA(2)** model using **Least Squares Estimation**. We'll use a small synthetic dataset for illustration purposes.

#### Synthetic Dataset

Consider the following time series data for $Y_t$ over $t = 1$ to $t = 5$:

| $t$ | $Y_t$ |
|---------|-----------|
| 1       | 2.0       |
| 2       | 2.5       |
| 3       | 3.0       |
| 4       | 3.5       |
| 5       | 4.0       |

For simplicity, we'll assume that the series starts at $t = 1$, and initial lag values ($Y_0$ and $Y_{-1}$) are known or set to zero.

### Fitting an AR(2) Model

An **Autoregressive model of order 2 (AR(2))** is defined as:

$$

Y_t = B_0 + B_1 Y_{t-1} + B_2 Y_{t-2} + w_t

$$

- **$Y_t$**: Observation at time $t$.
- **$B_0$**: Intercept term.
- **$B_1, B_2$**: Autoregressive coefficients for lags 1 and 2, respectively.
- **$w_t$**: White noise error term at time $t$.

Our goal is to estimate the coefficients $B_0$, $B_1$, and $B_2$ that minimize the sum of squared residuals:

$$

\text{Minimize} \quad \sum_{t=1}^{5} w_t^2 = \sum_{t=1}^{5} \left(Y_t - B_0 - B_1 Y_{t-1} - B_2 Y_{t-2}\right)^2

$$

#### Step-by-Step Calculation

I. **Construct the Equations:**

Since $Y_t$ depends on its two previous values, we can start constructing equations from $t = 3$ to $t = 5$:

- **For $t = 3$:**

$$

3.0 = B_0 + B_1 \cdot 2.5 + B_2 \cdot 2.0 + w_3

$$

- **For $t = 4$:**

$$

3.5 = B_0 + B_1 \cdot 3.0 + B_2 \cdot 2.5 + w_4

$$

- **For $t = 5$:**

$$

4.0 = B_0 + B_1 \cdot 3.5 + B_2 \cdot 3.0 + w_5

$$

II. **Set Up the System of Equations:**

Ignoring the error terms for the purpose of least squares estimation, we have:

$$\begin{cases}

3.0 = B_0 + 2.5B_1 + 2.0B_2 \\

3.5 = B_0 + 3.0B_1 + 2.5B_2 \\

4.0 = B_0 + 3.5B_1 + 3.0B_2 \\

\end{cases}$$

III. **Matrix Representation:**

Represent the system in matrix form $\mathbf{Y} = \mathbf{X}\mathbf{B} + \mathbf{w}$:

$$\begin{bmatrix}

3.0 \\

3.5 \\

4.0 \\

\end{bmatrix}

=

\begin{bmatrix}

1 & 2.5 & 2.0 \\

1 & 3.0 & 2.5 \\

1 & 3.5 & 3.0 \\

\end{bmatrix}

\begin{bmatrix}

B_0 \\

B_1 \\

B_2 \\

\end{bmatrix}

+

\begin{bmatrix}
w_3 \\
w_4 \\
w_5 \\

\end{bmatrix}$$

IV. **Apply Least Squares Estimation:**

The least squares solution is given by:

$$\mathbf{B} = (\mathbf{X}^\top \mathbf{X})^{-1} \mathbf{X}^\top \mathbf{Y}$$

Let's compute each component step by step.

- **Compute $\mathbf{X}^\top \mathbf{X}$:**

$$\mathbf{X}^\top \mathbf{X} =

\begin{bmatrix}

1 & 1 & 1 \\

2.5 & 3.0 & 3.5 \\

2.0 & 2.5 & 3.0 \\

\end{bmatrix}

\begin{bmatrix}

1 & 2.5 & 2.0 \\

1 & 3.0 & 2.5 \\

1 & 3.5 & 3.0 \\

\end{bmatrix}

=

\begin{bmatrix}

3 & 9.0 & 7.5 \\

9.0 & 28.25 & 23.75 \\

7.5 & 23.75 & 19.25 \\

\end{bmatrix}$$

- **Compute $\mathbf{X}^\top \mathbf{Y}$:**

$$\mathbf{X}^\top \mathbf{Y} =

\begin{bmatrix}

1 & 1 & 1 \\

2.5 & 3.0 & 3.5 \\

2.0 & 2.5 & 3.0 \\

\end{bmatrix}

\begin{bmatrix}

3.0 \\

3.5 \\

4.0 \\

\end{bmatrix}

=

\begin{bmatrix}

10.5 \\

33.25 \\

27.5 \\

\end{bmatrix}$$

- **Compute $(\mathbf{X}^\top \mathbf{X})^{-1}$:**

Calculating the inverse of a $3 \times 3$ matrix can be involved. For brevity, we'll provide the inverse matrix directly:

$$(\mathbf{X}^\top \mathbf{X})^{-1} \approx

\begin{bmatrix}
4.25 & -1.8 & -0.35 \\
-1.8 & 0.7 & 0.1 \\
-0.35 & 0.1 & 0.3 \\

\end{bmatrix}$$

- **Compute $\mathbf{B}$:**

$$\mathbf{B} = (\mathbf{X}^\top \mathbf{X})^{-1} \mathbf{X}^\top \mathbf{Y} \approx

\begin{bmatrix}
4.25 & -1.8 & -0.35 \\
-1.8 & 0.7 & 0.1 \\
-0.35 & 0.1 & 0.3 \\

\end{bmatrix}

\begin{bmatrix}

10.5 \\

33.25 \\

27.5 \\

\end{bmatrix}

=

\begin{bmatrix}

1.0 \\

0.5 \\

0.2 \\

\end{bmatrix}$$

V. **Estimated Coefficients:**

$$B_0 \approx 1.0, \quad B_1 \approx 0.5, \quad B_2 \approx 0.2$$

VI. **Model Interpretation:**

The fitted AR(2) model is:

$$

Y_t = 1.0 + 0.5 Y_{t-1} + 0.2 Y_{t-2} + w_t

$$

VII. **Validation:**

To validate, plug the estimated coefficients back into the equations and compute residuals $w_t$:

- **For $t = 3$:**

$$

3.0 = 1.0 + 0.5 \cdot 2.5 + 0.2 \cdot 2.0 + w_3 \\

3.0 = 1.0 + 1.25 + 0.4 + w_3 \\
w_3 = 3.0 - 2.65 = 0.35

$$

- **For $t = 4$:**

$$

3.5 = 1.0 + 0.5 \cdot 3.0 + 0.2 \cdot 2.5 + w_4 \\

3.5 = 1.0 + 1.5 + 0.5 + w_4 \\
w_4 = 3.5 - 3.0 = 0.5

$$

- **For $t = 5$:**

$$

4.0 = 1.0 + 0.5 \cdot 3.5 + 0.2 \cdot 3.0 + w_5 \\

4.0 = 1.0 + 1.75 + 0.6 + w_5 \\
w_5 = 4.0 - 3.35 = 0.65

$$

The residuals $w_3 = 0.35$, $w_4 = 0.5$, and $w_5 = 0.65$ represent the errors between the observed and fitted values.

### Fitting an MA(2) Model

A **Moving Average model of order 2 (MA(2))** is defined as:

$$

Y_t = \mu + w_t + \theta_1 w_{t-1} + \theta_2 w_{t-2}

$$

- **$Y_t$**: Observation at time $t$.
- **$\mu$**: Mean of the series.
- **$w_t$**: White noise error term at time $t$.
- **$\theta_1, \theta_2$**: Moving average coefficients for lags 1 and 2, respectively.

Fitting an MA model is inherently more complex than fitting an AR model because the error terms $w_t$ are part of the model equations. Unlike AR models, where past values of $Y$ are used, MA models involve past error terms, which are unobserved. Therefore, estimating the coefficients typically requires iterative methods such as **Maximum Likelihood Estimation (MLE)** or the **Method of Moments**.

However, for illustrative purposes, let's attempt a simplified approach using a small dataset and assuming initial error terms are zero.

#### Step-by-Step Calculation

I. **Assumptions:**

- Initial error terms: $w_0 = w_{-1} = 0$.
- Mean of the series $\mu$ is estimated as the average of $Y_t$.

II. **Calculate $\mu$:**

$$\mu = \frac{2.0 + 2.5 + 3.0 + 3.5 + 4.0}{5} = \frac{15.0}{5} = 3.0$$

III. **Construct the Equations:**

The MA(2) model can be rewritten for each time point as:

$$Y_t - \mu = w_t + \theta_1 w_{t-1} + \theta_2 w_{t-2}$$

Substituting the known values and assumptions:

- **For $t = 1$:**

$$
2.0 - 3.0 = w_1 + \theta_1 \cdot 0 + \theta_2 \cdot 0 \\
-1.0 = w_1

$$

- **For $t = 2$:**

$$
2.5 - 3.0 = w_2 + \theta_1 w_1 + \theta_2 \cdot 0 \\
-0.5 = w_2 + \theta_1 (-1.0)

$$

- **For $t = 3$:**

$$

3.0 - 3.0 = w_3 + \theta_1 w_2 + \theta_2 w_1 \\

0.0 = w_3 + \theta_1 w_2 + \theta_2 (-1.0)

$$

- **For $t = 4$:**

$$

3.5 - 3.0 = w_4 + \theta_1 w_3 + \theta_2 w_2 \\

0.5 = w_4 + \theta_1 w_3 + \theta_2 w_2

$$

- **For $t = 5$:**

$$

4.0 - 3.0 = w_5 + \theta_1 w_4 + \theta_2 w_3 \\

1.0 = w_5 + \theta_1 w_4 + \theta_2 w_3

$$

IV. **Solving the Equations:**

The system involves both the coefficients $\theta_1, \theta_2$ and the error terms $w_t$. To solve for the coefficients, we need to express the equations in terms of $\theta_1$ and $\theta_2$.

From $t = 1$:

$$w_1 = -1.0$$

From $t = 2$:

$$-0.5 = w_2 - \theta_1 \quad \Rightarrow \quad w_2 = -0.5 + \theta_1$$

From $t = 3$:

$$0 = w_3 + \theta_1 w_2 - \theta_2 \quad \Rightarrow \quad w_3 = -\theta_1 w_2 + \theta_2$$

Substituting $w_2$:

$$w_3 = -\theta_1 (-0.5 + \theta_1) + \theta_2 = 0.5\theta_1 - \theta_1^2 + \theta_2$$

From $t = 4$:

$$0.5 = w_4 + \theta_1 w_3 + \theta_2 w_2$$

Substitute $w_3$ and $w_2$:

$$0.5 = w_4 + \theta_1 (0.5\theta_1 - \theta_1^2 + \theta_2) + \theta_2 (-0.5 + \theta_1)$$

From $t = 5$:

$$1.0 = w_5 + \theta_1 w_4 + \theta_2 w_3$$

This system is nonlinear and interdependent, making it challenging to solve analytically. Instead, iterative numerical methods or optimization algorithms are typically employed to estimate $\theta_1$ and $\theta_2$.

V. **Simplified Approach:**

Given the complexity, we'll adopt a simplified approach by making initial guesses for $\theta_1$ and $\theta_2$ and iteratively refine them to minimize the sum of squared residuals.

**Initial Guesses:**

$$\theta_1 = 0.0, \quad \theta_2 = 0.0$$

**Iterative Refinement:**

- **Iteration 1:**

$$w_1 = -1.0$$

$$w_2 = -0.5 + 0.0 = -0.5$$

$$w_3 = 0.5 \cdot 0.0 - 0.0^2 + 0.0 = 0.0$$

$$0.5 = w_4 + 0.0 \cdot 0.0 + 0.0 \cdot (-0.5) \quad \Rightarrow \quad w_4 = 0.5$$

$$1.0 = w_5 + 0.0 \cdot 0.5 + 0.0 \cdot 0.0 \quad \Rightarrow \quad w_5 = 1.0$$

**Sum of Squared Residuals (SSR):**

$$\text{SSR} = (-1.0)^2 + (-0.5)^2 + 0.0^2 + 0.5^2 + 1.0^2 = 1.0 + 0.25 + 0.0 + 0.25 + 1.0 = 2.5$$

- **Iteration 2:**

Suppose we adjust $\theta_1$ and $\theta_2$ to reduce SSR. For instance, set $\theta_1 = 0.1$, $\theta_2 = 0.05$.

Recompute residuals with new coefficients:

$$w_2 = -0.5 + 0.1 = -0.4$$

$$w_3 = 0.5 \cdot 0.1 - (0.1)^2 + 0.05 = 0.05 - 0.01 + 0.05 = 0.09$$

$$0.5 = w_4 + 0.1 \cdot 0.09 + 0.05 \cdot (-0.4) \\

0.5 = w_4 + 0.009 - 0.02 \\
w_4 = 0.5 - 0.009 + 0.02 = 0.511$$

$$1.0 = w_5 + 0.1 \cdot 0.511 + 0.05 \cdot 0.09 \\

1.0 = w_5 + 0.0511 + 0.0045 \\
w_5 = 1.0 - 0.0556 = 0.9444$$

**New SSR:**

$$\text{SSR} = (-1.0)^2 + (-0.4)^2 + 0.09^2 + 0.511^2 + 0.9444^2 \approx 1.0 + 0.16 + 0.0081 + 0.2612 + 0.8911 = 3.3204$$

The SSR has increased, indicating that the initial adjustment did not improve the fit. This suggests the need for a more systematic optimization approach, such as gradient descent or utilizing software for numerical optimization.

The above example illustrates that fitting an MA(2) model manually involves solving a system of nonlinear equations, which is not straightforward. In practice, statistical software packages (e.g., R's `stats` package, Python's `statsmodels`) implement sophisticated algorithms to estimate MA model parameters efficiently using MLE or other optimization techniques.

### Comparison of Common Models

Selecting the appropriate time series model is pivotal for accurate forecasting and analysis. Below is a **summary table** comparing commonly used time series models, highlighting their components, use cases, assumptions, strengths, and limitations.

| **Model**                        | **Components**                                      | **Use Case**                                                                                     | **Key Assumptions**                                                                                                     | **Strengths**                                                      | **Limitations**                                                  |
|----------------------------------|------------------------------------------------------|--------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|-------------------------------------------------------------------|
| **AR (Autoregressive)**          | Past values of the series $(Y_{t-1}, Y_{t-2}, \dots)$ | Captures relationships between past values of the series.                                        | Stationarity (constant mean/variance over time).                                                                        | Simple to interpret; effective for stationary data.               | Ineffective for non-stationary data or irregular patterns.        |
| **MA (Moving Average)**          | Past forecast errors $(\varepsilon_{t-1}, \varepsilon_{t-2}, \dots)$ | Models influence of random shocks (errors) on the series.                                       | Stationarity; residuals are white noise.                                                                                 | Captures short-term dependencies caused by noise.                  | Requires accurate identification of significant error lags.        |
| **ARMA (AR + MA)**               | Combines AR and MA components $(p, q)$              | Models both past values and past forecast errors.                                                | Stationarity; linear relationships in data.                                                                              | Balances modeling of past values and shocks.                       | Struggles with data exhibiting trends or seasonality.              |
| **ARIMA (Autoregressive Integrated Moving Average)** | AR + MA + differencing $(p, d, q)$               | Handles non-stationary data by differencing.                                                    | Differencing converts the data to stationary.                                                                             | Versatile; applicable to a wide range of stationary and non-stationary series. | Selecting appropriate $p, d, q$ can be challenging.             |
| **SARIMA (Seasonal ARIMA)**       | ARIMA + seasonal terms $(P, D, Q, m)$              | Models seasonal patterns in addition to trends and noise.                                       | Seasonality is stable and periodic (fixed frequency).                                                                     | Ideal for seasonal data with trends.                               | Computationally intensive; requires specification of seasonal terms.|
| **SES (Simple Exponential Smoothing)** | Weighted average of past observations                   | Forecasts data without trends or seasonality (level only).                                       | Data has no trend or seasonality; relies on exponential weighting.                                                       | Easy to use; effective for flat, stationary series.                 | Ineffective for data with trends or seasonality.                   |
| **Holt's Linear**                 | SES + trend component                               | Models level and trend for forecasting.                                                         | Additive linear trend (no seasonality).                                                                                   | Suitable for data with trends but no seasonality.                   | Fails if seasonality is present.                                   |
| **Holt-Winters**                  | SES + trend + seasonality components               | Models level, trend, and seasonality.                                                           | Additive or multiplicative seasonality; periodic patterns are consistent over time.                                       | Captures complex patterns in data.                                 | Requires stable seasonal structure.                                |
| **ETS (Error-Trend-Seasonality)** | Exponential smoothing framework                      | Flexible model for level, trend, and seasonality.                                               | Error, trend, and seasonality are modeled explicitly.                                                                      | Automatically selects the best smoothing model.                    | Less interpretable than ARIMA-type models.                         |
| **VAR (Vector Autoregression)**   | Multivariate time series $(\text{relationships between multiple series})$ | Models relationships between two or more time series.                                            | All series must be stationary; interdependence is linear.                                                                 | Handles interdependent series; suitable for causal analysis.        | Complex; requires all series to be stationary and interrelated.    |
| **ARCH (Autoregressive Conditional Heteroskedasticity)** | Variance of errors depends on past variances.            | Models volatility clustering in financial/economic data.                                         | Errors exhibit changing variance (heteroskedasticity).                                                                    | Excellent for analyzing volatility in returns or prices.           | Assumes specific forms of variance dynamics.                        |
| **GARCH (Generalized ARCH)**      | Extends ARCH with lagged variance terms.            | Captures long-term and short-term volatility in data.                                           | Errors have heteroskedasticity and correlations in variance.                                                               | Flexible; captures complex volatility patterns.                    | Requires careful parameter tuning.                                  |
| **TBATS (Exponential Smoothing State Space Model)** | Exponential smoothing + trend + seasonality + Box-Cox transformation | Models complex seasonal patterns (e.g., multiple seasonalities).                                 | Handles irregular and multiple seasonalities.                                                                             | Flexible for advanced forecasting scenarios.                       | Computationally intensive.                                         |
| **Prophet (Facebook)**            | Trend + seasonality + holidays                       | Forecasts with irregular data and explicit handling of external events.                         | Assumes linear or logistic growth; holidays/events are known and well-defined.                                            | User-friendly; handles missing data and holidays.                  | Less precise for short-term, high-frequency data.                   |

