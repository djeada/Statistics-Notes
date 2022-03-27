import numpy as np
from scipy.stats import beta, skew
import matplotlib.pyplot as plt

x = np.linspace(0.0, 1.0, 100)
yb_rt = beta.pdf(x, 1.5, 5)*10
yb_nm = beta.pdf(x, 5, 5)*10
yb_lt = beta.pdf(x, 5, 1.5)*10
x *= 100

d_rt = np.column_stack((x, yb_rt)).tolist()
d_nm = np.column_stack((x, yb_nm)).tolist()
d_lt = np.column_stack((x, yb_lt)).tolist()

pts_lt = [i for l in [int(round(yb_lt, 0))*[x] for x, yb_lt in d_rt] for i in l]
pts_nm = [i for l in [int(round(yb_nm, 0))*[x] for x, yb_nm in d_nm] for i in l]
pts_rt = [i for l in [int(round(yb_rt, 0))*[x] for x, yb_rt in d_lt] for i in l]

b_lt_skew = round(skew(pts_lt), 2)
b_nm_skew = round(skew(pts_nm), 2)
b_rt_skew = round(skew(pts_rt), 2)

plt.figure(figsize=(12, 5))
plt.plot(x, yb_lt)
plt.plot(x, yb_nm)
plt.plot(x, yb_rt)
plt.hist(pts_lt, bins=100, alpha=0.5)
plt.hist(pts_nm, bins=100, alpha=0.5)
plt.hist(pts_rt, bins=100, alpha=0.5)
plt.title(f'Skewness of Distributions')
plt.legend([b_lt_skew, b_lt_skew, b_nm_skew, b_nm_skew, b_rt_skew, b_rt_skew])
plt.show()
