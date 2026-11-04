# Task: sampling distributions and the central limit theorem

## Scenario

An online shop wants to monitor its average order value by auditing a **random sample of n orders** each week. Management proposes
n = 5 ("it is only an average") and the analytics team proposes n = 50. Order values are known to be very uneven: most customers
buy small baskets and a few place large orders. To settle the question you have a full table of last year's 1,000 orders and 250 simulated
audits, each a random sample of 50 orders drawn (with replacement) from that table.

## Data

`data.csv` - 1,000 rows. Columns:

| column | meaning |
|---|---|
| `customer_id` | order number 1-1000 |
| `order_value` | order value in dollars - the **entire population** (all 1,000 orders) |
| `rep` | audit number 1-250 (filled in rows 1-250 only) |
| `s1` ... `s50` | the 50 order values drawn in audit `rep` (rows 1-250 only). Use `s1:s5` for samples of size 5, `s1:s20` for size 20, `s1:s50` for size 50. |

## Questions

Work in a spreadsheet (import `data.csv`), then compare with `solution.xlsx`.

1. Compute the population mean, standard deviation (`STDEVP`), skewness and median of `order_value`. Why is the mean larger than the median?
2. For every audit (row) compute the mean of the first 5, the first 20 and all 50 draws (`AVERAGE` over `s1:s5`, `s1:s20`, `s1:s50`). Compare the average of
   the 250 means with the population mean for each n.
3. Compute the standard deviation of the 250 sample means for each n and compare it with $\sigma/\sqrt n$. How much does the spread shrink when n goes from 5 to 50?
4. Compute the skewness of the 250 sample means for each n and count how many fall in each $10 bucket (`COUNTIFS`). Describe how the shape changes.
5. For each audit and each n compute $s$ (`STDEV`) and check whether $\bar x \pm 1.96\,s/\sqrt n$ contains the population mean. What share of audits do?
6. How many orders per audit are needed for a standard error of 4 dollars? How many for half of it?
7. Using the normal approximation, what is the probability that the average of a 50-order audit exceeds 70 dollars? Compare with the share of the 250 audits that do. Repeat for n = 5.
8. *In two sentences:* which audit size would you recommend, and what does the central limit theorem *not* promise here?

## Grafana

Import `grafana/dashboard.json` (see `../grafana/README.md`; no data-source setup is needed).

- In "Population: single orders" and "Sample means", which distribution is skewed and which one becomes bell-shaped as n grows?
- In "Sample mean of each repetition", how does the scatter of the dots around the line for n = 5 compare with n = 50?
- In "Standard error vs sample size", at what sample size does the spread of the mean reach half of its value at n = 10?

## Deliverable

A short note (5-8 lines) to the management: recommended audit size, the expected size of the typical error for that size, the
share of audits with a misleading "alarm" at your chosen threshold, and one limitation. Include one chart.
