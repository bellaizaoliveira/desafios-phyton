# Verificador de Idade

'''
Será pedido ao usuário que digite sua idade. 

    - Se a idade for menor que 13, imprima 'Você é uma criança"

    - Se a idade estiver entre 13 e 19, imprima "Você é um adolescente"

    - Se a idade for 20 ou mais, imprima "Você é um adulto"
    
'''

idade = int(input('Digite a sua idade: '))

if idade > 13:
    print('Você é uma criança!')

elif idade >= 13 and idade < 20:
    print('Você é um adolescente!')

else:
    print('Você é um adulto!')

