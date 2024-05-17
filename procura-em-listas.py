# Procura em Listas

'''
Será criado uma lista com os carros que você tem em estoque:

    - BMW X6;
    - BMW i5;
    - BMW i8;

Será pedido ao usuário para que ele insira o nome do carro 
que deseja comprar. Se o carro estiver em estoque, imprima
"Este carro está disponível". Se o carro não estiver em estoque,
imprima:

    "Este carro está disponível"

Se o carro não estiver em estoque, imprima:

    "Descupe, este carro não está disponível"
    
'''

estoque = ['BMW X6', 'BMW i5', 'BMW i8']
pesquisa_carro = input('Digite o carro desejado: ')

if pesquisa_carro in estoque:
    print('O carro está disponível em estoque')

else:
    print('O carro não está disponível em estoque')