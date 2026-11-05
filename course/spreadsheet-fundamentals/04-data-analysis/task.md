# Task: pivot tables, charts, conditional formatting

## Scenario

The regional sales director asks three questions before the quarterly review: **where** do we sell what, **how has it moved month by
month**, and **who carries the team**. You have the raw transactions for January to June.

## Data

`data.csv` - 400 sales transactions.

| column | meaning |
|---|---|
| `sale_id` | unique id |
| `date` | date of the sale |
| `region` | North, South, East or West |
| `category` | Electronics, Furniture, Office or Software |
| `rep` | sales representative |
| `units` | units in the transaction |
| `revenue` | revenue in currency units |

Add two helper columns first: `month = MONTH(date)` and `revenue_per_unit = revenue / units`.

## Questions

1. What are the total revenue, total units and revenue per unit?
2. **Build a pivot table** with `region` in rows, `category` in columns, SUM of `revenue` in values. Which single cell is the largest, and which region has the largest total?
3. Reconcile: does the pivot grand total equal `SUM(revenue)` of the source? Then rebuild the same table with `SUMIFS` in ordinary cells and compare.
4. **Build a second pivot**: `month` in rows, `category` in columns. Which month has the highest total revenue? What happened to Furniture between January and June (percentage change)? Add a month-over-month change column.
5. **Build a third pivot** by `rep` with COUNT of sales, SUM of revenue and AVERAGE revenue. Who are the top three, and what share of all revenue does the best rep bring?
6. **Charts**: a clustered column chart of region x category, a line chart of monthly revenue by category, a bar chart of revenue by rep. Give each a title and axis labels, and say what each shows in one sentence.
7. **Conditional formatting**: a colour scale on the region x category matrix, data bars on rep revenue, and a rule that highlights the rows of the top three reps (formula rule using the rank column).
8. *Explain in two or three sentences* what you would tell the sales manager, and name one limitation of a pivot table.

## Deliverable

One sheet "Review" with the three summaries (pivot or `SUMIFS`), the three charts and the formatting, followed by a four-line
note for the director.

Compare with `solution.xlsx`: the `Analysis` sheet holds the three tables (as `SUMIFS` formulas), charts and the conditional-formatting rules; `Answers` has the numbers.
