#Exercício 5)
aut = 0
while aut == 0:
    num = int(input('Entre um número entre 1000 e 9999.'))
    if num >= 1000 and num <= 9999:
        print("Seu número é:", num)
        aut = 1
        break
    else:
        print("Número inválido.")
        aut = 0
print(num % 10)
dezena = int(((num-num%10)/10)%10)
print(dezena)
centena = int(((num-(dezena*10 + num%10))/100)%10)
print(centena)
milhar = int(((num-(centena*100 + dezena*10 + num%10))/1000))
print(milhar)

