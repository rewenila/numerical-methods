import numpy as np
import matplotlib.pyplot as plt

x0 = 0.0
xn = 2.0
h = 0.25
#n = (xn-x0)/h + 1
#n=9 para h=0.25, n=21 para h=0.10, n=41 para h=0.05
n = 9

X = np.arange(x0, xn+h, h) 
Y = np.array([0.0]*n)  
M = []       
K = np.array([0.0]*n)     

print("h = ", h)

for i in range(1,n):
    K[i] = (X[i-1])**2*(5-(Y[i-1]))
    Y[i] = Y[i-1] + (K[i])*h
    print("i = ", i, ", t = {:.5f}".format(X[i]), ", u = {:.5f}".format(Y[i]), ", k = {:.5f}".format(K[i]))
    
#derivada segunda da solução analítica
d2 = lambda x: 5*(-np.exp((-x**3)/3)*x**4+2*np.exp((-x**3)/3)*x) 

#máximo
for x in X[0:n]:
    M.append(d2(x))

erro = (h**2/2)*np.max(M)
print("\nErro máximo para h = ", h, ": ", erro)


Xex = np.arange(0, 2, 0.01)
Yex = []
sol_ex = lambda x: 5 - 5*np.exp(-x**3/3)

for x in Xex:
    Yex.append(sol_ex(x))

#plots
plt.plot(X, Y, "r-", Xex, Yex, "b-")
plt.grid()
plt.show()