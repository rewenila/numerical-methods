
import math
e = math.e

f = lambda x: (e**(1/x))/(1+(e**(1/x)))
g = lambda x: 1/((e**(-1/x))+1)

x = 0.1
while(x>0.001):
        print(x, g(x))
        x = x - 0.0001

x = 0.1
while(x>0.001):
        print(x, f(x))
        x = x - 0.0001


