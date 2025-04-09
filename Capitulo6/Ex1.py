# EXERCÍCIO 1

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('.\Capitulo6\paises.csv', delimiter=';')

companyEUA = df[df["Location"].str.contains("USA")]["Company Name"].unique()
companyChina = df[df["Location"].str.contains("China")]["Company Name"].unique()
countries = ["EUA", "China"]
countriesData = [len(companyEUA), len(companyChina)]

plt.bar(countries, countriesData, color=['blue', 'red'])
plt.xlabel('País')
plt.ylabel('Empresas Espaciais')
plt.title('Empresas Espaciais nos EUA e na China')
plt.show()