# Task: backtesting and forecast accuracy

## Scenario

Hearthside's operations team must pick a method for the **weekly staffing forecast**: every Sunday evening they forecast the
next seven days of orders. Three candidate rules exist, and a colleague who tested them on "the last month" says the
4-week weekday average wins clearly. You are asked to check that claim with a proper backtest before the rule is adopted.

## Data

`data.csv` - 336 consecutive days, 2025-01-06 (Monday) to 2025-12-07, one row per day.

| column | meaning |
|---|---|
| `date` | calendar day |
| `orders` | orders placed that day |

**Forecast rules** (all use only data up to the forecast origin T, a Sunday evening; target day t = T+h, h = 1..7):

- *Naive*: every day equals the last observed day (y at T).
- *Seasonal naive*: y at t-7.
- *Weekday mean (4 wk)*: the average of the same weekday over the 4 most recent weeks (t-7, t-14, t-21, t-28).
- *Weekday mean (all history)*: the average of the same weekday over **all** days up to T.

**Origins:** T = 84, 91, ..., 329 (36 weekly origins, 252 forecasts, first origin has 12 weeks of history).

## Questions

Work in a spreadsheet (import `data.csv`), then compare with `solution.xlsx`.

1. Add day index `t` and weekday columns. For each day t = 85..336 find its origin T = 84 + 7*INT((t-85)/7) and horizon h = t - T.
   How many origins and forecasts are there?
2. Build the four forecast columns using only data up to the origin. Compute MAE, RMSE and bias for each rule over all 252 forecasts.
3. Compute MAPE, sMAPE and MASE (scale = mean |y[t] - y[t-7]| over t = 8..84). Which rules have MASE below 1?
4. Compute the MAE of each origin (7 days) for every rule and, for each origin, the best rule. Count how often each rule wins.
5. Suppose you had evaluated only the last 28 days (the last 4 origins). Compute each rule's MAE there and rank the rules; compare with the ranking over all origins.
6. For the seasonal naive, report the lowest and highest per-origin MAE and their ratio.
7. Build a "calibrated" forecast: the mean orders of the target week (Mon-Sun, i.e. the week that follows the origin) plus the average deviation of that
   weekday from its own week mean, computed over all 252 days. Compare its MAE with the plain seasonal naive. Why can this number never be produced on a Sunday evening?
8. Compute the MAE of the weekday mean for windows of 1, 2, 4, 6, 8 and 12 weeks. Which window is best?
9. *Explain in 3-4 sentences* which rule you recommend, how confident you are, and why 252 forecasts are fewer independent observations than they look.

## Grafana

Import `grafana/dashboard.json` (see `../grafana/README.md`; no data-source setup is needed).

- In "MAE of each weekly forecast origin", which weeks hurt every method, and what happens in the last weeks?
- In "MAE: all 36 origins vs the last 4 only", does the ranking agree with your answers to questions 2 and 5?
- In "Leakage: honest vs calibrated", how much better does the peeking forecast look, and why?

## Deliverable

A one-page note: *which weekly rule should operations adopt?* Include the metric table, the per-origin chart, a sentence on
why the colleague's "last month" test misled, and one sentence on how you would keep monitoring the chosen rule after launch.
