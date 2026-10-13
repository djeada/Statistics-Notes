# Uniform Distribution - Exercises

Read [Uniform distribution](../../notes/random_variables_and_distributions/continuous/uniform_distribution.md) first.

## Problems

1. $X\sim\text{Uniform}(0,10)$. Find $P(3<X<7)$, $E[X]$ and $\operatorname{Var}(X)$.
2. A bus arrives uniformly at random during a 15-minute period after you reach the stop. Find the probability that you wait more than 10 minutes, and the 80th percentile of the wait.
3. Derive $\operatorname{Var}(X)=(b-a)^2/12$ from $E[X]$ and $E[X^2]$.
4. In the note's simulation game the event time is $\text{Uniform}(2,4)$ seconds. Given that no event has occurred by 2.5 seconds, find the probability it occurs after 3.5 seconds.
5. Derive the MGF of $\text{Uniform}(a,b)$ and show that $M(t)\to1$ as $t\to0$ (use the series for $e^{tx}$).
6. Let $U\sim\text{Uniform}(0,1)$ and $Y=-\ln(U)/\lambda$. Show $Y\sim\text{Exp}(\lambda)$ (inverse-transform sampling).
7. For $X\sim\text{Uniform}(a,b)$, find the interval centred on the mean that contains 50% of the mass. For $\text{Uniform}(2,4)$ evaluate it.
8. Conceptual: why is $P(X=x)=0$ for every $x$ yet the variable always takes some value? And is $\text{Uniform}(0,1)$ density $f(x)=1$ a probability?

## Solutions

### 1.
$P(3<X<7)=\dfrac{7-3}{10}=0.4$. $E[X]=\tfrac{0+10}{2}=5$. $\operatorname{Var}(X)=\dfrac{10^2}{12}=8.333$.

### 2.
$X\sim\text{Uniform}(0,15)$. $P(X>10)=\dfrac{15-10}{15}=\tfrac13$.
80th percentile $x$: $F(x)=\tfrac{x}{15}=0.8\Rightarrow x=12$ minutes.

### 3.
$E[X^2]=\dfrac1{b-a}\int_a^bx^2dx=\dfrac{b^3-a^3}{3(b-a)}=\dfrac{a^2+ab+b^2}{3}$.
$\operatorname{Var}(X)=\dfrac{a^2+ab+b^2}{3}-\dfrac{(a+b)^2}{4}=\dfrac{4a^2+4ab+4b^2-3a^2-6ab-3b^2}{12}=\dfrac{a^2-2ab+b^2}{12}=\dfrac{(b-a)^2}{12}$.

### 4.
Conditioning on $X>2.5$ gives a uniform distribution on $(2.5,4)$ of length 1.5.
$P(X>3.5\mid X>2.5)=\dfrac{4-3.5}{4-2.5}=\dfrac{0.5}{1.5}=\tfrac13$.

### 5.
$M(t)=\dfrac1{b-a}\int_a^be^{tx}dx=\dfrac{e^{tb}-e^{ta}}{t(b-a)}$.
Near 0: $e^{tb}-e^{ta}=t(b-a)+\tfrac{t^2}{2}(b^2-a^2)+\dots$, so $M(t)=1+\tfrac{t}{2}(a+b)+\dots\to1$, and the linear coefficient is $\tfrac{a+b}{2}=E[X]$.

### 6.
For $y\ge0$: $P(Y\le y)=P(-\ln U\le\lambda y)=P(U\ge e^{-\lambda y})=1-e^{-\lambda y}$. This is the Exp($\lambda$) CDF.

### 7.
The middle 50% is $\mu\pm\tfrac{b-a}{4}$ (half of the length $\tfrac{b-a}{2}$ on each side). For $(2,4)$: $3\pm0.5=(2.5,3.5)$, length 1 out of 2 gives $0.5$.

### 8.
Single points have zero length, so zero probability; probability comes from intervals. Uncountably many outcomes each with probability 0 can still add to 1 through integration. The value $f(x)=1$ is a density (probability per unit length), not the probability of any outcome; on $\text{Uniform}(0,0.5)$ the density would be 2.
