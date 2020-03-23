import matplotlib
import matplotlib.pyplot as plt
import matplotlib.transforms as transforms
import numpy as np


revolutions = np.array([0, 5, 10, 50, 100, 150, 200, 250, 500, 1000, 2000])

# Data Undoped HS for plotting
UD_HS_raw_s1_30mm = np.array([0, 0.555, 0.816, 0.738, 1.614, 1.607, 1.654, 1.67, np.nan, 1.789, np.nan])
UD_HS_raw_s1_18mm = np.array([0, 0.418, 0.556, 1.356, 1.356, 1.425, 1.461, 1.506, np.nan, 1.778, np.nan])
UD_HS_raw_s2_30mm = np.array([0, 0.67, 0.66, 1.16, 1.82, 1.85, 1.82, 1.93, np.nan, 1.878, np.nan])
UD_HS_raw_s2_18mm = np.array([0, 0.489, 0.622, 0.798, 1.5432, 1.568, 1.6172, 1.6404, np.nan, np.nan, np.nan])
#UD_HS_raw_s1_15mm = np.array([0, np.nan, np.nan, np.nan,np.nan, np.nan, np.nan,np.nan, np.nan, 1.789, np.nan])
#UD_HS_raw_s1_22_5mm = np.array([0, np.nan, np.nan, np.nan,np.nan, np.nan, np.nan,np.nan, np.nan, 1.778, np.nan])
#UD_HS_raw_s2_15mm = np.array([0, np.nan, np.nan, np.nan,np.nan, np.nan, np.nan,np.nan, np.nan, 1.878, np.nan])
#UD_HS_raw_s2_22_5mm = np.array([0, np.nan, np.nan, np.nan,np.nan, np.nan, np.nan,np.nan, np.nan, np.nan, np.nan])
UD_HS_array = np.array([UD_HS_raw_s1_30mm,UD_HS_raw_s2_30mm, UD_HS_raw_s1_18mm, UD_HS_raw_s2_18mm])

UD_HS_mean = np.mean(UD_HS_array, axis = 0)
UD_HS_std = np.std(UD_HS_array, axis = 0)
print(UD_HS_mean)
print(UD_HS_std)

# Data Ni-doped HS for plotting
ND_HS_raw_s1_30mm = np.array([0, 0.426, 0.422, 0.641, 0.717, 1.3786, 1.4544, 1.481, np.NA, 1.667, np.NA])
ND_HS_raw_s1_18mm = np.array([0, 0.333, 0.382, 1.222, 1.2445, 1.2346, 1.2624, 1.3315, np.NA, 1.656, np.NA])
ND_HS_raw_s2_30mm = np.array([0, 0.061, 0.126, 0.200, 0.563, 0.741, 0.593, 0.603, np.NA, 0.844, np.NA])
ND_HS_raw_s2_18mm = np.array([0, 0.068, 0.0704, 0.037, 0.326, 0.548, 0.681, 0.852, np.NA, 0.833, np.NA])
#ND_HS_raw_s1_15mm = np.array([0, np.nan, np.nan, np.nan,np.nan, np.nan, np.nan,np.nan, np.nan, 1.667, np.nan])
#ND_HS_raw_s1_28_5mm = np.array([0, np.nan, np.nan, np.nan,np.nan, np.nan, np.nan,np.nan, np.nan, 1.656, np.nan])
#ND_HS_raw_s2_15mm = np.array([0, np.nan, np.nan, np.nan,np.nan, np.nan, np.nan,np.nan, np.nan, 0.844, np.nan])
#ND_HS_raw_s2_28_5mm = np.array([0, np.nan, np.nan, np.nan,np.nan, np.nan, np.nan,np.nan, np.nan, 0.833, np.nan])

ND_HS_array = np.array([ND_HS_raw_s1_30mm,ND_HS_raw_s2_30mm,ND_HS_raw_s1_18mm, ND_HS_raw_s2_18mm])


ND_HS_mean = np.mean(ND_HS_array, axis = 0)
ND_HS_std = np.std(ND_HS_array, axis = 0)
print(ND_HS_mean)
print(ND_HS_std)


