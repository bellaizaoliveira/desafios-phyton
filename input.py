# Input

'''
Crie um script que pergunte o nome e a idade do usuário.

Após isso, o script deve imprimir uma mensagem que diga:

    "Hello Love, seu nome é [nome]! Você tem [idade] anos."
    
'''

first_name = input('Qual é o seu nome? ')
age = int(input('Quantos anos você tem? '))

# print("Hello Love, seu nome é {}! Você tem {} anos.".format(first_name, age))
# print("Hello Love, seu nome é ", first_name, "! Você tem ", age, " anos.")

print(f"Hello Love, seu nome é {first_name}! Você tem {age} anos.")
