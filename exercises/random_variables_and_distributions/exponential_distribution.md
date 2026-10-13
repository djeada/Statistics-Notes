# Exponential Distribution - Exercises

Read [Exponential distribution](../../notes/random_variables_and_distributions/continuous/exponential_distribution.md) first. Parameter $\lambda$ is the rate.

## Problems

1. A device has exponential lifetime with mean 8 hours. Find $P(X>12)$.
2. Find the median of an exponential distribution with mean 8 hours and compare it with the mean.
3. Show the memoryless property and use it to find $P(X>15\mid X>5)$ for the device above.
4. Derive $E[X]$ and $\operatorname{Var}(X)$ by integration, using $E[X^2]$.
5. Customers arrive as a Poisson process with rate 3 per hour. Find the probability that the wait for the next arrival exceeds 30 minutes.
6. Two independent components have exponential lifetimes with means 2 and 3 hours. The system fails when the first one fails. Find the distribution of the system lifetime, its mean, and $P(\text{survive}>1)$.
7. Find the time $t$ such that 90% of devices (mean 8 hours) have failed.
8. Conceptual: show that the hazard rate $h(x)=f(x)/(1-F(x))$ of an exponential is constant and explain what this means for ageing.

## Solutions

### 1.
$\lambda=\tfrac18$. $P(X>12)=e^{-12/8}=e^{-1.5}=0.2231$.

### 2.
$P(X\le m)=0.5\Rightarrow1-e^{-\lambda m}=0.5\Rightarrow m=\dfrac{\ln2}{\lambda}=8\ln2=5.545$ hours.
The median is below the mean (8) because the distribution is right-skewed; $m/\text{mean}=\ln2=0.693$.

### 3.
$P(X>s+t\mid X>s)=\dfrac{e^{-\lambda(s+t)}}{e^{-\lambda s}}=e^{-\lambda t}=P(X>t)$.
$P(X>15\mid X>5)=P(X>10)=e^{-10/8}=e^{-1.25}=0.2865$.

### 4.
$E[X]=\int_0^\infty x\lambda e^{-\lambda x}dx$. By parts with $u=x$, $dv=\lambda e^{-\lambda x}dx$: $=\big[-xe^{-\lambda x}\big]_0^\infty+\int_0^\infty e^{-\lambda x}dx=0+\tfrac1\lambda$.
$E[X^2]=\int_0^\infty x^2\lambda e^{-\lambda x}dx=\big[-x^2e^{-\lambda x}\big]_0^\infty+2\int_0^\infty xe^{-\lambda x}dx=\tfrac{2}{\lambda}\cdot E[X]=\tfrac{2}{\lambda^2}$.
$\operatorname{Var}(X)=\tfrac2{\lambda^2}-\tfrac1{\lambda^2}=\tfrac1{\lambda^2}$.

### 5.
$\lambda=3$ per hour, $t=0.5$ hours: $P(T>0.5)=e^{-3(0.5)}=e^{-1.5}=0.2231$.

### 6.
$P(\min>t)=P(X_1>t)P(X_2>t)=e^{-t/2}e^{-t/3}=e^{-(1/2+1/3)t}=e^{-5t/6}$.
So the system lifetime is $\text{Exp}(5/6)$ with mean $\tfrac65=1.2$ hours.
$P(\text{survive}>1)=e^{-5/6}=0.4346$.

### 7.
$1-e^{-t/8}=0.9\Rightarrow e^{-t/8}=0.1\Rightarrow t=-8\ln0.1=8(2.3026)=18.42$ hours.

### 8.
$h(x)=\dfrac{\lambda e^{-\lambda x}}{e^{-\lambda x}}=\lambda$ for all $x$.
A constant hazard means a surviving item is "as good as new": the chance of failing in the next instant does not depend on age, which is the memoryless property.
