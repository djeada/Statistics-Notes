# Task: multiple regression and confounding

## Scenario

A retail chain wants to know whether to increase its weekly advertising budget. A first regression of sales on ad spend gives a
striking slope, and the finance team has already used it to forecast the return on an extra 10 k$ per week. You are asked to
review that estimate before the budget is signed. You also have weekly price, a promotion flag and a holiday flag.

## Data

`data.csv` - 156 weeks (2023-01-02 onwards), one row per week.

| column | meaning |
|---|---|
| `week` | Monday of the week |
| `ad_spend_k` | advertising spend, thousand dollars |
| `unit_price` | average selling price, dollars |
| `promo` | 1 if a price promotion ran that week, else 0 |
| `holiday` | 1 if the week contains a public holiday / peak-season event, else 0 |
| `temp_c` | mean outdoor temperature, degrees Celsius |
| `sales_units` | units sold |

## Questions

Work in a spreadsheet (import `data.csv`), then compare with `solution.xlsx`. Use `LINEST` inside `INDEX` for multiple regression.

1. Regress `sales_units` on `ad_spend_k` alone (`SLOPE`, `RSQ`). Report the slope and R-squared.
2. Regress `sales_units` on `unit_price` alone. What sign do you get, and does it make business sense?
3. Fit `sales_units ~ ad_spend_k + unit_price + promo`. Report the three coefficients. What changed relative to questions 1-2?
4. Add `holiday` as a fourth predictor. Report all coefficients, R-squared, adjusted R-squared and the t-statistic of the ad
   coefficient.
5. Explain the change in the ad coefficient quantitatively: regress each other predictor on `ad_spend_k` (`SLOPE`) and show that
   `ad coefficient + sum(coefficient x slope)` reproduces the simple slope from question 1.
6. Add `temp_c` as a fifth predictor. What happens to R-squared and adjusted R-squared? Keep it or drop it?
7. Compute the VIF of `ad_spend_k` against the other three predictors. What does it imply for the precision of its coefficient
   (give the 95% interval from question 4)?
8. Using the full model, how many extra units does +10 k$ per week buy in an otherwise normal week? How many would the
   simple regression have promised?
9. *In two or three sentences:* what would have to be true for the full-model coefficient to still be biased?

## Grafana

Import `grafana/dashboard.json` (see `../grafana/README.md`; no data-source setup is needed).

- In "Sales vs ad spend, holiday weeks separated", what do the two clouds look like, and how does the slope inside each compare with the simple line?
- In "Coefficients by model", what happens to the unit price bar across the three specifications?
- In "Where the bias in the simple slope comes from", which variable dominates?

## Deliverable

A short note (6-8 lines) to the finance team: the corrected return on +10 k$, why the earlier estimate was too high, the
uncertainty of the corrected number, and one residual risk. Include one chart.
