# Spatial Data, Support, and Distance Exercises

Use this problem set with the [chapter notes](../../notes/spatial_statistics/spatial_data_and_distance.md) and the [visualization script](../../scripts/spatial_statistics/spatial_data_support_distance_visualizations.py).


## Exercise 1: projected Euclidean distance

Two locations have projected coordinates

\[
(1200,3400)
\]

and

\[
(1500,3800)
\]

in meters.

Calculate the Euclidean distance.

---

## Exercise 2: longitude distance

Using the approximation

\[
111.2\cos(\phi)\text{ km},
\]

estimate the east-west distance represented by one degree of longitude at

\[
\phi=30^\circ.
\]

---

## Exercise 3: support

Explain why:

- a temperature sensor reading;
- a 5 km satellite pixel average

cannot be treated as measurements with identical support.

---

## Exercise 4: zoning

Fine-scale values are

\[
1,\ 3,\ 7,\ 9.
\]

Calculate regional means under these two zoning schemes:

\[
(1,3),\ (7,9)
\]

and

\[
(1,7),\ (3,9).
\]

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

\[
4,\ 8,\ 10
\]

and area-overlap proportions

\[
0.2,\ 0.5,\ 0.3.
\]

Calculate the area-weighted district average.

---
