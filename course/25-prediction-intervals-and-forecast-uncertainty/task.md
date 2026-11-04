# Task: prediction intervals and forecast uncertainty

## Scenario

Operations plans packing capacity from Hearthside's order forecast, which is simply "the same weekday last week" (the seasonal
naive rule). They now ask for a **range**: *"give us a number we can staff for with 95% confidence, one to four weeks ahead."*
You will build the ranges from the method's own past errors and then test whether a nominal 80% / 95% range really contains
that share of future days.

## Data

`data.csv` - 350 consecutive days, 2025-01-06 (Monday) to 2025-12-20, one row per day.

| column | meaning |
|---|---|
| `date` | calendar day |
| `orders` | orders placed that day |

The forecast for day t made k weeks earlier is `orders[t - 7k]` (k = 1, 2, 3, 4), so its error is `e_k(t) = orders[t] - orders[t - 7k]`.
**Calibration period: t <= 224** (first 32 weeks). **Evaluation: t > 224** (the last 126 days). Put 224 and the two confidence
levels (80%, 95%) in input cells.

## Questions

Work in a spreadsheet (import `data.csv`), then compare with `solution.xlsx`.

1. Build the four error columns e_1..e_4. Compute the mean and SD of each over the calibration period. How does the SD change with k?
2. Compare SD(k) with the random-walk rule SD(1) * sqrt(k). Which is larger at k = 4, and why?
3. Build normal intervals (forecast +/- z * SD(k)) for 80% and 95%. Report the 95% half-widths for k = 1..4.
4. Build empirical intervals from the 10%/90% and 2.5%/97.5% percentiles of the calibration errors (`PERCENTILE`). How do they differ from the normal ones?
5. For each horizon, compute the share of calibration-period days whose error lies inside each of the four intervals (normal/empirical x 80%/95%).
6. Repeat on the evaluation days (t > 224). Which intervals under-cover, by how much, and is the shortfall larger than the binomial standard error?
7. Compute the RMS error after t = 224 relative to the calibration SD, and the SD of the 1-week error in consecutive 28-day blocks. What happened?
8. Produce the 28-day forecast after the last observation with 80% and 95% bounds (use the SD of all errors at each k). How much wider is the interval at h = 28 than at h = 1?
9. *Explain in 3-4 sentences* what you would change before sending 95% ranges to operations.

## Grafana

Import `grafana/dashboard.json` (see `../grafana/README.md`; no data-source setup is needed).

- In "Orders (last 16 weeks) and the 28-day forecast fan", where does the band step wider, and does it look wide enough compared with the recent day-to-day swings?
- In "95% coverage by horizon", compare the calibration and evaluation bars. Which intervals are closest to the nominal level?
- In "Volatility of the 1-week error (28-day blocks)", in which blocks does the volatility change?

## Deliverable

A short note (6-8 lines): *what range do you give operations, how often will it fail, and why?* Include the coverage table (calibration vs
evaluation), the fan chart, and one sentence on how you would keep the intervals honest as new data arrive.
