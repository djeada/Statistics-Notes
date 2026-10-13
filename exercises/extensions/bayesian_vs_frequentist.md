# Bayesian vs Frequentist Statistics

Read [Bayesian vs Frequentist Statistics](../../notes/extensions/bayesian_vs_frequentist.md) first. Solutions are at the end; numbers can be checked with [bayesian_vs_frequentist.py](../../scripts/extensions/bayesian_vs_frequentist.py) and the [notebook](../../notebooks/extensions/bayesian_vs_frequentist.ipynb).

1. A sample of $n=4$ items has $x=2$ successes. Compute the 95% Wald interval for $p$ and the 95% Wilson interval. Which would you trust more, and why?
2. A coin is flipped $n=10$ times and shows $x=7$ heads. With a $\mathrm{Beta}(1,1)$ prior, give the posterior, the posterior mean, the posterior mode, and the posterior standard deviation.
3. Using the posterior $\mathrm{Beta}(4,1)$ from the note (three heads in three flips, uniform prior), compute $P(p>0.5\mid D)$ in closed form.
4. Using the Jeffreys prior $\mathrm{Beta}(0.5,0.5)$ and the data in exercise 3, give the posterior and its mean. Compare with the posterior mean under $\mathrm{Beta}(1,1)$.
5. For the posterior in exercise 2, give the posterior predictive probability that the next flip is heads, and the probability that the next two flips are both heads.
6. Exact binomial test: 9 heads in 10 flips, $H_0:p=0.5$, two-sided. Compute the p-value and explain why it is not $P(H_0\mid\text{data})$.
7. Normal mean with known $\sigma=5$: $n=25$, $\bar x=10$, prior $\mu\sim N(8,2^2)$. Find the posterior mean, standard deviation, and 95% credible interval, then the 95% confidence interval, and compare.
8. A $\mathrm{Beta}(20,20)$ prior is used for the coin of exercise 3 (three heads in three flips). Find the posterior mean and the 95% credible interval, and interpret $a+b$ as a prior sample size.
9. (Conceptual) A 95% confidence interval is $(4.44,5.15)$ and a 95% credible interval is $(4.42,5.18)$. State, for each, what the 95% refers to.
10. (Conceptual) List two situations where a Bayesian and a frequentist analysis of the same data would differ noticeably, and one where they would nearly agree.

## Solutions

**1.** $\hat p=0.5$, $SE=\sqrt{0.5\cdot0.5/4}=0.25$. Wald: $0.5\pm1.96(0.25)=0.5\pm0.49=[0.01,0.99]$.
Wilson: $z^2=3.8416$, $z^2/n=0.9604$, denominator $1+0.9604=1.9604$. Centre $=(0.5+3.8416/8)/1.9604=(0.5+0.4802)/1.9604=0.5$. Half-width $=\dfrac{1.96\sqrt{0.0625+3.8416/64}}{1.9604}=\dfrac{1.96\sqrt{0.122525}}{1.9604}=\dfrac{1.96(0.35004)}{1.9604}\approx0.350$. Wilson interval $\approx[0.150,0.850]$. Wilson is preferable: its actual coverage is much closer to nominal for small $n$, whereas the Wald interval relies on a normal approximation that is poor with $n=4$.

**2.** Posterior $\mathrm{Beta}(1+7,1+3)=\mathrm{Beta}(8,4)$. Mean $=8/12=0.667$. Mode $=(a-1)/(a+b-2)=7/10=0.7$. Variance $=\dfrac{ab}{(a+b)^2(a+b+1)}=\dfrac{32}{144\cdot13}=0.01709$, so SD $\approx0.131$.

**3.** The $\mathrm{Beta}(4,1)$ CDF is $F(p)=p^4$. So $P(p>0.5\mid D)=1-0.5^4=1-0.0625=0.9375$.

**4.** Posterior $\mathrm{Beta}(0.5+3,\,0.5+0)=\mathrm{Beta}(3.5,0.5)$, mean $3.5/4=0.875$. The uniform prior gave $4/5=0.8$. The Jeffreys prior is less conservative (adds only one pseudo-observation in total instead of two), so the mean is pulled less toward $0.5$.

**5.** Next flip: $E[p\mid D]=8/12=2/3\approx0.667$. Two heads: $E[p^2\mid D]=\dfrac{a(a+1)}{(a+b)(a+b+1)}=\dfrac{8\cdot9}{12\cdot13}=\dfrac{72}{156}=0.4615$. This is larger than $(2/3)^2=0.444$ because the parameter uncertainty is retained: $E[p^2]=E[p]^2+\mathrm{Var}(p)=0.4444+0.0171$.

**6.** Under $H_0$, $X\sim\mathrm{Bin}(10,0.5)$. $P(X\ge9)=(10+1)/1024=11/1024$. Two-sided doubles it: $22/1024=0.0215$. This is the probability of data at least this extreme if $H_0$ and the model are true; it is not the probability that $H_0$ is true, which would additionally require a prior on $H_0$ and its alternatives.

**7.** Prior precision $1/4=0.25$; data precision $n/\sigma^2=25/25=1$. Posterior precision $=1.25$, variance $=0.8$, SD $=0.894$. Mean $=(0.25\cdot8+1\cdot10)/1.25=12/1.25=9.6$. Credible interval $9.6\pm1.96(0.894)=[7.85,11.35]$. Confidence interval: $SE=5/\sqrt{25}=1$, $10\pm1.96=[8.04,11.96]$. The posterior is shrunk toward the prior mean $8$ and is narrower, since the prior adds information (weight $0.8$ on the data, $0.2$ on the prior).

**8.** Posterior $\mathrm{Beta}(23,20)$, mean $23/43=0.535$; 95% credible interval $\approx[0.387,0.680]$. The prior acts like $a+b=40$ pseudo-observations, far outweighing 3 real ones, so the three heads barely move the estimate from $0.5$. Compare $0.8$ under the uniform prior.

**9.** Confidence interval: the procedure that generated it captures the true mean in 95% of repeated samples (the fixed true mean is either in this particular interval or not). Credible interval: given the model, prior and observed data, the posterior probability that the mean lies in $(4.42,5.18)$ is $0.95$.

**10.** Differ: very small samples (exercises 1-4 and 8, where the prior matters) and strong informative priors or hierarchical models/parameters near boundaries. Nearly agree: large samples from a regular model with a weak prior, where the likelihood dominates (e.g. the $n=100$ normal-mean example with 4.79 vs 4.80). Even then the interpretations differ.
