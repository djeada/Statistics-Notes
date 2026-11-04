# Task: linear and nonlinear regression

## Scenario

You are the marketing analyst for an online retailer. Over the last 120 weeks the weekly advertising budget has been raised
steadily, and sales have grown with it. The head of marketing wants to approve **80 k$ per week** next quarter and
asks you: "What does one more thousand dollars of advertising buy us, and what will we sell at 80 k$?" A colleague
has already fitted a straight line through the data and reports its R-squared as proof that "sales grow linearly with spend".

## Data

`data.csv` - 120 rows, one per week (2024-01-01 onwards).

| column | meaning |
|---|---|
| `week` | Monday of the week |
| `ad_spend_k` | advertising spend in that week, thousand dollars |
| `sales_units` | units sold in that week |

## Questions

Work in a spreadsheet (import `data.csv`), then compare with `solution.xlsx`.

1. Fit `sales_units = a + b * ad_spend_k` with `SLOPE`, `INTERCEPT`, `RSQ`. State the slope in words and with units.
2. Use the line to predict weekly sales at 40 k$.
3. Add a residual column (actual minus fitted). Sort or group the weeks into three equal spend ranges (lowest third, middle,
   highest third) and compute the mean residual in each. What pattern do you see?
4. Add a column `ln(ad_spend_k)` and refit `sales_units` on it. Report slope, intercept and R-squared.
5. Compare the two models with `STEYX` (residual standard error). Which one has the smaller typical miss, and by how much?
6. Fit both models on the first 96 weeks only and compute the RMSE of each on the last 24 weeks. Which model generalises?
7. Predict sales at 80 k$ with each model. Is that prediction an interpolation?
8. For the log model, how many extra units does one more k$ buy at 10 k$ and at 50 k$ per week (slope divided by spend)?
   How does that compare with the line's slope?
9. *Explain in two or three sentences* what could still be wrong with the log model when it is used to approve a budget.

## Grafana

Import `grafana/dashboard.json` (see `../grafana/README.md`; no data-source setup is needed).

- In "Sales vs ad spend with both fits", where does the straight line sit relative to the dots at low, middle and high spend?
- In "Residuals vs ad spend", which model leaves a visible pattern? What does that pattern tell you about the model's shape?
- In "Holdout weeks", what happens to the straight-line prediction as spend rises?

## Deliverable

A short note (6-8 lines) to the head of marketing with: the recommended model and why, the expected sales at 80 k$ with
a clear statement of how reliable that number is, the return on the next k$ at low and high spend, and one chart.
