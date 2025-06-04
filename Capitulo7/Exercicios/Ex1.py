import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# Carregando os datasets
dataset1 = pd.read_csv('./Capitulo7/Datasets/airtravel.csv', delimiter=',', index_col='Date', parse_dates=True)
dataset2 = pd.read_csv('./Capitulo7/Datasets/co2_emissions.csv', delimiter=',', index_col='Year', parse_dates=True)

# Convertendo os dados para float
dataset1['Passengers'] = dataset1['Passengers'].astype(float)
dataset2['CO2_Emissions'] = dataset2['CO2_Emissions'].astype(float)

# ========================
# SÉRIE 1 - airtravel.csv
# ========================

# Plotagem da série temporal
plt.figure(figsize=(10, 6))
dataset1['Passengers'].plot(title='Número de passageiros aéreos ao longo do tempo', ylabel='Passageiros', xlabel='Data')
plt.grid()
plt.show()

# Decomposição da série temporal
decomp1 = seasonal_decompose(dataset1['Passengers'], model='multiplicative', period=12)
decomp1.plot()
plt.suptitle('Decomposição da Série - Passageiros')
plt.tight_layout()
plt.show()

# Respostas sobre a série 1:
# a. A série possui Tendência? Sim. Há uma tendência de crescimento no número de passageiros ao longo do tempo.
# b. A série possui Sazonalidade? Sim. Há uma clara sazonalidade anual (repetição a cada 12 meses).
# c. A série apresenta um Ciclo? Não há evidência de ciclos econômicos claros. O comportamento é mais sazonal do que cíclico.

# ============================
# SÉRIE 2 - co2_emissions.csv
# ============================

# Plotagem da série temporal
plt.figure(figsize=(10, 6))
dataset2['CO2_Emissions'].plot(title='Emissões de CO2 ao longo do tempo', ylabel='CO2 (milhões de toneladas)', xlabel='Ano')
plt.grid()
plt.show()

# Decomposição da série temporal
# Ajuste do período: assumindo dados anuais, não há sazonalidade mensal. Usamos aditivo sem período fixo.
decomp2 = seasonal_decompose(dataset2['CO2_Emissions'], model='additive', period=1)
decomp2.plot()
plt.suptitle('Decomposição da Série - Emissões de CO2')
plt.tight_layout()
plt.show()

# Respostas sobre a série 2:
# a. A série possui Tendência? Sim. Há uma tendência de aumento das emissões ao longo dos anos.
# b. A série possui Sazonalidade? Não. Como são dados anuais, não há padrão sazonal evidente.
# c. A série apresenta um Ciclo? Pode haver influência de ciclos econômicos globais, mas não é claramente visível nesta decomposição simples.
