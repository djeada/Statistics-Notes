## The Multiplication Rule in Probability

The multiplication rule is a fundamental concept in probability theory. It is particularly useful when dealing with the probability of two or more events occurring in sequence or simultaneously. This rule has two forms, depending on whether the events are independent or dependent.

### Independent Events

Two events A and B are independent if the occurrence of one does not affect the probability of occurrence of the other. For independent events, the multiplication rule states:

$$
P(A \cap B) = P(A) \times P(B)
$$

This means the probability of both events A and B occurring is the product of their individual probabilities.

### Dependent Events

If the occurrence of event A in some way influences the occurrence of event B, these events are considered dependent. For dependent events, the probability of both events occurring is given by:

$$
P(A \cap B) = P(A|B) \times P(B)
$$

Here, \( P(A|B) \) is the conditional probability of event A given that event B has occurred. It represents the probability of A under the condition that B is known to have occurred.


## Independent Events

Two events are independent if the occurrence of one event does not affect the probability of the other event. In other words, events A and B are independent if:

$$
P(A|B) = P(A) \quad \text{and} \quad P(B|A) = P(B)
$$

### Example

In a deck of 52 playing cards, drawing two cards without replacement. Are the events "drawing a king on the first draw" and "drawing a king on the second draw" independent?

No, they are not independent. After drawing a king on the first draw, there are only 3 kings and 51 cards left in the deck. So, the probability of drawing a king on the second draw is affected by the first draw.

### Example

Consider two events defined on the set of integers from 1 to 100:

- A: The randomly drawn number from this set is divisible by 3
- B: The randomly drawn number is divisible by 7

Are events A and B statistically independent?

$$
P(A) = \frac{33}{100}, \quad P(B) = \frac{14}{100}, \quad P(A \cap B) = \frac{4}{100}
$$

Since $P(A) \cdot P(B) \neq P(A \cap B)$, the events are not statistically independent.

However, when we extend the set by numbers 101, 102, 103, 104, and 105, we have:

$$
P(A) = \frac{35}{105}, \quad P(B) = \frac{15}{105}, \quad P(A \cap B) = \frac{5}{105}
$$

Now, $P(A) \cdot P(B) = P(A \cap B)$, so the events are statistically independent in this case.


### Example: Probability of at least one of n independent events occurring

For n = 3:

$$
P(A \cup B \cup C) = P(A) + P(B) + P(C) - P(A \cap B) - P(A \cap C) - P(B \cap C) + P(A \cap B \cap C)
$$

We can reach this result more easily by using the probability of the complementary event.

For n independent events, the probability of none of the events occurring is the product of the probabilities of their complementary events. Thus, the probability of at least one event occurring is the complement of this probability:

$$
P(A \cup B \cup \cdots \cup_n) = 1 - P(A^c) \cdot P(B^c) \cdot \cdots \cdot P_n^c)
$$

where $A^c, B^c, \ldots, P_n^c$ are the complementary events of $A, B, \ldots, P_n$.

## Conditional Probability 

Conditional probability is the probability of an event occurring, given that another event has already occurred. The conditional probability of event A happening given that event B has occurred is denoted as P(A|B), and can be calculated using the formula:

$$
P(A|B) = \frac{P(A \cap B)}{P(B)}
$$

### Example

In a deck of 52 playing cards, there are 4 suits (hearts, diamonds, clubs, and spades) with 13 cards in each suit. What is the probability of drawing a king, given that the drawn card is a heart?

$$
P(\text{King}|\text{Heart}) = \frac{P(\text{King} \cap \text{Heart})}{P(\text{Heart})} = \frac{1/52}{13/52} = \frac{1}{13}
$$

### Example 

**Example**: What is the probability that the birthdays of two randomly selected people are different (B2)?

$$
P(B_2) = 1 - \frac{1}{365}
$$

What is the probability that the birthdays of three randomly selected people are different (B3)?

Let A3 be the event "the birthday of the third person is different from the birthdays of the first two people":

$$
P(B_3) = P(A_3 \cap B_2) = P(A_3 | B_2) P(B_2)
$$

$$
P(A_3 | B_2) = 1 - \frac{2}{365} \Rightarrow P(B_3) = P(A_3 | B_2) P(B_2) = \left(1 - \frac{2}{365}\right) \left(1 - \frac{1}{365}\right) = 0.9918
$$

For n people, we have:

$$
P(B_n) = P(A_n | B_{n-1}) \cdots P(A_3 | B_2) P(B_2)
$$

Note: When solving problems, it is important to identify which event is the condition:

$$
P(A \cap B) = P(A | B) P(B) \quad \text{or} \quad P(A \cap B) = P(B | A) P(A)
$$


