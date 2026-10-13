# Central Limit Theorem Exercises

Read the note first: [Central Limit Theorem](../../notes/sampling_and_sampling_distributions/central_limit_theorem.md). Solutions are at the end of this file.

## Problems

1. A fair die has $\mu=3.5$ and $\sigma^2=35/12$. For the mean of $n=50$ rolls, find the standard error and approximate $P(\bar X>3.8)$.
2. A fair coin is tossed $100$ times. Approximate $P(\text{heads}\ge60)$ with the CLT, with and without continuity correction, and compare with the exact binomial value.
3. Household incomes have $\mu=67{,}000$ and $\sigma=38{,}000$. For a random sample of $n=100$ households, approximate $P(|\bar X-\mu|<5{,}000)$.
4. A measurement has $\sigma=6$. How large must $n$ be so that $\bar X$ is within $1$ unit of $\mu$ with probability at least $0.95$?
5. True or false, with a reason: (a) with $n=30$ the data themselves are approximately normal; (b) the sampling distribution of $\bar X$ has standard deviation $\sigma/\sqrt n$ for every $n$; (c) the sampling distribution of $\bar X$ is exactly normal for every $n$ when the population is normal.
6. Observations are Exponential with mean $1$ (so $\sigma=1$). For $n=5$, the exact distribution of $\bar X$ is Gamma with shape $5$ and scale $1/5$. Compare the exact $P(\bar X>2)$ ($=0.0293$) with the CLT approximation. What does this say about small $n$ and skewed populations?
7. A population has $\mu=70$ and $\sigma=15$. A sample of $n=36$ has $\bar x=72$. Compute the $z$-score of the sample mean and the approximate probability of a sample mean at least this large.
8. Let $X\sim\text{Poisson}(25)$. Use the normal approximation with continuity correction to estimate $P(X\le20)$. The exact value is $0.1855$.

## Solutions

**1.** $\sigma=\sqrt{35/12}=1.7078$, $SE=1.7078/\sqrt{50}=0.2415$. $z=(3.8-3.5)/0.2415=1.242$, so $P(\bar X>3.8)\approx1-\Phi(1.242)=0.107$.

**2.** Heads $\sim\text{Bin}(100,0.5)$: mean $50$, SD $\sqrt{25}=5$. Without correction: $z=(60-50)/5=2$, $P=0.0228$. With continuity correction use $59.5$: $z=(59.5-50)/5=1.9$, $P=0.0287$. Exact: $P(X\ge60)=0.0284$. The corrected approximation is much closer.

**3.** $SE=38{,}000/10=3{,}800$. $z=5{,}000/3{,}800=1.316$. $P(|Z|<1.316)=2\Phi(1.316)-1=0.812$.

**4.** Need $1.96\,\sigma/\sqrt n\le1$, i.e. $\sqrt n\ge1.96\cdot6=11.76$, so $n\ge138.3$; take $n=139$.

**5.** (a) False: the CLT concerns the distribution of $\bar X$ (or sums), not individual observations. (b) True: $\operatorname{Var}(\bar X)=\sigma^2/n$ holds for independent observations of any size, no CLT needed. (c) True: linear combinations of independent normals are exactly normal.

**6.** CLT: $\bar X\approx N(1,\,1/5)$, $SE=1/\sqrt5=0.447$, $z=(2-1)/0.447=2.236$, $P\approx0.0127$. The exact value $0.0293$ is more than twice as large, because the true distribution of $\bar X$ is still right-skewed at $n=5$ and has a heavier upper tail. Skewed populations need larger $n$ before the normal approximation is accurate in the tails.

**7.** $SE=15/6=2.5$, $z=(72-70)/2.5=0.8$, $P(\bar X\ge72)\approx1-\Phi(0.8)=0.2119$. Two points above the mean is not unusual for a sample of this size.

**8.** Mean $=25$, SD $=5$. With continuity correction: $P(X\le20)\approx\Phi\!\left(\frac{20.5-25}{5}\right)=\Phi(-0.9)=0.1841$, close to the exact $0.1855$ (without correction, $\Phi(-1)=0.1587$).
