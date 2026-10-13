# Statistical Moments - Exercises

Read [Statistical Moments](../../notes/random_variables_and_distributions/statistical_moments.md) first.

## Problems

1. $X$ takes values $0,1,2$ with probabilities $0.2,0.5,0.3$. Compute $E[X]$, $E[X^2]$, $\operatorname{Var}(X)$ and the third central moment $\mu_3$. Is the distribution skewed left or right?
2. Derive the MGF of a Bernoulli($p$) variable and use it to recover $E[X]$ and $\operatorname{Var}(X)$.
3. For $X\sim\text{Exp}(\lambda)$ with $M_X(t)=\lambda/(\lambda-t)$, find $E[X^n]$ for general $n$ by differentiating, and evaluate $E[X^3]$ for $\lambda=2$.
4. $X\sim\text{Poisson}(\lambda_1)$ and $Y\sim\text{Poisson}(\lambda_2)$ are independent. Use MGFs to identify the distribution of $X+Y$.
5. A variable has MGF $M(t)=(0.3e^t+0.7)^5$. Identify the distribution, then find the mean, the variance and $P(X=2)$.
6. If $E[X]=3$ and $\operatorname{Var}(X)=4$, find the mean and variance of $Y=2X-1$, and express $M_Y(t)$ in terms of $M_X$.
7. Using raw moments, show that the exponential distribution has third central moment $2/\lambda^3$ and skewness 2, independent of $\lambda$.
8. Three unit point masses sit at positions $-1,0,3$. Compute the moment of inertia about the axis at $0$ and about the centre of mass, and relate the two to $E[X^2]$ and $\operatorname{Var}(X)$.

## Solutions

### 1.
$E[X]=0(0.2)+1(0.5)+2(0.3)=1.1$.
$E[X^2]=0+0.5+4(0.3)=1.7$, so $\operatorname{Var}(X)=1.7-1.1^2=1.7-1.21=0.49$.
Central moments: $\mu_3=0.2(-1.1)^3+0.5(-0.1)^3+0.3(0.9)^3=0.2(-1.331)+0.5(-0.001)+0.3(0.729)=-0.2662-0.0005+0.2187=-0.048$.
The third central moment is negative, so the distribution is (slightly) left-skewed; skewness $=\mu_3/\sigma^3=-0.048/0.343=-0.140$.

### 2.
$X\in\{0,1\}$, so $M_X(t)=E[e^{tX}]=(1-p)e^{0}+pe^{t}=1-p+pe^t$.
$M_X'(t)=pe^t\Rightarrow E[X]=M'(0)=p$. $M_X''(t)=pe^t\Rightarrow E[X^2]=p$.
$\operatorname{Var}(X)=p-p^2=p(1-p)$.

### 3.
Write $M(t)=\lambda(\lambda-t)^{-1}$. Then $M'(t)=\lambda(\lambda-t)^{-2}$, $M''(t)=2\lambda(\lambda-t)^{-3}$, $M'''(t)=6\lambda(\lambda-t)^{-4}$, and in general $M^{(n)}(t)=n!\,\lambda(\lambda-t)^{-(n+1)}$.
At $t=0$: $E[X^n]=n!\,\lambda\cdot\lambda^{-(n+1)}=\dfrac{n!}{\lambda^n}$.
For $\lambda=2$, $n=3$: $E[X^3]=\tfrac{6}{8}=0.75$.

### 4.
$M_{X+Y}(t)=M_X(t)M_Y(t)$ by independence $=e^{\lambda_1(e^t-1)}e^{\lambda_2(e^t-1)}=e^{(\lambda_1+\lambda_2)(e^t-1)}$.
This is the MGF of a Poisson($\lambda_1+\lambda_2$) variable, so by uniqueness of the MGF $X+Y\sim\text{Poisson}(\lambda_1+\lambda_2)$.

### 5.
The binomial MGF is $(pe^t+1-p)^n$, so $n=5$, $p=0.3$.
Mean $np=1.5$; variance $np(1-p)=5(0.3)(0.7)=1.05$.
$P(X=2)=\binom52(0.3)^2(0.7)^3=10(0.09)(0.343)=0.3087$.

### 6.
$E[Y]=2(3)-1=5$. $\operatorname{Var}(Y)=2^2\cdot4=16$ (the shift $-1$ does not change the spread).
$M_Y(t)=E[e^{t(2X-1)}]=e^{-t}E[e^{2tX}]=e^{-t}M_X(2t)$.

### 7.
Raw moments: $E[X]=\tfrac1\lambda$, $E[X^2]=\tfrac{2}{\lambda^2}$, $E[X^3]=\tfrac{6}{\lambda^3}$.
Expand $\mu_3=E[(X-\mu)^3]=E[X^3]-3\mu E[X^2]+3\mu^2E[X]-\mu^3=E[X^3]-3\mu E[X^2]+2\mu^3$.
$\mu_3=\tfrac6{\lambda^3}-3\cdot\tfrac1\lambda\cdot\tfrac2{\lambda^2}+2\cdot\tfrac1{\lambda^3}=\tfrac{6-6+2}{\lambda^3}=\tfrac{2}{\lambda^3}$.
$\sigma^3=\lambda^{-3}$, so skewness $=\tfrac{2/\lambda^3}{1/\lambda^3}=2$.

### 8.
About the axis at 0: $I_0=\sum m_ir_i^2=1+0+9=10$ (so $E[X^2]=10/3$ per unit probability weight $1/3$).
Centre of mass: $\bar x=\tfrac{-1+0+3}{3}=\tfrac23$.
About $\bar x$: $I_c=\left(-\tfrac53\right)^2+\left(-\tfrac23\right)^2+\left(\tfrac73\right)^2=\tfrac{25+4+49}{9}=\tfrac{78}{9}=\tfrac{26}{3}\approx8.667$.
Parallel-axis check: $I_0-N\bar x^2=10-3\cdot\tfrac49=10-\tfrac43=\tfrac{26}{3}$. In probability terms, with weights $1/3$: $\operatorname{Var}=E[X^2]-\mu^2=\tfrac{10}{3}-\tfrac49=\tfrac{26}{9}$, which is $I_c/3$.
