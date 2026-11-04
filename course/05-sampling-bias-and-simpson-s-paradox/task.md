# Task: sampling bias and Simpson's paradox

## Scenario

An e-commerce team tested a redesigned checkout (**variant B**) against the current one (**variant A**) for two weeks. The product owner
presents the headline: "B converts at 22 % versus 15 % for A - ship B!" The analyst who set up the test remembers that the two variants were switched on
through different marketing campaigns. Before the decision, you must check whether the comparison is fair, say which variant is actually better, and warn
about what the customer-satisfaction survey does and does not tell you.

## Data

`data.csv` - 2,800 checkout sessions, one row per session.

| column | meaning |
|---|---|
| `session_id` | running number |
| `date` | day of the session (2 March - 15 March 2026) |
| `device` | `desktop` or `mobile` |
| `variant` | `A` (current checkout) or `B` (redesign) |
| `converted` | 1 if the session ended in a purchase, else 0 |
| `csat` | exit-survey score 1-5, empty if the visitor did not answer |

## Questions

Work in a spreadsheet (import `data.csv`; `COUNTIFS`, `SUMIF` and `AVERAGEIF` are enough), then compare with `solution.xlsx`.

1. Compute sessions, conversions and conversion rate for A and B pooled over all sessions. Which variant wins?
2. Compute the same by device (a 2 x 2 table of device x variant). Who wins within desktop and within mobile?
3. What share of variant A's sessions and of variant B's sessions is on desktop?
4. Write each variant's pooled rate as share_desktop x rate_desktop + share_mobile x rate_mobile and verify it. What do you get if you average the two segment rates without weights?
5. Standardise both variants to the overall traffic mix (desktop share of all sessions) and compare the standardised rates.
6. Run a two-proportion z-test (A versus B) within desktop, within mobile and pooled. Report z and the two-sided p-value for each.
7. Build a day-by-day table of the pooled conversion rate of A and B and the desktop share of B. On how many of the 14 days does B beat A pooled?
8. Count the `csat` responses. What share of all sessions answered, how many answers come from non-converting sessions, and what are the mean scores for A and B? What population do those scores describe?
9. *Explain in three sentences* what went wrong in the experiment design, which number you would report to the product owner and one limitation of your fix.

## Grafana

Import `grafana/dashboard.json` (no data-source setup is needed).

- In "Conversion rate: pooled vs segments vs standardised", which bars flip the ranking compared with the pooled group?
- In "Who saw which variant?", how different are the two bars, and how does that explain the paradox?
- In "Daily pooled rate...", is the pooled advantage of B a one-off or present every day?

## Deliverable

A short note (6-10 lines) titled *Should we ship B?* with three named parts: **Headline versus segments** (pooled and per-device rates), **Why they disagree**
(the mix, with numbers) and **Recommendation** (which comparison to trust, what to run next, what the survey cannot show). Include one chart.
