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
