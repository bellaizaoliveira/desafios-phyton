# Lambda com If e Else

'''
Será criado uma função lambda que aceite um número e retornará 
"Par" se o número for par e "Ímpar" se o número for ímpar.

'''

# def par_ou_impar(num):
#   if num % 2 == 0:
#       return 'Par'
#   else: 
#       return 'Ímpar'

par_ou_impar = lambda num: 'Par' if num % 2 == 0 else 'Ímpar'

user_number = int(input('Digite um número: '))
print(f'O número {user_number} é {par_ou_impar(user_number)}')