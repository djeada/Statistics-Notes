## Axioms of Probability

Probability theory is based on a set of principles, or axioms, that define the properties of the probability measure. These axioms, first formalized by the Russian mathematician Andrey Kolmogorov, are the foundation upon which the entire framework of probability is built.

### The Three Axioms

I. **Non-negativity** states that the probability of any event A is a non-negative number. This reflects the idea that an event either happens or it doesn't, and thus, the probability cannot be negative.

$$
P(A) \geq 0
$$

II. **Unit Measure** ensures that the probability of the sample space S, which includes all possible outcomes of an experiment, is always equal to 1. This is equivalent to saying that it's certain at least one of the possible outcomes will occur.

$$
P(S) = 1
$$

III. The axiom of **additivity** is about disjoint events, also known as mutually exclusive events. If events A and B cannot both occur at the same time, the probability of either event A or event B occurring is the sum of their individual probabilities.

$$
P(A \cup B) = P(A) + P(B) \ \text{if} \ A \cap B = \emptyset
$$

Let's expand the example of rolling a fair six-sided die with more rigor, detailing the probability calculations and clarifying how to apply the rules of probability step-by-step.

### Example: Probabilities of Events in a Dice Roll

We'll examine various probability calculations based on outcomes when rolling a fair six-sided die. The sample space for a single roll of a six-sided die is:

$$
S = \{1, 2, 3, 4, 5, 6\}
$$

Each face of the die is equally likely to occur, so the probability of any single outcome is:

$$
P(\text{any specific number}) = \frac{1}{6}
$$

#### 1. Probability of Rolling a 5 or 6

