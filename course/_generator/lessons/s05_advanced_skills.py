"""Spreadsheet fundamentals 5 - dashboards, QUERY, FILTER, data cleaning."""
import re
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from openpyxl.styles import Font

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import Book, md, write_csv  # noqa: E402
from _sheets_util import add_sheet_df, text_formula  # noqa: E402

SLUG = "spreadsheet-fundamentals/05-advanced-skills"
TITLE = "Advanced skills: dashboards, QUERY, FILTER, data cleaning"
MODULE = "Spreadsheet fundamentals"
DATASET = "160-row messy CRM export (spaces, case, text numbers, duplicates)"

COUNTRY_MAP = pd.DataFrame({
    "key": ["usa", "us", "unitedstates", "america", "uk", "gb", "unitedkingdom", "england", "pl", "poland", "polska", "de",
            "germany", "deutschland"],
    "country": ["United States"] * 4 + ["United Kingdom"] * 4 + ["Poland"] * 3 + ["Germany"] * 3})
RAW_COUNTRY = {"United States": ["USA", "U.S.A.", "United States", "us", " USA", "US "],
               "United Kingdom": ["UK", "U.K.", "United Kingdom", "gb", "England"],
               "Poland": ["Poland", "PL", "polska", "Poland "], "Germany": ["Germany", "DE", "Deutschland", "germany "]}
FIRST = ["Ana", "Ben", "Carla", "Dev", "Elena", "Farid", "Greta", "Hugo", "Iris", "Jon", "Kira", "Leo", "Mina", "Nils", "Olga",
         "Pavel", "Quinn", "Rosa", "Sven", "Tara", "Ugo", "Vera", "Will", "Xena", "Yuri", "Zoe"]
LAST = ["Nowak", "Smith", "Mueller", "Kowalski", "Brown", "Weber", "Taylor", "Zielinski", "Johnson", "Fischer", "Wilson", "Lewandowski"]


def mess(rng, s: str, case: bool = True) -> str:
    out = s
    r = rng.random()
    if case:
        out = out.upper() if r < .15 else out.lower() if r < .35 else out
    if rng.random() < .25:
        out = "  " + out
    if rng.random() < .25:
        out = out + " "
    return out


def make_data() -> pd.DataFrame:
    rng = np.random.default_rng(1505)
    n_unique, n_dup = 144, 16
    people = []
    seen = set()
    while len(people) < n_unique:
        f, l = rng.choice(FIRST), rng.choice(LAST)
        if (f, l) not in seen:
            seen.add((f, l))
            people.append((f, l))
    truth = []
    for i, (f, l) in enumerate(people):
        country = rng.choice(list(RAW_COUNTRY), p=[.4, .25, .2, .15])
        stage = rng.choice(["won", "lost", "open"], p=[.27, .3, .43])
        truth.append(dict(first=f, last=l, email=f"{f}.{l}@{rng.choice(['acme', 'birch', 'cedar', 'delta'])}.com".lower(),
                          country=country, source=rng.choice(["web", "referral", "event"], p=[.5, .3, .2]), stage=stage,
                          value=int(rng.integers(3, 50) * 100) if rng.random() > .08 else None,
                          created=pd.Timestamp("2026-01-05") + pd.Timedelta(days=int(rng.integers(0, 170)))))
    rows = list(truth)
    for j in rng.choice(n_unique, n_dup, replace=False):  # the same person entered again, later
        t = dict(truth[j])
        t["created"] = t["created"] + pd.Timedelta(days=int(rng.integers(3, 40)))
        t["source"] = rng.choice(["web", "referral", "event"])
        rows.append(t)
    rows.sort(key=lambda t: t["created"])
    recs = []
    for i, t in enumerate(rows):
        val = t["value"]
        sval = None if val is None else rng.choice([f"{val:,}", f"${val:,}", f" {val} ", f"{val}.00", f"{val}"])
        country = RAW_COUNTRY[t["country"]][rng.integers(0, len(RAW_COUNTRY[t["country"]]))]
        recs.append({
            "lead_id": 9001 + i,
            "created": mess(rng, t["created"].strftime("%Y-%m-%d"), case=False),
            "name": mess(rng, f"{t['first']} {t['last']}") if rng.random() > .1 else f"{t['first']}  {t['last']}",
            "email": mess(rng, t["email"]),
            "country": country,
            "source": mess(rng, t["source"]).title() if rng.random() < .5 else mess(rng, t["source"]),
            "stage": mess(rng, t["stage"]),
            "deal_value": sval})
    for k in rng.choice(len(recs), 3, replace=False):
        recs[k]["country"] = "Scotland"  # not in the mapping table
    return pd.DataFrame(recs)


