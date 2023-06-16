import numpy as np

def decomposicaoLU(A):

    L = []
    U = []

    for i in range(n):
        L.append([0]*n)
        U.append([0]*n)  
    
    for m in range(n):
        L[m][m] = 1
        
        soma = 0    
        for k in range(n):
            soma = soma + L[m][k]*U[k][m]
        U[m][m] = A[m][m] - soma   
            
        for j in range(m,n):
            soma = 0
            for k in range(m):
                soma =  soma + L[m][k]*U[k][j]
            U[m][j] = A[m][j] - soma
            
        for i in range(m+1,n):
            soma = 0
            for k in range(m+1):
                soma = soma +  L[i][k]*U[k][m]
            L[i][m] = (A[i][m] - soma)/U[m][m]
            
    print('U = \n'+str(np.matrix(U))+'\n')
    print('L = \n'+str(np.matrix(L))+'\n')
    
    return L, U

def inferior(L, b):
    
    y1 = b[0]/L[0][0]
    y = [y1]
    
    for i in range(1,len(L)):
        soma = 0
        for j in range(0,i):
            soma = soma +  L[i][j]*y[j]
        y.append((b[i] - soma)/L[i][i])
        
    print('y = '+str(np.matrix(y))+'\n')
    
    return y

def superior(U, y):
    n = len(U)-1       
    xn = y[n]/U[n][n]

    x = [0]*len(U)       
    x[-1] = xn         
    
    for i in range(n-1,-1,-1):
        soma = 0
        for j in range(i+1,n+1):
            soma = soma +  U[i][j]*x[j]
        xi = (y[i]-soma)/U[i][i]
        x[i] = xi
        
    print('x = '+str(np.matrix(x)))
    
    return x
    
A = [[2.0,  3.0,  1.0,  5.0],
     [1.0,  3.5,  1.0,  7.5],
     [1.4,  2.7,  5.5,  12 ],
     [-2.0, 1.0,  3.0,  28 ]]

b = [11, 13, 21.6, 30]

n = 4

decomposicaoLU(A)
y = inferior(L, b)
superior(U, y)
