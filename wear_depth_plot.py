import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# Data Undoped for plotting
t1 = np.arange(50, 300, 50)
s1 = np.array([0.791, 0.840, 0.857, 0.8635, 0.8545])
e1 = [0.1407, 0.1061, 0.0827, 0.1223, 0.1506]

# Data Ni-doped for plotting
t2 = np.arange(50, 300, 50)
s2 = np.array([0.4435, 0.707, 0.594, 0.5705, 0.5465])
e2 = [0.1944, 0, 0.2758, 0.3118, 0.3189]

fig, ax = plt.subplots()

ax.set_ylim(1.2,0)
ax.plot(t1, s1, 'o')
ax.errorbar(t1, s1, yerr=e1,fmt='-')
# arr_img = mpimg.imread('UD_HS_AM_RT_17mm_50rev.png')

ax.set(xlabel='Revolutions', ylabel="Wear depth ($\mu$m)",
       title='Undoped MoS$_2$ High Stress Wear Depth')
#ab = AnnotationBbox(imagebox, (0.4, 0.6))

#ax.add_artist(ab)

ax.grid()

plt.draw()
fig.savefig("UD_HS_AM_RT.png")
plt.show()

