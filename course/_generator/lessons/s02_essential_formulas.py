"""Spreadsheet fundamentals 2 - SUM, AVERAGE, IF, COUNTIF, SUMIF (and their IFS cousins)."""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import INPUT_FILL, Book, md, write_csv  # noqa: E402

SLUG = "spreadsheet-fundamentals/02-essential-formulas"
TITLE = "Essential formulas: SUM, AVERAGE, IF, COUNTIF, SUMIF"
MODULE = "Spreadsheet fundamentals"
DATASET = "150 team expense lines with blanks and refunds"
CATS = ["Travel", "Software", "Meals", "Office", "Training"]
BUDGET = {"Travel": 9000, "Software": 3000, "Meals": 1000, "Office": 1200, "Training": 7500}
VENDORS = {"Travel": ["AirNova", "AirLink", "RailGo", "StayWell"], "Software": ["CloudBox", "CodeDesk", "DataLoop"],
           "Meals": ["Corner Cafe", "Lunch Box", "Pizza Hub"], "Office": ["PaperPlus", "DeskDepot"],
           "Training": ["LearnHub", "SkillUp"]}
MU = {"Travel": (5.6, .7), "Software": (4.6, .9), "Meals": (3.4, .5), "Office": (3.9, .7), "Training": (5.9, .5)}


def make_data() -> pd.DataFrame:
    rng = np.random.default_rng(1202)
    n = 150
    cat = rng.choice(CATS, n, p=[.22, .18, .30, .18, .12])
    amt = np.array([rng.lognormal(*MU[c]) for c in cat]).round(2)
    amt[rng.choice(n, 5, replace=False)] *= -1  # refunds
    amt = amt.astype(object)
    for i in rng.choice(n, 3, replace=False):
        amt[i] = np.nan  # receipt not yet entered
    dates = pd.to_datetime("2026-01-01") + pd.to_timedelta(np.sort(rng.integers(0, 90, n)), unit="D")
    approved = rng.choice(["Yes", "No"], n, p=[.85, .15]).astype(object)
    for i in rng.choice(n, 6, replace=False):
        approved[i] = np.nan
    return pd.DataFrame({
        "expense_id": 5001 + np.arange(n), "date": dates, "category": cat,
        "vendor": [rng.choice(VENDORS[c]) for c in cat], "amount": amt.astype(float),
        "payment": rng.choice(["Card", "Transfer", "Cash"], n, p=[.6, .3, .1]), "approved": approved})


def tier(x):
    if pd.isna(x):
        return "missing"
    return "refund" if x < 0 else "small" if x < 50 else "medium" if x < 500 else "large"