# Data Undoped LS for plotting
UD_LS_raw_s1_24mm = np.array([0, 0.319, 0.359, 0.417, 0.644, 0.700, 0.729, 0.883, 0.906, 0.956, 1.656])
UD_LS_raw_s1_16_5mm = np.array([0, 0.302, 0.344, 0.457, 0.498, 0.622, 0.670, 0.744, 0.853, 0.926, 1.444])
UD_LS_raw_s2_24mm = np.array([0, 0.546, 0.563, 0.681, 0.800, 0.817, 0.867, 0.922, 0.956, 1.852, 1.87])
UD_LS_raw_s2_16_5mm = np.array([0, 0.341, 0.361, 0.461, 0.506, 0.681, 0.733, 0.815, 0.941, 0.989, 1.511])

UD_LS_array = np.array([UD_LS_raw_s1_24mm, UD_LS_raw_s2_24mm, UD_LS_raw_s1_16_5mm, UD_LS_raw_s2_16_5mm])

UD_LS_mean = np.mean(UD_LS_array, axis=0)
UD_LS_std = np.std(UD_LS_array, axis=0)
print(UD_LS_mean)
print(UD_LS_std)

# Data Ni-doped LS for plotting
ND_LS_raw_s1_24mm = np.array([0, 0.178, 0.189, 0.233, 0.326, 0.344, 0.439, 0.456, 1.389, 1.356, 1.356])
ND_LS_raw_s1_16_5mm = np.array([0, 0.222, 0.302, 0.368, 0.46, 0.526, 0.521, 0.578, 0.63, 0.844, 0.902])
ND_LS_raw_s2_24mm = np.array([0, 0.037, 0.067, 0.178, 0.25, 0.293, 0.396, 0.5, 0.524, 0.563, 0.589])
ND_LS_raw_s2_16_5mm = np.array([0, 0.67, 0.057, 0.141, 0.124, 0.159, 0.181, 0.328, 0.367, 0.422, 0.45])
ND_LS_array = np.array([ND_LS_raw_s1_24mm, ND_LS_raw_s2_24mm, ND_LS_raw_s1_16_5mm, ND_LS_raw_s2_16_5mm])


ND_LS_mean = np.mean(ND_LS_array, axis = 0)
ND_LS_std = np.std(ND_LS_array, axis = 0)
print(ND_LS_mean)
print(ND_LS_std)

# Single plot
fig, ax = plt.subplots()

ax.set_ylim(2,-1)
ax.set_xlim(-5,2050)

ax.plot(revolutions, UD_HS_mean, 'b^',
        linestyle='--',
        label='UD-HS MoS$_2$')
ax.errorbar(revolutions, UD_HS_mean,
            yerr=UD_HS_std,
            ecolor='b',
            linestyle='None',
            capsize=5)

ax.plot(revolutions, UD_LS_mean, 'g^',
        linestyle='--',
        label='UD-LS- MoS$_2$')
ax.errorbar(revolutions, UD_LS_mean,
            yerr=UD_LS_std,
            linestyle='None',
            ecolor='g',
            capsize=5)

ax.plot(revolutions, ND_HS_mean, 'yo',
        linestyle='--',
        label='Ni-HS MoS$_2$')
ax.errorbar(revolutions, ND_HS_mean,
            yerr=ND_HS_std,
            linestyle='None',
            ecolor='y',
            capsize=5)

ax.plot(revolutions, ND_LS_mean, 'ko',
        linestyle='--',
        label='Ni-LS- MoS$_2$')
ax.errorbar(revolutions, ND_LS_mean,
            yerr=ND_LS_std,
            linestyle='None',
            ecolor='k',
            capsize=5)

ax.axhline(y=0.0, linestyle='--', color="green", label='Disk Surface')
#ax.axhline(y=0.8, linestyle='--', color="red", label='Coating Theoretical Thickness')


ax.set(xlabel='Revolutions', ylabel="Wear depth ($\mu$m)",
       title='Wear Depth')
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

