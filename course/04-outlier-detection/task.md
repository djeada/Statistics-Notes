# Task: outlier detection

## Scenario

The procurement team of a research institute exports its purchase-order lines for February and March. Finance wants to publish the average
amount per line and the total spend, but the monthly audit has found "some crazy numbers". You are asked to flag suspicious lines, decide which
are errors that must be corrected and which are legitimate, and say how much the published figures change depending on your decision.

## Data

`data.csv` - 300 purchase-order lines, one row per line.

| column | meaning |
|---|---|
| `line_id` | running number |
| `date` | date the order was placed |
| `category` | `stationery`, `lab_supplies` or `it_hardware` |
| `quantity` | units ordered |
| `unit_price_eur` | price per unit in EUR |
| `amount_eur` | line total in EUR (`quantity` x `unit_price_eur`) |

## Questions

Work in a spreadsheet (import `data.csv`), then compare with `solution.xlsx`. Use `STDEV` (sample), `QUARTILE` (inclusive) and thresholds z = 3.0, Tukey k = 1.5 (inner) and 3 (outer), modified z = 3.5.

1. Compute mean, SD, median, MAD, Q1, Q3 and IQR of `amount_eur`.
2. Flag lines with $|z|>3$. How many are there, and what is the upper limit in EUR?
3. Compute the Tukey fences for k = 1.5 and k = 3. How many lines does each flag?
4. Compute the modified z for every line. How many have $|M|>3.5$ and what is the equivalent upper limit in EUR?
5. How many lines are flagged by the modified z but *not* by the z-score? Why can that happen? (Compare the SD with 1.4826 x MAD.)
6. Repeat the three rules on $\ln(\text{amount})$. How do the counts change and why?
7. Compute the median unit price per category and the ratio of each line's unit price to its category median. Call a line a *price error* if the ratio is above 5 or below 1/5. How many price errors are there? Of the lines flagged by the modified z on the raw amount, how many are price errors and how many are not?
8. Build a table with, for each of the six rules (three rules, raw and log scale): lines flagged, price errors caught, legitimate lines flagged, price errors missed.
9. Compute the total spend and the mean amount (a) over all lines, (b) without the price errors, (c) without every line flagged by the modified z. How much legitimate spend would (c) delete?
10. *Explain in three sentences* what you would do with each kind of flagged line, and one situation in which none of these rules would find a wrong value.

## Grafana

Import `grafana/dashboard.json` (no data-source setup is needed).

- In "Order-line amount with the three upper limits", which dashed limit lies above many of the red dots? Which limit is below many blue dots?
- In "Context: quantity vs unit price", where do the red dots sit compared with the large blue ones?
- In "Rule performance", which rule gives the best trade-off between caught errors and false alarms?

## Deliverable

A short note (6-10 lines) titled *Which lines do we correct, keep or investigate?* with three named parts: **Method** (rules and thresholds used),
**Findings** (counts, what the errors look like, what the large legitimate lines look like) and **Impact** (how total and mean spend change under each choice).
Include one chart and state one limitation.
