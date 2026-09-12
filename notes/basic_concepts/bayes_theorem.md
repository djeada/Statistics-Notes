# Bayes' Theorem

Bayes' theorem provides a way to update the probability of an event when new evidence becomes available. It connects conditional probabilities and allows us to revise an initial probability, or prior, in light of additional information.

The theorem is:

$$
P(A|B) = \frac{P(B|A) \times P(A)}{P(B)}
$$

where:

* $P(A|B)$ is the probability of event $A$ given that event $B$ has occurred,
* $P(B|A)$ is the probability of event $B$ given that event $A$ has occurred,
* $P(A)$ is the prior probability of event $A$,
* $P(B)$ is the overall probability of event $B$.

The formula assumes that $P(B) > 0$.

### Derivation from Conditional Probability

Bayes' theorem follows directly from the definition of conditional probability. Recall that:

$$
P(A|B) = \frac{P(A \cap B)}{P(B)}
$$

Similarly:

$$
P(B|A) = \frac{P(A \cap B)}{P(A)}
$$

From the second equation, we can solve for the joint probability:

$$
P(A \cap B) = P(B|A) \times P(A)
$$

Substituting this expression for $P(A \cap B)$ into the first equation gives Bayes' theorem:

$$
P(A|B) = \frac{P(B|A) \times P(A)}{P(B)}
$$

When $P(B)$ is not known directly, it can often be calculated using the law of total probability. If $A$ and $A^c$, the complement of $A$, partition the sample space, then:

$$
P(B) = P(B|A) \times P(A) + P(B|A^c) \times P(A^c)
$$

Substituting this into Bayes' theorem gives:

$$
P(A|B) = \frac{P(B|A)P(A)} {P(B|A)P(A) + P(B|A^c)P(A^c)}
$$

This form is especially useful in diagnostic and classification problems, where the prior probability $P(A)$ and the likelihoods $P(B|A)$ and $P(B|A^c)$ are known.

For example, suppose $P(A)=0.3$ and $P(B)=0.4$. The diagram below can help visualize the relationship between the events:

![a10438be-8900-4dab-92ce-9c9fcb89875b](https://github.com/djeada/Statistics-Notes/assets/37275728/34f9b564-ba7b-4d70-aa57-ad324c168b82)

However, these two marginal probabilities alone are not enough to calculate $P(A|B)$. We also need information about how $A$ and $B$ overlap, such as $P(A \cap B)$ or $P(B|A)$.

### Example: Medical Diagnosis

Consider a medical test designed to detect a particular disease. The test has the following characteristics:

* True positive rate (sensitivity): 95%. If a person has the disease, the test is positive 95% of the time.
* False positive rate: 5%. If a person does not have the disease, the test is positive 5% of the time.
* Prevalence of the disease in the general population: 2%.

![9f1ea5e9-cad4-4fc2-a6aa-5fee4f309a2d](https://github.com/djeada/Statistics-Notes/assets/37275728/dbdb3a4d-4f73-4efe-bacb-87a7bab167c7)

Let $A$ be the event "the person has the disease" and $B$ be the event "the person tests positive."

We want to calculate:

$$
P(A|B)
$$

Using Bayes' theorem:

$$
P(A|B) = \frac{P(B|A) \times P(A)}{P(B)}
$$

First, calculate the total probability of a positive test result. A positive result can come from either a true positive or a false positive:

$$
P(B) = P(B|A) \times P(A) + P(B|A^c) \times P(A^c)
$$

The given values are:

* True positive rate: $P(B|A) = 0.95$
* Disease prevalence: $P(A) = 0.02$
* False positive rate: $P(B|A^c) = 0.05$
* Probability of not having the disease: $P(A^c) = 0.98$

![3a2138ad-9dbb-4b0c-9b5e-8bbaab5d4e70](https://github.com/djeada/Statistics-Notes/assets/37275728/e6d36e01-6d39-4762-b29e-c24d4b8a19d2)

The total probability of a positive test is:

$$
P(B) = (0.95 \times 0.02) + (0.05 \times 0.98)
$$

Therefore:

$$
P(B) = 0.019 + 0.049 = 0.068
$$

Now apply Bayes' theorem:

$$
P(A|B) = \frac{0.95 \times 0.02} {(0.95 \times 0.02) + (0.05 \times 0.98)} \approx 0.2794
$$

Therefore, given a positive test result, the probability that the person actually has the disease is approximately 27.94%.

This example shows why the prevalence of a condition matters. Even a test with high sensitivity can produce a substantial proportion of false positives when the condition itself is rare.

### Example: BSE "Mad Cow" Disease Test

Suppose we want to determine the probability that a cow actually has BSE (Bovine Spongiform Encephalopathy) given that it has tested positive.

Given Quantities:

* True positive rate: $P(T|B) = 0.70$
* False positive rate: $P(T|B^c) = 0.10$
* Prior probability, or prevalence, of BSE: $P(B) = 0.02$

Here:

* $B$ is the event that the cow has BSE,
* $B^c$ is the event that the cow does not have BSE,
* $T$ is the event that the test result is positive.

![bcde4473-8acf-4dd8-a60e-c4a7b551f02d](https://github.com/djeada/Statistics-Notes/assets/37275728/69f47572-5fa7-4365-90f3-983e90340b24)

Complementary Probability:

The probability that a cow does not have BSE is:

$$
P(B^c) = 1 - P(B)
$$

so:

$$
P(B^c) = 1 - 0.02 = 0.98
$$

To find the conditional probability $P(B|T)$, we use Bayes' theorem:

$$
P(B|T) = \frac{P(T|B) \cdot P(B)} {P(T)}
$$

The denominator $P(T)$ is the total probability of a positive test. It includes both true positives and false positives:

$$
P(T) = P(T|B) \cdot P(B) + P(T|B^c) \cdot P(B^c)
$$

![0663c27b-403f-4b28-8a3d-8999625f2bdd](https://github.com/djeada/Statistics-Notes/assets/37275728/51943b61-62d0-4bfb-b5dc-3198d764efdc)

Substituting the given values:

$$
P(T) = 0.70 \cdot 0.02 + 0.10 \cdot 0.98
$$

Therefore:

$$
P(T) = 0.014 + 0.098 = 0.112
$$

Now apply Bayes' theorem:

$$
P(B|T) = \frac{0.70 \cdot 0.02} {0.70 \cdot 0.02 + 0.10 \cdot 0.98} =
\frac{0.014}{0.112} = 0.125
$$

Thus, given a positive BSE test result, the probability that the cow actually has BSE is 12.5%.

As in the medical diagnosis example, the result depends not only on the accuracy of the test but also on the prior prevalence of the disease. When the disease is uncommon, false positives can make up a significant share of all positive test results.
