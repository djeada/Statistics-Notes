"""Spreadsheet fundamentals 1 - cell references, sorting, filtering, formatting."""
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from openpyxl.formatting.rule import CellIsRule
from openpyxl.styles import PatternFill

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import Book, md, write_csv  # noqa: E402
from _sheets_util import add_sheet_df  # noqa: E402

SLUG = "spreadsheet-fundamentals/01-basics-references-sorting-filtering"
TITLE = "Basics: cell references, sorting, filtering, formatting"
MODULE = "Spreadsheet fundamentals"
DATASET = "48 stationery-shop orders"
TAX = 0.23
BIG = 200
PRICES = {"Notebook": 4.5, "Pen box": 6.2, "Stapler": 12.9, "Desk lamp": 29.0, "Whiteboard": 55.0, "Office chair": 89.0}


def make_data() -> pd.DataFrame:
    rng = np.random.default_rng(1101)
    n = 48
    dates = pd.to_datetime("2026-01-05") + pd.to_timedelta(np.sort(rng.integers(0, 83, n)), unit="D")
    prod = rng.choice(list(PRICES), n, p=[0.25, 0.2, 0.15, 0.15, 0.13, 0.12])
    qty = np.where(np.isin(prod, ["Notebook", "Pen box"]), rng.integers(5, 41, n), rng.integers(1, 9, n))
    return pd.DataFrame({
        "order_id": 1001 + np.arange(n),
        "order_date": dates,
        "customer": rng.choice(["Acme Ltd", "Birch & Co", "Cedar School", "Delta Studio", "Elm Clinic"], n),
        "region": rng.choice(["North", "South", "East", "West"], n),
        "product": prod,
        "qty": qty,
        "unit_price": [PRICES[p] for p in prod],
    })


