# Task: trend, seasonality and noise

## Scenario

You analyse daily orders for an online shop. Management reads the daily number every morning and keeps asking
"is it growing?", "why are weekends so bad?" and "was last month's campaign day special?". You have been given 21 weeks
of data and must separate what is *structure* (growth and weekly rhythm) from what is *noise*, so that the team stops
reacting to ordinary Saturdays and spots days that are really unusual.

## Data

`data.csv` - 147 consecutive days from 2026-01-05 (a Monday) to 2026-05-31; one row = one day.

| column | meaning |
|---|---|
| `date` | calendar day |
| `orders` | number of completed orders that day (count) |

## Questions

Work in a spreadsheet (import `data.csv`), then compare with `solution.xlsx`.

1. Fit a straight line to `orders` against the day number (0, 1, 2, ...). What is the slope in orders per day, and per week?
2. Compute a **centred 7-day moving average** as the trend estimate. How many rows have no value, and why?
3. Subtract the trend from the orders. Average the result for each weekday (Mon = 1 ... Sun = 7) and centre the seven
   values so they sum to zero. Which weekday is best, which is worst, and how large is the weekend dip?
4. Subtract the seasonal index from the orders to get the **seasonally adjusted** series and fit a line to it. Compare slope
   and intercept with question 1.
5. Compute the **residual** (orders - trend - seasonal index). What is its standard deviation? Which day has the largest
   absolute residual, and how many days are further than 3 SD from zero?
6. Compute the trend strength and the seasonal strength (formulas in the theory file). Which component is more
   important here?
7. Forecast the orders of the day after the last one (a Monday) as `intercept + slope x day number + Monday index`.
8. Check that the seven seasonal indices sum to zero, and explain why they are centred.
9. *Interpretation:* name two ways in which this decomposition could mislead the team (think about the edges of the series,
   one-off events and the assumption of a fixed weekly pattern).

## Grafana

Import `grafana/dashboard.json` (see `../grafana/README.md`; no data-source setup is needed).

- On "Orders and centred 7-day mean", where does the smooth line start and stop, and why?
- On "Seasonally adjusted orders and fitted trend", what disappeared compared with the raw series, and what stayed?
- On "Residuals", what does the flagged point tell you, and do the other residuals look patternless?

## Deliverable

A note (6-8 lines) for the head of e-commerce with named parts: **Growth** (orders per day, with the seasonally adjusted
slope), **Weekly pattern** (the indices and what to do about them), **Unusual days** (date, size in orders, how you know it
is unusual) and **Caveat** (one limitation of the method).
