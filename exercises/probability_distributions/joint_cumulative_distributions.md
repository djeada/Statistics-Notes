# Example - Time Between Dispatches

Two delivery trucks are scheduled to depart from a warehouse, with their dispatch times uniformly distributed between 8 AM and 10 AM (a 120-minute window), independently of each other. Each truck has a 20-minute window to leave the warehouse before it falls behind schedule. What is the probability that the two dispatch times differ by more than 20 minutes?

Measure time in minutes after 8 AM and let $T_1, T_2 \sim \text{Uniform}(0, 120)$ be independent, so the joint density is $f(t_1, t_2) = \left(\frac{1}{120}\right)^2$ on the square $[0,120]^2$.

The event of interest is $|T_1 - T_2| > 20$, which is

$$
P(T_2 > T_1 + 20) + P(T_1 > T_2 + 20) = 2\,P(T_1 + 20 < T_2)
$$

by symmetry. Integrating the joint density over the region $0 \le t_1 < t_2 - 20$, $20 \le t_2 \le 120$:

$$
2 \int_{20}^{120} \int_{0}^{t_2-20} \left( \frac{1}{120} \right)^2 dt_1\, dt_2
= \frac{2}{120^2} \int_{20}^{120} (t_2 - 20)\, dt_2
$$

$$
= \frac{2}{14400} \cdot \frac{100^2}{2}
= \frac{10000}{14400}
= \frac{25}{36} \approx 0.694
$$

Check by geometry: the region $|t_1 - t_2| \le 20$ is a diagonal band of the square. Its complement is two right triangles with legs $100$, total area $100^2 = 10000$, out of $120^2 = 14400$, giving the same $\frac{25}{36}$.
