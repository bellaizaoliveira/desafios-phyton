# Calculando base e expoente

'''
Será criado uma função que calcule a potência de um número.
A função deverá aceitar dois argumentos: a base e o expoente.
No entanto, se o expoente não for fornecido ao chamar a função,
ele deve assumir o valor padrão de 2.

'''

def potencia(base, expoente = 2):
    return base ** expoente

user_number = int(input('Digite o número base: '))
user_expoente = input('Digite um expoente (default 2): ')

if user_expoente:
    print(f'O resultado é: {potencia(user_number, int (user_expoente))}')

else:
    print(f'O resultado é: {potencia(user_number)}')