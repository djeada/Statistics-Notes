"""Spreadsheet fundamentals 4 - pivot tables, charts, conditional formatting."""
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from openpyxl.formatting.rule import ColorScaleRule, DataBarRule, FormulaRule
from openpyxl.styles import PatternFill

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import Book, md, write_csv  # noqa: E402

SLUG = "spreadsheet-fundamentals/04-data-analysis"
TITLE = "Data analysis: pivot tables, charts, conditional formatting"
MODULE = "Spreadsheet fundamentals"
DATASET = "400 sales transactions, Jan-Jun 2026"
REGIONS = ["North", "South", "East", "West"]
CATS = ["Electronics", "Furniture", "Office", "Software"]
REPS = {"North": ["Maya", "Ibrahim"], "South": ["Lena", "Tomasz"], "East": ["Sofia", "Kenji"], "West": ["Aisha", "Diego"]}
PRICE = {"Electronics": 240, "Furniture": 180, "Office": 35, "Software": 90}


def make_data() -> pd.DataFrame:
    rng = np.random.default_rng(1404)
    n = 400
    dates = pd.to_datetime("2026-01-01") + pd.to_timedelta(np.sort(rng.integers(0, 181, n)), unit="D")
    region = rng.choice(REGIONS, n, p=[.3, .28, .17, .25])
    cat = np.empty(n, dtype=object)
    for i, r in enumerate(region):  # West buys more electronics, East more office supplies
        p = {"West": [.5, .15, .15, .2], "East": [.15, .15, .5, .2]}.get(r, [.3, .25, .25, .2])
        cat[i] = rng.choice(CATS, p=p)
    rep = np.array([rng.choice(REPS[r], p=[.65, .35]) for r in region])
    units = rng.integers(1, 13, n)
    month_idx = (dates.month - 1).to_numpy()
    trend = np.array([{"Furniture": 1 - 0.13 * m, "Electronics": 1 + 0.05 * m}.get(c, 1.0) for c, m in zip(cat, month_idx)])
    revenue = (units * np.array([PRICE[c] for c in cat]) * trend * rng.lognormal(0, 0.12, n)).round(2)
    return pd.DataFrame({"sale_id": 7001 + np.arange(n), "date": dates, "region": region, "category": cat, "rep": rep,
                         "units": units, "revenue": revenue})


