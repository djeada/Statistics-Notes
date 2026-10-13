# Bayes' Theorem: Exercises

Practice for the note [Bayes' Theorem](../../notes/probability/bayes_theorem.md).

## Problems

1. **Screening.** A disease has prevalence 1%. A test has sensitivity 90% and false positive rate 8%. Find $P(\text{disease}\mid+)$.

2. **Higher prevalence.** Repeat Problem 1 with prevalence 20% and explain why the answer changes so much.

3. **Which machine?** Machines $M_1,M_2,M_3$ produce 50%, 30%, 20% of items with defect rates 2%, 3%, 5%. A defective item is found. Find the probability it came from each machine.

4. **Spam.** 40% of email is spam. The word "prize" appears in 50% of spam and 5% of non-spam. Find $P(\text{spam}\mid\text{"prize"})$.

5. **Two tests.** Using the test of Problem 1 twice, with results independent given the true status, find $P(\text{disease}\mid++)$. Verify by updating sequentially.

6. **Natural frequencies.** Redo Problem 1 by imagining 10,000 people and counting.

7. **Prosecutor's fallacy.** A DNA profile matches a suspect; a random innocent person matches with probability $0.001$. The suspect was one of 100,000 equally likely candidates, exactly one of whom is guilty. Find $P(\text{guilty}\mid\text{match})$ and comment on the statement "there is a 99.9% chance he is guilty".

8. **Monty Hall.** You pick door A. The host, who knows where the car is, opens door C showing a goat (choosing at random when he has a choice). Find the probability that the car is behind B.

## Solutions

### Solution 1

Let $D$ = disease, $+$ = positive test.

$$P(+)=0.90(0.01)+0.08(0.99)=0.009+0.0792=0.0882.$$

$$P(D\mid+)=\frac{0.009}{0.0882}\approx0.102.$$

Only about 10% of positives truly have the disease.

### Solution 2

$$P(+)=0.90(0.20)+0.08(0.80)=0.18+0.064=0.244,\qquad P(D\mid+)=\frac{0.18}{0.244}\approx0.738.$$

The posterior depends on the prior. When the disease is rare, the large healthy population produces many false positives relative to the few true positives; at higher prevalence the true positives dominate.

### Solution 3

From the total probability $P(D)=0.029$:

$$P(M_1\mid D)=\frac{0.02(0.5)}{0.029}=\frac{0.010}{0.029}\approx0.345,$$

$$P(M_2\mid D)=\frac{0.009}{0.029}\approx0.310,\qquad P(M_3\mid D)=\frac{0.010}{0.029}\approx0.345.$$

These sum to 1. Machine 3 makes only 20% of items but accounts for about 34.5% of defects.

### Solution 4

$$P(\text{prize})=0.5(0.4)+0.05(0.6)=0.20+0.03=0.23,$$

$$P(\text{spam}\mid\text{prize})=\frac{0.20}{0.23}\approx0.870.$$

### Solution 5

Joint likelihoods: $P(++\mid D)=0.9^2=0.81$ and $P(++\mid D^c)=0.08^2=0.0064$.

$$P(D\mid++)=\frac{0.81(0.01)}{0.81(0.01)+0.0064(0.99)}=\frac{0.0081}{0.0081+0.006336}=\frac{0.0081}{0.014436}\approx0.561.$$

Sequential check: after the first positive, the posterior is $0.102$ (odds $0.102/0.898\approx0.1136$). The likelihood ratio of a positive is $0.9/0.08=11.25$, so the new odds are $0.1136\times11.25\approx1.278$ and the probability is $1.278/2.278\approx0.561$.

### Solution 6

Out of 10,000 people: 100 have the disease, 9,900 do not.

- Diseased who test positive: $0.9\times100=90$.
- Healthy who test positive: $0.08\times9900=792$.

$$P(D\mid+)=\frac{90}{90+792}=\frac{90}{882}\approx0.102.$$

### Solution 7

Prior $P(G)=10^{-5}$, $P(\text{match}\mid G)=1$, $P(\text{match}\mid G^c)=0.001$.

$$P(G\mid\text{match})=\frac{1\cdot10^{-5}}{10^{-5}+0.001(1-10^{-5})}\approx\frac{0.00001}{0.0010100}\approx0.0099.$$

Equivalently, among 100,000 people we expect about $100$ innocent matches plus the guilty one, so the chance that a matching person is guilty is about $1/101\approx1\%$. The statement "99.9% chance of guilt" confuses $P(\text{match}\mid\text{innocent})=0.001$ with $P(\text{innocent}\mid\text{match})$ and ignores the prior.

### Solution 8

Let the car be behind A, B, or C with probability $1/3$ each. Likelihood that the host opens C:

- car at A: host chooses between B and C at random, $P=\frac12$;
- car at B: host must open C, $P=1$;
- car at C: host cannot open C, $P=0$.

$$P(\text{car at B}\mid\text{host opens C})=\frac{\frac13\cdot1}{\frac13\cdot\frac12+\frac13\cdot1+\frac13\cdot0}=\frac{1}{1.5}=\frac23.$$

Switching wins with probability $2/3$, staying with $1/3$.
