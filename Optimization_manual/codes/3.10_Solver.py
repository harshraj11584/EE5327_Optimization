from cvxpy import *
import numpy as np
from numpy import matrix

x = Variable((2,1),nonneg=False)
# w = Variable((2,1),nonneg=False)
# # print(type(w))
# #Cost function
# # f = sum (np.square([w1 for w1 in w]))
f = (x[0]-8)**2 + (x[1]-6)**2
print(type(f))
obj = Minimize(f)
#Constraints
constraints = [ x[0]+x[1]-18>=0 ]
#solution
Problem(obj, constraints).solve()
#print(type(f.value))
print("Minimum value of Cost function= ", f.value)
print("Minima is at x1,x2 = \n",x.value)