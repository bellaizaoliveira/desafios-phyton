# Funções

'''
Criar um programa que calcula a quantidade de tinta necessária
para pintar uma parede. Ousuário deverá fonrcer as seguintes
informações: Rendimento, altura e largura.

O programa deve mostrar na tela a mensagem  "Você necessita de X
latas de tinta".

'''

rendimento = int(input('Qual é o rendimento da lata de tinta? '))
altura = int(input('Qual a altura da parede? '))
largura = int(input('Qual a largura da parede? '))

def calculo_tinta():
    area = altura * largura
    total = area / rendimento
    print(f'Você precisa de {total} latas de tinta')

calculo_tinta()