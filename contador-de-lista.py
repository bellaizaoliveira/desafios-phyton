# Desafio 15

'''
Será criado uma lista de frutas que inclui "maçã" três vezes e 
outras frutas de sua escolha. Será utilizado um for loop para 
contar quantas vezes "maçã" aparece na lista e imprima o resultado
'''

frutas = ['Maçã','Banana', 'Maçã', 'Maçã', 'Abacate', 'Uva' ]
contador = 0

for fruta in frutas:
    if fruta == 'maça':
        contador += 1


print('Número de maçãs na lista', contador)