import numpy as np
import matplotlib.pyplot as plt

h = 0.5
x0 = 0.0
xn = 25

X = np.arange(x0, xn+h, h) 
#print ("pontos xi:", X)

Y = [0.0]                  

f = lambda x: 0.5*12*((100*(20-2.5)*(20-x))/(100-2.5*x))
#print(f(0))

for x in X[0:-1]:
    Y.append(Y[-1] + f(x)*h)
    
print ("pontos yi:", Y)


print(X)
print(len(X))
print(Y)
print(len(Y))
plt.plot(X, Y, "r-")
plt.grid()
plt.show()