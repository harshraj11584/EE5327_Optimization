from cvxpy import *
from numpy import matrix
import numpy as np

p = matrix([
	[0, -4 , 0],
	[0, 0 , 2],
	[0, -6 , -8],
	])

print("Penalty Matrix for given solution = \n",p)
print("As p(2,3)=2>0, initial solution given is not optimal\n\n")

x = Variable((3,3),nonneg=True)

A = matrix([ [1.0], [1.0],[1.0] ])
b = matrix([ [40.0], [60.0],[10.0] ])
d = matrix([ [40.0], [50.0],[20.0] ])
e = matrix([ [1.0], [1.0],[1.0]])
# print("A=",A)
# print("b=",b)
# print("d=",d)
c = matrix([
	[2.0, 1.0 , 2.0],
	[9.0, 4.0 , 7.0], 
	[1.0, 2.0 , 9.0]
	])
# print("c=",c)
f = 0
for i in range(3):
	for j in range(3):
		f = f+c[i,j]*x[i,j]

obj = Minimize(f)
#Constraints
constraints = [x*A <= b , e.transpose()*x>=d.transpose()]

#solution
Problem(obj, constraints).solve()
print("Min Transport Cost = ", f.value)
print("Minima is at x = \n",x.value)