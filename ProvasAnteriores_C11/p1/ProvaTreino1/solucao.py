import numpy as np

dataset = np.loadtxt('./ProvasAnteriores_C11/p1/ProvaTreino1/artists_v2.csv', delimiter = ',' , dtype = str , encoding = 'utf-8')

# Slicing 
artist = dataset[1:, 0]
country = dataset[1:, 1]
period_active = dataset[1:, 2]
year = dataset[1:, 3]
genre = dataset[1:, 4]
tcu = dataset[1:, 5]
sales = dataset[1:, 6]



# Questão 1
# print(country)
country_eua = np.char.startswith(country, 'United States') > 0
sum_country_eua = country_eua[country_eua == True].sum()
print('A porcentagem de artistas dos Estados Unidos é de:', (sum_country_eua*100)/country.size, '%')

# Questão 2
# print(artist)
artist_present = np.char.find(period_active, 'present') > 0
sum_artist_present = artist_present[artist_present == True].sum()
print('A quantidade de artistas que não estão mais em atividade é de:', period_active.size - sum_artist_present, 'artistas.')

# Questão 3
min = np.argmin(year)
min_country = country[min]
min_artist = artist[min]
print('O artista com o álbum mais antigo é', min_artist, 'do país', min_country + '.')

# Questão 4
top_artists = artist[0:10] # 0 exclusive e 10 inclusive 
print(top_artists)
