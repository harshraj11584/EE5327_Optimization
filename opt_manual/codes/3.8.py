import matplotlib.pyplot as plt
import numpy as np 

fig, ax = plt.subplots()

plt.plot(0,0,color='black',label="$f(x)= (x_1-8)^2 + (x_2-6)^2 = r^2$ for varying $r$")
r = np.arange(0,5,0.25)
for rad in r:
	c = plt.Circle((8,6),rad,fill=False)
	ax.add_artist(c)
ax.set_xlim([2,15])
ax.set_ylim([-2,14])

plt.plot([0,18],[18,0],label="$g(x)= x_1 + x_2 -18 = 0$")
plt.legend(loc='best')
plt.grid()
plt.savefig('../figs/3.8.pdf')
plt.show()
