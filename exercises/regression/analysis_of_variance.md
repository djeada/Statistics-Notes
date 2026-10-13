# Analysis of Variance Exercises

Read [ANOVA and the Analysis of Variance for Multiple Groups](../../notes/regression/analysis_of_variance.md) first. Solutions are at the end; try each problem before reading them.

## Problems

1. Three teaching methods give the exam scores A $=(5,7,9)$, B $=(8,10,12)$, C $=(11,13,15)$. Compute $SST$, $SSE$, $SSTotal$, $MST$, $MSE$, $F$, and the p-value (use $F_{2,6}$). State the decision at $\alpha=0.05$.
2. A one-way ANOVA with $k=4$ groups and $N=24$ observations has $SST=120$ and $SSE=300$. Complete the ANOVA table (degrees of freedom, mean squares, $F$) and find the p-value from $F_{3,20}$.
3. Test $H_0:\mu_A=\mu_B$ for the groups A and B of Problem 1 with a pooled two-sample t-test. Show that $t^2$ equals the ANOVA $F$ for those two groups.
4. A study has 5 groups and all pairwise t-tests are run at $\alpha=0.05$. How many tests are there? If they were independent and every null were true, what is the probability of at least one false positive? What is the Bonferroni-adjusted level?
5. Using $MSE$ from Problem 1, test A versus C with the post-ANOVA pairwise t-statistic, and compare the p-value with the Bonferroni threshold for all three pairwise comparisons.
6. Two group samples have standard deviations $2.86$ and $11.49$. Does the rule of thumb for equal variances support the ANOVA assumption? Which assumption would you check next and how?
7. Explain why $F$ is close to 1 when $H_0$ is true and why a large $F$ is evidence against $H_0$. State what $MST$ and $MSE$ estimate.
8. For Problem 1, compute the proportion of total variability explained by group membership ($\eta^2=SST/SSTotal$) and explain how it relates to $R^2$ in a regression on group indicator variables.
9. In the note's peer-assessment example, $SST=98.4$, $SSE=723.8$, $k=3$, $N=41$. Reproduce $F$, the p-value, and the critical value at $\alpha=0.05$. Why does "fail to reject" not mean "the methods are equally effective"?

## Solutions

**1.** Group means: $\bar y_A=7$, $\bar y_B=10$, $\bar y_C=13$; grand mean $\bar y=10$.

- $SST=\sum n_j(\bar y_j-\bar y)^2=3(9+0+9)=54$.
- Within each group the deviations from the group mean are $(-2,0,2)$, so each group contributes $4+0+4=8$ and $SSE=24$.
- $SSTotal=SST+SSE=78$.
- $df_T=k-1=2$, $df_E=N-k=9-3=6$, so $MST=54/2=27$ and $MSE=24/6=4$.
- $F=27/4=6.75$; with $F_{2,6}$ the p-value is $\approx 0.029$.

Since $0.029<0.05$, reject $H_0$: at least one method mean differs.

**2.** $df_T=3$, $df_E=24-4=20$, $df_{Total}=23$.

| Source | df | SS | MS | F |
|---|---|---|---|---|
| Treatment | 3 | 120 | 40 | 2.667 |
| Error | 20 | 300 | 15 | |
| Total | 23 | 420 | | |

$F=40/15\approx 2.67$, p-value $\approx 0.076$ from $F_{3,20}$; not significant at $0.05$.

**3.** $\bar y_A=7$, $\bar y_B=10$, $s_A^2=s_B^2=4$, so the pooled variance is $s^2=\frac{2\cdot4+2\cdot4}{4}=4$. Then $SE=\sqrt{4/3+4/3}=\sqrt{8/3}\approx1.633$ and $t=(7-10)/1.633\approx-1.837$ with $n_1+n_2-2=4$ df ($p\approx0.140$). Then $t^2\approx3.375$. The ANOVA on two groups: grand mean $8.5$, $SST=3(1.5^2)\cdot2=13.5$, $SSE=16$, $MSE=16/4=4$, $F=13.5/4=3.375=t^2$, with the same p-value $0.140$.

**4.** Number of pairs: $\binom52=10$. Probability of at least one false positive: $1-0.95^{10}\approx0.401$. Bonferroni level: $0.05/10=0.005$ per test.

**5.** $SE=\sqrt{MSE(1/3+1/3)}=\sqrt{4\cdot 2/3}\approx1.633$. $t=(7-13)/1.633\approx-3.674$ with $N-k=6$ df, two-sided $p\approx0.0104$. The Bonferroni threshold is $0.05/3\approx0.0167$. Since $0.0104<0.0167$, A and C differ significantly even after adjustment.

**6.** The ratio of the largest to the smallest standard deviation is $11.49/2.86\approx4.0>2$, so the rule of thumb says the equal-variance assumption is doubtful. Check boxplots of the spread and run Levene's test; if variances are unequal, use Welch's ANOVA or a variance-stabilizing transformation.

**7.** $MSE$ estimates $\sigma^2$ regardless of whether $H_0$ holds. $MST$ estimates $\sigma^2+\sum n_j\tau_j^2/(k-1)$, which equals $\sigma^2$ only when all effects $\tau_j$ are zero. So under $H_0$ both estimate $\sigma^2$ and $F\approx1$ (its expected value is slightly above 1, $\frac{df_E}{df_E-2}$). When the group means truly differ, the numerator is inflated and $F$ becomes large.

**8.** $\eta^2=54/78\approx0.692$. In the regression $y=\beta_0+\beta_1 D_B+\beta_2 D_C+\epsilon$ with indicator variables, the fitted values are the group means, so $SSR=SST$ and $R^2=SST/SSTotal=\eta^2$. Also the regression overall F-test is identical to the ANOVA F-test.

**9.** $MST=98.4/2=49.2$, $MSE=723.8/38\approx19.047$, $F=49.2/19.047\approx2.583$. With $F_{2,38}$ the p-value is $\approx0.089$ and the 5% critical value is $\approx3.245$. Since $2.583<3.245$ (equivalently $p>0.05$) we fail to reject. Failing to reject only says the data are compatible with equal means; with $N=41$ the test may have low power against modest true differences, so absence of evidence is not evidence of absence.
