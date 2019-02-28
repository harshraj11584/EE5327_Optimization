import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np 

x = np.outer(np.linspace(-12, 28, 100), np.ones(100))
y = x.copy().T
z = (x-8)**2+(y-6)**2

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.plot_surface(x, y, z, cmap=plt.cm.jet, rstride=1, cstride=1, linewidth=0)
ax.text2D(0.05, 0.99, "Objective $r^2 = f(x_1,x_2) = (x_1 -8)^2 + (x_2 - 6)^2$", transform=ax.transAxes)
ax.text2D(0.05, 1.11, '◼ : Feasible Region $x_1+x_2=9$', transform=ax.transAxes , color='brown')
ax.set_xlabel('$x_1 Axis $')
ax.set_ylabel('$x_2 Axis $')
ax.set_zlabel('$f(x_1,x_2)$')
ax.set_xlim(-12, 28)
ax.set_ylim(-12, 28)
ax.set_zlim(-100, 900)
xs = np.linspace(-12, 28, 100)
zs = np.linspace(-100, 900, 100)

X, Z = np.meshgrid(xs, zs)
Y = 9 - X
ax.plot_surface(X, Y, Z ,color='brown')

ax.scatter(5.5,3.5,12.5,c='green',s=320,marker='o')
plt.show()