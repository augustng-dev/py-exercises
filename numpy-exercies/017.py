import numpy as np

arr = np.arange(9).reshape(3,3)

# C1
arr[0], arr[1] = arr[1].copy(), arr[0].copy()

print(arr)

# C2
# print(arr[(1, 0, 2), :])