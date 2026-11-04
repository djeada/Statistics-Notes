"""Spreadsheet fundamentals 3 - VLOOKUP, XLOOKUP, INDEX + MATCH."""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import INPUT_FILL, Book, md, write_csv  # noqa: E402
from _sheets_util import add_sheet_df, text_formula, write_csv_named  # noqa: E402

SLUG = "spreadsheet-fundamentals/03-lookup-functions"
TITLE = "Lookup functions: VLOOKUP, XLOOKUP, INDEX + MATCH"
MODULE = "Spreadsheet fundamentals"
DATASET = "120 orders + product, customer, discount and shipping tables"

PRODUCTS = pd.DataFrame({
    "product_name": ["A5 Notebook", "Gel Pen Box", "Stapler", "Desk Lamp", "Whiteboard", "Office Chair", "Paper Ream",
                     "Marker Set", "Desk Organiser", "Monitor Stand", "Headset", "Webcam", "Label Printer", "Shredder", "Footrest"],
    "sku": ["NB-101", "PN-210", "ST-330", "LM-410", "WB-520", "CH-600", "PA-115", "MK-225", "DO-340", "MS-450", "HS-710",
            "WC-720", "LP-810", "SH-820", "FR-630"],
    "unit_price": [4.5, 6.2, 12.9, 29.0, 55.0, 89.0, 5.8, 9.4, 15.5, 34.0, 62.0, 48.0, 79.0, 120.0, 25.0],
    "category": ["Paper", "Writing", "Desk", "Desk", "Board", "Furniture", "Paper", "Writing", "Desk", "Desk", "Tech", "Tech",
                 "Tech", "Tech", "Furniture"],
    "weight_kg": [0.2, 0.15, 0.4, 1.8, 6.0, 9.5, 2.5, 0.3, 0.9, 2.2, 0.4, 0.2, 1.6, 8.0, 1.5],
})
CUSTOMERS = pd.DataFrame({
    "customer_id": [f"C{i:03d}" for i in range(1, 21)] + ["C007"],
    "customer_name": ["Acme Ltd", "Birch & Co", "Cedar School", "Delta Studio", "Elm Clinic", "Fjord Foods", "Granite Law",
                      "Harbor Cafe", "Iris Dental", "Juniper Labs", "Kite Travel", "Lark Books", "Maple Bakery", "Nova Tech",
                      "Oak Garage", "Pine Hotel", "Quartz Design", "Ridge Gym", "Sage Spa", "Tide Marine", "Granite Law"],
    "tier": ["Gold", "Basic", "Basic", "Silver", "Basic", "Gold", "Basic", "Silver", "Basic", "Gold", "Silver", "Basic",
             "Basic", "Gold", "Basic", "Silver", "Basic", "Basic", "Silver", "Gold", "Gold"],
})  # C007 appears twice: an old Basic record first, a newer Gold record last
DISCOUNTS = pd.DataFrame({"min_qty": [0, 10, 25, 50], "discount": [0.0, 0.03, 0.05, 0.08]})
RATE = pd.DataFrame({"weight_from_kg": [0, 1, 5, 10, 25], "A": [5, 8, 12, 18, 30], "B": [7, 11, 16, 24, 40],
                     "C": [9, 14, 21, 32, 55]})


def make_orders() -> pd.DataFrame:
    rng = np.random.default_rng(1303)
    n = 120
    sku = rng.choice(PRODUCTS.sku, n).astype(object)
    sku[rng.choice(n, 6, replace=False)] = rng.choice(["ZZ-999", "OLD-001"], 6)  # discontinued SKUs
    cust = rng.choice(CUSTOMERS.customer_id.unique(), n).astype(object)
    cust[rng.choice(n, 3, replace=False)] = "C099"  # not in the customer table
    qty = rng.choice([1, 2, 3, 5, 8, 10, 12, 15, 20, 30, 40, 60], n, p=[.14, .12, .1, .1, .1, .1, .09, .07, .07, .05, .04, .02])
    return pd.DataFrame({
        "order_id": 2001 + np.arange(n),
        "order_date": pd.to_datetime("2026-02-02") + pd.to_timedelta(np.sort(rng.integers(0, 56, n)), unit="D"),
        "sku": sku, "customer_id": cust, "qty": qty, "zone": rng.choice(["A", "B", "C"], n, p=[.5, .3, .2])})


