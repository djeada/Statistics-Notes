# Multiple Comparisons

When conducting multiple hypothesis tests, the probability of making at least one Type I error—falsely rejecting a true null hypothesis—increases. This is known as the **multiple comparisons problem** or, in some contexts, the **look-elsewhere effect**.

Methods for addressing this problem typically adjust significance thresholds or p-values. Different methods control different types of error and involve different trade-offs between false positives and statistical power.

## Data Snooping and the Multiple Testing Fallacy

* A Swedish power-line study, published by [Feychting and Ahlbom in 1993](https://pubmed.ncbi.nlm.nih.gov/8213751/), reported an association between calculated magnetic-field exposure and childhood leukemia. Evaluating this observational result requires the study design, exposure definitions, uncertainty, and subsequent evidence.
* A historical association should not be labeled a multiple-testing artifact merely because several outcomes were examined. The relevant question is which analyses were prespecified, which were selected after exploration, and what family of claims the inference was intended to cover. The hypothetical example below isolates the mathematical multiplicity issue without attributing an unsupported number of tests to that study.
* The **multiple testing fallacy** occurs when many tests are performed without accounting for the increased chance of false positives. For example, if 800 independent null hypotheses are all true and each is tested at a 1% significance level, about 8 false positives would be expected on average.

### Multiple Comparisons Problem

* A **p-value** is the probability, assuming the null hypothesis is true, of obtaining a result at least as extreme as the one observed. A smaller p-value indicates stronger evidence against the null hypothesis.
* The **look-elsewhere effect** refers to the increased chance of finding an apparently significant result when many possible comparisons are examined.
* **Data snooping** is the broader practice of repeatedly exploring data and then treating selected patterns as if they had been specified in advance.

### Reproducibility and Replicability Crisis

* **Reproducibility** refers to obtaining the same results using the same data and analysis procedures, while **replicability** refers to obtaining consistent results in a new study using new data.
* Concerns about the reliability of published findings are often described as the **reproducibility and replicability crisis**. Practices such as extensive data exploration, selective reporting, and uncorrected multiple testing can contribute to this problem. John Ioannidis's 2005 essay, [*Why Most Published Research Findings Are False*](https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.0020124), develops a model relating the credibility of findings to power, bias, multiplicity, and the proportion of tested relationships that are real. Its conclusions depend on those modeling assumptions rather than supplying a universal measured fraction of false papers.

### Addressing the Multiple Testing Problem

* The **Bonferroni correction** controls the probability of making at least one Type I error across a family of tests. It can be implemented by dividing the desired family-wise significance level by the number of tests, or equivalently by multiplying each p-value by the number of tests. The method is simple but can be conservative, reducing statistical power.
* The **false discovery proportion (FDP)** is the proportion of rejected null hypotheses that are actually false discoveries. For example, if 80 true discoveries and 41 false discoveries are made, then the FDP is:

$$
\frac{41}{80+41}\approx0.34
$$

so about 34% of the reported discoveries are false positives.

### False Discovery Rate (FDR)

* The **false discovery rate (FDR)** is the expected value of the false discovery proportion.
* The **Benjamini-Hochberg procedure** controls the FDR by ranking p-values and comparing them with thresholds that depend on their rank. It is generally less conservative than methods designed to control the family-wise error rate.

### Using a Validation Set to Avoid Data Snooping

* The **validation set approach** divides the available data into separate sets so that exploratory findings can be evaluated on data that were not used to generate them.
* The **model-building set** is used to explore the data and identify possible relationships.
* The **validation set** is reserved for evaluating hypotheses or models that emerged during the exploratory phase.
* It is important that the validation set remain separate from the exploratory analysis. Repeatedly examining or tuning decisions based on the validation set can reintroduce data snooping.

## Family-wise Error Rate (FWER)

The family-wise error rate (FWER) is the probability of making at least one Type I error among a defined family of hypothesis tests. Controlling FWER limits the probability of any false rejection within that family.

### Bonferroni Correction

If $m$ independent tests are each run at level $\alpha$ and all null hypotheses are true, the probability of at least one false rejection is

$$
1-(1-\alpha)^m.
$$

For $m=20$ and $\alpha=0.05$ this is $1-0.95^{20}\approx0.64$. The Bonferroni correction is a common method for controlling the FWER. If the desired family-wise significance level is $\alpha$ and $m$ tests are performed, each individual test uses:

$$
\alpha_{\text{adjusted}} = \frac{\alpha}{m}
$$

The Bonferroni correction is conservative, particularly when many tests are performed. This reduces the probability of false positives but can increase the probability of Type II errors, where a false null hypothesis is not rejected.

### Example: Bonferroni Correction

Suppose we conduct 20 hypothesis tests and want to control the family-wise error rate at $\alpha = 0.05$. The Bonferroni-adjusted significance level is:

$$
\alpha_{\text{adjusted}} = \frac{\alpha}{m} = \frac{0.05}{20} = 0.0025
$$

where:

* $\alpha = 0.05$ is the desired family-wise significance level,
* $m = 20$ is the number of tests.

**Conclusion:**

After applying the Bonferroni correction, we reject the null hypothesis for an individual test only if its p-value is less than or equal to $0.0025$.

This controls the family-wise error rate at no more than 0.05, but the stricter threshold also reduces power and can increase the number of false negatives.

Bonferroni does not require independence. If $I_0$ indexes the true nulls and every null p-value is valid, the union bound gives

```math
P(\text{at least one false rejection})
\leq\sum_{i\in I_0}P(p_i\leq\alpha/m)
\leq |I_0|\alpha/m\leq\alpha.
```

The independent-tests expression above computes an exact probability when the null rejection probabilities equal $\alpha$ and rejections are independent. The bound here remains valid with dependence. Adjusted Bonferroni p-values are $\min(1,mp_i)$ so they remain on the probability scale.

## False Discovery Rate (FDR)

Unlike FWER, which controls the probability of making at least one false rejection, the false discovery rate controls the expected proportion of false discoveries among all rejected null hypotheses.

FDR-controlling procedures are generally more powerful than FWER-controlling methods, making them useful in exploratory settings where many hypotheses are tested and some false discoveries can be tolerated.

Write $V$ for the number of false rejections and $R$ for the total number of rejections. Define $\mathrm{FDP}=V/\max(R,1)$, so it is zero when no discoveries are reported, and $\mathrm{FDR}=E[\mathrm{FDP}]$. Controlling this expectation at 5% does not guarantee that every realized discovery list contains at most 5% false entries. FWER instead controls $P(V\geq1)$. When all nulls are true, any nonempty discovery list has FDP one, so FDR and FWER coincide in that special case.

### Benjamini-Hochberg Procedure

The Benjamini-Hochberg (BH) procedure controls the FDR by ordering the p-values from smallest to largest:

$$
p_{(1)} \leq p_{(2)} \leq \cdots \leq p_{(m)}
$$

Each ordered p-value is compared with:

$$
\frac{i}{m}\alpha
$$

where:

* $i$ is the rank of the p-value,
* $m$ is the total number of tests,
* $\alpha$ is the desired FDR level.

We find the largest rank $k$ such that:

$$
p_{(k)} \leq \frac{k}{m}\alpha
$$

and reject the null hypotheses corresponding to:

$$
p_{(1)},\ldots,p_{(k)}.
$$

If no rank satisfies the inequality, reject none. Otherwise the step-up rule rejects every rank up to $k$; it does not stop at the first failed comparison. The standard BH guarantee requires valid null p-values and independence or a suitable positive regression dependence condition. Arbitrary dependence is not covered by that guarantee; the Benjamini-Yekutieli adjustment uses the additional harmonic factor $\sum_{j=1}^m1/j$ in the thresholds to obtain broader dependence protection.

### Example: Multiple Hypothesis Testing

Suppose we conduct six hypothesis tests and obtain the p-values:

$$
\{0.001, 0.008, 0.039, 0.041, 0.042, 0.06\}
$$

The following example uses the **Holm-Bonferroni procedure**, which controls the family-wise error rate rather than the false discovery rate.

We apply the procedure at $\alpha = 0.05$ by comparing each ordered p-value with a sequentially adjusted significance level.

**Step-by-Step Procedure:**

I. **Order the p-values** in ascending order:

$$
0.001, 0.008, 0.039, 0.041, 0.042, 0.06
$$

II. **Adjust the significance level** for each test:

$$
\alpha_i = \frac{\alpha}{m-i+1}
$$

where $m=6$ and $\alpha=0.05$.

III. **Compare each p-value with its adjusted threshold**:

For $p_1 = 0.001$:

$$
0.001 < \frac{0.05}{6} \approx 0.00833
\quad \text{(Reject $H_0$)}
$$

For $p_2 = 0.008$:

$$
0.008 < \frac{0.05}{5} = 0.01
\quad \text{(Reject $H_0$)}
$$

For $p_3 = 0.039$:

$$
0.039 > \frac{0.05}{4} = 0.0125
\quad \text{(Fail to reject $H_0$)}
$$

The Holm-Bonferroni procedure stops at the first hypothesis that is not rejected. Therefore, the remaining hypotheses are also not rejected.

For comparison, the Benjamini-Hochberg thresholds $\frac{i}{6}(0.05)$ are $0.0083,\,0.0167,\,0.025,\,0.0333,\,0.0417,\,0.05$. The largest $i$ with $p_{(i)}\le\frac{i}{6}(0.05)$ is $i=2$ (since $0.039>0.025$, $0.041>0.0333$, $0.042>0.0417$, and $0.06>0.05$), so BH also rejects the first two hypotheses here. BH can reject more hypotheses than Holm in other settings, because its FDR guarantee is weaker than FWER control.

![Figure for Example: Multiple Hypothesis Testing](https://github.com/user-attachments/assets/e1dfbabc-e720-448d-a8b3-228f91d665eb)

Using the Holm-Bonferroni procedure, we reject the first two null hypotheses and fail to reject the remaining four.

The procedure controls the family-wise error rate while generally being less conservative than the standard Bonferroni correction. As with other multiple-testing procedures, stronger protection against false positives comes at the cost of reduced power and a greater risk of failing to detect real effects.


Define the family before looking at which results are attractive. Selecting one outcome, subgroup, transformation, or time window from many attempted analyses can create multiplicity even when only one final p-value is reported. A separate validation dataset can evaluate a fixed selected claim, but repeatedly revising the claim using that dataset turns validation into further exploration. The [SciPy false-discovery documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.false_discovery_control.html) states the dependence conditions for BH and the more conservative BY procedure.
