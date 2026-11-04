# Theory: data cleaning, QUERY, FILTER and dashboards

## Why

Real exports are messy: `"  ANA kowalska "`, `"U.S.A."`, `"$1,200"`, the same lead entered twice. Every formula you build on top of
messy data is quietly wrong. The craft of advanced spreadsheet work is therefore three steps in this order:
**clean → query → present**.

## 1. Data cleaning

**Golden rule: never overwrite the raw data.** Add *derived* columns next to it (or on another sheet) so every change is
visible and reversible.

| problem | symptom | tool |
|---|---|---|
| stray spaces | `"Ana "` ≠ `"Ana"` in lookups and COUNTIF | `TRIM(x)` (also collapses repeated inner spaces) |
| inconsistent case | `"WEB"`, `"web"`, `"Web"` | `LOWER`, `UPPER`, `PROPER` |
| synonyms | `USA`, `U.S.A.`, `United States` | normalise to a key, then a **mapping table** + `VLOOKUP` |
| numbers stored as text | `"$1,200"` is left-aligned, `SUM` gives 0 | `VALUE(SUBSTITUTE(SUBSTITUTE(x,"$",""),",",""))` |
| dates stored as text | `"2026-03-05 "` does not sort or group by month | `DATEVALUE(TRIM(x))`, then `MONTH` |
| duplicates | the same person counted twice | `COUNTIF($J$2:J2, J2) > 1` (running count: the first occurrence stays) |
| blanks | unknown vs zero | keep blank; `IF(TRIM(x)="","",...)` |

**Worked example.** `"  jOHN   smith "`: `TRIM` → `"jOHN smith"`; `PROPER` → `"John Smith"`. The country `"U.S.A."` →
`SUBSTITUTE(.,".","")` → `"USA"` → `LOWER` → `"usa"`, which the mapping table sends to `United States`. The deal `"$1,200"` →
remove `$` and `,` → `"1200"` → `VALUE` → 1200. Check the cleaning: `COUNT(clean_column)` should now equal the number of non-blank deals,
and the number of distinct countries should be the number of real countries (plus an `UNMAPPED` bucket you must look at).

**Running count for duplicates.** `COUNTIF($J$2:J5, J5)` counts how often the value in row 5 has appeared from row 2 down to row 5; if it is
greater than 1, this row repeats an earlier one. The anchored start (`$J$2`) and moving end (`J5`) is the mixed-reference idea from lesson 1.

**Unique count without a helper**: `SUMPRODUCT(1/COUNTIF(range, range))` counts distinct values (no blanks allowed).

## 2. QUERY and FILTER (Google Sheets; FILTER also Excel 365)

`FILTER(range, condition1, condition2, ...)` returns the rows that satisfy **all** conditions, as a spilled table:

```
=FILTER(Data!A2:R161, Data!N2:N161="won", Data!O2:O161>1000)
```

`QUERY(range, "select ... where ... group by ... order by ... label ...", headers)` runs a small SQL-like language on a range:

```
=QUERY(Data!A1:R161, "select L, sum(O) where N = 'won' and Q = 'first' group by L order by sum(O) desc label sum(O) 'Won revenue'", 1)
```

Columns are named by **letter** of the range, strings are in single quotes, the last argument is the number of header rows.
`UNIQUE`, `SORT`, `ARRAYFORMULA` complete the set: `=SORT(UNIQUE(range))`, `=ARRAYFORMULA(PROPER(TRIM(C2:C161)))`.

When to use which: `SUMIFS/COUNTIFS` for single numbers that must work everywhere; `FILTER` to *show* matching rows; `QUERY` for grouped summaries
in Google Sheets (it replaces a pivot table that updates itself); a pivot table for interactive exploration.

**Stored as text in the solution.** The checker used for this course (LibreOffice 24.2) does not evaluate QUERY/FILTER/UNIQUE/SORT, so the sheet
`Sheets-only formulas` shows each formula as text beside the result it must give. The dashboard itself uses `COUNTIFS`/`SUMIFS` and works in every spreadsheet.

Pitfalls: a column letter inside a QUERY string does not follow if you insert a column; QUERY guesses a column's type from its majority (mixed
text and numbers → numbers silently dropped, which is why cleaning comes first); FILTER with no match returns `#N/A`
(wrap with `IFERROR(..., "no rows")`); results spill and need empty cells below and to the right.

## 3. Dashboards

A dashboard answers a few questions at a glance. Method:

1. **Decide the questions first** (how many leads, how well do they convert, where does the money come from, is it growing?).
2. **KPI block** at the top: a handful of numbers computed by formulas from *clean* data (`COUNTIFS`, `SUMIFS`, `AVERAGEIFS`).
3. **One chart per question** next to its small table; chart the summary table, not the raw rows. Bars for groups, line for time.
4. Define every KPI exactly: *win rate = won / (won + lost)*, **excluding open deals** and counting each lead once.
5. Keep inputs (date range, threshold) in labelled cells, and have formulas reference them, so the dashboard can be re-used.
6. Check it: KPIs must reconcile with the raw table (total of the country table = the KPI, tables sum to the number of leads).

**Worked example of a KPI definition.** 100 unique leads, 25 won, 30 lost, 45 open: win rate $= 25/(25+30) = 45.5\%$, not $25/100 = 25\%$,
because open deals have no outcome yet. If you let 8 duplicates stay, "100 leads" becomes 108 and every revenue number is inflated.

## Pitfalls

1. Cleaning *in place*: you can no longer prove what changed.
2. Deleting rows that "look like duplicates" without agreeing which record wins (the first? the newest? merge?).
3. `UNMAPPED` swept under the rug: unmapped values are signals - add a mapping or ask the owner.
4. KPIs with undefined denominators (`#DIV/0!`) - wrap with `IFERROR` or show `n/a`.
5. Dashboards with 15 charts and no questions.

## Next

Back to the main course: [Distribution shapes and heavy tails](../../01-distribution-shapes-and-heavy-tails/theory.md) - the same spreadsheet skills, now applied to statistics.
