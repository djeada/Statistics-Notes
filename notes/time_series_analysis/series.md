Series


2. Sequences and Series

A sequence is an ordered list of numbers. A sequence {an}{an​} is denoted as:
a1,a2,a3,…,an,…
a1​,a2​,a3​,…,an​,…

If the limit of the sequence exists, i.e.,
lim⁡n→∞an=a,
n→∞lim​an​=a,

then the sequence is said to be convergent.
Examples of Sequences:

    an=nn+1an​=n+1n​:
    12,23,34,…,nn+1→1asn→∞
    21​,32​,43​,…,n+1n​→1asn→∞
    an=3nan​=3n:
    3,9,27,…,3n
    3,9,27,…,3n This sequence diverges (grows without bound).
    an=nan​=n:
    1,2,3,…,n
    1,2,3,…,n This sequence diverges as well.
    an=1n2an​=n21​:
    1,14,19,…,1n2→0asn→∞
    1,41​,91​,…,n21​→0asn→∞

3. Partial Sums

The partial sum snsn​ of a sequence {an}{an​} is the sum of the first nn terms:
sn=a1+a2+⋯+an
sn​=a1​+a2​+⋯+an​

For example:

    s1=a1s1​=a1​
    s2=a1+a2s2​=a1​+a2​
    s3=a1+a2+a3s3​=a1​+a2​+a3​
    ……

4. Series

A series is the sum of the terms of a sequence. If the sequence of partial sums snsn​ converges to a limit ss, then we say the infinite series is convergent and equal to ss:
∑k=1∞ak=lim⁡n→∞sn=lim⁡n→∞(a1+a2+⋯+an)=s
k=1∑∞​ak​=n→∞lim​sn​=n→∞lim​(a1​+a2​+⋯+an​)=s

Otherwise, the series is said to be divergent.
5. Examples of Convergent Series

    Geometric series:
    ∑k=1∞12k=1
    k=1∑∞​2k1​=1
    P-series (convergent for p>1p>1):
    ∑k=1∞1k2=π26
    k=1∑∞​k21​=6π2​
    Alternating series:
    ∑k=1∞(−1)k+1k=ln⁡(2)
    k=1∑∞​k(−1)k+1​=ln(2)

6. Examples of Divergent Series

    Geometric series with growth factor greater than 1:
    ∑k=1∞3k
    k=1∑∞​3k
    Arithmetic series:
    ∑k=1∞(2k+1)
    k=1∑∞​(2k+1)
    Harmonic series:
    ∑k=1∞1k
    k=1∑∞​k1​ Although the terms 1kk1​ approach 0, the harmonic series diverges.

7. Absolute Convergence

A series is absolutely convergent if the series of the absolute values of its terms is convergent:
∑k=1∞∣ak∣
k=1∑∞​∣ak​∣

Absolute convergence implies convergence. This is stronger than regular convergence, as a series can be convergent without being absolutely convergent (e.g., alternating series).
8. Convergence Tests

There are various tests to determine if a series converges:

    Integral Test: Compares a series to the integral of a continuous function.
    Comparison Test: Compares the given series with a known convergent or divergent series.
    Limit Comparison Test: Uses the limit of the ratio between the terms of two series.
    Alternating Series Test: Used for series whose terms alternate in sign.
    Ratio Test: Uses the ratio between successive terms to test convergence.
    Root Test: Uses the nn-th root of the terms to test convergence.

Geometric Series and Rational Functions

A geometric series is a series of the form:
∑k=0∞rk=11−r,for ∣r∣<1
k=0∑∞​rk=1−r1​,for ∣r∣<1

This result can be used to represent certain rational functions as infinite series. For example:
11−x=∑k=0∞xk,for ∣x∣<1
1−x1​=k=0∑∞​xk,for ∣x∣<1

This is useful in time series analysis when dealing with autoregressive models and other representations involving rational functions.



Mean-Square Convergence
1. Definition of Mean-Square Convergence

Let X1,X2,X3,…X1​,X2​,X3​,… be a sequence of random variables, representing a stochastic process. We say that XnXn​ converges to a random variable XX in the mean-square sense if:
E[(Xn−X)2]→0asn→∞
E[(Xn​−X)2]→0asn→∞

This means that the expected value of the squared difference between XnXn​ and XX becomes arbitrarily small as nn increases.
2. Inverting the MA(1) Model

We previously inverted the MA(1) model:
Xt=Zt+βZt−1
Xt​=Zt​+βZt−1​

and expressed the white noise ZtZt​ as an infinite sum:
Zt=∑k=0∞(−β)kXt−k
Zt​=k=0∑∞​(−β)kXt−k​

The infinite sum is said to converge in the mean-square sense under certain conditions on ββ. To ensure this convergence, we need to verify that the sum of these terms remains bounded.
3. Autocovariance Function of the MA(1) Process

The autocovariance function γ(k)γ(k) for the MA(1) process is defined as follows:
γ(k)={(1+β2)σZ2if k=0βσZ2if k=10if k>1
γ(k)=⎩
⎨
⎧​(1+β2)σZ2​βσZ2​0​if k=0if k=1if k>1​

For negative values of kk, the autocovariance is symmetric, i.e., γ(−k)=γ(k)γ(−k)=γ(k).
4. Series Convergence

To investigate the convergence of the infinite series for ZtZt​, consider the partial sum:
∑k=0n(−β)kXt−k
k=0∑n​(−β)kXt−k​

We want to ensure that this sum converges to ZtZt​ in the mean-square sense, meaning:
E[(∑k=0n(−β)kXt−k−Zt)2]→0asn→∞
E
​(k=0∑n​(−β)kXt−k​−Zt​)2
​→0asn→∞

This expands as:
E[(∑k=0n(−β)kXt−k)2−2E(∑k=0n(−β)kXt−kZt)+E[Zt2]]
E
​(k=0∑n​(−β)kXt−k​)2−2E(k=0∑n​(−β)kXt−k​Zt​)+E[Zt2​]
​

Breaking this down, the terms become:

    E[∑k=0nβ2kXt−k2]E[∑k=0n​β2kXt−k2​]
    Cross terms between Xt−kXt−k​ and ZtZt​
    σZ2σZ2​, the variance of ZtZt​

We need the expression:
E[(∑k=0n(−β)kXt−k−Zt)2]→0
E
​(k=0∑n​(−β)kXt−k​−Zt​)2
​→0

to hold as n→∞n→∞.
5. Condition for Convergence

For the series to converge in the mean-square sense, we require the following condition:
σZ2β2(n+2)→0asn→∞
σZ2​β2(n+2)→0asn→∞

This happens when:
∣β∣<1
∣β∣<1

This condition ensures that the powers of ββ decay as nn increases, leading to the convergence of the infinite sum.
6. Invertibility Condition

The requirement that ∣β∣<1∣β∣<1 corresponds to the invertibility condition for the MA(1) process. This condition is often described in terms of the roots of the polynomial β(B)=1+βBβ(B)=1+βB. For invertibility, the zero of the polynomial must lie outside the unit circle in the complex plane, meaning:
∣β∣>−1or equivalently∣β∣<1
∣β∣>−1or equivalently∣β∣<1

Thus, the invertibility condition ensures that the MA process can be uniquely represented as an AR(∞) process.
