aux = 1

while aux == 1:
    sexo = input("Digite M se for mulher ou digite H se for homem.") 
    if sexo == 'M':
        print("Mulher autenticada")
        break
    if sexo == 'H':
        print("Homem autenticado")
        break
    else:
        print('Caractere inválido')
    
    