def build(out: Path) -> Book:
    df = make_data()
    write_csv(out, df)
    n = len(df)
    lt = (df.qty * df.unit_price).to_numpy()
    df["_lt"] = lt

    b = Book(df.drop(columns="_lt"), "Spreadsheet basics - references, sorting, filtering, formatting",
             "Yellow cells are inputs. Every other number is a formula.")
    b.section("Inputs")
    tax = b.row("Tax rate", TAX, None, "0%", "one cell, referenced absolutely ($B$..)", is_input=True)
    f_start = b.row("Filter: first date", pd.Timestamp("2026-02-01").to_pydatetime(), None, "yyyy-mm-dd", is_input=True)
    f_end = b.row("Filter: last date (exclusive)", pd.Timestamp("2026-03-01").to_pydatetime(), None, "yyyy-mm-dd",
                  is_input=True)

    # helper columns on Data: A order_id B date C customer D region E product F qty G unit_price
    b.add_column("line_total", lambda r: f"=F{r}*G{r}", lt, "$#,##0.00")
    b.add_column("tax", lambda r: f"=H{r}*{tax}", lt * TAX, "$#,##0.00")
    b.add_column("gross", lambda r: f"=H{r}+I{r}", lt * (1 + TAX), "$#,##0.00")
    for col in ("unit_price",):
        for r in range(2, n + 2):
            b.data[f"{b.col(col)}{r}"].number_format = "$#,##0.00"
    LT = f"Data!$H$2:$H${n + 1}"

    b.section("1-2. Totals built from relative formulas")
    total = b.row("Total revenue (sum of line_total)", f"=SUM({LT})", lt.sum(), "$#,##0.00")
    b.row("Average order value", f"=AVERAGE({LT})", lt.mean(), "$#,##0.00")
    tax_tot = b.row("Total tax", f"=SUM(Data!$I$2:$I${n + 1})", lt.sum() * TAX, "$#,##0.00")
    b.row("Gross total (revenue + tax)", f"=SUM(Data!$J$2:$J${n + 1})", lt.sum() * (1 + TAX), "$#,##0.00")

    b.section("3. Mixed references: one formula, filled over a 4 x 4 grid")
    prices_grid, qtys = [2, 5, 10, 20], [10, 25, 50, 100]
    hdr = b.next_row
    rows = [[q] + [f"=$A{hdr + 1 + i}*{'BCDE'[j]}${hdr}" for j in range(4)] for i, q in enumerate(qtys)]
    exp = {(i, j + 1): q * prices_grid[j] for i, q in enumerate(qtys) for j in range(4)}
    g0, g1 = b.table(["qty \\ unit price", *prices_grid], rows, fmt={1: "#,##0", 2: "#,##0", 3: "#,##0", 4: "#,##0"},
                     expect=exp)
    grid_cell = f"Analysis!D{g0 + 2}"  # qty 50 x price 10

    # sorted copy (values) -------------------------------------------------
    srt = df.drop(columns="_lt").assign(line_total=lt).sort_values(["region", "line_total"], ascending=[True, False])
    add_sheet_df(b, "Sorted", srt, {"order_date": "yyyy-mm-dd", "line_total": "$#,##0.00", "unit_price": "$#,##0.00"})
    first_id = int(srt.order_id.iloc[0])

    b.section("4. Sorting (see the Sorted sheet: region A-Z, then line_total largest first)")
    sid = b.row("order_id in the first row after sorting", "=Sorted!A2", first_id, "0")
    b.row("Total after sorting (must be unchanged)", f"=SUM(Sorted!H2:H{n + 1})", lt.sum(), "$#,##0.00",
          "sorting reorders rows, it never changes values")

    b.section("5-6. What a filter shows, computed with COUNTIFS / SUMIFS")
    north_big = (df.region == "North") & (lt > 100)
    cnt5 = b.row("Region = North AND line_total > 100: rows", f'=COUNTIFS(Data!$D$2:$D${n + 1},"North",{LT},">100")',
                 int(north_big.sum()), "0")
    sum5 = b.row("... their total", f'=SUMIFS({LT},Data!$D$2:$D${n + 1},"North",{LT},">100")', lt[north_big].sum(),
                 "$#,##0.00")
    feb = (df.order_date >= "2026-02-01") & (df.order_date < "2026-03-01")
    D = f"Data!$B$2:$B${n + 1}"
    cnt6 = b.row("Orders placed in the date window: rows",
                 f'=COUNTIFS({D},">="&{b.local(f_start)},{D},"<"&{b.local(f_end)})', int(feb.sum()), "0")
    sum6 = b.row("... their revenue", f'=SUMIFS({LT},{D},">="&{b.local(f_start)},{D},"<"&{b.local(f_end)})',
                 lt[feb].sum(), "$#,##0.00")
    ns = df.region.isin(["North", "South"])
    b.row("Region North OR South: rows (two COUNTIFs added)",
          f'=COUNTIF(Data!$D$2:$D${n + 1},"North")+COUNTIF(Data!$D$2:$D${n + 1},"South")', int(ns.sum()), "0")

    b.section("7. Formatting: which rows does the highlight rule colour?")
    hi = b.row("Rows with line_total above the threshold", f'=COUNTIF({LT},">{BIG}")', int((lt > BIG).sum()), "0")

    # formatting on Data sheet ------------------------------------------------
    b.data.freeze_panes = "A2"
    b.data.auto_filter.ref = f"A1:J{n + 1}"
    for r in range(2, n + 2):
        b.data[f"B{r}"].number_format = "yyyy-mm-dd"
    b.data.conditional_formatting.add(
        f"H2:H{n + 1}", CellIsRule(operator="greaterThan", formula=[str(BIG)],
                                   fill=PatternFill("solid", bgColor="FFC7CE", fgColor="FFC7CE")))
    for L, w in zip("ABCDEFGHIJ", [10, 12, 16, 9, 14, 7, 11, 12, 11, 12]):
        b.data.column_dimensions[L].width = w

    b.bar_chart_from_table("Revenue grid: qty x unit price", 1, [2, 3, 4, 5], g0, g1, anchor="H4",
                           x_title="quantity", y_title="revenue")

    top = srt.iloc[0]
    b.answers([
        ("Total revenue of all orders (sum of line_total)", f"={total}",
         f"{lt.sum():,.2f}. Average order value {lt.mean():,.2f} over {n} orders."),
        ("Total tax at the rate in the input cell, and the gross total", f"={tax_tot}", f"Tax = {lt.sum() * TAX:,.2f}; gross = {lt.sum() * (1 + TAX):,.2f}. Changing the rate cell updates every row."),
        ("Value of the grid at qty 50, unit price 10 - and which references the formula uses", f"={grid_cell}",
         "500. The formula has the shape =$A5*B$4: the $ locks the column of the quantity and the row of the prices, so one "
         "formula can be filled right and down."),
        ("order_id of the first row after sorting by region A-Z, then line_total largest first", f"={sid}",
         f"{first_id} ({top.region}, line total {top.line_total:,.2f}). The total is unchanged by sorting."),
        ("Rows with Region = North and line_total > 100", f"={cnt5}",
         f"{int(north_big.sum())} rows worth {lt[north_big].sum():,.2f}."),
        ("Orders placed in February: how many and what revenue?", f"={cnt6}",
         f"{int(feb.sum())} orders, {lt[feb].sum():,.2f}."),
        (f"Rows highlighted by the 'line_total > {BIG}' rule", f"={hi}",
         f"{int((lt > BIG).sum())} of {n} rows. Formatting changes what you see, never the value."),
        ("Absolute vs relative reference - explain in one sentence", "text",
         "A relative reference (H2) shifts when the formula is copied; an absolute one ($B$6) stays pinned, which is what a "
         "single input such as the tax rate needs. Sorting or filtering a range with formulas that point to other rows "
         "breaks relative references - sort the whole table, and keep inputs in absolute cells."),
    ])
    md(out / "theory.md", THEORY)
    md(out / "task.md", TASK)
    return b


