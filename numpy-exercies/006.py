import numpy as np

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

out = np.where(arr % 2 != 0, -1, arr)

print(out)