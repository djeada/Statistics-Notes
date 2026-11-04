# Task: how long does a ticket take to resolve?

## Scenario

A support team advertises that its **average ticket resolution time is under 8 hours**. Management has a sample of 30
resolved tickets and asks: *can we keep making this promise?* The times are clearly not bell-shaped, so you decide to
compare the textbook interval with a bootstrap interval. Random draws were generated in advance so every analyst gets the
same resamples.

## Data

`data.csv` - two blocks in one table:

| column | meaning |
|---|---|
| `ticket_id` | 1-30 (rows 1-30 only; blank below) |
| `resolution_hours` | time from opening to resolution, hours (rows 1-30 only) |
| `resample` | resample number 1-400 |
| `draw_01` ... `draw_30` | for resample `r`, the 30 ticket numbers drawn **with replacement** (so `draw_05 = 17` means "the 5th value of resample `r` is ticket 17") |

n = 30 tickets; 400 resamples of size 30. A resample value is `=INDEX(resolution_hours range, draw cell)`.

## Questions

1. Compute the mean, median, standard deviation, skewness and largest value of `resolution_hours`.
2. Compute the standard error of the mean and the **95 % t interval** (`TINV`). Does it contain the 8 h promise?
3. Build the 400 resamples (30 `INDEX` lookups each) and compute the mean of every resample. What is the **bootstrap standard error**
   (standard deviation of the 400 means)? Compare with $s/\sqrt n$.
4. Compute the **95 % percentile bootstrap interval** for the mean. Compare its width and its shape (distance from the sample mean to each end) with the t interval.
5. Compute the bootstrap interval for the **median**. Why can't you get this one from a simple formula?
6. Recompute the interval using only the first 50, 100, 200 and 400 resamples. How stable are the ends?
7. What is the bootstrap **bias** (mean of the resample means minus the sample mean)?
8. Change the confidence level to 90 % and 99 %. What happens to both intervals?
9. *Interpretation:* in two or three sentences, state what the 95 % interval means (and what it does not), and name one reason to
   distrust the interval with this sample.

## Grafana

Import `grafana/dashboard.json` (see `../grafana/README.md`; no data-source setup is needed).

- In "The data" panel, describe the shape. What does it imply for a symmetric interval?
- In the two bootstrap-distribution panels, which values form the central 95 % (blue bars)? Compare the arms of the mean's distribution around its centre.
- In "Interval comparison", which interval would you show to management, and why?

## Deliverable

A short note (5-8 lines) with named parts: **Estimate** (mean and median), **Uncertainty** (the two intervals), **Decision** (can
the promise be kept? say "cannot tell" if that is the answer) and **Limitation**. Include one chart of the bootstrap distribution.
