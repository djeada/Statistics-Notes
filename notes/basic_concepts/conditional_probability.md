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

Here, $P(A|B)$ is the conditional probability of event A given that event B has occurred. It represents the probability of A under the condition that B is known to have occurred.

### Example: Deck of Cards

When analyzing probabilities with a deck of 52 playing cards, consider the following scenarios:

#### Probability of Drawing Two Diamonds Consecutively
- The probability of drawing a diamond as the first card is 13 out of the total 52 cards.
- Once a diamond is drawn, for the second draw, there are only 12 diamonds left and 51 cards remaining in the deck.

So, the probability of drawing a diamond as the second card given that the first was a diamond is:

$$ P(\text{second card Diamond | first card Diamond}) = \frac{12}{51} $$

Using the multiplication rule, the joint probability of both events is:

$$ P(\text{first card Diamond} \cap \text{second card Diamond}) = P(\text{first card Diamond}) \times P(\text{second card Diamond | first card Diamond}) = \frac{13}{52} \times \frac{12}{51} \approx 0.0588 $$

#### Probability of Drawing an Ace Followed by a King
- The probability of drawing an Ace first is 4 out of 52.
- If an Ace has been drawn, there are 4 Kings left in the remaining 51 cards, so the probability of drawing a King next is:

$$ P(\text{second card King | first card Ace}) = \frac{4}{51} $$

Applying the multiplication rule here gives us:

$$ P(\text{first card Ace} \cap \text{second card King}) = P(\text{first card Ace}) \times P(\text{second card King | first card Ace}) = \frac{4}{52} \times \frac{4}{51} \approx 0.0060 $$

## Independence of Events

The concept of independence in probability theory refers to a scenario where the occurrence of one event has no effect on the probability of another event. Formally, two events A and B are considered independent if and only if:

$$
P(A|B) = P(A) \quad \text{and} \quad P(B|A) = P(B)
$$

This means that the probability of A occurring given that B has occurred is the same as the probability of A occurring without any knowledge of B, and vice versa.

### Example: Card Drawing

When dealing with a deck of 52 playing cards, consider these two events:

- Drawing a king on the first draw.
- Drawing a king on the second draw without replacement.

The events are not independent because the outcome of the first draw affects the probability of the second. Specifically, if you draw a king on the first draw, the probability of drawing a king on the second draw is no longer $\frac{4}{52}$, but $\frac{3}{51}$ since one king has been removed from the deck and only 51 cards remain.

### Example: Divisibility within a Set of Integers

Let's define two events based on the set of integers from 1 to 100:

- Event A: The number is divisible by 3.
- Event B: The number is divisible by 7.

The probabilities are calculated as follows:

- $P(A) = \frac{33}{100}$ because there are 33 multiples of 3 between 1 and 100.
- $P(B) = \frac{14}{100}$ since there are 14 multiples of 7 in that range.
- $P(A \cap B) = \frac{4}{100}$, as there are 4 numbers that are multiples of both 3 and 7.

To check for independence, we compare $P(A) \cdot P(B)$ with $P(A \cap B)$:

- $P(A) \cdot P(B) = \frac{33}{100} \times \frac{14}{100}$
- $P(A \cdot B) \neq P(A \cap B)$, thus A and B are not independent.

However, if we extend our set to include numbers 101 to 105, the situation changes:

- $P(A) = \frac{35}{105}$ because 35 of the numbers from 1 to 105 are divisible by 3.
- $P(B) = \frac{15}{105}$ as there are 15 multiples of 7.
- $P(A \cap B) = \frac{5}{105}$, since 5 numbers are divisible by both 3 and 7 within the new set.

Here, $P(A) \cdot P(B) = \frac{35}{105} \times \frac{15}{105}$ does equal $P(A \cap B)$, making events A and B independent with the extended set.

### Example: Probability of At Least One of n Independent Events Occurring

When considering the probability of at least one of multiple independent events occurring, it's often easier to use the complementary rule rather than the addition rule directly, especially when the events are independent. This is because the inclusion-exclusion principle (used in the addition rule) becomes increasingly cumbersome as the number of events grows.

#### For Three Independent Events

Let's take three independent events A, B, and C. The probability that at least one of these events occurs can be expressed through the complementary probability—the probability that none of the events occur:

$$
P(A \cup B \cup C) = 1 - P(A^c \cap B^c \cap C^c)
$$

Since the events are independent, the probability that none of the events occur is the product of the probabilities that each individual event does not occur:

