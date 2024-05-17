# Multiplicando Lambda

'''
Será criado uma função lambda que aceite dois números e retorne 
a multiplicação desses números.

'''

# def multiplicar(num, num 2):
#  return num1 * num2

multiplicar = lambda num1, num2: num1 * num2

user_number1 = int(input('Digite o primeiro número: '))
user_number2 = int(input('Digite o segundo número: '))

print(f'A multiplicação de {user_number1} e {user_number2} é
      {multiplicar(user_number1, user_number2)}')
