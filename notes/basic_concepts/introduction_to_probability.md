# Introduction to Probability

Probability theory offers a structured approach to assessing the probability of events, allowing for logical and systematic reasoning about their likelihood.

## Terminology

* **Experiment**: A process that produces one of several possible outcomes, such as repeatedly tossing a die or coin.
* **Sample Space (S)**: The complete set of possible outcomes for an experiment. For example, when tossing a die, S = {1, 2, 3, 4, 5, 6}.
* **Event (E)**: A subset of the sample space, representing a specific occurrence. Examples include rolling a 5 or obtaining a sum of 7 from two dice rolls.
* **Probability of an Outcome (P(s))**: A numerical value assigned to each outcome in the sample space, satisfying two properties:
  * For each outcome s, 0 ≤ P(s) ≤ 1.
  * The sum of probabilities for all outcomes in the sample space equals 1: $\sum p(s) = 1$.
* **Probability of an Event (P(E))**: The sum of the probabilities of all outcomes within the event: 

$$P(E) = \sum_{s\in E} P(s)$$

* **Random Variable (V)**: A numerical function that allocates a value to each outcome in a probability space.
* **Expected Value of a Random Variable (E(V))**: The weighted average of the values of the random variable, calculated as 

$$E(V) = \sum_{s\in S} P(s) * V(s)$$

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