## The Law of Total Probability

The law of total probability is used to calculate the probability of an event A occurring, given a partition of the sample space into events B1, B2, ..., Bn. The formula for the law of total probability is:

$$
P(A) = \sum_{i=1}^{n} P(A|B_i) \times P(B_i)
$$

### Example
In a bag, there are 3 red balls, 4 blue balls, and 5 green balls. We draw two balls without replacement. What is the probability that the second ball is red?

Partition the sample space into events B1 (first ball is red), B2 (first ball is blue), and B3 (first ball is green). Then, use the law of total probability:

1. If the first ball is red (B1), there are 2 red balls left out of 11 total balls. So, $P(\text{Red}|\text{B1}) = \frac{2}{11}$, and $P(\text{B1}) = \frac{3}{12}$.
2. If the first ball is blue (B2), there are still 3 red balls left out of 11 total balls. So, $P(\text{Red}|\text{B2}) = \frac{3}{11}$, and $P(\text{B2}) = \frac{4}{12}$.
3. If the first ball is green (B3), again there are 3 red balls left out of 11 total balls. So, $P(\text{Red}|\text{B3}) = \frac{3}{11}$, and $P(\text{B3}) = \frac{5}{12}$.

$$
P(\text{Second ball is red}) = P(\text{Red}|\text{B1})P(\text{B1}) + P(\text{Red}|\text{B2})P(\text{B2}) + P(\text{Red}|\text{B3})P(\text{B3}) \\
= \frac{2}{11} \times \frac{3}{12} + \frac{3}{11} \times \frac{4}{12} + \frac{3}{11} \times \frac{5}{12} = \frac{18}{44} = \frac{9}{22}
$$

### Example 1: Probability of drawing a white ball

Given n+1 urns with white and black balls, the ratio of the number of white balls to the total number of balls for the i-th urn is i/n (i=0, 1, 2, ..., n). We randomly draw one ball from a randomly chosen urn. What is the probability that the chosen ball is white?

The conditional probability of drawing a white ball from the i-th urn is:

$$
P(W | U_i) = \frac{i}{n}
$$

Where:
- `W` represents the event of drawing a white ball.
- `U_i` represents the event of choosing the i-th urn.

The probability of choosing each urn is equal:

$$
P(U_i) = \frac{1}{n+1}
$$

The desired probability of drawing a white ball is determined using the total probability formula:

$$
P(W) = \sum_{i=0}^{n} P(W | U_i) \cdot P(U_i) = \frac{1}{n+1} \sum_{i=0}^{n} \frac{i}{n} = \frac{1}{n(n+1)} \sum_{i=0}^{n} i
$$

Using the formula for the sum of the first n integers:

$$
\sum_{i=0}^{n} i = \frac{n(n+1)}{2}
$$

Now substitute this into the previous equation:

$$
P(W) = \frac{1}{n(n+1)} \cdot \frac{n(n+1)}{2} = \frac{1}{2}
$$


## Bayes' Theorem

Bayes' theorem is used to update the probability of an event based on new evidence. It relates the conditional probability of an event A given event B, to the conditional probability of event B given event A:

$$
P(A|B) = \frac{P(B|A) \times P(A)}{P(B)}
$$

### Example

In a medical test for a disease, the test has a 95% true positive rate (meaning that if someone has the disease, the test will be positive 95% of the time) and a 5% false positive rate (meaning that if someone does not have the disease, the test will be positive 5% of the time). The prevalence of the disease in the population is 2%. If a person tests positive, what is the probability that they actually have the disease?

Let A be the event "person has the disease" and B be the event "person tests positive". We want to find P(A|B):

$$
P(A|B) = \frac{P(B|A) \times P(A)}{P(B)}
$$

Using the law of total probability for P(B):

$$
P(B) = P(B|A) \times P(A) + P(B|\text{not } A) \times P(\text{not } A)
$$

Plugging in the values:

$$
P(A|B) = \frac{0.95 \times 0.02}{(0.95 \times 0.02) + (0.05 \times 0.98)} = \frac{0.019}{0.058} \approx 0.3276
$$

So, there is approximately a 32.76% chance that the person actually has the disease, given that they tested positive.


### Example 2: BSE "mad cow" disease test

Assuming the test result is positive, what is the probability that a cow has BSE?

Given quantities:

$$
P(T | B) = 0.70, P(T | B^c) = 0.10, P(B) = 0.02
$$

Where:
- `B` represents the event that a cow has BSE.
- `T` represents the event of a positive test result.
- `B^c` represents the complement of the event B, i.e., the event that a cow does not have BSE.

