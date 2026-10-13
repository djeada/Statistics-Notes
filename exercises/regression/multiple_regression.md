# Multiple Regression: Exercises

Review the note [Multiple Linear Regression](../../notes/regression/multiple_regression.md) first. Problems 1, 2, 5 and 7 use the five-student data set from the note:

| Student | Hours ($x_1$) | Attendance ($x_2$) | Score ($y$) |
|---|---|---|---|
| 1 | 2 | 70 | 65 |
| 2 | 3 | 80 | 70 |
| 3 | 5 | 60 | 75 |
| 4 | 7 | 90 | 85 |
| 5 | 9 | 95 | 95 |

with $\sum x_1=26$, $\sum x_2=395$, $\sum y=390$, $\sum x_1^2=168$, $\sum x_2^2=32025$, $\sum x_1x_2=2165$, $\sum x_1y=2165$, $\sum x_2y=31325$, and $\mathrm{SST}=580$.

## Problems

1. Write the normal equations $\mathbf{X}^\top\mathbf{X}\hat{\boldsymbol\beta}=\mathbf{X}^\top\mathbf{y}$ explicitly (a $3\times3$ system) for the data above and verify that $\hat{\boldsymbol\beta}\approx(49.182,\ 3.7856,\ 0.1156)^\top$ satisfies the first row.
2. Compute the centred sums $S_{11},S_{22},S_{12},S_{1y},S_{2y}$ and use the two-predictor closed form to obtain $\hat\beta_1$, $\hat\beta_2$, $\hat\beta_0$.
3. For the balanced design $x_1=(0,0,1,1)$, $x_2=(0,1,0,1)$, $y=(3,5,6,10)$, compute $\hat\beta_0,\hat\beta_1,\hat\beta_2$, the residuals, SSE, SST, $R^2$ and adjusted $R^2$. Why are the hand calculations so easy here?
4. For the same balanced data compute $F$ for the overall test and the $t$ statistic for $\hat\beta_1$. Give the degrees of freedom and comment on the power of the test.
5. For the five-student data, SSE $\approx1.835$. Compute $R^2$, adjusted $R^2$, and $F$ for $H_0:\beta_1=\beta_2=0$. The critical value is $F_{0.95}(2,2)=19.0$. Decide.
6. In problem 5 the individual statistic for $x_2$ is $t\approx2.54$ with $\mathrm{SE}(\hat\beta_2)\approx0.0454$ and $t_{0.975,2}=4.303$. Is $x_2$ significant? Reconcile this with the highly significant overall $F$.
7. Regress $y$ on $x_1$ alone for the five-student data. Compare the slope with $\hat\beta_1=3.786$ from problem 2 and explain why they differ.
8. (Conceptual) A model with $n=20$ and $p=5$ has $R^2=0.60$. Compute adjusted $R^2$ and the overall $F$. Then add a sixth predictor that raises $R^2$ to $0.61$ and recompute adjusted $R^2$. Should the predictor be kept?
9. Compute the VIF for $r_{x_1x_2}=0.677$, $0.95$ and $0.99$, and the corresponding inflation of the standard error of $\hat\beta_1$.
10. Take $x_1=(2,4,6,8)$, $x_2=(1,2,3,4)$, $y=(50,60,70,80)$. Show that $\mathbf{X}^\top\mathbf{X}$ is singular, and show that every pair $(\beta_1,\beta_2)$ with $\beta_1+\beta_2/2=5$ (and $\beta_0=40$) gives the same fit.
11. (Conceptual) In the model $y=2+3x_1+1x_2+0.5x_1x_2+\varepsilon$ interpret the effect of a one-unit increase in $x_1$ when $x_2=0$ and when $x_2=4$. Why is the coefficient 3 not "the effect of $x_1$" in general?

## Solutions

**Problem 1.** With $n=5$:

$$
\begin{pmatrix}5&26&395\\26&168&2165\\395&2165&32025\end{pmatrix}
\begin{pmatrix}\hat\beta_0\\\hat\beta_1\\\hat\beta_2\end{pmatrix}=
\begin{pmatrix}390\\2165\\31325\end{pmatrix}.
$$

First row: $5(49.182)+26(3.7856)+395(0.1156)=245.91+98.43+45.66=390.0$. ✓

**Problem 2.** $\bar x_1=5.2$, $\bar x_2=79$, $\bar y=78$.
$S_{11}=168-5(5.2)^2=32.8$; $S_{22}=32025-5(79)^2=820$; $S_{12}=2165-5(5.2)(79)=111$; $S_{1y}=2165-5(5.2)(78)=137$; $S_{2y}=31325-5(79)(78)=515$.
$D=S_{11}S_{22}-S_{12}^2=26896-12321=14575$.
$\hat\beta_1=(S_{1y}S_{22}-S_{12}S_{2y})/D=(112340-57165)/14575=55175/14575\approx3.7856$.
$\hat\beta_2=(S_{2y}S_{11}-S_{12}S_{1y})/D=(16892-15207)/14575=1685/14575\approx0.1156$.
$\hat\beta_0=78-3.7856(5.2)-0.1156(79)=78-19.685-9.133\approx49.182$.

