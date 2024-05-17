# Comparação em Sets 

'''
Será criado dois conjuntos, cada um contendo 5 nomes de seus amigos.
Alguns nomes devem estar presentes em ambos os conjuntos. Será usado 
um método para encontrar quais nomes aparecem em ambos os conjuntos e 
será impresso o resultado.

'''

friends1 = {'Ana','Arthur,' 'Hugo', 'Isac', 'Léo', 'Madu'}
friends2 = {'Aline', 'Arthur', 'Hugo', 'Isac', 'Léo'}

result = friends1.intersection(friends2)

# result = friends1.unio(friends2)
# result = friends1.difference(friends2)

print(result)