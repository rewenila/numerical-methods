import numpy as np
from scipy.linalg import solve
import matplotlib.pyplot as plt

X = np.array([0, 5, 10, 20, 30, 40])
Y = np.array([1.787, 1.510, 1.307, 1.002, 0.7975, 0.6529])


# Calcula os elementos das marizes
A11 = np.sum(X**4)
A12 = np.sum(X**3)
A13 = np.sum(X**2)
A23 = np.sum(X)
A33 = len(X)
B1 = np.sum(X**2*Y) 
B2 = np.sum(X*Y)
B3 = np.sum(Y)

# Monta e resolve o sistema
A = np.array([[A11,A12, A13],[A12, A13, A23], [A13, A23, A33]])
B = np.array([B1,B2,B3])
a = solve(A, B)

# define a funcao u(T) para plotar 
u = lambda T: a[0]*T*T+a[1]*T+a[2]

Xr = np.arange(X[0], X[5], 0.00005)
Yr = []
for y in Xr:
    Yr.append(u(y))    

plt.plot(X, Y, ".", Xr, Yr, "-")
plt.xlabel('T')
plt.ylabel('μ')
plt.grid()
plt.show()

print ("μ(7.5) =", u(7.5))