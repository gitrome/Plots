import numpy as np
import numpy.random as nr
import matplotlib.pyplot as plt
import pandas as pd
import os, glob, re

#x = np.arange(1000)
#data = pd.Series(nr.randn(1000)+0.001*x+1)

######### Reading Date from Tribometer CSV output #########

os.chdir("")
extension = 'csv'
all_filenames = [i for i in glob.glob('*{}'.format(extension))]
all_filenames.sort(key=lambda f: int(re.sub('\D', '', f)))

data = []

for filename in all_filenames:
    df = pd.read_csv(filename, index_col=None, header=2)
    df1 = df.transpose()
    data.append(df1)

CoF_raw_0 = data[0].loc['DAQ.COF ()']
Raw_Rev_0 = data[0].loc['Rotary.Position (rev)']



#data = df['DAQ.COF ()']
#print(data)
#x = data['Rotary.Position (rev)']
#print(x)

###########################################################

# found here
# https://towardsdatascience.com/outlier-detection-with-hampel-filter-85ddf523c73d
def hampel_filter_pandas(input_series, window_size, n_sigmas=3):
    k = 1.4826  # scale factor for Gaussian distribution
    new_series = input_series.copy()

    # helper lambda function
    MAD = lambda x: np.median(np.abs(x - np.median(x)))

    rolling_median = input_series.rolling(window=2 * window_size, center=True).median()
    rolling_mad = k * input_series.rolling(window=2 * window_size, center=True).apply(MAD, raw=True)
    diff = np.abs(input_series - rolling_median)

    indices = list(np.argwhere(diff > (n_sigmas * rolling_mad)).flatten())
    new_series[indices] = rolling_median[indices]

    return new_series, indices

fig, ax = plt.subplots()
pd.Series(CoF_raw_0).plot(ax=ax, label='original', alpha=0.6)
# 3 sample for hampel on each side
hamplel_filtered, indices = hampel_filter_pandas(CoF_raw_0, 3)

# pd.Series(hamplel_filtered).plot(ax=ax, label='hampel')

#ax.scatter(Raw_Rev_0[indices], CoF_raw_0[indices], label='outliers')
ax.scatter(Raw_Rev_0[indices], hamplel_filtered[indices], label='set to mean', c='C5', marker='^')

hamplel_filtered.rolling(21, center=True).median().plot(ax=ax)

plt.draw()
fig.savefig("COF.png")
plt.show()
