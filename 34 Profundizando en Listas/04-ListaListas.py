# Multiplicación listas
lista_multiplicacion = 5*[[2, 5]]
print(lista_multiplicacion)
print(f'Misma referencia: {lista_multiplicacion[0] is lista_multiplicacion[1]}')
print(f'Mismo contenido: {lista_multiplicacion[0] == lista_multiplicacion[1]}')
lista_multiplicacion[2].append(10)
print(lista_multiplicacion)
