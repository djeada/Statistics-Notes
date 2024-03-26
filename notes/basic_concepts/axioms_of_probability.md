## Axioms of Probability

Probability theory is based on a set of principles, or axioms, that define the properties of the probability measure. These axioms, first formalized by the Russian mathematician Andrey Kolmogorov, are the foundation upon which the entire framework of probability is built.

### The Three Axioms

1. **Non-negativity**: This axiom states that the probability of any event A is a non-negative number. This reflects the idea that an event either happens or it doesn't, and thus, the probability cannot be negative.

$$
P(A) \geq 0
$$

2. **Unit Measure**: This axiom ensures that the probability of the sample space S, which includes all possible outcomes of an experiment, is always equal to 1. This is equivalent to saying that it's certain at least one of the possible outcomes will occur.

$$
 P(S) = 1
$$

3. **Additivity**: The axiom of additivity is about disjoint events, also known as mutually exclusive events. If events A and B cannot both occur at the same time, the probability of either event A or event B occurring is the sum of their individual probabilities.

$$
P(A \cup B) = P(A) + P(B) \ \text{if} \ A \cap B = \emptyset
$$

### Example: Dice Roll

Let's analyze the probabilities for certain outcomes when rolling a fair six-sided die:

#### P(5 or 6)

- These are mutually exclusive events. 
- $P(5) = 1/6, P(6) = 1/6$, and there's no overlap.
- $P(5 \ or \ 6) = P(5) + P(6) = 1/6 + 1/6 = 2/6 = 1/3$

#### P(even or odd)

- Every number is either even or odd, not both, and all numbers are either even or odd.
- Since the sample space is fully covered by even and odd numbers,
- $P(even \ or \ odd) = P(S) = 1$

#### P(even or 3)

- The events "even" and "3" are mutually exclusive because 3 is not even.
- There are 3 even numbers in a die roll (2, 4, 6), so
- $P(even) = 3/6 = 1/2$.
- $P(3) = 1/6$.
- $P(even \ or \ 3) = P(even) + P(3) = 1/2 + 1/6 = 3/6 + 1/6 = 4/6 = 2/3$

#### P(even or 4)

- These events are not mutually exclusive since 4 is an even number.
- $P(even) = 3/6 = 1/2$ as before.
- $P(4) = 1/6$, but we should not count it separately as it's included in the even count.
- $P(4 \ and \ even) = P(4) = 1/6$ (since 4 is the only even number that is also specifically the number 4).
- $P(even \ or \ 4) = P(even) + P(4) - P(4 \ and \ even) = 1/2 + 1/6 - 1/6 = 1/2$

### Example: Deck of Cards

When calculating probabilities with a standard deck of 52 cards, consider the following scenario:

- We want to find the probability of drawing a card that is either a heart or a queen.
- There are 13 hearts in a deck and 4 queens, but the queen of hearts is counted in both groups.

The probability is calculated as:

$$
P(\text{Heart} \cup \text{Queen}) = P(\text{Heart}) + P(\text{Queen}) - P(\text{Heart} \cap \text{Queen})
$$

Breaking it down:

- P(Heart) = 13/52 (since there are 13 hearts)
- P(Queen) = 4/52 (as there are 4 queens)
- P(Heart ∩ Queen) = 1/52 (the queen of hearts is the overlap)

Substituting these values gives us:

$$
P(\text{Heart} \cup \text{Queen}) = \frac{13}{52} + \frac{4}{52} - \frac{1}{52} = \frac{16}{52} = \frac{4}{13}
$$
