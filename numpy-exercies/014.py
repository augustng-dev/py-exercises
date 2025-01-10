import numpy as np

a = np.array([2, 6, 1, 9, 10, 3, 27])

# C1
index = np.where((a >= 5) & (a <= 10))

print(index)
print(a[index])

# C2
index = np.where(np.logical_and(a>=5, a<=10))

print(a[index])

# C3
print(a[(a >= 5) & (a <= 10)])