THEORY = r"""
# Theory: cell references, sorting, filtering and formatting

## Why start here

Almost every spreadsheet error comes from one of four things: a formula copied with the wrong kind of reference, a table
sorted so that rows no longer belong together, a filter mistaken for a deletion, or a number that *looks* right because of
its format but is something else underneath. This lesson is about getting those four right.

## Cells, ranges, references

A cell is addressed by column letter and row number: `B7`. A **range** is a rectangle: `B2:D10`. A range on another sheet is
`Data!B2:B49`. A formula starts with `=` and can contain numbers, cell references, operators (`+ - * / ^ &`) and functions.

## Relative, absolute and mixed references

When you copy a formula, references are rewritten *relative to the move*:

| written | copied one row down | copied one column right | meaning |
|---|---|---|---|
| `B2` | `B3` | `C2` | relative: both parts move |
| `$B$2` | `$B$2` | `$B$2` | absolute: pinned (shortcut: `F4`) |
| `$B2` | `$B3` | `$B2` | mixed: column pinned, row moves |
| `B$2` | `B$2` | `C$2` | mixed: row pinned, column moves |

**Worked example.** Row 2 holds `qty = 12`, `unit_price = 4.50`, and the tax rate sits in `Analysis!B6 = 0.23`.

- `line_total = F2*G2 = 54.00`: fully relative, correct to fill down.
- `tax = H2*Analysis!$B$6 = 54.00 * 0.23 = 12.42`: the rate is pinned. Written as `Analysis!B6` it would become `B7`, `B8`... in
  the rows below and silently multiply by blank cells or labels.

Mixed references let **one** formula fill a whole grid. A price table with quantities down column A (10, 25, 50, 100) and unit
prices across row 4 (2, 5, 10, 20) needs only `=$A5*B$4`: the `$` in front of `A` keeps the quantity column fixed while the
formula moves right, and the `$` in front of `4` keeps the price row fixed while it moves down. At quantity 50 and price 10 the cell
shows 500.

**Names.** A named range (`TaxRate` for `Analysis!$B$6`) is an absolute reference with a readable label. It is the same
mechanism, useful once a model has more than a handful of inputs.

## Sorting

Sorting **reorders rows**; it never changes values. Rules that prevent damage:

1. Sort the **whole table**, not one column. Sorting only column D separates every region from its order.
2. Tell the tool the first row is a **header** so it is not sorted into the data.
3. Multi-key sorts apply keys in priority order: region A-Z first, then line total descending *within* each region.
4. Formulas that refer to *other rows* (`=H2-H1`, running totals) change meaning after a sort. Formulas that refer to
   their own row (`=F2*G2`) survive it.
5. Keep an untouched copy or an id column (`order_id`) so the original order can be recovered.

## Filtering

A filter **hides** rows that do not match; the data are untouched. Conditions combine as AND across columns
(`region = North` and `line_total > 100`) and as OR within one column (`North` or `South`). Two pitfalls:

- Hidden rows are still counted by `SUM`, `AVERAGE`, `COUNT`. To total only what is visible use `SUBTOTAL(109, range)` (or
  `AGGREGATE`); the status bar also reports the visible selection.
- A filter on a range that has blank rows stops at the first blank row. Keep the table contiguous.

The same selection can be computed with a formula: `COUNTIFS`, `SUMIFS` take the same conditions and do not depend on what
is currently hidden. That is how the solution workbook reports "what the filter would show".

## Formatting

Formatting changes **display**, not value:

- A date is a number (days since 1899-12-30); `2026-02-01` formatted as *General* shows 46054. A cell that shows `0.23` or
  `23%` holds the same number.
- Text that looks like a number (left-aligned, a green corner in Excel, a leading apostrophe) does not add up. Convert it
  (lesson 5).
- Rounding by format does not round: `1.005` displayed with two decimals still sums as `1.005`. Use `ROUND` when the value itself
  must change.
- **Conditional formatting** colours cells by a rule (`> 200`); the rule reads the cell, the cell does not store the colour.
  Freeze the header row so labels stay visible while scrolling.

## Common mistakes

1. Typing a number into a formula (`*0.23`) instead of referencing an input cell.
2. Sorting a selection that does not include all columns.
3. Treating a filtered `SUM` as a filtered result.
4. Using colour as data ("the red rows are late"): it cannot be counted or filtered by formulas. Add a column.

## Next

[Essential formulas](../02-essential-formulas/theory.md)
"""

TASK = r"""
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
"""
