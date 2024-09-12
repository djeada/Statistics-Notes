# Introduction to Probability

Probability theory offers a structured approach to assessing the probability of events, allowing for logical and systematic reasoning about their likelihood.

## Introductory Terminology

- An **experiment** refers to any procedure that can be repeated indefinitely and has a clearly defined set of possible outcomes, known as the sample space. Examples include rolling dice, flipping coins, or drawing cards from a deck.
- The **sample space (S)** represents the complete set of possible outcomes of an experiment. It can be finite or infinite, and either discrete or continuous. For example, for a 6-sided die, the sample space is \( S = \{1, 2, 3, 4, 5, 6\} \). For a coin flip, the sample space is \( S = \{\text{heads}, \text{tails}\} \). If two coins are flipped simultaneously, the sample space expands to \( S = \{(\text{H}, \text{H}), (\text{H}, \text{T}), (\text{T}, \text{H}), (\text{T}, \text{T})\} \).
- An **event (E)** is any collection of outcomes drawn from the sample space \( S \), forming a subset of \( S \). An event can consist of a single outcome or multiple outcomes. For example, rolling an even number on a die corresponds to the event \( E = \{2, 4, 6\} \), getting tails when flipping a coin is \( E = \{\text{tails}\} \), and drawing a heart from a standard deck of cards is \( E = \{2\heartsuit, 3\heartsuit, \dots, A\heartsuit\} \).

### Example: Dice Rolling

When you roll a 6-sided (fair) die, the sample space is:

$$S = {1, 2, 3, 4, 5, 6}$$

And the possible events include:

* Odd Numbers = ${1, 3, 5}$
* Even Numbers = ${2, 4, 6}$
* Rolling at Least a 5 = ${5, 6}$
* Prime Numbers = ${2, 3, 5}$
* Rolling a Number Less Than 4 = ${1, 2, 3}$

Each event is a subset of the sample space and represents a particular outcome or set of outcomes that we are interested in observing. The probability of an event is a measure of how likely that event is to occur, calculated by dividing the number of favorable outcomes (the size of event set) by the total number of possible outcomes (the size of sample space).

### Additional Examples

- In **traffic observation**, counting the number of accidents at an intersection over a month defines the sample space as \( S = \{0, 1, 2, 3, \dots, n\} \), where \( n \) represents a reasonable upper limit based on historical data.
- The **life span of a light bulb** measured in hours has a sample space of any positive number, formally \( S = \{t \mid t > 0\} \). In practice, this could be limited to a range such as \( S = \{1, 2, 3, \dots, 10000\} \) hours.
- For an individual's **birth month**, the sample space is \( S = \{\text{January}, \text{February}, \dots, \text{December}\} \).
- In the case of **radioactive decay**, where decay occurs in intervals of 1 second, the sample space consists of sequences of decay (D) and non-decay (N), such as \( S = \{\text{D}, \text{ND}, \text{NND}, \text{NNND}, \dots\} \).
- When **rolling two dice**, the sample space for the sum of the points on the two dice is \( S = \{2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12\} \).
- In the **seating at a square table** scenario, if two people can sit at any of the four corners, the sample space for their seating positions can be represented as pairs of positions.

|   | 1   | 2   | 3   | 4   | 5   | 6   |
|---|-----|-----|-----|-----|-----|-----|
| 1 | (1,1)| (1,2)| (1,3)| (1,4)| (1,5)| (1,6)|
| 2 | (2,1)| (2,2)| (2,3)| (2,4)| (2,5)| (2,6)|
| 3 | (3,1)| (3,2)| (3,3)| (3,4)| (3,5)| (3,6)|
| 4 | (4,1)| (4,2)| (4,3)| (4,4)| (4,5)| (4,6)|
| 5 | (5,1)| (5,2)| (5,3)| (5,4)| (5,5)| (5,6)|
| 6 | (6,1)| (6,2)| (6,3)| (6,4)| (6,5)| (6,6)|

For instance, (1,1) means both are in the first corner, and (1,2) means the first is in the first corner and the second in the second corner.

## Probability

Probability is a measure that quantifies the likelihood of a specific event occurring, given a set of possible outcomes. It is a value between 0 and 1, where 0 indicates that the event is impossible, and 1 indicates that the event is certain. Mathematically, the probability of an event A, denoted as P(A), can be expressed as:

$$
P(A) = \frac{\text{Number of favorable outcomes}}{\text{Total number of possible outcomes}}
$$

* **Probability of an Outcome (P(s))**: The probability of a particular outcome s is a measure of the likelihood that this outcome will occur when the experiment is performed. It is a value between 0 (impossible event) and 1 (certain event), satisfying:
  * $0 \leq P(s) \leq 1$ for each outcome $s$.
  * The sum of the probabilities of all outcomes equals 1, or $\sum_{s \in S} P(s) = 1$, where $S$ is the sample space.

