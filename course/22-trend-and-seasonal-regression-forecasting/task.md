# Task: trend and seasonal regression forecasting

## Scenario

You plan staffing and stock for **Hearthside**, an online candle shop. Next month's packing capacity is booked four weeks in
advance, so the operations lead wants a **daily orders forecast for the next 28 days**. A teammate proposes the "obvious" fix
for a growing, weekly-patterned series: regress orders on time plus weekday and month dummies. You must decide whether that
beats the simple rule "next four weeks look like last week" (the seasonal naive forecast from lesson 21).

## Data

`data.csv` - 420 consecutive days, 2025-01-01 to 2026-02-24, one row per day.

| column | meaning |
|---|---|
| `date` | calendar day |
| `orders` | number of orders placed that day |

Use the **first 392 days (to 2026-01-27) as the training set** and the **last 28 days as the holdout**. Nothing from the
holdout may enter a fitted coefficient.

## Questions

Work in a spreadsheet (import `data.csv`), then compare with `solution.xlsx`.

1. Add a day index `t` and fit `orders = a + b*t` on the training days (`SLOPE`, `INTERCEPT`, `RSQ`). How many orders per day is
   the series growing by, and how much variance does the trend explain?
2. Add six weekday dummies (Monday = base) and fit trend + weekday with `LINEST`. What is the Saturday effect relative to Monday and
   what is the new $R^2$?
3. Add eleven month dummies (January = base) and fit the full model. Report $R^2$, the residual standard error, and the lowest and
   highest month relative to January.
4. Forecast the 28 holdout days with each of the three regression models. Report holdout RMSE, MAE and bias (actual - forecast)
   for each.
5. Build the seasonal naive forecast for the holdout (repeat the last training week four times) and compute the same three numbers.
   Which method wins on RMSE?
6. Compare the in-sample RMSE and the holdout RMSE of the full model. What does the gap mean?
7. Sum actual and forecast orders for each of the four holdout weeks. In which direction, and by how much, does the full model err?
8. Compute the lag-1 autocorrelation of the full model's training residuals and find the date of the largest residual.
9. *Explain in 3-4 sentences* two limitations of using this regression to plan the next four weeks.

## Grafana

Import `grafana/dashboard.json` (see `../grafana/README.md`; no data-source setup is needed).

- In "Orders, regression fit and holdout forecast", where does the red forecast leave the actual orders, and in which direction?
- Compare "Weekday effect vs Monday" and "Month effect vs January" with your coefficients from questions 2 and 3.
- In "Training residuals", what are the points flagged in red, and why can the dummies not absorb them?

## Deliverable

A short note (6-8 lines) with a recommendation: *which forecast would you give operations for the next four weeks, and
how wrong do you expect it to be?* Include the holdout RMSE table, one chart of forecast vs actual, and one statement
about what you would change before trusting the model for a longer horizon.
