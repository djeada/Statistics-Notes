# Theory: sampling bias and Simpson's paradox

## Why a correct average can still point to the wrong decision

A comparison of two rates can be arithmetically right and still mislead, for two different reasons. **Selection bias** means the units you observe are not
a fair sample of the units you want to talk about (only buyers answer the exit survey; only surviving companies appear in the database). **Confounding**
means the groups you compare differ in something else that also affects the outcome - and, in the extreme, **Simpson's paradox** shows the pooled rate favouring
one group while every subgroup favours the other. Both failures come from comparing numbers without asking who is in each group and how they got there.

## Rates are weighted averages

Let a population split into segments $k=1,\dots,K$ (device, hospital, age band). If segment $k$ contains a fraction $w_k$ of the sessions and has conversion rate $p_k$,
then by the law of total probability

$$
p = \sum_{k=1}^{K} w_k\,p_k, \qquad w_k = \frac{n_k}{n}.
$$

The pooled rate is the segment rates **weighted by the traffic mix**. Two variants have comparable pooled rates only if they have the same mix $w_k$. If variant B has more
of the high-converting segment in its mix, its pooled rate is higher even when B is worse inside every segment.

## Simpson's paradox, with numbers

Toy example (conversions / sessions):

| | desktop | mobile | pooled |
|---|---|---|---|
| A | 34/100 = 34% | 100/1000 = 10% | 134/1100 = 12.2% |
| B | 270/1000 = 27% | 6/100 = 6% | 276/1100 = 25.1% |

A beats B on desktop (34% vs 27%) and on mobile (10% vs 6%), but B beats A pooled (25.1% vs 12.2%). The reason is the mix: A has only 9% desktop sessions,
B has 91%. Standardising both to a 50/50 mix gives A $0.5\cdot0.34+0.5\cdot0.10=22.0%$ and B $0.5\cdot0.27+0.5\cdot0.06=16.5%$: A is clearly better.
Note that *no arithmetic is wrong*; the paradox is that the pooled number answers a question nobody asked ("which variant did better on whatever traffic it happened to get?").

The reversal needs two ingredients: the segment variable must **change the outcome rate** a lot (desktop converts much better), and it must be **unevenly distributed across the
groups** (B got mostly desktop). If assignment is random, the mix is the same in expectation and the pooled and stratified answers agree.

## Which table is right? It depends on the causal story

- If the segment *causes the assignment* and affects the outcome (a marketing campaign sends desktop users to B): the segment is a **confounder**; compare within segments or standardise.
- If the segment is *caused by the treatment* (B's new page makes more people use the desktop site): the segment is a **mediator**; conditioning on it would remove part of the effect you want to measure,
  and the pooled number may be right.

Statistics alone cannot tell you which; you need to know how the data were generated. This is why a randomised experiment is preferable: randomisation breaks the link between
assignment and everything else (see [A/B testing](../19-a-b-testing-and-effect-sizes/theory.md)); for observational data see [confounding in regression](../13-multiple-regression-and-confounding/theory.md).

## Standardisation and tests

**Direct standardisation** reports $\sum_k w_k^{*}\,p_{k}$ with one common reference mix $w^*$ for all groups. A within-segment comparison of proportions uses the two-proportion $z$-test

$$
z=\frac{\hat p_A-\hat p_B}{\sqrt{\hat p\,(1-\hat p)\,(1/n_A+1/n_B)}},\qquad \hat p=\frac{x_A+x_B}{n_A+n_B},
$$

with a two-sided p-value $2\,(1-\Phi(|z|))$ (Excel `NORMSDIST`). Mantel-Haenszel and logistic regression with the segment as a covariate generalise this to many segments and continuous confounders.
A small $p$ in the pooled table does not rescue a biased comparison: bias is not reduced by sample size.

## Selection and survivorship bias

- **Survivorship bias**: you only see units that "made it". Classic case: armour was added where returning bombers had bullet holes, but the planes that were hit elsewhere never returned.
  In this lesson's data the exit-survey score exists only for sessions that converted: its mean says nothing about visitors who left.
- **Self-selection and non-response**: respondents to an opt-in survey differ from non-respondents (happy or furious users answer).
- **Selection on the outcome**: studying "successful startups" or "customers who stayed" to find what drives success guarantees spurious findings.
- **Sample-ratio mismatch**: if an experiment designed for 50/50 traffic shows 78/22 in some segment, assignment is broken; check the split before the result.

## Checklist before trusting a comparison

1. Who is in each group and how did they get there (random, campaign, opt-in, survival)?
2. **Table 1 / balance check**: compare the mix of key segments across groups (here: the desktop share of A and B).
3. Compute the comparison within segments and standardised; do they agree with the pooled one?
4. Is any variable used to define the sample affected by the outcome?
5. Report denominators ($x/n$), not only rates.

## Assumptions and pitfalls

1. **Stratifying on the wrong variable can create bias** (conditioning on a mediator or a collider).
2. **Too many strata** give tiny cells and noisy rates; standardisation weights then need care.
3. **Averaging rates**: never average segment rates without weights; never average a ratio of sums as a sum of ratios.
4. **Adjustment covers only what you observed**: unobserved confounders remain.
5. **Subgroup hunting**: after slicing many ways, some reversal will appear by chance ([multiple comparisons](../../notes/hypothesis_testing_and_confidence_intervals/multiple_comparisons.md)).

## Related notes

- [Percentiles and extreme values](../03-percentiles-and-extreme-values/theory.md)
- [Total probability](../../notes/probability/total_probability.md) and [conditional probability](../../notes/probability/conditional_probability.md)
- [Spurious correlation](../14-spurious-correlation-and-autocorrelation/theory.md)
- [Analysis of categorical data](../../notes/hypothesis_testing_and_confidence_intervals/analysis_of_categorical_data.md)
