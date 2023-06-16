ln_ant = 0
n = 1
x = 0

for n in range(1, 11, 1):
    ln = ln_ant + (((-1)**(n+1))/n)*x**n
    print('Valor com ' + str(n) + ' termos da série = ', ln)
    ln_ant = ln
 

