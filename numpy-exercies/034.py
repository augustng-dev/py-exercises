import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])

conditions = (iris_2d[:, 2] > 1.5) & (iris_2d[:, 0] < 5.0)

print(iris_2d[conditions])