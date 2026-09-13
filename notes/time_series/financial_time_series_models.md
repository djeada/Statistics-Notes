# Financial Time Series Models

## Worked calculation: returns and conditional variance

If a price rises from $P_{t-1}=100$ to $P_t=102$, the log return is

$$
r_t=\log(102)-\log(100)=\log(1.02)\approx0.01980.
$$

For a GARCH-style variance recursion with $\alpha_0=0.01$, $\alpha_1=0.10$, $\beta_1=0.85$, previous return $r_{t-1}=0.2$, and previous variance $h_{t-1}=0.04$,

$$
h_t=0.01+0.10(0.2^2)+0.85(0.04)
=0.048.
$$

The conditional standard deviation is $\sqrt{0.048}\approx0.219$. The squared previous return contributes a shock effect, while the previous variance carries persistence. This is why raw returns may have little autocorrelation while squared returns remain dependent.

![Synthetic volatility clustering](../../assets/time_series/student/20_financial_volatility.png)

Financial series (prices, returns, exchange rates) often look very different from the classical stationary Gaussian assumptions. Common features include:

- **Heavy tails** (extreme events occur more often than normal theory predicts).
- **Asymmetry** (returns can be skewed).
- **Volatility clustering** (large moves tend to follow large moves).
- **Serial dependence in variance**, even when raw returns have weak autocorrelation.

### Log Returns

If $P_t$ is the price at time $t$, the **log return** is:

$$
Z_t = \log(P_t) - \log(P_{t-1})
$$

Working with returns instead of prices often produces a more stable series for modeling.

### ARCH and GARCH

ARCH-type models describe changing variance over time by making variance depend on past shocks.

**ARCH($p$):**

$$
Z_t = \sqrt{h_t} \, \epsilon_t, \quad \epsilon_t \sim IID\,N(0,1)
$$

$$
h_t = \alpha_0 + \sum_{i=1}^{p} \alpha_i Z_{t-i}^2
$$

**GARCH($p, q$):**

$$
h_t = \alpha_0 + \sum_{i=1}^{p} \alpha_i Z_{t-i}^2 + \sum_{j=1}^{q} \beta_j h_{t-j}
$$

with $\alpha_0 > 0$ and $\alpha_i, \beta_j \ge 0$.

### Synthetic Volatility Example

The plot below shows a synthetic series with volatility clustering and the corresponding conditional volatility.

![garch volatility](../../assets/time_series/garch_volatility.png)

These models are foundational for risk management, option pricing, and measuring time-varying uncertainty in financial markets.

## Student guide: separate the price, return, and volatility questions

Financial time series are often modeled in layers:

1. choose a price or return representation;
2. specify the conditional mean;
3. specify the conditional variance;
4. choose an innovation distribution;
5. evaluate forecasts of returns and risk with time-respecting backtests.

A model that describes the mean well can still produce poor risk intervals if it leaves volatility clustering or heavy tails in the residuals.

### Price levels and log returns

For a positive price $P_t$,

$$
r_t=\log(P_t)-\log(P_{t-1})
=\log\left(\frac{P_t}{P_{t-1}}\right).
$$

If $P_{t-1}=100$ and $P_t=102$, then

$$
r_t=\log(1.02)\approx0.01980.
$$

The simple return is $102/100-1=0.02$. For small changes, the two are close:

$$
\log(1+r)\approx r.
$$

Log returns add over time:

$$
\log(P_{t+h}/P_t)=\sum_{j=1}^{h}r_{t+j}.
$$

This makes them convenient for aggregation. It does not make returns independent, Gaussian, or stationary automatically.

### Conditional mean and variance

A useful separation is

$$
r_t=\mu_t+\sqrt{h_t}\,z_t,
\qquad
E(z_t)=0,\quad \operatorname{Var}(z_t)=1.
$$

The conditional mean $\mu_t$ describes expected return given the information set; $h_t$ describes conditional variance. Even when $\mu_t$ is constant or zero, $h_t$ can change over time.

### ARCH calculation

An ARCH($p$) model uses recent squared shocks:

$$
h_t=\alpha_0+\sum_{i=1}^{p}\alpha_i r_{t-i}^2.
$$

For ARCH(1) with $\alpha_0=0.02$, $\alpha_1=0.35$, and $r_{t-1}=0.4$,

$$
h_t=0.02+0.35(0.4^2)=0.076.
$$

The conditional standard deviation is $\sqrt{0.076}\approx0.276$. A large shock raises next-period risk even if its sign has no effect.

