import numpy as np
import pandas as pd

ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))

# Solution 1
pf = pd.concat((ser1, ser2), axis=1)

# Solution 2
# pf = pd.DataFrame({'col1': ser1, 'col2': ser2})

print(pf)