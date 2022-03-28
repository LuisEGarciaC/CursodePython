
import pathlib

# Obtengo la ruta absoluta
path = pathlib .Path( __file__ ) .parent .absolute()

with open( str( path ) + '/prueba.txt','r', encoding='utf8') as archivo:
    print(archivo.read())
