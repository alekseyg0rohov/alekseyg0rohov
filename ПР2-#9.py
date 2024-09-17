from math import *

x = float(1.825*10**2)
y = float(18.225)
z = float(-3.298*10**(-2))

s = fabs(x**(y/x) - (y/x)**(1/3)) + (y-x) * ((cos(y) - (z / (y-x))) / (1 + (y-x)**2))

print('%.5f'%(s))