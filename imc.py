# Calculo de IMC - Índice de Massa Corporal

'''
Qual é a sua altura em cm:
Qual é o seu peso em kg:

# Menor que 18,5 magreza
# Entre 18,5 e 24,9 normal
# Entre 25,0 e 29,9 sobrepeso
# Entre 30,0 e 39,9 obesidade
# Maior que 40,0 obesidade grave

'''
altura = float(input('Qual é a sua altura em cm: '))
peso = float(input('Qual é o seu peso em kg: '))

IMC = peso / (altura/100)**2

if IMC < 18.5:
    print('Magreza')

elif IMC >= 18.5 and IMC < 24.9:
    print('Normal')

elif IMC >= 25.0 and IMC < 29.9:
    print('Sobrepeso')

elif IMC >= 30.0 and IMC < 39.9:
    print('Obesidade')

else:
    print('Obesidade Grave')

