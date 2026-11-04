# Theory: lookup functions

## Why

Real data lives in several tables: orders refer to a SKU, the SKU belongs in a price list; a customer id belongs in a customer
table. A **lookup** takes a key from one table, finds it in another and brings back a related value. Done with formulas instead of
copy/paste, the result updates when the source table changes.

## VLOOKUP

```
=VLOOKUP(key, table, column_number, exact?)
```

It searches the **first column** of `table` for `key` and returns the value from the `column_number`-th column of the same row.

- `exact? = FALSE` (or `0`) demands an exact match and returns `#N/A` if there is none. **This is what you want almost
  always.**
- `exact? = TRUE` (or omitted) is an *approximate* match: the table must be **sorted ascending** and the result is the row with the
  largest key that is **not above** the lookup key. That is the right tool for bands (quantity → discount, income → tax
  bracket), and a nasty trap when left on by accident: with an unsorted table it silently returns wrong values.

Limits: it cannot look **left** of the key column; the column number is a hard-coded position, so inserting a column inside the
table changes the answer; it returns the **first** match when the key repeats.

**Worked example (data of this lesson).** Price list `B:E` = (sku, unit_price, category, weight_kg). `VLOOKUP("NB-101", B:E, 2, FALSE)`
returns 4.5. `VLOOKUP("ZZ-999", B:E, 2, FALSE)` returns `#N/A`; wrap it as `IFERROR(..., "")` to keep the column numeric-friendly.
Discount bands `0→0 %, 10→3 %, 25→5 %, 50→8 %`: `VLOOKUP(49, bands, 2, TRUE)` = 5 % (largest key not above 49 is 25) and
`VLOOKUP(50, bands, 2, TRUE)` = 8 %.

## INDEX + MATCH

```
=INDEX(result_range, MATCH(key, lookup_range, 0))
```

`MATCH(key, lookup_range, 0)` returns the *position* of the key (0 = exact; `1` = largest value ≤ key in an ascending range; `-1`
= smallest value ≥ key in a descending range). `INDEX(result_range, position)` returns the item at that position. Because the lookup
range and the result range are separate, you can look **left** (product name sits left of the SKU), and inserting columns cannot break it.

**Two-way lookup.** `INDEX(grid, MATCH(row_key, row_labels, 1), MATCH(col_key, column_labels, 0))` reads a rate card: a 7.5 kg parcel
to zone B finds the 5-10 kg bracket with an approximate match on the rows and zone B with an exact match on the columns.

## XLOOKUP

```
=XLOOKUP(key, lookup_range, result_range, [if_not_found], [match_mode], [search_mode])
```

Exact match by default, built-in "not found" text, looks left or right, can return several columns, and `search_mode -1` finds
the **last** match. Available in Google Sheets and Excel 365/2021; not in Excel 2016/2019, where INDEX/MATCH remains the portable
choice. The `XLOOKUP examples` sheet of the solution stores the formulas as text with the result each should give, because
the checker used to verify the workbook (LibreOffice 24.2) cannot evaluate XLOOKUP.

## Choosing

| situation | use |
|---|---|
| quick exact lookup, key is the leftmost column | `VLOOKUP(..., FALSE)` |
| look left, or table may change shape | `INDEX/MATCH` or `XLOOKUP` |
| bands / tiers | `VLOOKUP(..., TRUE)` or `MATCH(..., 1)` on a sorted table |
| need last match, several columns, built-in fallback | `XLOOKUP` |

## Pitfalls

1. **Approximate match left on** (`TRUE`/omitted) for IDs.
2. **Duplicate keys**: the first match is returned. Customer `C007` has an old Basic record and a newer Gold record; the
   lookup silently returns Basic. De-duplicate the table or ask for the last match.
3. **Keys that look equal but are not**: `"NB-101 "` (trailing space) vs `"NB-101"`; number vs text `"7"`. Clean keys first
   (lesson 5).
4. **Missing keys** produce `#N/A`; handle with `IFERROR` for the expected case, but investigate if many appear.
5. **Hard-coded column numbers** and **unlocked table ranges** (`$B$2:$E$16`).
6. Lookup tables that are not sorted when `TRUE` is used.

## Next

[Data analysis: pivot tables, charts, conditional formatting](../04-data-analysis/theory.md)
