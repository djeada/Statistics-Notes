# Quizzes on Probability

This series of quizzes covers essential topics in probability theory, including:

- **Bayes' Theorem**: Deepen your understanding of Bayes' Theorem, exploring its applications in real-world scenarios such as medical diagnoses, spam filtering, and more.
- **Conditional Probability**: Test your ability to calculate probabilities under given conditions and explore the behavior of dependent and independent events.
- **Joint Probability**: Learn how to compute the probability of multiple events occurring together, and discover how joint probability is applied in various fields like machine learning and decision-making.
- **Marginal Probability**: Understand how to derive the probability of a single event by aggregating joint probabilities over other variables.
- **Independence**: Explore the concept of event independence and how to determine if two or more events are independent or dependent on each other.
- **Law of Total Probability**: Apply the law of total probability to break down complex probability problems.

## Bayes' Theorem

<details>
<summary>What is Bayes' Theorem?</summary>

Bayes' Theorem updates the probability of a hypothesis $A$ after observing evidence $B$ (with $P(B) > 0$):

$$P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}$$

where:

- $P(A|B)$ is the **posterior probability**, the probability of $A$ given that $B$ occurred,
- $P(B|A)$ is the **likelihood**, the probability of observing $B$ if $A$ is true,
- $P(A)$ is the **prior probability** of $A$,
- $P(B)$ is the **marginal probability** of the evidence, often computed as $P(B|A)P(A) + P(B|A^c)P(A^c)$.

It is widely used in medical testing, spam filtering and other diagnostic problems.

</details>

<details>
<summary>What is an example of applying Bayes' Theorem in medical testing?</summary>

A disease affects 1% of people, so $P(D) = 0.01$. The test has sensitivity $P(+|D) = 0.99$ and a false-positive rate $P(+|D^c) = 0.05$. For a person who tests positive:

$$P(D|+) = \frac{0.99 \times 0.01}{0.99 \times 0.01 + 0.05 \times 0.99} = \frac{0.0099}{0.0594} \approx 0.17$$

Even with an accurate test, only about 17% of positives actually have the disease, because the disease is rare and false positives outnumber true positives.

</details>

<details>
<summary>How does the Bayesian use of Bayes' Theorem differ from the frequentist view of probability?</summary>

Bayes' Theorem itself is a valid rule under every interpretation of probability. The difference lies in what probability means:

- **Frequentist**: probability is a long-run relative frequency, so parameters are fixed unknown constants and are not given probability distributions.
- **Bayesian**: probability expresses a degree of belief, so parameters get a **prior** distribution that Bayes' Theorem updates to a **posterior** as data arrive.

</details>

## Conditional Probability

<details>
<summary>What is conditional probability?</summary>

Conditional probability is the probability of an event $A$ given that another event $B$ has occurred. Knowing $B$ restricts the sample space to outcomes in $B$. For $P(B) > 0$:

$$P(A|B) = \frac{P(A \cap B)}{P(B)}$$

Here $P(A \cap B)$ is the joint probability that both $A$ and $B$ occur.

</details>

<details>
<summary>What is an example of conditional probability in everyday life?</summary>

Consider the probability of rain ($A$) given that the sky is cloudy ($B$). Because clouds make rain more likely, $P(A|B)$ is higher than the unconditional probability $P(A)$. For example, rain might happen on 20% of all days but on 50% of cloudy days.

</details>

<details>
<summary>How does conditional probability relate to independent events?</summary>

If $A$ and $B$ are **independent** and $P(B) > 0$, knowing that $B$ occurred does not change the probability of $A$:

$$P(A|B) = P(A)$$

This is equivalent to the product rule $P(A \cap B) = P(A)P(B)$.

</details>

<details>
<summary>How do you calculate the probability that two dependent events both occur?</summary>

Use the multiplication rule: multiply the probability of the first event by the conditional probability of the second given the first:

$$P(A \cap B) = P(A) \times P(B|A)$$

For example, drawing two aces without replacement from a 52-card deck has probability $\frac{4}{52} \times \frac{3}{51} = \frac{1}{221}$.

</details>

## Joint Probability

<details>
<summary>What is joint probability?</summary>

Joint probability is the probability that two or more events occur together, written $P(A \cap B)$ for two events. In general $P(A \cap B) = P(A)P(B|A)$. If the events are **independent**, this simplifies to the product of their individual probabilities:

$$P(A \cap B) = P(A) \times P(B)$$

</details>

<details>
<summary>What is an example of joint probability?</summary>

When rolling two fair dice, the probability that the first shows a 6 and the second shows a 6 is a joint probability. The dice are independent, so:

$$P(6 \cap 6) = \frac{1}{6} \times \frac{1}{6} = \frac{1}{36}$$

</details>

<details>
<summary>How does joint probability differ for dependent events?</summary>

For dependent events the joint probability is not the product of the individual probabilities. Use the conditional probability instead:

$$P(A \cap B) = P(A) \times P(B|A)$$

This accounts for the fact that the occurrence of $A$ changes the probability of $B$.

</details>

## Marginal Probability

<details>
<summary>What is marginal probability?</summary>

Marginal probability is the probability of a single event, regardless of the outcomes of other variables. If $B_1, \dots, B_n$ form a partition of the sample space, it is obtained by summing the joint probabilities:

$$P(A) = \sum_{j} P(A \cap B_j)$$

In a contingency table, marginal probabilities are the row or column totals divided by the grand total.

</details>

<details>
<summary>How does marginal probability relate to joint probability?</summary>

Marginal probabilities are obtained from a joint distribution by **summing** (discrete case) or **integrating** (continuous case) over the other variable. For example, $P(X = x) = \sum_y P(X = x, Y = y)$ and $f_X(x) = \int f_{X,Y}(x, y)\,dy$. The reverse is not possible in general: the marginals alone do not determine the joint distribution unless the variables are independent.

</details>

## Independence

<details>
<summary>What does it mean for two events to be independent?</summary>

Two events are independent if the occurrence of one does not change the probability of the other. Formally, $A$ and $B$ are independent if:

$$P(A \cap B) = P(A) \times P(B)$$

Then knowing that $B$ occurred gives no information about $A$, and vice versa. Independence is different from mutual exclusivity: disjoint events with positive probabilities are always dependent.

</details>

<details>
<summary>How can you test if two events are independent?</summary>

Check whether the joint probability equals the product of the individual probabilities, $P(A \cap B) = P(A) \times P(B)$, or equivalently whether $P(A|B) = P(A)$. For example, $P(A) = 0.3$, $P(B) = 0.5$ and $P(A \cap B) = 0.15$ are independent. With sample data the equality holds only approximately, so a chi-square test of independence is used instead.

</details>

## Law of Total Probability

<details>
<summary>What is the Law of Total Probability?</summary>

If $B_1, B_2, \dots, B_n$ are mutually exclusive events that together cover the whole sample space (a partition), each with $P(B_i) > 0$, then for any event $A$:

$$P(A) = \sum_{i} P(A|B_i) P(B_i)$$

For example, if machine 1 makes 60% of parts with a 2% defect rate and machine 2 makes 40% with a 5% defect rate, $P(\text{defect}) = 0.6(0.02) + 0.4(0.05) = 0.032$. The result is also the denominator in Bayes' Theorem.

</details>
