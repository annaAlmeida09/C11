# EXERCÍCIO 2

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('.\Capitulo6\space.csv', delimiter=';')

usaData = df[df['Region'].str.contains("NORTHERN AMERICA")]


plt.plot(usaData["Country"], usaData["Deathrate"], label='Taxa de Mortalidade', marker='o')
plt.plot(usaData["Country"], usaData["Birthrate"], label='Taxa de Natalidade', marker='o')
plt.xlabel('Países')
plt.ylabel('Taxas')
plt.title('Taxa de Mortalidade e Natalidade nos Países da América do Norte')
plt.legend(loc='upper right')
plt.grid(True)

plt.tight_layout()
plt.show()