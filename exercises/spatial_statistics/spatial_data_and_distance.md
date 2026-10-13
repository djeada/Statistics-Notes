# Spatial Data, Support, and Distance Exercises

Use this problem set with the [chapter notes](../../notes/spatial_statistics/spatial_data_and_distance.md) and the [visualization script](../../scripts/spatial_statistics/spatial_data_support_distance_visualizations.py).


## Exercise 1: projected Euclidean distance

Two locations have projected coordinates

$$
(1200,3400)
$$

and

$$
(1500,3800)
$$

in meters.

Calculate the Euclidean distance.

---

## Exercise 2: longitude distance

Using the approximation

$$
111.2\cos(\phi)\text{ km},
$$

estimate the east-west distance represented by one degree of longitude at

$$
\phi=30^\circ.
$$

---

## Exercise 3: support

Explain why:

- a temperature sensor reading;
- a 5 km satellite pixel average

cannot be treated as measurements with identical support.

---

## Exercise 4: zoning

Fine-scale values are

$$
1,\ 3,\ 7,\ 9.
$$

Calculate regional means under these two zoning schemes:

$$
(1,3),\ (7,9)
$$

and

$$
(1,7),\ (3,9).
$$

Explain what changes.

---

## Exercise 5: distance choice

Give one application where each is appropriate:

- Euclidean distance;
- road-network distance;
- river-network distance;
- travel time;
- geodesic distance.

---

## Exercise 6: support mismatch

A district overlaps three raster cells with values

$$
4,\ 8,\ 10
$$

and area-overlap proportions

$$
0.2,\ 0.5,\ 0.3.
$$

Calculate the area-weighted district average.

---

## Worked solutions

### Exercise 1

$$
\Delta x=1500-1200=300\text{ m},
\qquad
\Delta y=3800-3400=400\text{ m}.
$$

$$
d=\sqrt{300^2+400^2}=\sqrt{90000+160000}=\sqrt{250000}=500\text{ m}.
$$

### Exercise 2

$$
\cos(30^\circ)=\frac{\sqrt3}{2}\approx0.8660,
$$

$$
111.2\times0.8660\approx96.3\text{ km}.
$$

One degree of longitude at $30^\circ$ is about 96.3 km, versus 111.2 km at the equator.

### Exercise 3

Model answer: a sensor reading approximates **point support**, describing conditions in a tiny neighborhood of the sensor. A 5 km pixel average has **area support** of about 25 km$^2$ and mixes everything inside the pixel (hills, water, buildings). Averaging smooths extremes, so pixel values have smaller variance than point values and their correlations with other variables can differ. Even when the pixel centroid coincides with the sensor, the two values answer different questions, so comparing or merging them requires an explicit change-of-support step (for example, upscaling the sensors to the pixel or downscaling the pixel).

### Exercise 4

Scheme 1, $(1,3)$ and $(7,9)$:

$$
\frac{1+3}{2}=2,
\qquad
\frac{7+9}{2}=8.
$$

Scheme 2, $(1,7)$ and $(3,9)$:

$$
\frac{1+7}{2}=4,
\qquad
\frac{3+9}{2}=6.
$$

Both schemes preserve the overall mean, $(2+8)/2=(4+6)/2=5$. The variance of the regional means differs:

$$
\text{scheme 1: }\frac{(2-5)^2+(8-5)^2}{2}=9,
\qquad
\text{scheme 2: }\frac{(4-5)^2+(6-5)^2}{2}=1.
$$

Same data, same number of regions, but the apparent regional contrast changes ninefold. This is the **zoning effect** of the MAUP.

### Exercise 5

Model answers:

- Euclidean distance: spacing of soil samples in a small projected field plot.
- Road-network distance: ambulance response or delivery access, where travel follows roads.
- River-network distance: spread of a pollutant or fish between sampling sites on a stream network.
- Travel time: commuting or health-service access, where speed limits and congestion matter.
- Geodesic distance: distances between weather stations or cities across a continent, where projected planar distance is distorted.

### Exercise 6

$$
0.2(4)+0.5(8)+0.3(10)=0.8+4.0+3.0=7.8.
$$

The weights sum to $0.2+0.5+0.3=1$, so no renormalization is required. The unweighted mean of the three cells is $(4+8+10)/3\approx7.33$, which understates the heavily overlapped value 8 and the high value 10.
