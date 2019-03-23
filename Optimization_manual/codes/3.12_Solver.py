from cvxpy import *
import numpy as np
from numpy import matrix

x = Variable((2,1),nonneg=False)
f = 4*x[0]**2 + 2*x[1]**2
#print(type(f))
obj = Minimize(f)
#Constraints
constraints = [ 3*x[0]+x[1]-8>=0, 15-2*x[0]-4*x[1]>=0 ,3*x[0]+x[1]-8<=0]
#solution
Problem(obj, constraints).solve()
#print(type(f.value))
print("Minimum value of Cost function= ", f.value)
print("Minima is at x1,x2 = \n",x.value)