# Axioms of Probability

Probability theory is built on a small set of principles, called axioms, that define how probability measures behave. These axioms, formalized by the Russian mathematician Andrey Kolmogorov, provide the foundation for the rules used throughout probability theory.

### The Three Axioms

I. Non-negativity states that the probability of any event $A$ cannot be negative:

$$
P(A) \geq 0
$$

Probabilities represent the likelihood of events, so their values must always be non-negative.

II. Unit Measure states that the probability of the entire sample space $S$, which contains all possible outcomes of an experiment, is equal to 1:

$$
P(S) = 1
$$

In other words, some outcome from the sample space must occur.

III. Additivity applies to disjoint, or mutually exclusive, events. More precisely, if $A_1, A_2, \ldots$ are pairwise disjoint events, then:

$$
P\left(\bigcup_{i=1}^{\infty} A_i\right) = \sum_{i=1}^{\infty} P(A_i)
$$

For two mutually exclusive events $A$ and $B$, this gives the familiar rule:

$$
P(A \cup B) = P(A) + P(B)
\quad \text{if} \quad
A \cap B = \emptyset
$$

These axioms are the starting point from which many other probability rules can be derived. The following examples show how they work in simple settings.

### Example: Probabilities of Events in a Dice Roll

Consider a fair six-sided die. The sample space for a single roll is:

$$
S = \{1, 2, 3, 4, 5, 6\}
$$

Because the die is fair, each outcome is equally likely:

$$
P(\text{any specific number}) = \frac{1}{6}
$$

#### 1. Probability of Rolling a 5 or 6

The events "rolling a 5" and "rolling a 6" are mutually exclusive because they cannot occur on the same roll.

Therefore, we can use the addition rule for mutually exclusive events:

$$
P(5 \text{ or } 6) = P(5) + P(6)
$$

Since:

$$
P(5) = \frac{1}{6}, \quad P(6) = \frac{1}{6}
$$

we get:

$$
P(5 \text{ or } 6) = \frac{1}{6} + \frac{1}{6} = \frac{2}{6} = \frac{1}{3}
$$

So, the probability of rolling either a 5 or a 6 is $\frac{1}{3}$.

#### 2. Probability of Rolling an Even or Odd Number

Every possible outcome is either even or odd, and no outcome can be both. The two events are therefore mutually exclusive, and together they cover the entire sample space $S$.

The even outcomes are:

$$
\{2, 4, 6\}
$$

and the odd outcomes are:

$$
\{1, 3, 5\}
$$

Because their union is the entire sample space:

$$
P(\text{even} \text{ or } \text{odd}) = P(S) = 1
$$

This matches the intuitive result: every roll must produce either an even or an odd number.

#### 3. Probability of Rolling an Even Number or a 3

The events "rolling an even number" and "rolling a 3" are mutually exclusive because 3 is not even.

The even outcomes are $\{2,4,6\}$, so:

$$
P(\text{even}) = \frac{3}{6} = \frac{1}{2}
$$

The probability of rolling a 3 is:

$$
P(3) = \frac{1}{6}
$$

Since the events are mutually exclusive, their probabilities can be added:

$$
P(\text{even} \text{ or } 3) = P(\text{even}) + P(3) = \frac{1}{2} + \frac{1}{6}
$$

Using a common denominator:

$$
\frac{1}{2} = \frac{3}{6}
$$

Therefore:

$$
P(\text{even} \text{ or } 3) = \frac{3}{6} + \frac{1}{6} = \frac{4}{6} = \frac{2}{3}
$$

So, the probability of rolling either an even number or a 3 is $\frac{2}{3}$.

#### 4. Probability of Rolling an Even Number or a 4

In this case, the events "rolling an even number" and "rolling a 4" are not mutually exclusive because 4 is already one of the even outcomes. Simply adding the two probabilities would count the outcome 4 twice.

First, the probability of rolling an even number is:

$$
P(\text{even}) = \frac{3}{6} = \frac{1}{2}
$$

The probability of rolling a 4 is:

$$
P(4) = \frac{1}{6}
$$

Because rolling a 4 belongs to both events, their overlap is:

$$
P(\text{even} \text{ and } 4) = P(4) = \frac{1}{6}
$$

For events that are not mutually exclusive, we use the general addition rule:

$$
P(A \cup B) = P(A) + P(B) - P(A \cap B)
$$

Applying it here:

$$
P(\text{even} \text{ or } 4) = P(\text{even}) + P(4) - P(\text{even} \text{ and } 4)
$$

Substituting the values:

$$
P(\text{even} \text{ or } 4) = \frac{1}{2} + \frac{1}{6} - \frac{1}{6}
$$

Therefore:

$$
P(\text{even} \text{ or } 4) = \frac{1}{2} = \frac{3}{6}
$$

