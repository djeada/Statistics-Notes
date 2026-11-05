# Task: correlation and lagged relationships

## Scenario

You work in growth analytics. Marketing spends on paid ads and believes "ads bring sign-ups right away"; the same-day numbers
do not show it clearly, so the budget owner wants to cut the ads. A product manager adds that the **newsletter** must be
working too, because newsletter opens and sign-ups "move together". You have 150 days of data and must decide when and whether
spend relates to sign-ups, what the newsletter relationship really is, and how much of it you can claim as cause.

## Data

`data.csv` - 150 consecutive days from 2026-01-05 (a Monday) to 2026-06-03; one row = one day.

| column | meaning |
|---|---|
| `date` | calendar day |
| `ad_spend_usd` | paid-ad spend that day (USD) |
| `signups` | new accounts created that day (count) |
| `newsletter_opens` | number of newsletter e-mails opened that day (count) |

## Questions

Work in a spreadsheet (import `data.csv`), then compare with `solution.xlsx`.

1. Compute the Pearson correlation of `ad_spend_usd` and `signups` **on the same day**. Compare with the rough noise band
   $2/\sqrt{n}$.
2. Compute the **cross-correlation** $r_k = \operatorname{corr}(\text{spend}_t, \text{signups}_{t+k})$ for $k = 0,\dots,10$. Which lag is highest?
   Why are the neighbouring lags high as well?
3. Compute the reverse direction, $\operatorname{corr}(\text{signups}_t, \text{spend}_{t+k})$, for $k = 1,\dots,10$. What does the comparison say?
4. At the best lag compute **Pearson** and **Spearman** correlation (Spearman = Pearson of the ranks; ties get average ranks). Find the day with
   the most sign-ups and say what it does to the two coefficients.
5. Fit a line of sign-ups on spend (at the best lag). How many extra sign-ups per extra 1,000 USD?
6. Compute the correlation of `newsletter_opens` and `signups`. Then subtract each weekday's average from both columns and correlate again.
   What changes, and what does it mean?
7. Explain in two sentences why the profile in question 2 has a wide hump instead of one spike.
8. *Interpretation:* what can you conclude about ads and about the newsletter, and what would you need to claim that ads *cause* sign-ups?

## Grafana

Import `grafana/dashboard.json` (see `../grafana/README.md`; no data-source setup is needed).

- On "Standardised sign-ups and ad spend", which curve do the sign-up peaks follow, and by how many days is it late?
- On "Cross-correlation by lag", why do the two bar series look different?
- Compare the three scatter plots: which alignment gives a tight cloud, and which point does not fit?

## Deliverable

A short note (6-8 lines) to the budget owner with named parts: **Timing** (the lag and how sure you are), **Strength** (correlation
and extra sign-ups per 1,000 USD), **Newsletter** (why the correlation is not an effect) and **Caveat** (what correlation cannot tell you).
