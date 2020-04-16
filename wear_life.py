import matplotlib
import matplotlib.pyplot as plt
import matplotlib.transforms as transforms
import numpy as np


Contact_pressure = np.array([300, 500, 800, 1100])

# Data
UD_HS_AM = np.array([1250, 1250, 2000])*(1/1000)
ND_HS_AM = np.array([2750, 1250, 1500])*(1/1000)
UD_LS_AM = np.array([35000,37000, 35000])*(1/1000)
ND_LS_AM = np.array([90000,75000,50000])*(1/1000)
UD_IHS_AM = np.array([4000,3000,3700])*(1/1000)
ND_IHS_AM = np.array([6000,5300,2700])*(1/1000)
UD_ILS_AM = np.array([7800,4300,8200])*(1/1000)
ND_ILS_AM = np.array([32000,22000,5000,38000])*(1/1000)

UD_HS_mean = np.mean(UD_HS_AM, axis = 0)
UD_HS_std = np.std(UD_HS_AM, axis = 0)
UD_LS_mean = np.mean(UD_LS_AM, axis = 0)
UD_LS_std = np.std(UD_LS_AM, axis = 0)
UD_IHS_mean = np.mean(UD_IHS_AM, axis = 0)
UD_IHS_std = np.std(UD_IHS_AM, axis = 0)
UD_ILS_mean = np.mean(UD_ILS_AM, axis = 0)
UD_ILS_std = np.std(UD_ILS_AM, axis = 0)

ND_HS_mean = np.mean(ND_HS_AM, axis = 0)
ND_HS_std = np.std(ND_HS_AM, axis = 0)
ND_LS_mean = np.mean(ND_LS_AM, axis = 0)
ND_LS_std = np.std(ND_LS_AM, axis = 0)
ND_IHS_mean = np.mean(ND_IHS_AM, axis = 0)
ND_IHS_std = np.std(ND_IHS_AM, axis = 0)
ND_ILS_mean = np.mean(ND_ILS_AM, axis = 0)
ND_ILS_std = np.std(ND_ILS_AM, axis = 0)

########################## Mean and Std ###########################

ND_Array =  [ND_LS_mean, ND_ILS_mean, ND_IHS_mean, ND_HS_mean] #array with ND mean
ND_error = [ND_LS_std, ND_ILS_std, ND_IHS_std, ND_HS_std] #array with ND error (std)

UD_Array =  [UD_LS_mean, UD_ILS_mean, UD_IHS_mean, UD_HS_mean] #array with ND mean
UD_error = [UD_LS_std, UD_ILS_std, UD_IHS_std, UD_HS_std] #array with ND error (std)

################################# Plot #################################
fig, ax = plt.subplots(figsize=[14,10])

plt.rcParams["font.family"] = "Times New Roman"

ax.set_ylim(-10,100)
ax.set_xlim(200,1200)

ax.plot(Contact_pressure, UD_Array, 'ko',
        linestyle='--',
        markersize=12,
        label='Undoped MoS$_2$')
ax.errorbar(Contact_pressure, UD_Array,
            yerr=UD_error,
            ecolor='k',
            linestyle='None',
            capsize=5)

ax.plot(Contact_pressure, ND_Array, 'o',
        color= '#4dbeee',
        linestyle='--',
        markersize=12,
        label='Ni Doped MoS$_2$')
ax.errorbar(Contact_pressure, ND_Array,
            yerr=ND_error,
            ecolor= '#4dbeee',
            linestyle='None',
            capsize=5)

for i,j in zip(Contact_pressure, ND_Array):
    ax.annotate(str(round(j,1)),xy=(i+5,j+2),fontsize=18)
    
for i,j in zip(Contact_pressure, UD_Array):
    ax.annotate(str(round(j,1)),xy=(i-30,j-10),fontsize=18)

ax.set_xlabel('Contact Pressure ($MPa$)',fontsize=18)
ax.set_ylabel('Coating Life ($x 10^3 Cycles$)',fontsize=18)
ax.tick_params(axis='both', which='major', labelsize=18)
ax.grid()
ax.legend(fontsize=18)

plt.draw()
fig.savefig("wear_life.png",bbox_inch='tight')
plt.show()
