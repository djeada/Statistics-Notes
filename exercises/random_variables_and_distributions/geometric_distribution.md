# Geometric Distribution - Exercises

Read [Geometric distribution](../../notes/random_variables_and_distributions/discrete/geometric_distribution.md) first. $X$ counts trials up to and including the first success.

## Problems

1. $X\sim\text{Geometric}(0.2)$. Find $P(X=4)$ and $P(X>5)$.
2. Find the mean, variance and standard deviation for $p=0.2$.
3. Derive the CDF $F(k)=1-(1-p)^k$ by summing the pmf.
4. Show the memoryless property $P(X>m+n\mid X>m)=P(X>n)$, and evaluate $P(X>8\mid X>3)$ for $p=0.2$.
5. Derive $E[X]=1/p$ by a first-step (conditioning) argument.
6. How many trials are needed so that the probability of at least one success is at least 95% when $p=0.1$?
7. A coin lands heads with $p=0.5$. Find $P(X\text{ is even})$ and $E[X]$.
8. Let $Y=X-1$ be the number of failures before the first success. Give the pmf, mean and variance of $Y$ for $p=0.25$, and note which software convention it matches.

## Solutions

### 1.
$P(X=4)=(0.8)^3(0.2)=0.512(0.2)=0.1024$.
$P(X>5)$ means the first 5 trials all fail: $0.8^5=0.32768$.

### 2.
$E[X]=\tfrac1p=5$. $\operatorname{Var}(X)=\tfrac{1-p}{p^2}=\tfrac{0.8}{0.04}=20$. $\text{SD}=\sqrt{20}=4.472$.

### 3.
Let $q=1-p$. $F(k)=\sum_{i=1}^kq^{i-1}p=p\cdot\dfrac{1-q^k}{1-q}=p\cdot\dfrac{1-q^k}{p}=1-q^k$.

### 4.
$P(X>m)=q^m$. Then $P(X>m+n\mid X>m)=\dfrac{P(X>m+n)}{P(X>m)}=\dfrac{q^{m+n}}{q^m}=q^n=P(X>n)$.
For $p=0.2$: $P(X>8\mid X>3)=P(X>5)=0.8^5=0.32768$.

### 5.
Condition on the first trial: with probability $p$ it succeeds ($X=1$); otherwise one trial is used and the process restarts.
$E[X]=p\cdot1+(1-p)(1+E[X])\Rightarrow E[X]=1+(1-p)E[X]\Rightarrow pE[X]=1\Rightarrow E[X]=\tfrac1p$.

### 6.
Need $1-0.9^k\ge0.95\iff0.9^k\le0.05\iff k\ge\dfrac{\ln0.05}{\ln0.9}=\dfrac{-2.9957}{-0.10536}=28.43$.
So $k=29$ trials. Check: $0.9^{28}=0.0523>0.05$, $0.9^{29}=0.0471<0.05$.

### 7.
$P(X\text{ even})=\sum_{j\ge1}q^{2j-1}p=p\,q\sum_{j\ge0}q^{2j}=\dfrac{pq}{1-q^2}=\dfrac{0.25}{0.75}=\tfrac13$.
(So an even number is less likely than odd, because the geometric pmf decreases.) $E[X]=1/0.5=2$.

### 8.
$P(Y=j)=(1-p)^jp$ for $j=0,1,2,\dots$, i.e. $(0.75)^j(0.25)$.
$E[Y]=E[X]-1=\tfrac1p-1=\tfrac{1-p}{p}=\tfrac{0.75}{0.25}=3$. The variance is unchanged by the shift: $\tfrac{1-p}{p^2}=\tfrac{0.75}{0.0625}=12$.
This failures-before-success form is the convention of `scipy.stats.nbinom(1, p)`; `scipy.stats.geom` uses the trial-count convention of the note.
