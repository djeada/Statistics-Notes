## Conditional Probability and Multiplication Rule

**Conditional Probability** is the likelihood of an event occurring given that another event has already occurred. It is denoted as \( P(A|B) \), representing the probability of event \( A \) happening, assuming event \( B \) has already taken place. This concept is crucial in understanding dependent events in probability theory. The **Multiplication Rule** uses conditional probability to calculate the probability of the intersection of two events. For dependent events, it is written as \( P(A \cap B) = P(A|B) \times P(B) \). If the events are independent, it simplifies to \( P(A \cap B) = P(A) \times P(B) \), as \( P(A|B) = P(A) \) in this case. This rule helps in determining joint probabilities of multiple events.

### Conditional Probability

Conditional probability refers to the probability of an event $A$ occurring given that another event $B$ has already occurred. It quantifies how the occurrence of one event affects the likelihood of another event. The formal definition of conditional probability is given by:

$$
P(A|B) = \frac{P(A \cap B)}{P(B)}
$$

Where:

- $P(A|B)$ is the conditional probability of event $A$ given that $B$ has occurred.
- $P(A \cap B)$ is the joint probability of both $A$ and $B$ occurring (the probability that both events happen together).
- $P(B)$ is the probability that event $B$ has occurred, and it must be non-zero (i.e., $P(B) > 0$) for the conditional probability to be well-defined.

Important Notes:

- Conditional probability is only defined when $P(B) \neq 0$.
- $P(A|B)$ describes how knowledge of $B$ influences our belief about the likelihood of $A$.

#### Example: Rolling a Die

Consider a fair six-sided die, where each face shows a number from 1 to 6, and all outcomes are equally likely. 

I. Probability of rolling a 4:

The probability of rolling a 4 on a six-sided die, $P(4)$, is simply:

$$
P(4) = \frac{1}{6}
$$

II. Probability of rolling an odd number:

There are three odd numbers (1, 3, 5) on a six-sided die. The probability of rolling any odd number, $P(\text{odd})$, is:

$$
P(\text{odd}) = \frac{3}{6} = \frac{1}{2}
$$

##### Conditional probability: $P(4 | \text{odd})$

The conditional probability $P(4 | \text{odd})$ represents the probability of rolling a 4 given that the outcome is known to be an odd number. Since 4 is an even number, it is impossible to roll a 4 if the die shows an odd number. Therefore, the conditional probability is:

$$
P(4 | \text{odd}) = 0
$$

##### Conditional probability: $P(\text{odd} | 4)$

The conditional probability $P(\text{odd} | 4)$ represents the probability that the die shows an odd number, given that a 4 has been rolled. Again, since 4 is even, this event is impossible, so:

$$
P(\text{odd} | 4) = 0
$$

##### Conditional Probability: $P(4 | \text{even})$

$P(4 | \text{even})$ represents the probability of rolling a 4, given that we know the die shows an even number.

To compute this, we apply the formula for conditional probability:

$$
P(4 | \text{even}) = \frac{P(4 \cap \text{even})}{P(\text{even})}
$$

- $P(4 \cap \text{even})$: This is the probability of rolling a number that is both 4 and even. Since 4 is an even number, $P(4 \cap \text{even}) = P(4) = \frac{1}{6}$.
- $P(\text{even})$: The probability of rolling any even number (2, 4, or 6), which is:

$$
P(\text{even}) = \frac{3}{6} = \frac{1}{2}
$$

Now, calculate $P(4 | \text{even})$:

$$
P(4 | \text{even}) = \frac{P(4 \cap \text{even})}{P(\text{even})} = \frac{1/6}{1/2} = \frac{1}{3}
$$

Thus, the probability of rolling a 4 given that an even number has been rolled is $\frac{1}{3}$.

##### Conditional Probability: $P(\text{even} | 4)$

$P(\text{even} | 4)$ represents the probability that the number rolled is even, given that the die shows a 4. This is an easy case because 4 is already an even number. So, we expect $P(\text{even} | 4) = 1$, but let's confirm it using the conditional probability formula:

$$
P(\text{even} | 4) = \frac{P(\text{even} \cap 4)}{P(4)}
$$

- $P(\text{even} \cap 4)$: This is the probability that the number rolled is both 4 and even. Since 4 is an even number, this is just $P(4)$, so $P(\text{even} \cap 4) = P(4) = \frac{1}{6}$.
- $P(4)$: The probability of rolling a 4 is $\frac{1}{6}$.

Now, calculate $P(\text{even} | 4)$:

$$
P(\text{even} | 4) = \frac{P(\text{even} \cap 4)}{P(4)} = \frac{1/6}{1/6} = 1
$$

Thus, the probability that the number is even given that a 4 was rolled is $1$, as expected.

#### Example: Deck of Cards

Now let’s apply conditional probability to a standard deck of 52 playing cards. Suppose we want to calculate the conditional probability of drawing a king given that the card drawn is a heart.

**I. Probability of drawing a king**:

The probability of drawing any specific card (such as a king) is:

$$
P(\text{King}) = \frac{4}{52} = \frac{1}{13}
$$

**II. Probability of drawing a heart**:

The probability of drawing any heart from the deck is:

$$
P(\text{Heart}) = \frac{13}{52} = \frac{1}{4}
$$

**III. Joint probability of drawing a king and a heart**:

There is exactly one king in the suit of hearts. Therefore, the probability of drawing the king of hearts is:

$$
P(\text{King} \cap \text{Heart}) = \frac{1}{52}
$$

**IV. Conditional probability $P(\text{King}|\text{Heart})$**:

Now, applying the formula for conditional probability:

$$
P(\text{King}|\text{Heart}) = \frac{P(\text{King} \cap \text{Heart})}{P(\text{Heart})} = \frac{1/52}{13/52} = \frac{1}{13}
$$

Thus, the probability of drawing a king given that the card drawn is a heart is $\frac{1}{13}$.

