# Sets

'''
Criar um programa que gera 3 listas de acordo com a necessidade logo abaixo:

Lista1 - Funcionários que tem carro e trabalham a noite
Lista2 = Funcionários que tem carro e trabalham de dia
Lista3 = Funcionários que não tem carro

'''

funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Julia', 'Bruno', 'Melissa']
turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
turno_noite = ['Pedro', 'Julia', 'Bruno']
tem_carro = ['Marcos', 'Alice', 'Brunco', 'Melissa']

# Lista1
lista1 = set(tem_carro).intersection(turno_noite)
print(lista1)

# Lista2
lista2 = set(tem_carro).intersection(turno_dia)
print(lista2)

# Lista3
lista3 = set(funcionarios).difference(tem_carro)
print(lista3)