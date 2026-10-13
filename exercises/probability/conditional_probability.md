# Conditional Probability: Exercises

Practice for the note [Conditional Probability and Multiplication Rule](../../notes/probability/conditional_probability.md).

## Problems

1. **Dice.** Two fair dice are rolled. Find $P(\text{sum}=8\mid\text{first die}=3)$ and $P(\text{first die}=3\mid\text{sum}=8)$.

2. **Contingency table.** Of 200 people, 30 of the 120 women and 32 of the 80 men own a bicycle. Find $P(\text{bicycle}\mid\text{woman})$, $P(\text{bicycle}\mid\text{man})$, and $P(\text{woman}\mid\text{bicycle})$.

3. **Cards without replacement.** Find the probability of drawing (a) two hearts in a row, (b) three aces in a row, from a standard deck without replacement.

4. **Urn.** An urn contains 5 red and 3 blue balls. Two are drawn without replacement. Find the probability that they have different colors.

5. **Independence check.** Two fair dice are rolled. Let $A$ be "the first die is even". Are $A$ and $B=\{\text{sum}=7\}$ independent? Are $A$ and $C=\{\text{sum}=8\}$ independent?

6. **At least one.** Find (a) the probability of at least one six in 4 rolls of a die, (b) the probability of at least one double-six in 24 throws of two dice.

7. **Birthdays.** For 15 people (365 equally likely birthdays) find the probability that at least two share a birthday. What is the smallest group size for which this probability exceeds $1/2$?

8. **Direction of conditioning.** $P(A)=0.1$, $P(B)=0.5$, $P(A\cap B)=0.08$. Compute $P(A\mid B)$ and $P(B\mid A)$ and explain why they differ.

9. **Two children.** A family has two children, each equally likely to be a girl or boy independently. Find $P(\text{both girls}\mid\text{at least one girl})$ and $P(\text{both girls}\mid\text{the older child is a girl})$.

## Solutions

### Solution 1

$P(\text{sum}=8\mid D_1=3)$: given the first die is 3, the sum is 8 only if the second die is 5, so $1/6$.

$P(D_1=3\mid\text{sum}=8)$: the sum 8 has 5 equally likely pairs $(2,6),(3,5),(4,4),(5,3),(6,2)$, and exactly one has first die 3, so $1/5$.

Via the definition: $\frac{P(D_1=3\cap\text{sum}=8)}{P(\text{sum}=8)}=\frac{1/36}{5/36}=\frac15$.

### Solution 2

Counts: women with bicycle 30, men with bicycle 32, so 62 bicycle owners in total.

$$P(\text{bicycle}\mid\text{woman})=\frac{30}{120}=0.25,\qquad P(\text{bicycle}\mid\text{man})=\frac{32}{80}=0.40,$$

$$P(\text{woman}\mid\text{bicycle})=\frac{30}{62}\approx0.484.$$

### Solution 3

(a) $\frac{13}{52}\cdot\frac{12}{51}=\frac{156}{2652}=\frac{1}{17}\approx0.0588$.

(b) $\frac{4}{52}\cdot\frac{3}{51}\cdot\frac{2}{50}=\frac{24}{132600}=\frac{1}{5525}\approx0.000181$.

### Solution 4

Two orders: red then blue, blue then red.

$$P=\frac58\cdot\frac37+\frac38\cdot\frac57=\frac{15}{56}+\frac{15}{56}=\frac{30}{56}=\frac{15}{28}\approx0.536.$$

### Solution 5

$P(A)=\frac12$, $P(B)=\frac{6}{36}=\frac16$. $A\cap B$: first die even and sum 7: $(2,5),(4,3),(6,1)$, so $P(A\cap B)=\frac{3}{36}=\frac1{12}$. Since $P(A)P(B)=\frac12\cdot\frac16=\frac1{12}$, $A$ and $B$ are **independent**.

$P(C)=\frac{5}{36}$. $A\cap C$: $(2,6),(4,4),(6,2)$, so $P(A\cap C)=\frac{3}{36}=\frac{6}{72}$. But $P(A)P(C)=\frac12\cdot\frac5{36}=\frac{5}{72}$. Not equal, so $A$ and $C$ are **dependent**.

### Solution 6

Use the complement of "no success".

(a) $1-\left(\frac56\right)^4=1-\frac{625}{1296}=\frac{671}{1296}\approx0.518$.

(b) $1-\left(\frac{35}{36}\right)^{24}\approx1-0.5086=0.4914$.

### Solution 7

$$P(\text{all different})=\frac{365}{365}\cdot\frac{364}{365}\cdots\frac{351}{365}\approx0.7471,$$

so $P(\text{shared})\approx1-0.7471=0.2529$.

For $n=22$: $P\approx0.4757$; for $n=23$: $P\approx0.5073$. The smallest group size exceeding $1/2$ is $n=23$.

### Solution 8

$$P(A\mid B)=\frac{0.08}{0.5}=0.16,\qquad P(B\mid A)=\frac{0.08}{0.1}=0.8.$$

They share the same numerator $P(A\cap B)$ but have different denominators, $P(B)$ versus $P(A)$. Since $A$ is rarer than $B$, most of $A$ lies inside $B$ ($80\%$), but only a small share of $B$ lies in $A$ ($16\%$).

### Solution 9

Equally likely outcomes (older, younger): $GG,GB,BG,BB$, each $1/4$.

At least one girl: $\{GG,GB,BG\}$, so $P(GG\mid\text{at least one girl})=\frac{1/4}{3/4}=\frac13$.

Older is a girl: $\{GG,GB\}$, so $P(GG\mid\text{older girl})=\frac{1/4}{2/4}=\frac12$.
