import numpy as np
import matplotlib.pyplot as plt

xData = np.array([0.15, 0.17, 0.19, 0.21, 0.23, 0.25, 0.27, 0.29, 0.31])
yData = np.array([0.1761, 0.2304, 0.2788, 0.3222, 0.3617, 0.3979, 0.4314, 0.4624, 0.4914])


def calculaP(dd,xData,x):
    n = len(xData) - 1
    # Degree of polynomial
    p = dd[n]
    for k in range(1,n+1):
        p = dd[n-k] + (x -xData[n-k])*p
    return p

def difdiv(xData,yData):
    m = len(xData)
    dd = yData.copy()

    for k in range(1,m):
        dd[k:m] = (dd[k:m] - dd[k-1])/(xData[k:m] - xData[k-1])
    return dd


dd = difdiv(xData,yData)

Xplot = np.linspace(0.12, 0.35, 21)
Yplot = []

for x in Xplot:
    Yplot.append(calculaP(dd,xData,x))

plt.plot(xData, yData, "o", Xplot, Yplot, "-")
plt.grid()
plt.show()

print ("P(0.20) =", calculaP(dd,xData,0.20))
print ("P(0.22) =", calculaP(dd,xData,0.22))