# Validation and Model Selection: Exercises

Read [Validation and Model Selection](../../notes/resampling_and_model_assessment/validation_and_model_selection.md) first. Script: [validation_and_model_selection.py](../../scripts/resampling_and_model_assessment/validation_and_model_selection.py).

## Problems

1. Five-fold CV gives fold MSEs $(2.1,1.8,2.4,2.0,1.7)$. Compute the CV estimate and the standard error of the mean of the folds. Why is this standard error only approximate?
2. With $n=1000$, state the training and test sizes per fold for 5-fold CV, 10-fold CV and leave-one-out CV, and the number of model fits each needs.
3. A pipeline standardizes all 100 features using the whole dataset and then runs 5-fold CV. Name the leak and give the correct procedure. Is it more serious for $n=50$ or $n=5000$?
4. Nested CV uses 5 outer folds, 3 inner folds and a grid of 8 hyperparameter values. How many model fits are needed, counting one final refit per outer fold?
5. In a regression task the training mean is 10, and the test responses are $(8,12,13,9)$. Compute the test MSE of the mean baseline. A model has test MSE 1.5; is it useful?
6. Ten candidate models have the same true error. Each is scored on a 50-observation validation set and you keep the best score. Explain why that best score is optimistic and what to do.
7. For a monthly series of $n=12$ observations, list the splits of an expanding-window scheme with initial window 6 and horizon 2, stepping by 2.
8. CV MSEs for polynomial degrees 1 to 5 are $(3.2,2.1,2.0,2.05,2.2)$, each with standard error 0.15. Which degree does the minimum rule choose and which does the one-standard-error rule choose?
9. Describe three differences between choosing a model for prediction and choosing one for scientific explanation.

## Solutions

**1.** Mean $=(2.1+1.8+2.4+2.0+1.7)/5=10/5=2.0$. Deviations $0.1,-0.2,0.4,0,-0.3$; squares $0.01+0.04+0.16+0+0.09=0.30$; $s=\sqrt{0.30/4}=0.274$; $SE=0.274/\sqrt5=0.122$. It is approximate because folds share training data, so fold scores are positively correlated and not independent; the true uncertainty is larger.

**2.** 5-fold: train 800, test 200, 5 fits. 10-fold: train 900, test 100, 10 fits. LOOCV: train 999, test 1, 1000 fits.

**3.** Test-fold information (means and variances) leaks into the training transformation. Correct: fit the scaler on the training folds only inside each split (a pipeline). The effect is larger when $n$ is small relative to the number of features, so $n=50$.

**4.** Per outer fold: inner search $3\times8=24$ fits plus 1 refit $=25$. Total $5\times25=125$ fits.

**5.** Errors $(8-10,12-10,13-10,9-10)=(-2,2,3,-1)$; squares $4+4+9+1=18$; MSE $=18/4=4.5$. Test MSE 1.5 is much lower than 4.5, so the model beats the baseline (about 67% reduction), which is useful evidence.

**6.** The maximum of ten noisy scores is biased upward: even with equal true error, the winner is the one with the luckiest validation draw. Report performance on a fresh test set (or nested CV), not the winning validation score.

**7.** Train $1$-$6$, test $7$-$8$; train $1$-$8$, test $9$-$10$; train $1$-$10$, test $11$-$12$. Training windows always end before the test block.

**8.** The minimum rule picks degree 3 (2.0). Threshold $2.0+0.15=2.15$; the simplest model within it is degree 2 (2.1), so the one-SE rule picks degree 2.

**9.** For example: (i) prediction can use any informative variable, while explanation needs interpretable, theoretically justified terms; (ii) prediction tolerates correlated predictors and regularization bias, while explanation needs unbiased, interpretable coefficients; (iii) prediction is judged on held-out error, while explanation also requires causal assumptions (confounding, mechanism) that predictive score cannot verify.
