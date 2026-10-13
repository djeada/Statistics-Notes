# Multiple Comparisons: Exercises

These problems accompany the note **[Multiple Comparisons](../../notes/hypothesis_testing_and_confidence_intervals/multiple_comparisons.md)**. Worked solutions are in the [Solutions](#solutions) section; numbers were checked in Python (see `scripts/hypothesis_testing_and_confidence_intervals/multiple_comparisons.py`).

## Problems

**1. Family-wise error.** If $m$ independent tests are each run at $\alpha=0.05$ with all nulls true, what is the probability of at least one false rejection for $m=10$ and $m=50$?

**2. Bonferroni threshold.** A study tests 12 hypotheses with a family-wise error rate of $0.05$. What per-test threshold is used? A test has raw $p=0.004$. Is it significant?

**3. Three procedures compared.** Five tests give $p=0.003,\ 0.012,\ 0.018,\ 0.040,\ 0.30$. At level $0.05$, find the rejections under (a) Bonferroni, (b) Holm, (c) Benjamini-Hochberg.

**4. Adjusted p-values.** For the five p-values in Problem 3, compute the Bonferroni-adjusted p-values and compare with $0.05$.

**5. False discovery proportion.** A screen rejects 60 hypotheses, of which 12 are false discoveries. What is the FDP? What would FDR control at $0.1$ promise?

**6. Expected counts.** A genomics study tests 1,000 genes at $\alpha=0.05$ with no correction. 100 genes truly have an effect and the test has power $0.80$. Compute the expected number of true positives, false positives, and the expected FDP.

**7. Data snooping.** A team explores 40 candidate predictors, picks the one with the smallest p-value ($0.004$), and reports it as a single pre-planned test. What is wrong, and what is the Bonferroni-adjusted p-value? How could a validation set help?

## Solutions

**1.** $P(\ge1\text{ false rejection})=1-(1-\alpha)^m$.

$$
m=10:\ 1-0.95^{10}=0.401,
\qquad
m=50:\ 1-0.95^{50}=0.923.
$$

**2.** The Bonferroni threshold is $0.05/12=0.00417$. Since $0.004<0.00417$, the test is (barely) significant.

**3.**
(a) Bonferroni: threshold $0.05/5=0.01$. Only $0.003$ passes: 1 rejection.
(b) Holm: compare the sorted p-values with $0.05/5,0.05/4,0.05/3,0.05/2,0.05=0.01,\ 0.0125,\ 0.0167,\ 0.025,\ 0.05$. $0.003\le0.01$ yes; $0.012\le0.0125$ yes; $0.018>0.0167$ stop. 2 rejections.
(c) BH: thresholds $\frac{i}{5}(0.05)=0.01,\ 0.02,\ 0.03,\ 0.04,\ 0.05$. $0.003\le0.01$, $0.012\le0.02$, $0.018\le0.03$, $0.040\le0.04$ (equal), $0.30>0.05$. The largest $i$ with $p_{(i)}\le$ threshold is $4$, so 4 rejections.

The ordering Bonferroni $\le$ Holm $\le$ BH in rejections reflects the weaker guarantee that BH offers (FDR instead of FWER).

**4.** Adjusted $p=\min(1,\,5p)$: $0.015,\ 0.06,\ 0.09,\ 0.20,\ 1.00$. Only $0.015<0.05$, so just the first test is significant, consistent with Problem 3(a).

**5.** $\mathrm{FDP}=12/60=0.20$. FDR control at $0.1$ would promise that the *expected* FDP is at most $10\%$; this particular realized FDP of $20\%$ is above that target, which is possible for a single realization.

**6.** True positives: $100(0.80)=80$. False positives: $900(0.05)=45$. Total rejections $=125$, so

$$
\mathrm{FDP}\approx\frac{45}{125}=0.36.
$$

Over a third of the "discoveries" are expected to be false even though each test used $\alpha=0.05$.

**7.** The reported test ignores that the minimum of 40 p-values was selected, which is the look-elsewhere effect. The Bonferroni-adjusted p-value is $\min(1,40\times0.004)=0.16$, not significant. Holding out a validation set, used only to test the single predictor chosen on the exploration data, gives an honest p-value for that one hypothesis.
