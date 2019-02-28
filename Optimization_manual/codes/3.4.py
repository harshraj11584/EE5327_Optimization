import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()


plt.plot(0,0,color='black',label="$f(x)= (x_1-8)^2 + (x_2-6)^2 = r^2$ for varying $r$")
r = np.arange(0,5,0.25)
for rad in r:
	c = plt.Circle((8,6),rad,fill=False)
	ax.add_artist(c)
ax.set_xlim([2,15])
ax.set_ylim([0,14])

plt.plot([0,9],[9,0],label="$g(x)= x_1 + x_2 -9 = 0$")
plt.legend(loc='best')
plt.grid()

x = np.array([0,15])
y1 = 9-x
y2 = 40-x
plt.fill_between(x,y1,y2,color='cyan')


plt.savefig('../figs/3.7.pdf')
plt.show()