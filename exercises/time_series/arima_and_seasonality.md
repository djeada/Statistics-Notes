# ARIMA and Seasonality

Read [the backshift operator](../../notes/time_series/backward_shift_operator.md), [ARIMA models](../../notes/time_series/arima_models.md), and [seasonality and trends](../../notes/time_series/seasonality_and_trends.md).

1. For $y=(120,123,126,130)$, calculate the first differences. Which level information is removed?
2. For monthly observations with $y_{t-12}=92$ and $y_t=100$, calculate the seasonal difference. Write the operator form.
3. Expand $(1-B)^2y_t$ and evaluate it for $(y_{t-2},y_{t-1},y_t)=(13,12,15)$.
4. A quarterly additive seasonal pattern is $(-3,1,4,-2)$. Check its normalization and calculate the deterministic value at $t=5$ when the level is $50+2t$.
5. Explain when an additive decomposition is more appropriate than a multiplicative decomposition. Use a plot or a small simulated example.
6. A differenced series has an ACF that still decays slowly. Give three possible explanations and a next diagnostic for each.
7. Write the full model equation for ARIMA$(1,1,1)$ and SARIMA$(0,1,1)(0,1,1)_{12}$ using the backshift operator.
8. Explain why differencing twice can make a series harder to model even when it reduces the apparent trend.

## Checks

- First differences are $(3,3,4)$.
- The seasonal difference is $100-92=8$, written $(1-B^{12})y_t$.
- $(1-B)^2y_t=y_t-2y_{t-1}+y_{t-2}=4$ for the supplied values.
- The seasonal indices sum to zero, and the deterministic value at $t=5$ is $60-3=57$.
