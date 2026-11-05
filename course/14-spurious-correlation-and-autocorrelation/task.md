# Task: spurious correlation and autocorrelation

## Scenario

Your growth team has found what it calls a "leading indicator": a market index published by a partner seems to move together with
the number of daily website sessions. The team wants to put the index on the weekly KPI dashboard and base the traffic forecast
on it. Before that happens, you are asked whether the relationship is real. A second metric, orders, is also available.

## Data

`data.csv` - 250 consecutive days from 2025-01-01, one row per day.

| column | meaning |
|---|---|
| `date` | calendar day |
| `sessions_k` | website sessions that day, thousands |
| `stock_index` | closing value of the partner's market index (index points) |
| `orders_k` | orders placed that day, thousands |

## Questions

Work in a spreadsheet (import `data.csv`), then compare with `solution.xlsx`.

1. Correlate `sessions_k` with `stock_index` (levels): report `CORREL`, R-squared and the slope of sessions on the index.
2. Compute the naive t-statistic $t = r\sqrt{(n-2)/(1-r^2)}$. What would you conclude if you believed the days were independent?
3. Create day-to-day changes for all three columns (`=B3-B2`, ...). What is the correlation of the changes of sessions and the index?
4. Compute the autocorrelation at lags 1, 2, 5, 10, 20 for the **levels** of sessions and for the **changes** of sessions, using
   $r_k = \sum (x_t-\bar x)(x_{t-k}-\bar x) / \sum (x_t-\bar x)^2$. Compare with the band $\pm 2/\sqrt n$.
5. Compute the residuals of the regression in question 1 and their Durbin-Watson statistic `SUMXMY2(...)/SUMSQ(...)`. Do the same
   for the regression of the changes. How do the two compare with 2?
6. Estimate the effective sample size $n(1-r_x r_y)/(1+r_x r_y)$ from the lag-1 autocorrelations of both series, then the smallest
   $|r|$ that would be significant at 5% with that many degrees of freedom. Is the observed correlation of levels informative?
7. Repeat questions 1 and 3 for `orders_k` against `sessions_k`. What is different?
8. *Explain in two or three sentences* which of the two relationships you would put on a dashboard, and what further evidence
   you would want.

## Grafana

Import `grafana/dashboard.json` (see `../grafana/README.md`; no data-source setup is needed).

- In "Rolling 60-day correlation, sessions vs stock", describe how stable the correlation of levels is compared with that of changes.
- In "Daily changes scatter", which of the two series shows a pattern against `d_sessions`?
- In "Autocorrelation of sessions", how long does the memory of the levels last compared with that of the changes?

## Deliverable

A short note (5-8 lines) to the growth team: is the index a usable leading indicator, what you checked, which numbers
support your answer, and what you recommend instead. Include one chart.
