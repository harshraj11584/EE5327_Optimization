from cvxpy import *
from numpy import matrix
import numpy as np

x = Variable((4,1))
A = matrix([
	[6.0, 8.0 , 5.0 , 0.0],
	[6.0, 2.0 , -3.0, 1.0], 
	[1.0, 0.0 , 0.0, 0.0],
	[0.0, 1.0 , 0.0, 0.0],
	[0.0, 0.0 , 1.0, 0.0],
	[0.0, 0.0 , 0.0, 1.0]
	])
b = matrix([
	[3.0],
	[5.0],
	[0.0],
	[0.0],
	[0.0],
	[0.0]
	])

f = 55*x[0,0]+30*x[1,0]+18*x[2,0]+28*x[3,0]
obj = Minimize(f)

constraints = [A*x >= b ]

#solution
Problem(obj, constraints).solve()
print("Min Cost = ", f.value)
print("Minima is at x = \n",x.value)