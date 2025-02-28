#Exercício 3
import numpy as np

field = np.zeros([2, 2], dtype=int)
coluna_aleatória = np.random.randint(0, 2)
linha_aleatória = np.random.randint(0, 2)
field[linha_aleatória][coluna_aleatória] = 1 

mascara = [['*', '*'], ['*', '*']]
contador = 0

def print_mask(mask):
    for row in mask:
        print(" ".join(str(cell) for cell in row))

while 1:
    
    if(contador == 3):
        print("Parabéns, você venceu o jogo!!!")
        break
    
    print("Selecione uma posição x e y (0 ou 1):")
    print_mask(mascara)
    x = int(input("Digite o valor de x:"))
    y = int(input("Digite o valor de y:"))
    
    if field[x][y] == 1:
        print("Você perdeu...")
        break
    else:
        mascara[x][y] = '0'
        contador += 1