# Task: essential formulas

## Scenario

A team lead has three months of expense lines and has to report to finance on Friday: how much was spent, where, what needs a
second look, and which categories are over budget. The export is not perfect: some receipts have no amount yet, a few lines are
refunds, and some lines were never marked approved.

## Data

`data.csv` - 150 expense lines, 2026-01-01 to 2026-03-31.

| column | meaning |
|---|---|
| `expense_id` | unique id |
| `date` | date of the expense |
| `category` | Travel, Software, Meals, Office or Training |
| `vendor` | who was paid |
| `amount` | amount in currency units (negative = refund, blank = not yet entered) |
| `payment` | Card, Transfer or Cash |
| `approved` | Yes, No, or blank (nobody has looked yet) |

## Questions

1. Compute `SUM`, `AVERAGE`, `MEDIAN`, `MIN` and `MAX` of `amount`. Round the average to a whole number with `ROUND`.
2. How do `COUNT`, `COUNTA` and `COUNTBLANK` differ on `amount`? How many expenses have no amount?
3. With `COUNTIF`: how many Travel rows; how many amounts above 500; how many `approved = No`; how many `approved` blank?
4. Build a category table with `SUMIF` (spend), `COUNTIF` (rows), `AVERAGEIF` (mean per row) and each category's share of the total.
   Which category spends most?
5. How much was paid to vendors whose name starts with "Air"? (wildcard)
6. Add `review = IF(amount > 500, "review", "ok")` and a nested-`IF` size tier (missing / refund / small < 50 / medium < 500 / large).
   How many rows are flagged, and how many rows and how much spend per tier?
7. With `COUNTIFS`/`SUMIFS`: how many Travel rows were paid by Card and what do they sum to? What was the Travel spend in February
   (add a `month` column with `MONTH`)?
8. The budgets for the quarter are Travel 9 000, Software 3 000, Meals 1 000, Office 1 200, Training 7 500. Put them in input cells, flag each
   category `over`/`ok` with `IF`, and count how many are over. Then compute the average of a category called "Marketing" that is not in
   the data - make it show 0 instead of an error.
9. *Explain in two sentences* why typing 0 for a missing receipt would change the average, and why mean and median differ here.

## Deliverable

A one-page summary sheet for finance: total spend, spend by category with share, count of rows to review, categories over
budget, and one sentence on the data-quality problems you noticed (blank amounts, blank approvals).

Compare with `solution.xlsx` (`Answers` for values, `Analysis` for the formulas).
