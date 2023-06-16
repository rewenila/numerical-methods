import math

a = 0.1
b = 10
err = 10

f = lambda x: x-1

while err>0.00001:
    x = (a+b)/2
    if f(a)*f(x)<0:
        b = x
    else:
        a = x
    err = abs(b-a)/abs(b)
    print(x, err)

