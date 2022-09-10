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
print(directorio['juan'])