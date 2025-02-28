#Exercício 2
#importando o numpy
import numpy as np

#criando arrays
array1 = np.ones(8, dtype=int)
array2 = np.random.randint(0, 9, [8]) 

array3 = array1 + array2

soma = np.sum(array3)
print(soma)
if soma >= 40:
    array3 = np.reshape(array3, (8,1)) 
else:
    array3 = np.reshape(array3, (1,8)) 

print(array3)