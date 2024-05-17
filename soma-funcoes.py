# Soma de Funções

'''
Será criado uma função que aceite dois números como entrada 
e retorne a soma desses dois números.

'''

def soma(num1, num2):
    return num1 + num2

user_num1 = int(input('Digite o primeiro número: '))
user_num2 = int(input('Digite o segundo número: '))

print(f'A soma dos dois números é igual a: {soma(user_num1, user_num2)}')