This also makes sense directly: because every 4 is already an even number, the event "even or 4" is simply the event "even. "

Thus, the probability is $\frac{1}{2}$.

### Example: Deck of Cards

The same ideas apply to events in a standard deck of 52 playing cards. These examples also illustrate why overlapping events require us to subtract the intersection when calculating a union.

#### 1. Probability of Drawing a Heart or a Queen

Consider a standard deck of 52 playing cards. It contains:

* 13 hearts,
* 4 queens, one from each suit,
* 1 queen of hearts, which belongs to both groups.

We want to calculate the probability of drawing a card that is either a heart or a queen.

These events are not mutually exclusive because the queen of hearts belongs to both categories. We therefore use the general addition rule:

$$
P(\text{Heart} \cup \text{Queen}) = P(\text{Heart})
+
P(\text{Queen})
-
P(\text{Heart} \cap \text{Queen})
$$

where:

* $P(\text{Heart})$ is the probability of drawing a heart,
* $P(\text{Queen})$ is the probability of drawing a queen,
* $P(\text{Heart} \cap \text{Queen})$ is the probability of drawing the queen of hearts.

Step-by-Step Breakdown:

I. Calculate $P(\text{Heart})$

There are 13 hearts in a 52-card deck, so:

$$
P(\text{Heart}) = \frac{13}{52}
$$

II. Calculate $P(\text{Queen})$

There are 4 queens in the deck, so:

$$
P(\text{Queen}) = \frac{4}{52}
$$

III. Calculate $P(\text{Heart} \cap \text{Queen})$

Only the queen of hearts is both a heart and a queen. Therefore:

$$
P(\text{Heart} \cap \text{Queen}) = \frac{1}{52}
$$

IV. Apply the Addition Rule

Substitute the values into the formula:

$$
P(\text{Heart} \cup \text{Queen}) = \frac{13}{52}
+
\frac{4}{52}
-
\frac{1}{52}
$$

Simplifying:

$$
P(\text{Heart} \cup \text{Queen}) = \frac{13 + 4 - 1}{52} = \frac{16}{52} = \frac{4}{13}
$$

Thus, the probability of drawing either a heart or a queen is $\frac{4}{13}$.

#### 2. Drawing an Ace or a Red Card

Consider a standard deck of 52 cards. We will calculate the probability of drawing a card that is either an Ace or a red card.

There are:

* 4 Aces, one from each suit,
* 26 red cards: 13 hearts and 13 diamonds,
* 2 red Aces: the Ace of hearts and the Ace of diamonds.

Because the two red Aces belong to both groups, the events overlap.

We want to calculate:

$$
P(\text{Ace} \cup \text{Red})
$$

Using the general addition rule:

$$
P(A \cup B) = P(A) + P(B) - P(A \cap B)
$$

where:

* $P(A)$ is the probability of drawing an Ace,
* $P(B)$ is the probability of drawing a red card,
* $P(A \cap B)$ is the probability of drawing a card that is both an Ace and red.

Step-by-Step Breakdown:

I. Calculate $P(\text{Ace})$

There are 4 Aces in the deck, so:

$$
P(\text{Ace}) = \frac{4}{52} = \frac{1}{13}
$$

This is non-negative, as required by the non-negativity axiom.

II. Calculate $P(\text{Red})$

There are 26 red cards in the deck, so:

$$
P(\text{Red}) = \frac{26}{52} = \frac{1}{2}
$$

Again, the probability is non-negative.

III. Calculate $P(\text{Ace} \cap \text{Red})$

The Ace of hearts and the Ace of diamonds are both red Aces, so there are 2 cards in the intersection:

$$
P(\text{Ace} \cap \text{Red}) = \frac{2}{52} = \frac{1}{26}
$$

IV. Apply the Addition Rule

Now apply the general addition rule:

$$
P(\text{Ace} \cup \text{Red}) = 
P(\text{Ace}) + P(\text{Red}) - P(\text{Ace} \cap \text{Red})
$$

Substituting the values:

$$
P(\text{Ace} \cup \text{Red}) = 
\frac{1}{13} + \frac{1}{2} - \frac{1}{26}
$$

Using a common denominator of 52:

$$
P(\text{Ace}) = \frac{4}{52},
\quad
P(\text{Red}) = \frac{26}{52},
\quad
P(\text{Ace} \cap \text{Red}) = \frac{2}{52}
$$

Therefore:

$$
P(\text{Ace} \cup \text{Red}) = 
\frac{4}{52} + \frac{26}{52} - \frac{2}{52} = 
\frac{28}{52} = \frac{7}{13}
$$

Thus, the probability of drawing either an Ace or a red card is $\frac{7}{13}$.
