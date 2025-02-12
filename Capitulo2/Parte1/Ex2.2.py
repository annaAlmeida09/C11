#Exercicio 2)
numero = int(input('Escreva um numero inteiro.'))
intervaloInicio = int(input('Escreva o inicio do intervalo.'))
intervaloFim = int(input('Escreva o fim do intervalo.'))

for c in range(intervaloInicio,(intervaloFim+1)):
    print(c, 'x', numero, '=', c*numero)
