import os, glob
import pandas as pd
import re
os.chdir("D:/Short_Test/ND_HS_AM_RT/1/ND_HS_AM_RT_18mm/raw_data")

extension = 'csv'
all_filenames = [i for i in glob.glob('*{}'.format(extension))]
all_filenames.sort(key=lambda f: int(re.sub('\D', '', f)))
print(all_filenames)

li = []

for filename in all_filenames:
    df = pd.read_csv(filename, index_col=None, header=2, skiprows=-2)
    df = df[df['Rotary.Angle (deg)'] != 0]
    li.append(df)


frame = pd.concat(li, axis=0, ignore_index=True)
frame.to_csv('ND_HS_AM_RT_18mm.csv', index=False, encoding='utf-8-sig')



