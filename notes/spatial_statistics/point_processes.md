# Point Processes

A spatial point process models a random collection of event locations. The observed object is not a value attached to a fixed site; the **number and positions of events are random**.

Examples include tree stems, earthquake epicenters, disease cases, nests, stores, or incidents observed inside a study window $W$.

## Counting Measure

For region $B\subseteq W$,

$$
N(B)
=
\text{number of observed events in } B
$$

is a random variable.

The point process can therefore be viewed as a random counting measure.

## First-Order Structure: Intensity

The intensity $\lambda(s)$ describes expected event density:

$$
E[N(B)]
=
\int_B \lambda(s)\,ds.
$$

For a homogeneous process,

$$
\lambda(s)=\lambda
$$

and

$$
E[N(B)]=\lambda |B|.
$$

If intensity changes with environmental covariates or location, apparent clustering can arise even when events are conditionally independent given that intensity.

This is the point-process analogue of separating mean trend from residual dependence.

## Homogeneous Poisson Process and CSR

For a homogeneous Poisson point process:

1. counts in disjoint regions are independent;
2. for region $B$,

$$
N(B)\sim\operatorname{Poisson}(\lambda |B|);
$$

3. conditional on $N(W)=n$, the $n$ locations are independent and uniform over $W$.

A simulation that fixes $n$ first and samples $n$ uniform locations is therefore a simulation from the **Poisson process conditional on its count**, not a full unconditional homogeneous Poisson-process simulation.

The companion [`point_pattern_analysis.py`](../../scripts/spatial_statistics/point_pattern_analysis.py) makes this distinction explicit.

## Interaction vs Inhomogeneous Intensity

Two mechanisms can produce clusters:

- a varying first-order intensity $\lambda(s)$;
- second-order interaction among events.

A raw cluster map cannot distinguish them.

For example, stores may cluster downtown because downtown has higher underlying opportunity/intensity, even if stores are otherwise independently located conditional on that intensity.

## Nearest-Neighbor Distance

The distance from each event to its nearest other event is a simple short-range summary.

For a homogeneous planar Poisson process on an unbounded region, the theoretical nearest-neighbor distribution is

$$
G(r)=1-e^{-\lambda\pi r^2}.
$$

Real study windows create boundary effects, so naive nearest-neighbor summaries near the edge should be interpreted carefully.

## Ripley's K Function

For a stationary process with intensity $\lambda$,

$$
K(r)
=
\frac{1}{\lambda}
E[
\text{number of additional events within distance }r
\text{ of a typical event}
].
$$

Under homogeneous complete spatial randomness in two dimensions,

$$
K_{\mathrm{CSR}}(r)=\pi r^2.
$$

Broadly:

- $\hat K(r)>\pi r^2$ suggests more nearby pairs than under CSR;
- $\hat K(r)<\pi r^2$ suggests inhibition/regularity.

The comparison is scale-dependent: a pattern may be inhibited at short distances and clustered at longer distances.

## Edge Correction

A point near the observation-window boundary has part of its radius-$r$ neighborhood outside the observed window. Ignoring this creates downward bias in pair counts and in $\hat K(r)$.

Common corrections include:

- border/guard-zone correction;
- translation correction;
- isotropic correction.

The companion script implements a simple border correction and limits radii to scales for which interior points remain available.

## Monte Carlo Envelopes

A common goodness-of-fit workflow is:

1. fit or specify a reference process;
2. simulate many patterns under it;
3. compute the same summary curve for every simulation;
4. compare the observed curve with simulated envelopes.

Pointwise envelopes are useful exploratory diagnostics but are not automatically global simultaneous tests over all distances.

## Cluster Processes

A Thomas process is a common clustered model:

1. parent events follow a Poisson process;
2. each parent produces a Poisson number of offspring;
3. offspring are displaced around the parent, commonly with Gaussian displacement.

The parent process can be latent; only offspring may be observed.

## Inhibitory Processes

Hard-core and Gibbs processes represent repulsion or spacing constraints. They are useful when events compete for space or cannot occur closer than a physical minimum distance.

## Marked Point Processes

Events can carry marks such as tree species, tree height, earthquake magnitude, or incident type.

Do not confuse:

- analysis of the point pattern itself;
- spatial autocorrelation of a mark attached to the observed points.

Those are different questions and may require different null models.

## Modeling Workflow

1. Define the observation window and event definition.
2. Map the points and inspect potential intensity covariates.
3. Model first-order intensity.
4. Examine nearest-neighbor or $K$-function summaries with edge correction.
5. Compare with simulations from a scientifically meaningful reference process.
6. Fit an interaction/cluster model only when needed.
7. Validate using residual or simulation diagnostics rather than visual fit alone.
