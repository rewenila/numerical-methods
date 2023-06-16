import numpy as np
import matplotlib.pyplot as plt

o = np.array([50.0, 52.0, 54.0]) #[50.0, 52.0, 54.0, 56.6, 58.0, 60.0]
F = np.array([2.75, 1.45, 0.50]) #[2.75, 1.45, 0.50, 0.15, 0.20, 0.85]


def evalPoly(dd,F,x):
    n = 2
    # Degree of polynomial
    p = dd[n]
    for k in range(1,n+1):
        p = dd[n-k] + (x -F[n-k])*p
    return p

def coeffts(F,o):
    m = len(F)
    # Number of data points
    dd = o.copy()

    for k in range(1,m):
        dd[k:m] = (dd[k:m] - dd[k-1])/(F[k:m] - F[k-1])
    return dd


dd = coeffts(F,o)

ob = evalPoly(dd,F,0.00)

Xplot = np.linspace(-0.1, 3.0, 21)
Yplot = []

for x in Xplot:
    Yplot.append(evalPoly(dd,F,x))

plt.plot(F, o, "o", Xplot, Yplot, "-")
plt.scatter(0.0, ob, color = "black")
plt.ylabel('θ')
plt.xlabel('F')
plt.grid()
plt.show()

print("F(0)=",evalPoly(dd,F,0.00))