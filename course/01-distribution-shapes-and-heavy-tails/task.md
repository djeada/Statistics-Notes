# Task: distribution shapes and heavy tails

## Scenario

You analyse an online shop that is preparing a revenue forecast and a delivery-time promise. The finance lead quotes
"the average order is about 60 EUR with a standard deviation of 83", and the logistics lead says "delivery takes 48 hours,
give or take 9". You are asked whether the same style of summary is appropriate for both numbers, and which figure you
would put in a plan for (a) total revenue and (b) the typical customer.

## Data

`data.csv` - 500 consecutive orders, one every 11 minutes.

| column | meaning |
|---|---|
| `order_id` | running number |
| `timestamp` | when the order was placed |
| `channel` | `web` or `app` |
| `basket_value_eur` | order value in EUR |
| `delivery_hours` | hours from order to delivery |

## Questions

Work in a spreadsheet (import `data.csv`), then compare with `solution.xlsx`. Use `STDEV.S`, `SKEW` and `KURT` (excess).

1. Compute mean, median and standard deviation of `basket_value_eur` and `delivery_hours`, and the mean/median ratio of each.
2. Compute `SKEW` and `KURT` for both columns. Which column looks normal and which does not?
3. What share of observations lies within mean $\pm$ 2 SD in each column? How many baskets exceed mean + 3 SD? Compare with the 95.4 % expected for a normal distribution.
4. What share of total revenue comes from the top 1 % and the top 10 % of orders? What share of orders is below the mean basket?
5. Add a column $\ln(\text{basket})$. Compute its `SKEW` and `KURT`, the geometric mean $e^{\overline{\ln x}}$ and compare with the median.
6. Estimate the tail index $\alpha$ of the basket value with the Hill estimator using the {k} largest orders. What does a value below 2 imply for the standard deviation?
7. Compute the mean and median of the first 50, 100, ..., 500 orders. Which of the two settles down faster?
8. Build a histogram with doubling bins (0-10, 10-20, 20-40, ..., 640-1280). *Explain in three sentences* which summary you would use for the revenue forecast and which for the "typical customer", and one limitation of the 500-order sample for tail statistics.

## Grafana

Import `grafana/dashboard.json` (no data-source setup is needed).

- Compare the two histograms of basket value. What does the linear scale hide that the log scale shows?
- In "Running mean vs running median", find the jumps of the mean. What kind of order causes each jump, and why does the median ignore them?
- In the log-log survival plot, over which range of basket values is the curve a straight line, and what is its slope?

## Deliverable

A short note (6-10 lines) titled *What is a typical order, and what drives total revenue?* with three named parts: **Shape**
(skewness, kurtosis, mean vs median), **Tail** (concentration and tail index) and **Recommendation** (which summary for
which decision). Include one chart and state one limitation.