We are looking for the conditional probability:

$$
P(B | T) = \frac{P(B \cap T)}{P(T)} = \frac{P(T | B) \cdot P(B)}{P(T | B) \cdot P(B) + P(T | B^c) \cdot P(B^c)}
$$

First, we need to find the probability of a cow not having BSE:

$$
P(B^c) = 1 - P(B) = 1 - 0.02 = 0.98
$$

Now, we can calculate the conditional probability:

$$
P(B | T) = \frac{0.70 \cdot 0.02}{0.70 \cdot 0.02 + 0.10 \cdot 0.98} \approx 0.125
$$

The probability that a cow has BSE given a positive test result is approximately 0.125.


## Inclusion-Exclusion Principle

Example: What is the probability that during n dice rolls, at least one of the faces of the die does not appear even once?

Let Ai denote the event that face i does not appear during n dice rolls, i = 1,..., 6

Theorem: The Inclusion-Exclusion Principle allows us to find bounds on the sought probability. Introducing the following notation:

$$p_n(S_1, \dots, S_n) \equiv P(A_1 \cup A_2 \cup \dots \cup A_n) = P(A_1) - P(A_1 \cap A_2) + P(A_1 \cap A_2 \cap A_3) - \dots$$

We have:

$$p_n(S_1) \leq p_n(S_1, S_2) \geq p_n(S_1, S_2, S_3) \leq \dots$$

Calculate probabilities (i < j < k < ...):

$$p_n = \left(1 - \frac{5}{6}\right)^n + \binom{6}{2}\left(1 - \frac{4}{6}\right)^n - \binom{6}{3}\left(1 - \frac{3}{6}\right)^n + \binom{6}{4}\left(1 - \frac{2}{6}\right)^n - \binom{6}{5}\left(1 - \frac{1}{6}\right)^n$$

The sought probability is:

* 1-pn is the probability that during n rolls each face will appear at least once.
* $p_{10} ≈ 0.73$, $p_{12} ≈ 0.56$, $p_{13} ≈ 0.50$, $p_{15} ≈ 0.35$, $p_{20} ≈ 0.03$, $p_{25} ≈ 0.001$

## Probability Trees

Probability trees are a useful graphical tool to represent the possible outcomes of an experiment and their associated probabilities. They help in visualizing the structure of a probability problem and are particularly useful when dealing with conditional probabilities and independent events.

### Structure of Probability Trees

A probability tree is a directed tree diagram where each node represents a possible outcome of the experiment, and each edge is labeled with the probability of the corresponding outcome. The tree starts with a single node representing the initial state, and branches out to cover all possible outcomes. Each level of the tree corresponds to a different stage of the experiment.

### Rules for Probability Trees

1. The probabilities along each path from the root to a leaf must sum to 1.
2. The probability of an event is the sum of the probabilities of all paths that lead to that event.

### Example: Drawing Cards

```plaintext
           __Heart (1/4)
          |
Initial ──┤
          |
          |__Not Heart (3/4)
```

In this example, we are drawing one card from a standard deck of 52 cards. There are two possible outcomes: drawing a heart (with a probability of 1/4) and not drawing a heart (with a probability of 3/4).

In this example, we are drawing one card from a standard deck of 52 cards. There are two possible outcomes: drawing a heart (with a probability of 1/4) and not drawing a heart (with a probability of 3/4).

### Example: Tossing a Coin and Rolling a Die

```plaintext

           __Head (1/2)───1 (1/6)
          |               .
          |               .
Initial ──┤               6 (1/6)
          |       
          |__Tail (1/2)───1 (1/6)
                          .
                          .
                          6 (1/6)
```

In this example, we first toss a coin and then roll a die. The tree branches at the first level represent the outcomes of the coin toss (heads or tails), each with a probability of 1/2. The second level of branches represents the outcomes of rolling the die (1 to 6), each with a probability of 1/6.

### Example: Rolling Two Dice

```plaintext
           __1 (1/6)──1 (1/6)
          |          .
          |          .
          |          6 (1/6)
          |
          |__2 (1/6)──1 (1/6)
Initial ──┤          .
          |          .
          |          6 (1/6)
          |
          |__ ... (1/6)──1 (1/6)
          |          .
          |          .
          |          6 (1/6)
          |
          |__6 (1/6)──1 (1/6)
                   .
                   .
                   6 (1/6)
```

In this example, we roll two dice simultaneously. The first level of branches represents the outcomes of the first die (1 to 6), each with a probability of 1/6. The second level of branches represents the outcomes of the second die (1 to 6), each with a probability of 1/6. The probability of any specific combination is the product of the probabilities along the path (1/36).
