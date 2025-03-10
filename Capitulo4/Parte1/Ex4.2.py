#Exercício 2
import numpy as np

array1 = np.arange(0, 51, 2)
print(array1)
array2 = np.arange(100, 50, -2)
print(array2)
array3 = np.concatenate([array1, array2])
print(array3)