#Exercício 5

import numpy as np

np.random.seed(10)

matriz = np.random.randint(1, 50, [4, 4])

media_linhas = matriz.sum(axis=1)/4
print(media_linhas)
media_colunas = matriz.sum(axis=0)/2
print(media_colunas)

print(media_linhas.max())
print(media_colunas.max())

contador = np.unique(matriz, return_counts=True)

print('Ocorrência dos valores:')
for i in range(len(contador[1])):
    print(f'{contador[0][i]}: {contador[1][i]}')

print('Valores que aparecem 2 vezes:')
for j in range(len(contador[1])):
    if contador[1][j] == 2:  
        print(contador[0][j]) 