# Pesquisa de Páis e Capital

'''
Será criado uma lista com 5 nomes de países e as capitais
desses países.

Será pedido ao usuário para digitar o nome de um país.

    Se o país estiver na lista, imprima:

        'A capital de [país] é [capital]'
    
    Se o país não estiver na lista, imprima:

        'Descupe, não temos informações sobre a capital desse país'
        
'''

capitais = {
    'Brasil': 'Brasília',
    'Argentina': 'Buenos Aires',
    'Chile': 'Santiago',
    'Austrália': 'Canberra',
    'Canadá': 'Ottawa'

}

pais_usuario = input('Digite o nome do país: ')

if pais_usuario in capitais:
    print(f'A capital de {pais_usuario} é {capitais[pais_usuario]}')

else:
    print('Descupe, não temos informções sobre a capital desse país.')