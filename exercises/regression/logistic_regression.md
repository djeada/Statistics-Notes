# Logistic Regression Exercises

Read [Logistic Regression](../../notes/regression/logistic_regression.md) first. Solutions are at the end.

## Problems

1. Convert between probability, odds and log-odds: (a) $p=0.8$; (b) logit $=-1.2$.
2. In the note's example, $\hat\beta_1=0.618$ per hour studied. Compute the odds ratio for one hour and for five extra hours, holding practice exams fixed.
3. Using $\hat\beta=(-4.530,\,0.618,\,0.613)$ from the note, compute the predicted pass probability for a student with 5 hours and 2 practice exams, and for one with 7 hours and 3 practice exams.
4. A one-predictor model has $\hat\beta_0=-3$, $\hat\beta_1=0.5$. (a) At what $x$ is $p=0.5$? (b) Find $p$ at $x=8$. (c) Compare the increase in probability when $x$ goes from 6 to 7 with the increase from 2 to 3. What does that say about the effect of $x$ on the probability scale?
5. For $x=(0,1,2,3)$, $y=(0,1,0,1)$ and $\beta=(-1,1)$, compute each predicted probability and the log-likelihood.
6. For an intercept-only logistic model with 6 successes among 10 trials, perform one Newton-Raphson step from $\beta_0^{(0)}=0$ and compare with the exact MLE.
7. For the note's example, the first Newton step from $\boldsymbol\beta=\mathbf 0$ needs $\mathbf g=\mathbf X^\top(\mathbf y-\mathbf p)$. Compute $\mathbf g$ using $\mathbf y=(0,0,0,1,0,1,0,1,1,1)$, hours $=1,\dots,10$, and exams $=(0,1,2,3,0,2,3,1,4,2)$.
8. With the 0.5 threshold the note's model classifies 10 students with TP=4, TN=4, FP=1, FN=1. Compute accuracy, precision, recall and F1. If the threshold is lowered to 0.4 (fitted probabilities: 0.020, 0.064, 0.190, 0.445, 0.192, 0.600, 0.837, 0.736, 0.970, 0.947 for students 1 to 10, with $y=(0,0,0,1,0,1,0,1,1,1)$), recompute these four metrics.
9. In a 2x2 table, 30 of 100 exposed subjects and 10 of 100 unexposed subjects have the event. Compute the odds in each group, the odds ratio, and the logistic regression coefficient for the exposure indicator.
10. Data: $x=(1,2,3,4)$, $y=(0,0,1,1)$. Explain why the MLE does not exist, and what practical symptoms you would see in software.
11. Explain why a linear model for a binary response is unsatisfactory and what role the logit link plays. Why can we not interpret $\beta_j$ as a change in probability?

## Solutions

**1.** (a) Odds $=0.8/0.2=4$, log-odds $=\ln4\approx1.386$. (b) Odds $=e^{-1.2}\approx0.301$, $p=\frac{1}{1+e^{1.2}}\approx0.2315$.

**2.** One hour: $e^{0.618}\approx1.855$. Five hours: $e^{5\times0.618}=e^{3.09}\approx21.98$ (equivalently $1.855^5$); odds multiply, they do not add.

**3.** (5,2): $z=-4.530+0.618(5)+0.613(2)=-4.530+3.090+1.226=-0.214$, $p=1/(1+e^{0.214})\approx0.447$. (7,3): $z=-4.530+4.326+1.839=1.635$, $p=1/(1+e^{-1.635})\approx0.837$.

**4.** (a) $p=0.5$ when $-3+0.5x=0$, so $x=6$. (b) $z=-3+4=1$, $p=1/(1+e^{-1})\approx0.731$. (c) From 6 to 7: $z$ goes $0\to0.5$, $p$ goes $0.5\to0.622$, an increase of $0.122$. From 2 to 3: $z$ goes $-2\to-1.5$, $p$ goes $0.119\to0.182$, an increase of $0.063$. The same one-unit change in $x$ (constant change of $0.5$ in log-odds) produces a larger probability change near $p=0.5$ than near the tails.

**5.** $z=(-1,0,1,2)$, $p=(0.269,0.5,0.731,0.881)$. Log-likelihood contributions: $y=0$ with $p=0.269$: $\ln(0.731)=-0.313$; $y=1$ with $p=0.5$: $\ln0.5=-0.693$; $y=0$ with $p=0.731$: $\ln(0.269)=-1.313$; $y=1$ with $p=0.881$: $\ln0.881=-0.127$. Sum $\ell\approx-2.447$.

**6.** At $\beta_0=0$, $p=0.5$. Gradient $g=\sum(y_i-p)=6-5=1$. Hessian $H=-\sum p(1-p)=-10(0.25)=-2.5$. Update $\beta_0^{(1)}=0-(-2.5)^{-1}(1)=0.4$. The exact MLE is $\ln(0.6/0.4)=\ln1.5\approx0.405$, so one step is already close.

**7.** At $\boldsymbol\beta=\mathbf0$, $y_i-p_i=\pm0.5$, so $\mathbf g=0.5\,\mathbf X^\top(2\mathbf y-1)$. Intercept: $0.5(5-5)=0$. Hours: passes have hours $4+6+8+9+10=37$, fails $1+2+3+5+7=18$, so $0.5(37-18)=9.5$. Exams: passes $3+2+1+4+2=12$, fails $0+1+2+0+3=6$, so $0.5(12-6)=3$. Hence $\mathbf g=(0,9.5,3)^\top$, matching the note.

**8.** Threshold 0.5: accuracy $=(4+4)/10=0.8$, precision $=4/5=0.8$, recall $=4/5=0.8$, $F1=0.8$. Threshold 0.4: predictions are 1 for students 4,6,7,8,9,10, so TP=5 (4,6,8,9,10), FP=1 (7), FN=0, TN=4. Accuracy $=9/10=0.9$, precision $=5/6\approx0.833$, recall $=5/5=1$, $F1=2(0.833)(1)/(1.833)\approx0.909$. Lowering the threshold raised recall at a small cost in precision.

**9.** Exposed odds $=30/70\approx0.429$; unexposed odds $=10/90\approx0.111$. $OR=0.429/0.111\approx3.857$. In a logistic regression with an exposure indicator, $\hat\beta_1=\ln3.857\approx1.350$ and $\hat\beta_0=\ln(0.111)\approx-2.197$.

**10.** The classes are separated perfectly by $x>2.5$. For $\beta=(-2.5k,k)$, every observation is classified correctly and its predicted probability tends to the observed class as $k\to\infty$, so $\ell$ increases toward 0 without a maximum; no finite MLE exists. In software you see enormous coefficients and standard errors, convergence warnings or perfect-separation warnings. Remedies: penalization (ridge or Firth), more data, or dropping the predictor.

**11.** A linear model can predict probabilities outside $[0,1]$ and has non-constant error variance $p(1-p)$ and non-normal errors. The logit link $\ln\frac{p}{1-p}=\mathbf x^\top\boldsymbol\beta$ maps $(0,1)$ to the real line, so any linear predictor gives a valid probability. Because $p$ is a nonlinear (S-shaped) function of the linear predictor, a unit change in $x_j$ changes the log-odds by $\beta_j$ (odds by factor $e^{\beta_j}$) while the change in probability depends on the current value of $p$ (see Problem 4).
