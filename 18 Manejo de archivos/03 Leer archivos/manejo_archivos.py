import pathlib

# Obtengo la ruta absoluta
path = pathlib .Path( __file__ ) .parent .absolute()

try :
    archivo = open( str( path ) + '/prueba.txt' , 'w', encoding='utf8')
    archivo.write('Agregamos información al archivo Luis García\n')
    archivo.write('Adios')
except Exception as e:
    print(e)
finally:
    archivo.close()
    print('Fin del archivo')
    # archivo.write('nueva info')
