import numpy as np

P = lambda x: -7.2133*10**(-7)*x**3+4.7405*10**(-3)*x**2+1.702*x-2135.36
dP = lambda x: -21.64*10**(-7)*x**2+9.481*10**(-3)*x+1.702

err = 10
x = 1000
x_ant = 0 

while err>= 0.00001:
    
    x = x - P(x)/dP(x)
    err = err = np.amax(np.absolute(x-x_ant))/np.amax(np.absolute(x))
    
    print('x = '+str(x)+', err = '+str(err))
    
    x_ant = x
    
    
    