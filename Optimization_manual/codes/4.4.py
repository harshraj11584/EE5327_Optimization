from cvxopt import matrix
from cvxopt import solvers

c = matrix([-1.,-2.,-5.])
G = [ matrix([[-1.],[ -1.],[0.]]) , matrix([[-1.],[ 0.],[0.]]) , matrix([[0.],[ -1.],[0.]]) , matrix([[0.],[ 0.],[-1.]]), matrix([[-1.,0.,0.,0.],[0.,-1.,-1.,0.],[0.,00.,0.,-1.]]) ]

Aval = matrix([2.,3.,1.],(1,3))
bval = matrix([7.])

h = [ matrix([-1.]) , matrix([0.]) , matrix([0.]) , matrix([0.]) , matrix([[0.,0.],[0.,0.]])]

sol = solvers.sdp(c, Gs=G, hs=h,A=Aval, b=bval)
                          
print("c=",c)
print("G=",G)
print("aval=",Aval)
print("BVAL=",bval)
print("h=",h)
print("\n\nSol=\n",sol['x'])