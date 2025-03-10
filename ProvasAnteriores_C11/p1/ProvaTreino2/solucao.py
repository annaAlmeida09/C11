import numpy as np

dataset = np.loadtxt('./ProvasAnteriores_C11/p1/ProvaTreino2/brands.csv', delimiter = ';', dtype = str, enconding = 'utf-8')

# Slicing

brand = dataset [1:,0]
founded_by = dataset [1:,1]
founded_in = dataset [1:,2]
country = dataset [1:,3]
people = dataset [1:,4]
genre = dataset [1:,5]
website = dataset [1:,6]
rank_2022 = dataset [1:,7]
rank_2021 = dataset [1:,8]
value_2022 = dataset[1:,9]
value_2021 = dataset[1:,10]
change_porcent = dataset[1:,11]
rating_2022 = dataset[1:,12]
rating_2021 = dataset[1:,13]

# Questão 1