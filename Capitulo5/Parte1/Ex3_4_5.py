# EXERCÍCIO 3
import pandas as pd

labels1 = ['Java', 'C', 'Python']
data1 = [16.21, 16.04, 9.85]
seriesAno1 = pd.Series(index = labels1, data = data1)

labels2 = ['C', 'Python', 'Java']
data2 = [16.21, 12.12, 11.68]
seriesAno2 = pd.Series(index = labels2, data = data2)

labels3 = ['Java', 'C', 'Python']

data3 = [seriesAno2['Java'] - seriesAno1['Java'], seriesAno2['C'] - seriesAno1['C'], seriesAno2['Python'] - seriesAno1['Python']]
crescimento_decrescimento = pd.Series(index = labels3, data = data3)

print('Crescimento/declínio de Java:', round(crescimento_decrescimento['Java'], 3))
print('Crescimento/declínio de C:', round(crescimento_decrescimento['C'], 3))
print('Crescimento/declínio de Python:', round(crescimento_decrescimento['Python'], 3))
# EXERCÍCIO 4
print('Dados das linguagens que tiveram crescimento (nome e quanto de crescimento):', crescimento_decrescimento[crescimento_decrescimento > 0])
# EXERCÍCIO 5
labels4 = ['Java', 'C', 'Python']
data4 = [seriesAno2['Java'] + 2 * crescimento_decrescimento['Java'], seriesAno2['C'] + 2 * crescimento_decrescimento['C'], seriesAno2['Python'] + 2 * crescimento_decrescimento['Python']]
doisAnos = pd.Series(index = labels4, data = data4)

print('Linguagem mais popular nos próximos dois anos:')
print(doisAnos.nlargest(1))