$$
P(A^c \cap B^c \cap C^c) = P(A^c) \times P(B^c) \times P(C^c)
$$

#### For n Independent Events

This extends naturally to any number n of independent events. If $A_1, A_2, \ldots, A_n$ are independent events, the probability that at least one occurs is:

$$
P(A_1 \cup A_2 \cup \cdots \cup A_n) = 1 - P(A_1^c) \times P(A_2^c) \times \cdots \times P(A_n^c)
$$

Here, $A_i^c$ represents the complement of event $A_i$, which is the event that $A_i$ does not occur.

#### Example with Dice

Consider the event of rolling a die three times and looking for at least one six. Let A, B, and C be the events where a six is rolled on the first, second, and third roll, respectively.

- $P(A) = P(B) = P(C) = \frac{1}{6}$
- $P(A^c) = P(B^c) = P(C^c) = \frac{5}{6}$

The probability of not rolling a six in any of the three rolls is:

$$
P(A^c \cap B^c \cap C^c) = P(A^c) \times P(B^c) \times P(C^c) = \left(\frac{5}{6}\right)^3
$$

Hence, the probability of rolling at least one six in three rolls is:

$$
P(A \cup B \cup C) = 1 - \left(\frac{5}{6}\right)^3
$$

## Conditional Probability

Conditional probability refers to the likelihood of an event occurring after another event has already happened. The notation P(A|B) denotes the probability of event A given that B has occurred. To calculate this, we use the formula:

$$
P(A|B) = \frac{P(A \cap B)}{P(B)}
$$

where:
- P(A|B) is the conditional probability of A given B,
- P(A ∩ B) is the joint probability of both A and B occurring,
- P(B) is the probability of B occurring.

### Example: Dice Roll

Consider the scenario of rolling a fair 6-sided die:

1. **P(4)**: The probability of rolling a 4 on a 6-sided die is one out of the six possible outcomes.
   
$$P(4) = \frac{1}{6}$$

3. **P(odd)**: An odd number can be rolled in three out of the six possible outcomes (1, 3, or 5).
   
$$P(odd) = \frac{3}{6} = \frac{1}{2}$$

5. **P(4 | odd)**: The conditional probability of rolling a 4 given that the die shows an odd number. Since 4 is an even number, it cannot be rolled if we know an odd number is rolled.

$$ P(4 | odd) = 0 $$

7. **P(odd | 4)**: The probability that the die shows an odd number given that a 4 is rolled. This is not possible as 4 is even, so this probability is zero.

$$ P(odd | 4) = 0 $$

### Example: Deck of Cards

Now let's apply conditional probability to a standard deck of 52 playing cards:

- Each suit (hearts, diamonds, clubs, spades) contains 13 cards.
- The probability of drawing any specific card, like a king, from the entire deck is 1 out of 52.
- The probability of drawing a card from a specific suit, like hearts, is 13 out of 52.

Given that we've drawn a heart, what is the probability that it's also a king?

- There is only one king in each suit, so the joint probability of drawing a card that is both a king and a heart is 1 out of 52.
- The probability of drawing a heart is 13 out of 52.

Therefore, the conditional probability is:

$$
P(\text{King}|\text{Heart}) = \frac{P(\text{King} \cap \text{Heart})}{P(\text{Heart})} = \frac{1/52}{13/52} = \frac{1}{13}
$$

### Example: Birthday Paradox

The birthday paradox explores the counter-intuitive probability that in a group of randomly chosen people, some will have the same birthday. Here, we'll consider the complementary probability that all chosen people have different birthdays.

#### Probability of Two People Having Different Birthdays (B2)

For two people, the probability that their birthdays are different is found by subtracting the probability that they have the same birthday from 1:

$$
P(B_2) = 1 - \frac{1}{365}
$$

Assuming there are 365 days in a year and ignoring leap years for simplicity.

#### Probability of Three People Having Different Birthdays (B3)

For three people, let A3 be the event that the third person's birthday is different from the first two. We assume that we already know that the first two people have different birthdays (B2).

The probability that A3 occurs given B2 is:

$$
P(A_3 | B_2) = 1 - \frac{2}{365}
$$

This is because there are two specific days that the third person must avoid to not match the birthdays of the first two people.

The overall probability of all three people having different birthdays is:

$$
P(B_3) = P(A_3 | B_2) \times P(B_2)
$$

Substituting the probabilities we get:

