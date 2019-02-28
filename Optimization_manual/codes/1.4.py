import numpy as np
import matplotlib.pyplot as plt
import scipy as sc
def sq(x):
	return x**2
x = np.linspace(0.5,8,50)#points on the x axis
f=sc.vectorize(sq)#Objective function
y= f(x)
plt.plot(x,y,color=(1,0,1), label="$f(x)=x^2$")
plt.grid()
plt.xlabel('$x$')
plt.ylabel('$x^2$')
#Plot commands
#Plotting line segments with x>0 and y=logx 
#color used to color each line with a different color
plt.plot([1,4],[sq(1),sq(4)],color=(1,0,0),marker='o',label="($1$,$(1)^2$)-($4$,$(4)^2$)")
plt.plot([2,6],[sq(2),sq(6)],color=(0,1,0),marker='o',label="($2$,$(2)^2$)-($6$,$(6)^2$)")
plt.plot([3,5],[sq(3),sq(5)],color=(0,0,1),marker='o',label="($3$,$(3)^2$)-($5$,$(5)^2$)")
plt.legend(loc='best')
plt.savefig('../figs/1.4.pdf')
plt.show()
#Reveals the plot










