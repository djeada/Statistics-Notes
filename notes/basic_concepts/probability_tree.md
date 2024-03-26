## Probability Trees

Probability trees are a visual representation of all possible outcomes of a probabilistic experiment and the paths leading to these outcomes. They are especially helpful in understanding sequences of events, particularly when these events are conditional on previous outcomes.

### Structure of Probability Trees

A probability tree starts with a root node that branches out into possible outcomes of the first event. Each of these outcomes becomes a node that branches into further outcomes, continuing for as many events as are being considered. The branches are labeled with probabilities, and the path to each outcome shows the sequence of events leading to that outcome.

### Rules for Probability Trees

1. The sum of the probabilities of all branches from a single node must equal 1, as they represent all possible outcomes of that event.
2. The probability of an event or sequence of events represented by a path is found by multiplying the probabilities along the path.
3. The probability of an event that can occur in multiple ways is the sum of the probabilities of all paths leading to that event.

### Example: Drawing Cards

Consider a simplified example where we draw one card from a standard deck of 52 cards, and we're interested in the event of drawing a heart or not drawing a heart.

```plaintext
Tree:
           __Heart (1/4)
          |
Initial ──┤
          |
          |__Not Heart (3/4)
```

Here's how to interpret this tree:

- The initial node represents the state before any card is drawn.
- From the initial node, there are two possible outcomes: drawing a heart or not drawing a heart.
- The probability of drawing a heart is calculated by the number of hearts in a deck (13) divided by the total number of cards (52), giving us $P(\text{Heart}) = \frac{13}{52} = \frac{1}{4}$.
- Conversely, the probability of not drawing a heart is $P(\text{Not Heart}) = \frac{39}{52} = \frac{3}{4}$.

### Example: Tossing a Coin and Rolling a Die

In this example, we combine two independent events: first, we toss a coin, and then we roll a die. The probability tree for this scenario illustrates the outcomes and probabilities for each stage of the experiment.

```plaintext
Tree:
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

Interpreting the Probability Tree:

I. **Initial Node**: The experiment starts with a coin toss. The initial node represents the state before this action.
II. **First Level Branches (Coin Toss)**:

- The first branching of the tree represents the two outcomes of tossing the coin: "Head" and "Tail."
- Each outcome of the coin toss has a probability of 1/2, as a fair coin has equal chances of landing on either side.
  
III. **Second Level Branches (Die Roll)**:

- After the coin toss, the next event is rolling a six-sided die.
- The second level of branches represents the outcomes of the die roll, which are the numbers 1 through 6.
- Each outcome of the die roll has a probability of 1/6, as each face of a fair die has an equal chance of appearing.

Calculating Probabilities:

- To calculate the probability of a combined event (like getting a "Head" followed by rolling a "4"), we multiply the probabilities along the path: $P(\text{Head}) \times P(4) = \frac{1}{2} \times \frac{1}{6}$.
- The tree can be used to compute the probabilities of all possible combinations of outcomes from the two events.

### Example: Rolling Two Dice

In this example, we consider the scenario of rolling two dice simultaneously. A probability tree can be used to visualize all the possible outcomes and their associated probabilities.

```plaintext
Tree:
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

Interpreting the Probability Tree:

I. **Initial Node**: Represents the state before any dice are rolled.
II. **First Level Branches (First Die Roll)**:

- Each branch from the initial node represents one of the six possible outcomes of rolling the first die (numbered 1 to 6).
- Each outcome has an equal probability of 1/6, reflecting the fairness of the die.

III. **Second Level Branches (Second Die Roll)**:

- For each outcome of the first die, there are branches representing the possible outcomes of rolling the second die.
- Like the first die, each possible outcome (numbered 1 to 6) of the second die has a probability of 1/6.

Calculating Probabilities:

- The probability of a specific combination (like rolling a 3 on the first die and a 5 on the second) is calculated by multiplying the probabilities along the path: For a "3" followed by a "5": $P(3 \text{ and } 5) = P(3) \times P(5) = \frac{1}{6} \times \frac{1}{6} = \frac{1}{36}$.
- The tree illustrates all 36 possible outcomes (6 outcomes from the first die multiplied by 6 outcomes from the second die), each with an equal probability of 1/36.

### Example: Drawing Marbles from a Bag

Consider a bag that contains 6 red marbles (R) and 4 green marbles (G). We draw two marbles from the bag one after the other without replacement. We are interested in calculating the probabilities of the following outcomes:

1. **P(R then G)**: Drawing a red marble followed by a green marble.
2. **P(G then R)**: Drawing a green marble followed by a red marble.
3. **P(both R)**: Drawing two red marbles.
4. **P(both G)**: Drawing two green marbles.

```plaintext
                      ┌── R (5/9)
               ┌── R (6/10)
               │      └── G (4/9)
Initial Node──┤
               │      ┌── R (6/9)
               └── G (4/10)
                      └── G (3/9)

```

Calculations:

I. **P(R then G)**: 

- The probability of drawing a red marble first is $\frac{6}{10}$ because there are 6 red marbles out of a total of 10.
- Given the first marble drawn is red, the probability of then drawing a green marble is $\frac{4}{9}$ since there are now 4 green marbles out of the remaining 9 marbles.
- Therefore, the probability of drawing a red marble followed by a green marble is $\frac{6}{10} \times \frac{4}{9} \approx 0.267$.

II. **P(G then R)**:

- The probability of drawing a green marble first is $\frac{4}{10}$.
- If the first marble is green, there are still 6 red marbles left out of 9.
- Thus, the probability of drawing a green marble followed by a red marble is $\frac{4}{10} \times \frac{6}{9} \approx 0.267$.

III. **P(both R)**:

- After drawing one red marble, there are 5 red marbles left out of 9.
- The probability of drawing two red marbles consecutively is $\frac{6}{10} \times \frac{5}{9} \approx 0.333$.

IV. **P(both G)**:

- After drawing one green marble, there are 3 green marbles left out of 9.
- The probability of drawing two green marbles consecutively is $\frac{4}{10} \times \frac{3}{9} \approx 0.133$.
