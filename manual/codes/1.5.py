from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

def f(x1, x2):
    return x1*x2

x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 100, cmap='binary')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z');
ax.plot((-2,4),(4,-2),(-6,-6),label="chord")
plt.legend(loc='best')
plt.savefig('../figs/1.5.pdf')
plt.show()

print("Chord is below curve, hence not convex")






