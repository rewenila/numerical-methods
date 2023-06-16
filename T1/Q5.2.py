import math

ln_ant = 0
n = 1

err = 100
x = -0.2

while(err>=0.0001):
    ln = ln_ant + (((-1)**(n+1))/n)*x**n
    err = ln - math.log(0.8)
    print('Valor com ' + str(n) + ' termos = ', ln)
    print('Erro = ', err)
    
    ln_ant = ln
    n = n+1

