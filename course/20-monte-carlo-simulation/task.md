# Task: is the product launch safe?

## Scenario

Your company plans a seasonal product launch. The finance sheet says: demand 10 000 units, price \$27, unit cost \$15, fixed launch cost \$90 000, so
**profit = \$30 000** - approve. You suspect the plan ignores uncertainty. Management accepts the launch if the probability of losing money is below
10 % and the 5th-percentile outcome is no worse than a \$20 000 loss. Build a Monte Carlo model and report whether the launch meets the rule.

Model assumptions (provided by the business):

- demand: Normal, mean 10 000, SD 2 500 units (negative values are impossible: use 0);
- the factory can make at most **11 000 units**, so units sold = MIN(demand, capacity);
- selling price: Uniform between \$24 and \$30;
- unit cost: Normal, mean \$15, SD \$1.50;
- fixed launch cost: \$90 000. Profit = units sold x (price - unit cost) - fixed cost.

## Data

`data.csv` - 2 000 trials of pre-generated uniform random numbers (so everyone gets identical results).

| column | meaning |
|---|---|
| `trial` | trial number 1-2000 |
| `u_demand` | uniform(0,1) draw used for demand: `demand = mean + sd * NORMSINV(u)` |
| `u_price` | uniform(0,1) draw used for price: `price = min + (max - min) * u` |
| `u_cost` | uniform(0,1) draw used for unit cost: `cost = mean + sd * NORMSINV(u)` |

## Questions

1. Compute the base-case profit from the average inputs.
2. Turn the draws into demand, units sold, price, unit cost and profit for all 2 000 trials. What is the **expected profit**, and how far is it from the base case? Why?
3. What is the probability of a loss (profit < 0)?
4. What are the 5th percentile of profit and the average profit in the worst 5 % of trials?
5. What is the probability of reaching a profit of \$50 000?
6. Compute the Monte Carlo standard error of the expected profit and a 95 % interval for it.
7. Using only the first 100, 200, ..., 2 000 trials, tabulate the running mean and P(loss). From about which N do they stop moving noticeably?
8. Compare trials 1-1 000 with trials 1 001-2 000 (mean, P(loss), 5th percentile). What does the difference tell you?
9. How many trials would you need to know P(loss) to within +-1 percentage point?
10. *Interpretation:* does the launch meet management's rule? Name two assumptions of the model that could change the answer.

## Grafana

Import `grafana/dashboard.json` (see `../grafana/README.md`; no data-source setup is needed).

- In "Distribution of simulated profit", what share of the bars is red, and how does that compare with the base case?
- In "Why the average misleads", what happens to units sold as demand rises above 11 000, and why does that pull the average profit below the base case?
- In "Convergence: running mean profit", after how many trials does the running mean stay inside the band, and where is the base case relative to it?

## Deliverable

A one-page risk note with named parts: **Base case vs simulation**, **Risk measures** (P(loss), 5th percentile, expected shortfall), **Precision** (Monte Carlo error),
**Decision** against the management rule and **Assumptions to challenge**. Include the profit histogram.
