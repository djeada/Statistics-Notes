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

![40ae7df7-57fc-413d-8054-d592e9256bc8](https://github.com/djeada/Statistics-Notes/assets/37275728/dc0b84d6-ff74-4681-b329-f67a53512282)

#### Probability of Drawing an Ace Followed by a King
- The probability of drawing an Ace first is 4 out of 52.
- If an Ace has been drawn, there are 4 Kings left in the remaining 51 cards, so the probability of drawing a King next is:

$$ P(\text{second card King | first card Ace}) = \frac{4}{51} $$

Applying the multiplication rule here gives us:

$$ P(\text{first card Ace} \cap \text{second card King}) = P(\text{first card Ace}) \times P(\text{second card King | first card Ace}) = \frac{4}{52} \times \frac{4}{51} \approx 0.0060 $$

![20c6bf41-f037-46fa-b741-94f20aa0966f](https://github.com/djeada/Statistics-Notes/assets/37275728/e01bbe6f-a2d3-4109-a290-e9c619b7aa3c)

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

![3d0579b3-0e10-41ce-b77d-5fc5528908ee](https://github.com/djeada/Statistics-Notes/assets/37275728/813b1539-531f-4a1f-8248-757aca88bf8c)

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

![65566289-77a5-453b-8f85-ea2de49db0c5](https://github.com/djeada/Statistics-Notes/assets/37275728/b0cc8b8e-b795-4998-a2df-a5f5f131c23d)

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

![a22b209a-c8da-4825-a5cc-936dc62eb27c](https://github.com/djeada/Statistics-Notes/assets/37275728/4a2bfafd-c123-4dff-8219-342ab8fe185c)

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

