import numpy as np

dataset = np.loadtxt('.\Capitulo4\Space - Parte3\space.csv', delimiter =';', dtype = str, encoding = 'utf-8')

# Slicing 

num = dataset[1:,0]
company = dataset[1:,1]
location = dataset[1:,2]
datum = dataset[1:,3]
detail = dataset[1:,4]
rocket = dataset[1:,5]
cost = dataset[1:,6].astype(float)
mission = dataset[1:,7]

success_mission = np.char.startswith(mission, 'Success') > 0
sum_success_mission = success_mission[success_mission == True].sum()
print('A porcentagem de foguetes que obteve sucesso é de:', round((sum_success_mission*100)/mission.size,4), '%')

avaible_costs = cost[cost > 0]
print('O valor médio de uma missão espacial é de:', round(avaible_costs.sum()/avaible_costs.size,4),'dólares.')

usa_location = np.char.find(location, 'USA') > 0
sum_usa_location = usa_location[usa_location == True].sum()
print('A quantidade de missões realizadas pelos estados unidos é:', sum_usa_location)

cost_spacex = cost[company == 'SpaceX']
detail_spacex = detail[company == 'SpaceX']
max_spacex = np.argmax(cost_spacex)
print('A missão mais cara é:', detail_spacex[max_spacex])

unique_companys, frequency_companys = np.unique(company, return_counts = True)

i = 0
for cont in unique_companys:
    print(unique_companys[i], frequency_companys[i])
    i += 1  




