# Theory: pivot tables, charts and conditional formatting

## From rows to answers

A table of 400 transactions answers nothing until it is **summarised**: revenue by region, by month, by person. A **pivot table**
does that grouping interactively. Think of it as a drag-and-drop `SUMIFS`: you choose which field defines the rows, which defines
the columns, and which number to aggregate in the cells.

## Anatomy of a pivot table

| part | role | example |
|---|---|---|
| **Rows** | each distinct value becomes a row | region |
| **Columns** | each distinct value becomes a column | category |
| **Values** | the number aggregated in each cell, and *how* (SUM, COUNT, AVERAGE, MAX) | SUM of revenue |
| **Filters** | restrict the source rows before grouping | month >= 3 |
| **Calculated field** | a formula on aggregated fields | revenue / units |
| **Show as** | display values as % of row / column / grand total | % of column total |

**Build one** (Google Sheets: select the data → *Insert → Pivot table*; Excel: *Insert → PivotTable*): put `region` in Rows,
`category` in Columns, `revenue` in Values (Summarize by: SUM). The grand total at the bottom right must equal `SUM(revenue)` of the source.

**Why the solution workbook has no pivot table.** A pivot table is an object created and refreshed in the application; it is not a
formula and the files in this course are generated programmatically and verified by recalculation. The `Analysis` sheet therefore holds
the same tables built with `SUMIFS`, `COUNTIFS`, `AVERAGEIFS`. Use them as the **answer key** for your pivot: the numbers must match cell for cell.

**Pivot vs formulas.** A pivot is fast to build and explore, handles new categories automatically and shows totals; it needs a manual
refresh (Excel) and is awkward to place inside a bigger model. `SUMIFS` tables update with the data, can be referenced by other
formulas and do not hide rows, but you list the categories yourself.

## Checks every analyst runs

1. **Reconcile**: the pivot grand total equals the source total. A text-stored number or a stray blank row is skipped silently.
2. **Count the rows**: pivot with COUNT; it should equal the number of data rows.
3. **Look for "(blank)" and typos**: `North` and `north ` form two rows; clean the key first (lesson 5).
4. **Percent of total** after a total: shares sum to 100 %.

**Worked example.** If January Furniture revenue is 9 800 and June is 5 900, the change is $5\,900/9\,800 - 1 = -39.8\%$: always
express a trend relative to its starting point. A change of "-3 900" is not comparable across categories of different size.

## Charts: pick the form for the question

| question | chart |
|---|---|
| compare categories / groups | column or bar chart (sort the bars) |
| change over time | **line** chart, time on the x axis |
| parts of a whole (few parts) | stacked bar; pie only for 2-4 slices |
| relationship between two numbers | scatter |
| distribution of one number | histogram |

Rules that prevent misleading charts: start bar charts at zero; label axes and units; one message per chart; do not use colour
for decoration; do not put 12 lines on one plot. Plot **summaries** (pivot output), not 400 raw rows.

## Conditional formatting

Colours a cell according to a **rule** about its value. Types used here:

- **Color scale** on a matrix: white → green by magnitude, so the biggest cells jump out.
- **Data bars**: a bar inside the cell proportional to the value.
- **Formula rule**: `=$F5<=3` highlights the whole row when the rank in column F is 3 or better (the `$` locks the column, the row is relative).

Conditional formatting is a **display layer**: it does not change values and cannot be counted by formulas, so add a flag column if you
need to count the highlighted rows. Use it sparingly: if everything is red, nothing is.

## Pitfalls

1. Pivot on a range that does not include newly added rows (use a whole-column or table source).
2. Averaging averages: the average of regional averages is not the overall average; aggregate sums and counts, then divide.
3. Mixing units in one value field.
4. Truncated y axes, 3-D charts, rainbow colour scales.
5. Treating the pivot as the data: copy-paste *values* when you need a frozen snapshot.

## Next

[Advanced skills: dashboards, QUERY, FILTER, data cleaning](../05-advanced-skills/theory.md)
