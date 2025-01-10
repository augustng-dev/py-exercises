import numpy as np

# C1: basic
print(np.array([[True for _ in range(3)] for _ in range(3)]))

# C2:
print(np.full((3, 3), True, dtype=bool))

# C3:
print(np.ones((3,3), dtype=bool))