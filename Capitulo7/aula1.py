# Introdução as Séries Temporais
# Tendências, Sazonalidades e Ciclos 
# Previsão
#
# Definição: Série de valores que acontecem (são coletados) ao longo de um padrão bem definido de tempo.
#
# Medida -> Fato -> Unidade de Tempo
#
# Erro (medida) de quantização (medida) por minuto (tempo)
#
# outliar = fora do padrão
#
# tendência -> crescente 
#           -> decrescente
#           -> estacionária
# sazionalidade
#           -> minuto
#           -> dia 
#           -> mês, etc.
# ciclos
#           -> Não segue padrão fixo como a sazonalidade. (Exemplo crise econômica)
# ruído

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
 
# importar os dados da time serie
# index_col = 'date' para definir o eixo x como a coluna de datas
# parse_dates = True para o codigo considerar como datas 

dataset = pd.read_csv('./Capitulo7/Datasets/retail_index_br.csv', delimiter=';', index_col='date',parse_dates=True)
 
# transformando os dados do eixo y em float
dataset['retail_index'].astype(float)
 
# traçar a time serie
dataset['retail_index'].plot(figsize=(8,6),title ='indice de venda do varejo brasileiro', xlabel='Data',ylabel='Indice de vendas')
plt.show()

# Decomposição aditiva
decomposition = seasonal_decompose(dataset['retail_index'], model='additive')
# Plotando os componentes
decomposition.plot()
plt.tight_layout()
plt.show()
