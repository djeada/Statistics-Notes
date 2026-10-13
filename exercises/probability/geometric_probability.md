# Geometric Probability: Exercises

Practice for the note [Geometric Probability](../../notes/probability/geometric_probability.md). In all problems "random" means uniform over the stated region.

## Problems

1. **Segment.** A point $X$ is chosen uniformly on $[0,10]$. Find $P(3\le X\le7)$, $P(X<2\text{ or }X>8)$, and $P(|X-5|<1)$.

2. **Dartboard.** A dart lands uniformly on a circular board of radius 20 cm. The bullseye has radius 2 cm, and a scoring ring lies between radii 10 cm and 20 cm. Find the probability of the bullseye and of the ring.

3. **Meeting.** Two friends arrive independently and uniformly between 12:00 and 13:00 and each waits 15 minutes. Find the probability they meet.

4. **Quarter circle.** A point is uniform in the unit square. Find $P(D<0.6)$ where $D$ is the distance to the origin, and the radius $r\le1$ for which this probability is $0.5$.

5. **Beyond the square.** For the same setting, find $P(D<1.3)$ using the formula from the note.

6. **Sum and product.** For independent uniform $X,Y$ on $[0,1]$ find $P(X+Y<1.5)$ and $P(XY<\tfrac14)$.

7. **Bertrand.** A chord of a circle of radius $R$ is chosen by fixing one endpoint and choosing the other uniformly on the circumference. Find the probability that its length exceeds $R$. Then find the probability under the method "choose a point uniformly along a random radius as the chord's midpoint".

8. **Broken stick.** A stick of length 1 is broken at two independent uniform points. Find the probability the three pieces form a triangle.

9. **Buffon.** A needle of length $l$ is dropped on a floor ruled with parallel lines a distance $d\ge l$ apart. Find the probability it crosses a line, and evaluate for $l=d$.

## Solutions

### Solution 1

Probability equals length of the favorable set divided by total length 10.

- $P(3\le X\le7)=\frac{4}{10}=0.4$.
- $P(X<2\text{ or }X>8)=\frac{2+2}{10}=0.4$.
- $P(|X-5|<1)=P(4<X<6)=\frac{2}{10}=0.2$.

### Solution 2

$$P(\text{bullseye})=\frac{\pi(2)^2}{\pi(20)^2}=\frac{4}{400}=0.01.$$

$$P(\text{ring})=\frac{\pi(20^2-10^2)}{\pi(20)^2}=\frac{400-100}{400}=0.75.$$

### Solution 3

Let $X,Y\in[0,60]$ be arrival minutes. They meet iff $|X-Y|\le15$. The failing region consists of two triangles with legs $60-15=45$, so each has area $\frac12\cdot45^2=1012.5$.

$$P(\text{meet})=1-\frac{2(1012.5)}{3600}=1-\frac{2025}{3600}=1-0.5625=0.4375.$$

### Solution 4

For $r\le1$ the region is a quarter disk of area $\frac{\pi r^2}{4}$, and the square has area 1.

$$P(D<0.6)=\frac{\pi(0.36)}{4}=0.09\pi\approx0.2827.$$

Set $\frac{\pi r^2}{4}=\frac12$, so $r^2=\frac{2}{\pi}$ and $r=\sqrt{2/\pi}\approx0.798$.

### Solution 5

For $1<r\le\sqrt2$: $P=r^2\left(\arcsin\frac1r-\frac\pi4\right)+\sqrt{r^2-1}$.

With $r=1.3$: $r^2=1.69$, $\arcsin(1/1.3)=\arcsin(0.7692)\approx0.8776$, $\sqrt{1.69-1}=\sqrt{0.69}\approx0.8307$.

$$P=1.69(0.8776-0.7854)+0.8307=1.69(0.0922)+0.8307=0.1558+0.8307\approx0.9865.$$

### Solution 6

$P(X+Y<1.5)$: the complement is the triangle $x+y\ge1.5$ with legs $0.5$, area $\frac12(0.5)^2=0.125$. So $P=1-0.125=0.875$.

$P(XY<\frac14)$: for $x\le\frac14$ every $y\in[0,1]$ works; for $x>\frac14$ we need $y<\frac1{4x}$.

$$P=\frac14+\int_{1/4}^{1}\frac{1}{4x}\,dx=\frac14+\frac14\left[\ln x\right]_{1/4}^{1}=\frac14+\frac14\ln4\approx0.25+0.3466=0.5966.$$

### Solution 7

**Random endpoints.** Fix one endpoint; the other is at angle $\varphi$ uniform on $[0,2\pi)$. The chord length is $2R\sin(\varphi/2)$ (taking $\varphi\in[0,2\pi)$ so $\sin\ge0$). It exceeds $R$ iff $\sin(\varphi/2)>\frac12$, i.e. $\frac\varphi2\in(\frac\pi6,\frac{5\pi}6)$, i.e. $\varphi\in(\frac\pi3,\frac{5\pi}3)$. The length of this interval is $\frac{4\pi}{3}$, so

$$P=\frac{4\pi/3}{2\pi}=\frac23.$$

**Random radial midpoint.** The midpoint distance $d$ is uniform on $[0,R]$. Since $L=2\sqrt{R^2-d^2}>R$ iff $d<\frac{\sqrt3}{2}R$,

$$P=\frac{\sqrt3}{2}\approx0.866.$$

The three methods (endpoints $\frac23$, radial $0.866$, uniform midpoint in the disk $\frac34$) disagree, which is Bertrand's paradox.

### Solution 8

Let the break points be $x<y$ (the unordered pair has probability $\frac12$ for each ordering, so we can work in the half-square $x<y$ of area $\frac12$). The pieces are $x$, $y-x$, $1-y$ and each must be less than $\frac12$: $x<\frac12$, $y>\frac12$, $y-x<\frac12$.

This is the triangle with vertices $(0,\frac12)$, $(\frac12,\frac12)$, $(\frac12,1)$, area $\frac12\cdot\frac12\cdot\frac12=\frac18$.

$$P=\frac{1/8}{1/2}=\frac14.$$

### Solution 9

Let $x\in[0,\frac d2]$ be the distance from the needle's center to the nearest line and $\theta\in[0,\frac\pi2]$ the angle with the lines, independent and uniform. The needle crosses iff $x\le\frac l2\sin\theta$.

$$P=\frac{1}{(d/2)(\pi/2)}\int_0^{\pi/2}\frac l2\sin\theta\,d\theta=\frac{4}{\pi d}\cdot\frac l2\cdot1=\frac{2l}{\pi d}.$$

For $l=d$: $P=\frac2\pi\approx0.637$.
