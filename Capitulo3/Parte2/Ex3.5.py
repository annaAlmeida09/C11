# Exercicio 5)
nome = []
sexo = []
idade = []

num_pessoas = int(input("Quantas pessoas deseja cadastrar?"))

for i in range(num_pessoas):
    nome.append(input('Escreva o nome da pessoa. '))
    sexo.append(input('Escreva o sexo da pessoa. '))
    idade.append(float(input('Escreva a idade da pessoa. ')))

for i in range(num_pessoas):
    media = 0
    media += idade[i]

media = media/num_pessoas

for i in range(num_pessoas):
    mulheres = 0
    if sexo[i] == 'F' and idade[i] < 20:
        mulheres += 1

print('A media das idades:', media)
print('O numero de mulheres com menos de vinte anos:', mulheres)
    


