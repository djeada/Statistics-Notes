import matplotlib.pyplot as plt


def PDF(x, mean=0, std_dev=1):
    # define e and pi explicitly
    e = 2.718281828
    pi = 3.1415927
    # calculate in two steps
    p = 1.0 / (std_dev * ((2 * pi) ** 0.5))
    p *= e ** (-0.5 * ((x - mean)/std_dev)**2)
 
    return p


def CDF(mean=0, std_dev=1, x_left=-5, x_right=5, width=0.0001):
    CDF = 0
    X = []  # for plotting only
    CDF_y = []  # for plotting only
 
    x = x_left + width / 2
    while x < x_right:
        X.append(x)  # for plotting only
        panel = PDF(x, mean, std_dev) * width  # panel under PDF
        CDF += panel  # running sum of panels = integration
        CDF_y.append(CDF)  # for plotting only
        x += width  # current x value
       
    return CDF, X, CDF_y


total_integral, X, CDF_y = CDF()
P = [PDF(x) for x in X]
total_integral = round(total_integral, 5)
msg = f'Total integral of PDF = {total_integral}'
print(msg)
plt.plot(X, P)
plt.plot(X, CDF_y)
plt.show()
