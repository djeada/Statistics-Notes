# Time Series Extensions Flashcards

<details>
<summary>What is weak white noise?</summary><br>
A zero-mean process with constant variance and zero autocovariance at every nonzero lag. It need not be independent unless independence is assumed separately.
</details>

<details>
<summary>Why should time-series cross-validation preserve temporal order?</summary><br>
Because training on observations that occur after the validation target leaks future information and produces an unrealistically optimistic estimate of forecast performance.
</details>

<details>
<summary>What is rolling-origin evaluation?</summary><br>
Repeatedly refit or update a forecasting procedure at successive historical forecast origins and score predictions only on observations that occur after each origin.
</details>

<details>
<summary>Why is MASE useful?</summary><br>
It scales forecast errors by a naive in-sample error, is comparable across series with different units, and remains defined when actual observations are zero.
</details>

<details>
<summary>What is dynamic regression?</summary><br>
A regression model with external predictors plus time-series dynamics, often represented by ARMA/ARIMA errors or lagged predictor effects.
</details>

<details>
<summary>What does Granger causality mean?</summary><br>
Past values of one variable add predictive information for another conditional on the included history. It is not by itself evidence of intervention or structural causality.
</details>

<details>
<summary>What is cointegration?</summary><br>
A set of non-stationary variables is cointegrated when some nontrivial linear combination of them is stationary, indicating a stable long-run relationship.
</details>

<details>
<summary>Why use a VECM?</summary><br>
A VECM models short-run changes while preserving cointegrating long-run equilibrium relationships among integrated variables.
</details>

<details>
<summary>What is the distinction between Kalman filtering and smoothing?</summary><br>
Filtering estimates the current state using observations available up to the current time. Smoothing estimates past states using the full dataset, including later observations.
</details>

<details>
<summary>What does a periodogram show?</summary><br>
It estimates how a finite sample's variability is distributed across Fourier frequencies. Peaks can indicate prominent periodic components.
</details>

<details>
<summary>What is aliasing?</summary><br>
When sampling is too slow to distinguish a high-frequency signal, that signal appears at a different lower frequency in the sampled data.
</details>
