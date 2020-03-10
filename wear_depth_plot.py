import matplotlib
import matplotlib.pyplot as plt
import matplotlib.transforms as transforms
import numpy as np


revolutions = np.array([0, 5, 10, 50, 100, 150, 200, 250, 500, 1000, 2000])

# Data Undoped for plotting
UD_HS_raw_s1_30mm = np.array([0, 0.555,0.816,0.738,1.614,1.607,1.654,1.675, 0, 0, 0])
UD_HS_raw_s1_18mm = np.array([0, 0.418, 0.556, 1.356, 1.356, 1.425, 1.461, 1.506, 0, 0, 0])
UD_HS_raw_s2_30mm = np.array([0, 0.67, 0.66, 1.16, 1.82, 1.85, 1.82, 1.93, 0, 0, 0])
UD_HS_raw_s2_18mm = np.array([0, 0.489, 0.622, 0.798, 1.5432, 1.568, 1.6172, 1.6404, 0, 0, 0])
UD_HS_array = np.array([UD_HS_raw_s1_30mm,UD_HS_raw_s2_30mm, UD_HS_raw_s1_18mm, UD_HS_raw_s2_18mm])

UD_HS_mean = np.mean(UD_HS_array, axis = 0)
UD_HS_std = np.std(UD_HS_array, axis = 0)
print(UD_HS_mean)
#print(UD_HS_std)

# Data Ni-doped for plotting
ND_HS_raw_s1_30mm = np.array([0, 0.426, 0.422, 0.641, 0.717, 1.3786, 1.4544, 1.481, 0, 0, 0])
ND_HS_raw_s1_18mm = np.array([0, 0.333, 0.382, 1.222, 1.2445, 1.2346, 1.2624, 1.3315, 0, 0, 0])
ND_HS_raw_s2_30mm = np.array([0, 0.061, 0.126, 0.200, 0.563, 0.741, 0.593, 0.603, 0, 0, 0])
ND_HS_raw_s2_18mm = np.array([0,0,0,0,0,0,0,0,0,0,0])
ND_HS_array = np.array([ND_HS_raw_s1_30mm,ND_HS_raw_s2_30mm,ND_HS_raw_s1_18mm])

ND_HS_mean = np.mean(ND_HS_array, axis = 0)
ND_HS_std = np.std(ND_HS_array, axis = 0)
#print(ND_HS_mean)
#print(ND_HS_std)


# Data Undoped for plotting
UD_LS_raw_s1_24mm = np.array([0, 0.319, 0.359, 0.417, 0.644, 0.700, 0.729, 0.883, 0.906, 0.956, 1.656])
UD_LS_raw_s1_16_5mm = np.array([0, 0.302, 0.344, 0.457, 0.498, 0.622, 0.670, 0.744, 0.853, 0.926, 1.444])
UD_LS_raw_s2_24mm = np.array([0, 0.546, 0.563, 0.681, 0.800, 0.817, 0.867, 0.922, 0.956, 1.852, 1.870])
UD_LS_raw_s2_16_5mm = np.array([0, 0.341, 0.361, 0.461, 0.506, 0.681, 0.733, 0.815, 0.941, 0.989, 1.511])
UD_LS_array = np.array([UD_LS_raw_s1_24mm, UD_LS_raw_s2_24mm, UD_LS_raw_s1_16_5mm, UD_LS_raw_s2_16_5mm])

UD_LS_mean = np.mean(UD_LS_array, axis=0)
UD_LS_std = np.std(UD_LS_array, axis=0)
print(UD_LS_mean)
print(UD_LS_std)

# Data Ni-doped for plotting
ND_LS_raw_s1_24mm = np.array([0, 0.178, 0.189, 0.233, 0.326, 0.344, 0.439, 0.456, 1.389, 1.356, 1.356])
'''
ND_LS_raw_s1_16_5mm = np.array([0, 0.333, 0.382, 1.222, 1.2445, 1.2346, 1.2624, 1.3315])
ND_LS_raw_s2_24mm = np.array([0, 0.061, 0.126, 0.200, 0.563, 0.741, 0.593, 0.603])
ND_LS_raw_s2_16_5mm = np.array([0, ])'''
ND_LS_array = np.array([ND_LS_raw_s1_24mm])


ND_LS_mean = np.mean(ND_LS_array, axis = 0)
ND_LS_std = np.std(ND_LS_array, axis = 0)
print(ND_LS_mean)
print(ND_LS_std)

# Single plot
fig, ax = plt.subplots()

ax.set_ylim(2,-.5)
ax.set_xlim(-5,1000)

ax.plot(revolutions, UD_HS_mean, 'b^',
        linestyle='--',
        label='Undoped-High Stress MoS$_2$')
ax.errorbar(revolutions, UD_HS_mean, yerr=UD_HS_std, linestyle='None', capsize=5)

ax.plot(revolutions, UD_LS_mean, 'g^',
        linestyle='--',
        label='Undoped-Low Stress- MoS$_2$')
ax.errorbar(revolutions, UD_LS_mean, yerr=UD_LS_std, linestyle='None', capsize=5)

ax.plot(revolutions, ND_HS_mean, 'yo',
        linestyle='--',
        label='Ni-doped-High Stress MoS$_2$')
ax.errorbar(revolutions, ND_HS_mean, yerr=ND_HS_std, linestyle='None', capsize=5)

ax.plot(revolutions, ND_LS_mean, 'ko',
        linestyle='--',
        label='Ni-doped-Low Stress- MoS$_2$')
ax.errorbar(revolutions, ND_LS_mean, yerr=ND_LS_std, linestyle='None', capsize=5)

ax.axhline(y=0.0, linestyle='--', color="green", label='Disk Surface')
#ax.axhline(y=0.8, linestyle='--', color="red", label='Coating Theoretical Thickness')


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

