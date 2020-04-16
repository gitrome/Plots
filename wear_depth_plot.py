import matplotlib
import matplotlib.pyplot as plt
import matplotlib.transforms as transforms
import numpy as np


revolutions = np.array([0, 5, 10, 50, 100, 150, 200, 250, 500, 1000])

# Data Undoped HS for plotting
UD_HS_raw_s1_30mm = np.array([0, 0.555, 0.816, 0.738, 1.614, 1.607, 1.654, 1.67, np.nan, np.nan])
UD_HS_raw_s1_18mm = np.array([0, 0.418, 0.556, 1.356, 1.356, 1.425, 1.461, 1.506, np.nan, np.nan])
UD_HS_raw_s2_30mm = np.array([0, 0.67, 0.66, 1.16, 1.82, 1.85, 1.82, 1.93, np.nan, np.nan])
UD_HS_raw_s2_18mm = np.array([0, 0.489, 0.622, 0.798, 1.5432, 1.568, 1.6172, 1.6404, np.nan, np.nan])
UD_HS_raw_s1_15mm = np.array([0, np.nan, np.nan, np.nan,np.nan, np.nan, np.nan,np.nan, np.nan, 1.789])
UD_HS_raw_s1_22_5mm = np.array([0, np.nan, np.nan, np.nan,np.nan, np.nan, np.nan,np.nan, np.nan, 1.778])
UD_HS_raw_s2_15mm = np.array([0, np.nan, np.nan, np.nan,np.nan, np.nan, np.nan,np.nan, np.nan, 1.878])
UD_HS_raw_s2_22_5mm = np.array([0, np.nan, np.nan, np.nan,np.nan, np.nan, np.nan,np.nan, np.nan, np.nan])

UD_HS_array = np.array([UD_HS_raw_s1_30mm,UD_HS_raw_s2_30mm, UD_HS_raw_s1_18mm, UD_HS_raw_s2_18mm,
                        UD_HS_raw_s1_15mm, UD_HS_raw_s1_22_5mm, UD_HS_raw_s2_15mm, UD_HS_raw_s2_22_5mm])

UD_HS_mean = np.nanmean(UD_HS_array, axis = 0)
mask_UD_HS = np.isfinite(UD_HS_mean)
UD_HS_std = np.nanstd(UD_HS_array, axis = 0)


# Data Ni-doped HS for plotting
ND_HS_raw_s1_30mm = np.array([0, 0.426, 0.422, 0.641, 0.717, 1.3786, 1.4544, 1.481, np.nan, np.nan])
ND_HS_raw_s1_18mm = np.array([0, 0.333, 0.382, 1.222, 1.2445, 1.2346, 1.2624, 1.3315, np.nan, np.nan])
ND_HS_raw_s2_30mm = np.array([0, 0.061, 0.126, 0.200, 0.563, 0.741, 0.593, 0.603, np.nan, np.nan])
ND_HS_raw_s2_18mm = np.array([0, 0.068, 0.0704, 0.037, 0.326, 0.548, 0.681, 0.852, np.nan, np.nan])
ND_HS_raw_s1_15mm = np.array([0, np.nan, np.nan, np.nan,np.nan, np.nan, np.nan,np.nan, np.nan, 1.667])
ND_HS_raw_s1_28_5mm = np.array([0, np.nan, np.nan, np.nan,np.nan, np.nan, np.nan,np.nan, np.nan, 1.656])
ND_HS_raw_s2_15mm = np.array([0, np.nan, np.nan, np.nan,np.nan, np.nan, np.nan,np.nan, np.nan, 0.844])
ND_HS_raw_s2_28_5mm = np.array([0, np.nan, np.nan, np.nan,np.nan, np.nan, np.nan,np.nan, np.nan, 0.833])

#ND_HS_array = np.array([ND_HS_raw_s1_30mm,ND_HS_raw_s2_30mm,ND_HS_raw_s1_18mm, ND_HS_raw_s2_18mm,
#                        ND_HS_raw_s1_15mm, ND_HS_raw_s1_28_5mm, ND_HS_raw_s2_15mm, ND_HS_raw_s2_28_5mm])

ND_HS_array = np.array([ND_HS_raw_s1_30mm,ND_HS_raw_s1_18mm,ND_HS_raw_s1_15mm, ND_HS_raw_s1_28_5mm])


ND_HS_mean = np.nanmean(ND_HS_array, axis = 0)
mask_ND_HS = np.isfinite(ND_HS_mean)
ND_HS_std = np.nanstd(ND_HS_array, axis = 0)


