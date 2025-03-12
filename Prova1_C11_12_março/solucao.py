import numpy as np

dataset = np.loadtxt('.\Prova1_C11_12_março\social_media.csv', delimiter = ';', dtype = str, encoding = 'utf-8')

# SLICING 

platform = dataset[1:, 1]
hashtag = dataset[1:, 2]
region = dataset[1:, 4]
views = dataset[1:, 5].astype(float)
likes = dataset[1:, 6].astype(float)

# QUESTÃO 1

brazil_region = np.char.startswith(region,'Brazil') > 0
sum_brazil_region = brazil_region[brazil_region==True].sum()
print(sum_brazil_region, 'posts são do Brasil.')

# QUESTÃO 2

education_hashtag = np.char.startswith(hashtag,'Education') > 0
sum_education_hashtag = education_hashtag[education_hashtag == True].sum()
print('A porcentagem de posts que possuem a hashtag "Education" no dataset é de:', round(sum_education_hashtag*100/hashtag.size, 4), 'porcento.')

# QUESTÃO 3

instagram_views = views[platform == 'Instagram']
instagram_likes = likes[platform == 'Instagram']

#print('A média de views do Instagram é:', round(instagram_views.mean(),3), 'views.')
#print('A média de likes do Instagram é:', round(instagram_likes.mean(),3), 'likes.')

mean_instagram = {'views': instagram_views.mean(),'likes': instagram_views.mean()}  # armazenando os valores em um dicionário
print('Os valores médios de views e likes do instagram são:', mean_instagram)       # mostrando o dicionário

# QUESTÃO 4

unique_platform, frequency_platform = np.unique(platform, return_counts = True)
most_platform = np.argmax(frequency_platform)
print(unique_platform[most_platform], 'é a plataforma com maior quantidade de posts neste dataset com', frequency_platform[most_platform], 'posts.')

# QUESTÃO 5

most_likes = np.argmax(likes)
print('A região de onde saiu o post com maior número de likes é:', region[most_likes])


