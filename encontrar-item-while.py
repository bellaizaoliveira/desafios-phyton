# Encontrando um item com While

'''
Será criado um loop que peça ao usuário para digitar o nome de uma fruta.

    - Se a fruta digitada não for 'Morango', o loop deve continuar pedindo
    ao usuário para digitar o nome de uma fruta.

    - Se a fruta for 'Morango', o loop deve terminar e o programa deve imprimir
    'Parabéns, você acertou a fruta!'.

'''

while True:
    fruta = input('Digite o nome de uma fruta: ')
    if fruta.lower() == 'morango':
        break

print('Parabéns, você acertou a fruta!')