* **Probability of an Event (P(E))**: The probability of an event E is determined by adding up the probabilities of the outcomes that compose E. Mathematically, this is represented by the formula:

$$
P(E) = \sum_{s \in E} P(s)
$$

* A **random variable** X is a function that assigns a numerical value to each outcome in a sample space. For instance, X could represent the total number of points scored in a basketball game.
* The **expected value** of a random variable X gives a measure of the central tendency of the distribution of the random variable. It is computed as the weighted average of all possible values that the random variable can take on, with the weights being the probabilities of the values. The formula for the expected value is:

$$
E(X) = \sum_{s \in S} P(s) \cdot X(s)
$$

### Example: Full Calculation for Two Six-Sided Dice

Consider the random variable X which represents the sum of the numbers that come up when two fair six-sided dice are rolled. To calculate the expected value E(X), we must first enumerate the sample space and the associated probabilities.

The sample space S for the sum of two dice is:

$$S = {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}$$

Which is better represented using a table:

| - | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| 5 | 6 | 7 | 8 | 9 | 10 | 11 |
| 6 | 7 | 8 | 9 | 10 | 11 | 12 |

The probability of each sum, given that there are 36 possible combinations when rolling two dice, is:

$$P(2) = 1/36, P(3) = 2/36, P(4) = 3/36, ..., P(7) = 6/36, ..., P(12) = 1/36$$

Now, we calculate the expected value E(X) by multiplying each sum by its probability and adding all the products together:

$$E(X) = (1/36)*2 + (2/36)*3 + (3/36)*4 + ... + (6/36)*7 + ... + (1/36)*12$$

When you perform this calculation, you'll find that E(X) equals 7, which is the average sum of rolling two six-sided dice.

### Example: Cards

A standard deck of playing cards contains 52 cards, divided evenly into four suits: hearts, diamonds, clubs, and spades. Each suit has 13 cards consisting of numbers 2 through 10, a Jack, Queen, King, and Ace. If we draw a single card at random from a well-shuffled deck, we can calculate the probability of various events.

| Clubs     | Diamonds  | Hearts    | Spades    |
|-----------|-----------|-----------|-----------|
| 2♣        | 2♦        | 2♥        | 2♠        |
| 3♣        | 3♦        | 3♥        | 3♠        |
| 4♣        | 4♦        | 4♥        | 4♠        |
| 5♣        | 5♦        | 5♥        | 5♠        |
| 6♣        | 6♦        | 6♥        | 6♠        |
| 7♣        | 7♦        | 7♥        | 7♠        |
| 8♣        | 8♦        | 8♥        | 8♠        |
| 9♣        | 9♦        | 9♥        | 9♠        |
| 10♣       | 10♦       | 10♥       | 10♠       |
| J♣        | J♦        | J♥        | J♠        |
| Q♣        | Q♦        | Q♥        | Q♠        |
| K♣        | K♦        | K♥        | K♠        |
| A♣        | A♦        | A♥        | A♠        |


#### Probability of Drawing a Heart

The probability of drawing a card from any particular suit, like hearts, is given by the ratio of the number of cards in that suit to the total number of cards in the deck:

$$
P(\text{Heart}) = \frac{\text{Number of hearts}}{\text{Total number of cards}} = \frac{13}{52} = \frac{1}{4}
$$

This is because there are 13 hearts and 52 cards in total, so the probability is $\frac{13}{52}$, which simplifies to $\frac{1}{4}$ or 25%.

#### Probability of Drawing a Face Card

Face cards are the Jack, Queen, and King of each suit. There are 3 face cards per suit, and 4 suits, so there are 12 face cards in total.

$$
P(\text{Face Card}) = \frac{\text{Number of face cards}}{\text{Total number of cards}} = \frac{12}{52} = \frac{3}{13}
$$

#### Probability of Drawing an Ace

Since there are four Aces in a deck, one for each suit, the probability of drawing an Ace is:

$$
P(\text{Ace}) = \frac{\text{Number of Aces}}{\text{Total number of cards}} = \frac{4}{52} = \frac{1}{13}
$$

#### Probability of Drawing a Card Lower than 5

Cards lower than 5 will be the numbers 2, 3, and 4 from each suit. Since there are 4 suits, this gives us 12 cards.

$$
P(\text{Card} < 5) = \frac{\text{Number of cards lower than 5}}{\text{Total number of cards}} = \frac{12}{52} = \frac{3}{13}
$$

#### Expected Value of Card Numbers
If we assign numerical values to each card (Jack = 11, Queen = 12, King = 13, Ace = 1), we can calculate the expected value for the number on a card drawn at random from the deck. We'll denote this random variable as $X$.

