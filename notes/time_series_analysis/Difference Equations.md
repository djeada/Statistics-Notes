## Difference Equation

A **difference equation** (also known as a recurrence relation) defines each term of a sequence based on previous terms. In some cases, the general term of a sequence is given explicitly (e.g., $a_n = 3n + 2$, resulting in the sequence $5, 8, 11, \dots$). However, more commonly, a difference equation provides a relationship between terms.

For example:

$$
a_n = 4 a_{n-1} - 5 a_{n-2}
$$

is a second-order difference equation because it relates $a_n$ to the two previous terms $a_{n-1}$ and $a_{n-2}$.

---

### Solving Difference Equations

To solve a difference equation, we often look for a solution of the form:

$$
a_n = \lambda^n
$$

This assumes a solution structure where each term is proportional to the previous term by some factor $\lambda$.

**Example:**

For the difference equation:

$$
a_n = 4 a_{n-1} - 5 a_{n-2}
$$

Substitute $a_n = \lambda^n$ into the equation:

$$
\lambda^n = 4 \lambda^{n-1} - 5 \lambda^{n-2}
$$

Dividing both sides by $\lambda^{n-2}$, we get the **characteristic equation**:

$$
\lambda^2 - 4 \lambda + 5 = 0
$$

This is a quadratic equation. Solving for $\lambda$, we get the roots:

$$
\lambda = 2, \lambda = 3
$$

Thus, the general solution to the difference equation is:

$$
a_n = c_1 2^n + c_2 3^n
$$

where $c_1$ and $c_2$ are constants determined by the initial conditions.

---

### Example: Solving with Initial Conditions

Given the initial conditions $a_0 = 4$ and $a_1 = 10$, we can solve for $c_1$ and $c_2$.

At $n = 0$:

$$
a_0 = c_1 2^0 + c_2 3^0 = c_1 + c_2 = 4
$$

At $n = 1$:

$$
a_1 = c_1 2^1 + c_2 3^1 = 2 c_1 + 3 c_2 = 10
$$

Solving this system of equations:

$$
\begin{aligned}
c_1 + c_2 &= 4 \\
2 c_1 + 3 c_2 &= 10
\end{aligned}
$$

We find:

$$
c_1 = 2, \quad c_2 = 2
$$

Thus, the solution to the difference equation is:

$$
a_n = 2 \cdot 2^n + 2 \cdot 3^n
$$

---

### Higher-Order Difference Equations

A $k$-th order difference equation has the form:

$$
a_n = \beta_1 a_{n-1} + \beta_2 a_{n-2} + \dots + \beta_k a_{n-k}
$$

The characteristic equation for such a difference equation is:

$$
\lambda^k - \beta_1 \lambda^{k-1} - \dots - \beta_k = 0
$$

Once we find the $k$ roots $\lambda_1, \lambda_2, \dots, \lambda_k$, the general solution is:

$$
a_n = c_1 \lambda_1^n + c_2 \lambda_2^n + \dots + c_k \lambda_k^n
$$

The constants $c_1, c_2, \dots, c_k$ are determined by the initial conditions.

---

### Example: Fibonacci Sequence

The Fibonacci sequence is a classic example of a difference equation:

$$
a_n = a_{n-1} + a_{n-2}
$$

with initial conditions $a_0 = 2$ and $a_1 = 3$.

The characteristic equation is:

$$
\lambda^2 - \lambda - 1 = 0
$$

Solving this quadratic equation:

$$
\lambda_1 = \frac{1 - \sqrt{5}}{2}, \quad \lambda_2 = \frac{1 + \sqrt{5}}{2}
$$

Thus, the general solution is:

$$
a_n = c_1 \left( \frac{1 - \sqrt{5}}{2} \right)^n + c_2 \left( \frac{1 + \sqrt{5}}{2} \right)^n
$$

Using the initial conditions:

$$
c_1 + c_2 = 2
$$

$$
c_1 \left( \frac{1 - \sqrt{5}}{2} \right) + c_2 \left( \frac{1 + \sqrt{5}}{2} \right) = 3
$$

Solving for $c_1$ and $c_2$, we find:

$$
c_1 = \frac{3 - \sqrt{5}}{2}, \quad c_2 = \frac{3 + \sqrt{5}}{2}
$$

Thus, the general term of the Fibonacci sequence is:

$$
a_n = \frac{1}{\sqrt{5}} \left( \left( \frac{1 + \sqrt{5}}{2} \right)^n - \left( \frac{1 - \sqrt{5}}{2} \right)^n \right)
$$

---

### Relation to Differential Equations

A $k$-th order linear ordinary differential equation has a similar form to the $k$-th order difference equation:

$$
y^{(k)} = \beta_1 y^{(k-1)} + \dots + \beta_k y
$$

The solution for the differential equation is found using the same characteristic equation:

$$
\lambda^k - \beta_1 \lambda^{k-1} - \dots - \beta_k = 0
$$

Once the roots are found, the general solution is expressed as a sum of exponentials, analogous to the powers of $\lambda$ in the difference equation solution.

