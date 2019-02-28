from cvxpy import *
from numpy import matrix
import numpy as np
x = Variable((3,4),nonneg=True)

A = matrix([ [1.0], [1.0],[1.0],[1.0]])
b = matrix([ [22.0], [15.0],[18.0]])
d = matrix([ [7.0], [12.0],[17.0],[9.0]])
e = matrix([ [1.0], [1.0],[1.0]])
# print("A=",A)
# print("b=",b)
# print("d=",d)
c = matrix([[6.0,3.0,5.0,4.0],[5.0, 9.0 ,2.0 , 7.0], [5.0, 7.0 ,8.0 , 6.0]])
# print("c=",c)
f = 0
for i in range(3):
	for j in range(4):
		f = f+c[i,j]*x[i,j]

obj = Minimize(f)
#Constraints
constraints = [x*A <= b , e.transpose()*x>=d.transpose()]

#solution
Problem(obj, constraints).solve()
print("Min Transport Cost = ", f.value)
print("Minima is at x = \n",x.value)