![65566289-77a5-453b-8f85-ea2de49db0c5](https://github.com/djeada/Statistics-Notes/assets/37275728/b0cc8b8e-b795-4998-a2df-a5f5f131c23d)

### Multiplication Rule for Dependent Events

If the occurrence of event A in some way influences the occurrence of event B, these events are considered dependent. For dependent events, the probability of both events occurring is given by:

$$
P(A \cap B) = P(A|B) \times P(B)
$$

Here, $P(A|B)$ is the conditional probability of event A given that event B has occurred. It represents the probability of A under the condition that B is known to have occurred.

### Example: Probabilities of Drawing Two Cards Consecutively from a Deck

We will compute the probability of two different card-drawing scenarios from a standard deck of 52 playing cards. Throughout the process, we will refer to the **three axioms of probability** where applicable.

#### Scenario 1: Probability of Drawing Two Diamonds Consecutively

I. **First Draw (Probability of Drawing a Diamond)**:  

There are 13 diamonds in a deck of 52 cards, so the probability of drawing a diamond on the first draw is:

$$
P(\text{first card Diamond}) = \frac{13}{52} = \frac{1}{4}
$$

This satisfies **Axiom 1 (Non-Negativity)** because the probability is a non-negative number.

II. **Second Draw (Probability of Drawing a Diamond Given the First was a Diamond)**:  

If the first card drawn was a diamond, only 12 diamonds remain in the deck, and the total number of remaining cards is 51. So, the conditional probability of drawing a diamond on the second draw, given that the first card was a diamond, is:

$$
P(\text{second card Diamond | first card Diamond}) = \frac{12}{51}
$$

This also satisfies **Axiom 1 (Non-Negativity)** as the probability is non-negative.

III. **Joint Probability of Both Events**: 

To find the probability of drawing two diamonds consecutively, we use the **Multiplication Rule** for dependent events:

$$
P(\text{first card Diamond} \cap \text{second card Diamond}) = P(\text{first card Diamond}) \times P(\text{second card Diamond | first card Diamond})
$$

Substituting the values:

$$
P(\text{first card Diamond} \cap \text{second card Diamond}) = \frac{13}{52} \times \frac{12}{51} = \frac{13 \times 12}{52 \times 51} = \frac{156}{2652} \approx 0.0588
$$

This probability satisfies **Axiom 3 (Additivity)**, since we are correctly combining probabilities of two dependent events, and we ensure that no probabilities exceed 1.

![40ae7df7-57fc-413d-8054-d592e9256bc8](https://github.com/djeada/Statistics-Notes/assets/37275728/dc0b84d6-ff74-4681-b329-f67a53512282)

#### Scenario 2: Probability of Drawing an Ace Followed by a King

I. **First Draw (Probability of Drawing an Ace)**:  

There are 4 Aces in the deck, so the probability of drawing an Ace on the first draw is:

$$
P(\text{first card Ace}) = \frac{4}{52} = \frac{1}{13}
$$

This satisfies **Axiom 1 (Non-Negativity)**, as the probability is non-negative.

II. **Second Draw (Probability of Drawing a King Given the First was an Ace)**:  

If an Ace is drawn on the first draw, the remaining deck has 51 cards, and there are still 4 Kings available. Therefore, the probability of drawing a King on the second draw, given that the first card was an Ace, is:

$$
P(\text{second card King | first card Ace}) = \frac{4}{51}
$$

This also satisfies **Axiom 1 (Non-Negativity)**.

III. **Joint Probability of Both Events**:

The probability of drawing an Ace followed by a King is calculated using the **Multiplication Rule**:

$$
P(\text{first card Ace} \cap \text{second card King}) = P(\text{first card Ace}) \times P(\text{second card King | first card Ace})
$$

Substituting the values:

$$
P(\text{first card Ace} \cap \text{second card King}) = \frac{4}{52} \times \frac{4}{51} = \frac{4 \times 4}{52 \times 51} = \frac{16}{2652} \approx 0.0060
$$

Again, this satisfies **Axiom 3 (Additivity)**, since we are combining the probabilities of two dependent events properly.

![20c6bf41-f037-46fa-b741-94f20aa0966f](https://github.com/djeada/Statistics-Notes/assets/37275728/e01bbe6f-a2d3-4109-a290-e9c619b7aa3c)

### Multiplication Rule for Independent Events

In probability theory, **independence** between two events means that the occurrence of one event does not affect the probability of the other. Formally, two events $A$ and $B$ are independent if:

$$
P(A|B) = P(A) \quad \text{and} \quad P(B|A) = P(B)
$$

This implies that knowing whether $B$ occurred does not change the probability of $A$ occurring, and vice versa. Another equivalent definition of independence is:

$$
P(A \cap B) = P(A) \cdot P(B)
$$

This means that the joint probability of both events occurring is the product of their individual probabilities.

#### Example: Independence of Events in Divisibility

Now let’s examine an example where two events might be independent, based on the set of integers from 1 to 100. The two events are:

- **Event A**: The number is divisible by 3.
- **Event B**: The number is divisible by 7.

**Step 1: Calculate $P(A)$** (Probability that a number is divisible by 3):

- The multiples of 3 between 1 and 100 are: $3, 6, 9, \dots, 99$.
- There are 33 such numbers, so:

$$
P(A) = \frac{33}{100}
$$

This satisfies **Axiom 1 (Non-Negativity)**, as $\frac{33}{100} \geq 0$.

**Step 2: Calculate $P(B)$** (Probability that a number is divisible by 7):

- The multiples of 7 between 1 and 100 are: $7, 14, 21, \dots, 98$.

- There are 14 such numbers, so:

$$
P(B) = \frac{14}{100}
$$

**Step 3: Calculate probability that a number is divisible by both 3 and 7**:

- To find numbers divisible by both 3 and 7, we look for multiples of the least common multiple (LCM) of 3 and 7, which is 21.
- The multiples of 21 between 1 and 100 are: $21, 42, 63, 84$, so there are 4 such numbers. Thus:

$$
P(A \cap B) = \frac{4}{100}
$$

**Step 4: Check for Independence**:

For independence, we need to check whether:

$$
P(A \cap B) = P(A) \cdot P(B)
$$

Calculate $P(A) \cdot P(B)$:

$$
P(A) \cdot P(B) = \frac{33}{100} \times \frac{14}{100} = \frac{462}{10000} = 0.0462
$$

The actual value of $P(A \cap B) = \frac{4}{100} = 0.04$.

Since $P(A \cap B) \neq P(A) \cdot P(B)$, the events are **not independent**.

#### Extending the Set to 105

Now, let’s extend the set of integers to 105 and check for independence again.

- **Event A**: Divisible by 3.
- **Event B**: Divisible by 7.

**Step 1: Calculate $P(A)$** (Divisibility by 3):

The multiples of 3 between 1 and 105 are: $3, 6, 9, \dots, 105$. There are 35 such numbers, so:

$$
P(A) = \frac{35}{105}
$$

**Step 2: Calculate $P(B)$** (Divisibility by 7):

The multiples of 7 between 1 and 105 are: $7, 14, 21, \dots, 105$. There are 15 such numbers, so:

$$
P(B) = \frac{15}{105}
$$

**Step 3: Calculate $P(A \cap B)$**:

The multiples of 21 between 1 and 105 are: $21, 42, 63, 84, 105$, so there are 5 such numbers.

$$
P(A \cap B) = \frac{5}{105}
$$

**Step 4: Check for Independence**:

Calculate $P(A) \cdot P(B)$:

$$
P(A) \cdot P(B) = \frac{35}{105} \times \frac{15}{105} = \frac{525}{11025} = \frac{5}{105}
$$

Since $P(A) \cdot P(B) = P(A \cap B)$, the events are now **independent** with this extended set of numbers.

#### Example: Probability of At Least One of n Independent Events Occurring

In probability theory, when calculating the probability that at least one of several independent events occurs, the easiest method is often using the **complementary rule**. This approach is particularly useful when dealing with independent events, where directly applying the **inclusion-exclusion principle** (from the addition rule) can become cumbersome as the number of events increases.

##### Case 1: Three Independent Events

Consider three independent events $A$, $B$, and $C$. We want to find the probability that **at least one of these events occurs**. 

The complementary approach is easier because it first calculates the probability that **none** of the events occur and then subtracts that from 1 (the total probability of the sample space, by Axiom 2).

**Step 1: Probability that none of the events occur**

The events $A$, $B$, and $C$ are independent, so the probability that none occur is the product of the individual probabilities that each does not occur:

$$
P(A^c \cap B^c \cap C^c) = P(A^c) \times P(B^c) \times P(C^c)
$$

This step is based on the **Multiplication Rule** for independent events and satisfies **Axiom 1 (Non-Negativity)**, ensuring that each term in the product is non-negative.

**Step 2: Complement Rule**

The probability that **at least one** event occurs is the complement of the probability that none of them occur:

$$
P(A \cup B \cup C) = 1 - P(A^c \cap B^c \cap C^c)
$$

This satisfies **Axiom 2 (Normalization)**, which ensures that the total probability across all possible outcomes sums to 1.

**Example Calculation:**

Suppose each of the events $A$, $B$, and $C$ has a probability of occurring equal to $P(A) = P(B) = P(C) = \frac{1}{6}$.

- The probability of each event **not** occurring is $P(A^c) = P(B^c) = P(C^c) = \frac{5}{6}$.
- Therefore:

$$
P(A^c \cap B^c \cap C^c) = \left(\frac{5}{6}\right) \times \left(\frac{5}{6}\right) \times \left(\frac{5}{6}\right) = \left(\frac{5}{6}\right)^3 = \frac{125}{216}
$$

The probability that at least one event occurs is:

$$
P(A \cup B \cup C) = 1 - \frac{125}{216} = \frac{91}{216} \approx 0.4213
$$

Thus, the probability that at least one of the three events occurs is approximately $0.4213$.

##### Case 2: n Independent Events

For $n$ independent events $A_1, A_2, \dots, A_n$, the same complementary approach can be extended.

**Step 1: Generalize the Complement Rule**

The probability that **none** of the events occur is:

$$
P(A_1^c \cap A_2^c \cap \dots \cap A_n^c) = P(A_1^c) \times P(A_2^c) \times \cdots \times P(A_n^c)
$$

Again, this is based on the **Multiplication Rule** for independent events.

**Step 2: Calculate the Complementary Probability**

The probability that at least one of the $n$ independent events occurs is:

$$
P(A_1 \cup A_2 \cup \cdots \cup A_n) = 1 - P(A_1^c) \times P(A_2^c) \times \cdots \times P(A_n^c)
$$

This applies **Axiom 2 (Normalization)**, ensuring that the probability of the entire sample space (i.e., at least one event occurring) equals 1.

#### Dice Example: At Least One Six in Three Rolls

Consider rolling a fair six-sided die three times, and let $A$, $B$, and $C$ represent the events of rolling a six on the first, second, and third rolls, respectively.

**Step 1: Calculate the Complementary Probability**

- The probability of rolling a six on any roll is $P(A) = P(B) = P(C) = \frac{1}{6}$.
- The probability of **not** rolling a six on any roll is $P(A^c) = P(B^c) = P(C^c) = \frac{5}{6}$.
- The probability of **not** rolling a six in any of the three rolls is:

$$
P(A^c \cap B^c \cap C^c) = \left(\frac{5}{6}\right)^3 = \frac{125}{216}
$$

**Step 2: Calculate the Probability of Rolling at Least One Six**

The probability of rolling at least one six in the three rolls is:

$$
P(A \cup B \cup C) = 1 - \frac{125}{216} = \frac{91}{216} \approx 0.4213
$$

Thus, the probability of rolling at least one six in three rolls is approximately $0.4213$.

This example demonstrates the use of the **Multiplication Rule** for independent events, **Axiom 2 (Normalization)** to ensure the total probability is 1, and **Axiom 1 (Non-Negativity)** to ensure all probabilities are non-negative.

![3d0579b3-0e10-41ce-b77d-5fc5528908ee](https://github.com/djeada/Statistics-Notes/assets/37275728/813b1539-531f-4a1f-8248-757aca88bf8c)

### The Birthday Paradox

The birthday paradox refers to the surprising probability that in a group of randomly chosen people, at least two will share the same birthday. The intuition might suggest that this probability is low for small groups, but in fact, it's much higher than one might expect. To understand this better, we calculate the complementary probability — the probability that **all** people in the group have **different birthdays**.

Assumptions:

- There are 365 days in a year.
- We ignore leap years for simplicity.
- Birthdays are uniformly distributed, meaning each day is equally likely to be a birthday.

To find the probability that at least two people share a birthday, we use the complement of the event where all $n$ people have different birthdays. That is:

$$
P(\text{at least one shared birthday}) = 1 - P(\text{all birthdays different})
$$

#### For Two People

For two people, the probability that they **do not** share the same birthday is:

$$
P(B_2) = \frac{364}{365}
$$

This is the probability that the second person chooses a different birthday from the first person.

Therefore, the probability that **at least two people share the same birthday** is the complement:

$$
P(\text{at least one shared birthday for 2 people}) = 1 - P(B_2) = 1 - \frac{364}{365} \approx 0.00274
$$

So, the probability is approximately 0.27% for two people.

#### For Three People

For three people, we first calculate the probability that all three have different birthdays:

$$
P(B_3) = \frac{364}{365} \times \frac{363}{365}
$$

The second person avoids the first person's birthday, and the third person avoids the birthdays of the first two people.

Therefore, the probability that at least two people share the same birthday is:

$$
P(\text{at least one shared birthday for 3 people}) = 1 - P(B_3) = 1 - \frac{364}{365} \times \frac{363}{365} \approx 1 - 0.9918 = 0.0082
$$

This gives a probability of approximately 0.82%.

#### For Four People

For four people, the probability that all four have different birthdays is:

$$
P(B_4) = \frac{364}{365} \times \frac{363}{365} \times \frac{362}{365}
$$

The fourth person avoids the birthdays of the first three.

Therefore, the probability that at least two people share the same birthday is:

$$
P(\text{at least one shared birthday for 4 people}) = 1 - P(B_4) = 1 - \frac{364}{365} \times \frac{363}{365} \times \frac{362}{365} \approx 1 - 0.9836 = 0.0164
$$

This gives a probability of approximately 1.64%.

#### General Case for $n$ People

For $n$ people, we generalize this approach. The probability that all $n$ people have different birthdays is calculated by successively multiplying the probabilities that each additional person has a different birthday, given that the previous people have already chosen different birthdays.

For the $n$-th person, the probability that they have a different birthday from the previous $n-1$ people, given that the first $n-1$ people have different birthdays, is:

$$
P(A_n | B_{n-1}) = 1 - \frac{n-1}{365} = \frac{365 - (n-1)}{365}
$$

Thus, the overall probability that all $n$ people have different birthdays is the product of all these conditional probabilities:

$$
P(B_n) = P(A_n | B_{n-1}) \times P(A_{n-1} | B_{n-2}) \times \cdots \times P(A_3 | B_2) \times P(B_2)
$$

This product simplifies to:

$$
P(B_n) = \frac{365}{365} \times \frac{364}{365} \times \frac{363}{365} \times \cdots \times \frac{365 - (n-1)}{365}
$$

Therefore, the probability that at least two people share a birthday is:

$$
P(\text{at least one shared birthday for } n \text{ people}) = 1 - P(B_n)
$$

Let's calculate the probabilities for small group sizes:

- **2 people**: $P(\text{at least one shared birthday}) \approx 0.00274$ (0.27%)
- **3 people**: $P(\text{at least one shared birthday}) \approx 0.0082$ (0.82%)
- **4 people**: $P(\text{at least one shared birthday}) \approx 0.0164$ (1.64%)
- **5 people**: $P(\text{at least one shared birthday}) \approx 0.027$ (2.7%)
- **10 people**: $P(\text{at least one shared birthday}) \approx 0.117$ (11.7%)
- **23 people**: $P(\text{at least one shared birthday}) \approx 0.507$ (50.7%)
- **30 people**: $P(\text{at least one shared birthday}) \approx 0.706$ (70.6%)
- **50 people**: $P(\text{at least one shared birthday}) \approx 0.97$ (97%)

Below is the visualization of the probability that at least two people share the same birthday as the group size increases. The red dashed line indicates the 50% probability mark, which occurs at around 23 people:

![output(10)](https://github.com/user-attachments/assets/c0b74baa-a2d8-4695-ac32-ab0fdeb49543)
