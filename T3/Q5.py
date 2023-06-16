import numpy as np
from scipy.linalg import solve
import matplotlib.pyplot as plt

X = np.array([ 0.0004, 0.0011, 0.0021, 0.0031])
Y = np.array([ 5.775, 8.577, 10.874, 12.555])
X1 = np.log10(X)
Yl = np.log10(Y) 

# montando a matriz do sistema
A = np.array([[np.sum(X1*X1), np.sum(X1)],
              [np.sum(X1),   len(X1)]])
B = np.array([np.sum(X1*Yl), np.sum(Yl)])

a = solve(A, B)

h = lambda X1: a[0]*X1 + a[1]
X1r = np.linspace(X1[0], X1[-1], 51)
plt.plot(X1, Yl, "o", X1r, h(X1r), "-") 
plt.grid()
plt.show()
print('y =',a[0],'x','+',a[1])
  
B = 10**(a[1])
m = (a[0])
y = lambda x: B*x**m

Xr = np.linspace(X[0], X[-1], 51)
Yr = y(Xr)
plt.plot(X, Y, "o", Xr, Yr, "-") 
plt.grid()
plt.show()
print('B =', B)
print('m =', m)
print('ε = ', B, 'σ ^(', m, ')')