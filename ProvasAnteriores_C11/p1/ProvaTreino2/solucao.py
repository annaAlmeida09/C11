import numpy as np

dataset = np.loadtxt('./ProvasAnteriores_C11/p1/ProvaTreino2/brands.csv', delimiter = ';', dtype = str, encoding = 'utf-8')

# Slicing

brand = dataset [1:,0]
founded_by = dataset [1:,1]
founded_in = dataset [1:,2].astype(float)
country = dataset [1:,3]
people = dataset [1:,4]
genre = dataset [1:,5]
website = dataset [1:,6]
rank_2022 = dataset[1:,7]
rank_2021 = dataset[1:,8]
value_2022 = dataset[1:,9].astype(float)
value_2021 = dataset[1:,10].astype(float)
change_porcent = dataset[1:,11]
rating_2022 = dataset[1:,12]
rating_2021 = dataset[1:,13]

# Questão 1
cond = brand == 'Google' # Encontrando os dados da google
value_google_2021 = value_2021[cond][0]
value_google_2022 = value_2022[cond][0]
print(value_google_2022 - value_google_2021)

# Questão 2
brand_name = np.char.find(brand, 'Group') > 0
sum_brand_name = brand_name[brand_name == True].sum()
print(sum_brand_name)

#Questão 3
five_brand = brand[:5]
five_values_2022 = value_2022[:5]
five_values_2023 = five_values_2022 * 1.1
print('Possíveis valores para as 5 primeiras marcas em 2023')
for i in range (0,5):
     print(five_brand[i],':', round(five_values_2023[i], 2))

# Questão 4
founded_in_2000 = founded_in[founded_in > 2000]
cond2 = founded_in > 2000
sum_founded_in_2000 = cond2.sum()
print(founded_in_2000)
print(sum_founded_in_2000)


