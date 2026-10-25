# Probability

Probability assigns coherent numerical weights to possible outcomes. A sample space specifies what can happen, and an event is a set of outcomes that answers a particular question. Once a probability model is specified, the same rules apply whether uncertainty concerns a die roll, a sample from a population, or a sequence of dependent events.

## Combining and conditioning events

The axioms require nonnegative probabilities, total probability one, and additivity for disjoint events. Other rules follow from these requirements. The complement rule counts everything outside an event. The addition rule subtracts an overlap that would otherwise be counted twice.

Conditioning changes the reference set: after learning that an event occurred, we renormalize probabilities within that event. Independence is the special case in which this information does not change the probability of the other event. Disjointness has a different meaning: two events cannot occur together, so observing one rules out the other.

## Choosing a useful decomposition

The law of total probability splits a question across mutually exclusive cases that cover the sample space. Bayes' theorem uses the same decomposition to reverse a conditional probability. Probability trees organize sequential cases by multiplying along a path and adding across disjoint paths.

Geometric probability replaces counting with length, area, or volume only when the sampling model is uniform in the relevant geometric measure. A random variable then maps outcomes to numbers, allowing the same probability rules to describe distributions, expected values, and numerical summaries of uncertainty.
