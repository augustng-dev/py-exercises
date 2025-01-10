import numpy as np

arr = np.arange(9).reshape(3,3)

# C1
# print(arr[[2, 1, 0], :])

# C2
# print(np.flip(arr, axis=0))

# C3
print(arr[::-1])