def build(out: Path) -> Book:
    df = make_data()
    write_csv(out, df)
    n = len(df)
    a = df.amount
    last = n + 1
    A, C, D, F, G = (f"Data!${c}$2:${c}${last}" for c in "ACDFG")
    E = f"Data!$E$2:$E${last}"
    cat = f"Data!$C$2:$C${last}"

    b = Book(df, "Spreadsheet basics - essential formulas",
             "Columns: A id, B date, C category, D vendor, E amount, F payment, G approved, H review, I size_tier, J month.")
    b.add_column("review", lambda r: f'=IF(E{r}>500,"review","ok")', None)
    b.add_column("size_tier", lambda r: f'=IF(E{r}="","missing",IF(E{r}<0,"refund",IF(E{r}<50,"small",IF(E{r}<500,"medium","large"))))', None)
    b.add_column("month", lambda r: f"=MONTH(B{r})", df.date.dt.month.to_numpy(float), "0")
    H, I, J = (f"Data!${c}$2:${c}${last}" for c in "HIJ")

    b.section("1. The basic aggregates (blank cells are ignored)")
    s = b.row("SUM of amount", f"=SUM({E})", a.sum(), "#,##0.00")
    avg = b.row("AVERAGE of amount", f"=AVERAGE({E})", a.mean(), "#,##0.00")
    b.row("MEDIAN of amount", f"=MEDIAN({E})", a.median(), "#,##0.00")
    b.row("MIN (largest refund)", f"=MIN({E})", a.min(), "#,##0.00")
    b.row("MAX", f"=MAX({E})", a.max(), "#,##0.00")
    b.row("ROUND(average, 0)", f"=ROUND({b.local(avg)},0)", round(a.mean()), "0", "ROUND changes the value, formats do not")

    b.section("2. COUNT, COUNTA, COUNTBLANK on the amount column")
    cnt = b.row("COUNT (cells holding a number)", f"=COUNT({E})", int(a.notna().sum()), "0")
    b.row("COUNTA (non-empty cells)", f"=COUNTA({E})", int(a.notna().sum()), "0")
    miss = b.row("COUNTBLANK (empty cells)", f"=COUNTBLANK({E})", int(a.isna().sum()), "0")
    b.row("Rows in the table", f"=ROWS({E})", n, "0")

    b.section("3. COUNTIF")
    travel = b.row('Rows with category = "Travel"', f'=COUNTIF({cat},"Travel")', int((df.category == "Travel").sum()), "0")
    over500 = b.row("Rows with amount > 500", f'=COUNTIF({E},">500")', int((a > 500).sum()), "0")
    no = b.row('Rows with approved = "No"', f'=COUNTIF({G},"No")', int((df.approved == "No").sum()), "0")
    nb = b.row("Rows with approved left blank", f"=COUNTBLANK({G})", int(df.approved.isna().sum()), "0")

    b.section("4. Category summary: SUMIF / COUNTIF / AVERAGEIF and budget check")
    hdr = b.next_row
    rows, exp = [], {}
    sums = {}
    for i, c in enumerate(CATS):
        r = hdr + 1 + i
        sub = a[df.category == c]
        sums[c] = sub.sum()
        rows.append([c, f"=SUMIF({cat},A{r},{E})", f"=COUNTIF({cat},A{r})", f"=AVERAGEIF({cat},A{r},{E})",
                     f"=B{r}/{b.local(s)}", BUDGET[c], f'=IF(B{r}>F{r},"over","ok")'])
        exp.update({(i, 1): sub.sum(), (i, 2): int((df.category == c).sum()), (i, 3): sub.mean(),
                    (i, 4): sub.sum() / a.sum()})
    c0, c1 = b.table(["category", "SUMIF spend", "rows", "AVERAGEIF", "share of total", "budget (input)", "status"], rows,
                     fmt={1: "#,##0.00", 3: "#,##0.00", 4: "0.0%", 5: "#,##0"}, expect=exp)
    for r in range(c0, c1 + 1):
        b.an[f"F{r}"].fill = INPUT_FILL
    over_cnt = int(sum(sums[c] > BUDGET[c] for c in CATS))
    n_over = b.row("Categories over budget", f'=COUNTIF(G{c0}:G{c1},"over")', over_cnt, "0")
    biggest = max(sums, key=sums.get)
    b.row("Largest category share", f"=MAX(E{c0}:E{c1})", sums[biggest] / a.sum(), "0.0%")
    b.bar_chart_from_table("Spend by category", 1, [2], c0, c1, anchor="J4", y_title="amount")

    b.section("5. Wildcards and IFERROR")
    air = df.vendor.str.startswith("Air")
    airsum = b.row('SUMIF vendor like "Air*"', f'=SUMIF({D},"Air*",{E})', a[air].sum(), "#,##0.00",
                   "* = any characters, ? = one character")
    b.row('AVERAGEIF for category "Marketing" (not in data), wrapped in IFERROR',
          f'=IFERROR(AVERAGEIF({cat},"Marketing",{E}),0)', 0, "0.00", "without IFERROR this is #DIV/0!")

    b.section("6. IF flags and nested IF tiers (helper columns H and I)")
    flagged = b.row('Rows flagged "review" (amount > 500)', f'=COUNTIF({H},"review")', int((a > 500).sum()), "0")
    tiers = df.amount.map(tier)
    t0, t1 = b.table(["tier", "rows", "spend"], [[t, f'=COUNTIF({I},A{b.next_row + 1 + k})',
                                                  f'=SUMIF({I},A{b.next_row + 1 + k},{E})']
                                                 for k, t in enumerate(["small", "medium", "large", "refund", "missing"])],
                     fmt={2: "#,##0.00"}, expect={(k, 1): int((tiers == t).sum()) for k, t in
                                                  enumerate(["small", "medium", "large", "refund", "missing"])} | {
                         (k, 2): a[tiers == t].sum() for k, t in enumerate(["small", "medium", "large", "refund", "missing"])})

    b.section("7. COUNTIFS / SUMIFS: several conditions at once")
    tc = (df.category == "Travel") & (df.payment == "Card")
    tcc = b.row("Travel AND paid by Card: rows", f'=COUNTIFS({cat},"Travel",{F},"Card")', int(tc.sum()), "0")
    tcs = b.row("Travel AND paid by Card: spend", f'=SUMIFS({E},{cat},"Travel",{F},"Card")', a[tc].sum(), "#,##0.00")
    tf = (df.category == "Travel") & (df.date.dt.month == 2)
    tfs = b.row("Travel spend in February (month column = 2)", f'=SUMIFS({E},{cat},"Travel",{J},2)', a[tf].sum(), "#,##0.00")
    un = df.approved == "No"
    uns = b.row("Spend not approved (approved = No)", f'=SUMIFS({E},{G},"No")', a[un].sum(), "#,##0.00")

    top = max(sums, key=sums.get)
    b.answers([
        ("SUM, AVERAGE, MEDIAN, MIN, MAX of amount", f"={s}",
         f"Sum {a.sum():,.2f}; mean {a.mean():.2f}; median {a.median():.2f}; min {a.min():.2f} (a refund); max {a.max():.2f}. "
         "Mean above median: a few big expenses pull the mean up."),
        ("COUNT vs COUNTA vs COUNTBLANK on amount: how many rows have no amount?", f"={miss}",
         f"{int(a.isna().sum())} blank amounts; COUNT = COUNTA = {int(a.notna().sum())} because the column holds only numbers. "
         "AVERAGE divides by COUNT, not by the number of rows."),
        ('COUNTIF: Travel rows; amount > 500; approved = No; approved blank', f"={travel}",
         f"Travel {int((df.category == 'Travel').sum())}; over 500: {int((a > 500).sum())}; 'No': {int((df.approved == 'No').sum())}; "
         f"blank approved: {int(df.approved.isna().sum())}. A blank is not 'No'."),
        ("Which category has the largest spend and what share of the total is it?", f"=Analysis!B{c0 + CATS.index(top)}",
         f"{top}: {sums[top]:,.2f} = {sums[top] / a.sum():.1%} of the total."),
        ('Total spend with vendors whose name starts with "Air"', f"={airsum}", f"{a[air].sum():,.2f} (AirNova + AirLink)."),
        ('How many rows are flagged "review" (> 500)? How many are in each tier?', f"={flagged}",
         "Tiers small/medium/large/refund/missing: " + ", ".join(f"{t} {int((tiers == t).sum())}" for t in
                                                                  ["small", "medium", "large", "refund", "missing"]) + "."),
        ("Travel paid by Card (rows and spend); Travel spend in February", f"={tcs}",
         f"Card travel: {int(tc.sum())} rows, {a[tc].sum():,.2f}; Travel in February: {a[tf].sum():,.2f}."),
        ("How many categories are over their budget? What does IFERROR do for a category that is not in the data?", f"={n_over}",
         f"{over_cnt} over budget: " + ", ".join(c for c in CATS if sums[c] > BUDGET[c]) + ". IFERROR turns the #DIV/0! of an "
         "average over zero matching rows into 0 (or any fallback you choose)."),
        ("Why can the mean differ from the median, and why must blanks not be typed as 0?", "text",
         "AVERAGE skips blanks but includes zeros, so typing 0 for a missing receipt drags the mean down. The mean is "
         "pulled up by a few large expenses; the median is not."),
    ])
    md(out / "theory.md", THEORY)
    md(out / "task.md", TASK)
    return b


