# DICIONÁRIO

pessoa = {'nome':'Goku','idade': 42} # Lembra um struct ou Json
print(pessoa)
# Acessar
print(pessoa['nome'])
# Insert
pessoa['sexo'] = 'M'
# Update
pessoa['nome'] = 'Vegeta'

print(pessoa)

del pessoa['sexo']

print(pessoa)
