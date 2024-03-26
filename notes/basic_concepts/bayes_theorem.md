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

Let's say $P(A)=0.3$ and $P(B)=0.4$ then:

![a10438be-8900-4dab-92ce-9c9fcb89875b](https://github.com/djeada/Statistics-Notes/assets/37275728/34f9b564-ba7b-4d70-aa57-ad324c168b82)

### Example: Medical Diagnosis

Consider a medical test that is designed to diagnose a certain disease. The characteristics of the test are:
- True positive rate (sensitivity): 95% (if the person has the disease, the test is positive 95% of the time).
- False positive rate: 5% (if the person does not have the disease, the test is positive 5% of the time).
- Prevalence of the disease in the general population: 2%.
  
![9f1ea5e9-cad4-4fc2-a6aa-5fee4f309a2d](https://github.com/djeada/Statistics-Notes/assets/37275728/dbdb3a4d-4f73-4efe-bacb-87a7bab167c7)

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

![3a2138ad-9dbb-4b0c-9b5e-8bbaab5d4e70](https://github.com/djeada/Statistics-Notes/assets/37275728/e6d36e01-6d39-4762-b29e-c24d4b8a19d2)

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

![bcde4473-8acf-4dd8-a60e-c4a7b551f02d](https://github.com/djeada/Statistics-Notes/assets/37275728/69f47572-5fa7-4365-90f3-983e90340b24)

- $P(T | B) = 0.70$: The probability that the test is positive given the cow has BSE (true positive rate).
- $P(T | B^c) = 0.10$: The probability that the test is positive given the cow does not have BSE (false positive rate).
- $P(B) = 0.02$: The prevalence of the disease in the cow population (prior probability).

Complementary Probability:

- $P(B^c) = 1 - P(B)$: The probability that a cow does not have BSE.

To find the conditional probability $P(B | T)$, we use Bayes' Theorem:

$$
P(B | T) = \frac{P(T | B) \cdot P(B)}{P(T)}
$$

The denominator, $P(T)$, is the total probability of a positive test result, which includes both true positives and false positives. This is obtained using the law of total probability:

$$
P(T) = P(T | B) \cdot P(B) + P(T | B^c) \cdot P(B^c)
$$

![0663c27b-403f-4b28-8a3d-8999625f2bdd](https://github.com/djeada/Statistics-Notes/assets/37275728/51943b61-62d0-4bfb-b5dc-3198d764efdc)

With the provided values:

- $P(B^c) = 0.98$
- $P(T) = 0.70 \cdot 0.02 + 0.10 \cdot 0.98$

We calculate $P(B | T)$:

$$
P(B | T) = \frac{0.70 \cdot 0.02}{0.70 \cdot 0.02 + 0.10 \cdot 0.98} \approx 0.125
$$

Thus, if a cow tests positive for BSE, there is a 12.5% chance that the cow actually has the disease.