def build(out: Path) -> Book:
    df = make_data()
    write_csv(out, df)
    n = len(df)
    last = n + 1
    df["month"] = df.date.dt.month
    R = lambda L: f"Data!${L}${2}:${L}${last}"  # noqa: E731
    REG, CAT, REP, UN, REV, MON = R("C"), R("D"), R("E"), R("F"), R("G"), R("H")

    b = Book(df.drop(columns="month"), "Spreadsheet basics - analysis tables, charts, conditional formatting",
             "The tables below are what the pivot tables must show (SUMIFS version). Real pivot tables are built in the UI.")
    b.add_column("month", lambda r: f"=MONTH(B{r})", df.month.to_numpy(float), "0")
    b.add_column("revenue_per_unit", lambda r: f"=G{r}/F{r}", (df.revenue / df.units).to_numpy(), "0.00")

    b.section("1. Grand totals")
    tot = b.row("Total revenue", f"=SUM({REV})", df.revenue.sum(), "#,##0.00")
    b.row("Total units", f"=SUM({UN})", int(df.units.sum()), "#,##0")
    b.row("Transactions", f"=COUNT({REV})", n, "0")
    b.row("Revenue per unit", f"={b.local(tot)}/SUM({UN})", df.revenue.sum() / df.units.sum(), "0.00")

    # ---- pivot 1: region x category ------------------------------------------
    b.section("2. Pivot 1 - revenue by region (rows) and category (columns)")
    h1 = b.next_row
    rows, exp = [], {}
    pv = df.pivot_table(index="region", columns="category", values="revenue", aggfunc="sum").reindex(index=REGIONS, columns=CATS)
    for i, rg in enumerate(REGIONS):
        r = h1 + 1 + i
        rows.append([rg] + [f"=SUMIFS({REV},{REG},$A{r},{CAT},{c}${h1})" for c in "BCDE"] + [f"=SUM(B{r}:E{r})"])
        for j, c in enumerate(CATS):
            exp[(i, j + 1)] = pv.loc[rg, c]
        exp[(i, 5)] = pv.loc[rg].sum()
    rt = h1 + 5
    rows.append(["Total"] + [f"=SUM({c}{h1 + 1}:{c}{h1 + 4})" for c in "BCDEF"])
    for j, c in enumerate(CATS):
        exp[(4, j + 1)] = pv[c].sum()
    exp[(4, 5)] = pv.to_numpy().sum()
    p0, p1 = b.table(["region \\ category", *CATS, "Total"], rows, fmt={k: "#,##0" for k in range(1, 6)}, expect=exp)
    b.an.conditional_formatting.add(f"B{p0}:E{p1 - 1}", ColorScaleRule(start_type="min", start_color="FFFFFF", end_type="max",
                                                                       end_color="63BE7B"))
    rec = b.row("Reconciliation: pivot grand total minus SUM of Data (must be 0)", f"=F{p1}-{b.local(tot)}", 0.0, "0.00")
    best = pv.stack().idxmax()
    bestreg = pv.sum(axis=1).idxmax()
    b.bar_chart_from_table("Revenue by region and category", 1, [2, 3, 4, 5], p0, p1 - 1, anchor="J4", y_title="revenue")

    # ---- pivot 2: month x category --------------------------------------------
    b.section("3. Pivot 2 - revenue by month (rows) and category (columns)")
    h2 = b.next_row
    pm = df.pivot_table(index="month", columns="category", values="revenue", aggfunc="sum").reindex(columns=CATS)
    tm = pm.sum(axis=1)
    rows, exp = [], {}
    for i, m in enumerate(range(1, 7)):
        r = h2 + 1 + i
        rows.append([m] + [f"=SUMIFS({REV},{MON},$A{r},{CAT},{c}${h2})" for c in "BCDE"] + [f"=SUM(B{r}:E{r})",
                    "" if i == 0 else f"=F{r}/F{r - 1}-1"])
        for j, c in enumerate(CATS):
            exp[(i, j + 1)] = pm.loc[m, c]
        exp[(i, 5)] = tm.loc[m]
        if i:
            exp[(i, 6)] = tm.loc[m] / tm.loc[m - 1] - 1
    m0, m1 = b.table(["month", *CATS, "Total", "MoM change"], rows,
                     fmt={**{k: "#,##0" for k in range(1, 6)}, 6: "0.0%"}, expect=exp)
    b.line_chart_from_table("Monthly revenue by category", 1, [2, 3, 4, 5], m0, m1, anchor="J24", x_title="month", y_title="revenue")
    furn_change = pm.loc[6, "Furniture"] / pm.loc[1, "Furniture"] - 1
    fc = b.row("Furniture revenue, June vs January", f"=C{m1}/C{m0}-1", furn_change, "0.0%")
    topm = int(tm.idxmax())
    tmc = b.row("Month with the highest total revenue (number)", f"=INDEX(A{m0}:A{m1},MATCH(MAX(F{m0}:F{m1}),F{m0}:F{m1},0))", topm, "0")

    # ---- pivot 3: reps -------------------------------------------------------
    b.section("4. Pivot 3 - sales reps")
    h3 = b.next_row
    reps = [r for rg in REGIONS for r in REPS[rg]]
    g = df.groupby("rep").agg(tx=("revenue", "size"), rev=("revenue", "sum"), avg=("revenue", "mean")).reindex(reps)
    rank = g.rev.rank(ascending=False, method="min")
    rows, exp = [], {}
    for i, rp in enumerate(reps):
        r = h3 + 1 + i
        rows.append([rp, f"=COUNTIFS({REP},A{r})", f"=SUMIFS({REV},{REP},A{r})", f"=AVERAGEIFS({REV},{REP},A{r})",
                     f"=C{r}/{b.local(tot)}", f"=RANK(C{r},C${h3 + 1}:C${h3 + len(reps)})"])
        exp.update({(i, 1): g.tx[rp], (i, 2): g.rev[rp], (i, 3): g.avg[rp], (i, 4): g.rev[rp] / df.revenue.sum(),
                    (i, 5): rank[rp]})
    q0, q1 = b.table(["rep", "transactions", "revenue", "avg per transaction", "share of total", "rank"], rows,
                     fmt={2: "#,##0", 3: "#,##0.00", 4: "0.0%", 5: "0"}, expect=exp)
    b.an.conditional_formatting.add(f"C{q0}:C{q1}", DataBarRule(start_type="num", start_value=0, end_type="max", color="5B9BD5"))
    b.an.conditional_formatting.add(f"A{q0}:F{q1}", FormulaRule(formula=[f"$F{q0}<=3"], fill=PatternFill("solid", bgColor="FFEB9C", fgColor="FFEB9C")))
    toprep = g.rev.idxmax()
    topsh = b.row("Revenue share of the best rep", f"=MAX(E{q0}:E{q1})", g.rev.max() / df.revenue.sum(), "0.0%")
    b.bar_chart_from_table("Revenue by rep", 1, [3], q0, q1, anchor="J44", y_title="revenue")

    sorted_reps = g.rev.sort_values(ascending=False)
    b.answers([
        ("Total revenue, total units, revenue per unit", f"={tot}",
         f"{df.revenue.sum():,.2f} from {int(df.units.sum())} units in {n} transactions = {df.revenue.sum() / df.units.sum():.2f} per unit."),
        ("Region x category pivot: which single cell is largest, and which region has the largest total?", f"=MAX(Analysis!B{p0}:E{p1 - 1})",
         f"{best[0]} / {best[1]} = {pv.loc[best]:,.0f}. Region totals: " + ", ".join(f"{r} {pv.loc[r].sum():,.0f}" for r in REGIONS)
         + f" - {bestreg} is the largest."),
        ("Does the pivot grand total reconcile with the raw data?", f"={rec}",
         "Difference 0.00. Always reconcile a pivot with SUM of the source: a filter or a text-number can silently drop rows."),
        ("Monthly pivot: which month is best, and what happened to Furniture between January and June?", f"={tmc}",
         f"Month {topm} is highest ({tm.max():,.0f}). Furniture fell {abs(furn_change):.0%} from January to June while Electronics rose "
         f"{pm.loc[6, 'Electronics'] / pm.loc[1, 'Electronics'] - 1:.0%}."),
        ("Rep table: top 3 reps by revenue and the share of the best one", f"={topsh}",
         "Top 3: " + ", ".join(f"{r} ({v:,.0f})" for r, v in sorted_reps.head(3).items()) +
         f". {toprep} alone brings {g.rev.max() / df.revenue.sum():.1%}."),
        ("Three charts: clustered column (region x category), line (month x category), bar (rep)", "text",
         "See the three charts on the Analysis sheet. The line chart shows the Furniture decline fastest; the clustered column shows "
         "West's Electronics and East's Office strength."),
        ("Conditional formatting: colour scale on the region matrix, data bars on rep revenue, highlight the top 3", "text",
         "Rules are applied on the Analysis sheet (colour scale B:E of pivot 1, data bars on rep revenue, formula rule rank <= 3)."),
        ("What would you tell the sales manager, and what is one limitation of a pivot table?", "text",
         f"Furniture fell {abs(furn_change):.0%} in six months while Electronics grew; the top three reps bring {sorted_reps.head(3).sum() / df.revenue.sum():.0%} of revenue (dependence on a few people). "
         "A pivot is a summary of the data at one moment: refresh it after the source changes, and check the grand total against the raw data."),
    ])
    md(out / "theory.md", THEORY)
    md(out / "task.md", TASK)
    return b


THEORY = r"""
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
"""

TASK = r"""
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
"""
