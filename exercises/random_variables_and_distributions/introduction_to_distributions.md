# Introduction to Distributions - Exercises

Read [Introduction to Distributions](../../notes/random_variables_and_distributions/introduction_to_distributions.md) first. All problems have worked solutions below.

## Problems

1. A discrete random variable $X$ takes values $1,2,3,4,5$ with $P(X=x)=c\,x$. (a) Find $c$. (b) Find $P(X\ge 4)$. (c) Find $E[X]$ and $\operatorname{Var}(X)$.
2. A fair die is rolled until a 6 appears; let $X$ be the number of rolls. Find $P(X>4)$, $P(X\le 4)$ and $P(2\le X\le 4)$.
3. A continuous variable has density $f(x)=c\,x^2$ on $[0,3]$ and $0$ elsewhere. (a) Find $c$. (b) Find the CDF. (c) Find $P(1<X<2)$. (d) Find $E[X]$.
4. Explain why a density value can exceed 1 while a probability cannot. Give a concrete density with $f(x)=2$ on its support and show it integrates to 1. What is $P(X=0.25)$ for this variable?
5. The pmf of $X$ is $P(X=0)=0.2$, $P(X=1)=0.5$, $P(X=3)=0.3$. Write the CDF $F(x)$ for all real $x$, and evaluate $F(-1)$, $F(1)$, $F(2.5)$, $F(3)$. Where does $F$ jump and by how much?
6. A random variable has CDF $F(x)=1-e^{-2x}$ for $x\ge 0$ and $0$ for $x<0$. Find the density, $P(0.5<X\le 1)$ and the median.
7. A game costs 3 dollars to play. You roll a fair die and win the number shown in dollars if it is even, and nothing if it is odd. Find the expected net gain. Is the game fair?
8. The number of pets $N$ in a household has pmf $0.28, 0.35, 0.22, 0.10, 0.04, 0.01$ for $N=0,\dots,5$. Compute $E[N]$ and $\operatorname{Var}(N)$, and $P(N\le E[N])$.

## Solutions

### 1.
(a) The pmf must sum to 1: $c(1+2+3+4+5)=15c=1$, so $c=\tfrac1{15}$.

(b) $P(X\ge4)=\tfrac{4}{15}+\tfrac5{15}=\tfrac9{15}=0.6$.

(c) $E[X]=\sum x\cdot\tfrac{x}{15}=\tfrac{1+4+9+16+25}{15}=\tfrac{55}{15}=\tfrac{11}{3}\approx3.667$.
$E[X^2]=\sum x^2\cdot\tfrac{x}{15}=\tfrac{1+8+27+64+125}{15}=\tfrac{225}{15}=15$.
$\operatorname{Var}(X)=15-\left(\tfrac{11}{3}\right)^2=15-\tfrac{121}{9}=\tfrac{14}{9}\approx1.556$.

### 2.
$P(X=k)=(5/6)^{k-1}(1/6)$. "More than 4 rolls" means the first four rolls are all non-6: $P(X>4)=(5/6)^4=\tfrac{625}{1296}\approx0.4823$.
Then $P(X\le4)=1-0.4823=0.5177$.
$P(2\le X\le4)=P(X\le4)-P(X=1)=0.5177-0.1667=0.3510$.
Check: $0.1389+0.1157+0.0964=0.3510$.

### 3.
(a) $\int_0^3 c x^2\,dx=c\cdot\tfrac{3^3}{3}=9c=1\Rightarrow c=\tfrac19$.

(b) For $0\le x\le3$: $F(x)=\int_0^x \tfrac{t^2}{9}dt=\tfrac{x^3}{27}$; $F=0$ for $x<0$ and $F=1$ for $x>3$.

(c) $P(1<X<2)=F(2)-F(1)=\tfrac{8}{27}-\tfrac1{27}=\tfrac{7}{27}\approx0.2593$.

(d) $E[X]=\int_0^3 x\cdot\tfrac{x^2}{9}dx=\tfrac19\cdot\tfrac{3^4}{4}=\tfrac{81}{36}=\tfrac94=2.25$.

### 4.
A density is a probability per unit length, so only its integral over an interval has to be at most 1. Take $X\sim\text{Uniform}(0,0.5)$: $f(x)=2$ on $[0,0.5]$ and $\int_0^{0.5}2\,dx=1$. For any single point the interval has length 0, so $P(X=0.25)=\int_{0.25}^{0.25}2\,dx=0$.

### 5.
Accumulate the mass: $F(x)=0$ for $x<0$; $0.2$ for $0\le x<1$; $0.7$ for $1\le x<3$; $1$ for $x\ge3$.
$F(-1)=0$, $F(1)=0.2+0.5=0.7$, $F(2.5)=0.7$, $F(3)=1$.
Jumps occur at $0$ (size $0.2$), $1$ (size $0.5$) and $3$ (size $0.3$); each jump equals the pmf there, and $F$ is right-continuous.

### 6.
Density: $f(x)=F'(x)=2e^{-2x}$ for $x\ge0$.
$P(0.5<X\le1)=F(1)-F(0.5)=(1-e^{-2})-(1-e^{-1})=e^{-1}-e^{-2}=0.3679-0.1353=0.2325$.
Median $m$: $1-e^{-2m}=0.5\Rightarrow e^{-2m}=0.5\Rightarrow m=\tfrac{\ln2}{2}\approx0.3466$.

### 7.
Gain $G$ (before cost): $0$ for $1,3,5$ and $2,4,6$ dollars for the even faces.
$E[G]=\tfrac16(0+2+0+4+0+6)=\tfrac{12}{6}=2$ dollars.
Net gain $=2-3=-1$ dollar per play, so the game is not fair (it would be fair at a price of 2 dollars).

### 8.
$E[N]=0(0.28)+1(0.35)+2(0.22)+3(0.10)+4(0.04)+5(0.01)=0.35+0.44+0.30+0.16+0.05=1.30$.
$E[N^2]=0.35+4(0.22)+9(0.10)+16(0.04)+25(0.01)=0.35+0.88+0.90+0.64+0.25=3.02$.
$\operatorname{Var}(N)=3.02-1.30^2=3.02-1.69=1.33$.
$P(N\le1.3)=P(N\le1)=0.28+0.35=0.63$.
