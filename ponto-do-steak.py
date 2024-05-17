# If, Elif, Else

'''
Criar um programa que dependendo da temperatura (em celsius) do steak ele
retorna o ponto de cozimento. O usuário deverá fornecer a temperatura.

Temperaturas - Cozimento
120ºF ou 48ºC - Rare (Selado)
130ºF ou 54ºC - Medium rare (Ao ponto para o mal)
140ºF ou 60ºC - Medium (Ao ponto)
150ºF ou 65ºC - Medium well (Ao ponto para o bem)
160ºF ou 71ºC - Well done (Bem Passada)

'''

tem_cel = int(input('Qual é a temperatura da carne? '))

if tem_cel < 48:
    print('Cozinhas por mais alguns minutos')

elif tem_cel in range(48, 53):
    print('Selada')

elif tem_cel in range(54, 59):
    print('Ao ponto para mal')

elif tem_cel in range(60, 64):
    print('Ao ponto')

elif tem_cel in range(65, 70):
    print('Ao ponto para o bem')

elif tem_cel>=71:
    print('Bem Passada')