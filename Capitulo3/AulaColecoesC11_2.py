# LISTAS

nomes = ['Goku', 'Vegeta', 'Trunks', 'Gohan']
# INSERT
nomes.append('Bulma') # Insere no final da lista
nomes.insert(2, 'Picolo') # Insere na posição 2
print(nomes)

# UPDATE
nomes[0] = 'Goten' # Substituir Goku por Goten

# DELETE
del nomes[1] # excluindo pelo indice / nomes.pop(1)
nomes.remove('Trunks') # excluindo pelo nome

print(nomes)

if 'Picolo' in nomes:       # em outras linguagens um for seria necessário
    print('Picolo is here!!!')
