import numpy as np

# Input
rand_arr = np.random.random((5,3))

# Create the random array
# rand_arr = np.random.random([5,3])

# Limit to 3 decimal places
np.set_printoptions(precision=3)
print(rand_arr[:4])
#> array([[ 0.443,  0.109,  0.97 ],
#>        [ 0.388,  0.447,  0.191],
#>        [ 0.891,  0.474,  0.212],
#>        [ 0.609,  0.518,  0.403]])