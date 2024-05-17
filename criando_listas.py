# Criando Listas

'''
Será criado um script que solicite ao usuário dois números.

Em seguida, o script deve imprimir a soma, a subtração, a multiplicação, 
a divisão (resultado decimal) e exponênciação (primeiro número elevado ao 
segundo número) desses dois números.

'''

# Pedir ao usuário que digite dois números
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo numero: '))

# Realizar os cálculos matemáticos
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
exponenciacao = num1 ** num2

# Imprimindo os resultados na console
print(f'Soma: {soma}')
print(f'Subtração: {subtracao}')
print(f'Multiplicacao: {multiplicacao}')
print(f'Divisao: {divisao}')    
print(f'Exponenciação: {exponenciacao}')


