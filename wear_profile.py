import numpy as np
import numpy.random as nr
import matplotlib.pyplot as plt
import pandas as pd
import os
import glob

'''
os.listdir(os.getcwd())
df = pd.read_csv('ND_HS_AM_RT_14mm_50.csv', sep = ";", skiprows=[0,2])
print(df.head())
x = df['x.1']
y = df['y.1']

fig, ax1 = plt.subplots()

#ax1.set_ylim(1.05,-0.5)
#ax1.set_xlim(-5,300)

ax1.plot(x, y, 'k')
ax1.set(xlabel='x', ylabel="y",
       title='Undoped MoS$_2$ High Stress Wear Profile')
ax1.grid()

plt.legend()
plt.draw()
fig.savefig("UD_HS_AM_RT_profile.png")
plt.show()


'''
our_files = glob.glob('*.csv')
for filename in our_files:
    print(filename, 'number')
    df = pd.read_csv(filename, sep = ";", skiprows=[0,2])





