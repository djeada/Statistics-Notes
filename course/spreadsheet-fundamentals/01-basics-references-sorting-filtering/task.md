# Task: references, sorting, filtering, formatting

## Scenario

You have just taken over the order book of a small stationery shop. The owner wants totals with tax, a quick price grid for
customers, and answers to a few "how many orders ..." questions. The previous file had numbers typed straight into formulas,
and someone once sorted one column by accident. Rebuild it properly.

## Data

`data.csv` - 48 orders, January to March 2026, one row per order line.

| column | meaning |
|---|---|
| `order_id` | unique order number |
| `order_date` | date of the order |
| `customer` | customer name |
| `region` | North, South, East or West |
| `product` | product sold |
| `qty` | units sold |
| `unit_price` | price per unit |

Import it into Google Sheets (File → Import → Upload) or Excel.

## Questions

1. Add a column `line_total = qty * unit_price` (one formula, filled down). What is the total revenue and the average order value?
2. Put the tax rate (23 %) in **one** input cell. Add `tax` and `gross` columns that reference it absolutely. What are the total tax and the gross total?
3. Build a 4 x 4 revenue grid: quantities 10, 25, 50, 100 down, unit prices 2, 5, 10, 20 across. Use **one** formula filled
   over the whole grid. What does the cell for quantity 50 and price 10 contain, and which references are mixed?
4. Sort the table by `region` (A-Z) and then by `line_total` (largest first). What is the `order_id` in the first row? Check that
   the total is unchanged and that each row's `order_id` still matches its product (no column was sorted alone).
5. Filter `region = North` and `line_total > 100`. How many rows remain and what is their total? Compare the status-bar sum with
   `SUM`, `SUBTOTAL(109, ...)` and `SUMIFS`.
6. How many orders were placed in February, and what revenue did they bring? Keep the first and last date in input cells.
7. Apply: currency format for money columns, `yyyy-mm-dd` for dates, a frozen header row, and a conditional-format rule that colours
   `line_total` above 200. How many rows are coloured?
8. *Explain in two sentences* when you need an absolute reference and what can go wrong when a table that contains formulas is sorted.

## Deliverable

A cleaned workbook with the formula columns, the mixed-reference grid, the formatting, and a short note (4-6 lines)
listing the four numbers the owner asked for: revenue, tax, February orders, North orders above 100.

Compare with `solution.xlsx`: sheet `Answers` has the values; `Analysis` shows the formulas; the `Sorted` sheet is your question-4 result.