$$
E(X) = \sum_{i=1}^{13} P(i) \cdot i
$$

Where $P(i)$ is the probability of drawing a card with number $i$, which is $\frac{1}{13}$ for each card number since there is an equal number of each card number in the deck.

These probabilities and expected values provide the fundamental basis for a wide range of card games and can be used to calculate more complex odds based on game rules and strategies.

### Example: Distinguishable Balls in Cells

Consider an experiment where r = 3 distinguishable balls, labeled a, b, and c, are to be placed in n = 3 cells. We'll enumerate the elementary events and then calculate the probabilities of several interesting events related to this setup.

Elementary events are unique arrangements of the balls in the cells. Since the balls are distinguishable, each different arrangement counts as a separate event.

| Index | Cell 1 | Cell 2 | Cell 3 |
|-------|--------|--------|--------|
| 1     | abc    |        |        |
| 2     |        | abc    |        |
| 3     |        |        | abc    |
| 4     | ab     | c      |        |
| 5     | ac     | b      |        |
| 6     | bc     | a      |        |
| 7     | ab     |        | c      |
| 8     | ac     |        | b      |
| 9     | bc     |        | a      |
| 10    | c      | ab     |        |
| 11    | b      | ac     |        |
| 12    | a      | bc     |        |
| 13    |        | ab     | c      |
| 14    |        | ac     | b      |
| 15    |        | bc     | a      |
| 16    | c      |        | ab     |
| 17    | b      |        | ac     |
| 18    | a      |        | bc     |
| 19    |        | c      | ab     |
| 20    |        | b      | ac     |
| 21    |        | a      | bc     |
| 22    | a      | b      | c      |
| 23    | a      | c      | b      |
| 24    | b      | a      | c      |
| 25    | b      | c      | a      |
| 26    | c      | a      | b      |
| 27    | c      | b      | a      |

We can define several events based on these arrangements:

- The **event A**, "At least two balls are in one cell," includes any arrangement where a single cell contains two or three balls.
- For **event B**, "The first cell is not empty," this event includes any arrangement where the first cell contains at least one ball.
- The **event C**, "Both A and B occur," refers to the intersection of events A and B, meaning that both the first cell is not empty and at least one cell contains two or more balls.
- In the **event D**, "Either A or B occurs," this event represents the union of events A and B, meaning that either the first cell is not empty, or at least two balls are in one cell, or both.

#### Probability Calculations

With 27 possible outcomes, each equally likely, the probabilities of the events are:

$$
P(A) = \frac{\text{Number of favorable outcomes for A}}{\text{Total outcomes}} = \frac{21}{27}
$$

$$
P(B) = \frac{\text{Number of favorable outcomes for B}}{\text{Total outcomes}} = \frac{19}{27}
$$

$$
P(C) = \frac{\text{Number of favorable outcomes for C}}{\text{Total outcomes}} = \frac{12}{27}
$$

$$
P(D) = \frac{\text{Number of favorable outcomes for D}}{\text{Total outcomes}} = \frac{27}{27} = 1
$$

These probabilities can be simplified:

$$
P(A) = \frac{7}{9}, P(B) = \frac{19}{27}, P(C) = \frac{4}{9}, P(D) = 1
$$

### Example: Indistinguishable Balls

In this scenario, we consider the placement of r = 3 indistinguishable balls into n = 3 cells. Since the balls are indistinguishable, the order in which they are placed does not matter, which reduces the number of elementary events compared to the case with distinguishable balls.

The elementary events are represented by the arrangements of the balls across the cells as follows:

| Index | Cell 1 | Cell 2 | Cell 3 |
|-------|--------|--------|--------|
| 1     | ooo    |        |        |
| 2     |        | ooo    |        |
| 3     |        |        | ooo    |
| 4     | oo     | o      |        |
| 5     | oo     |        | o      |
| 6     | o      | oo     |        |
| 7     |        | oo     | o      |
| 8     | o      |        | oo     |
| 9     |        | o      | oo     |
| 10    | o      | o      | o      |

Events of Interest:

- The **event A**, "At least two balls are in one cell," includes all arrangements where any cell contains two or more balls. This covers situations where a single cell has either two or three balls.
- For **event B**, "The first cell is not empty," the event consists of all arrangements where the first cell contains at least one ball. This means the first cell cannot be empty in any valid outcome.

#### Probability Calculations

With 10 unique outcomes and each outcome equally likely, the probabilities are:

$$
P(A) = \frac{\text{Number of favorable outcomes for A}}{\text{Total unique outcomes}} = \frac{9}{10}
$$

$$
P(B) = \frac{\text{Number of favorable outcomes for B}}{\text{Total unique outcomes}} = \frac{6}{10} = \frac{3}{5}
$$
