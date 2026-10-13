# Poisson Distribution - Exercises

Read [Poisson distribution](../../notes/random_variables_and_distributions/discrete/poisson_distribution.md) first.

## Problems

1. $X\sim\text{Poisson}(4)$. Find $P(X=2)$, $P(X\le1)$ and $P(X\ge3)$.
2. An emergency room has on average 5 arrivals per hour. Find the probability of no arrivals in a 30-minute interval.
3. Derive $E[X]$ and $\operatorname{Var}(X)$ from the MGF $e^{\lambda(e^t-1)}$.
4. Calls to two help desks are independent Poisson with rates 3 and 5 per hour. What is the distribution of the total, and $P(\text{total}=8)$?
5. A binomial has $n=500$, $p=0.01$. Compare $P(X=2)$ exactly and by a Poisson approximation.
6. The counts $2,5,3,7,4,3$ are observed in six equal intervals. Estimate $\lambda$ and compute the dispersion ratio sample variance / mean. Does a Poisson model look plausible?
7. For $\lambda=3$ find the mode(s) using the ratio $P(k)/P(k-1)$.
8. Arrivals follow a Poisson process with rate 5 per hour. Relate $P(\text{no arrivals in } t \text{ hours})$ to the waiting time $T$ to the first arrival and give its distribution.

## Solutions

### 1.
$P(X=2)=\dfrac{e^{-4}4^2}{2!}=8e^{-4}=8(0.018316)=0.1465$.
$P(X\le1)=e^{-4}(1+4)=5(0.018316)=0.0916$.
$P(X\ge3)=1-e^{-4}(1+4+8)=1-13(0.018316)=1-0.2381=0.7619$.

### 2.
Rate scales with interval length: $\lambda=5\times0.5=2.5$.
$P(X=0)=e^{-2.5}=0.0821$.

### 3.
$M(t)=e^{\lambda(e^t-1)}$, $M'(t)=\lambda e^t M(t)\Rightarrow E[X]=\lambda$.
$M''(t)=\lambda e^tM(t)+(\lambda e^t)^2M(t)\Rightarrow E[X^2]=\lambda+\lambda^2$.
$\operatorname{Var}(X)=\lambda+\lambda^2-\lambda^2=\lambda$.

### 4.
The MGFs multiply: $e^{3(e^t-1)}e^{5(e^t-1)}=e^{8(e^t-1)}$, so total $\sim\text{Poisson}(8)$.
$P(8)=\dfrac{e^{-8}8^8}{8!}=\dfrac{0.00033546(16777216)}{40320}=0.1396$.

### 5.
Binomial: $\binom{500}{2}(0.01)^2(0.99)^{498}=124750(0.0001)(0.006704)=0.0836$ (using $0.99^{498}=0.006704$).
Poisson, $\lambda=np=5$: $\dfrac{e^{-5}5^2}{2}=\dfrac{0.006738(25)}{2}=0.0842$.
Difference is about $0.0006$.

### 6.
$\hat\lambda=\bar x=\tfrac{2+5+3+7+4+3}{6}=\tfrac{24}{6}=4$.
Deviations: $-2,1,-1,3,0,-1$; squares sum to $4+1+1+9+0+1=16$, so $s^2=16/5=3.2$.
Ratio $=3.2/4=0.8$. A Poisson model implies a ratio near 1; with only six observations 0.8 is quite consistent with it.

### 7.
$\dfrac{P(k)}{P(k-1)}=\dfrac{\lambda}{k}=\dfrac3k$. This is $>1$ for $k<3$ and equals 1 at $k=3$.
So $P(3)=P(2)$ are both maximal (bimodal at 2 and 3): $P(2)=P(3)=\tfrac{9}{2}e^{-3}=0.2240$.

### 8.
No arrival in $[0,t]$ means $T>t$. Number of arrivals in time $t$ is Poisson($5t$), so $P(T>t)=e^{-5t}$. This is the survival function of an exponential distribution with rate 5, i.e. $T\sim\text{Exp}(5)$ with mean $0.2$ hours.
