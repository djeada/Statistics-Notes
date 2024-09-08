Backward Shift Operator and Time Series Modeling


The backward shift operator (denoted BB) is a fundamental tool in time series analysis. It shifts the time index of a time series back by one period.

    For a time series {Xt}{Xt​}, the backward shift operator is defined as:
    BXt=Xt−1
    BXt​=Xt−1​

    Higher powers of the backward shift operator correspond to multiple shifts:
    B2Xt=B(BXt)=BXt−1=Xt−2
    B2Xt​=B(BXt​)=BXt−1​=Xt−2​
    BkXt=Xt−k
    BkXt​=Xt−k​

3. Example: Random Walk

Consider a simple random walk:
Xt=Xt−1+Zt
Xt​=Xt−1​+Zt​

Using the backward shift operator, this can be written as:
Xt=BXt+Zt
Xt​=BXt​+Zt​

Rearranging:
(1−B)Xt=Zt
(1−B)Xt​=Zt​

This expression simplifies the random walk using the operator notation, where 1−B1−B operates on XtXt​. Let’s denote this operator as:
ϕ(B)=1−B
ϕ(B)=1−B

Thus, the random walk can be expressed as:
ϕ(B)Xt=Zt
ϕ(B)Xt​=Zt​

where ZtZt​ is the noise (e.g., white noise).
4. Example: Moving Average (MA) Process

Consider an MA(2) process:
Xt=Zt+0.2Zt−1+0.04Zt−2
Xt​=Zt​+0.2Zt−1​+0.04Zt−2​

Using the backward shift operator, this can be written as:
Xt=Zt+0.2BZt+0.04B2Zt
Xt​=Zt​+0.2BZt​+0.04B2Zt​

Factoring the right-hand side:
Xt=(1+0.2B+0.04B2)Zt
Xt​=(1+0.2B+0.04B2)Zt​

Let’s define:
β(B)=1+0.2B+0.04B2
β(B)=1+0.2B+0.04B2

Thus, the MA(2) process can be written as:
Xt=β(B)Zt
Xt​=β(B)Zt​

This operator form is convenient for analyzing and solving MA models.
5. Example: Autoregressive (AR) Process

Consider an AR(2) process:
Xt=0.2Xt−1+0.3Xt−2+Zt
Xt​=0.2Xt−1​+0.3Xt−2​+Zt​

Using the backward shift operator, this becomes:
Xt=0.2BXt+0.3B2Xt+Zt
Xt​=0.2BXt​+0.3B2Xt​+Zt​

Rearranging:
(1−0.2B−0.3B2)Xt=Zt
(1−0.2B−0.3B2)Xt​=Zt​

Let’s define the AR operator as:
ϕ(B)=1−0.2B−0.3B2
ϕ(B)=1−0.2B−0.3B2

Thus, the AR(2) process can be written as:
ϕ(B)Xt=Zt
ϕ(B)Xt​=Zt​

This is the standard form of an AR process in terms of the backward shift operator.
6. MA(q) Process with Drift

An MA(q) process with drift is given by:
Xt=μ+β0Zt+β1Zt−1+⋯+βqZt−q
Xt​=μ+β0​Zt​+β1​Zt−1​+⋯+βq​Zt−q​

Using the backward shift operator:
Xt=μ+β0Zt+β1BZt+⋯+βqBqZt
Xt​=μ+β0​Zt​+β1​BZt​+⋯+βq​BqZt​

Factoring the right-hand side:
Xt=μ+β(B)Zt
Xt​=μ+β(B)Zt​

where β(B)=β0+β1B+⋯+βqBqβ(B)=β0​+β1​B+⋯+βq​Bq. Subtracting the drift term μμ:
Xt−μ=β(B)Zt
Xt​−μ=β(B)Zt​
7. AR(p) Process

An AR(p) process is given by:
Xt=ϕ1Xt−1+ϕ2Xt−2+⋯+ϕpXt−p+Zt
Xt​=ϕ1​Xt−1​+ϕ2​Xt−2​+⋯+ϕp​Xt−p​+Zt​

Using the backward shift operator:
Xt=ϕ1BXt+ϕ2B2Xt+⋯+ϕpBpXt+Zt
Xt​=ϕ1​BXt​+ϕ2​B2Xt​+⋯+ϕp​BpXt​+Zt​

Rearranging:
(1−ϕ1B−ϕ2B2−⋯−ϕpBp)Xt=Zt
(1−ϕ1​B−ϕ2​B2−⋯−ϕp​Bp)Xt​=Zt​

This can be written as:
ϕ(B)Xt=Zt
ϕ(B)Xt​=Zt​

where ϕ(B)=1−ϕ1B−ϕ2B2−⋯−ϕpBpϕ(B)=1−ϕ1​B−ϕ2​B2−⋯−ϕp​Bp.
