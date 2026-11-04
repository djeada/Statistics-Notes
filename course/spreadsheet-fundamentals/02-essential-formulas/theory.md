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
