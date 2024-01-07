## Geometric Probability

Geometric probability involves finding the likelihood of an event by using geometric figures and measures such as area or volume. It often relates to continuous random variables and can be calculated using integral calculus.

### Example: Distance from a Corner in a Square

Consider a square with side lengths of 1 unit, and we are interested in the probability that a randomly chosen point inside the square is at a distance less than r from a specific corner of the square, let's say the bottom left corner at the origin (0,0).

#### Visual Setup

Visualize the square in the coordinate plane with corners at (0,0), (1,0), (0,1), and (1,1). The event space is the set of all points (x, y) that lie within this square. We're looking at the area within a quarter circle of radius r centered at the origin, which represents the points less than a distance r from that corner.

![5536c72b-ce5f-4e20-8683-3ede2d2a8a94](https://github.com/djeada/Statistics-Notes/assets/37275728/79a9a1dc-4716-46a1-8c6b-4d0a2da6f47c)


#### Probability Calculation

The probability is the area of the segment of the circle that lies within the square, divided by the total area of the square.

For r < 1 (when the circle is completely within the square):

The area of the quarter circle is $\frac{\pi r^2}{4}$, so the probability $P(r)$ that a point lies within this circle is:

$$
P(r) = \frac{\text{Area of quarter circle with radius r}}{\text{Area of square}} = \frac{\pi r^2}{4}
$$

For example, when $r = 0.8$, the calculated probability is approximately 50.27%. This indicates that there is about a 50.27% chance that a randomly chosen point inside the square is within 0.8 units of the bottom left corner.

This calculation is accurate for $r < 1$, where the entire quarter circle is within the boundaries of the square.

For r > 1 (when the circle extends outside the square):

We need to calculate the area of the quarter circle and subtract the area that lies outside the square. This results in:

$$
P(r) = \frac{\pi r^2}{4} - \text{Area outside the square}
$$

To find the area outside the square, we calculate the area under the curve from $x = 1$ to $r$, which represents the part of the circle that extends beyond the square's boundary. This results in the subtraction of the area of two such segments from the total area of the quarter circle.

For $r = \sqrt{2}$, the quarter circle exactly covers the square, making the probability equal to 1.
