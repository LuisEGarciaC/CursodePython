# Qué son las tuplas
# En Python, una tupla es un conjunto ordenado e inmutable de elementos del mismo o diferente tipo.

# Las tuplas se representan escribiendo los elementos entre paréntesis y separados por comas.

# >>> (1, "a", 3.14)
# (1, 'a', 3.14)

# En realidad no es necesario escribir los paréntesis para indicar que se trata de una tupla, basta con escribir las comas, pero Python escribe siempre los paréntesis:

# >>> 1, "a", 3.14
# (1, 'a', 3.14)
# La función len() devuelve el número de elementos de una tupla:

# >>> len((1, "a", 3.14))
# 3
# Una tupla puede no contener ningún elemento, es decir, ser una tupla vacía.

# >>> ()
# ()
# >>> len(())
# 0
# Una tupla puede incluir un único elemento, pero para que Python entienda que nos estamos refiriendo a una tupla es necesario escribir al menos una coma.

# El ejemplo siguiente muestra la diferencia entre escribir o no una coma. En el primer caso Python interpreta la expresión como un número y en el segundo como una tupla de un único elemento.

# >>> (3)
# 3
# >>> (3,)
# (3,)
# Python escribe una coma al final en las tuplas de un único elemento para indicar que se trata de un tupla, pero esa coma no indica que hay un elemento después:

# >>> (3,)
# (3,)
# >>> len((3,))
# 1


#Definir una tupla
frutas = ('Naranja', 'Plátano', 'Guayaba')
print(frutas)
#saber el largo
print(len(frutas))
#acceder a un elemento
print(frutas[0])
# navegación inversa
print(frutas[-1])
# acceder a un rango
print(frutas[0:1])# sin incluir el último índice
#recorrer elementos
for fruta in frutas:
    print(fruta, end=' ')
#cambiar valor tupla
# frutas[0] = 'Pera'
frutasLista = list(frutas)
frutasLista[0] = 'Pera'
frutas = tuple(frutasLista)
print('\n',frutas)
#eliminar la tupla
del frutas
print(frutas)
