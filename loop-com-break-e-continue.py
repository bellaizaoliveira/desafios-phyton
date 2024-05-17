# Loop com Break e Continue

'''
Será criado um loop que imprima os números de 1 a 10,
mas pare de imprimir assim que chegar a 5 usando o comando 'break'.

Em seguida, crie um segundo loop que imprima os números de 1 a 10,
mas pule a impressão do número 5 usando o comando 'continue'.

'''

print('Loop com o break: ')
for numero in range(1, 11):
    if numero > 5:
        break
    print(numero)

print('\nloop com o continue:')
for numero in range(1, 11):
    if numero == 8:
        continue
    print(numero)