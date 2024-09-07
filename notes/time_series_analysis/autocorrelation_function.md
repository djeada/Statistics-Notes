## ACF and PACF

### **Autocorrelation Function (ACF) and Estimation**

#### **1. Another Way to Write \( r_k \)**

- The **autocorrelation coefficient** \( r_k \) is a normalized version of the autocovariance coefficient \( \gamma_k \). It measures the linear relationship between the values of a time series at different time lags \( k \). The formula for \( r_k \) is given by:
  \[
  r_k = \frac{\sum_{t=1}^{N-k} (x_t - \bar{x})(x_{t+k} - \bar{x})}{\sum_{t=1}^{N} (x_t - \bar{x})^2}
  \]
  Where:
  - \( \bar{x} = \frac{1}{N} \sum_{t=1}^{N} x_t \) is the sample mean of the series.
  - \( N \) is the total number of observations in the series.
  
  This expression for \( r_k \) is the **autocorrelation coefficient at lag \( k \)**. It normalizes the autocovariance \( c_k \) by the total variance, making it dimensionless and easier to interpret.

#### **2. Autocovariance and Autocorrelation Functions**

- **Autocovariance Coefficient** \( c_k \):
  \[
  c_k = \frac{1}{N} \sum_{t=1}^{N-k} (x_t - \bar{x})(x_{t+k} - \bar{x})
  \]
  is the measure of the covariance between the values of the series at times \( t \) and \( t+k \).

- **Autocorrelation Coefficient** \( r_k \) normalizes \( c_k \) by dividing it by the variance of the series:
  \[
  r_k = \frac{c_k}{c_0}
  \]
  Where:
  - \( c_0 \) is the autocovariance at lag \( 0 \), which is the **variance** of the series:
    \[
    c_0 = \frac{1}{N} \sum_{t=1}^{N} (x_t - \bar{x})^2
    \]

#### **3. ACF (Autocorrelation Function) Routine**

- In practice, the **acf()** function in statistical software (such as R or Python) computes and plots the autocorrelation coefficients for different lags. This plot is called a **Correlogram** and helps visualize how the values of a time series relate to each other at various time intervals (lags).

- The **Correlogram** typically shows \( r_k \) for different values of \( k \), starting at \( r_0 = 1 \), since the autocorrelation at lag 0 (comparing the series with itself at the same point) is always 1:
  \[
  r_0 = \frac{c_0}{c_0} = 1
  \]
  - The plot will typically start at 1, and as the lag increases, \( r_k \) usually decreases as the values become less correlated.

### Autocorrelation Function (ACF)

The Autocorrelation Function (ACF) measures the correlation between a time series and its lagged versions. It is a crucial tool in time series analysis for identifying patterns, such as trends and seasonality.

I. **Definition**:

For a given time series \( X = \{X_t\}_{t=1}^T \), the autocorrelation function at lag \( k \) is defined as:

\[ \rho_k = \frac{\gamma_k}{\gamma_0} \]

where:

- \( \gamma_k \) is the autocovariance at lag \( k \).
- \( \gamma_0 \) is the variance of the series.

II. **Autocovariance**:

The autocovariance at lag \( k \) is given by:

\[ \gamma_k = \text{Cov}(X_t, X_{t+k}) = \mathbb{E}[(X_t - \mu)(X_{t+k} - \mu)] \]

where \( \mu \) is the mean of the series.

III. **Autocorrelation**:

The autocorrelation at lag \( k \) normalizes the autocovariance by the variance:

\[ \rho_k = \frac{\mathbb{E}[(X_t - \mu)(X_{t+k} - \mu)]}{\mathbb{E}[(X_t - \mu)^2]} \]

### Partial Autocorrelation Function (PACF)

The Partial Autocorrelation Function (PACF) measures the correlation between the time series and its lagged versions, after removing the effects of the intermediate lags.

I. **Definition**: For a given time series \( X = \{X_t\}_{t=1}^T \), the partial autocorrelation at lag \( k \), denoted by \( \phi_{kk} \), is the autocorrelation between \( X_t \) and \( X_{t+k} \) after removing the linear effects of \( X_{t+1}, X_{t+2}, \ldots, X_{t+k-1} \).

II. **Yule-Walker Equations**:

The partial autocorrelations are the solutions to the Yule-Walker equations for an autoregressive process of order \( p \) (AR(p)):

\[ \gamma_k = \sum_{j=1}^p \phi_{pj} \gamma_{k-j} \]

where \( \phi_{pj} \) are the partial autocorrelation coefficients.

**PACF Calculation**:
The PACF at lag \( k \) can be calculated using the following recursive relationship:

1. \( \phi_{11} = \rho_1 \)
2. For \( k \geq 2 \):
   
\[ \phi_{kk} = \frac{\rho_k - \sum_{j=1}^{k-1} \phi_{k-1,j} \rho_{k-j}}{1 - \sum_{j=1}^{k-1} \phi_{k-1,j} \rho_j} \]

3. The coefficients \( \phi_{kj} \) for \( j < k \) are updated as:

\[ \phi_{kj} = \phi_{k-1,j} - \phi_{kk} \phi_{k-1,k-j} \]

**Interpreting ACF and PACF**:
- **ACF**:
  - Peaks at lag 1 indicate a strong correlation with the first lag.
  - Gradual decay suggests a trend in the data.
  - Seasonal patterns are indicated by repeated peaks at regular intervals.
- **PACF**:
  - Significant spikes indicate the number of AR terms needed to model the time series.
  - If the PACF cuts off after a few lags, it suggests an autoregressive process.
  - The number of significant spikes in the PACF indicates the order of the AR process (AR(p)).

### Example of ACF and PACF for AR(1) Process

Consider an autoregressive process of order 1 (AR(1)):

\[ X_t = \phi X_{t-1} + \epsilon_t \]

where \( \epsilon_t \) is white noise.

I. **ACF**:

- The autocorrelation function for AR(1) is given by:
  \[ \rho_k = \phi^k \]
- This shows an exponential decay in the ACF plot.

II. **PACF**:

- The partial autocorrelation function for AR(1) shows a significant spike at lag 1 and zero thereafter.
- This is because, for an AR(1) process, only the first lag has a direct effect on the series, while the higher lags' effects are indirect.

### Example plot

![c20f0056-8024-4e6d-a91b-3202c158da64](https://github.com/djeada/Statistics-Notes/assets/37275728/1154a4f5-6105-452a-a5fa-30399f43094b)

**Observation on ACF Plot**

- The ACF plot shows a significant correlation at lag 1, which gradually decreases as the lag increases.
- The correlations remain positive and significant up to around lag 20, indicating a strong trend in the data.
- The seasonal component is evident from the sinusoidal pattern in the ACF plot, reflecting the periodic nature of the time series.
- The shaded area represents the confidence interval. If the bars cross the confidence bounds, those lags are significantly correlated.

**Observation on PACF Plot**

- The PACF plot shows a significant spike at lag 1, indicating that the first lag has a strong partial correlation with the time series.
- Subsequent lags show much smaller correlations, with most falling within the confidence interval bounds, suggesting that once the effect of lag 1 is accounted for, the additional lags do not contribute much additional explanatory power.
- The lack of significant partial autocorrelations beyond lag 1 indicates that the time series may be well-modeled by an autoregressive process of order 1 (AR(1)).
