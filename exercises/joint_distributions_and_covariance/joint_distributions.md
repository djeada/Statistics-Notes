# Joint Distributions Exercises

Read the note first: [Joint Distributions](../../notes/joint_distributions_and_covariance/joint_distributions.md). Solutions are at the end of this file; try each problem by hand before looking.

Problems 1-5 use this joint pmf of $X\in\{0,1\}$ and $Y\in\{0,1,2\}$:

| | $Y=0$ | $Y=1$ | $Y=2$ |
|---|---|---|---|
| $X=0$ | 0.10 | 0.15 | 0.05 |
| $X=1$ | 0.10 | 0.20 | 0.40 |

## Problems

1. Verify that the table is a valid joint pmf and find the marginal pmfs $p_X$ and $p_Y$.
2. Find the conditional pmf $p_{Y\mid X}(y\mid 1)$ and the conditional means $E[Y\mid X=0]$ and $E[Y\mid X=1]$. Check the law of total expectation $E[Y]=\sum_x E[Y\mid X=x]\,p_X(x)$.
3. Are $X$ and $Y$ independent? Justify with a single cell of the table.
4. Compute $E[X]$, $E[Y]$, $E[XY]$, $\operatorname{Var}(X)$, $\operatorname{Var}(Y)$, $\operatorname{Cov}(X,Y)$ and the correlation.
5. Compute $E[(X+Y)^2]$ directly from the joint pmf and verify it using $\operatorname{Var}(X+Y)$.
6. Let $f_{X,Y}(x,y)=x+y$ on the unit square $0\le x,y\le1$ (and $0$ elsewhere). Show that it is a valid density, find $f_X(x)$, $E[X]$, $P(X\le\tfrac12,Y\le\tfrac12)$ and the conditional density $f_{Y\mid X}(y\mid x)$.
7. Let $f_{X,Y}(x,y)=4xy$ on the unit square. Show that $X$ and $Y$ are independent and find $P(X>Y)$.
8. Give two different joint pmfs for $(X,Y)$, with $X,Y\in\{0,1\}$ and both marginals uniform, such that in one $X,Y$ are independent and in the other $Y=X$. What does this say about recovering a joint distribution from its marginals?
9. Explain in two or three sentences why $E[Y\mid X=x]$ is a function of $x$ and why this is the object regression models.

## Solutions

**1.** All entries are nonnegative and the total is $0.10+0.15+0.05+0.10+0.20+0.40=1.00$. Row sums give $p_X$: $p_X(0)=0.30$, $p_X(1)=0.70$. Column sums give $p_Y$: $p_Y(0)=0.20$, $p_Y(1)=0.35$, $p_Y(2)=0.45$.

**2.** $p_{Y\mid X}(y\mid 1)=p(1,y)/0.70$ gives $(0.10,0.20,0.40)/0.70=(1/7,\,2/7,\,4/7)\approx(0.143,0.286,0.571)$.
$E[Y\mid X=1]=0\cdot\tfrac17+1\cdot\tfrac27+2\cdot\tfrac47=\tfrac{10}{7}\approx1.4286$.
For $X=0$: $(0.10,0.15,0.05)/0.30=(1/3,1/2,1/6)$, so $E[Y\mid X=0]=\tfrac12+\tfrac26=\tfrac56\approx0.8333$.
Total expectation: $0.30\cdot\tfrac56+0.70\cdot\tfrac{10}{7}=0.25+1.00=1.25$, which equals $E[Y]=0.35+0.90=1.25$ (see problem 4).

**3.** If independent, $p(0,0)=p_X(0)p_Y(0)=0.30\times0.20=0.06$. The table says $p(0,0)=0.10\ne0.06$, so $X$ and $Y$ are dependent. (The largest discrepancy over all cells is $0.085$, at $(1,2)$: $0.40$ versus $0.7\times0.45=0.315$.)

**4.** $E[X]=0.70$. $E[Y]=0.35+2(0.45)=1.25$. $E[XY]=\sum xy\,p=1\cdot1\cdot0.20+1\cdot2\cdot0.40=1.00$.
$\operatorname{Var}(X)=0.7\cdot0.3=0.21$. $E[Y^2]=0.35+4(0.45)=2.15$, so $\operatorname{Var}(Y)=2.15-1.25^2=0.5875$.
$\operatorname{Cov}(X,Y)=1.00-0.70\cdot1.25=0.125$.
$\rho=0.125/\sqrt{0.21\times0.5875}=0.125/0.3512\approx0.356$.

**5.** Directly: row $X=0$ gives $(0^2,1^2,2^2)\cdot(0.10,0.15,0.05)=0+0.15+0.20=0.35$; row $X=1$ gives $(1,4,9)\cdot(0.10,0.20,0.40)=0.10+0.80+3.60=4.50$. Total $4.85$.
Check: $E[X+Y]=1.95$, $\operatorname{Var}(X+Y)=0.21+0.5875+2(0.125)=1.0475$, and $1.0475+1.95^2=1.0475+3.8025=4.85$. ✓

**6.** Normalization: $\int_0^1\!\int_0^1(x+y)\,dy\,dx=\int_0^1(x+\tfrac12)\,dx=\tfrac12+\tfrac12=1$, and $f\ge0$.
Marginal: $f_X(x)=\int_0^1(x+y)\,dy=x+\tfrac12$ for $0\le x\le1$.
$E[X]=\int_0^1x(x+\tfrac12)\,dx=\tfrac13+\tfrac14=\tfrac{7}{12}\approx0.5833$.
$P(X\le\tfrac12,Y\le\tfrac12)=\int_0^{1/2}\!\int_0^{1/2}(x+y)\,dy\,dx=\int_0^{1/2}\left(\tfrac x2+\tfrac18\right)dx=\tfrac1{16}+\tfrac1{16}=\tfrac18$.
Conditional: $f_{Y\mid X}(y\mid x)=\dfrac{x+y}{x+\tfrac12}$ for $0\le y\le1$.

**7.** $f_X(x)=\int_0^1 4xy\,dy=2x$ and $f_Y(y)=2y$, so $f_X(x)f_Y(y)=4xy=f_{X,Y}(x,y)$: independent. By symmetry of the density in $x\leftrightarrow y$ and $P(X=Y)=0$, $P(X>Y)=\tfrac12$. (Directly: $\int_0^1\!\int_0^x4xy\,dy\,dx=\int_0^12x^3\,dx=\tfrac12$.)

**8.** Independent: $p(x,y)=0.25$ for all four cells. Perfect dependence: $p(0,0)=p(1,1)=0.5$ and $p(0,1)=p(1,0)=0$. Both have marginals $(0.5,0.5)$ for $X$ and $Y$, but correlation $0$ versus $1$. Marginals alone do not determine the joint distribution; the dependence structure is extra information.

**9.** For each value $x$, the conditional distribution of $Y$ given $X=x$ has its own mean, so $E[Y\mid X=x]$ varies with $x$ and is a function $m(x)$. Regression models $m(x)$ (the conditional mean of the response given predictors), so the conditional distributions defined here are what the regression model is about.
