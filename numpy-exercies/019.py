import numpy as np

arr = np.arange(9).reshape(3,3)

# C1
# num_cols = arr.shape[1]
# print(arr[:, np.arange(num_cols-1, -1, -1)])

# C2
# print(np.array([row[::-1] for row in arr]))

# C3
# print(arr[:,[2,1,0]])

# C4
# print(np.flip(arr, axis=1))

# C5
# print(arr[:,::-1])

# C6
# print(np.fliplr(arr))

