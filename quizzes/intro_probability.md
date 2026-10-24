# Introduction to Probability Quiz

Notes: [Introduction to Probability](../notes/probability/introduction_to_probability.md), [Axioms of Probability](../notes/probability/axioms_of_probability.md), [Conditional Probability](../notes/probability/conditional_probability.md), [Total Probability](../notes/probability/total_probability.md), [Bayes' Theorem](../notes/probability/bayes_theorem.md), [Probability Trees](../notes/probability/probability_tree.md), [Geometric Probability](../notes/probability/geometric_probability.md)

Check your understanding of sample spaces, the probability axioms, conditional probability, independence and Bayes' theorem.

#### Q. What is the probability of getting exactly **two heads** when flipping three fair coins?

* [ ] 1/8
* [ ] 1/4
* [x] 3/8
* [ ] 1/2

> **Explanation:** There are $2^3 = 8$ equally likely outcomes and $\binom{3}{2} = 3$ of them (HHT, HTH, THH) contain exactly two heads, so the probability is $3/8$.

#### Q. Which statement is a **consequence derived from** Kolmogorov's axioms rather than one of the axioms themselves?

* [ ] $P(A) \ge 0$ for every event $A$
* [ ] $P(S) = 1$ for the whole sample space $S$
* [ ] $P(A \cup B) = P(A) + P(B)$ for disjoint $A$ and $B$
* [x] $P(A^c) = 1 - P(A)$ for every event $A$

> **Explanation:** The axioms are non-negativity, normalisation and additivity for disjoint events. The complement rule follows from them because $A$ and $A^c$ are disjoint and together make up $S$.

#### Q. The probability of an event **A** given that event **B** has occurred is known as:

* [ ] Joint probability
* [ ] Marginal probability
* [x] Conditional probability
* [ ] Complementary probability

> **Explanation:** $P(A \mid B) = P(A \cap B)/P(B)$ restricts attention to outcomes where $B$ happened. Joint probability $P(A \cap B)$ does not condition on anything.

#### Q. Which statement is true for two **independent** events A and B with positive probabilities?

* [ ] The probability of their intersection is zero
* [ ] Knowing that B occurred changes the probability of A
* [x] The probability of their intersection is the product of their probabilities
* [ ] The probability of their union is the sum of their probabilities

> **Explanation:** Independence means $P(A \cap B) = P(A)P(B)$. A zero intersection describes mutually exclusive events, which are in fact dependent when both have positive probability.

#### Q. If a fair die is rolled, what is the probability of getting a number **greater than 4**?

* [ ] 1/6
* [x] 1/3
* [ ] 1/2
* [ ] 2/3

> **Explanation:** Only 5 and 6 are greater than 4, so the probability is $2/6 = 1/3$.

#### Q. What does **Bayes' theorem** let you compute?

* [x] $P(A \mid B)$ from $P(B \mid A)$, the prior $P(A)$ and $P(B)$
* [ ] $P(A \cap B)$ for events that are known to be independent
* [ ] $P(A \cup B)$ for events that are mutually exclusive
* [ ] $P(A^c)$ from the probability of the event $A$

> **Explanation:** Bayes' theorem reverses a conditional probability: $P(A \mid B) = P(B \mid A)P(A)/P(B)$. It is how a prior belief is updated after observing evidence $B$.

#### Q. If $P(A) = 0.4$ and $P(B) = 0.5$, and A and B are **independent**, what is $P(A \cap B)$?

* [x] 0.2
* [ ] 0.9
* [ ] 0.1
* [ ] 0.7

> **Explanation:** For independent events $P(A \cap B) = P(A)P(B) = 0.4 \times 0.5 = 0.2$. Adding the probabilities (0.9) would give the union of disjoint events instead.

#### Q. Two events A and B are **mutually exclusive** with $P(A) = 0.3$ and $P(B) = 0.4$. What is $P(A \cup B)$?

* [x] 0.7
* [ ] 0.12
* [ ] 0.58
* [ ] 1.0

> **Explanation:** Mutually exclusive events cannot occur together, so $P(A \cap B) = 0$ and $P(A \cup B) = 0.3 + 0.4 = 0.7$. The value 0.58 would apply only if the events were independent.

#### Q. If $P(A \mid B) = 0.8$ and $P(B) = 0.5$, what is $P(A \cap B)$?

* [ ] 0.3
* [x] 0.4
* [ ] 0.625
* [ ] 1.3

> **Explanation:** The multiplication rule gives $P(A \cap B) = P(A \mid B)P(B) = 0.8 \times 0.5 = 0.4$.

#### Q. A random variable X takes only the values 1, 2 and 3. Which assignment of $P(X=1), P(X=2), P(X=3)$ is a **valid probability distribution**?

* [ ] 0.5, 0.4, 0.2
* [ ] 0.6, 0.5, −0.1
* [x] 0.25, 0.25, 0.5
* [ ] 0.3, 0.3, 0.3

> **Explanation:** Probabilities must be non-negative and sum to 1. Only 0.25 + 0.25 + 0.5 = 1 satisfies both; the second option sums to 1 but contains a negative value.

#### Q. What is the **complement** of an event A?

* [ ] The event that A and some other event both occur
* [ ] The event that A occurs at least once in repeated trials
* [x] The set of all outcomes in the sample space that are not in A
* [ ] The event that A occurs given that another event occurred

> **Explanation:** The complement $A^c$ contains exactly the outcomes where $A$ does not happen, so $P(A^c) = 1 - P(A)$.

#### Q. One card is drawn from a standard 52-card deck. What is the probability that it is an **Ace or a King**?

* [ ] 2/52
* [ ] 4/52
* [x] 8/52
* [ ] 16/52

> **Explanation:** There are 4 Aces and 4 Kings and no card is both, so the events are disjoint: $4/52 + 4/52 = 8/52 = 2/13$.

#### Q. If $P(A) = 0.6$, $P(B) = 0.5$ and $P(A \cap B) = 0.3$, what is $P(A \cup B)$?

* [x] 0.8
* [ ] 1.1
* [ ] 0.3
* [ ] 0.9

> **Explanation:** The general addition rule subtracts the overlap that would otherwise be counted twice: $0.6 + 0.5 - 0.3 = 0.8$.

#### Q. In Bayes' theorem, what is the term for $P(B \mid A)$, the probability of the evidence B given the hypothesis A?

* [ ] Prior probability
* [ ] Marginal probability
* [ ] Posterior probability
* [x] Likelihood

> **Explanation:** $P(B \mid A)$ is the likelihood. The prior is $P(A)$, the posterior is $P(A \mid B)$, and the marginal probability of the evidence is $P(B)$.

#### Q. Two fair six-sided dice are rolled. What is the probability that the **sum is 7**?

* [x] 1/6
* [ ] 1/12
* [ ] 7/36
* [ ] 1/36

> **Explanation:** Six of the 36 equally likely ordered pairs sum to 7: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1). So the probability is $6/36 = 1/6$.

