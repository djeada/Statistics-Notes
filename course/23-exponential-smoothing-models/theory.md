# Theory: exponential smoothing models

## Why smoothing instead of a fixed regression

A regression on time ([lesson 22](../22-trend-and-seasonal-regression-forecasting/theory.md)) gives every observation the same
weight and assumes the level, slope and seasonal pattern never change. A **moving average** forgets abruptly. **Exponential
smoothing** keeps a small *state* (level, trend, seasonal indices) that is updated by one line per new observation, so recent
data counts more than old data and the forecast adapts when the business changes. The price is that you must choose how fast to
adapt: the smoothing parameters. This lesson builds the three standard models by hand as row-by-row recursions.

## Simple exponential smoothing (SES)

State: the level $\ell_t$. Forecast and update, with $0<\alpha<1$:

$$
\hat y_{t+1\mid t} = \ell_t, \qquad \ell_t = \alpha\, y_t + (1-\alpha)\,\ell_{t-1}.
$$

Unrolling the recursion shows $\ell_t = \sum_{k\ge 0} \alpha(1-\alpha)^k\, y_{t-k}$ plus a fading contribution of the start value:
weights **decay geometrically** and sum to 1. The weight on the observation $k$ days back is $\alpha(1-\alpha)^k$; the effective
memory is about $1/\alpha$ observations. A step in the level is $90\%$ absorbed after $\ln 0.1/\ln(1-\alpha)$ periods
(6.5 days for $\alpha=0.3$). SES forecasts a **flat line** for every horizon: it cannot represent trend or seasonality.

## Holt's linear trend

Add a slope state $b_t$ with weight $\beta$:

$$
\ell_t = \alpha y_t + (1-\alpha)(\ell_{t-1}+b_{t-1}),\qquad
b_t = \beta(\ell_t-\ell_{t-1}) + (1-\beta)\,b_{t-1},\qquad
\hat y_{t+h\mid t} = \ell_t + h\,b_t .
$$

## Holt-Winters, additive seasonality (period $m=7$)

$$
\hat y_{t+1\mid t} = \ell_t + b_t + s_{t+1-m},\qquad
\ell_t = \alpha(y_t - s_{t-m}) + (1-\alpha)(\ell_{t-1}+b_{t-1}),
$$
$$
b_t = \beta(\ell_t-\ell_{t-1}) + (1-\beta)b_{t-1},\qquad
s_t = \gamma\,(y_t-\ell_{t-1}-b_{t-1}) + (1-\gamma)\,s_{t-m}.
$$

For a horizon of $h$ days the seasonal index is the last estimate for that weekday:
$\hat y_{t+h\mid t} = \ell_t + h\,b_t + s_{t+h-m\lceil h/m\rceil}$. Use the *multiplicative* form
($s$ multiplies instead of adds) when the weekly swing grows with the level.

## Initial values and parameters

The recursion needs starting states. A simple, transparent choice, used here, takes them from the first two weeks:
$\ell_7=\bar y_{1..7}$, $b_7=(\bar y_{8..14}-\bar y_{1..7})/7$ and $s_i=y_i-\ell_7$ for $i=1..7$. Parameters are normally
chosen to minimise the one-step **sum of squared errors** $\text{SSE}=\sum_t (y_t-\hat y_{t\mid t-1})^2$. This course keeps them fixed
in yellow cells so you can see their effect; a grid search over 0.01 steps (done in Python, the optimum is printed in the
workbook) finds the same optimum a solver would.

**Worked example (SES, $\alpha=0.4$, start $\ell_0=100$)** for $y=(110,104,98,120)$:
$\ell_1 = 0.4\cdot110+0.6\cdot100=104.0$; the forecast for $t=2$ is $104.0$ and its error is $104-104.0=0.0$.
$\ell_2=0.4\cdot104+0.6\cdot104.0=104.0$; forecast for $t=3$ is $104.0$ (error $-6.0$). $\ell_3 = 0.4\cdot98+0.6\cdot104=101.6$;
forecast for $t=4$ is $101.6$ (error $+18.4$). The level moves only 40% of the way towards each surprise, so a single odd day
does not rewrite the forecast.

## What the parameters mean in practice

- **Large $\alpha$**: the level follows the data closely (short memory); good after structural changes, but weekday noise leaks into
  the level. **Small $\alpha$**: stable, slow to react. With a weekly pattern *outside* the model the SSE-optimal $\alpha$ is small
  because averaging the ripple is more valuable than speed.
- **$\beta$ near 0**: the slope is nearly constant after initialisation, so it inherits the noise of the initial estimate.
- **$\gamma$ near 0**: the seasonal pattern is frozen at its initial shape; large values let the pattern drift with the data.

## Pitfalls

1. **Optimising and judging on the same rows.** The training SSE always favours the richest model; use a holdout ([lesson 24](../24-backtesting-and-forecast-accuracy/theory.md)).
2. **Flat or straight-line forecasts at long horizons.** SES ignores a trend, Holt extrapolates it forever (damped trend variants shrink it).
3. **Noisy initial states** from a short start-up window, particularly the trend.
4. **Wrong seasonality form** (additive vs multiplicative) or a changing period (holidays, month-end).
5. **A one-step SSE is not a multi-step error.** The 28-day holdout uses states frozen at the end of training and is much harder.
6. **Parameters at the boundary** (0 or 1) usually signal a mis-specified model, not a precise one.

## Related notes

- [Moving averages and exponential smoothing](../08-moving-averages-and-exponential-smoothing/theory.md)
- [Trend, seasonality and noise](../07-trend-seasonality-and-noise/theory.md)
- [Naive and seasonal naive forecasts](../21-naive-and-seasonal-naive-forecasts/theory.md)
- [Backtesting and forecast accuracy](../24-backtesting-and-forecast-accuracy/theory.md)
- Repo notes: [forecasting](../../notes/time_series/forecasting.md), [seasonality and trends](../../notes/time_series/seasonality_and_trends.md)