# Data Undoped LS for plotting
UD_LS_raw_s1_24mm = np.array([0, 0.319, 0.359, 0.417, 0.644, 0.700, 0.729, 0.883, np.nan, 0.956])
UD_LS_raw_s1_16_5mm = np.array([0, 0.302, 0.344, 0.457, 0.498, 0.622, 0.670, 0.744, np.nan, 0.926])
UD_LS_raw_s2_24mm = np.array([0, 0.546, 0.563, 0.681, 0.800, 0.817, 0.867, 0.922, np.nan, 1.852])
UD_LS_raw_s2_16_5mm = np.array([0, 0.341, 0.361, 0.461, 0.506, 0.681, 0.733, 0.815, np.nan, 0.989])

UD_LS_array = np.array([UD_LS_raw_s1_24mm, UD_LS_raw_s2_24mm, UD_LS_raw_s1_16_5mm, UD_LS_raw_s2_16_5mm])

UD_LS_mean = np.mean(UD_LS_array, axis=0)
mask_UD_LS = np.isfinite(UD_LS_mean)
UD_LS_std = np.std(UD_LS_array, axis=0)

# Data Ni-doped LS for plotting
ND_LS_raw_s1_24mm = np.array([0, 0.178, 0.189, 0.233, 0.326, 0.344, 0.439, 0.456, np.nan, 1.356])
ND_LS_raw_s1_16_5mm = np.array([0, 0.222, 0.302, 0.368, 0.46, 0.526, 0.521, 0.578, np.nan, 0.844])
ND_LS_raw_s2_24mm = np.array([0, 0.037, 0.067, 0.178, 0.25, 0.293, 0.396, 0.5,np.nan, 0.563])
ND_LS_raw_s2_16_5mm = np.array([0, 0.67, 0.057, 0.141, 0.124, 0.159, 0.181, 0.328, np.nan, 0.422])

#ND_LS_array = np.array([ND_LS_raw_s1_24mm, ND_LS_raw_s2_24mm, ND_LS_raw_s1_16_5mm, ND_LS_raw_s2_16_5mm])
ND_LS_array = np.array([ND_LS_raw_s1_24mm, ND_LS_raw_s1_16_5mm])

ND_LS_mean = np.mean(ND_LS_array, axis = 0)
mask_ND_LS = np.isfinite(ND_LS_mean)
ND_LS_std = np.std(ND_LS_array, axis = 0)

# Single plot
fig, ax = plt.subplots(figsize=[14,10])

plt.rcParams["font.family"] = "Times New Roman"

ax.set_ylim(0,2)
ax.set_xlim(-50,1050)



ax.plot(revolutions[mask_UD_HS], UD_HS_mean[mask_UD_HS], 'ko',
        linestyle='--',
        markersize=12,
        label='Undoped 1100 $MPa$')
ax.errorbar(revolutions, UD_HS_mean,
            yerr=UD_HS_std,
            ecolor='k',
            linestyle='None',
            capsize=5)

ax.plot(revolutions[mask_ND_HS], ND_HS_mean[mask_ND_HS], 'co',
        linestyle='--',
        color= '#4dbeee',
        markersize=12,
        label='Ni Doped 1100 $MPa$')
ax.errorbar(revolutions, ND_HS_mean,
            yerr=ND_HS_std,
            linestyle='None',
            ecolor='#4dbeee',
            capsize=5)

ax.plot(revolutions[mask_UD_LS], UD_LS_mean[mask_UD_LS], 'k^',
        linestyle='--',
        markersize=12,
        label='Undoped 300 $MPa$')
ax.errorbar(revolutions, UD_LS_mean,
            yerr=UD_LS_std,
            linestyle='None',
            ecolor='k',
            capsize=5)

ax.plot(revolutions[mask_ND_LS], ND_LS_mean[mask_ND_LS], 'c^',
        linestyle='--',
        color= '#4dbeee',
        markersize=12,
        label='Ni Doped 300 $MPa$')
ax.errorbar(revolutions, ND_LS_mean,
            yerr=ND_LS_std,
            linestyle='None',
            ecolor='#4dbeee',
            capsize=5)


#ax.axhline(y=0.0, linestyle='--', color="green", label='Coating Surface')

ax.set_xlabel('Cycles', fontsize=22)
ax.set_ylabel('Wear Depth ($\mu$m)', fontsize=22)
ax.tick_params(axis='both', which='major', labelsize=22)
ax.legend(fontsize=22)

plt.draw()
fig.savefig("wear_depth.png",bbox_inches='tight')
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

