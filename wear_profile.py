import numpy as np
import os, glob, math, re
import pandas as pd
import matplotlib.pyplot as plt

os.chdir('C:/Users/Sergio/Desktop/Short_Test/UD_LS_AM_RT/1/UD_LS_AM_RT_24mm/processed')

extension = 'csv'
all_filenames = [i for i in glob.glob('*{}'.format(extension))]
all_filenames.sort(key=lambda f: int(re.sub('\D', '', f)))
print(all_filenames)

data=[]

for filename in all_filenames:
    df = pd.read_csv(filename, sep=';', delimiter=None, header=1)
    df = df[1:]
    data.append(df)

data1 = pd.concat(data, axis=1).astype(float) #concatenate into columns

#plt.figure()
#plt.plot(data1['x'], data1['y'])
#plt.show()

#for t in range(len(data1)):
#    a = (pd.to_numeric(data[t].x)).div(1e-6)  
#    b = (pd.to_numeric(data[t].y)).div(1e-6) 
        

################################# Plot #################################    

    

 
'''
fig, ax1 = plt.subplots(nrows=2, ncols=2, sharex=True, sharey=True)
fig.subplots_adjust(hspace=0.15, wspace=0.1)
  
fig.text(0.5, 0.04, 'x ($\mu$m)', ha='center', va='center')
fig.text(0.06, 0.5, 'y ($\mu$m)', ha='center', va='center', rotation='vertical')

#ax.set_ylim(0,2)
#ax.set_xlim(0,450)  


ax1.plot(data1['x'], data1['y'])


plt.show()


plt.draw()
fig.savefig('wear_profile.png')
plt.show()    
'''