THEORY = r"""
# Theory: essential formulas

## Why these ten functions

`SUM`, `AVERAGE`, `COUNT`, `IF`, `COUNTIF`, `SUMIF` and their multi-condition versions answer most everyday questions: *how
much, how many, which ones, is it over the limit?* They also teach the one idea behind all spreadsheet analysis: a formula takes
a **range** (what to look at), optionally a **condition** (which cells count), and returns a **value**.

## Aggregates over a range

| function | returns | ignores |
|---|---|---|
| `SUM(range)` | total | blanks and text |
| `AVERAGE(range)` | sum / number of numeric cells | blanks and text (but **not** zeros) |
| `MEDIAN(range)` | middle value | blanks and text |
| `MIN`, `MAX` | smallest / largest | blanks and text |
| `COUNT(range)` | number of cells that hold a number | blanks, text |
| `COUNTA(range)` | number of non-empty cells | nothing that is non-empty |
| `COUNTBLANK(range)` | number of empty cells | - |

**Worked example.** Amounts `{120, 80, (blank), 0, 200}`: `SUM = 400`; `COUNT = 4` (the blank is skipped, the zero is counted);
`AVERAGE = 400/4 = 100`. If the blank had been typed as `0`, `AVERAGE = 400/5 = 80`. A blank means "unknown", a zero means
"nothing was spent": they are different statements, and `AVERAGE` treats them differently.

The mean is pulled by large values and the median is not. When they differ a lot the data are skewed, as with expenses (see
the main course, [distribution shapes](../../01-distribution-shapes-and-heavy-tails/theory.md)).

## IF

`=IF(condition, value_if_true, value_if_false)`. Conditions compare with `= <> < <= > >=` and can be joined with `AND(...)`,
`OR(...)`. Nest an `IF` in the false branch to build tiers:

```
=IF(E2="","missing",IF(E2<0,"refund",IF(E2<50,"small",IF(E2<500,"medium","large"))))
```

Order matters: the first true test wins, so test the special cases (`blank`, `negative`) before the ranges. For many tiers a lookup
table (lesson 3) is easier to maintain than a deep `IF`. Note that a **blank cell is `< 50` and `= 0`** in a comparison, which is
why the blank test goes first.

## COUNTIF, SUMIF, AVERAGEIF

```
=COUNTIF(range, criterion)            how many cells match
=SUMIF(range, criterion, sum_range)   add sum_range where range matches
=AVERAGEIF(range, criterion, avg_range)
```

Criteria are text or expressions in quotes: `"Travel"`, `">500"`, `"<>No"`, `">"&B2` (join an operator to a cell value so the
threshold can live in an input cell). **Wildcards**: `"Air*"` matches any text starting with Air; `"?at"` matches *cat*, *bat*.
To count empty cells use `COUNTBLANK` (it also counts cells whose formula returns `""`).

`COUNTIFS` and `SUMIFS` take several range/criterion pairs, all of which must hold (AND). Note the argument order: `SUMIFS`
puts the **sum range first**, `SUMIF` puts it last.

`SUMIF` returns 0 when nothing matches; `AVERAGEIF` returns `#DIV/0!` (an average over zero cells). Wrap with
`IFERROR(expr, fallback)` - but use it for expected cases like this one, not to silence every error: it also hides real mistakes.

## Pitfalls

1. **Text numbers**: `"1,200"` typed as text is skipped by `SUM`. Check with `COUNT` vs `COUNTA`.
2. **Ranges that do not line up** in `SUMIF`/`COUNTIFS` (different sizes) give wrong or error results.
3. **Typed constants** in criteria (`">500"`) that should be inputs.
4. **Blank vs zero vs "No"**: three different things; count them separately.
5. **Dividing by a filtered or empty count** without `IFERROR`.
6. Absolute vs relative ranges: lock them (`$E$2:$E$151`) when a formula is copied down (lesson 1).

## Next

[Lookup functions](../03-lookup-functions/theory.md)
"""

TASK = r"""
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
"""
