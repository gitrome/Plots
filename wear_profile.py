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

################################# Plot #################################

fig, axs = plt.subplots(nrows=2, ncols=2, figsize=[14,10], sharex='col', sharey='row')
axs = axs.flatten()

plt.rcParams["font.family"] = "Times New Roman"

fig.subplots_adjust(hspace=0.10, wspace=0.07)
  
fig.text(0.5, 0.0, 'x ( $\mu$m )', fontsize=22, ha='center', va='center')
fig.text(0, 0.5, 'y ( $\mu$m )',fontsize=22, ha='center', va='center',
         rotation='vertical')

lineObjects = [axs[2].plot(x1, y1,'--'),
               axs[3].plot(x2, y2,'--'),
               axs[0].plot(x3, y3,'--'),
               axs[1].plot(x4,y4,'--')]

for i, label in enumerate(('a', 'b', 'c', 'd')):
    axs[i].text(0.1, 0.95, label, transform=axs[i].transAxes,
      fontsize=30, fontweight='bold', va='top', ha='right')
    axs[i].set_ylim(-1.5, 1.5)
    axs[i].set_xlim(0, 800)
    axs[i].tick_params(axis='both', which='major', labelsize=22)
    '''axs[i].legend(iter(lineObjects[i]),("5 Cycles ", "10 Cycles",
                               "50 Cycles","100 Cycles ",
                               "150 Cycles","200 Cycles ",
                               "250 Cycles"))'''

axs[2].legend(iter(lineObjects[0]),("5 Cycles ", "10 Cycles",
                               "50 Cycles","100 Cycles ",
                               "150 Cycles","200 Cycles ",
                               "250 Cycles"), loc='lower right',fontsize=12)
axs[2].text(500, 1, 'Ni Doped 1100 MPa', fontsize =15,
        bbox={'facecolor': 'white', 'alpha': 0.5, 'pad': 10}) 

axs[3].legend(iter(lineObjects[1]),("5 Cycles ", "10 Cycles",
                               "50 Cycles","100 Cycles ",
                               "150 Cycles","200 Cycles ",
                               "250 Cycles"), loc='lower right',fontsize=12)
axs[3].text(500, 1, 'Ni Doped 1100 MPa', fontsize =15,
        bbox={'facecolor': 'white', 'alpha': 0.5, 'pad': 10})

axs[0].legend(iter(lineObjects[2]),("5 Cycles ", "10 Cycles",
                               "50 Cycles","100 Cycles ",
                               "150 Cycles","200 Cycles ",
                               "250 Cycles"), loc='lower right',fontsize=12)
axs[0].text(500, 1, 'Undoped 1100 MPa', fontsize =15,
        bbox={'facecolor': 'white', 'alpha': 0.5, 'pad': 10})

axs[1].legend(iter(lineObjects[3]),("5 Cycles ", "10 Cycles",
                               "50 Cycles","100 Cycles ",
                               "150 Cycles","200 Cycles ",
                               "250 Cycles"), loc='lower right',fontsize=12)
axs[1].text(500, 1, 'Undoped 300 MPa', fontsize =15,
        bbox={'facecolor': 'white', 'alpha': 0.5, 'pad': 10})  

fig.tight_layout(pad=5, w_pad=0.5, h_pad=2.0)
plt.draw()
fig.savefig('wear_profile.png',bbox_inches='tight')
plt.show()