#### Q. What is the probability of drawing a **red card** from a standard 52-card deck?

* [x] 1/2
* [ ] 1/4
* [ ] 1/13
* [ ] 3/4

> **Explanation:** Hearts and diamonds are red, giving 26 red cards out of 52, so the probability is $26/52 = 1/2$.

#### Q. $P(A) = 0.3$, $P(B) = 0.5$ and $P(A \cap B) = 0.15$. Are A and B independent?

* [x] Yes, because $P(A \cap B) = P(A)P(B)$
* [ ] No, because $P(A \cap B)$ is not zero
* [ ] No, because $P(A) + P(B)$ is less than 1
* [ ] It cannot be decided without $P(A \cup B)$

> **Explanation:** $P(A)P(B) = 0.3 \times 0.5 = 0.15$, which equals $P(A \cap B)$, so the defining condition for independence holds. A non-zero intersection only rules out mutual exclusivity.

#### Q. If the probability of drawing a blue marble from a bag is 0.3, what is the probability of **not** drawing a blue marble?

* [ ] 0.3
* [x] 0.7
* [ ] 0.09
* [ ] 1.3

> **Explanation:** By the complement rule, $P(\text{not blue}) = 1 - 0.3 = 0.7$.

#### Q. A and B are **independent** with $P(A) = 0.3$ and $P(B) = 0.6$. What is $P(A \cup B)$?

* [ ] 0.9
* [x] 0.72
* [ ] 0.18
* [ ] 0.82

> **Explanation:** $P(A \cup B) = P(A) + P(B) - P(A)P(B) = 0.3 + 0.6 - 0.18 = 0.72$. Simply adding (0.9) double-counts the overlap.

#### Q. Which of the following is **not** an example of a conditional probability?

* [ ] The probability of drawing a red card given the first card drawn was black
* [x] The probability of rolling a 6 on a single fair die
* [ ] The probability of being late to work given that it is raining
* [ ] The probability of passing a test given that you studied

> **Explanation:** Rolling a 6 is an unconditional probability (1/6). Every other option restricts attention to cases where some other event has already happened.

#### Q. Machine M1 makes 60% of a factory's parts with a 2% defect rate; machine M2 makes the other 40% with a 5% defect rate. What is the probability that a randomly chosen part is **defective**?

* [ ] 0.035
* [x] 0.032
* [ ] 0.070
* [ ] 0.020

> **Explanation:** By the law of total probability, $P(D) = 0.6 \times 0.02 + 0.4 \times 0.05 = 0.012 + 0.020 = 0.032$. Averaging the two rates (0.035) ignores the different production shares.

#### Q. In a factory, M1 makes 60% of parts (2% defective) and M2 makes 40% (5% defective). Given that a part is defective, what is the probability it came from **M2**?

* [ ] 0.40
* [ ] 0.05
* [x] 0.625
* [ ] 0.375

> **Explanation:** Bayes' theorem gives $P(M2 \mid D) = \frac{0.4 \times 0.05}{0.032} = \frac{0.020}{0.032} = 0.625$. The prior share 0.40 rises because M2 has the higher defect rate.

#### Q. A disease affects 1% of a population. A test detects it 99% of the time and gives a false positive 5% of the time. Approximately what is the probability that a person who tests positive **has the disease**?

* [ ] 0.99
* [ ] 0.95
* [ ] 0.50
* [x] 0.17

> **Explanation:** $P(D \mid +) = \frac{0.01 \times 0.99}{0.01 \times 0.99 + 0.99 \times 0.05} = \frac{0.0099}{0.0594} \approx 0.17$. Because the disease is rare, false positives outnumber true positives.

#### Q. A point is chosen uniformly at random inside the unit square $[0,1] \times [0,1]$. What is the probability that its coordinates satisfy $x + y < 1$?

* [ ] 1/4
* [x] 1/2
* [ ] $\pi/4$
* [ ] 2/3

> **Explanation:** In geometric probability the answer is a ratio of areas. The region $x + y < 1$ is the triangle below the diagonal, with area $1/2$, out of a total area of 1.
