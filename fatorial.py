# Calculando Fatorial

'''
As funções recursivas são funções que se chamam dentro do seu próprio
bloco de código. Elas são úteis para resolver problemas que podem ser
divididos em problemas menores de natureza semelhante.

Um exemplo clássico de onde a recursão é usada é o cálculo de um número.
O fatorial de um número n é o produto de todos os números de n até 1.

'''

def fatorial(n):
    if n == 0 or n  == 1:
        return 1
    
    else:
        return n * fatorial(n - 1)
    
user_number = int(input('Digite umnúmero: '))

print(f'O fatorial de {user_number} é {fatorial(user_number)}')