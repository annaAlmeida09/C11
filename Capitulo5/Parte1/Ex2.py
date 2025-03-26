# EXERCÍCIO 2

import pandas as pd

labels1 = ['Java', 'C', 'Python']
dados1 = [16.21, 16.04, 9.85]
seriesAno1 = pd.Series(index = labels1, data = dados1)

labels2 = ['C', 'Python', 'Java']
dados2 = [16.21, 12.12, 11.68]
seriesAno2 = pd.Series(index = labels2, data = dados2)

print('Porcentagem do ano 1:', seriesAno1.sum())
print('Porcentagem do ano 2:', seriesAno2.sum())
