from cvxpy import *
from numpy import matrix
import numpy as np

x = Variable((2,1))
A = matrix([
	[6.0, 6.0],
	[8.0, 2.0], 
	[5.0, -3.0],
	[0.0, 1.0], 
	[-1.0, 0.0],
	[0.0 , -1.0]	
	])
b = matrix([
	[55.0],
	[30.0],
	[18.0],
	[28.0],
	[0.0],
	[0.0]
	])

f = 3*x[0,0]+5*x[1,0]
obj = Maximize(f)

constraints = [A*x <= b ]

#solution
Problem(obj, constraints).solve()
print("Max Cost = ", f.value)
print("Maxima is at x = \n",x.value)