$$
P(B_3) = \left(1 - \frac{2}{365}\right) \times \left(1 - \frac{1}{365}\right) \approx 0.9918
$$

#### General Case for n People

For n people, we generalize this approach. The probability that the nth person has a different birthday from the previous n-1 people, given that all previous n-1 birthdays are different (B_{n-1}), is:

$$
P(A_n | B_{n-1}) = 1 - \frac{n-1}{365}
$$

So the probability that all n people have different birthdays can be found by multiplying all the individual conditional probabilities together:

$$
P(B_n) = P(A_n | B_{n-1}) \times P(A_{n-1} | B_{n-2}) \times \cdots \times P(A_3 | B_2) \times P(B_2)
$$

This product will continue until we reach P(B_2), which is the base case for two people.

## The Law of Total Probability

The law of total probability allows for the computation of the probability of an event A based on a set of mutually exclusive and exhaustive events. It's particularly useful when the overall sample space is divided into several distinct scenarios, or partitions, that cover all possible outcomes. The formula for the law of total probability is given by:

$$
P(A) = \sum_{i=1}^{n} P(A|B_i) \times P(B_i)
$$

where $B_1, B_2, ..., B_n$ are the partitions of the sample space and $P(A|B_i)$ is the conditional probability of A given $B_i$.

### Example: Probability of Drawing a Red Ball Second

Suppose we have a bag containing 3 red balls, 4 blue balls, and 5 green balls, and we want to find the probability of drawing a red ball on the second draw without replacement. We can partition the sample space into three mutually exclusive events based on the outcome of the first draw:

- $B_1$: The first ball drawn is red.
- $B_2$: The first ball drawn is blue.
- $B_3$: The first ball drawn is green.

Using the law of total probability:

1. If the first ball is red ($B_1$), then there are 2 red balls left out of the remaining 11 balls. So:
   - $P(\text{Red}|B_1) = \frac{2}{11}$
   - $P(B_1) = \frac{3}{12}$

2. If the first ball is blue ($B_2$), there are still 3 red balls left out of the remaining 11 balls. So:
   - $P(\text{Red}|B_2) = \frac{3}{11}$
   - $P(B_2) = \frac{4}{12}$

3. If the first ball is green ($B_3$), there are still 3 red balls left out of the remaining 11 balls. So:
   - $P(\text{Red}|B_3) = \frac{3}{11}$
   - $P(B_3) = \frac{5}{12}$

The total probability that the second ball is red is the sum of the probabilities of drawing a red ball given each initial event times the probability of each initial event:

$$
P(\text{Second ball is red}) = P(\text{Red}|B_1)P(B_1) + P(\text{Red}|B_2)P(B_2) + P(\text{Red}|B_3)P(B_3)
$$

Substituting in the values:

$$
P(\text{Second ball is red}) = \frac{2}{11} \times \frac{3}{12} + \frac{3}{11} \times \frac{4}{12} + \frac{3}{11} \times \frac{5}{12} = \frac{6}{132} + \frac{12}{132} + \frac{15}{132} = \frac{33}{132} = 0.25
$$

Therefore, the probability of drawing a red ball second, without replacement, is $0.25$ or $\frac{1}{4}$.

### Example: Probability of Drawing a White Ball

Consider a set of n+1 urns labeled from 0 to n. Each urn contains a mix of white and black balls, where the ratio of white balls to the total number of balls in the i-th urn is i/n. If we randomly select one urn and then draw one ball from it, we want to find the probability that this ball is white.

#### Conditional Probability

The conditional probability of drawing a white ball from the i-th urn, denoted as $U_i$, is given by the ratio of white balls in that urn:

$$
P(W | U_i) = \frac{i}{n}
$$

Where:
- $W$ represents the event of drawing a white ball.
- $U_i$ represents the event of selecting the i-th urn.

#### Probability of Selecting Each Urn

Assuming each urn has an equal probability of being chosen, the probability of selecting any particular urn is:

$$
P(U_i) = \frac{1}{n+1}
$$

#### Total Probability

To find the overall probability of drawing a white ball, we use the law of total probability. This accounts for the probability of drawing a white ball from each urn weighted by the probability of selecting that urn:

$$
P(W) = \sum_{i=0}^{n} P(W | U_i) \cdot P(U_i) = \frac{1}{n+1} \sum_{i=0}^{n} \frac{i}{n}
$$

#### Summation

The sum of the first n integers is given by the formula:

