# Covariance Exercises

Read the note first: [Covariance](../../notes/joint_distributions_and_covariance/covariance.md). Solutions are at the end of this file.

## Problems

1. For the paired data $X=(2,4,6,8)$ and $Y=(1,5,4,10)$, compute the sample covariance (with $n-1$) step by step. Then compute the version with divisor $n$.
2. Without recomputing, what is the sample covariance if $100$ is added to every $X_i$? What if every $Y_i$ is multiplied by $3$?
3. A random pair takes the values $(0,1)$, $(1,0)$ and $(2,3)$ with probabilities $0.25$, $0.50$, $0.25$. Compute $\operatorname{Cov}(X,Y)$ in two ways: from the definition and from $E[XY]-E[X]E[Y]$.
4. Suppose $\operatorname{Var}(X)=4$, $\operatorname{Var}(Y)=9$ and $\operatorname{Cov}(X,Y)=3$. Compute $\operatorname{Var}(2X-3Y)$ and $\operatorname{Cov}(2X+1,\,3Y-5)$.
5. Let $X$ be uniform on $\{-1,0,1\}$ and $Y=X^2$. Show that $\operatorname{Cov}(X,Y)=0$ even though $Y$ is a function of $X$.
6. Let $\operatorname{Var}(X)=4$, $\operatorname{Var}(Y)=9$ and $\operatorname{Corr}(X,Y)=-0.5$. Compute $\operatorname{Var}(X+Y)$ and $\operatorname{Var}(X-Y)$. Compare with the independent case.
7. Height $H$ (in metres) and weight $W$ (in kg) have $\operatorname{Cov}(H,W)=0.9$. What is the covariance if height is expressed in centimetres? Why is covariance a poor measure of strength?
8. Is it possible to have $\sigma_X=2$, $\sigma_Y=4$ and $\operatorname{Cov}(X,Y)=10$? Explain.
9. The covariance matrix of $(X,Y)$ is $\Sigma=\begin{pmatrix}4&3\\3&9\end{pmatrix}$. Find the correlation and the eigenvalues of $\Sigma$. Which value is the largest variance along any direction?

## Solutions

**1.** $\bar X=20/4=5$ and $\bar Y=20/4=5$. Deviations: $X-\bar X=(-3,-1,1,3)$ and $Y-\bar Y=(-4,0,-1,5)$. Products: $(12,\,0,\,-1,\,15)$, sum $=26$.
Sample covariance: $26/(4-1)=8.667$. Divisor $n$: $26/4=6.5$. The $n$-divisor version is smaller by the factor $(n-1)/n=3/4$.

**2.** Adding a constant leaves deviations unchanged, so the covariance stays $8.667$. Multiplying $Y$ by $3$ multiplies the covariance by $3$: $3\times8.667=26$.

**3.** $E[X]=0(0.25)+1(0.50)+2(0.25)=1$; $E[Y]=1(0.25)+0+3(0.25)=1$.
Definition: $E[(X-1)(Y-1)]=(-1)(0)(0.25)+(0)(-1)(0.50)+(1)(2)(0.25)=0.5$.
Shortcut: $E[XY]=0\cdot1(0.25)+1\cdot0(0.50)+2\cdot3(0.25)=1.5$, so $\operatorname{Cov}=1.5-1\cdot1=0.5$. ✓

**4.** $\operatorname{Var}(2X-3Y)=2^2(4)+(-3)^2(9)+2(2)(-3)(3)=16+81-36=61$.
$\operatorname{Cov}(2X+1,3Y-5)=2\cdot3\cdot\operatorname{Cov}(X,Y)=6\cdot3=18$ (constants drop out).

**5.** $E[X]=0$, $Y\in\{1,0,1\}$ so $E[Y]=\tfrac23$, and $XY=X^3\in\{-1,0,1\}$ so $E[XY]=0$. Then $\operatorname{Cov}=0-0\cdot\tfrac23=0$. Knowing $X$ determines $Y$ exactly, so the variables are dependent; covariance only detects the linear part, and the dependence here is symmetric (U-shaped).

**6.** $\operatorname{Cov}=\rho\sigma_X\sigma_Y=-0.5\cdot2\cdot3=-3$. Then $\operatorname{Var}(X+Y)=4+9+2(-3)=7$ and $\operatorname{Var}(X-Y)=4+9-2(-3)=19$. If independent both would be $13$. Negative covariance makes the sum less variable and the difference more variable.

**7.** Converting metres to centimetres multiplies $H$ by $100$, so the covariance becomes $0.9\times100=90$ (cm kg). The relationship is unchanged but the number is $100$ times larger, so the magnitude depends on units and cannot be read as strength; correlation, which divides by both standard deviations, is unit-free.

**8.** No. The Cauchy-Schwarz inequality gives $|\operatorname{Cov}(X,Y)|\le\sigma_X\sigma_Y=8$, and $10>8$. Equivalently, this would imply a correlation of $10/8=1.25>1$.

**9.** $\rho=3/\sqrt{4\cdot9}=3/6=0.5$. The characteristic equation is $\lambda^2-13\lambda+(36-9)=\lambda^2-13\lambda+27=0$, so $\lambda=\dfrac{13\pm\sqrt{169-108}}{2}=\dfrac{13\pm\sqrt{61}}{2}\approx10.405,\ 2.595$. The largest variance along any direction (unit vector) is $\lambda_{\max}\approx10.405$, which exceeds both $\sigma_X^2=4$ and $\sigma_Y^2=9$ because of the positive covariance. The trace $13$ equals $\lambda_1+\lambda_2$ ✓.
