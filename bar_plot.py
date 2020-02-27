import numpy as np
import numpy.random as nr
import matplotlib.pyplot as plt
import pandas as pd

# Raw Data Dir A
sm_dir_A = np.array([3.337e-2, 5.363e-2, 5.385e-2])
me_dir_A = np.array([2.998e-2, 3.326e-2, 4.881e-2])
la_dir_A = np.array([6.509e-2, 6.436e-2, 6.280e-2])
co_dir_A = np.array([7.232e-3, 8.925e-3, 8.356e-3])
# Raw Data Dir B
sm_dir_B = np.array([0.080256407, 0.053958992, 0.075448866])
me_dir_B = np.array([0.029980659, 0.037241283, 0.037114288])
la_dir_B = np.array([0.072078271, 0.051596897, 0.072595269])
co_dir_B = np.array([0.006401509, 0.008770047, 0.009168721])
# Raw Data Dir C
sm_dir_C = np.array([0.051596897,0.052119924,0.052014684])
me_dir_C = np.array([0.035520798,0.048053155,0.063077863])
la_dir_C = np.array([0.070726306,0.077128567,0.072078271])
co_dir_C = np.array([0.008027776,0.006825227,0.007700462])

#calculate the average
sm_dir_A_mean = np.mean(sm_dir_A)
me_dir_A_mean = np.mean(me_dir_A)
la_dir_A_mean = np.mean(la_dir_A)
co_dir_A_mean = np.mean(co_dir_A)
#calculate the standard deviation
sm_dir_A_std = np.std(sm_dir_A)
me_dir_A_std = np.std(me_dir_A)
la_dir_A_std = np.std(la_dir_A)
co_dir_A_std = np.std(co_dir_A)
#calculate the average
sm_dir_B_mean = np.mean(sm_dir_B)
me_dir_B_mean = np.mean(me_dir_B)
la_dir_B_mean = np.mean(la_dir_B)
co_dir_B_mean = np.mean(co_dir_B)
#calculate the standard deviation
sm_dir_B_std = np.std(sm_dir_B)
me_dir_B_std = np.std(me_dir_B)
la_dir_B_std = np.std(la_dir_B)
co_dir_B_std = np.std(co_dir_B)
#calculate the average
sm_dir_C_mean = np.mean(sm_dir_C)
me_dir_C_mean = np.mean(me_dir_C)
la_dir_C_mean = np.mean(la_dir_C)
co_dir_C_mean = np.mean(co_dir_C)
#calculate the standard deviation
sm_dir_C_std = np.std(sm_dir_C)
me_dir_C_std = np.std(me_dir_C)
la_dir_C_std = np.std(la_dir_C)
co_dir_C_std = np.std(co_dir_C)

#list for plot
dir_A = ['R-1', 'R-2', 'R-3', 'N Control']
x_pos =  np.arange(len(dir_A)) # array with the count of the number of bars
CTEs =  [sm_dir_A_mean, me_dir_A_mean, la_dir_A_mean, co_dir_A_mean] #array with the mean
error = [sm_dir_A_std, me_dir_A_std, la_dir_A_std, co_dir_A_std] #array with the error (std)

#BAr plot with error
fig, ax = plt.subplots()
ax.bar(x_pos,  CTEs, color = ['black', 'red', 'blue', 'yellow'], yerr = error, align = 'center', alpha = 0.75, ecolor = 'black', capsize = 10)
ax.set_ylabel('Scratch Hardness ($GPa$)')
ax.set_xticks(x_pos)
ax.set_xticklabels(dir_A)
ax.set_title('Scratch Hardness Direction A')
#ax.yaxis.grid(True)

# Save the figure and show
plt.tight_layout()
plt.savefig('bar_sh_dir_A.png')
plt.show()

#list for plot
dir_B = ['R-1', 'R-2', 'R-3', 'N Control']
x_pos =  np.arange(len(dir_B)) # array with the count of the number of bars
CTEs =  [sm_dir_B_mean, me_dir_B_mean, la_dir_B_mean, co_dir_B_mean] #array with the mean
error = [sm_dir_B_std, me_dir_B_std, la_dir_B_std, co_dir_B_std] #array with the error (std)

#BAr plot with error
fig, ax = plt.subplots()
ax.bar(x_pos,  CTEs, color = ['black', 'red', 'blue', 'yellow'], yerr = error, align = 'center', alpha = 0.75, ecolor = 'black', capsize = 10)
ax.set_ylabel('Scratch Hardness ($GPa$)')
ax.set_xticks(x_pos)
ax.set_xticklabels(dir_B)
ax.set_title('Scratch Hardness Direction B')
#ax.yaxis.grid(True)

# Save the figure and show
plt.tight_layout()
plt.savefig('bar_sh_dir_B.png')
plt.show()

#list for plot
dir_C = ['R-1', 'R-2', 'R-3', 'N Control']
x_pos =  np.arange(len(dir_C)) # array with the count of the number of bars
CTEs =  [sm_dir_C_mean, me_dir_C_mean, la_dir_C_mean, co_dir_C_mean] #array with the mean
error = [sm_dir_C_std, me_dir_C_std, la_dir_C_std, co_dir_C_std] #array with the error (std)

#BAr plot with error
fig, ax = plt.subplots()
ax.bar(x_pos,  CTEs, color = ['black', 'red', 'blue', 'yellow'], yerr = error, align = 'center', alpha = 0.75, ecolor = 'black', capsize = 10)
ax.set_ylabel('Scratch Hardness ($GPa$)')
ax.set_xticks(x_pos)
ax.set_xticklabels(dir_C)
ax.set_title('Scratch Hardness Direction C')
#ax.yaxis.grid(True)

# Save the figure and show
plt.tight_layout()
plt.savefig('bar_sh_dir_C.png')
plt.show()