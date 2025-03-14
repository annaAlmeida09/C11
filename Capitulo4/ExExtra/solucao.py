import numpy as np

dataset = np.loadtxt('.\Capitulo4\ExExtra\paises.csv', delimiter=';', dtype = str, encoding = 'utf-8' )

# SLICING

country = dataset[1:, 0]
region = dataset[1:, 1]
population = dataset[1:, 2].astype(float)
area = dataset[1:, 3].astype(float)
literacy = dataset[1:, 9].astype(float)
gpd =  dataset[1:, 8].astype(float)

# Questão 1

slicing = dataset[1:, :4]
print('Os países, regiões, populações e áreas deste dataset:', slicing)

# Questão 2

unique_region, frequency_region = np.unique(region, return_counts=True)
print('O planeta possui', unique_region.size, 'regiões')
print('As regiões são:', unique_region)

# Questão 3

print('A taxa media de alfabetização é de:', round(literacy.mean(),3), 'porcento')

# Questão 4

northern_america_region = np.char.startswith(region, 'NORTHERN AMERICA') > 0
sum_northern_america_region = northern_america_region[northern_america_region==True].sum()
print(sum_northern_america_region, 'países são de NORTHERN AMERICA')

# Questão 5

cond = np.char.find(region, "LATIN AMER. & CARIB") >= 0
caribe_gpd = gpd[cond]
caribe_country  =  country[cond]
max_caribe_gpd = np.argmax(caribe_gpd)
print('O país com maior renda per capita da america do sul e caribe é:', caribe_country[max_caribe_gpd])
