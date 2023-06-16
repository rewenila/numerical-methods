import  numpy as np
 
x0 = 0.0
xn = 1200.0 
n = 6

h = (xn-x0)/n

p = np.array([4.00, 3.95, 3.80, 3.60, 3.41, 3.30, 3.20])
a = np.array([100, 103, 110, 120, 133, 150, 170])
f = p*a

Simpson = ((h/3)*((f[0]) + 4*np.sum(f[1:n:2]) + 2*np.sum(f[2:n:2])+ f[-1]))/1000

print("Massa: ", Simpson, "Kg")
