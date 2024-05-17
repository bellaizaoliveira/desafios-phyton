# Funções Simples

'''
Será criado uma função que aceitará um número como entrada e 
retorna o quadrado desse número.

'''

def quadrado(numero):
    return numero ** 2

num = int(input('Digite um número: '))

print(f'O quadrado de {num} é {quadrado(num)}')