from cvxpy import *
from numpy import matrix
import numpy as np
from scipy.optimize import linear_sum_assignment


# c = matrix([
# 	[5.0, 3.0 ,2.0 , 8.0],
# 	[7.0, 9.0 ,2.0 , 6.0], 
# 	[6.0, 4.0 ,5.0 , 7.0],
# 	[5.0, 7.0 ,7.0 , 8.0]
# 	])

# row,col = linear_sum_assignment(c)

# print(c[row,col].sum())

# print(row)
# print(col)

c = matrix([
	[5.0, 3.0 ,2.0 , 5.0],
	[7.0, 9.0 ,2.0 , 3.0], 
	[4.0, 2.0 ,3.0 , 2.0],
	[5.0, 7.0 ,7.0 , 5.0]
	])

row,col = linear_sum_assignment(c)

print("Min time required is = ",c[row,col].sum())

# print(row)
# print(col)