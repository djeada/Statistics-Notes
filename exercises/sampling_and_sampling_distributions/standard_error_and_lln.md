# Standard Error and the Law of Large Numbers Exercises

Read the note first: [Standard Error and Law of Large Numbers](../../notes/sampling_and_sampling_distributions/standard_error_and_lln.md). Solutions are at the end of this file.

## Problems

1. A population has $\sigma=12$. Find the standard error of the sample mean for $n=36$. What sample size gives a standard error of $1$? By what factor must $n$ grow to halve the standard error?
2. Draws are made independently from a box with mean $\mu=3$ and standard deviation $\sigma=1.5$. For $n=100$ draws, find the expected value and standard error of the sum, and use the normal approximation to estimate $P(S_{100}>330)$.
3. A population has $30\%$ successes. Find the expected value and standard error of the percentage of successes in a sample of $n=400$.
4. For a population with $50\%$ successes, how large must $n$ be so that the standard error of the sample percentage is at most $1$ percentage point?
5. Take $\mu=20$ and $\sigma=4$. Compare $n=16$ and $n=64$: the standard error of the mean, the standard error of the sum, and the standard error of the sum relative to its expected value. Why does the LLN apply to the mean but not to the sum?
6. A fair coin lands heads in the first $10$ tosses. A friend says tails are "due". Using the LLN correctly, what is the expected proportion of heads after $1{,}000$ tosses in total?
7. A population of $N=1000$ has $\sigma=10$. A sample of $n=100$ is drawn without replacement. Compute the standard error of the mean with and without the finite population correction.
8. Use Chebyshev's inequality to bound $P(|\bar X_n-\mu|>0.5)$ when $\sigma=2$ and $n=400$. Is the bound close to the normal-approximation value?
9. The Cauchy distribution has no mean. What does the LLN say about the sample mean of Cauchy data, and what would a running-mean plot look like?

## Solutions

**1.** $SE=\sigma/\sqrt n=12/6=2$. For $SE=1$: $\sqrt n=12$, so $n=144$. To halve the SE, $\sqrt n$ must double, so $n$ must be multiplied by $4$ (inverse square-root law).

**2.** $E[S]=n\mu=100\cdot3=300$ and $SE(S)=\sqrt n\,\sigma=10\cdot1.5=15$. Standardizing: $z=(330-300)/15=2$, so $P(S>330)\approx1-\Phi(2)=0.0228$.

**3.** Expected percentage $=30\%$. $\sigma=\sqrt{0.3\cdot0.7}=\sqrt{0.21}=0.4583$. $SE=0.4583/\sqrt{400}=0.4583/20=0.02291$, i.e. $2.29\%$.

**4.** $\sigma=\sqrt{0.5\cdot0.5}=0.5$. Require $0.5/\sqrt n\le0.01$, so $\sqrt n\ge50$ and $n\ge2500$.

**5.** Mean: $SE=4/\sqrt{16}=1$ and $4/\sqrt{64}=0.5$. Sum: $SE=\sqrt{16}\cdot4=16$ and $\sqrt{64}\cdot4=32$; $E[S]=320$ and $1280$. Relative: $16/320=0.05$ and $32/1280=0.025$. The mean converges to $\mu$ (its spread shrinks like $1/\sqrt n$), but the sum has expected value $n\mu\to\infty$ and absolute spread $\sqrt n\sigma\to\infty$, so the sum does not settle on a number; only the sum relative to its size (equivalently the mean) stabilizes.

**6.** Future tosses are independent and fair, so in the remaining $990$ tosses we expect $495$ heads. Total expected heads $=10+495=505$, a proportion $0.505$. The $5$-head excess is not corrected; it is diluted. The LLN is about the proportion converging, not about the count being compensated.

**7.** Without correction: $10/\sqrt{100}=1$. Correction factor $\sqrt{(N-n)/(N-1)}=\sqrt{900/999}=0.9492$, so $SE=0.949$.

**8.** Chebyshev: $P(|\bar X-\mu|>\varepsilon)\le\sigma^2/(n\varepsilon^2)=4/(400\cdot0.25)=0.04$. With $SE=2/20=0.1$, the normal approximation gives $z=0.5/0.1=5$ and $P\approx2\times2.9\times10^{-7}\approx5.7\times10^{-7}$. Chebyshev is valid for any distribution with finite variance but very conservative.

**9.** The LLN requires a finite mean, which the Cauchy lacks, so there is no $\mu$ to converge to. In fact the mean of $n$ i.i.d. standard Cauchy variables is again standard Cauchy for every $n$, so the running mean never settles: it keeps making occasional large jumps no matter how many observations are included.