Nonnegative parameters ensure nonnegative variance. For a stable finite unconditional variance in ARCH(1), $\alpha_1<1$.

### GARCH calculation

GARCH(1,1) extends the recursion:

$$
h_t=\alpha_0+\alpha_1r_{t-1}^2+\beta_1h_{t-1}.
$$

With $\alpha_0=0.01$, $\alpha_1=0.10$, $\beta_1=0.85$, $r_{t-1}=0.2$, and $h_{t-1}=0.04$:

$$
h_t=0.01+0.10(0.2^2)+0.85(0.04)=0.048.
$$

The persistence parameter is $\alpha_1+\beta_1=0.95$. The unconditional variance, when the sum is below 1, is

$$
\bar h=\frac{\alpha_0}{1-\alpha_1-\beta_1}
=\frac{0.01}{0.05}=0.2.
$$

High persistence means a volatility shock can affect many future risk forecasts. A value close to 1 can also make parameter estimates and long-horizon forecasts sensitive to the sample period.

### Why squared returns matter

A volatility process can have

$$
\operatorname{Corr}(r_t,r_{t-1})\approx0
$$

while

$$
\operatorname{Corr}(r_t^2,r_{t-1}^2)>0.
$$

The sign of a shock may be unpredictable even when its magnitude is persistent. Inspect both the return ACF and squared-return ACF before concluding that returns are unstructured.

### Asymmetric volatility

Some markets respond differently to negative and positive returns. An asymmetric recursion can include an indicator:

$$
h_t=\alpha_0+\alpha r_{t-1}^2
\,+\gamma\mathbf 1(r_{t-1}<0)r_{t-1}^2
\,+\beta h_{t-1}.
$$

If $\gamma>0$, a negative shock of a given magnitude raises variance more than a positive shock. The sign convention and leverage interpretation depend on the conditional mean and return definition.

### Innovation distributions

Normal innovations make likelihood calculations simple, but financial returns often have heavy tails. A Student-$t$ innovation can assign more probability to extremes. Compare:

$$
P(|Z|>3)
$$

under the fitted distribution, not only the center of a histogram. A model can match volatility clustering while still understating tail risk if the innovation distribution is too light-tailed.

### Risk forecasts

For a one-step return forecast with conditional standard deviation $\sqrt{h_{t+1}}$, a Gaussian lower quantile at level $\alpha$ is

$$
q_{\alpha,t+1}=\mu_{t+1}+z_\alpha\sqrt{h_{t+1}}.
$$

Value-at-Risk asks for a quantile; expected shortfall averages losses beyond that quantile. Both require backtesting and a clearly stated loss sign. A 99% interval is not validated by observing only whether a few points fall inside it.

### Modeling cautions

- Prices are usually non-stationary; returns may be closer to stationary but can have breaks.
- Trading calendars create missing or irregular time points.
- Volatility can change after market-wide events.
- High-frequency returns can contain microstructure effects.
- Using revised or survivorship-biased price data can make a backtest unrealistic.
- Parameters estimated over a calm period may not describe a crisis period.

Fit and evaluate on chronological data. If a risk forecast is updated daily, reproduce the daily information set and record the forecast horizon.

### Workflow

1. Check prices, corporate actions, units, and missing trading days.
2. Convert prices to returns when the model concerns relative change.
3. Plot returns, absolute returns, and squared returns.
4. Fit a mean model before interpreting variance residuals.
5. Fit ARCH/GARCH or an asymmetric/heavy-tailed extension when diagnostics justify it.
6. Check standardized residuals and squared standardized residuals.
7. Backtest volatility forecasts and tail quantiles.
8. Examine stability across regimes and sensitivity to the innovation distribution.

### Visual companions

Run [financial_time_series_visualizations.py](../../scripts/time_series/financial_time_series_visualizations.py):

![Prices and returns](../../assets/time_series/financial/01_prices_and_returns.png)

![ARCH variance](../../assets/time_series/financial/02_arch_variance.png)

![GARCH persistence](../../assets/time_series/financial/03_garch_persistence.png)

![Returns versus squared returns](../../assets/time_series/financial/04_returns_vs_squared_returns.png)

![Volatility shock response](../../assets/time_series/financial/05_volatility_shock_response.png)

![Leverage effect](../../assets/time_series/financial/06_leverage_effect.png)

![Heavy tails](../../assets/time_series/financial/07_heavy_tails.png)

![Price and log price](../../assets/time_series/financial/08_price_and_log_price.png)
