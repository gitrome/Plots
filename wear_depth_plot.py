import matplotlib
import matplotlib.pyplot as plt
import matplotlib.transforms as transforms
import numpy as np
from sqlalchemy.sql.functions import sum

revolutions = np.array([0, 5, 10, 50, 100, 150, 200, 250])

# Data Undoped for plotting
UD_raw_s1 = np.array([0, 0.555,0.816,0.738,1.614,1.607,1.654,1.675])
UD_raw_s2 = np.array([0, 0.67, 0.66,1.16,1.82,1.85,1.82,1.93])

UD_mean = np.mean([UD_raw_s1,UD_raw_s2], axis = 0)
UD_std = np.std([UD_raw_s1,UD_raw_s2], axis = 0)
print(UD_mean)
print(UD_std)

'''
# Data Ni-doped for plotting
ND_raw_s1 = np.array([0, ])
ND_raw_s2 = np.array([0, ])
'''



# Single plot
fig, ax = plt.subplots()

ax.set_ylim(2,-.5)
ax.set_xlim(-5,300)
ax.plot(revolutions, UD_mean, 'o', label='Undoped MoS$_2$')
ax.errorbar(revolutions, UD_mean, yerr=UD_std)
ax.axhline(y=0.0, linestyle='--', color="green", label='Disk Surface')
ax.axhline(y=0.8, linestyle='--', color="red", label='Coating Theoretical Thickness')


ax.set(xlabel='Revolutions', ylabel="Wear depth ($\mu$m)",
       title='High Stress Wear Depth')
ax.grid()
ax.legend()

plt.draw()
fig.savefig("test.png")
plt.show()

'''
# 2 Subplots
def plot_wear_depth(t1,s1,t2,s2)

       fig, (ax1, ax2) = plt.subplots(2, 1)
       fig.subplots_adjust(hspace=0.5)

       ax1.set_ylim(1.05,-0.5)
       ax1.set_xlim(-5,300)
       ax1.plot(t1, s1, 'ko')
       ax1.axhline(y = 0.0, linestyle= '--', color="green")
       ax1.axhline(y = 0.8, linestyle='--', color="red")
       ax1.errorbar(t1, s1, yerr=e1,fmt='p', ecolor='blue')

       ax1.set(xlabel='Revolutions', ylabel="Wear depth ($\mu$m)",
       title='Undoped MoS$_2$ High Stress Wear Depth')
       ax1.grid()

       ax2.set_ylim(1.05,-0.5)
       ax2.set_xlim(-5,300)
       ax2.plot(t2, s2, 'ro')
       ax2.axhline(y = 0.0, linestyle= '--', color="green")
       ax2.axhline(y = 0.8, linestyle= '--', color="red")
       ax2.errorbar(t2, s2, yerr=e2,fmt='p', ecolor='blue')

       ax2.set(xlabel='Revolutions', ylabel="Wear depth ($\mu$m)",
       title='Ni Doped MoS$_2$ High Stress Wear Depth')
       ax2.grid()

       plt.draw()
       fig.savefig("UD_HS_AM_RT.png")
       plt.show()
'''

