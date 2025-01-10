import numpy as np
import sys

np.set_printoptions(threshold=6)
a = np.arange(15)

# C1
np.set_printoptions(threshold=len(a))

# C2
np.set_printoptions(threshold=sys.maxsize)

print(a)