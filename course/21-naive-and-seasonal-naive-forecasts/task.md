# Task: can we beat "same as last week"?

## Scenario

A bakery chain plans next month's baking volumes for one shop. The analyst proposes an elaborate model, but the operations manager asks a blunt question: **"does it beat
copying what we sold last week?"** You have 20 weeks of daily sales. Treat the first 16 weeks (112 days) as history and the last 4 weeks (28 days) as the
holdout. Build the benchmark forecasts, score them, and decide which baseline any new model must beat.

## Data

`data.csv` - 140 rows, one per day, 2026-01-05 (Monday) to 2026-05-24.

| column | meaning |
|---|---|
| `date` | calendar day |
| `loaves_sold` | loaves sold that day (units) |

Rows 1-112 are the training history (up to 2026-04-26); rows 113-140 are the holdout (2026-04-27 to 2026-05-24).

## Questions

1. Compute the mean daily sales in the training period and in the holdout. Compute the mean by weekday (Monday-Sunday) in the training period.
2. Forecast all 28 holdout days with the **mean** of the training data. Compute MAE, RMSE and MAPE.
3. Forecast the holdout with the **naive** method (the last training value, repeated). Compute MAE, RMSE, MAPE. Why is the result so poor?
4. Forecast the holdout with **seasonal naive** (same weekday, last observed week). Compute MAE, RMSE, MAPE. Add the **drift** forecast and compare all four.
5. Compute the skill of seasonal naive against naive and against the mean forecast: $1 - \text{MAE}_{snaive}/\text{MAE}_{other}$.
6. Compute the MASE of each method, using the in-sample mean of $|y_t - y_{t-7}|$ over the training period as the scale. What does a value above 1 mean?
7. Now forecast each holdout day **one step ahead** with naive (yesterday) and seasonal naive (7 days ago). Compare MAE with the 28-day-ahead versions.
8. Compute the seasonal naive absolute error by weekday. Which weekday is worst, and what in the training data explains it? Recompute the MAE without that weekday.
9. Compute the mean error (actual - forecast) of each method. Which are biased high and which low?
10. *Interpretation:* which benchmark should a new model have to beat, what would you change in the seasonal naive forecast, and what is one limitation of judging on a single 28-day holdout?

## Grafana

Import `grafana/dashboard.json` (see `../grafana/README.md`; no data-source setup is needed).

- In "Sales and benchmark forecasts", which dashed line follows the weekly pattern and which ones are flat or straight lines?
- In "Holdout errors", which days stand out and what do they have in common?
- In "Weekday profile", compare the training and holdout bars: what do they say about a forecast built from last week alone?

## Deliverable

A short note (5-8 lines) with named parts: **Benchmarks** (table of MAE/RMSE/MAPE), **Winner** (and by how much), **Weak spot** (the failing weekday and why), **Next step**
(what a model must beat). Include a chart of actual sales and the forecasts over the holdout.
