# The Law of Total Probability

The law of total probability computes an event's overall probability by separating the possible cases that can produce it. The cases must be disjoint and cover the sample space, so every outcome contributes exactly once. Within each case, multiply the event's conditional probability by the chance of reaching that case; then add the resulting joint probabilities:

$$
P(A) = \sum_{i=1}^{n} P(A|B_i) \times P(B_i)
$$

where $B_1, B_2, \ldots, B_n$ is a partition of the sample space (each with $P(B_i)>0$) and $P(A|B_i)$ is the conditional probability of A given $B_i$.

## Conditions for Applying the Law

For the law of total probability to hold, the events $B_1, B_2, \ldots, B_n$ must satisfy two conditions:

- **Mutually exclusive**: No two events can occur simultaneously, meaning $B_i \cap B_j = \emptyset$ for all $i \neq j$.
- **Exhaustive**: Together, the events cover the entire sample space, so $B_1 \cup B_2 \cup \cdots \cup B_n = S$.

When these conditions are met, every outcome in the sample space belongs to exactly one partition $B_i$. The law then computes $P(A)$ by summing the probability of $A$ within each partition, weighted by the probability of that partition itself. This decomposition is especially valuable when $P(A)$ is difficult to calculate directly but the conditional probabilities $P(A|B_i)$ and the partition probabilities $P(B_i)$ are known or easier to determine.

The law of total probability also serves as a key step in deriving Bayes' theorem, where $P(B)$ in the denominator is often expanded using this law.

## Why the weights are necessary

Because $A=\bigcup_i(A\cap B_i)$ is a disjoint union, additivity gives $P(A)=\sum_iP(A\cap B_i)$. The multiplication rule replaces each joint probability by $P(A\mid B_i)P(B_i)$. Thus total probability is a weighted average of the case-specific rates, with nonnegative weights summing to one. It must lie between the smallest and largest rates. An unweighted average is valid only when the case probabilities are equal.

For example, suppose a process uses machine one 90% of the time and machine two 10% of the time, with defect rates 1% and 10%. The overall defect probability is $0.9(0.01)+0.1(0.10)=0.019$, rather than the unweighted 5.5%. The weights describe the mixture of outputs in the target process.

## Example: Probability of Drawing a Red Ball Second

Suppose we have a bag containing 3 red balls, 4 blue balls, and 5 green balls, and we want to find the probability of drawing a red ball on the second draw without replacement. We can partition the sample space into three mutually exclusive events based on the outcome of the first draw:

- $B_1$: The first ball drawn is red.
- $B_2$: The first ball drawn is blue.
- $B_3$: The first ball drawn is green.

Using the law of total probability:

I. If the first ball is red ($B_1$), then there are 2 red balls left out of the remaining 11 balls. So:

- $P(\text{Red}|B_1) = \frac{2}{11}$
- $P(B_1) = \frac{3}{12}$

II. If the first ball is blue ($B_2$), there are still 3 red balls left out of the remaining 11 balls. So:

- $P(\text{Red}|B_2) = \frac{3}{11}$
- $P(B_2) = \frac{4}{12}$

III. If the first ball is green ($B_3$), there are still 3 red balls left out of the remaining 11 balls. So:

- $P(\text{Red}|B_3) = \frac{3}{11}$
- $P(B_3) = \frac{5}{12}$

The total probability that the second ball is red is the sum of the probabilities of drawing a red ball given each initial event times the probability of each initial event:

$$
P(\text{Second ball is red}) = P(\text{Red}|B_1)P(B_1) + P(\text{Red}|B_2)P(B_2) + P(\text{Red}|B_3)P(B_3)
$$

Substituting in the values:

$$
P(\text{Second ball is red}) = \frac{2}{11} \times \frac{3}{12} + \frac{3}{11} \times \frac{4}{12} + \frac{3}{11} \times \frac{5}{12} = \frac{6}{132} + \frac{12}{132} + \frac{15}{132} = \frac{33}{132} = 0.25
$$

Therefore, the probability of drawing a red ball second, without replacement, is $0.25$ or $\frac{1}{4}$.

This equals the initial red fraction, $3/12$, by symmetry: in a uniformly random ordering, every ball has the same chance of occupying the second position. Nevertheless, the first and second colors are dependent, since a red first draw lowers the conditional red probability from $3/12$ to $2/11$. A marginal probability can remain the same across positions even when the observations at those positions are dependent.

## Example: Probability of Drawing a White Ball

Consider a set of n+1 urns labeled from 0 to n. Each urn contains a mix of white and black balls, where the ratio of white balls to the total number of balls in the i-th urn is i/n. If we randomly select one urn and then draw one ball from it, we want to find the probability that this ball is white.

### Conditional Probability

The conditional probability of drawing a white ball from the i-th urn, denoted as $U_i$, is given by the ratio of white balls in that urn:

$$
P(W | U_i) = \frac{i}{n}
$$

Where:

- $W$ represents the event of drawing a white ball.
- $U_i$ represents the event of selecting the i-th urn.

### Probability of Selecting Each Urn

Assuming each urn has an equal probability of being chosen, the probability of selecting any particular urn is:

$$
P(U_i) = \frac{1}{n+1}
$$

### Total Probability

To find the overall probability of drawing a white ball, we use the law of total probability. This accounts for the probability of drawing a white ball from each urn weighted by the probability of selecting that urn:

$$
P(W) = \sum_{i=0}^{n} P(W | U_i) \cdot P(U_i) = \frac{1}{n+1} \sum_{i=0}^{n} \frac{i}{n}
$$

### Summation

The sum of the first n integers is given by the formula:

$$
\sum_{i=1}^{n} i = \frac{n(n+1)}{2}
$$

Note that the summation starts from i=1 since the 0-th urn contains no white balls and thus does not contribute to the probability of drawing a white ball.

Substituting the summation into the total probability formula, we get:

$$
P(W) = \frac{1}{n+1} \cdot \frac{1}{n} \cdot \frac{n(n+1)}{2} = \frac{1}{2}
$$

Thus, the probability of drawing a white ball from a randomly chosen urn is $\frac{1}{2}$, regardless of the number of urns.

Here $n$ is a positive integer, and urn selection is uniform across the $n+1$ urns. Pair urn $i$ with urn $n-i$: their white fractions sum to one, so their average is one half. This is a second way to see the result. Choosing uniformly from all balls pooled across urns would be a different experiment: larger urns would receive more weight, and the answer need not be one half unless their sizes and compositions imply that weighted average.
