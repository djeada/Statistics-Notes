## The Law of Total Probability

The law of total probability allows for the computation of the probability of an event A based on a set of mutually exclusive and exhaustive events. It's particularly useful when the overall sample space is divided into several distinct scenarios, or partitions, that cover all possible outcomes. The formula for the law of total probability is given by:

$$
P(A) = \sum_{i=1}^{n} P(A|B_i) \times P(B_i)
$$

where $B_1, B_2, ..., B_n$ are the partitions of the sample space and $P(A|B_i)$ is the conditional probability of A given $B_i$.

### Example: Probability of Drawing a Red Ball Second

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

### Example: Probability of Drawing a White Ball

Consider a set of n+1 urns labeled from 0 to n. Each urn contains a mix of white and black balls, where the ratio of white balls to the total number of balls in the i-th urn is i/n. If we randomly select one urn and then draw one ball from it, we want to find the probability that this ball is white.

#### Conditional Probability

The conditional probability of drawing a white ball from the i-th urn, denoted as $U_i$, is given by the ratio of white balls in that urn:

$$
P(W | U_i) = \frac{i}{n}
$$

Where:

- $W$ represents the event of drawing a white ball.
- $U_i$ represents the event of selecting the i-th urn.

#### Probability of Selecting Each Urn

Assuming each urn has an equal probability of being chosen, the probability of selecting any particular urn is:

$$
P(U_i) = \frac{1}{n+1}
$$

#### Total Probability

To find the overall probability of drawing a white ball, we use the law of total probability. This accounts for the probability of drawing a white ball from each urn weighted by the probability of selecting that urn:

$$
P(W) = \sum_{i=0}^{n} P(W | U_i) \cdot P(U_i) = \frac{1}{n+1} \sum_{i=0}^{n} \frac{i}{n}
$$

#### Summation

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