$$
\sum_{i=1}^{n} i = \frac{n(n+1)}{2}
$$

Note that the summation starts from i=1 since the 0-th urn contains no white balls and thus does not contribute to the probability of drawing a white ball.

#### Final Probability Calculation

Substituting the summation into the total probability formula, we get:

$$
P(W) = \frac{1}{n+1} \cdot \frac{1}{n} \cdot \frac{n(n+1)}{2} = \frac{1}{2}
$$

Thus, the probability of drawing a white ball from a randomly chosen urn is $\frac{1}{2}$, regardless of the number of urns.

## Bayes' Theorem

Bayes' theorem provides a way to update our probability estimates for an event based on new evidence. It connects the conditional and marginal probabilities of events, allowing us to revise our predictions or hypotheses in light of additional information. The theorem is stated mathematically as:

$$
P(A|B) = \frac{P(B|A) \times P(A)}{P(B)}
$$

where:
- $P(A|B)$ is the probability of event A given event B has occurred,
- $P(B|A)$ is the probability of event B given event A has occurred,
- $P(A)$ is the probability of event A, and
- $P(B)$ is the probability of event B.

### Example: Medical Diagnosis

Consider a medical test that is designed to diagnose a certain disease. The characteristics of the test are:
- True positive rate (sensitivity): 95% (if the person has the disease, the test is positive 95% of the time).
- False positive rate: 5% (if the person does not have the disease, the test is positive 5% of the time).
- Prevalence of the disease in the general population: 2%.

Let A be the event "person has the disease" and B be the event "person tests positive". Applying Bayes' theorem:

$$
P(A|B) = \frac{P(B|A) \times P(A)}{P(B)}
$$

First, we calculate the total probability of a positive test (P(B)), which includes both true and false positives:

$$
P(B) = P(B|A) \times P(A) + P(B|\text{not } A) \times P(\text{not } A)
$$

Plugging in the given rates:

- True positive rate $P(B|A) = 0.95$
- Prevalence $P(A) = 0.02$
- False positive rate $P(B|\text{not } A) = 0.05$
- Probability of not having the disease $P(\text{not } A) = 0.98$

The total probability of a positive test result is then:

$$
P(B) = (0.95 \times 0.02) + (0.05 \times 0.98)
$$

Applying these values to Bayes' theorem gives us:

$$
P(A|B) = \frac{0.95 \times 0.02}{(0.95 \times 0.02) + (0.05 \times 0.98)} \approx 0.2794
$$

Therefore, if a person tests positive, there is approximately a 27.94% chance that they actually have the disease.

### Example: BSE "Mad Cow" Disease Test

We are given a scenario where we need to determine the probability that a cow actually has BSE (Bovine Spongiform Encephalopathy), given that it has tested positive for the disease.

Given Quantities:

- The probability that the test is positive given the cow has BSE (true positive rate): $P(T | B) = 0.70$
- The probability that the test is positive given the cow does not have BSE (false positive rate): $P(T | B^c) = 0.10$
- The prior probability that a cow has BSE (prevalence of the disease): $P(B) = 0.02$

- $P(T | B) = 0.70$: The probability that the test is positive given the cow has BSE (true positive rate).
- $P(T | B^c) = 0.10$: The probability that the test is positive given the cow does not have BSE (false positive rate).
- $P(B) = 0.02$: The prevalence of the disease in the cow population (prior probability).

Complementary Probability:

- $P(B^c) = 1 - P(B)$: The probability that a cow does not have BSE.

#### Bayes' Theorem Application:

To find the conditional probability $P(B | T)$, we use Bayes' Theorem:

$$
P(B | T) = \frac{P(T | B) \cdot P(B)}{P(T)}
$$

The denominator, $P(T)$, is the total probability of a positive test result, which includes both true positives and false positives. This is obtained using the law of total probability:

$$
P(T) = P(T | B) \cdot P(B) + P(T | B^c) \cdot P(B^c)
$$

#### Calculation:

With the provided values:

- $P(B^c) = 0.98$
- $P(T) = 0.70 \cdot 0.02 + 0.10 \cdot 0.98$

We calculate $P(B | T)$:

$$
P(B | T) = \frac{0.70 \cdot 0.02}{0.70 \cdot 0.02 + 0.10 \cdot 0.98} \approx 0.125
$$

Thus, if a cow tests positive for BSE, there is a 12.5% chance that the cow actually has the disease.

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
