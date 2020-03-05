'''import pandas as pd
import glob, os

for filename in glob.glob('RT_plots/*.csv'):
    data = pd.read_csv(filename, index_col='P')

print(filename)
'''

import os, glob
import pandas as pd
os.chdir("F:/Short_Test/UD_HS_AM_RT/2/UD_HS_AM_RT_18mm/raw_data")

extension = 'csv'
all_filenames = [i for i in glob.glob('*{}'.format(extension))]

li = []

for filename in all_filenames:
    df = pd.read_csv(filename, index_col=None, header=2)
    li.append(df)

print(li)
df.to_csv('UD_HS_AM_RT_18mm.csv', index=False, encoding='utf-8-sig')

frame = pd.concat(li, axis=0, ignore_index=True)

'''
# Combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])

# Export to csv
combined_csv.to_csv('UD_HS_AM_RT_18mm.csv', index = False, encoding = 'utf-8-sig')
'''


