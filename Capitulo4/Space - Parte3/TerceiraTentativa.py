import numpy as np

dataset = np.loadtxt('.\Capitulo4\Space - Parte3\space.csv', delimiter=';', dtype = str, encoding = 'utf-8')

# SLICING 
company = dataset[1:, 1]
location = dataset[1:, 2]
detail = dataset[1:, 4]
cost = dataset[1:, 6].astype(float)
mission = dataset[1:, 7]

# QUESTÃO 1 

success_mission = np.char.startswith(mission, 'Success') > 0
sum_success_mission = success_mission[success_mission == True].sum()
print(sum_success_mission, 'missões foram realizadas com sucesso.')
print('A porcentagem de missões que deram certo é de:',  round(sum_success_mission*100/mission.size, 4), 'porcento')

# QUESTÃO 2

cost_positive = cost[cost > 0]
print('O valor medio de uma viagem espacial é de:', round(cost_positive.mean(),3), 'dólares')

# QUESTÃO 3

usa_mission = np.char.find(location, 'USA') > 0
sum_usa_mission = usa_mission[usa_mission==True].sum()
print(sum_usa_mission, 'missões realizadas pelos estados unidos.')

# QUESTÃO 4

spacex_detail = detail[company == 'SpaceX']
spacex_cost = cost[company == 'SpaceX']

max_spacex_cost = np.argmax(spacex_cost)
print('A missão mais cara realizada pela spacex é:', spacex_detail[max_spacex_cost])

# QUESTÃO 5

unique_company, frequency_company = np.unique(company, return_counts = True)
i = 0
for cont in unique_company:
    print(unique_company[i], ':', frequency_company[i])
    i += 1




