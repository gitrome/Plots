import matplotlib
import matplotlib.pyplot as plt
import matplotlib.transforms as transforms
import numpy as np

# Data Undoped for plotting
t1 = np.arange(50, 300, 50)
s1 = np.array([0.791, 0.840, 0.857, 0.8635, 0.8545])
e1 = [0.1407, 0.1061, 0.0827, 0.1223, 0.1506]

# Data Ni-doped for plotting
t2 = np.arange(50, 300, 50)
s2 = np.array([0.4435, 0.707, 0.594, 0.5705, 0.5465])
e2 = [0.1944, 0, 0.2758, 0.3118, 0.3189]

# Single plot
#fig, ax = plt.subplots()

#ax.set_ylim(1.2,0)
#ax.plot(t1, s1, 'o')
#ax.errorbar(t1, s1, yerr=e1,fmt='p')
#ax.plot(t2, s2, 'o')
#ax.errorbar(t2, s2, yerr=e2,fmt='p')

#ax.set(xlabel='Revolutions', ylabel="Wear depth ($\mu$m)",
#       title='Undoped MoS$_2$ High Stress Wear Depth')


#ax.grid()

# 2 Subplots

fig, (ax1, ax2) = plt.subplots(2, 1)
fig.subplots_adjust(hspace=0.5)

ax1.set_ylim(1.2,0)
ax1.plot(t1, s1, 'ko')
ax1.axhline(y = 0.8, linestyle='--', color="red")
ax1.errorbar(t1, s1, yerr=e1,fmt='p', ecolor='blue')

#trans = transforms.blended_transform_factory(
#    ax1.get_yticklabels()[0].get_transform(), ax1.transData)
#ax1.text(0,0.8, "{:.0f}".format(0.8), color="red", transform=trans,
#        ha="left", va="center")

ax1.set(xlabel='Revolutions', ylabel="Wear depth ($\mu$m)",
       title='Undoped MoS$_2$ High Stress Wear Depth')
ax1.grid()

ax2.set_ylim(1.2,0)
ax2.plot(t2, s2, 'ro')
ax2.axhline(y = 0.8, linestyle= '--', color="red")
ax2.errorbar(t2, s2, yerr=e2,fmt='p', ecolor='blue')

ax2.set(xlabel='Revolutions', ylabel="Wear depth ($\mu$m)",
       title='Ni Doped MoS$_2$ High Stress Wear Depth')
ax2.grid()

plt.draw()
fig.savefig("UD_HS_AM_RT.png")
plt.show()

