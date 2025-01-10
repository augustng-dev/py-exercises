import numpy as np

a = np.array([1, 2, 3])

print(np.r_[np.repeat(a, 3), np.tile(a, 3)])