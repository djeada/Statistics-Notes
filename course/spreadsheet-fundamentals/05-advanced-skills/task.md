# Task: data cleaning, QUERY, FILTER, dashboards

## Scenario

Marketing exported 160 leads from the CRM and wants a sales dashboard by Friday. The export is a mess: nobody agreed how to type
country names, some people were entered twice, deal values are text, and names have random capitals and spaces. Clean it, count
each lead once, and build the dashboard.

## Data

`data.csv` - 160 rows, **all columns stored as text**, deliberately dirty.

| column | content (and what is wrong with it) |
|---|---|
| `lead_id` | unique row id |
| `created` | date as text `YYYY-MM-DD`, sometimes with spaces |
| `name` | free text: random case, leading/trailing/double spaces |
| `email` | random case and spaces; the same email can appear in two rows |
| `country` | USA / U.S.A. / United States / ... |
| `source` | web, referral or event in various spellings |
| `stage` | won, lost or open in various spellings |
| `deal_value` | text such as `1,200`, `$950`, ` 300 `, `1200.00`; blank when unknown |

## Questions

1. **Audit** (formulas, not eyeballing): how many names have stray spaces, how many emails are not already trimmed lower case, how many distinct raw country spellings are there, how many deal values are stored as text?
2. **Clean text**: add derived columns `name_clean` (`TRIM`+`PROPER`), `email_clean`, `source_clean`, `stage_clean`. Keep the raw columns.
3. **Standardise country**: build a mapping table (key → country) and a `country_key` helper (`LOWER`, remove dots and spaces, `VLOOKUP`; `UNMAPPED` if missing). How many countries remain and how many rows are unmapped?
4. **Convert deal values** to numbers (`SUBSTITUTE`, `VALUE`), keeping unknown values blank. What is the total of all deals?
5. **Convert `created`** to real dates with `DATEVALUE` and add a `month` column.
6. **Duplicates**: flag a row as `duplicate` when its clean email appeared earlier (`COUNTIF` with a growing range). How many duplicates? How many unique leads? Cross-check with a distinct count.
7. **Dashboard** (first occurrences only): KPIs (unique leads, won, lost, win rate = won / (won + lost), won revenue, average won deal, open leads); tables and charts for won revenue by country, win rate by source, new leads per month.
8. **Google Sheets only**: with `QUERY`, list won revenue by country, largest first; with `FILTER`, list won deals above 1000; with `UNIQUE`, count the distinct emails. Compare with the dashboard.
9. *Explain in three sentences* why you clean in new columns, why you remove duplicates before computing KPIs, and one risk of QUERY/FILTER.

## Deliverable

A workbook with the raw sheet untouched, the cleaned columns, a Dashboard sheet, and a short note listing every cleaning rule you applied
and the rows you could not resolve (unmapped countries, blank deal values).

Compare with `solution.xlsx`: `Dashboard` (KPIs, tables, charts), `Analysis` (audit and checks), `Sheets-only formulas` (QUERY/FILTER as text with expected results) and `Answers`.
