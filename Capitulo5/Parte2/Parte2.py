import numpy as np
import pandas as pd

df = pd.DataFrame(
    index = ['A', 'B', 'C', 'D', 'E'],
    columns = ['W', 'X', 'Y', 'Z'],
    data = np.random.randint(1, 50 , [5, 4])
)
# EXERCÍCIO 6
print('Dataframe:')
print(df)

print('Média dos elementos da coluna X que são menores que 30:', round(df[df['X'] < 30]['X'].mean(), 3))

# EXERCÍCIO 7
print('Média dos elementos da linha D:', round(df.loc['D'].mean(), 3))
print('Soma dos elementos da linha E:', df.iloc[4].sum())

# EXERCÍCIO 8
dfSliced = df.loc[['A', 'C', 'E'], ['X', 'Y']]

print('Dataframe depois do slicing:')
print(dfSliced)

print('Soma de cada linha:')
print(dfSliced.sum(axis = 1))

print('Soma de cada coluna:')
print(dfSliced.sum(axis = 0))