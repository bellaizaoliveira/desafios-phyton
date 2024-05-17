# Lambda com for loop

'''
Será criado uma função lambda que deve elevar um número ao 
quadrado. Em seguida, seráusado essa função para calcular o
quadrado de todos os números em uma lista usando um for loop.

'''

numeros = [1, 2, 3, 4, 5, 6]
quadrado = lambda num: num ** 2

resultados = []
for i in numeros: 
    resultados.append(quadrado(i))

print(f'Os quadrados dos números {numeros} são {resultados}')