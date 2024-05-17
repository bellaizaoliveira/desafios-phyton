# Duas Funções

'''
Será criado duas funções. A primeira deve aceitar um
número e retornar o dobro desse número. A segunda função
deve aceitar um número e retornar o quadrado desse número. 
Em seguida, será chamado a primeira função dentro da segunda
para retornar o quadrado do dobro de um número.

'''

def dobrar(num):
    return num * 2

def quadrado(num):
    return dobrar(num) ** 2

user_number = int(input('Digite um número: '))
print(f'O quadrado do dobro do número {user_number} é {quadrado(user_number)}')