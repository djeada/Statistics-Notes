# Quizzes on Probability

This series of quizzes covers essential topics in probability theory, including:

- **Bayes' Theorem**: Deepen your understanding of Bayes' Theorem, exploring its applications in real-world scenarios such as medical diagnoses, spam filtering, and more.
- **Conditional Probability**: Test your ability to calculate probabilities under given conditions and explore the behavior of dependent and independent events.
- **Joint Probability**: Learn how to compute the probability of multiple events occurring together, and discover how joint probability is applied in various fields like machine learning and decision-making.
- **Marginal Probability**: Understand how to derive the probability of a single event by aggregating joint probabilities over other variables.
- **Independence**: Explore the concept of event independence and how to determine if two or more events are independent or dependent on each other.
- **Law of Total Probability**: Apply the law of total probability to break down complex probability problems.


## Bayes' Theorem

<details>
<summary>What is Bayes' Theorem?</summary><br>
Bayes' Theorem is a fundamental formula in probability theory that allows you to update the probability of a hypothesis based on new evidence. It is written as:  
\[ P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)} \]  
where:
- $P(A|B)$ is the **posterior probability** (the probability of event A occurring given that B is true),
- $P(B|A)$ is the **likelihood** (the probability of event B occurring given that A is true),
- $P(A)$ is the **prior probability** of A,
- $P(B)$ is the **marginal probability** of B.

Bayes' Theorem is widely used in fields such as medical testing, where it helps calculate the probability of a disease given a positive test result.
</details>

<details>
<summary>What is an example of applying Bayes' Theorem in medical testing?</summary><br>
Suppose a test for a certain disease has a 99% accuracy rate, meaning the probability of testing positive given the disease is 99% $P(Pos|Disease) = 0.99$. However, if the disease only affects 1% of the population, the **prior probability** of the disease $P(Disease) = 0.01$. If a person tests positive, Bayes' Theorem can be used to update the probability that they actually have the disease, factoring in the false positive rate and the disease prevalence.

Bayes' Theorem in this case would provide a more accurate probability based on available data rather than assuming a positive test always means the presence of the disease.
</details>

<details>
<summary>How does Bayes' Theorem differ from classical probability?</summary><br>
Classical probability often deals with frequencies of events, whereas Bayes' Theorem introduces the concept of **updating** a probability based on new evidence. Classical probability is static and does not consider past events, while Bayes' Theorem evolves with new data and is used to update **beliefs** or **hypotheses** dynamically.
</details>

---

## Conditional Probability

<details>
<summary>What is conditional probability?</summary><br>
Conditional probability is the probability of an event occurring given that another event has already occurred. It helps in understanding how the probability of one event is affected by the presence or absence of another event. The formula for conditional probability is:  
\[ P(A|B) = \frac{P(A \cap B)}{P(B)} \]  
where $P(A|B)$ is the probability of A occurring given that B has occurred, and $P(A \cap B)$ is the joint probability of A and B happening together.
</details>

<details>
<summary>What is an example of conditional probability in everyday life?</summary><br>
Consider the probability of it raining given that the sky is cloudy. The probability of rain (A) is influenced by the presence of clouds (B). The conditional probability $P(A|B)$ will likely be higher than the unconditional probability of rain, as clouds increase the likelihood of rain.
</details>

<details>
<summary>How does conditional probability relate to independent events?</summary><br>
If two events are **independent**, the occurrence of one does not affect the probability of the other, meaning:
\[ P(A|B) = P(A) \]  
For independent events, the conditional probability is the same as the unconditional probability, as there is no relationship between A and B.
</details>

<details>
<summary>How do you calculate the probability of multiple dependent events?</summary><br>
For dependent events, the probability of multiple events occurring in sequence (e.g., A then B) is the product of the first event's probability and the conditional probability of the second event given the first:
\[ P(A \cap B) = P(A) \times P(B|A) \]  
This formula accounts for the fact that the occurrence of A affects the probability of B.
</details>

---

## Joint Probability

<details>
<summary>What is joint probability?</summary><br>
Joint probability is the probability that two or more events occur together. For two events A and B, the joint probability $P(A \cap B)$ represents the likelihood that both A and B happen. If the events are **independent**, the joint probability is the product of their individual probabilities:
\[ P(A \cap B) = P(A) \times P(B) \]
</details>

<details>
<summary>What is an example of joint probability?</summary><br>
Suppose you are rolling two dice. The probability of rolling a 6 on the first die and a 6 on the second die is the joint probability $P(6 \cap 6)$. Since these events are independent, you can calculate this by multiplying the probabilities:
\[ P(6 \cap 6) = \frac{1}{6} \times \frac{1}{6} = \frac{1}{36} \]
</details>

<details>
<summary>How does joint probability differ for dependent events?</summary><br>
For dependent events, the joint probability is not simply the product of individual probabilities. Instead, you must use the conditional probability formula:
\[ P(A \cap B) = P(A) \times P(B|A) \]  
This accounts for the fact that the occurrence of event A influences the probability of event B.
</details>

---

## Marginal Probability

<details>
<summary>What is marginal probability?</summary><br>
Marginal probability refers to the probability of a single event occurring, without regard to other events. It is derived from the joint probabilities by summing over all possible outcomes for other variables. For example, the marginal probability of A can be written as:
\[ P(A) = \sum_{B} P(A \cap B) \]
</details>

<details>
<summary>How does marginal probability relate to joint probability?</summary><br>
Marginal probability is the result of **summing** or **integrating** over the joint probabilities of related events. For example, if A and B are two events, the marginal probability of A is obtained by summing the joint probabilities of A occurring with each possible outcome of B.
</details>

---

## Independence

<details>
<summary>What does it mean for two events to be independent?</summary><br>
Two events are independent if the occurrence of one does not affect the probability of the other. Mathematically, events A and B are independent if:
\[ P(A \cap B) = P(A) \times P(B) \]  
In this case, knowing that event B has occurred gives no additional information about the likelihood of A occurring, and vice versa.
</details>

<details>
<summary>How can you test if two events are independent?</summary><br>
To test for independence, check if the joint probability $P(A \cap B)$ equals the product of the individual probabilities $P(A) \times P(B)$. If the equality holds, the events are independent; otherwise, they are dependent.
</details>

---

## Law of Total Probability

<details>
<summary>What is the Law of Total Probability?</summary><br>
The Law of Total Probability states that if you have a set of mutually exclusive events $B_1, B_2, ..., B_n$ that cover all possible outcomes, the probability of any event A can be expressed as:
\[ P(A) = \sum_{i} P(A|B_i) P(B_i) \]
This law is useful for breaking down complex probability problems by considering all possible conditions.
</details>
