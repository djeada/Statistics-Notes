# Spatial Validation Exercises

Use this problem set with the [chapter notes](../../notes/spatial_statistics/spatial_validation.md) and the [visualization script](../../scripts/spatial_statistics/spatial_validation_visualizations.py).


## Exercise 1: RMSE

Observed values are

$$
5,\ 7,\ 8,\ 10
$$

and predictions are

$$
6,\ 6,\ 9,\ 11.
$$

Calculate RMSE.

---

## Exercise 2: nearest-training distance

A test point is at coordinate

$$
(4,3).
$$

Training points are

$$
(0,0),\ (4,0),\ (10,3).
$$

Calculate the nearest Euclidean training distance.

---

## Exercise 3: buffer

A test block has three nearby training observations at distances

$$
0.8,\ 1.4,\ 2.7\text{ km}.
$$

Which remain if the buffer is

$$
b=1.5\text{ km}?
$$

---

## Exercise 4: fold interpretation

Random CV gives RMSE 0.9.

Leave-region-out CV gives RMSE 2.4.

Give a scientifically reasonable explanation without saying one result must be wrong.

---

## Exercise 5: leakage

Explain why fitting a spatial interpolator for a predictor using all observations before cross-validation can leak information.

---

## Exercise 6: unsupported extrapolation

Training elevations range from 100 to 900 m.

Deployment will occur above 1800 m.

Explain why spatial block CV within the original dataset cannot fully validate this deployment.

---

## Worked solutions

### Solution 1

Errors $y-\hat y$: $5-6=-1,\ 7-6=1,\ 8-9=-1,\ 10-11=-1$. Squared errors: $1,1,1,1$; mean $=4/4=1$.

$$
\mathrm{RMSE}=\sqrt1=1.
$$

### Solution 2

Distances from $(4,3)$:

- to $(0,0)$: $\sqrt{16+9}=5$;
- to $(4,0)$: $\sqrt{0+9}=3$;
- to $(10,3)$: $\sqrt{36+0}=6$.

The nearest training distance is $d=\min(5,3,6)=3$, attained by $(4,0)$.

### Solution 3

Observations within the buffer $b=1.5$ km are removed: $0.8$ and $1.4$ km are dropped. Only the $2.7$ km observation remains. The nearest-training separation for this block therefore increases from $0.8$ km to $2.7$ km.

### Solution 4

Random CV (0.9) mostly asks the model to interpolate between sampled sites: held-out points have nearby training neighbors, and spatial dependence makes them easy to predict. Leave-region-out CV (2.4) removes whole regions, so the model must transfer to places without nearby data and with possibly different local conditions (unmodeled regional effects, different covariate ranges). Both are valid estimates of different tasks; the gap, $2.4/0.9\approx2.7$ times, measures how much of the skill depends on nearby training information. Which is relevant depends on whether deployment is gap-filling or prediction in new regions.

### Solution 5

Suppose the predictor is interpolated (e.g. kriged or smoothed) from all sites before splitting. The interpolated value at a training site then incorporates the held-out sites' values, so the training features encode information about the test observations (and vice versa). If the predictor is derived from the outcome or correlated with it, the model has indirectly seen the test data and the CV error is optimistic. The interpolator must be refit within each training fold and applied to the test locations using training data only.

### Solution 6

Spatial blocks only rearrange the observations that exist, all of which lie between 100 and 900 m. No fold contains conditions above 1800 m, so the model's behavior there (new climate, vegetation, nonlinear responses) is never tested. This is extrapolation in covariate space; block CV can only validate transfer within the observed range. Evidence must come from additional data at high elevations, a mechanistic argument, or at least a clearly labelled, unvalidated extrapolation with uncertainty caveats.
