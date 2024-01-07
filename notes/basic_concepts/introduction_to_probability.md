# Introduction to Probability

Probability theory offers a structured approach to assessing the probability of events, allowing for logical and systematic reasoning about their likelihood.

## Introductory Terminology

* **Experiment**: This is any procedure that can be infinitely repeated and has a well-defined set of outcomes, known as the sample space. Common examples include rolling dice, flipping coins, or drawing cards from a deck.

* **Sample Space (S)**: The set of all possible outcomes of an experiment. This can be finite or infinite, discrete or continuous. For a 6-sided die, the sample space is S = {1, 2, 3, 4, 5, 6}. For the flip of a coin, S = {"heads", "tails"}. If flipping two coins simultaneously, the sample space expands to S = {(H, H), (H, T), (T, H), (T, T)}.

* **Event (E)**: Any collection of outcomes from the sample space (S), which forms a subset of S. An event can consist of one outcome or multiple outcomes. Examples of events include rolling an even number on a die (E = {2, 4, 6}), getting tails when flipping a coin (E = {"tails"}), or drawing a heart from a standard deck of cards (E = {2♥, 3♥, ..., A♥}).

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

* **Traffic Observation**: Counting the number of accidents at an intersection in a month. The sample space might be S = {0, 1, 2, 3, ..., n}, where n is a reasonable upper limit based on historical data.

* **Life Span of a Light Bulb**: If measuring in hours, the sample space could be any positive number (S = {t | t > 0}). In a practical scenario, it might be limited to a certain range like S = {1, 2, 3, ..., 10000} hours.

* **Birth Month**: For an individual's birth month, the sample space is S = {January, February, ..., December}.

* **Radioactive Decay**: For a radioactive nucleus decaying in intervals of 1 second, the sample space is all sequences of decay (D) and non-decay (N) over time, like S = {D, ND, NND, NNND, ...}.

* **Rolling Two Dice**: The sample space for the sum of points is S = {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}.

* **Seating at a Square Table**: If two people can sit at any of the four corners of a square table, the sample space for their seating positions can be represented as pairs of positions (1 through 4). 

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

* **Random Variable (X)**: A random variable X is a function that assigns a numerical value to each outcome in a sample space. For instance, X could represent the total number of points scored in a basketball game.

* **Expected Value of a Random Variable (E(X))**: The expected value of a random variable X gives a measure of the central tendency of the distribution of the random variable. It is computed as the weighted average of all possible values that the random variable can take on, with the weights being the probabilities of the values. The formula for the expected value is:

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

* **Event A**: "At least two balls are in one cell." This event includes any arrangement where one cell contains two or three balls.
* **Event B**: "The first cell is not empty." This includes any arrangement where cell 1 contains at least one ball.
* **Event C**: "Both A and B occur." This is the intersection of events A and B.
* **Event D**: "Either A or B occurs." This is the union of events A and B.

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

* **Event A**: "At least two balls are in one cell." This event includes arrangements where any cell has two or three balls.
* **Event B**: "The first cell is not empty." This event includes arrangements where there is at least one ball in the first cell.

#### Probability Calculations

With 10 unique outcomes and each outcome equally likely, the probabilities are:

$$
P(A) = \frac{\text{Number of favorable outcomes for A}}{\text{Total unique outcomes}} = \frac{9}{10}
$$

$$
P(B) = \frac{\text{Number of favorable outcomes for B}}{\text{Total unique outcomes}} = \frac{6}{10} = \frac{3}{5}
$$
