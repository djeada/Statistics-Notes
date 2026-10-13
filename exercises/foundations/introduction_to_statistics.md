# Introduction to Statistics: Exercises

Practice for the note [Introduction to Statistics](../../notes/foundations/introduction_to_statistics.md).

## Problems

1. **Variable types.** Classify each variable as nominal, ordinal, discrete numerical, or continuous numerical: (a) blood type, (b) number of siblings, (c) customer satisfaction on the scale poor/fair/good/excellent, (d) time to run 5 km, (e) postal code, (f) number of defects per batch.

2. **Parameter or statistic.** A factory produces 5,000 bulbs in a day. An inspector tests 50 of them and finds a mean lifetime of 1,180 hours with 3 defective bulbs. Identify the population, the sample, two statistics, and a parameter that could be estimated.

3. **Identifying bias.** Name the main source of bias in each scenario: (a) a phone-in poll about a TV show; (b) a survey of mutual-fund performance that includes only funds still operating today; (c) 40% of mailed questionnaires are returned, mostly by people with strong opinions; (d) a scale that always reads 2 kg too high.

4. **Sampling designs.** A school has 1,000 students: 600 undergraduates and 400 graduate students. (a) How many of each should a proportional stratified sample of 100 contain? (b) For a systematic sample of 50 students, what is the sampling interval $k$?

5. **Estimating.** Five randomly selected adults have incomes (in thousands) $42,55,48,61,39$. Compute the sample mean and sample standard deviation. In a separate survey, 18 of 120 respondents said they use public transport; compute $\hat p$.

6. **Explanatory and response.** A study records weekly hours of exercise and resting heart rate for 200 adults. Identify the explanatory and response variables. If the data are observational and heavier exercisers also tend to be younger, what is the role of age?

7. **Random assignment.** An agronomist has 12 plots and wants to give fertilizer to exactly 6 of them chosen at random. How many different assignments are possible? What is the probability that a particular set of 6 plots receives fertilizer?

8. **Sampling versus assignment.** Explain the difference between random sampling and random assignment, and say which one supports generalization to a population and which supports causal conclusions.

## Solutions

### Solution 1

(a) Nominal: categories without order.
(b) Discrete numerical: counts $0,1,2,\ldots$.
(c) Ordinal: ordered categories with unequal or unknown spacing.
(d) Continuous numerical: any value in an interval (recorded with finite precision).
(e) Nominal: it is an identifier made of digits, and arithmetic on it is meaningless.
(f) Discrete numerical: a count.

### Solution 2

- Population: all 5,000 bulbs produced that day (or the production process).
- Sample: the 50 bulbs tested.
- Statistics: the sample mean $\bar{x}=1180$ hours and the sample proportion defective $\hat p=3/50=0.06$.
- Parameters estimated: the population mean lifetime $\mu$ and the population proportion defective $p$.

### Solution 3

(a) Selection (self-selection, voluntary response) bias: those who call in differ from the audience.
(b) Survivorship bias: failed funds are missing, so performance looks better than it was.
(c) Non-response bias: respondents differ systematically from non-respondents.
(d) Measurement bias: the instrument systematically produces values different from the true quantity.

### Solution 4

(a) Proportional allocation: $100\cdot\frac{600}{1000}=60$ undergraduates and $100\cdot\frac{400}{1000}=40$ graduate students.
(b) $k=\frac{N}{n}=\frac{1000}{50}=20$: choose a random start between 1 and 20 and take every 20th student.

### Solution 5

Mean: $\bar{x}=\frac{42+55+48+61+39}{5}=\frac{245}{5}=49$.

Deviations: $-7,\;6,\;-1,\;12,\;-10$. Squares: $49,36,1,144,100$, sum $=330$.

$$s^2=\frac{330}{4}=82.5,\qquad s=\sqrt{82.5}\approx9.08.$$

Proportion: $\hat p=\frac{18}{120}=0.15$.

### Solution 6

Explanatory variable: weekly hours of exercise. Response variable: resting heart rate. Age is a potential **confounder**: it is associated with both exercise (explanatory) and heart rate (response), so an observed association cannot be attributed to exercise alone without adjusting for age or randomizing.

### Solution 7

The number of ways to choose 6 plots out of 12 is

$$\binom{12}{6}=\frac{12!}{6!\,6!}=\frac{12\cdot11\cdot10\cdot9\cdot8\cdot7}{6\cdot5\cdot4\cdot3\cdot2\cdot1}=\frac{665{,}280}{720}=924.$$

Under random assignment each is equally likely, so a particular set has probability $1/924\approx0.00108$.

### Solution 8

Random **sampling** determines who enters the study; it supports generalizing from the sample to the population (external validity). Random **assignment** determines which treatment each participant receives; it balances confounders across groups and supports causal conclusions about the treatment (internal validity). A study can have one without the other.
