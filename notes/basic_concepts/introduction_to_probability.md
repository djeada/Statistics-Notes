# Introduction to Probability

Probability theory offers a structured approach to assessing the probability of events, allowing for logical and systematic reasoning about their likelihood.
## Terminology

* **Experiment**: A process that produces one of several possible outcomes, such as repeatedly tossing a die or coin, or observing the number of accidents at an intersection in a month.
* **Sample Space (S)**: The complete set of possible outcomes for an experiment. For example, when tossing a die, S = {1, 2, 3, 4, 5, 6}. In a single coin flip, S = {"heads", "tails"}. When tossing two coins, S = {(H,H), (H,T), (T,H), (T,T)}.
* **Event (E)**: A subset of the sample space, representing a specific occurrence. Examples include rolling a 5, obtaining a sum of 7 from two dice rolls, or two people sitting in a corner of a square table.
* **Probability of an Outcome (P(s))**: A numerical value assigned to each outcome in the sample space, satisfying two properties:
  * For each outcome s, 0 ≤ P(s) ≤ 1.
  * The sum of probabilities for all outcomes in the sample space equals 1: $\sum p(s) = 1$.
* **Probability of an Event (P(E))**: The sum of the probabilities of all outcomes within the event:

$$P(E) = \sum_{s\in E} P(s)$$

* **Random Variable (V)**: A numerical function that allocates a value to each outcome in a probability space. Examples include the number of points obtained by rolling two dice or the life span of a light bulb.
* **Expected Value of a Random Variable (E(V))**: The weighted average of the values of the random variable, calculated as 

$$E(V) = \sum_{s\in S} P(s) * V(s)$$

## Examples

* Number of accidents at an intersection in a month: S = {1, 2, 3, ...} or S = {1, 2, 3, ..., 1000}.
* Life span of a light bulb: elementary events are any positive numbers, t > 0, and the space is infinite; but in a specific problem, it may be better to choose S = {1, 2, 3, ...} hours/days/months.
* Birth month: S = {Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec}.
* A radioactive nucleus can decay (D) or not (N) in successive intervals of 1 second. The space of elementary events is infinite: D, ND, NND, NNND, ...
* Rolling two dice: S = {x, y}, where x = 1,...,6 and y = 1,...,6.
* Sum of points obtained by rolling two dice: S = {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}.
* Two people at a square table - we are interested in event A: "they sit in a corner". Examples of different choices of the space of elementary events (each cell represents a possible outcome):

|   | 1   | 2   | 3   | 4   | 5   | 6   |
|---|-----|-----|-----|-----|-----|-----|
| 1 | (1,1)| (1,2)| (1,3)| (1,4)| (1,5)| (1,6)|
| 2 | (2,1)| (2,2)| (2,3)| (2,4)| (2,5)| (2,6)|
| 3 | (3,1)| (3,2)| (3,3)| (3,4)| (3,5)| (3,6)|
| 4 | (4,1)| (4,2)| (4,3)| (4,4)| (4,5)| (4,6)|
| 5 | (5,1)| (5,2)| (5,3)| (5,4)| (5,5)| (5,6)|
| 6 | (6,1)| (6,2)| (6,3)| (6,4)| (6,5)| (6,6)|

In this table, each pair of numbers represents the position of the two people at the table. For example, (1,1) means both are sitting in the first corner, (1,2) means the first person is in the first corner and the second person is in the second corner, and so on. The event "they sit in a corner" corresponds to the outcomes (1,1), (2,2), (3,3), and (4,4).

## Definition of Probability

Probability is a measure that quantifies the likelihood of a specific event occurring, given a set of possible outcomes. It is a value between 0 and 1, where 0 indicates that the event is impossible, and 1 indicates that the event is certain. Mathematically, the probability of an event A, denoted as P(A), can be expressed as:

$$
P(A) = \frac{\text{Number of favorable outcomes}}{\text{Total number of possible outcomes}}
$$

### Example with Cards

In a standard deck of 52 playing cards, there are 4 suits (hearts, diamonds, clubs, and spades) with 13 cards in each suit. If we draw one card at random, we can calculate the probability of drawing a heart:

$$
P(\text{Heart}) = \frac{\text{Number of hearts}}{\text{Total number of cards}} = \frac{13}{52} = \frac{1}{4}
$$

### Distinguishable Balls

Placing r = 3 distinguishable balls (a, b, c) in n = 3 cells:

Elementary events (each row represents a possible outcome):

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

