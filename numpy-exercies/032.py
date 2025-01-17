import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='object')

i, j = np.where(iris_2d)

# C1
np.random.seed(100)
iris_2d[np.random.choice((i), 20), np.random.choice((j), 20)] = np.nan

# C2
np.random.seed(100)
iris_2d[np.random.randint(150, size=20), np.random.randint(4, size=20)] = np.nan

# Print first 10 rows
print(iris_2d[:10])