**Problem 3.** $\bar x_1=\bar x_2=0.5$, $\bar y=6$. $S_{11}=S_{22}=1$ and $S_{12}=(-.5)(-.5)+(-.5)(.5)+(.5)(-.5)+(.5)(.5)=0$, so the predictors are orthogonal and each slope is a simple regression slope.
$S_{1y}=(-.5)(-3)+(-.5)(-1)+(.5)(0)+(.5)(4)=4$, $S_{2y}=(-.5)(-3)+(.5)(-1)+(-.5)(0)+(.5)(4)=3$.
$\hat\beta_1=4$, $\hat\beta_2=3$, $\hat\beta_0=6-4(.5)-3(.5)=2.5$.
Fitted: $2.5,\ 5.5,\ 6.5,\ 9.5$; residuals: $0.5,\ -0.5,\ -0.5,\ 0.5$; $\mathrm{SSE}=1$.
$\mathrm{SST}=9+1+0+16=26$, $R^2=1-1/26\approx0.962$.
Adjusted $R^2=1-\dfrac{1/(4-2-1)}{26/3}=1-0.1154\approx0.885$.
Because $S_{12}=0$ the normal equations decouple, so the coefficients do not depend on which other predictors are in the model.

**Problem 4.** $F=\dfrac{(26-1)/2}{1/1}=12.5$ on $(2,1)$ df. $s^2=1$, $\mathrm{SE}(\hat\beta_1)=s/\sqrt{S_{11}}=1$, so $t=4/1=4$ on $n-p-1=1$ df. With only one residual degree of freedom the critical values are enormous ($t_{0.975,1}=12.71$, $F_{0.95}(2,1)=199.5$), so the test has almost no power despite $R^2=0.96$: neither is significant.

**Problem 5.** $R^2=1-1.835/580=0.9968$.
Adjusted $R^2=1-\dfrac{1.835/2}{580/4}=1-\dfrac{0.9177}{145}=0.9937$.
$F=\dfrac{(580-1.835)/2}{1.835/2}=\dfrac{289.08}{0.9177}\approx315.0$. Since $315>19.0$ we reject $H_0$ (exact $p\approx0.003$): at least one slope is nonzero.

**Problem 6.** $t=0.1156/0.0454\approx2.54<4.303$, so $x_2$ is not significant at 5 % (exact $p\approx0.126$) once $x_1$ is in the model, while $x_1$ ($t\approx16.7$, $p\approx0.004$) is. There is no contradiction: $F$ tests whether *some* predictor helps, and $x_1$ alone gives that. The $t$ test for $x_2$ asks whether $x_2$ adds anything *beyond* $x_1$.

**Problem 7.** Simple slope $=S_{1y}/S_{11}=137/32.8\approx4.177$, versus $3.786$. The predictors are correlated ($r\approx0.677$) and $x_2$ has a positive coefficient, so the simple regression slope absorbs part of the effect of attendance: $\text{simple slope}=\hat\beta_1+\hat\beta_2\cdot(S_{12}/S_{11})=3.7856+0.1156(111/32.8)=3.7856+0.3912=4.177$. This is the omitted-variable bias formula. Multiple-regression coefficients are *partial* effects, holding the other predictors fixed.

**Problem 8.** $\text{Adj }R^2=1-(1-0.60)\dfrac{19}{14}=1-0.4(1.357)=0.457$.
$F=\dfrac{0.60/5}{0.40/14}=\dfrac{0.12}{0.02857}=4.2$ (critical $F_{0.95}(5,14)\approx2.96$: significant).
With six predictors: $\text{Adj }R^2=1-0.39\cdot\dfrac{19}{13}=1-0.570=0.430<0.457$. $R^2$ went up but adjusted $R^2$ fell, so the new predictor does not pay for the lost degree of freedom; do not keep it (on this criterion).

**Problem 9.** $\mathrm{VIF}=1/(1-r^2)$:
- $r=0.677$: $1/(1-0.458)=1.85$; $\sqrt{\mathrm{VIF}}=1.36$.
- $r=0.95$: $1/(1-0.9025)=10.26$; $\sqrt{\mathrm{VIF}}=3.20$.
- $r=0.99$: $1/(1-0.9801)=50.3$; $\sqrt{\mathrm{VIF}}=7.09$.
The standard error of $\hat\beta_1$ is multiplied by $\sqrt{\mathrm{VIF}}$ relative to the uncorrelated case.

**Problem 10.** Here $x_2=x_1/2$. Centred sums: $S_{11}=20$, $S_{22}=5$, $S_{12}=10$, so the $2\times2$ determinant $=20\cdot5-10^2=0$; equivalently the third column of $\mathbf{X}$ is a multiple of the second, the rank of $\mathbf{X}$ is $2<3$, and $\mathbf{X}^\top\mathbf{X}$ cannot be inverted. For any $(\beta_1,\beta_2)$: $\beta_1x_1+\beta_2x_2=(\beta_1+\beta_2/2)x_1$, so any pair with $\beta_1+\beta_2/2=5$ gives $\hat y=40+5x_1$, the same fitted values (and zero residuals). Only the combination $\gamma=\beta_1+\beta_2/2=5$ is identified; software typically returns the minimum-norm solution $(4,2)$.

**Problem 11.** The effect of a unit increase in $x_1$ is $\partial y/\partial x_1=3+0.5x_2$: it equals $3$ at $x_2=0$ and $3+0.5(4)=5$ at $x_2=4$. In a model with an interaction the coefficient 3 is the effect of $x_1$ only at $x_2=0$ (which may be outside the data); the "effect of $x_1$" depends on the value of $x_2$. Centering $x_2$ makes the main effect interpretable at the mean of $x_2$.