def build(out: Path) -> Book:
    orders = make_orders()
    write_csv(out, orders)
    write_csv_named(out, "products.csv", PRODUCTS)
    write_csv_named(out, "customers.csv", CUSTOMERS)
    write_csv_named(out, "discounts.csv", DISCOUNTS)
    write_csv_named(out, "rate_card.csv", RATE)
    n = len(orders)
    last = n + 1

    # ---- independent python expectations ------------------------------------
    price = orders.sku.map(PRODUCTS.set_index("sku").unit_price)
    pname = orders.sku.map(PRODUCTS.set_index("sku").product_name).fillna("UNKNOWN")
    wkg = orders.sku.map(PRODUCTS.set_index("sku").weight_kg) * orders.qty
    first = CUSTOMERS.drop_duplicates("customer_id", keep="first").set_index("customer_id")
    cname = orders.customer_id.map(first.customer_name).fillna("UNKNOWN")
    ctier = orders.customer_id.map(first.tier)
    disc = pd.Series(np.array(DISCOUNTS.discount)[np.searchsorted(DISCOUNTS.min_qty, orders.qty, side="right") - 1])
    total = orders.qty * price
    net = total * (1 - disc)
    bracket = np.searchsorted(RATE.weight_from_kg.to_numpy(), wkg.to_numpy(float), side="right") - 1
    zcol = orders.zone.map({"A": 0, "B": 1, "C": 2}).to_numpy()
    fee = pd.Series(np.where(wkg.isna(), np.nan, RATE[["A", "B", "C"]].to_numpy()[np.nan_to_num(bracket).astype(int), zcol]))

    b = Book(orders, "Spreadsheet basics - lookup functions",
             "Reference tables live on sheets Products, Customers, Discounts, RateCard.")
    add_sheet_df(b, "Products", PRODUCTS, {"unit_price": "0.00"})
    add_sheet_df(b, "Customers", CUSTOMERS)
    add_sheet_df(b, "Discounts", DISCOUNTS, {"discount": "0%"})
    add_sheet_df(b, "RateCard", RATE.rename(columns={"weight_from_kg": "weight_from_kg"}))
    NP, NC = len(PRODUCTS) + 1, len(CUSTOMERS) + 1

    def col(name, fn, expected, fmt="0.00"):
        """Add a formula column in *every* row (blank results are "" strings) and check the numeric rows."""
        L = b.add_column(name, fn, None, fmt)
        if expected is not None:
            for i, v in enumerate(np.asarray(expected, dtype=float)):
                if not np.isnan(v):
                    b.checks.append((f"Data!{L}{i + 2}", f"{name} row {i + 2}", float(v)))
        return L

    # Data columns: A id, B date, C sku, D customer_id, E qty, F zone
    col("product_name", lambda r: f'=IFERROR(INDEX(Products!$A$2:$A${NP},MATCH(C{r},Products!$B$2:$B${NP},0)),"UNKNOWN")', None)
    col("unit_price", lambda r: f'=IFERROR(VLOOKUP(C{r},Products!$B$2:$E${NP},2,FALSE),"")', price)
    col("line_total", lambda r: f'=IF(H{r}="","",E{r}*H{r})', total)
    col("customer_name", lambda r: f'=IFERROR(VLOOKUP(D{r},Customers!$A$2:$C${NC},2,FALSE),"UNKNOWN")', None)
    col("tier", lambda r: f'=IFERROR(VLOOKUP(D{r},Customers!$A$2:$C${NC},3,FALSE),"")', None)
    col("discount", lambda r: f"=VLOOKUP(E{r},Discounts!$A$2:$B$5,2,TRUE)", disc, "0%")
    col("net_total", lambda r: f'=IF(I{r}="","",I{r}*(1-L{r}))', net)
    col("weight_kg", lambda r: f'=IFERROR(E{r}*VLOOKUP(C{r},Products!$B$2:$E${NP},4,FALSE),"")', wkg)
    col("ship_fee", lambda r: f'=IF(N{r}="","",INDEX(RateCard!$B$2:$D$6,MATCH(N{r},RateCard!$A$2:$A$6,1),MATCH(F{r},RateCard!$B$1:$D$1,0)))',
        fee, "0")
    R = lambda L: f"Data!${L}$2:${L}${last}"  # noqa: E731

    b.section("1-2. Exact match: unknown SKUs and revenue")
    unk = b.row('Orders whose SKU is not in the price list ("UNKNOWN")', f'=COUNTIF({R("G")},"UNKNOWN")', int((pname == "UNKNOWN").sum()), "0")
    rev = b.row("Revenue of the priced orders (sum of line_total)", f"=SUM({R('I')})", total.sum(), "#,##0.00")
    b.row("Rows that could not be priced (COUNTBLANK-style check)", f'=COUNTIF({R("H")},"")', int(price.isna().sum()), "0")

    b.section("3. Customers: first match wins")
    dup = b.row("Rows for customer C007 in the Customers table", f'=COUNTIF(Customers!$A$2:$A${NC},"C007")', 2, "0")
    nocust = b.row('Orders from customers missing in the table ("UNKNOWN")', f'=COUNTIF({R("J")},"UNKNOWN")', int((cname == "UNKNOWN").sum()), "0")
    gold = b.row('Orders placed by "Gold" tier customers (first-match tier)', f'=COUNTIF({R("K")},"Gold")', int((ctier == "Gold").sum()), "0")
    b.row("Tier VLOOKUP returns for C007 (first match)", f'=VLOOKUP("C007",Customers!$A$2:$C${NC},3,FALSE)', None)

    b.section("4. Approximate match: quantity discount")
    b.row("Discount at quantity 50 (VLOOKUP, TRUE)", "=VLOOKUP(50,Discounts!$A$2:$B$5,2,TRUE)", 0.08, "0%")
    b.row("Discount at quantity 49", "=VLOOKUP(49,Discounts!$A$2:$B$5,2,TRUE)", 0.05, "0%", "49 is still in the 25-49 band")
    tot_disc = b.row("Total discount given (line_total - net_total)", f"=SUM({R('I')})-SUM({R('M')})", (total - net).sum(), "#,##0.00")
    d5 = b.row("Orders in the 5% band", f"=COUNTIF({R('L')},0.05)", int((disc == 0.05).sum()), "0")

    b.section("5. Two-way lookup: shipping fee from weight bracket and zone")
    wi = b.row("Parcel weight (kg)", 7.5, None, "0.0", is_input=True)
    zi = b.row("Zone", "B", None, "@", is_input=True)
    fee_card = b.row("Fee for that parcel: INDEX + MATCH(approx) + MATCH(exact)",
                     f"=INDEX(RateCard!$B$2:$D$6,MATCH({b.local(wi)},RateCard!$A$2:$A$6,1),MATCH({b.local(zi)},RateCard!$B$1:$D$1,0))", 16, "0")
    ship = b.row("Total shipping fees over all orders", f"=SUM({R('O')})", fee.sum(), "#,##0")
    b.row("Average fee per shippable order", f"=AVERAGE({R('O')})", fee.mean(), "0.00")

    b.section("6. Order card: type an order id, get the details")
    oid = b.row("Order id (input)", 2037, None, "0", is_input=True)
    k = 2037 - 2001
    m = f"MATCH({b.local(oid)},{R('A')},0)"
    b.row("Order date", f"=INDEX({R('B')},{m})", None, "yyyy-mm-dd")
    b.row("Product", f"=INDEX({R('G')},{m})", None, "@")
    b.row("Customer", f"=INDEX({R('J')},{m})", None, "@")
    card_net = b.row("Net total", f"=INDEX({R('M')},{m})", net.iloc[k], "#,##0.00")

    # ---- XLOOKUP examples as TEXT: LibreOffice 24.2 (used to verify this workbook) does not evaluate XLOOKUP -------
    xs = b.wb.create_sheet("XLOOKUP examples")
    xs["A1"] = ("These formulas are stored as text because the checker cannot evaluate XLOOKUP. Paste them into a cell of "
                "Google Sheets or Excel 365 (they refer to this workbook's sheets). Column D shows the result they must give.")
    xs.column_dimensions["A"].width = 8
    xs.column_dimensions["B"].width = 100
    xs.column_dimensions["C"].width = 22
    xs.column_dimensions["D"].width = 22
    ex = [
        ("1", 'exact match, with a fallback instead of #N/A (row 2 of Data)', '=XLOOKUP(C2,Products!B:B,Products!C:C,"not found")', price.iloc[0]),
        ("2", "look LEFT of the key column (product name for the SKU in row 2) - VLOOKUP cannot do this",
         '=XLOOKUP(C2,Products!B:B,Products!A:A,"UNKNOWN")', pname.iloc[0]),
        ("3", "unknown SKU on purpose", '=XLOOKUP("ZZ-999",Products!B:B,Products!C:C,"not found")', "not found"),
        ("4", "approximate: the discount for quantity 49 (match_mode -1 = exact or next smaller)",
         "=XLOOKUP(49,Discounts!A:A,Discounts!B:B,,-1)", 0.05),
        ("5", "LAST match instead of the first (search_mode -1): tier of C007",
         '=XLOOKUP("C007",Customers!A:A,Customers!C:C,,0,-1)', "Gold"),
        ("6", "return several columns at once (name and tier of C020) - spills into two cells",
         '=XLOOKUP("C020",Customers!A:A,Customers!B:C)', "Tide Marine | Gold"),
    ]
    for i, (num, desc, f, res) in enumerate(ex, start=3):
        xs[f"A{i}"] = num
        xs[f"B{i}"] = desc
        text_formula(xs, f"C{i}", f)
        xs[f"D{i}"] = res if not isinstance(res, float) else float(res)
    xs["B2"], xs["C2"], xs["D2"] = "what it shows", "formula (text)", "expected result"
    xs.column_dimensions["C"].width = 70

    b.answers([
        ("VLOOKUP the unit price by SKU (exact match). How many orders cannot be priced and what is the revenue of the rest?",
         f"={rev}", f"{int((pname == 'UNKNOWN').sum())} orders have a discontinued SKU (IFERROR turns #N/A into blank). Priced revenue = {total.sum():,.2f}."),
        ("Return the product name with INDEX + MATCH (the name is left of the SKU). How many UNKNOWN?", f"={unk}",
         f"{int((pname == 'UNKNOWN').sum())} UNKNOWN. VLOOKUP cannot return a column to the left of its key; INDEX/MATCH and XLOOKUP can."),
        ("How many rows does customer C007 have, which tier does VLOOKUP return, and how many orders come from unknown customers?",
         f"={dup}", f"2 rows; VLOOKUP returns the FIRST one (Basic) although the newer record says Gold. {int((cname == 'UNKNOWN').sum())} orders "
         "have customer C099, which is not in the table. De-duplicate the lookup table or use XLOOKUP search_mode -1."),
        ("Quantity discount with approximate match: total discount given; orders in the 5 % band", f"={tot_disc}",
         f"Discount total {(total - net).sum():,.2f}; {int((disc == 0.05).sum())} orders have 25-49 units. The table must be sorted "
         "ascending by the key; quantity 49 gets 5 %, quantity 50 gets 8 %."),
        ("Shipping: fee for a 7.5 kg parcel to zone B; total shipping over all orders", f"={fee_card}",
         f"7.5 kg falls in the 5-10 kg bracket: 16. Total shipping {fee.sum():,.0f} for {int(fee.notna().sum())} shippable orders."),
        ("Order card: what is the net total of order 2037?", f"={card_net}",
         f"{net.iloc[k]:,.2f} for {orders.sku.iloc[k]} x {orders.qty.iloc[k]} ({cname.iloc[k]})."),
        ("Write the XLOOKUP versions of the price, the product name and the LAST tier of C007", "text",
         f"See sheet 'XLOOKUP examples' (formulas stored as text, with the result each must give; for the order in row 2: {price.iloc[0]} / {pname.iloc[0]} / Gold)."),
        ("When does VLOOKUP break and why are INDEX/MATCH or XLOOKUP safer?", "text",
         "VLOOKUP counts columns by number (insert a column and the answer changes), cannot look left, and defaults to approximate "
         "matching. INDEX/MATCH and XLOOKUP point at the actual lookup and result columns, handle left lookups and take an explicit "
         "exact-match setting."),
    ])
    md(out / "theory.md", THEORY)
    md(out / "task.md", TASK)
    return b


