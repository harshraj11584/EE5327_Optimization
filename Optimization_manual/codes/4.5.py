import matplotlib.pyplot as plt
import numpy as np 


x = np.linspace(0, 20, 5000)
y1 = ((-3*x)+(x**2+28*x)**0.5)/2.0
plt.plot(x,y1,label="$f(x,y_1)<=0$",color='blue')
y2 = ((-3*x)-(x**2+28*x)**0.5)/2.0
plt.plot(x,y2,color='blue')

plt.plot((0,20),(1,-19),label = "$x_{11} + x_{12} >= 1$")
plt.plot((-1,20),(0,0),label = "$x_12 >= 0$")
plt.plot((0,0),(-1,20),label = "$x_11 >= 0$")
plt.plot((0,7.0/3.0),(7.0/2.0,0),label = "$7-2x_{11} - 3x_{12} >= 0$")

plt.xlim(-100,40)
plt.ylim(-100,40)

plt.plot((0,200),(((35-0.21)/13.0),(35-0.21-9*200)/13.0),label="obj")

plt.legend()
plt.show()