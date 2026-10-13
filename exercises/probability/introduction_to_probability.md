# Introduction to Probability: Exercises

Practice for the note [Introduction to Probability](../../notes/probability/introduction_to_probability.md).

## Problems

1. **Sample space.** A fair coin is flipped three times. List the sample space and find the probability of "at least two heads".

2. **Two dice.** Two fair dice are rolled. Find $P(\text{sum}=8)$, $P(\text{sum}\ge10)$, and $P(\text{both dice show the same number})$.

3. **Expected sum and maximum.** For two fair dice, find $E(\text{sum})$ and the expected value of the larger of the two numbers.

4. **Cards.** A card is drawn from a standard 52-card deck. Find (a) $P(\text{red face card})$, (b) $P(\text{rank between 5 and 9 inclusive})$, (c) $P(\text{neither a heart nor a face card})$.

5. **Balls in cells.** Two balls are placed in three cells. (a) If the balls are distinguishable and every placement is equally likely, find $P(\text{both in the same cell})$ and $P(\text{cell 1 is empty})$. (b) If the balls are indistinguishable and the resulting arrangements are treated as equally likely, find $P(\text{both in the same cell})$. Why do the answers differ?

6. **Equally likely?** Someone argues that the sum of two dice has 11 possible values, so each has probability $1/11$. Explain what is wrong and give the correct value of $P(12)$ and $P(7)$.

7. **Expected value of a game.** A fair die is rolled. If the result is even you win that many dollars; if it is odd you lose 3 dollars. Find the expected gain.

8. **Unfair die.** A die has $P(1)=P(2)=0.1$ and $P(3)=P(4)=P(5)=P(6)=0.2$. Verify it is a valid model, then find $P(\text{even})$, $P(\ge5)$, and the expected value of the roll.

## Solutions

### Solution 1

$S=\{HHH,HHT,HTH,HTT,THH,THT,TTH,TTT\}$, 8 equally likely outcomes.

"At least two heads" $=\{HHH,HHT,HTH,THH\}$, 4 outcomes, so

$$P=\frac{4}{8}=\frac12.$$

### Solution 2

There are 36 equally likely ordered pairs.

- Sum 8: $(2,6),(3,5),(4,4),(5,3),(6,2)$, so $5/36\approx0.139$.
- Sum $\ge10$: sum 10 has 3 pairs, sum 11 has 2, sum 12 has 1, total 6, so $6/36=1/6$.
- Same number: $(1,1),\ldots,(6,6)$, 6 pairs, so $6/36=1/6$.

### Solution 3

$E(\text{sum})=\sum_s s\,P(s)=\frac{1}{36}\left(2\cdot1+3\cdot2+4\cdot3+5\cdot4+6\cdot5+7\cdot6+8\cdot5+9\cdot4+10\cdot3+11\cdot2+12\cdot1\right)$.

The bracket is $2+6+12+20+30+42+40+36+30+22+12=252$, so $E=252/36=7$.

For the maximum $M$: $M=k$ happens in $2k-1$ pairs (one pair $(k,k)$ and $2(k-1)$ pairs with exactly one die equal to $k$ and the other smaller). Then

$$E(M)=\frac{1}{36}\sum_{k=1}^{6}k(2k-1)=\frac{1}{36}(1+6+15+28+45+66)=\frac{161}{36}\approx4.472.$$

### Solution 4

(a) Red face cards: J, Q, K in hearts and diamonds $=6$, so $6/52=3/26\approx0.115$.

(b) Ranks 5, 6, 7, 8, 9 in 4 suits $=20$ cards, so $20/52=5/13\approx0.385$.

(c) Hearts $=13$, face cards $=12$, hearts that are face cards $=3$. Cards that are a heart or a face card: $13+12-3=22$. Neither: $52-22=30$, so $30/52=15/26\approx0.577$.

### Solution 5

(a) Distinguishable balls: $3\times3=9$ equally likely placements. Both in the same cell: 3 placements, so $3/9=1/3$. Cell 1 empty: both balls in cells 2 or 3, $2\times2=4$ placements, so $4/9$.

(b) Indistinguishable balls: arrangements are $\{2,0,0\},\{0,2,0\},\{0,0,2\}$ (both in the same cell) and $\{1,1,0\},\{1,0,1\},\{0,1,1\}$, 6 in total. Treated as equally likely, $P(\text{same cell})=3/6=1/2$.

The answers differ because the two models assign different probabilities to the same physical event. With distinguishable balls, "one ball in each of two cells" arises in 2 ways ($ab$ and $ba$), so the 6 arrangements are not equally likely. Equal likelihood is a modeling assumption and must be justified.

### Solution 6

The 11 sums are not equally likely because they arise from different numbers of the 36 equally likely ordered pairs. The correct probabilities are $P(7)=6/36=1/6$ and $P(12)=1/36$, not $1/11\approx0.091$ for each. (Note that $P(7)=0.167$ compared with $1/11=0.091$.)

### Solution 7

Outcomes: 2, 4, 6 win $2$, $4$, $6$; outcomes 1, 3, 5 lose 3 (gain $-3$). Each has probability $1/6$.

$$E=\frac{2+4+6}{6}+\frac{3\cdot(-3)}{6}=2-1.5=0.5.$$

The expected gain is $+\$0.50$ per play.

### Solution 8

Total: $0.1+0.1+4(0.2)=1.0$ and all values are nonnegative, so the model is valid.

- $P(\text{even})=P(2)+P(4)+P(6)=0.1+0.2+0.2=0.5$.
- $P(\ge5)=0.2+0.2=0.4$.
- $E=1(0.1)+2(0.1)+3(0.2)+4(0.2)+5(0.2)+6(0.2)=0.1+0.2+0.6+0.8+1.0+1.2=3.9$.
