# Probability Trees: Exercises

Practice for the note [Probability Trees](../../notes/probability/probability_tree.md).

## Problems

1. **Coin then die.** A fair coin is tossed and then a fair die is rolled. Find $P(\text{heads and an even number})$ and $P(\text{tails and a 6})$. What is $P(\text{die}\ge5)$?

2. **Marbles.** A bag has 5 red and 3 green marbles. Two are drawn without replacement. Draw the tree and find $P(RR)$, $P(GG)$, and $P(\text{one of each})$.

3. **Three draws.** Three balls are drawn without replacement from 4 red and 6 blue. Find $P(\text{exactly two red})$ using the tree.

4. **Diagnostic tree.** Prevalence 5%, sensitivity 90%, specificity 95%. Build the tree and find $P(+)$ and $P(\text{disease}\mid+)$.

5. **Free throws.** A shooter hits the first shot with probability 0.7. After a hit the next shot is hit with probability 0.8; after a miss, with probability 0.5. Find $P(\text{both hit})$, $P(\text{exactly one hit})$, $P(\text{at least one hit})$.

6. **Best-of-three.** Team A wins each game independently with probability 0.6. Find the probability that A wins a best-of-three series.

7. **Spot the error.** A tree has first branches $\text{rain}\,(0.3)$ and $\text{no rain}\,(0.7)$. After rain: umbrella $0.9$, no umbrella $0.1$. After no rain: umbrella $0.2$, no umbrella $0.7$. What is wrong? Fix it and find $P(\text{umbrella})$.

8. **Biased coin.** A coin with $P(H)=0.6$ is tossed three times. How many leaves does the tree have, and what is $P(\text{exactly two heads})$?

## Solutions

### Solution 1

Branch probabilities multiply along a path.

$$P(H\text{ and even})=\frac12\cdot\frac36=\frac14,\qquad P(T\text{ and }6)=\frac12\cdot\frac16=\frac1{12}.$$

$P(\text{die}\ge5)=\frac26=\frac13$, regardless of the coin (the stages are independent).

### Solution 2

Tree: first draw R $(5/8)$ or G $(3/8)$. After R: R $(4/7)$, G $(3/7)$. After G: R $(5/7)$, G $(2/7)$.

$$P(RR)=\frac58\cdot\frac47=\frac{20}{56}=\frac5{14},\qquad P(GG)=\frac38\cdot\frac27=\frac6{56}=\frac3{28}.$$

One of each: $RG+GR=\frac58\cdot\frac37+\frac38\cdot\frac57=\frac{15}{56}+\frac{15}{56}=\frac{30}{56}=\frac{15}{28}$.

Check: $\frac{10}{28}+\frac{3}{28}+\frac{15}{28}=1$.

### Solution 3

Paths with exactly two red and one blue: RRB, RBR, BRR.

$$P(RRB)=\frac4{10}\cdot\frac39\cdot\frac68=\frac{72}{720},\quad P(RBR)=\frac4{10}\cdot\frac69\cdot\frac38=\frac{72}{720},\quad P(BRR)=\frac6{10}\cdot\frac49\cdot\frac38=\frac{72}{720}.$$

Sum: $\frac{216}{720}=0.3$.

### Solution 4

Specificity 95% means a false positive rate of 5%.

Paths: disease and $+$: $0.05\cdot0.9=0.045$; disease and $-$: $0.05\cdot0.1=0.005$; no disease and $+$: $0.95\cdot0.05=0.0475$; no disease and $-$: $0.95\cdot0.95=0.9025$ (the four add to 1).

$$P(+)=0.045+0.0475=0.0925,\qquad P(D\mid+)=\frac{0.045}{0.0925}\approx0.486.$$

### Solution 5

Let $H_1,H_2$ denote hits.

- Both hit: $0.7\cdot0.8=0.56$.
- Exactly one: hit then miss $0.7\cdot0.2=0.14$, miss then hit $0.3\cdot0.5=0.15$, total $0.29$.
- At least one $=1-P(\text{both miss})=1-0.3\cdot0.5=0.85$.

Check: $0.56+0.29+0.15=1$.

### Solution 6

A wins the series by winning the first two games (AA) or by winning two of the first three with a loss in between (ABA, BAA).

$$P=0.6^2+2(0.6^2)(0.4)=0.36+0.288=0.648.$$

### Solution 7

The branches leaving the node "no rain" must sum to 1, but $0.2+0.7=0.9$. The "no umbrella" branch should be $0.8$.

$$P(\text{umbrella})=0.3(0.9)+0.7(0.2)=0.27+0.14=0.41.$$

### Solution 8

Each toss has 2 branches, so there are $2^3=8$ leaves. Exactly two heads: HHT, HTH, THH, each with probability $0.6^2\cdot0.4=0.144$.

$$P=3(0.144)=0.432.$$
