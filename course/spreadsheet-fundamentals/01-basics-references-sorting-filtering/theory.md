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
