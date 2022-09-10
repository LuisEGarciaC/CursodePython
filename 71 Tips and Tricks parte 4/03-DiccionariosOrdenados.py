# Diccionarios - dicts
# maps, hashmaps, lookup tables, etc (llave-valor)
# Ejemplo clasico: directorio (llave=nombre, valor=telefono)
directorio = {
    'Juan': 55689001,
    'Alicia': 56432217,
    'Carlos': 56772345
}
# Imprimir el diccionario
print(directorio)

# Recuperar un elemento
print(directorio['Juan'])

# Arroja un error KeyError al no encontrar una llave
# print(directorio['juan'])

# Podemos utilizar una expresion para crear un diccionario
valores_al_cuadrado = {x: x*x for x in range(5)}
print(valores_al_cuadrado)

# Los tipos mutables no pueden ser llaves de un diccionario
lista = [1,2,3]
# diccionario_erroneo = {lista: 'A'}
# print(diccionario_erroneo)

# Pero los tipos inmutables pueden ser llaves de un diccionario
tupla = (1,2,3)
diccionario_correcto = {tupla: 'A'}
print(diccionario_correcto)

# Si queremos garantizar un orden de insercion, OrderedDict
from collections import OrderedDict

diccionario_ordenado = OrderedDict(uno=1,dos=2,tres=3)
print(diccionario_ordenado)
# Agregamos un nuevo elemento
diccionario_ordenado['cuatro']=4
print(diccionario_ordenado)
# Obtenemos las llaves
print(diccionario_ordenado.keys())

# Si cambiamos algun valor de alguna llave, se mantiene el orden de insercion de las llaves
diccionario_ordenado['uno']=-1
print(diccionario_ordenado)

# Eliminamos una llave
diccionario_ordenado.pop('tres')
print(diccionario_ordenado)

# Volvemos a insertar el elemento eliminado
diccionario_ordenado['tres']=3
print(diccionario_ordenado)
