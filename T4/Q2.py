import  numpy as np
 
x0 = 0.0
xn = 10.0 
n = 10
Erro = 10

Analitico = 334.17814
print("Resultado analítico: ", Analitico, "m\n")

while Erro > 0.001:
    
    n = n+1
    h = (xn-x0)/n
    f = lambda x: np.sqrt((9.81*68.1)/0.25)*np.tanh(np.sqrt((9.81*0.25)/68.1)*x)
    X = np.linspace(x0, xn, n+1)

    Simpson = (h/3)*(f(X[0]) + 4*np.sum(f(X[1:n:2])) + 2*np.sum(f(X[2:n:2]))+ f(X[-1]))
    Erro = np.abs(Analitico - Simpson)
    
print("Número de intervalos: ", n)
print("Deslocamento: ", Simpson, "m")
print("Erro: ", Erro, "\n")
