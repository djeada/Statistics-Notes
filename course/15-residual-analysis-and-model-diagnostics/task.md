# Task: residual analysis and model diagnostics

## Scenario

A food-delivery platform wants to show customers a promised delivery time computed from a regression of delivery time on distance, plus a
safety margin of "two residual standard errors". An analyst reports that the fitted line has an R-squared of about 0.9 and
proposes to ship it. You are the reviewer: before approval you must find out whether the model's assumptions hold and what the safety
margin really covers.

## Data

`data.csv` - 120 deliveries in time order (one every 45 minutes, starting 2026-02-02 08:00).

| column | meaning |
|---|---|
| `ordered_at` | when the order was placed |
| `distance_km` | restaurant-to-customer distance, kilometres |
| `delivery_min` | time from order to delivery, minutes |

## Questions

Work in a spreadsheet (import `data.csv`), then compare with `solution.xlsx`.

1. Fit `delivery_min = a + b * distance_km` (`SLOPE`, `INTERCEPT`, `RSQ`, `STEYX`). Report all four numbers.
2. Add fitted values and residuals. Compute the standard deviation of the residuals in three distance bands (< 6 km, 6-12 km, >= 12 km).
   What is the ratio far/near?
3. Run the Breusch-Pagan check: regress squared residuals on distance, compute $LM = n R^2$ and the p-value with `CHIDIST(LM,1)`.
4. Compute skewness, excess kurtosis, the share of standardised residuals beyond +-2, and the (approximate) Jarque-Bera statistic.
   Build a normal QQ plot (sorted standardised residuals vs `NORMSINV((i-0.5)/n)`).
5. Compute leverage $h_i = 1/n + (x_i-\bar x)^2/\sum(x_j-\bar x)^2$ and standardised residuals $e_i/(s\sqrt{1-h_i})$. How many orders have $h_i > 4/n$?
6. Compute Cook's distance $D_i = r_i^2 h_i / (2(1-h_i))$. Which orders have the largest values, and what do they look like?
7. Refit the line without the orders with $D_i > 0.5$ (weighted sums via `SUMPRODUCT`). How much does the slope change?
8. Refit with weights $w_i = 1/x_i^2$ (weighted least squares). Compute the SD of (residual / distance) in the three bands. What do you see?
9. *In two or three sentences:* is the "two residual standard errors" margin appropriate for all orders? What would you change before launch?

## Grafana

Import `grafana/dashboard.json` (see `../grafana/README.md`; no data-source setup is needed).

- In "Residuals vs distance", what shape do the residuals form, and what does that mean for the safety margin on long trips?
- In "Normal QQ plot", which tail departs from the diagonal, and which orders could be responsible?
- In "Cook's distance by order", how many orders exceed the cut-off, and where do they sit in "Delivery time vs distance"?

## Deliverable

A short review note (6-8 lines): verdict (ship / fix first), the three diagnostics that failed with their numbers, the effect on the slope
of the influential orders, and the change you propose. Include one chart.
