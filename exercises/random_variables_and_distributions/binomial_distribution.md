# Binomial Distribution - Exercises

Read [Binomial distribution](../../notes/random_variables_and_distributions/discrete/binomial_distribution.md) first.

## Problems

1. $X\sim\text{Binomial}(8,0.25)$. Find $P(X=2)$ and $P(X\ge1)$.
2. For $X\sim\text{Binomial}(20,0.3)$ find the mean, variance and standard deviation.
3. Derive $E[X]$ and $E[X^2]$ for $\text{Binomial}(5,0.4)$ from the MGF $M(t)=(pe^t+1-p)^n$.
4. For $\text{Binomial}(10,0.35)$ find the most likely value by computing the ratio $P(X=k+1)/P(X=k)$.
5. Each of 12 items is independently defective with probability 0.05. Find the probability that at least one is defective, and the expected number of defectives.
6. A multiple-choice quiz has 5 questions with 4 options each. A student guesses every answer. Find the probability of at least 3 correct.
7. A shipment of $n=1000$ parts has defect probability $p=0.002$. Compare the exact binomial $P(X=3)$ with its Poisson approximation.
8. Conceptual: a bag has 10 red and 10 blue balls; 5 balls are drawn without replacement and $X$ counts the red ones. Why is $X$ not exactly binomial? Which assumption fails?

## Solutions

### 1.
$P(X=2)=\binom82(0.25)^2(0.75)^6=28(0.0625)(0.17798)=0.3115$.
$P(X\ge1)=1-P(X=0)=1-0.75^8=1-0.1001=0.8999$.

### 2.
$E[X]=np=20(0.3)=6$. $\operatorname{Var}(X)=np(1-p)=20(0.3)(0.7)=4.2$. $\text{SD}=\sqrt{4.2}=2.049$.

### 3.
$M(t)=(0.4e^t+0.6)^5$.
$M'(t)=5(0.4e^t)(0.4e^t+0.6)^4\Rightarrow M'(0)=5(0.4)(1)^4=2$.
$M''(t)=5(0.4e^t)(0.4e^t+0.6)^4+20(0.4e^t)^2(0.4e^t+0.6)^3\Rightarrow M''(0)=2+20(0.16)=2+3.2=5.2$.
So $E[X]=2$, $E[X^2]=5.2$ and $\operatorname{Var}(X)=5.2-4=1.2=np(1-p)=5(0.4)(0.6)$. This agrees with $E[X^2]=np(1-p)+n^2p^2=1.2+4$.

### 4.
$\dfrac{P(X=k+1)}{P(X=k)}=\dfrac{n-k}{k+1}\cdot\dfrac{p}{1-p}=\dfrac{10-k}{k+1}\cdot\dfrac{0.35}{0.65}$. This exceeds 1 when $(10-k)(0.35)>(k+1)(0.65)$, i.e. $3.5-0.35k>0.65k+0.65$, i.e. $k<2.85$.
So the pmf increases up to $k=3$ and then falls: the mode is $k=3$, equal to $\lfloor(n+1)p\rfloor=\lfloor3.85\rfloor$.
Check: $P(2)=0.1757$, $P(3)=0.2522$, $P(4)=0.2377$.

### 5.
$P(\text{at least one})=1-0.95^{12}=1-0.5404=0.4596$.
Expected defectives $=12(0.05)=0.6$.

### 6.
$X\sim\text{Binomial}(5,0.25)$.
$P(3)=\binom53(0.25)^3(0.75)^2=10(0.015625)(0.5625)=0.0879$.
$P(4)=5(0.25)^4(0.75)=5(0.00390625)(0.75)=0.0146$.
$P(5)=(0.25)^5=0.00098$.
$P(X\ge3)=0.0879+0.0146+0.0010=0.1035$.

### 7.
Binomial: $\binom{1000}{3}(0.002)^3(0.998)^{997}=0.18063$.
Poisson with $\lambda=np=2$: $\dfrac{e^{-2}2^3}{3!}=\dfrac{8(0.13534)}{6}=0.18045$.
The two agree to three decimals because $n$ is large and $p$ small.

### 8.
Draws without replacement are not independent and the success probability changes after each draw (first red: $10/20$; second red given first red: $9/19$). The "independent trials with constant $p$" assumption fails; $X$ is hypergeometric. With a very large population relative to the sample size the binomial is a good approximation.
