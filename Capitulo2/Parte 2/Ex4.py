#Exercício 4)
distancia = float(input("Qual a distancia da viagem em km?"))
if distancia < 200.00:
    preco = 0.50*distancia
    print("Sua passagem custa R$", preco)
if distancia > 200.00:
    preco = 0.45*distancia
    print("Sua passagem custa R$", preco)
if distancia == 200.00:
    preco = 0.50200*distancia
    print("Sua passagem custa R$", preco)
else:
    print("distancia inválida")
