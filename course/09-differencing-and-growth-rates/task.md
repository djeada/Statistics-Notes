# Task: differencing and growth rates

## Scenario

You are the finance analyst of a subscription software company. The CFO's board slide says "revenue grows about
2,200 USD more every month" and the growth plan assumes it will continue. An operations manager objects: the company
is much bigger than it was, the 'steady' monthly change cannot have stayed the same, and one month "looks like an
accident". You have monthly revenue for six years and have to compute growth correctly and decide which view of the data
is safe to use for further statistics.

## Data

`data.csv` - 72 monthly observations from 2020-01 to 2025-12; one row = one calendar month.

| column | meaning |
|---|---|
| `month` | first day of the month |
| `revenue_usd` | recognised subscription revenue in the month (USD) |

## Questions

Work in a spreadsheet (import `data.csv`), then compare with `solution.xlsx`.

1. Compute the **first difference** (USD change from the previous month). What are its mean and SD? Is the SD the same in
   the first and the second half of the data?
2. Compute the **percent change**. What are its mean and SD, which month is the worst, and what happens in the month after it?
3. Compute the **log return** $\ln(x_t/x_{t-1})$. Mean and SD? Compare the log return and the percent change in the worst month and say which
   one is symmetric.
4. Compute the **CAGR** from the first to the last month, in three ways: from the ratio, from the mean log return, and as
   compounding the mean percent change, $(1+\bar r)^{12}-1$. Which one is biased and why?
5. Compute the **seasonal difference** (lag 12) and the **year-over-year growth**. What was the growth in the last month and the
   average over the last 12 months?
6. Compare median and IQR for the first 36 and the last 36 months, for the level, the first difference, the percent change, the log
   return and the 12-month log growth. Which series are stable over time?
7. Average the log return by calendar month. Which months grow fastest and slowest?
8. Compute the lag-1 autocorrelation of the level, of the log return and of the 12-month log growth, and the lag-12
   autocorrelation of the log return. What dependence is left after each transformation?
9. *Interpretation:* is the board's statement "revenue grows 2,200 USD every month" supported? Give one risk of using
   percent changes and one risk of differencing.

## Grafana

Import `grafana/dashboard.json` (see `../grafana/README.md`; no data-source setup is needed).

- Compare "Revenue (USD): the level" with "Monthly change in USD": what is still not constant after one difference?
- On "Monthly log return vs 12-month growth", what does each line remove and what does it keep?
- Which calendar months stand out in the bar chart, and is that visible in the level chart?

## Deliverable

A short memo (6-8 lines) to the CFO with named parts: **Growth rate** (CAGR and latest year-over-year, with the formula
you used), **Why not USD per month** (evidence from the two halves), **The unusual month** (date, size, effect on the level)
and **Caveat** (one limitation).
