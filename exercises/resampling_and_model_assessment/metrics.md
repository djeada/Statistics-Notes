# Evaluation Metrics: Exercises

Read [Evaluation Metrics](../../notes/resampling_and_model_assessment/metrics.md) first. Scripts: [metrics.py](../../scripts/resampling_and_model_assessment/metrics.py), [classification_metrics.py](../../scripts/resampling_and_model_assessment/classification_metrics.py), [r_squared.py](../../scripts/resampling_and_model_assessment/r_squared.py).

## Problems

1. A classifier produces $TP=40$, $FN=10$, $FP=20$, $TN=130$. Compute accuracy, precision, recall, specificity and F1.
2. In a screening set of 1000 patients, 10 have the disease. A classifier predicts "healthy" for everyone. Compute accuracy, recall and specificity, and say what precision is. What does this show about accuracy?
3. Lowering the decision threshold of a probabilistic classifier from 0.5 to 0.3 changes which metrics, and in which direction (precision, recall, specificity)? Give one application where you would prefer to lower it and one where you would raise it.
4. For $y=(3,5,7,9)$ and $\hat y=(2.5,5.5,7,10)$ compute MAE, MSE, RMSE and $R^2$.
5. In Problem 4, suppose the first prediction is off by an extra 10 units (its error becomes $0.5+10$). Recompute MAE, MSE and RMSE and comment on outlier sensitivity.
6. For $y=(2,4,6,8,10)$ a model always predicts 8. Compute $R^2$ and interpret the sign.
7. A model with 4 predictors fitted on $n=30$ observations has $R^2=0.85$. Compute adjusted $R^2$.
8. Positives have scores $(0.9,0.8,0.6,0.4)$ and negatives $(0.7,0.5,0.3,0.2)$. (a) Give TPR and FPR at threshold 0.55 (predict positive if score $\ge$ threshold). (b) Compute the AUC as the probability a random positive outscores a random negative.
9. Show that $F_1=\dfrac{2\,TP}{2\,TP+FP+FN}$ and check it on Problem 1.

## Solutions

**1.** $n=200$. Accuracy $=(40+130)/200=0.85$. Precision $=40/(40+20)=2/3\approx0.667$. Recall $=40/50=0.8$. Specificity $=130/150\approx0.867$. $F_1=2\cdot\frac{0.667\cdot0.8}{0.667+0.8}=0.727$.

**2.** Predicting all negative gives $TP=0$, $FN=10$, $FP=0$, $TN=990$. Accuracy $=990/1000=0.99$. Recall $=0/10=0$. Specificity $=990/990=1$. Precision is $0/0$, undefined (conventionally set to 0). A 99% accurate classifier detects no disease at all, so accuracy is misleading under heavy imbalance.

**3.** A lower threshold labels more cases positive: recall rises (or stays equal) and specificity falls; precision usually falls because the extra positives are less certain. Lower it for screening for a serious, treatable disease where missing a case is costly; raise it for, e.g., automatic account suspension where false accusations are costly.

**4.** Errors $y-\hat y=(0.5,-0.5,0,-1)$. MAE $=(0.5+0.5+0+1)/4=0.5$. MSE $=(0.25+0.25+0+1)/4=0.375$. RMSE $=\sqrt{0.375}=0.612$. $\bar y=6$, $SS_{tot}=9+1+1+9=20$, $SS_{res}=1.5$, so $R^2=1-1.5/20=0.925$.

**5.** The first error becomes $10.5$ (the other errors are unchanged). MAE $=(10.5+0.5+0+1)/4=3.0$. MSE $=(110.25+0.25+0+1)/4=27.875$. RMSE $=5.28$. MAE rose by a factor of 6, MSE by a factor of about 74 and RMSE by about 8.6, so squared-error metrics are far more sensitive to the single large error.

**6.** $\bar y=6$, $SS_{tot}=16+4+0+4+16=40$. $SS_{res}=(2-8)^2+(4-8)^2+(6-8)^2+0+(10-8)^2=36+16+4+0+4=60$. $R^2=1-60/40=-0.5$. Negative: the constant 8 is worse than the mean 6, the $R^2=0$ benchmark.

**7.** $\bar R^2=1-(1-0.85)\frac{29}{30-4-1}=1-0.15\cdot\frac{29}{25}=1-0.174=0.826$.

**8.** (a) Scores $\ge0.55$: positives $0.9,0.8,0.6$ (3 of 4) and negatives $0.7$ (1 of 4). TPR $=3/4=0.75$, FPR $=1/4=0.25$. (b) Count pairs with positive $>$ negative: $0.9$ beats all 4, $0.8$ beats all 4, $0.6$ beats $0.5,0.3,0.2$ (3), $0.4$ beats $0.3,0.2$ (2). Total $13/16=0.8125$.

**9.** $F_1=\frac{2PR}{P+R}$ with $P=\frac{TP}{TP+FP}$, $R=\frac{TP}{TP+FN}$. Then $PR=\frac{TP^2}{(TP+FP)(TP+FN)}$ and $P+R=\frac{TP(TP+FN)+TP(TP+FP)}{(TP+FP)(TP+FN)}=\frac{TP(2TP+FP+FN)}{(TP+FP)(TP+FN)}$. Dividing gives $F_1=\frac{2TP^2}{TP(2TP+FP+FN)}=\frac{2TP}{2TP+FP+FN}$. Check: $80/(80+20+10)=80/110=0.727$.
