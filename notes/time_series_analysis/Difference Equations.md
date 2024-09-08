Difference Equations and Solutions
1. What is a Difference Equation?

A difference equation (also known as a recurrence relation) defines each term of a sequence based on previous terms. In some cases, the general term of a sequence is given explicitly (e.g., an=2n+1an​=2n+1, resulting in the sequence 3, 5, 7, …). However, more commonly, a difference equation provides a relationship between terms.

For example:
an=5an−1−6an−2
an​=5an−1​−6an−2​

is a second-order difference equation because it relates anan​ to the two previous terms an−1an−1​ and an−2an−2​.
2. Solving Difference Equations

To solve a difference equation, we look for a solution of the form:
an=λn
an​=λn

This approach assumes a solution structure where each term is proportional to the previous term by some factor λλ.
Example:

For the difference equation:
an=5an−1−6an−2
an​=5an−1​−6an−2​

Substitute an=λnan​=λn into the equation:
λn=5λn−1−6λn−2
λn=5λn−1−6λn−2

Dividing both sides by λn−2λn−2, we get the characteristic equation:
λ2−5λ+6=0
λ2−5λ+6=0

This is a quadratic equation. Solving for λλ, we get the roots:
λ=2,λ=3
λ=2,λ=3

Thus, the general solution to the difference equation is:
an=c12n+c23n
an​=c1​2n+c2​3n

where c1c1​ and c2c2​ are constants determined by the initial conditions.
3. Example: Solving with Initial Conditions

Given the initial conditions a0=3a0​=3 and a1=8a1​=8, we can solve for c1c1​ and c2c2​.

At n=0n=0:
a0=c120+c230=c1+c2=3
a0​=c1​20+c2​30=c1​+c2​=3

At n=1n=1:
a1=c121+c231=2c1+3c2=8
a1​=c1​21+c2​31=2c1​+3c2​=8

Solving this system of equations:
c1+c2=32c1+3c2=8
c1​+c2​2c1​+3c2​​=3=8​

We find:
c1=1,c2=2
c1​=1,c2​=2

Thus, the solution to the difference equation is:
an=2n+2⋅3n
an​=2n+2⋅3n
4. Higher-Order Difference Equations

A k-th order difference equation has the form:
an=β1an−1+β2an−2+⋯+βkan−k
an​=β1​an−1​+β2​an−2​+⋯+βk​an−k​

The characteristic equation for such an equation is:
λk−β1λk−1−⋯−βk=0
λk−β1​λk−1−⋯−βk​=0

Once we find the kk roots λ1,λ2,…,λkλ1​,λ2​,…,λk​, the general solution is:
an=c1λ1n+c2λ2n+⋯+ckλkn
an​=c1​λ1n​+c2​λ2n​+⋯+ck​λkn​

The constants c1,c2,…,ckc1​,c2​,…,ck​ are determined by the initial conditions.
5. Example: Fibonacci Sequence

The Fibonacci sequence is a classic example of a difference equation:
an=an−1+an−2
an​=an−1​+an−2​

with initial conditions a0=1a0​=1 and a1=1a1​=1.

The characteristic equation is:
λ2−λ−1=0
λ2−λ−1=0

Solving this quadratic equation:
λ1=1−52,λ2=1+52
λ1​=21−5
​​,λ2​=21+5
​​

Thus, the general solution is:
an=c1(1−52)n+c2(1+52)n
an​=c1​(21−5
​​)n+c2​(21+5
​​)n

Using the initial conditions:
c1+c2=1
c1​+c2​=1
c1(1−52)+c2(1+52)=1
c1​(21−5
​​)+c2​(21+5
​​)=1

Solving for c1c1​ and c2c2​:
c1=5−510,c2=5+510
c1​=105−5
​​,c2​=105+5
​​

Thus, the general term of the Fibonacci sequence is:
an=15((1+52)n−(1−52)n)
an​=5
​1​((21+5
​​)n−(21−5
​​)n)
6. Relation to Differential Equations

A k-th order linear ordinary differential equation has a similar form to the k-th order difference equation:
y(k)=β1y(k−1)+⋯+βky
y(k)=β1​y(k−1)+⋯+βk​y

The solution for the differential equation is found using the same characteristic equation:
λk−β1λk−1−⋯−βk=0
λk−β1​λk−1−⋯−βk​=0

Once the roots are found, the general solution is expressed as a sum of exponentials, analogous to the powers of λλ in the difference equation solution.