THEORY = r"""
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
"""

TASK = r"""
# Task: lookup functions

## Scenario

The warehouse exports orders with only a SKU, a customer id and a quantity. To invoice them you must add the price, the
product name, the customer, a quantity discount and a shipping fee, each from a different reference table. The tables are not perfect:
some SKUs were discontinued, a few customers are not in the customer list, and one customer id appears twice.

## Data

| file | content |
|---|---|
| `data.csv` | 120 orders: `order_id`, `order_date`, `sku`, `customer_id`, `qty`, `zone` (A, B or C) |
| `products.csv` | `product_name`, `sku`, `unit_price`, `category`, `weight_kg` - note the SKU is the **second** column |
| `customers.csv` | `customer_id`, `customer_name`, `tier` (C007 appears twice) |
| `discounts.csv` | quantity bands: `min_qty`, `discount` |
| `rate_card.csv` | shipping fee by `weight_from_kg` and zone A / B / C |

Import each file as its own sheet of one workbook (Products, Customers, Discounts, RateCard).

## Questions

1. Add `unit_price` to each order with `VLOOKUP(..., FALSE)` and `line_total = qty * unit_price`. How many orders cannot be priced? What is the revenue of the rest? Use `IFERROR` so unknown SKUs give a blank.
2. Add `product_name` with `INDEX` + `MATCH` (why can't VLOOKUP do it here?). How many rows are `UNKNOWN`?
3. Add `customer_name` and `tier` with VLOOKUP. Which tier does C007 get, and why is that questionable? How many orders come from customers that are not in the table?
4. Add `discount` with an approximate-match lookup on the quantity bands and `net_total = line_total * (1 - discount)`. What is the total discount given? What does quantity 49 get and what does 50 get?
5. Add `weight_kg = qty * product weight` and `ship_fee` with a two-way lookup (weight bracket by approximate `MATCH`, zone by exact `MATCH`). What is the fee for a 7.5 kg parcel to zone B? What is the total shipping?
6. Build an "order card": type an order id in an input cell and show the date, product, customer and net total with `INDEX`/`MATCH`. What is the net total of order 2037?
7. Rewrite the price lookup, the product-name lookup and the **last** tier of C007 with `XLOOKUP` (Google Sheets or Excel 365). Check against `solution.xlsx`, sheet `XLOOKUP examples`.
8. *Explain in two sentences* what can go wrong with `VLOOKUP` and why INDEX/MATCH or XLOOKUP is safer.

## Deliverable

An invoice-ready orders sheet (price, name, customer, discount, shipping) plus a note listing the data problems the lookups
exposed (discontinued SKUs, unknown customers, the duplicate customer) and what you would ask the data owner to fix.

Compare with `solution.xlsx` (`Answers`, `Analysis`, helper columns on `Data`).
"""
