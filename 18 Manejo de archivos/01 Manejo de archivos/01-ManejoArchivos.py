import pathlib

# Obtengo la ruta absoluta
path = pathlib .Path( __file__ ) .parent .absolute()

try :
    archivo = open( str( path ) + '/test.txt' , 'w' )
    archivo .write( 'Hola Mundo!\n' )
    archivo .write( 'HOLA LUIS SI SE LOGRO!!\n' )
    archivo .write( 'Escribiendo archivo desde Python.' )
except Exception as e:
    print(e)
finally:
    archivo.close()
    print("Logrado!!!")
