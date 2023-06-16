import matplotlib.pyplot as plt
import numpy as np

X = [0.15, 0.17, 0.19, 0.21, 0.23, 0.25, 0.27, 0.29, 0.31]
Y = [0.1761, 0.2304, 0.2788, 0.3222, 0.3617, 0.3979, 0.4314, 0.4624, 0.4914]

n = len(Y)

def calculaP(x):
    valor = 0
    for k in range(n):
        lk = 1.0
        for i in range(n):
            if k != i:
                lk = lk*(x - X[i])/(X[k]-X[i])
        valor = valor + Y[k]*lk 
    return valor

Ynew = []
Xnew = np.linspace(X[0], X[-1], num=21)
for xnew in Xnew:
    ynew = calculaP(xnew)
    Ynew.append(ynew)

plt.plot(X, Y, 'o', Xnew, Ynew,'-')
plt.grid()
plt.show()

x = 0.20
y = 0.22

print ("P(",x,") =", calculaP(x))
print ("P(",y,") =", calculaP(y))