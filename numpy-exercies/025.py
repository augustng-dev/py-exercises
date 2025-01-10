import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')

# Print the first 3 rows
iris[:3]
#> array([[b'5.1', b'3.5', b'1.4', b'0.2', b'Iris-setosa'],
#>        [b'4.9', b'3.0', b'1.4', b'0.2', b'Iris-setosa'],
#>        [b'4.7', b'3.2', b'1.3', b'0.2', b'Iris-setosa']], dtype=object)