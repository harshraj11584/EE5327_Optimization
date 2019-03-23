from cvxpy import *
import numpy as np
from numpy import matrix

x1 = matrix([[ 2.0], [1.0 ]])
x2 = matrix([[ 0.8], [-0.6 ]])
y1 = 1.0
y2 = -1.0
d= Variable()
w = Variable((2,1),nonneg=False)
# print(type(w))
#Cost function
# f = sum (np.square([w1 for w1 in w]))
f = 0.5*(w[0]**2 + w[1]**2)
# print(type(f))
obj = Minimize(f)
#Constraints
constraints = [ y1* (x1.transpose() * w + d) >=1 , y2* (x2.transpose() * w + d) >=1 ]
#solution
Problem(obj, constraints).solve()
#print(type(f.value))
print("Minimum value of Cost function= ", f.value)
print("Minima is at w = \n",w.value)
print("Minima is at d= ",d.value)