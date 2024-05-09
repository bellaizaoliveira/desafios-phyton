# Nested For Loop

'''
Será criado uma lista de frutas e outra de vegetais.

Use um 'for loop' aninhado (Nested For Loop) para imprimir
todas as combinações possíveis de frutas e vegetais, com a 
fruta primeiro e o vegetal em segundo.
'''

frutas = ['Morango', 'Manga', 'Uva']
vegetais = ['cenoura', 'alface', 'brocolis']

for fruta in frutas:
    for vegetal in vegetais:
        print(fruta, vegetal)