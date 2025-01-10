import numpy as np

a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)

# Answers
# Method 1:
print(np.concatenate([a, b], axis=0))

# Method 2:
print(np.vstack([a, b]))

# Method 3:
print(np.r_[a, b])