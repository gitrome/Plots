#import numpy as np
import os, glob
import pandas as pd
#import matplotlib
import matplotlib.pyplot as plt

os.chdir('C:/Users/Sergio/Desktop/Short_Test/wear_profile')

extension = 'csv'
all_filenames = [i for i in glob.glob('*{}'.format(extension))]
#all_filenames.sort(key=lambda f: int(re.sub('\D', '', f)))
print(all_filenames)

data=[]

for filename in all_filenames:
    df = pd.read_csv(filename, sep=';', delimiter=None, header=1)
    df = df[1:]
    data.append(df)
'''
# Use if data needs to be concatenated into columns
data1 = pd.concat(data[0:7], axis=1).astype(float).div(1e-6) #concatenate into columns
data2 = pd.concat(data[7:16], axis=1).astype(float).div(1e-6)
data3 = pd.concat(data[16:23], axis=1).astype(float).div(1e-6)
data4 = pd.concat(data[23:31], axis=1).astype(float).div(1e-6) '''

# Use if data is already concat into columns
data1 = data[0].astype(float).div(1e-6)
data2 = data[1].astype(float).div(1e-6)
data3 = data[2].astype(float).div(1e-6)
data4 = data[3].astype(float).div(1e-6)

x1 = data1[data1.columns[0:14:2]]
y1 = data1[data1.columns[1::2]]
x2 = data2[data1.columns[0:14:2]]
y2 = data2[data1.columns[1::2]]
x3 = data3[data1.columns[0:14:2]]
y3 = data3[data1.columns[1::2]]
x4 = data4[data1.columns[0:14:2]]
y4 = data4[data1.columns[1::2]]
'''for j in range(len(data)):
    df= data[j]
    df.astype(float).div(1e-6)'''

################################# Plot #################################

fig, axs = plt.subplots(nrows=2, ncols=2, figsize=[14,10], sharex='col', sharey='row')
axs = axs.flatten()

plt.rcParams["font.family"] = "Times New Roman"

fig.subplots_adjust(hspace=0.25, wspace=0.25)
  
fig.text(0.5, 0.0, 'x ( $\mu$m )', fontsize=18, ha='center', va='center')
fig.text(-0.018, 0.5, 'y ( $\mu$m )',fontsize=18, ha='center', va='center',
         rotation='vertical')

axs[0].plot(x1, y1,)
#axs[0].fill(x1,y1)
axs[1].plot(x2, y2)
#axs[1].fill(x2,y2)
axs[2].plot(x3, y3)
#axs[2].fill(x3,y3)
axs[3].plot(x4,y4)
#axs[3].fill(x4,y4)

for i, label in enumerate(('A', 'B', 'C', 'D')):
    axs[i].text(-0.025, 0.95, label, transform=axs[i].transAxes,
      fontsize=25, fontweight='bold', va='top', ha='right')
    axs[i].set_ylim(-1.5, 1.5)
    axs[i].set_xlim(0, 800)
#    axs[i].legend(lineObjects,("5 Cycles ", "10 Cycles", 
#      "50 Cycles","100 Cycles ", "150 Cycles","200 Cycles ", "250 Cycles"))
    axs[i].tick_params(axis='both', which='major', labelsize=18)
    axs[i].grid()

#fig.text(0.8, 0.4, 'Placeholder',
#         fontsize=50, color='gray',
#         ha='right', va='bottom', alpha=0.5)

fig.tight_layout()
plt.draw()
fig.savefig('wear_profile.png',bbox_inches='tight')
plt.show()