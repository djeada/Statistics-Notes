# Theory: false alarms and detection performance

## Why an alert rule must be judged on both errors

Every detector can be made to catch all faults by alarming all the time, or to never raise a false alarm by never alarming. A rule is only
useful for the point it sets between those extremes. Judging it by "it caught the fault" or "it rarely fires" alone hides half of the
story and leads to alert fatigue (people stop reacting) or silent failures. To choose a threshold responsibly you need labelled history, a
vocabulary for the four outcomes, and a way to put prices on them.

## The confusion matrix

Compare the alarm with the truth for every reading:

| | fault | healthy |
|---|---|---|
| **alarm** | TP (true positive) | FP (false alarm) |
| **no alarm** | FN (miss) | TN |

Definitions (all conditional proportions):

$$\text{precision}=\frac{TP}{TP+FP},\qquad \text{recall (TPR)}=\frac{TP}{TP+FN},\qquad \text{FPR}=\frac{FP}{FP+TN},\qquad
F_1=\frac{2\,\text{precision}\cdot\text{recall}}{\text{precision}+\text{recall}} .$$

Recall and FPR condition on the **truth** (how the detector treats faults and healthy readings); precision conditions on the **alarm**
(how trustworthy an alert is). Worked example with $TP=8,\,FP=4,\,FN=2,\,TN=86$: precision $=8/12=0.667$, recall $=8/10=0.800$,
FPR $=4/90=0.044$, $F_1=2(0.667)(0.8)/(1.467)=0.727$. $F_1$ is a harmonic mean, so it is low whenever either component is low; it
ignores TN completely.

## Sweeping the threshold

For a score $s_t$ and threshold $T$ the detector alarms when $s_t\ge T$. Raising $T$ lowers FP and TP together. Evaluating many
thresholds traces:

- the **ROC curve**: recall against FPR. The diagonal is a coin flip; area under the curve (AUC) is the probability that a random fault
  scores higher than a random healthy reading. AUC is independent of the threshold and of prevalence.
- the **precision-recall curve**: preferable when faults are rare, because it shows what fraction of alarms are real.

The threshold is a decision, not an estimate: pick it by expected cost, $\text{cost}(T)=c_{FN}\,FN(T)+c_{FP}\,FP(T)$, or by a constraint such as
"recall at least 80 %" or "at most one false alarm per day".

## Base-rate fallacy

If faults are rare, even a detector with a small FPR produces mostly false alarms. By Bayes' theorem
([conditional probability](../../notes/probability/bayes_theorem.md))

$$\text{precision}=\frac{\text{recall}\cdot\pi}{\text{recall}\cdot\pi+\text{FPR}\cdot(1-\pi)},\qquad \pi=\text{prevalence}.$$

Worked example: recall 0.90, FPR 0.02, $\pi=1\,\%$. Per 1000 readings there are $1000\cdot0.01\cdot0.9=9$ true alarms and
$1000\cdot0.99\cdot0.02=19.8$ false ones, so precision is $9/28.8=31\,\%$. The same detector at $\pi=20\,\%$ has precision 92 %. Judge a
detector in the prevalence in which it will run; precision and F1 do not transfer, but recall and FPR do.

## Time-series specifics: ARL and delay

Sensors produce a stream, so two operational quantities matter more than FPR per reading:

- **ARL0**, the average run length between false alarms, $\approx 1/\text{FPR}$ readings when alarms are independent. An FPR of 1 % per hourly
  reading is one false alarm every four days.
- **Detection delay**, the number of faulty readings before the first alarm in an episode. Evaluate by **episode** (was the incident
  caught, and how late?) as well as by reading; a 6-hour fault with 5 alarms counts once as an incident but five times in TP.

Delay and ARL0 trade off exactly as in [lesson 27](../27-change-point-detection/theory.md): lowering the false-alarm rate lengthens the delay.

## Assumptions and pitfalls

1. **Labels are the ceiling.** Late, partial or wrong labels bias every metric; an unlabelled real fault counts as a false alarm.
2. **Tuning on the evaluation data is optimistic.** Choose $T$ on one period and report on another
   ([backtesting, lesson 24](../24-backtesting-and-forecast-accuracy/theory.md)).
3. **Prevalence shifts** (a new line, a bad batch) change precision without any change to the detector.
4. **Reading-level vs episode-level metrics** answer different questions; state which one you report.
5. **Accuracy is a trap**: with 5 % faults, "never alarm" has 95 % accuracy and recall 0.
6. **The score model matters more than the threshold.** If the set-point model is wrong at transitions the false alarms come in at specific hours;
   see [lesson 28](../28-time-series-anomaly-detection/theory.md).
7. **Alarms correlate**: consecutive hours are not independent, so ARL0 from a rate is only a rough guide.

## Related notes

- [Outlier detection](../04-outlier-detection/theory.md), [statistical process control](../26-statistical-process-control/theory.md)
- [Permutation tests](../18-permutation-tests/theory.md) for judging whether a difference in detection rate between two rules is real
- Repo notes: [Bayes' theorem](../../notes/probability/bayes_theorem.md)
