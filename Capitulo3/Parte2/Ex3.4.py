# Exercicio 4)

pessoas = []
pesada = 0
leve = 9999

for i in range (3):
    nome = str(input('Escreva o nome da pessoa.'))
    peso = float(input('Escreva o peso da pessoa.'))
    pessoas.append ({'nome':nome,'peso' : peso})
    if peso > pesada:
        pesada = peso
        pessoa_pesada = nome
    if peso < leve:
        leve = peso
        pessoa_leve = nome
print('A pessoa mais leve:', pessoa_leve)
print('A pessoa mais pesada:', pessoa_pesada)