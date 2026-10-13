# Axioms of Probability: Exercises

Practice for the note [Axioms of Probability](../../notes/probability/axioms_of_probability.md).

## Problems

1. **Valid assignments.** For $S=\{a,b,c\}$, which of the following are valid probability assignments? (i) $P(a)=0.5,P(b)=0.3,P(c)=0.3$; (ii) $P(a)=0.4,P(b)=0.6,P(c)=0$; (iii) $P(a)=0.7,P(b)=-0.1,P(c)=0.4$.

2. **Complement rule.** Derive $P(A^c)=1-P(A)$ from the axioms, then compute the probability of not rolling a six on a fair die.

3. **Addition rule.** Prove $P(A\cup B)=P(A)+P(B)-P(A\cap B)$ from the axioms. If $P(A)=0.5$, $P(B)=0.4$, $P(A\cap B)=0.2$, find $P(A\cup B)$, $P(\text{neither})$, and $P(A\text{ only})$.

4. **Monotonicity.** Show that $A\subseteq B$ implies $P(A)\le P(B)$. If $P(B)=0.6$ and $P(B\setminus A)=0.25$, find $P(A)$.

5. **Cards.** Find $P(\text{spade or face card})$ for one draw from a standard deck.

6. **Dice.** Two fair dice are rolled. Find $P(\text{sum is even or sum}\ge10)$.

7. **Three events.** $P(A)=0.5$, $P(B)=0.4$, $P(C)=0.3$, $P(A\cap B)=0.2$, $P(A\cap C)=0.1$, $P(B\cap C)=0.15$, $P(A\cap B\cap C)=0.05$. Find $P(A\cup B\cup C)$.

8. **Bounds.** If $P(A)=0.6$ and $P(B)=0.7$, what are the smallest and largest possible values of $P(A\cap B)$?

9. **Exclusive versus independent.** Events $A$ and $B$ have $P(A)=0.3$ and $P(B)=0.5$ and are mutually exclusive. Can they be independent?

## Solutions

### Solution 1

Check nonnegativity and $P(S)=1$ (sum of outcome probabilities).

(i) $0.5+0.3+0.3=1.1\neq1$: invalid.
(ii) $0.4+0.6+0=1$, all nonnegative: valid (an outcome may have probability 0).
(iii) Sum is $1.0$ but $P(b)=-0.1<0$: invalid.

### Solution 2

$A$ and $A^c$ are disjoint and $A\cup A^c=S$. By Axiom III, $P(A)+P(A^c)=P(S)$, and by Axiom II, $P(S)=1$. Hence $P(A^c)=1-P(A)$.

Not rolling a six: $1-\frac16=\frac56$.

### Solution 3

Write $A\cup B=A\cup(B\setminus A)$ as a disjoint union, and $B=(A\cap B)\cup(B\setminus A)$, also disjoint. By Axiom III:

$$P(A\cup B)=P(A)+P(B\setminus A),\qquad P(B)=P(A\cap B)+P(B\setminus A).$$

Substituting $P(B\setminus A)=P(B)-P(A\cap B)$ into the first equation gives the addition rule.

Numbers: $P(A\cup B)=0.5+0.4-0.2=0.7$. $P(\text{neither})=1-0.7=0.3$. $P(A\text{ only})=P(A)-P(A\cap B)=0.5-0.2=0.3$.

### Solution 4

If $A\subseteq B$ then $B=A\cup(B\setminus A)$, a disjoint union, so $P(B)=P(A)+P(B\setminus A)\ge P(A)$ because $P(B\setminus A)\ge0$ (Axiom I).

Numbers: $P(A)=P(B)-P(B\setminus A)=0.6-0.25=0.35$.

### Solution 5

Spades: 13. Face cards: 12. Spade face cards: 3.

$$P=\frac{13}{52}+\frac{12}{52}-\frac{3}{52}=\frac{22}{52}=\frac{11}{26}\approx0.423.$$

### Solution 6

- Even sum: sums 2, 4, 6, 8, 10, 12 occur $1+3+5+5+3+1=18$ times, so $P=18/36$.
- Sum $\ge10$: $3+2+1=6$ pairs, $P=6/36$.
- Both: sums 10 and 12 occur $3+1=4$ times, $P=4/36$.

$$P=\frac{18}{36}+\frac{6}{36}-\frac{4}{36}=\frac{20}{36}=\frac59\approx0.556.$$

### Solution 7

Inclusion-exclusion:

$$P(A\cup B\cup C)=0.5+0.4+0.3-0.2-0.1-0.15+0.05.$$

Singles: $1.2$. Pairs: $0.45$. Triple: $0.05$. Result: $1.2-0.45+0.05=0.8$.

### Solution 8

Largest: $A\cap B\subseteq A$ and $\subseteq B$, so $P(A\cap B)\le\min(0.6,0.7)=0.6$ (attained when $A\subseteq B$).

Smallest: $P(A\cup B)\le1$, so $P(A\cap B)=P(A)+P(B)-P(A\cup B)\ge0.6+0.7-1=0.3$.

Therefore $0.3\le P(A\cap B)\le0.6$.

### Solution 9

Mutually exclusive means $P(A\cap B)=0$. Independence would require $P(A\cap B)=P(A)P(B)=0.3\cdot0.5=0.15\neq0$. So they cannot be independent. In general, two events with positive probabilities are never both mutually exclusive and independent: knowing one occurred tells you the other did not.
