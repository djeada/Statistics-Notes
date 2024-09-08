Invertibility and Inversion of MA(1) Process


Consider the MA(1) (Moving Average of order 1) process:
Xt=Zt+βZt−1
Xt​=Zt​+βZt−1​

where ZtZt​ is white noise with mean 0 and variance σZ2σZ2​, and ββ is a constant.

Using backward substitution, we can express ZtZt​ in terms of XtXt​ and lagged values of XtXt​. First, rearrange the equation:
Zt=Xt−βZt−1
Zt​=Xt​−βZt−1​

Now, substitute Zt−1Zt−1​ from the same equation:
Zt=Xt−β(Xt−1−βZt−2)=Xt−βXt−1+β2Zt−2
Zt​=Xt​−β(Xt−1​−βZt−2​)=Xt​−βXt−1​+β2Zt−2​

Continuing this process:
Zt=Xt−βXt−1+β2Xt−2−β3Xt−3+…
Zt​=Xt​−βXt−1​+β2Xt−2​−β3Xt−3​+…

This shows that the MA(1) process can be written as an AR(∞) (AutoRegressive process of infinite order):
Xt=Zt+βXt−1−β2Xt−2+β3Xt−3−…
Xt​=Zt​+βXt−1​−β2Xt−2​+β3Xt−3​−…

This inversion is critical to understanding the relationship between MA and AR processes.
3. Inversion Using the Backward Shift Operator

Alternatively, we can use the backward shift operator to invert the MA(1) process.

Given:
Xt=(1+βB)Zt
Xt​=(1+βB)Zt​

where BB is the backward shift operator, BZt=Zt−1BZt​=Zt−1​, we aim to find ZtZt​ in terms of XtXt​ by inverting the operator 1+βB1+βB:
Zt=(1+βB)−1Xt
Zt​=(1+βB)−1Xt​

The inverse of 1+βB1+βB can be expanded as a power series:
(1+βB)−1=1−βB+β2B2−β3B3+…
(1+βB)−1=1−βB+β2B2−β3B3+…

Thus, applying this operator to XtXt​, we get:
Zt=Xt−βXt−1+β2Xt−2−β3Xt−3+…
Zt​=Xt​−βXt−1​+β2Xt−2​−β3Xt−3​+…

This is the same result obtained by backward substitution.
4. Convergence of the Series

For the series to converge in the mean-square sense, the absolute value of ββ must be less than 1. This ensures that the terms βnβn decay as n→∞n→∞, leading to convergence of the infinite sum.
∑n=0∞βnXt−nconverges if∣β∣<1
n=0∑∞​βnXt−n​converges if∣β∣<1

This is a necessary condition for the invertibility of the MA(1) process.
5. Invertibility: Definition

A time series process XtXt​ is called invertible if the white noise process ZtZt​ (also called the innovation) can be expressed as a convergent infinite sum of past values of XtXt​:
Zt=∑k=0∞πkXt−k
Zt​=k=0∑∞​πk​Xt−k​

where the series ∑k=0∞∣πk∣∑k=0∞​∣πk​∣ is convergent.
6. Example of Invertibility: Model 1 vs. Model 2

    Model 1 is not invertible:
    ∑k=0∞∣πk∣=∑k=0∞2kdiverges
    k=0∑∞​∣πk​∣=k=0∑∞​2kdiverges

    Model 2 is invertible:
    ∑k=0∞∣πk∣=∑k=0∞12kis a geometric series and converges.
    k=0∑∞​∣πk​∣=k=0∑∞​2k1​is a geometric series and converges.

To ensure invertibility, we must choose a model where ∣β∣<1∣β∣<1. In such cases, the autocorrelation function (ACF) uniquely determines the MA process.
