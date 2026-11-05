# Task: exponential smoothing models

## Scenario

Hearthside (the online candle shop from lesson 22) wants a forecast that **updates itself** each morning instead of a
regression refitted by hand. In late spring a marketing campaign started and the team is unsure how quickly the forecast should
react to it. You will build simple exponential smoothing (SES), Holt's linear trend and additive Holt-Winters in a spreadsheet,
compare them, and decide which smoothing speed the business should use.

## Data

`data.csv` - 168 consecutive days starting Monday 2025-03-03, one row per day.

| column | meaning |
|---|---|
| `date` | calendar day |
| `orders` | orders placed that day |

The first **140 days are the training period** (states are updated on them); the last **28 days are the holdout** (multi-step
forecast from the final training state; no updating). Use these parameters, found by a grid search on the training SSE:
SES alpha = 0.21; Holt alpha = 0.18, beta = 0.01; Holt-Winters alpha = 0.33, beta = 0.01, gamma = 0.15. Put them in
input cells and make every recursion refer to them.

## Questions

Work in a spreadsheet (import `data.csv`), then compare with `solution.xlsx`.

1. Compute the initial level (mean of week 1) and initial trend ((mean of week 2 - mean of week 1) / 7).
2. Build SES from day 8 on (forecast for day t = level after day t-1). Report the training SSE and RMSE over days 8-140 and the 28-day forecast.
3. Repeat SES with alpha = 0.05, 0.10, 0.20, 0.40 and 0.80. Which alpha minimises the SSE? Explain why neither extreme wins.
4. Build Holt's model. Report its SSE and the forecast for day 168 (h = 28). How much does the trend term improve on SES?
5. Build additive Holt-Winters with period 7 (initial indices = week-1 values minus week-1 mean). Report its SSE and the seven
   seasonal indices after day 140.
6. Compute the SSE of the seasonal naive forecast (y[t-7]) for the same days and rank all four models by training SSE.
7. Forecast the 28 holdout days with each model (flat level; level + h*trend; level + h*trend + seasonal index) and report RMSE,
   MAE and bias. Does the holdout ranking agree with the training ranking?
8. For your SES alpha, compute the weights alpha*(1-alpha)^k for k = 0..13, their sum, and the number of days needed to absorb 90% of a level jump.
9. *Explain in 3-4 sentences* why minimising training SSE does not guarantee the best forecast, and which of the three
   parameters you trust least.

## Grafana

Import `grafana/dashboard.json` (see `../grafana/README.md`; no data-source setup is needed).

- In "Orders and forecasts", what happens to the level around late May, and how long does each model take to catch up?
- In "Holdout days 1-28", which models reproduce the weekly zig-zag and which draw a smooth line?
- In "SES: SSE for five values of alpha", read off the shape. Where would you put alpha and why?

## Deliverable

A short note (6-8 lines): *which model would you run in production, with which parameters, and what would make you retune
them?* Include the SSE / holdout RMSE comparison table and one chart of the holdout forecasts. State the biggest weakness
of your chosen model.
