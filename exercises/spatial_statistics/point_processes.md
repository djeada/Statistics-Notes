# Point Process Exercises

Use this problem set with the [chapter notes](../../notes/spatial_statistics/point_processes.md) and the [visualization script](../../scripts/spatial_statistics/point_process_visualizations.py).


## Exercise 1: intensity

A rectangular study window is

$$
8\text{ km}\times5\text{ km}.
$$

It contains 60 events.

Calculate the homogeneous intensity estimate.

---

## Exercise 2: expected count

Suppose

$$
\lambda=1.5
$$

events per km$^2$.

Calculate the expected number of events in a region of area

$$
6\text{ km}^2.
$$

---

## Exercise 3: Poisson probability

If the expected count in a region is

$$
\mu=2,
$$

calculate

$$
P(N=0).
$$

---

## Exercise 4: nearest-neighbor distribution

For

$$
\lambda=0.1
$$

and

$$
r=1.5,
$$

calculate

$$
G(r)
=
1-e^{-\lambda\pi r^2}.
$$

---

## Exercise 5: K interpretation

At

$$
r=4,
$$

an analysis gives

$$
\hat K(4)=38.
$$

Calculate

$$
K_{\mathrm{CSR}}(4)
$$

and describe the direction of the departure.

Do not claim statistical significance without a simulation or inferential procedure.

---

## Exercise 6: mechanism

A pattern of coffee shops is concentrated strongly in a city center.

Give two different mechanisms that could create the visual clustering.

---

## Worked solutions

### Solution 1

$|W|=8\times5=40\text{ km}^2$, so

$$
\hat\lambda=\frac{n}{|W|}=\frac{60}{40}=1.5\text{ events per km}^2.
$$

### Solution 2

$$
E[N(B)]=\lambda|B|=1.5\times6=9.
$$

### Solution 3

$$
P(N=0)=e^{-\mu}\frac{\mu^0}{0!}=e^{-2}\approx0.1353.
$$

### Solution 4

$$
\lambda\pi r^2=0.1\pi(1.5)^2=0.1\pi(2.25)=0.225\pi\approx0.7069.
$$

$$
G(1.5)=1-e^{-0.7069}\approx1-0.4932=0.507.
$$

About 50.7% of events are expected to have their nearest neighbor within 1.5 units under CSR with $\lambda=0.1$.

### Solution 5

$$
K_{\mathrm{CSR}}(4)=\pi(4^2)=16\pi\approx50.27.
$$

Since $\hat K(4)=38<50.27$, the estimate lies below the CSR benchmark. Equivalently $\hat L(4)=\sqrt{38/\pi}\approx3.48<4$. Fewer neighbors within distance 4 are found than under CSR, which is consistent with inhibition or regular spacing at that scale. Without simulated envelopes (and edge correction, since uncorrected $K$ is biased downward) we cannot call the departure significant.

### Solution 6

Model answer: (a) first-order intensity: coffee shops follow customers, so the intensity $\lambda(s)$ is high where foot traffic, population and commercial zoning are high, and shops can be conditionally independent given that intensity; (b) interaction or agglomeration: shops deliberately locate next to competitors or complements (cluster attraction), which creates clustering beyond what intensity explains. A third possibility is observation or zoning effects (permitted areas, data recorded only for the center). Telling these apart requires fitting an inhomogeneous intensity and then examining $K$ or $L$ of the residual pattern against simulations from that fitted model.
