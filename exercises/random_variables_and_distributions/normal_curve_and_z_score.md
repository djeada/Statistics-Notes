# Normal Curve and Z-Scores - Exercises

Read [Normal Curve and Z-Scores](../../notes/random_variables_and_distributions/normal_curve_and_z_score.md) first. Heights of fathers: $\mu=68.3$ in, $\sigma=1.8$ in (as in the note) unless stated otherwise. Table values are rounded to four decimals; software gives slightly different last digits.

## Problems

1. Using the empirical rule, give the interval containing about 95% of heights and the percentage of fathers taller than 71.9 in.
2. Find $P(X<66)$.
3. Find $P(67<X<70)$.
4. Find the 90th percentile of heights.
5. Exam A has $\mu=70,\ \sigma=8$ and you scored 78. Exam B has $\mu=55,\ \sigma=5$ and you scored 65. On which exam did you do relatively better?
6. IQ scores are $N(100,15^2)$. Find $P(\text{IQ}>130)$ and the IQ needed to be in the top 1%.
7. A measurement is normal with mean 50 and $P(X<40)=0.1587$. Find $\sigma$.
8. For the data $4,8,6,5,12$ compute the sample mean, sample standard deviation and the z-score of each value. Verify that the z-scores have mean 0 and sample variance 1.

## Solutions

### 1.
Empirical rule: $\mu\pm2\sigma=68.3\pm3.6=(64.7,\,71.9)$.
The 5% outside is split evenly into two tails, so about $2.5\%$ lie above 71.9 in (indeed $71.9$ is $z=2$, and $1-0.9772=0.0228$).

### 2.
$z=\dfrac{66-68.3}{1.8}=\dfrac{-2.3}{1.8}=-1.28$. From the table $\Phi(-1.28)=0.1003$.
So $P(X<66)\approx0.100$ (exact $z=-1.278$ gives $0.1007$).

### 3.
$z_{70}=\dfrac{70-68.3}{1.8}=\dfrac{1.7}{1.8}=0.94$, $\Phi(0.94)=0.8264$.
$z_{67}=\dfrac{67-68.3}{1.8}=\dfrac{-1.3}{1.8}=-0.72$, $\Phi(-0.72)=0.2358$.
$P(67<X<70)=0.8264-0.2358=0.5906$ (unrounded: $0.5924$).

### 4.
For the 90th percentile $z_{0.90}=1.2816$.
$x=\mu+z\sigma=68.3+1.2816(1.8)=68.3+2.307=70.61$ inches.

### 5.
Exam A: $z=\dfrac{78-70}{8}=1.0$. Exam B: $z=\dfrac{65-55}{5}=2.0$.
Exam B is 2 standard deviations above the mean versus 1 for A, so you did relatively better on B.

### 6.
$z=\dfrac{130-100}{15}=2$, so $P(\text{IQ}>130)=1-\Phi(2)=1-0.9772=0.0228$.
Top 1%: $z_{0.99}=2.326$, IQ $=100+2.326(15)=100+34.9=134.9$.

### 7.
$\Phi(z)=0.1587\Rightarrow z=-1$. Hence $\dfrac{40-50}{\sigma}=-1\Rightarrow\sigma=10$.

### 8.
$\bar x=\tfrac{4+8+6+5+12}{5}=\tfrac{35}{5}=7$.
Deviations: $-3,\,1,\,-1,\,-2,\,5$; squares $9,1,1,4,25$ sum to 40.
$s^2=\tfrac{40}{4}=10$, $s=\sqrt{10}=3.162$.
z-scores: $-3/3.162=-0.949$, $0.316$, $-0.316$, $-0.632$, $1.581$.
Sum $=(-3+1-1-2+5)/3.162=0$, so mean 0. Sum of squares $=40/10=4$, divided by $n-1=4$ gives sample variance 1.
