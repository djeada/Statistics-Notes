# Total Probability: Exercises

Practice for the note [The Law of Total Probability](../../notes/probability/total_probability.md).

## Problems

1. **Factory.** Machines $M_1,M_2,M_3$ produce 50%, 30%, and 20% of a factory's items with defect rates 2%, 3%, and 5%. Find the probability that a randomly chosen item is defective.

2. **Second draw.** A bag has 4 red and 6 blue balls. Two are drawn without replacement. Find the probability that the second ball is red. Compare with the probability that the first is red.

3. **Insurance.** 20% of drivers are high-risk with a yearly accident probability 0.3; the remaining 80% have yearly accident probability 0.1. Find the probability that a random driver has an accident this year and the expected number of accidents among 1,000 drivers.

4. **Two stages.** A fair die is rolled. On 1 or 2, a ball is drawn from urn A (3 red, 1 blue); on 3 through 6, from urn B (1 red, 3 blue). Find $P(\text{red})$.

5. **Weather chain.** $P(\text{rain Monday})=0.3$. If it rains on a day, it rains the next day with probability 0.6; if not, with probability 0.2. Find $P(\text{rain Tuesday})$ and $P(\text{rain Wednesday})$.

6. **Three coins.** One of three coins is chosen uniformly: a fair coin, a two-headed coin, and a coin with $P(\text{heads})=0.25$. It is flipped once. Find $P(\text{heads})$.

7. **Urns.** There are 5 urns labeled $0,1,2,3,4$, and urn $i$ has a fraction $i/4$ of white balls. An urn is chosen uniformly and one ball is drawn. Find $P(\text{white})$.

8. **Not a partition.** A student computes $P(A)$ using $B_1=\{\text{age}<30\}$ and $B_2=\{\text{age}>25\}$ with $P(B_1)=0.5$, $P(B_2)=0.6$. Why is the law of total probability not valid here?

## Solutions

### Solution 1

$$P(D)=\sum_i P(D\mid M_i)P(M_i)=0.02(0.5)+0.03(0.3)+0.05(0.2)=0.010+0.009+0.010=0.029.$$

So 2.9% of items are defective.

### Solution 2

Partition on the first ball:

$$P(R_2)=P(R_2\mid R_1)P(R_1)+P(R_2\mid B_1)P(B_1)=\frac39\cdot\frac4{10}+\frac49\cdot\frac6{10}=\frac{12}{90}+\frac{24}{90}=\frac{36}{90}=0.4.$$

This equals $P(R_1)=4/10$. By symmetry, each position in a random order is equally likely to hold a red ball.

### Solution 3

$$P(\text{accident})=0.3(0.2)+0.1(0.8)=0.06+0.08=0.14.$$

Expected accidents among 1,000 drivers: $1000\times0.14=140$.

### Solution 4

$P(A)=\frac26=\frac13$ and $P(B)=\frac46=\frac23$.

$$P(\text{red})=\frac34\cdot\frac13+\frac14\cdot\frac23=\frac14+\frac16=\frac{3}{12}+\frac{2}{12}=\frac5{12}\approx0.417.$$

### Solution 5

$$P(\text{rain Tue})=0.6(0.3)+0.2(0.7)=0.18+0.14=0.32.$$

Now use $P(\text{rain Tue})=0.32$ as the new prior:

$$P(\text{rain Wed})=0.6(0.32)+0.2(0.68)=0.192+0.136=0.328.$$

### Solution 6

$$P(H)=\frac13(0.5)+\frac13(1)+\frac13(0.25)=\frac{1.75}{3}=\frac7{12}\approx0.583.$$

### Solution 7

$$P(W)=\frac15\left(0+\frac14+\frac24+\frac34+1\right)=\frac15\cdot\frac{10}{4}=\frac12.$$

This agrees with the note's general result $P(W)=\tfrac12$ for any number of urns.

### Solution 8

A partition requires events that are mutually exclusive and exhaustive. Here $B_1$ and $B_2$ overlap (ages between 25 and 30 belong to both), so $P(B_1)+P(B_2)=1.1>1$ shows they cannot be disjoint. Summing $P(A\mid B_i)P(B_i)$ would count outcomes in the overlap twice. The fix is to use disjoint pieces such as $\{\text{age}\le25\}$, $\{25<\text{age}<30\}$, $\{\text{age}\ge30\}$.