def build(out: Path) -> Book:
    raw = make_data()
    write_csv(out, raw)
    n = len(raw)
    last = n + 1

    # ---- independent python cleaning (regex / pandas, not the sheet's formulas) -----------------
    c = pd.DataFrame(index=raw.index)
    c["name"] = raw.name.map(lambda s: " ".join(w.capitalize() for w in s.split()))
    c["email"] = raw.email.str.strip().str.lower()
    key = raw.country.str.strip().str.replace(".", "", regex=False).str.replace(" ", "", regex=False).str.lower()
    cmap = dict(zip(COUNTRY_MAP.key, COUNTRY_MAP.country))
    c["country"] = key.map(cmap).fillna("UNMAPPED")
    c["source"] = raw.source.str.strip().str.title()
    c["stage"] = raw.stage.str.strip().str.lower()
    c["value"] = raw.deal_value.fillna("").map(lambda s: np.nan if s.strip() == "" else float(re.sub(r"[$,\s]", "", s)))
    c["created"] = pd.to_datetime(raw.created.str.strip())
    c["serial"] = (c.created - pd.Timestamp("1899-12-30")).dt.days.astype(float)
    c["month"] = c.created.dt.month.astype(float)
    c["dup"] = np.where(c.groupby("email").cumcount() > 0, "duplicate", "first")
    uniq = c[c.dup == "first"]

    b = Book(raw, "Spreadsheet basics - data cleaning, dashboard, QUERY/FILTER",
             "Raw columns A-H are untouched; cleaned columns I-R are formulas. KPIs use first occurrences only.")
    add_sheet_df(b, "CountryMap", COUNTRY_MAP)
    NM = len(COUNTRY_MAP) + 1

    def col(name, fn, expected=None, fmt="General"):
        L = b.add_column(name, fn, None, fmt)
        if expected is not None:
            for i, v in enumerate(np.asarray(expected, dtype=float)):
                if not np.isnan(v):
                    b.checks.append((f"Data!{L}{i + 2}", f"{name} row {i + 2}", float(v)))
        return L

    # Data: A lead_id B created C name D email E country F source G stage H deal_value
    col("name_clean", lambda r: f"=PROPER(TRIM(C{r}))")  # I
    col("email_clean", lambda r: f"=LOWER(TRIM(D{r}))")  # J
    col("country_key", lambda r: f'=LOWER(SUBSTITUTE(SUBSTITUTE(TRIM(E{r}),".","")," ",""))')  # K
    col("country_clean", lambda r: f'=IFERROR(VLOOKUP(K{r},CountryMap!$A$2:$B${NM},2,FALSE),"UNMAPPED")')  # L
    col("source_clean", lambda r: f"=PROPER(TRIM(F{r}))")  # M
    col("stage_clean", lambda r: f"=LOWER(TRIM(G{r}))")  # N
    col("deal_value_clean", lambda r: f'=IF(TRIM(H{r})="","",VALUE(SUBSTITUTE(SUBSTITUTE(TRIM(H{r}),"$",""),",","")))',
        c.value, "#,##0")  # O
    col("created_date", lambda r: f"=DATEVALUE(TRIM(B{r}))", c.serial, "yyyy-mm-dd")  # P
    col("is_duplicate", lambda r: f'=IF(COUNTIF($J$2:J{r},J{r})>1,"duplicate","first")')  # Q
    col("month", lambda r: f"=MONTH(P{r})", c.month, "0")  # R
    R = lambda L: f"Data!${L}$2:${L}${last}"  # noqa: E731

    b.section("1. Audit the raw export")
    sp_names = int((raw.name.map(len) != raw.name.map(lambda s: len(" ".join(s.split())))).sum())
    a1 = b.row("Names with stray or double spaces", f"=SUMPRODUCT(--(LEN({R('C')})<>LEN(TRIM({R('C')}))))", sp_names, "0")
    bad_mail = int((raw.email != raw.email.str.strip().str.lower()).sum())
    a2 = b.row("Emails that are not already trimmed lower-case", f"=SUMPRODUCT(--(EXACT({R('D')},LOWER(TRIM({R('D')})))=FALSE))", bad_mail, "0")
    raw_countries = int(raw.country.str.lower().nunique())
    a3 = b.row("Distinct raw country spellings", f"=SUMPRODUCT(1/COUNTIF({R('E')},{R('E')}))", raw_countries, "0")
    txt = int((raw.deal_value.fillna("").str.strip() != "").sum())
    a4 = b.row("Deal values stored as text", f"=SUMPRODUCT(--ISTEXT({R('H')}))", txt, "0")
    b.row("... of which Excel/Sheets can add up as they are (COUNT)", f"=COUNT({R('H')})", 0, "0", "COUNT ignores text")

    b.section("2. After cleaning")
    cc = int(c.country.nunique())
    b2 = b.row("Distinct countries after the mapping (incl. UNMAPPED)", f"=SUMPRODUCT(1/COUNTIF({R('L')},{R('L')}))", cc, "0")
    unm = b.row("Rows that could not be mapped", f'=COUNTIF({R("L")},"UNMAPPED")', int((c.country == "UNMAPPED").sum()), "0")
    tv = b.row("Total of all deal values (now numbers)", f"=SUM({R('O')})", float(c.value.sum()), "#,##0")
    dups = b.row("Duplicate rows (same clean email as an earlier row)", f'=COUNTIF({R("Q")},"duplicate")', int((c.dup == "duplicate").sum()), "0")
    ul = b.row("Unique leads", f'=COUNTIF({R("Q")},"first")', len(uniq), "0")
    dist_email = b.row("Cross-check: distinct clean emails", f"=SUMPRODUCT(1/COUNTIF({R('J')},{R('J')}))", int(c.email.nunique()), "0")

    # ---- Dashboard sheet ---------------------------------------------------------
    dash = b.wb.create_sheet("Dashboard")
    saved_an, saved_r = b.an, b._r
    b.an, b._r = dash, 3
    dash["A1"] = "Sales dashboard (first occurrence of each lead only)"
    dash["A1"].font = Font(bold=True, size=14)
    dash.column_dimensions["A"].width = 38
    for L in "BCDEF":
        dash.column_dimensions[L].width = 16
    n0 = len(b.checks)
    won = uniq[uniq.stage == "won"]
    lost = uniq[uniq.stage == "lost"]
    Q, N, O, Lc, M, Rm = R("Q"), R("N"), R("O"), R("L"), R("M"), R("R")
    b.section("KPIs")
    k_leads = b.row("Unique leads", f'=COUNTIF({Q},"first")', len(uniq), "0")
    b.row("Duplicates removed", f'=COUNTIF({Q},"duplicate")', int((c.dup == "duplicate").sum()), "0")
    k_won = b.row("Won deals", f'=COUNTIFS({Q},"first",{N},"won")', len(won), "0")
    k_lost = b.row("Lost deals", f'=COUNTIFS({Q},"first",{N},"lost")', len(lost), "0")
    k_rate = b.row("Win rate = won / (won + lost)", f"={b.local(k_won)}/({b.local(k_won)}+{b.local(k_lost)})", len(won) / (len(won) + len(lost)), "0.0%")
    k_rev = b.row("Won revenue", f'=SUMIFS({O},{Q},"first",{N},"won")', float(won.value.sum()), "#,##0")
    b.row("Average won deal", f'=AVERAGEIFS({O},{Q},"first",{N},"won")', float(won.value.mean()), "#,##0")
    b.row("Open leads (pipeline)", f'=COUNTIFS({Q},"first",{N},"open")', int((uniq.stage == "open").sum()), "0")

    b.section("Won revenue and leads by country")
    countries = ["United States", "United Kingdom", "Poland", "Germany", "UNMAPPED"]
    h = b.next_row
    rows, exp = [], {}
    for i, ct in enumerate(countries):
        r = h + 1 + i
        rows.append([ct, f'=COUNTIFS({Q},"first",{Lc},A{r})', f'=SUMIFS({O},{Q},"first",{N},"won",{Lc},A{r})'])
        exp[(i, 1)] = int((uniq.country == ct).sum())
        exp[(i, 2)] = float(won[won.country == ct].value.sum())
    t0, t1 = b.table(["country", "unique leads", "won revenue"], rows, fmt={2: "#,##0"}, expect=exp)
    b.bar_chart_from_table("Won revenue by country", 1, [3], t0, t1, anchor="H3", y_title="revenue")

    b.section("Win rate by source")
    h = b.next_row
    rows, exp = [], {}
    sources = ["Web", "Referral", "Event"]
    for i, sname in enumerate(sources):
        r = h + 1 + i
        rows.append([sname, f'=COUNTIFS({Q},"first",{M},A{r})', f'=COUNTIFS({Q},"first",{M},A{r},{N},"won")',
                     f'=COUNTIFS({Q},"first",{M},A{r},{N},"lost")', f"=C{r}/(C{r}+D{r})"])
        u = uniq[uniq.source == sname]
        w_, l_ = int((u.stage == "won").sum()), int((u.stage == "lost").sum())
        exp.update({(i, 1): len(u), (i, 2): w_, (i, 3): l_, (i, 4): w_ / (w_ + l_)})
    s0, s1 = b.table(["source", "unique leads", "won", "lost", "win rate"], rows, fmt={4: "0.0%"}, expect=exp)
    b.bar_chart_from_table("Win rate by source", 1, [5], s0, s1, anchor="H21", y_title="win rate")

    b.section("New leads per month")
    h = b.next_row
    rows, exp = [], {}
    months = sorted(uniq.month.unique().astype(int))
    for i, m in enumerate(months):
        r = h + 1 + i
        rows.append([m, f'=COUNTIFS({Q},"first",{Rm},A{r})'])
        exp[(i, 1)] = int((uniq.month == m).sum())
    mo0, mo1 = b.table(["month", "new leads"], rows, expect=exp)
    b.line_chart_from_table("New leads per month", 1, [2], mo0, mo1, anchor="H39", x_title="month", y_title="leads")
    # the helper methods wrote 'Analysis!' into the checks: point them at this sheet
    b.checks[n0:] = [(ref.replace("Analysis!", "Dashboard!"), lab, v) for ref, lab, v in b.checks[n0:]]
    b.an, b._r = saved_an, saved_r
    k_rev, k_rate, k_leads = (x.replace("Analysis!", "Dashboard!") for x in (k_rev, k_rate, k_leads))
    b.wb.move_sheet("Dashboard", offset=-(len(b.wb.sheetnames) - 2))  # right after Data

    # ---- Google-Sheets-only formulas, stored as text ------------------------------------------------------
    sf = b.wb.create_sheet("Sheets-only formulas")
    sf["A1"] = ("QUERY, FILTER, UNIQUE, SORT and ARRAYFORMULA are not evaluated by the tool that verifies this workbook, so they are "
                "stored as text. Paste each one into an empty cell of the imported Data sheet in Google Sheets. Column D is the result it must give "
                "(FILTER, UNIQUE, SORT, ARRAYFORMULA also work in Excel 365; QUERY exists only in Google Sheets).")
    for L, w in zip("ABCD", [5, 52, 110, 60]):
        sf.column_dimensions[L].width = w
    sf["A2"], sf["B2"], sf["C2"], sf["D2"] = "#", "what it does", "formula (text)", "expected result"
    by_country = won.groupby("country").value.sum().sort_values(ascending=False)
    big = won[won.value > 1000]
    ex = [
        ("won revenue by country, largest first (first occurrences only)",
         "=QUERY(Data!A1:R161,\"select L, sum(O) where N = 'won' and Q = 'first' group by L order by sum(O) desc label sum(O) 'Won revenue'\",1)",
         "; ".join(f"{k} {v:,.0f}" for k, v in by_country.items())),
        ("won deals above 1000 among first occurrences (spills a table with all 18 columns)",
         '=FILTER(Data!A2:R161,Data!N2:N161="won",Data!O2:O161>1000,Data!Q2:Q161="first")', f"{len(big)} rows"),
        ("how many rows does that FILTER return?", '=ROWS(FILTER(Data!A2:R161,Data!N2:N161="won",Data!O2:O161>1000,Data!Q2:Q161="first"))', len(big)),
        ("distinct clean emails", "=COUNTA(UNIQUE(Data!J2:J161))", int(c.email.nunique())),
        ("sorted list of the distinct sources", "=SORT(UNIQUE(Data!M2:M161))", "Event, Referral, Web"),
        ("clean every name in one formula (spills down)", "=ARRAYFORMULA(PROPER(TRIM(Data!C2:C161)))", f"first value: {c.name.iloc[0]}"),
    ]
    for i, (what, f, res) in enumerate(ex, start=3):
        sf[f"A{i}"] = i - 2
        sf[f"B{i}"] = what
        text_formula(sf, f"C{i}", f)
        sf[f"D{i}"] = res

    ph = c.country.value_counts()
    b.answers([
        ("Audit: names with stray spaces, emails not trimmed/lower-cased, distinct raw country spellings, deal values stored as text", f"={a3}",
         f"{sp_names} names, {bad_mail} emails, {raw_countries} country spellings (for 4 real countries), {txt} deal values are text "
         "so SUM would return 0 for them."),
        ("Clean names, emails, source and stage with TRIM / PROPER / LOWER (new columns, raw kept)", "text",
         "Helper columns I, J, M, N. TRIM removes leading, trailing and repeated inner spaces; PROPER and LOWER fix the case."),
        ("Map country spellings with a lookup table: how many countries remain and how many rows are unmapped?", f"={b2}",
         f"{cc} values: 4 countries + UNMAPPED. {int((c.country == 'UNMAPPED').sum())} rows say 'Scotland', which is not in the table: "
         "decide whether to add a mapping or to ask the owner."),
        ("Convert deal values to numbers (SUBSTITUTE + VALUE): what is the total?", f"={tv}",
         f"{c.value.sum():,.0f} across {int(c.value.notna().sum())} deals; {int(c.value.isna().sum())} are blank (unknown) and stay blank, not 0."),
        ("Convert created to real dates (DATEVALUE) and add the month", "text", "Columns P and R; the dates now sort and group correctly."),
        ("Flag duplicates by the clean email: how many duplicate rows, how many unique leads?", f"={ul}",
         f"{int((c.dup == 'duplicate').sum())} duplicates; {len(uniq)} unique leads (the first occurrence is kept). Cross-check: distinct clean emails = {int(c.email.nunique())}."),
        ("Dashboard KPIs: unique leads, win rate, won revenue", f"={k_rev}",
         f"{len(uniq)} leads; {len(won)} won, {len(lost)} lost (win rate {len(won) / (len(won) + len(lost)):.1%}); won revenue {won.value.sum():,.0f}; "
         f"{int((uniq.stage == 'open').sum())} still open. See sheet Dashboard (three tables, three charts)."),
        ("QUERY: won revenue by country; FILTER: won deals above 1000; UNIQUE count of emails", "text",
         "Sheet 'Sheets-only formulas' has the formulas (text) and the expected results: " + "; ".join(f"{k} {v:,.0f}" for k, v in by_country.items())
         + f". FILTER returns {len(big)} rows; {int(c.email.nunique())} distinct emails."),
        ("Why clean in new columns, why dedupe before computing KPIs, and one risk of QUERY / FILTER?", "text",
         "Raw data are evidence - keep them and derive clean columns. Duplicates double-count leads and revenue. QUERY/FILTER results are live "
         "views: column letters inside a QUERY string do not move when you insert columns, and a FILTER with no match returns #N/A."),
    ])
    md(out / "theory.md", THEORY)
    md(out / "task.md", TASK)
    return b


THEORY = r"""
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
"""

TASK = r"""
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
"""
