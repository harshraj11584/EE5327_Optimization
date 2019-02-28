import numpy as np
import matplotlib.pyplot as plt
import time
import scipy as sc
def func(x,c):
	return x**3 - 3*x*c

f = sc.vectorize(func)
plt.title("$y=x^3-3xc$"+" for varying c")
c1= np.arange(-4,4,1)
i=0
x = np.arange(-5,5,0.1)
plt.grid()
for c in c1:
	plt.plot(x, (x**3 - 3*x*c),label="c="+str(c))
	#plt.plot(x,y,label="c="+str(c))
	plt.legend()
	c=c+10
	i=i+1
plt.savefig('../figs/2.1.eps')
plt.show()