## Independence, Conditional, Compound
Independent Events: A and B are independent iff:
* $P(A \cap B) = P(A)P(B)$
* $P(A|B) = P(A)$
* $P(B|A) = P(B)$

* Conditional Probability: $P(A|B) = \frac{P(A,B)}{P(B)}$
* Bayes Theorem: $P(A|B) = \frac{P(B|A)P(A)}{P(B)}$
* Joint Probability: $P(A,B) = P(B|A)P(A)$
* Marginal Probability: $P(A)$

## Conditional Probability and Independence

### Definition of Conditional Probability

Conditional probability is the probability of an event occurring, given that another event has already occurred. The conditional probability of event A happening given that event B has occurred is denoted as P(A|B), and can be calculated using the formula:

$$
P(A|B) = \frac{P(A \cap B)}{P(B)}
$$

### Example

In a deck of 52 playing cards, there are 4 suits (hearts, diamonds, clubs, and spades) with 13 cards in each suit. What is the probability of drawing a king, given that the drawn card is a heart?

$$
P(\text{King}|\text{Heart}) = \frac{P(\text{King} \cap \text{Heart})}{P(\text{Heart})} = \frac{1/52}{13/52} = \frac{1}{13}
$$

### The Multiplication Rule

The multiplication rule is used to find the probability of two events A and B happening together:

$$
P(A \cap B) = P(A|B) \times P(B)
$$

### Independent Events

Two events are independent if the occurrence of one event does not affect the probability of the other event. In other words, events A and B are independent if:

$$
P(A|B) = P(A) \quad \text{and} \quad P(B|A) = P(B)
$$

This means that for independent events, the multiplication rule simplifies to:

$$
P(A \cap B) = P(A) \times P(B)
$$

### Example

In a deck of 52 playing cards, drawing two cards without replacement. Are the events "drawing a king on the first draw" and "drawing a king on the second draw" independent?

No, they are not independent. After drawing a king on the first draw, there are only 3 kings and 51 cards left in the deck. So, the probability of drawing a king on the second draw is affected by the first draw.

### The Law of Total Probability

The law of total probability is used to calculate the probability of an event A occurring, given a partition of the sample space into events B1, B2, ..., Bn. The formula for the law of total probability is:

$$
P(A) = \sum_{i=1}^{n} P(A|B_i) \times P(B_i)
$$

### Example

In a bag, there are 3 red balls, 4 blue balls, and 5 green balls. We draw two balls without replacement. What is the probability that the second ball is red?

Partition the sample space into events B1 (first ball is red), B2 (first ball is blue), and B3 (first ball is green). Then, use the law of total probability:

$$
P(\text{Second ball is red}) = P(\text{Red}|\text{B1})P(\text{B1}) + P(\text{Red}|\text{B2})P(\text{B2}) + P(\text{Red}|\text{B3})P(\text{B3}) \\
= \frac{2}{11} \times \frac{3}{12} + \frac{3}{11} \times \frac{4}{12} + \frac{3}{11} \times \frac{5}{12} = \frac{18}{44} = \frac{9}{22}
$$

### Bayes' Theorem

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

# Probability Trees

Probability trees are a useful graphical tool to represent the possible outcomes of an experiment and their associated probabilities. They help in visualizing the structure of a probability problem and are particularly useful when dealing with conditional probabilities and independent events.

### Structure of Probability Trees

A probability tree is a directed tree diagram where each node represents a possible outcome of the experiment, and each edge is labeled with the probability of the corresponding outcome. The tree starts with a single node representing the initial state, and branches out to cover all possible outcomes. Each level of the tree corresponds to a different stage of the experiment.

### Rules for Probability Trees

1. The probabilities along each path from the root to a leaf must sum to 1.
2. The probability of an event is the sum of the probabilities of all paths that lead to that event.

### Examples

#### Example 1: Drawing Cards

```plaintext
           __Heart (1/4)
          |
Initial ──┤
          |
          |__Not Heart (3/4)
```

In this example, we are drawing one card from a standard deck of 52 cards. There are two possible outcomes: drawing a heart (with a probability of 1/4) and not drawing a heart (with a probability of 3/4).

In this example, we are drawing one card from a standard deck of 52 cards. There are two possible outcomes: drawing a heart (with a probability of 1/4) and not drawing a heart (with a probability of 3/4).

#### Example 2: Tossing a Coin and Rolling a Die

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

## Example 3: Rolling Two Dice

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
