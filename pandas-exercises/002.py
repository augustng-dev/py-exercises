import numpy as np
import pandas as pd

mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))

pdlist = pd.Series(mylist)
pdarr = pd.Series(myarr)
pddict = pd.Series(mydict)

print(pdlist)
print(pdarr)
print(pddict)