- The events "rolling a 5" and "rolling a 6" are **mutually exclusive**, meaning they cannot happen at the same time (you can't roll both 5 and 6 on a single die roll).
- To find the probability of either event occurring, we use the addition rule for mutually exclusive events:

$$
P(5 \text{ or } 6) = P(5) + P(6)
$$

Since:

$$
P(5) = \frac{1}{6}, \quad P(6) = \frac{1}{6}
$$

we have:

$$
P(5 \text{ or } 6) = \frac{1}{6} + \frac{1}{6} = \frac{2}{6} = \frac{1}{3}
$$

So, the probability of rolling either a 5 or a 6 is $\frac{1}{3}$.

#### 2. Probability of Rolling an Even or Odd Number

- Every number on a die is either even or odd, and no number can be both. These events are **mutually exclusive**, but together they cover the entire sample space $S$.
- The possible even numbers are $\{2, 4, 6\}$, and the possible odd numbers are $\{1, 3, 5\}$. Since the entire sample space is covered by these two groups, the probability of rolling either an even or an odd number is:

$$
P(\text{even} \text{ or } \text{odd}) = P(S) = 1
$$

This makes sense intuitively because the outcome will always be either even or odd on a six-sided die.

#### 3. Probability of Rolling an Even Number or a 3

- The events "rolling an even number" and "rolling a 3" are **mutually exclusive** because 3 is not an even number. 
- The possible even numbers are $\{2, 4, 6\}$, so:

$$
P(\text{even}) = \frac{3}{6} = \frac{1}{2}
$$

The probability of rolling a 3 is:

$$
P(3) = \frac{1}{6}
$$

Since the events are mutually exclusive, we add the probabilities:

$$
P(\text{even} \text{ or } 3) = P(\text{even}) + P(3) = \frac{1}{2} + \frac{1}{6}
$$

To add these fractions, we convert to a common denominator:

$$
\frac{1}{2} = \frac{3}{6}
$$

Therefore:

$$
P(\text{even} \text{ or } 3) = \frac{3}{6} + \frac{1}{6} = \frac{4}{6} = \frac{2}{3}
$$

So, the probability of rolling either an even number or a 3 is $\frac{2}{3}$.

#### 4. Probability of Rolling an Even Number or a 4

In this case, the events "rolling an even number" and "rolling a 4" are **not mutually exclusive** because 4 is an even number. Therefore, if we simply added the probabilities of both events, we would count the outcome of rolling a 4 twice.

First, calculate the probability of rolling an even number (as above):

$$
P(\text{even}) = \frac{3}{6} = \frac{1}{2}
$$

Next, calculate the probability of rolling a 4:

$$
P(4) = \frac{1}{6}
$$

Since 4 is already included in the set of even numbers, we subtract the overlap to avoid double-counting. The overlap is the probability of rolling a 4, which is:

$$
P(\text{even} \text{ and } 4) = P(4) = \frac{1}{6}
$$

Now, applying the general addition rule for events that are **not mutually exclusive**:

$$
P(\text{even} \text{ or } 4) = P(\text{even}) + P(4) - P(\text{even} \text{ and } 4)
$$

Substituting the values:

$$
P(\text{even} \text{ or } 4) = \frac{1}{2} + \frac{1}{6} - \frac{1}{6}
$$

Simplifying:

$$
P(\text{even} \text{ or } 4) = \frac{1}{2} = \frac{3}{6}
$$

Therefore, the probability of rolling either an even number or a 4 is $\frac{1}{2}$.

### Example: Deck of Cards
Let’s break down this card deck probability example with more mathematical rigor and explicit steps to clarify how to calculate these probabilities in detail.

#### 1. Probability of Drawing a Heart or a Queen

Consider a standard deck of 52 playing cards, which includes:

- 13 hearts (one for each rank: 2 through Ace),
- 4 queens (one for each suit: hearts, diamonds, clubs, and spades),
- The **queen of hearts** belongs to both the hearts group and the queens group, creating an overlap.

We are tasked with calculating the probability of drawing a card that is either a heart or a queen. This is an example where the events are **not mutually exclusive**, as one card (the queen of hearts) belongs to both categories.

To find the probability of the union of two events (i.e., a card that is either a heart or a queen), we use the **addition rule** for probabilities:

$$
P(\text{Heart} \cup \text{Queen}) = P(\text{Heart}) + P(\text{Queen}) - P(\text{Heart} \cap \text{Queen})
$$

where:

- $P(\text{Heart})$ is the probability of drawing a heart,
- $P(\text{Queen})$ is the probability of drawing a queen,
- $P(\text{Heart} \cap \text{Queen})$ is the probability of drawing a card that is both a heart and a queen (i.e., the queen of hearts).

#### Step-by-Step Breakdown:

I. **Calculate $P(\text{Heart})$**:

- There are 13 hearts in the deck, and the deck contains 52 cards total.
- The probability of drawing a heart is:

$$
P(\text{Heart}) = \frac{13}{52}
$$

II. **Calculate $P(\text{Queen})$**:

- There are 4 queens in the deck (one from each suit: hearts, diamonds, clubs, spades).
- The probability of drawing a queen is:

$$
P(\text{Queen}) = \frac{4}{52}
$$

III. **Calculate $P(\text{Heart} \cap \text{Queen})$**:

- The queen of hearts is both a heart and a queen, so it is counted in both the "hearts" and "queens" categories. This is the overlap between the two events.
- The probability of drawing the queen of hearts is:

$$
P(\text{Heart} \cap \text{Queen}) = \frac{1}{52}
$$

IV. **Apply the Addition Rule**:

Now, we substitute the values into the addition rule formula:

$$
P(\text{Heart} \cup \text{Queen}) = P(\text{Heart}) + P(\text{Queen}) - P(\text{Heart} \cap \text{Queen})
$$

Plugging in the probabilities we calculated:

$$
P(\text{Heart} \cup \text{Queen}) = \frac{13}{52} + \frac{4}{52} - \frac{1}{52}
$$

Simplify the equation:

$$
P(\text{Heart} \cup \text{Queen}) = \frac{13 + 4 - 1}{52} = \frac{16}{52} = \frac{4}{13}
$$

Thus, the probability of drawing a card that is either a heart or a queen from a deck of 52 cards is $\frac{4}{13}$.

#### 2. Drawing an Ace or a Red Card

Consider a standard deck of 52 cards. In this example, we will calculate the probability of drawing a card that is either an **Ace** or a **Red card** (either a heart or a diamond) and demonstrate how the three axioms of probability apply.

- There are 4 Aces in a deck (one from each suit: hearts, diamonds, clubs, and spades).
- There are 26 Red cards (13 hearts and 13 diamonds).
- The **Ace of hearts** and the **Ace of diamonds** belong to both groups, so there is overlap between the events.

We will compute the probability of drawing either an Ace or a Red card:

$$
P(\text{Ace} \cup \text{Red})
$$

using the formula for the union of two events:

$$
P(A \cup B) = P(A) + P(B) - P(A \cap B)
$$

where:

- $P(A)$ is the probability of drawing an Ace,
- $P(B)$ is the probability of drawing a Red card,
- $P(A \cap B)$ is the probability of drawing a card that is both an Ace and a Red card.

#### Step-by-Step Breakdown:

I. **Calculate $P(\text{Ace})**

There are 4 Aces in the deck, so the probability of drawing an Ace is:

$$
P(\text{Ace}) = \frac{4}{52} = \frac{1}{13}
$$

This probability is non-negative, satisfying **Axiom 1 (Non-Negativity)**, which states that the probability of any event is always greater than or equal to 0:

$$
P(\text{Ace}) \geq 0
$$

II. **Calculate $P(\text{Red})$**

There are 26 Red cards (13 hearts and 13 diamonds) in the deck, so the probability of drawing a Red card is:

$$
P(\text{Red}) = \frac{26}{52} = \frac{1}{2}
$$

Again, this is a non-negative value, confirming **Axiom 1 (Non-Negativity)**.

III. **Calculate $P(\text{Ace} \cap \text{Red})$**

The Ace of hearts and the Ace of diamonds are both Aces and Red cards, so there are 2 cards in the overlap (Ace of hearts and Ace of diamonds). The probability of drawing one of these two cards is:

$$
P(\text{Ace} \cap \text{Red}) = \frac{2}{52} = \frac{1}{26}
$$

This probability satisfies **Axiom 1 (Non-Negativity)** as well because it is non-negative.

IV. **Apply the Addition Rule**

Now we apply the addition rule for probabilities of non-mutually exclusive events:

$$
P(\text{Ace} \cup \text{Red}) = P(\text{Ace}) + P(\text{Red}) - P(\text{Ace} \cap \text{Red})
$$

Substitute the values we calculated:

$$
P(\text{Ace} \cup \text{Red}) = \frac{1}{13} + \frac{1}{2} - \frac{1}{26}
$$

We need to express all terms with a common denominator. The least common denominator for 13, 2, and 26 is 52:

$$
P(\text{Ace}) = \frac{1}{13} = \frac{4}{52}, \quad P(\text{Red}) = \frac{1}{2} = \frac{26}{52}, \quad P(\text{Ace} \cap \text{Red}) = \frac{1}{26} = \frac{2}{52}
$$

Now, substituting into the formula:

$$
P(\text{Ace} \cup \text{Red}) = \frac{4}{52} + \frac{26}{52} - \frac{2}{52} = \frac{28}{52} = \frac{7}{13}
$$

Thus, the probability of drawing a card that is either an Ace or a Red card is $\frac{7}{13}$.
