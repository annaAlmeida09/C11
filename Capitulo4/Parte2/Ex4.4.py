#Exercício 4
import numpy as np

matriz = np.random.randint(1, 5, [np.random.randint(1, 5), np.random.randint(1, 5)])
print(matriz)

linhas, colunas = matriz.shape
total = linhas * colunas
print(total)

if total & 1:
    print("A matriz pode se tornar um vetor com números ímpares de elementos")
else:
    print("A matriz pode se tornar um vetor com um números pares de elementos")