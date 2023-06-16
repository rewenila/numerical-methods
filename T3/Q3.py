import numpy as np
from scipy.linalg import solve
import matplotlib.pyplot as plt

X = np.array([0.0, 0.002, 0.006, 0.012, 0.018, 0.024])
Y = np.array([0.0, 0.287, 0.899, 1.915, 3.048, 4.299])


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
print ('u =',a[0],'y^2 +',a[1],'y +', a[2])

# define a funcao g(x) para plotar 
u = lambda y: a[0]*y*y+a[1]*y+a[2]

# cria pontos (x, y) da reta 
Xr = np.arange(X[0], X[5], 0.00005)
Yr = []
for y in Xr:
    Yr.append(u(y))    

# Plota os pontos e a reta
plt.plot(X, Y, ".", Xr, Yr, "-")
plt.xlabel('y')
plt.ylabel('u')
plt.grid()
plt.show()

dudy = 2*a[0]*0+a[1]

t = (1.8*10**(-5))*dudy
print('t =', t)