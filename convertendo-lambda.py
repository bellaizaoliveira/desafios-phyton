# Convertendo para Lambda

'''
Será criado uma função lamba que aceite um número e retorne
o cubo desse número.

'''

# def cub(num):
#   return num ** 3

cubo = lambda num: num ** 3

user_number = int(input('Digite um número: '))
print(f'O cubo de {user_number} é {cubo(user_number)}')