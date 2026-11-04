# Theory: differencing and growth rates

## Why look at changes instead of levels

A revenue curve that climbs for six years looks like a story but is a poor object for statistics: its mean depends on
*when* you look, its swings grow with its size, and each value is almost determined by the previous one. Averages,
correlations and control limits computed on such a **level** series are unreliable. The remedy is to model the *change*
from one period to the next, in the form that makes the change comparable across time: a difference, a percent change or
a log return. This is also how growth is reported - "up 18 % on last year" is a seasonal percent change.

## The transformations

For a positive series $x_t$:

| name | formula | use |
|---|---|---|
| first difference | $\Delta x_t = x_t - x_{t-1}$ | absolute change; removes a *linear* trend |
| simple (percent) change | $r_t = x_t/x_{t-1} - 1$ | relative change; what people quote |
| log return | $g_t = \ln(x_t/x_{t-1}) = \ln(1+r_t)$ | relative change that **adds up** over time |
| seasonal difference | $x_t - x_{t-m}$ | change from the same period last cycle ($m=12$ for months) |
| year-over-year growth | $x_t/x_{t-12}-1$ | seasonal percent change |

**Simple vs log.** For small changes $\ln(1+r) \approx r$ ($r = 0.02$ gives $0.0198$), but for large changes they differ:
a $-25\,\%$ month has $g = \ln 0.75 = -0.288$. Log returns are **additive** over time,
$\sum_{t=1}^{n} g_t = \ln(x_n/x_0)$, and symmetric ($+x$ then $-x$ in logs returns to the start). Simple returns compound
multiplicatively: $+50\,\%$ followed by $-50\,\%$ is $1.5 \times 0.5 - 1 = -25\,\%$, not $0$. Use simple changes to
communicate, log returns to compute with.

## Compound annual growth rate

$$
\mathrm{CAGR} = \left(\frac{x_n}{x_0}\right)^{\frac{12}{n}} - 1 \quad (n \text{ months between first and last observation}),
$$

and because the log returns telescope, $\mathrm{CAGR} = \exp\bigl(12\,\bar g\bigr) - 1$ where $\bar g$ is the mean monthly log
return. The shortcut $(1+\bar r)^{12}-1$ built from the *arithmetic* mean percent change overstates compound growth (the arithmetic mean of growth
rates always exceeds the geometric mean), and the gap grows with volatility.

### Worked example (from `data.csv`)

Revenue goes from 77,473 USD to 234,818 USD over 5.92 years (71 months), a ratio of 3.031. CAGR =
$3.031^{12/71} - 1$ = 20.61%. The mean monthly log return is 0.01562, so $\exp(12 \cdot 0.01562) - 1$ = 20.61%, the same
number, while $(1+\bar r)^{12}-1$ = 22.59%. In the outage month (June 2023) revenue changed by -20.4%, i.e. a log return of -0.228; a rise of
25.6% is needed to get back to where it was.

## Differencing to make a series stationary

A **stationary** series has a mean, variance and dependence structure that do not drift
([notes](../../notes/time_series/stationarity.md)). Trends break it. Differencing is the cheapest repair:

- A linear trend plus noise becomes noise around a constant after one first difference.
- A **random walk** $x_t = x_{t-1} + e_t$ becomes plain white noise $e_t$.
- Exponential growth becomes stationary only after **taking logs first**, then differencing: $\Delta \ln x_t$.
- A seasonal pattern of period $m$ is removed by the seasonal difference $x_t - x_{t-m}$; trend and season together
  often need both (the seasonal difference of the first difference).

How to check: compare location and spread (median and IQR, which one outlier cannot distort) of the first and second half.
In `data.csv` the IQR in the last 36 months relative to the first 36 is
1.76 for the level, 2.10 for the USD difference, 1.24 for the percent change and 1.24 for the log return: only the
relative measures stay close to 1. The lag-1 autocorrelation drops from 0.987 for the level to -0.353 for the log return (negative, because every difference adds the noise of two months and the outage month enters twice).

## Assumptions and pitfalls

1. **Over-differencing.** Differencing white noise multiplies its variance by 2 and creates a lag-1 autocorrelation of
   $-0.5$. If the differenced series has a strongly negative lag-1 autocorrelation, you went too far.
2. **Information is lost.** Differences carry no level. Forecast the change and add it back
   ([lesson 22](../22-trend-and-seasonal-regression-forecasting/theory.md)).
3. **Percent change near zero or with negative values** explodes or is meaningless; use the difference instead.
4. **Seasonality survives first differencing** (see the autocorrelation at lag 12 in the workbook); use the seasonal difference
   or [decompose first](../07-trend-seasonality-and-noise/theory.md).
5. **Noise is amplified.** A difference of two noisy values has twice the noise variance; smoothing first
   ([lesson 08](../08-moving-averages-and-exponential-smoothing/theory.md)) or using longer spans reduces it.
6. **Overlapping windows.** 12-month growth computed every month shares 11 months with its neighbour, so it is strongly
   autocorrelated by construction; do not treat the points as independent.
7. **Single outliers appear twice**: a one-month dip creates a big negative change and a big positive change next month.

## Where this leads

Rolling windows of these changes are in [lesson 10](../10-rolling-statistics/theory.md); autocorrelation of a differenced
series and spurious correlation between trending series in [lesson 14](../14-spurious-correlation-and-autocorrelation/theory.md);
ARIMA formalises the "I" (integrated) as differencing ([notes](../../notes/time_series/arima_models.md),
[random walks](../../notes/time_series/random_walk.md)).
