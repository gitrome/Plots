import os, glob
import pandas as pd
import re
os.chdir("C:/Users/Sergio/Desktop/Short_Test")

extension = 'csv'
all_filenames = [i for i in glob.glob('*{}'.format(extension))]
#all_filenames.sort(key=lambda f: int(re.sub('\D', '', f)))
print(all_filenames)

for filename in all_filenames:
    df = pd.read_csv(filename)
    print(df)

print(df.loc[:,3:]) #Index df by revolutions
    
    



