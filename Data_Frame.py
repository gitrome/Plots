import pandas as pd
import glob, os

pd.set_option('display.max_colwidth', -1)

'''
# Rename multiple CSV files in a folder
def rename(dir, pathAndFilename, pattern, titlePattern):
    os.rename(pathAndFilename, os.path.join(dir, titlePattern))

path = os.path.expanduser('~//*csv')

for i, fname in enumerate(glob.glob(path)):
    rename(os.path.expanduser('`//*.csv'), fname = r'*.csv',r'test{}.csv'.format(i))
'''
# Load several
result = pd.DataFrame()

path = os.path.expanduser("/C:/Users/romer/PycharmProjects/RT_plots/ND_HS_AM_RT_14mm_*.csv")

for fname in glob.glob(path):
    head, tail = os.path.split(fname)
    df = pd.read_csv(fname, sep=";")
    df2 = df.sort_values(by=['Profile 1'], ascending=False).drop(['Fit', 'Fit'], axis=1).iloc[15:20,:]
    df2['y'] = tail
    result = pd.concat([result, df2])
#result.sort_values(by=['COF']).iloc[0:10,]

print(result)

'''
stock_files = sorted(glob('RT_plots/ND_*_AM_RT_14mm_*.csv'))
print(stock_files)

pd.concat((pd.read_csv(file).assign(filename = file)
          for file in stock_files), ignore_index = True)
'''