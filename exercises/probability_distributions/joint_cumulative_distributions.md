# Example - Time Between Dispatches

Two delivery trucks are scheduled to depart from a warehouse, with their dispatch times uniformly distributed between 8 AM and 10 AM. Each truck has a 20-minute window to leave the warehouse before it falls behind schedule. What is the probability that the second truck will not be dispatched on time due to the first truck's delay?

Let's denote the dispatch time of the first truck as $T_1$ and the second truck as $T_2$. The probability that the second truck falls behind schedule due to the first truck's delay can be given by:

This would be $P(T_1 + 20 < T_2) + P(T_2 + 20 < T_1) = 2 P(T_1 + 20 < T_2)$

$$
= 2 \int\limits_{-\infty}^{+\infty} \int\limits_{T_1+20}^{+\infty} f(t_1, t_2) \, \mathrm{d}t_1 \, \mathrm{d}t_2$$


$$
= 2 \int\limits_{-\infty}^{+\infty} \int\limits_{T_1+20}^{+\infty} f_{T_1}(t_1)f_{T_2}(t_2) \, \mathrm{d}t_1 \, \mathrm{d}t_2
$$

$$
= 2 \int_{0}^{120} \int_{0}^{t_2-20} \left( \frac{1}{120} \right)^2 \,dt_1 \,dt_2
$$

$$
= \frac{2}{(120)^2} \int_{20}^{120} (t_2 - 20) \,dt_2
$$

$$
= \frac{2500}{14400}
$$

$$
= \frac{25}{144}
$$
