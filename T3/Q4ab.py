import numpy as np
import matplotlib.pyplot as plt

T = np.array([0, 5, 10, 20, 30, 40])
u = np.array([1.787, 1.510, 1.307, 1.002, 0.7975, 0.6529])


def calculaP(dd,T,x):
    n = len(T)-1
    # Degree of polynomial
    p = dd[n]
    for k in range(1,n+1):
        p = dd[n-k] + (x -T[n-k])*p
    return p

def difdiv(T,u):
    m = len(T)
    dd = u.copy()

    for k in range(1,m):
        dd[k:m] = (dd[k:m] - dd[k-1])/(T[k:m] - T[k-1])
    return dd


dd = difdiv(T,u)

Xplot = np.linspace(T[0], T[5], 21)
Yplot = []

for x in Xplot:
    Yplot.append(calculaP(dd,T,x))

plt.plot(T, u, "o", Xplot, Yplot, "-")
plt.xlabel('T')
plt.ylabel('μ')
plt.grid()
plt.show()

print ("μ(7.5) =", calculaP(dd,T,7.5))