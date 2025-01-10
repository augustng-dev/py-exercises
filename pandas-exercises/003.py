import numpy as np
import pandas as pd

mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))
ser = pd.Series(mydict)

# Solution 1
# df = pd.DataFrame(ser).reset_index()

# Solution 2
df = ser.to_frame().reset_index()

print(df.head())