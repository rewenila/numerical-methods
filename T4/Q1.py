import  numpy as np
 
x0 = 0.0
xn = 3.0 
n = 12

h = (xn-x0)/n
f = lambda x: x**2*(np.exp(x))

X = np.linspace(x0, xn, n+1)

Analitico = 98.42768
print("Resultado analítico: ", Analitico, "\n")

Trapz = (h/2)*(f(X[0]) + 2*np.sum(f(X[1:n])) + f(X[-1]))
print("Resultado Trapézio: ", Trapz)
print("Erro: ", np.abs(Analitico - Trapz), "\n")

Simpson1 = (h/3)*(f(X[0]) + 4*np.sum(f(X[1:n:2])) + 2*np.sum(f(X[2:n:2]))+ f(X[-1]))
print("Resultado 1/3 Simpson: ", Simpson1)
print("Erro: ", np.abs(Analitico - Simpson1), "\n")

Simpson2 = (3*h/8)*(f(X[0]) + 3*np.sum(f(X[1:n:3])+f(X[2:n:3])) + 2*np.sum(f(X[3:n:3]))+ f(X[-1]))
print("Resultado 3/8 Simpson: ", Simpson2)
print("Erro: ", np.abs(Analitico - Simpson2))
