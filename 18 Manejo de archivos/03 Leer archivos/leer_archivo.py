import pathlib

# Obtengo la ruta absoluta
path = pathlib .Path( __file__ ) .parent .absolute()

archivo = open(str( path ) + '/prueba.txt', 'r', encoding='utf8')

# archivo = open('prueba.txt', 'r', encoding='utf8')
# lee el archivo completo
# print(archivo.read())

# leer algunos caracteres
# print(archivo.read(5))
# print(archivo.read(3))

# leer lineas completas
print(archivo.readline())
print(archivo.readline())
