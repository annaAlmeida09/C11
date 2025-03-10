import numpy as np

dataset = np.loadtxt('./Capitulo4/Space - Parte3/space.csv', delimiter = ';', dtype = str, encoding = 'utf-8')

# Slicing (fatiamento) do dataset

company = dataset[1:, 1]
location = dataset[1:, 2]
detail = dataset[1:, 4]
cost = dataset[1:, 6].astype(float) # Definir o custo como float
status = dataset[1:, 7] 

# Exercício 1 
sucess = np.char.startswith(status, 'Success') > 0
sum_sucess = sucess[sucess == True].sum()
porcent_sucess = (sum_sucess*100)/status.size
print('A porcentagem de sucesso das missões é de:', porcent_sucess, '%')

# Exercício 2
print('A media dos gastos de uma missão espacial é de:', cost[cost != 0].mean(), 'dólares.') 

# Exercício 3
location_USA = np.char.find(location, 'USA') > 0
sum_location_USA = location_USA[location_USA == True].sum()
print('A quantidade de missões espaciais realizadas pelos Estados Unidos é:', sum_location_USA)

# Exercício 4
detail_spacex = detail[company == "SpaceX"]
cost_spacex = cost[company == "SpaceX"]
max = np.argmax(cost_spacex)
print('A missão mais cara realizada pelas empresas SpaceX foi:', detail_spacex[max])

# Exercício 5
companys, missions = np.unique(company, return_counts = True)
#print(companys, missions)

i = 0
for cont in companys:
    print('Empresa:', companys[i] + ';', 'Total de missões:', missions[i])
    i += 1

