# Correlation Exercises

Read the note first: [Correlation](../../notes/joint_distributions_and_covariance/correlation.md). Solutions are at the end of this file.

## Problems

1. For $X=(1,2,3,4,5)$ and $Y=(2,1,4,3,5)$, compute Pearson's $r$ by hand.
2. For the same data compute Spearman's $r_s$ using the rank-difference formula.
3. For $X=(1,2,3,4,5,6)$ and $Y=(1,2,3,4,5,30)$ compute Pearson's $r$ and Spearman's $r_s$. Explain the difference.
4. Suppose $\operatorname{Cov}(X,Y)=-12$, $\sigma_X=3$ and $\sigma_Y=5$. Find $\rho_{XY}$ and the proportion of variance of $Y$ linearly explained by $X$. Could $\operatorname{Cov}(X,Y)=20$ with the same standard deviations?
5. Let $X$ take the values $-2,-1,0,1,2$ and $Y=X^2$. Compute Pearson's $r$ and Spearman's $r_s$ and comment.
6. If $r(X,Y)=0.6$, find $r(2X+3,\,-5Y+1)$. Does Spearman's $r_s$ change if $Y$ is replaced by $e^Y$? Does Pearson's $r$ necessarily stay the same?
7. A city finds a correlation of $0.85$ between monthly ice cream sales and monthly drowning incidents. Give two interpretations that do not involve ice cream causing drownings.
8. For the joint pmf below, compute $\rho_{XY}$ by hand.

| | $Y=0$ | $Y=1$ | $Y=2$ |
|---|---|---|---|
| $X=0$ | 0.10 | 0.15 | 0.05 |
| $X=1$ | 0.10 | 0.20 | 0.40 |

9. A report states $r=-0.8$ between $X$ and $Y$, with $s_X=2$ and $s_Y=10$. Interpret the sign and $r^2$, and find the least-squares slope of $Y$ on $X$.

## Solutions

**1.** $\bar X=3$, $\bar Y=3$. Deviations: $x$: $(-2,-1,0,1,2)$, $y$: $(-1,-2,1,0,2)$. Products: $(2,2,0,0,4)$, sum $8$. $\sum(x-\bar x)^2=10$, $\sum(y-\bar y)^2=1+4+1+0+4=10$. So $r=8/\sqrt{10\cdot10}=0.8$.

**2.** With no ties the ranks equal the values. $d=R(X)-R(Y)=(-1,1,-1,1,0)$, $\sum d^2=4$. $r_s=1-\dfrac{6\cdot4}{5(25-1)}=1-\dfrac{24}{120}=0.8$.

**3.** Pearson: $\bar X=3.5$, $\bar Y=45/6=7.5$. $\sum(x-\bar x)^2=17.5$, $\sum(y-\bar y)^2=6.5^2+5.5^2+4.5^2+3.5^2+2.5^2+22.5^2=617.5$, $\sum(x-\bar x)(y-\bar y)=77.5$. Hence $r=77.5/\sqrt{17.5\cdot617.5}=77.5/103.95\approx0.746$.
Spearman: the ranks of $Y$ equal those of $X$, so $\sum d^2=0$ and $r_s=1$. The single outlier ($30$) pulls the points away from a line and reduces $r$, but the relationship is perfectly monotone, so $r_s$ is unaffected.

**4.** $\rho=-12/(3\cdot5)=-0.8$. Variance explained by linear fit: $\rho^2=0.64$ (64%). $|\operatorname{Cov}|\le\sigma_X\sigma_Y=15$, so $\operatorname{Cov}=20$ is impossible (it would give $\rho=1.33$).

**5.** $Y=(4,1,0,1,4)$, $\bar X=0$, $\bar Y=2$. $\sum x(y-\bar y)=(-2)(2)+(-1)(-1)+0+(1)(-1)+(2)(2)=-4+1+0-1+4=0$, so $r=0$.
Ranks of $Y$ (with ties averaged): $(4.5,2.5,1,2.5,4.5)$; ranks of $X$: $(1,2,3,4,5)$. Both have mean $3$; deviations $(-2,-1,0,1,2)$ and $(1.5,-0.5,-2,-0.5,1.5)$; products $(-3,0.5,0,-0.5,3)$ sum to $0$. So $r_s=0$.
Both are zero although $Y$ is a deterministic function of $X$: the relationship is not monotone, so neither coefficient detects it.

**6.** Multiplying by a positive constant keeps the sign and multiplying $Y$ by $-5$ flips it: $r(2X+3,-5Y+1)=\operatorname{sign}(2)\operatorname{sign}(-5)\,r=-0.6$. Spearman depends only on ranks and $e^Y$ is increasing in $Y$, so $r_s$ is unchanged. Pearson's $r$ is not invariant to non-linear transformations and generally changes.

**7.** (i) A confounder: hot weather increases both ice cream sales and swimming (hence drownings). (ii) Seasonality or time trend: both series peak in summer, so they are correlated through shared calendar structure. (Spurious chance correlation or a reverse/other mechanism are also acceptable.) Correlation alone does not establish causation.

**8.** From the table: $E[X]=0.7$, $E[Y]=1.25$, $E[XY]=0.20+0.80=1.00$, so $\operatorname{Cov}=1.00-0.875=0.125$. $\operatorname{Var}(X)=0.21$, $\operatorname{Var}(Y)=2.15-1.5625=0.5875$. $\rho=0.125/\sqrt{0.21\cdot0.5875}=0.125/0.3512\approx0.356$: weak-to-moderate positive linear association.

**9.** Negative sign: larger $X$ goes with smaller $Y$ on average. $r^2=0.64$: about 64% of the variance of $Y$ is linearly associated with $X$. The least-squares slope is $b=r\,s_Y/s_X=-0.8\cdot10/2=-4$ units of $Y$ per unit of $X$.
