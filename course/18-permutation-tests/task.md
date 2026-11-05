# Task: is the new onboarding flow really faster?

## Scenario

A product team tested a redesigned onboarding flow with 10 volunteers. Five were randomly given the **new** flow and five the
**old** one; each was timed on the same set-up task. The new flow looks faster, and a colleague's t-test says
"significant". Before the redesign is rolled out to everyone, you are asked to check the claim without trusting a normal approximation:
by asking how often **random relabeling** of the same 10 numbers beats the observed difference.

## Data

`data.csv` - 10 rows, one per participant.

| column | meaning |
|---|---|
| `participant_id` | 1-10 |
| `flow` | `new` or `old` (randomly assigned, 5 each) |
| `task_minutes` | time to finish the set-up task, minutes |

## Questions

Work in a spreadsheet; the solution uses a second sheet listing every one of the $\binom{10}{5} = 252$ ways to pick which 5
participants get the "new" label (you can generate them yourself or build a smaller 3 vs 3 version by hand first).

1. Compute count, mean, median and standard deviation of `task_minutes` for each flow, and the observed differences of means and of medians (new - old).
2. How many different labelings (which 5 of 10 are "new") are there? Why is each equally likely under the null hypothesis?
3. For every labeling compute the difference of means. How many labelings give $|\text{difference}| \ge |\text{observed}|$?
4. What is the two-sided permutation p-value? What is the one-sided p-value (new is faster)?
5. Run the t-test for the same data (pooled variances, 8 degrees of freedom): t statistic and two-sided p-value (`TDIST`). Do the two tests reach the same decision at 5 %?
6. Repeat the permutation test with the difference of **medians**. What p-value do you get, and why is it coarser?
7. What is the smallest two-sided p-value this design can give? What would it be with only 3 vs 3 participants?
8. Compute Cohen's d. Is the effect large? Is the sample large enough to be sure?
9. *Interpretation:* write two sentences for the product manager - what the p-value means here, and two reasons not to roll out on this evidence alone.

## Grafana

Import `grafana/dashboard.json` (see `../grafana/README.md`; no data-source setup is needed).

- In "Task time by flow", how much do the two groups overlap?
- In "Permutation distribution: mean difference", where do the red bars lie and what share of all labelings do they make up?
- In "p-values by method", which bars are on which side of 0.05, and what does that say about trusting one test?

## Deliverable

A short note (5-8 lines) with named parts: **Result** (difference and both p-values), **Reasoning** (what the permutation p-value
counts), **Decision** (roll out / collect more data) and **Limitation**. Include one chart of the permutation distribution with the observed value marked.
