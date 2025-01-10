import numpy as np

arr = np.arange(9).reshape(3,3)

# C1
# arr[:, 1], arr[:, 0] = arr[:,0].copy(), arr[:, 1].copy()

# C2
arr[:, [1,0,2]]

print(arr)