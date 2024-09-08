Yule-Walker Equations 

The Yule-Walker equations are used to compute the autocorrelation function (ACF) of autoregressive (AR) processes. These equations link the autocovariances of the process to the parameters of the AR model, allowing us to estimate the ACF and solve for the model parameters.
2. Assumptions and Procedure

We begin with the assumption of stationarity. The general steps to derive the Yule-Walker equations are as follows:

    Multiply the AR model by Xn−kXn−k​.
    Take the expectation of both sides.
    Use the definition of covariance and divide by γ0=σX2γ0​=σX2​, where γ(k)γ(k) is the autocovariance and σX2σX2​ is the variance.
    This results in a difference equation for ρ(k)ρ(k), the ACF of the process.
    The set of equations obtained is called the Yule-Walker equations.
    Solve the difference equation to find the autocorrelation function.

3. Example: AR(2) Process

Consider the AR(2) process:
Xt=13Xt−1+12Xt−2+Zt(1)
Xt​=31​Xt−1​+21​Xt−2​+Zt​(1)

Here, ZtZt​ is white noise with mean zero and variance σZ2σZ2​.

The characteristic polynomial of the AR(2) process is:
ϕ(B)=1−13B−12B2
ϕ(B)=1−31​B−21​B2

The roots of this polynomial are:
λ=−2±766
λ=−2±676
​​

Since both roots have magnitudes greater than 1, they lie outside the unit circle, implying that the process is stationary.
4. Yule-Walker Equations for the AR(2) Process

We want to find the ACF ρ(k)ρ(k) of the AR(2) process.
Step 1: Multiply by Xt−kXt−k​ and Take Expectation

Multiply equation (1) by Xt−kXt−k​ and take the expectation:
E[Xt−kXt]=13E[Xt−kXt−1]+12E[Xt−kXt−2]+E[Xt−kZt]
E[Xt−k​Xt​]=31​E[Xt−k​Xt−1​]+21​E[Xt−k​Xt−2​]+E[Xt−k​Zt​]

Since ZtZt​ is white noise and uncorrelated with Xt−kXt−k​, the term E[Xt−kZt]=0E[Xt−k​Zt​]=0.

Using the autocovariance γ(k)=E[XtXt−k]γ(k)=E[Xt​Xt−k​] and the assumption that μ=0μ=0, we have:
γ(k)=13γ(k−1)+12γ(k−2)
γ(k)=31​γ(k−1)+21​γ(k−2)
Step 2: Express as ACF Equation

Dividing by γ0=σX2γ0​=σX2​, we obtain the ACF equation:
ρ(k)=13ρ(k−1)+12ρ(k−2)
ρ(k)=31​ρ(k−1)+21​ρ(k−2)

This is the Yule-Walker equation for the AR(2) process.
5. Solving the Difference Equation

We assume a solution of the form ρ(k)=λkρ(k)=λk. Substituting this into the Yule-Walker equation:
λk=13λk−1+12λk−2
λk=31​λk−1+21​λk−2

Dividing both sides by λk−2λk−2, we obtain the characteristic equation:
λ2−13λ−12=0
λ2−31​λ−21​=0
Step 1: Solve the Characteristic Equation

Solving this quadratic equation:
λ=16(2±76)
λ=61​(2±76
​)

Thus, the roots are:
λ1=2+7612,λ2=2−7612
λ1​=122+76
​​,λ2​=122−76
​​
Step 2: General Solution for ρ(k)ρ(k)

The general solution for ρ(k)ρ(k) is:
ρ(k)=c1λ1k+c2λ2k
ρ(k)=c1​λ1k​+c2​λ2k​
6. Determine c1c1​ and c2c2​

We use the initial conditions to determine the coefficients c1c1​ and c2c2​.
Step 1: Use ρ(0)=1ρ(0)=1

At k=0k=0:
ρ(0)=c1+c2=1
ρ(0)=c1​+c2​=1
Step 2: Use ρ(1)ρ(1)

At k=1k=1, use the Yule-Walker equation:
ρ(1)=13ρ(0)+12ρ(−1)
ρ(1)=31​ρ(0)+21​ρ(−1)

Since ρ(k)=ρ(−k)ρ(k)=ρ(−k), we have:
ρ(1)=23
ρ(1)=32​

Thus, substituting into the general solution:
ρ(1)=c1λ1+c2λ2=23
ρ(1)=c1​λ1​+c2​λ2​=32​
Step 3: Solve the System

We now solve the system of equations:
c1+c2=1c1λ1+c2λ2=23
c1​+c2​c1​λ1​+c2​λ2​​=1=32​​

Substituting the values of λ1λ1​ and λ2λ2​, we find:
c1=4+768,c2=4−768
c1​=84+76
​​,c2​=84−76
​​
7. ACF for AR(2) Process

Thus, the ACF ρ(k)ρ(k) for the AR(2) process is:
ρ(k)=4+768(2+7612)k+4−768(2−7612)k
ρ(k)=84+76
​​(122+76
​​)k+84−76
​​(122−76
​​)k

