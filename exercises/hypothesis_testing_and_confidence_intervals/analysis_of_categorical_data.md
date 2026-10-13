# Analysis of Categorical Data: Exercises

These problems accompany the note **[Analysis of Categorical Data](../../notes/hypothesis_testing_and_confidence_intervals/analysis_of_categorical_data.md)**. Worked solutions are in the [Solutions](#solutions) section; numbers were checked in Python (see `scripts/hypothesis_testing_and_confidence_intervals/analysis_of_categorical_data.py`).

Useful critical values at $\alpha=0.05$: $\chi^2_{1}=3.84$, $\chi^2_{2}=5.99$, $\chi^2_{3}=7.81$, $\chi^2_{4}=9.49$, $\chi^2_{5}=11.07$.

## Problems

**1. Goodness of fit.** A die is rolled 120 times with counts $25,\ 17,\ 15,\ 23,\ 24,\ 16$ for faces 1 to 6. Test whether the die is fair.

**2. 2x2 independence.** Of 100 exposed people, 30 developed a condition; of 200 unexposed people, 20 did. Test association at $\alpha=0.05$:
(a) Find the expected counts.
(b) Compute the Pearson $\chi^2$ and the Yates-corrected statistic.

**3. 3x3 table.** A survey of 450 people (150 per age group) classified satisfaction as Low / Medium / High:

| | Low | Medium | High |
|---|---:|---:|---:|
| Age 18-34 | 40 | 60 | 50 |
| Age 35-54 | 30 | 70 | 50 |
| Age 55+ | 20 | 40 | 90 |

(a) Compute expected counts and degrees of freedom. (b) Compute $\chi^2$ and make a decision. (c) Which cell contributes most?

**4. Degrees of freedom.** Give the degrees of freedom for (a) a goodness-of-fit test with 8 categories and fully specified probabilities; (b) a $4\times5$ contingency table; (c) a goodness-of-fit test of a Poisson model with 6 categories where $\lambda$ was estimated from the data.

**5. Validity condition.** A $2\times2$ table has row totals 10 and 90 and column totals 5 and 95. Compute the smallest expected count and say whether the chi-square approximation is trustworthy.

**6. Homogeneity versus independence.** Classify each design: (a) 300 voters each from three cities, compare party preference; (b) one random sample of 500 adults, cross-classified by education and smoking status.

**7. Causation.** The 3x3 table in Problem 3 shows a significant association. Can we conclude age causes satisfaction? What can we conclude?

## Solutions

**1.** The expected count is $120/6=20$ per face. Then

$$
\chi^2=\frac{(5)^2+(-3)^2+(-5)^2+3^2+4^2+(-4)^2}{20}=\frac{25+9+25+9+16+16}{20}=\frac{100}{20}=5.0.
$$

With $df=5$, the critical value is $11.07$ and $p\approx0.416$. Since $5.0<11.07$, we fail to reject: no evidence that the die is unfair.

**2.**
(a) Total $=300$; 50 developed the condition, 250 did not. Expected for exposed with condition: $100(50)/300=16.67$; exposed without: $83.33$; unexposed with: $200(50)/300=33.33$; unexposed without: $166.67$.
(b) Pearson:

$$
\chi^2=\frac{(30-16.67)^2}{16.67}+\frac{(70-83.33)^2}{83.33}+\frac{(20-33.33)^2}{33.33}+\frac{(180-166.67)^2}{166.67}
=10.67+2.13+5.33+1.07=19.2.
$$

Yates: each $|O-E|=13.33$, reduced by $0.5$ to $12.83$, giving $\frac{12.83^2}{1}\left(\frac1{16.67}+\frac1{83.33}+\frac1{33.33}+\frac1{166.67}\right)=164.69(0.108)=17.79$. With $df=1$, both exceed $3.84$ ($p\approx1.2\times10^{-5}$ and $2.5\times10^{-5}$), so we reject independence: exposure and the condition are associated.

**3.**
(a) Column totals are $90,\ 170,\ 190$ and each row total is 150, so expected counts are $150(90)/450=30$, $150(170)/450=56.67$, $150(190)/450=63.33$ in every row. $df=(3-1)(3-1)=4$.
(b) The contributions $(O-E)^2/E$ by row are: row 1: $3.33,\ 0.20,\ 2.81$; row 2: $0,\ 3.14,\ 2.81$; row 3: $3.33,\ 4.90,\ 11.23$. Sum $=31.74$. Since $31.74>9.49$ ($p\approx2\times10^{-6}$), we reject independence.
(c) Age 55+, High satisfaction contributes $11.23$: far more people are highly satisfied than expected (90 versus 63.3).

**4.**
(a) $df=8-1=7$.
(b) $df=(4-1)(5-1)=12$.
(c) $df=k-1-m=6-1-1=4$.

**5.** The smallest expected count is $10(5)/100=0.5$, far below the common rule of thumb of $5$. The chi-square approximation is not trustworthy here; use an exact method such as Fisher's exact test.

**6.**
(a) Homogeneity: separate samples from each city, one categorical variable compared across groups.
(b) Independence: a single sample classified on two variables.
The calculation is identical; the distinction lies in the sampling design and question asked.

**7.** No. A significant chi-square test shows the distributions of satisfaction differ across age groups, i.e., an association. It does not identify why; cohort effects, expectations, or other confounders may be involved, and the survey design does not support causal conclusions.
