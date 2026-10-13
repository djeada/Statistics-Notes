# Descriptive Statistics: Exercises

Practice for the note [Descriptive Statistics](../../notes/foundations/descriptive_statistics.md). Try each problem before opening the solutions. Unless stated otherwise, quartiles use the convention of the note: the one-based position $r=1+(n-1)\frac{P}{100}$ with linear interpolation.

## Problems

1. **Frequency table.** Twelve students rated a lecture on a 1-5 scale: $3,4,2,3,5,4,3,2,4,3,5,3$. Build a table with frequency, relative frequency, and cumulative relative frequency for each rating.

2. **Mean, median, mode.** Find the mean, median, and mode of $4,8,6,5,3,8,9,7$.

3. **Weighted mean.** A course grade is 50% exam, 30% project, and 20% homework. A student scores 80 on the exam, 90 on the project, and 70 on homework. Find the course grade.

4. **Geometric mean.** An investment grows by factors $1.10$, $0.95$, and $1.20$ in three consecutive years. Find the geometric mean growth factor, the average yearly growth rate, and compare it with the arithmetic mean of the factors.

5. **Variance and standard deviation.** For the data $2,4,4,4,5,5,7,9$ compute the population variance and standard deviation, and then the sample variance and standard deviation.

6. **Quartiles and outliers.** For the data $12,15,11,18,20,14,16,13,19$ find $Q_1$, $Q_2$, $Q_3$, the IQR, and the $1.5\,\mathrm{IQR}$ fences. Then a tenth value, $40$, is added. Recompute the quartiles, the fences, the mean, and the median, and decide whether $40$ is flagged as an outlier.

7. **Standardizing.** Anna scored 78 on an exam with mean 70 and standard deviation 8. Ben scored 85 on a different exam with mean 78 and standard deviation 10. Who did better relative to their class?

8. **Skewed data.** Annual incomes (in thousands) of six people are $30,32,35,36,38,400$. Compute the mean and median. Which better describes a typical person? How does the mean change if the value $400$ is removed?

9. **Linear transformation.** Every value in the data of Problem 5 is multiplied by 3 and then increased by 10. Find the new mean and the new population standard deviation without recomputing from scratch.

10. **Conceptual.** (a) Why does the sample variance divide by $n-1$ rather than $n$? (b) Name one situation where the mean is the right summary and one where the median is. (c) Can the standard deviation be negative? Can it be zero?

## Solutions

### Solution 1

$n=12$. Counting each rating: 2 appears 2 times, 3 appears 5 times, 4 appears 3 times, 5 appears 2 times. The frequencies add to $2+5+3+2=12$.

| Rating | Frequency | Relative frequency | Cumulative relative frequency |
| ---: | ---: | ---: | ---: |
| 2 | 2 | $2/12\approx16.7\%$ | $16.7\%$ |
| 3 | 5 | $5/12\approx41.7\%$ | $58.3\%$ |
| 4 | 3 | $3/12=25.0\%$ | $83.3\%$ |
| 5 | 2 | $2/12\approx16.7\%$ | $100\%$ |

### Solution 2

Sum: $4+8+6+5+3+8+9+7=50$, and $n=8$, so the mean is $50/8=6.25$.

Sorted: $3,4,5,6,7,8,8,9$. With $n=8$ the median is the average of the 4th and 5th values: $(6+7)/2=6.5$.

The value 8 appears twice and every other value once, so the mode is $8$.

### Solution 3

$$\bar{x}_w=\frac{0.5(80)+0.3(90)+0.2(70)}{0.5+0.3+0.2}=\frac{40+27+14}{1}=81.$$

### Solution 4

$$G=\sqrt[3]{1.10\times0.95\times1.20}=\sqrt[3]{1.254}\approx1.0784.$$

The average yearly growth is therefore about $7.84\%$. The arithmetic mean of the factors is $(1.10+0.95+1.20)/3=3.25/3\approx1.0833$, which is slightly larger, as expected ($G\le\bar{x}$). Only $G$ reproduces the total growth: $1.0784^3=1.254$.

### Solution 5

Mean: $(2+4+4+4+5+5+7+9)/8=40/8=5$.

Squared deviations: $(2-5)^2=9$, $(4-5)^2=1$ three times, $(5-5)^2=0$ twice, $(7-5)^2=4$, $(9-5)^2=16$. Sum: $9+3+0+4+16=32$.

Population: $\sigma^2=32/8=4$, so $\sigma=2$.

Sample: $s^2=32/7\approx4.571$, so $s=\sqrt{4.571}\approx2.138$.

### Solution 6

Sorted ($n=9$): $11,12,13,14,15,16,18,19,20$.

- $Q_1$: $r=1+8(0.25)=3$, so $Q_1=x_{(3)}=13$.
- $Q_2$: $r=1+8(0.5)=5$, so $Q_2=x_{(5)}=15$.
- $Q_3$: $r=1+8(0.75)=7$, so $Q_3=x_{(7)}=18$.
- $\mathrm{IQR}=18-13=5$. Fences: $13-1.5(5)=5.5$ and $18+1.5(5)=25.5$. All values lie inside.

With 40 added ($n=10$), sorted: $11,12,13,14,15,16,18,19,20,40$.

- $Q_1$: $r=1+9(0.25)=3.25$, so $Q_1=13+0.25(14-13)=13.25$.
- $Q_2$: $r=5.5$, so the median is $15+0.5(16-15)=15.5$.
- $Q_3$: $r=1+9(0.75)=7.75$, so $Q_3=18+0.75(19-18)=18.75$.
- $\mathrm{IQR}=18.75-13.25=5.5$. Upper fence: $18.75+1.5(5.5)=27$. Since $40>27$, it **is** flagged.
- Mean: the sum rises from 138 to 178, so the mean goes from $138/9\approx15.33$ to $178/10=17.8$. The median only moved from 15 to 15.5.

### Solution 7

$$z_{\text{Anna}}=\frac{78-70}{8}=1.0,\qquad z_{\text{Ben}}=\frac{85-78}{10}=0.7.$$

Anna is 1.0 standard deviations above her class mean, Ben 0.7. Anna did better relative to her class even though Ben's raw score is higher.

### Solution 8

Sum: $30+32+35+36+38+400=571$, so the mean is $571/6\approx95.17$ thousand.

Sorted values are already in order; the median is $(35+36)/2=35.5$ thousand.

The median describes a typical person far better: five of six people earn between 30 and 38, while the mean is pulled up by the single value 400. Removing 400: mean $=171/5=34.2$ thousand, close to the median, which confirms that the mean was driven by the extreme value.

### Solution 9

For $y=ax+b$ the mean transforms as $\bar{y}=a\bar{x}+b$ and the standard deviation as $\sigma_y=|a|\sigma_x$ (the shift does not change spread).

$$\bar{y}=3(5)+10=25,\qquad \sigma_y=3(2)=6.$$

### Solution 10

(a) Deviations are measured from $\bar{x}$, which is itself computed from the same data, so they are on average slightly smaller than deviations from the true mean $\mu$. Dividing by $n-1$ compensates for this and makes $s^2$ an unbiased estimator of $\sigma^2$.

(b) The mean is right when the total matters (revenue per customer, total cost divided by units) or for roughly symmetric data. The median is right for a "typical" value in strongly skewed data or data with outliers (incomes, house prices).

(c) $s=\sqrt{s^2}\ge0$ is never negative. It equals 0 exactly when all observations are identical.
