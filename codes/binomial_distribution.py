# binomial

# Independent Trials Success Probability = 0.73
import math
import matplotlib.pyplot as plt

fact = math.factorial

Ps = 0.73
p_D = {}
n = 7
for k in range(n+1):
nCk = fact(n) / (fact(k) * fact(n-k))
p = nCk * Ps**k * (1 - Ps)**(n - k)
p_D[k] = round(p, 2)

plt.bar(p_D.keys(), p_D.values())
plt.show()