* Event A: "at least two balls are in one cell" - elementary events 1-21
* Event B: "the first cell is not empty" - elementary events 1, 4-12, 16-18, 22-27
* Event C: "both A and B occur" - elementary events 1, 4-12, 16-18
* Event D: "either A or B occurs" - elementary events 1-27

Let's calculate probabilities for these events (assuming each outcome is equally likely):
There are $3^3 = 27$ possible outcomes in total.

$$P(A) = \frac{\text{Number of outcomes in A}}{\text{Total outcomes}} = 21 / 27$$

$$P(B) = \frac{\text{Number of outcomes in B}}{\text{Total outcomes}} = 19 / 27$$

$$P(C) = \frac{\text{Number of outcomes in C}}{\text{Total outcomes}} = 12 / 27$$

$$P(D) = \frac{\text{Number of outcomes in D}}{\text{Total outcomes}} = 27 / 27$$

### Indistinguishable Balls

Placing r = 3 indistinguishable balls in n = 3 cells:

Elementary events (each row represents a possible outcome):

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

* Event A: "at least two balls are in one cell" - elementary events 1-9
* Event B: "the first cell is not empty" - elementary events 1, 4-6, 8, 10

Let's calculate probabilities for these events (assuming each outcome is equally likely):
There are 10 unique outcomes in total.

$$P(A) = \frac{\text{Number of outcomes in A}}{\text{Total unique outcomes}} = 9 / 10$$

$$P(B) = \frac{\text{Number of outcomes in B}}{\text{Total unique outcomes}} = 6 / 10$$

## Geometric Probability

Example:

The elementary event space is defined by the set of points (x, y) in the plane and fills the interior of the square [0 ≤ x ≤ 1; 0 ≤ y ≤ 1]. Find the probability that any point inside the square is at a distance less than r from a chosen corner of the square.

The sought probability is expressed as the ratio of the area of the common part of the circle with radius r and the square to the area of the square (equal to 1):

For r < 1:

$$
P(r) = \int_{0}^{r} \sqrt{r^2 - x^2} dx =$$

$$
\frac{1}{2} (x \sqrt{r^2-x^2}+r^2\arcsin\frac{x}{r}) |^r_0= \frac{\pi r^2}{4}
$$

For r > 1:

$$
P(r) = \int_{0}^{r} \sqrt{r^2 - x^2} dx - 2 \int_{1}^{r} \sqrt{r^2 - x^2} dx = $$

$$
\frac{\pi r^2}{4} - 2(\frac{\pi r^2}{4} - \frac{1}{2}\sqrt{r^2-1}- \frac{1}{2}r^2\arcsin\frac{1}{r}) = $$

$$\sqrt{r^2-1} + r^2\arcsin\frac{1}{r} - \frac{\pi r^2}{4}
$$

As can be seen, for $r = \sqrt{2}$, the probability reaches a value equal to 1.

## Applications and Importance

Probability has a wide range of applications in various fields, including but not limited to:

1. **Statistics**: Estimating population parameters and making inferences about populations based on sample data.
2. **Finance**: Assessing the risk and return of investments, portfolio optimization, and option pricing.
3. **Gambling**: Determining the odds of winning and creating strategies for games of chance.
4. **Machine Learning**: Making predictions and classification based on historical data.
5. **Weather Forecasting**: Predicting the likelihood of certain weather conditions.
6. **Medicine**: Estimating the effectiveness of treatments and conducting clinical trials.

Understanding probability is essential for making informed decisions in uncertain situations and for modeling complex systems.

## Axioms of Probability

The three fundamental axioms of probability are:

1. **Non-negativity**: The probability of an event A is always non-negative.

$$
P(A) \geq 0
$$

2. **Unit Measure**: The probability of the sample space S (the set of all possible outcomes) is 1.

$$
P(S) = 1
$$

3. **Additivity**: If events A and B are mutually exclusive (i.e., they cannot occur simultaneously), then the probability of either A or B occurring is the sum of their individual probabilities.

$$
P(A \cup B) = P(A) + P(B) \quad \text{if} \quad A \cap B = \emptyset
$$

### Example with Cards

Let's calculate the probability of drawing either a heart or a queen from a standard deck of 52 cards. There are 13 hearts and 4 queens in the deck, but one card is both a heart and a queen (the queen of hearts). Since the events are not mutually exclusive, we need to account for the overlap:

$$
P(\text{Heart} \cup \text{Queen}) = P(\text{Heart}) + P(\text{Queen}) - P(\text{Heart} \cap \text{Queen}) = \frac{13}{52} + \frac{4}{52} - \frac{1}{52} = \frac{16}{52}
$$

These axioms provide the foundation for the theory of probability and enable us to derive other rules and properties.
