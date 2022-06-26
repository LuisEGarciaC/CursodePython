

# def encriptar(text):
#   PalabraFinal = ''
#   print(f"encritar {text}")
#   for letra in text:
#     PalabraFinal += letra + 'x'
#   return PalabraFinal
  
  
  
# def desencriptar(text):
#   print(f"desencriptar {text}")
#   textoFinal = ''
#   contador = 0
#   for letra in text:
#     if contador % 2 == 0:
#       textoFinal += letra 
#     contador += 1
#   return textoFinal
  
  
# def encriptar(texto):
#   textoFinal = ''
#   print(f"encritar {texto}")
#   for letra in texto:
#     ascii = ord(letra)
#     ascii += 1
#     textoFinal += chr(ascii)
#   return textoFinal
  
  
# def desencriptar(texto):
#   print(f"desencriptar {texto}")
#   textoFinal = ''
#   for letra in texto:
#     ascii = ord(letra)
#     ascii -= 1
#     textoFinal += chr(ascii)
#   return textoFinal

def encriptar(texto, desplazo):
  textoFinal = ''
  # print(f"encritar {texto}")
  for letra in texto:
    ascii = ord(letra)
    ascii += desplazo
    textoFinal += chr(ascii)
  return textoFinal
  
  
def desencriptar(texto, desplazo):
  # print(f"desencriptar {texto}")
  textoFinal = ''
  for letra in texto:
    ascii = ord(letra)
    ascii -= desplazo
    textoFinal += chr(ascii)
  return textoFinal


def encriptararchivo(lugarArchivo,desplazo):
  # encrytar
  arch = open(lugarArchivo, 'r')
  txt = arch.read()
  arch.close()
  txtencyp = encriptar(txt, desplazo)
  
  arch = open(lugarArchivo, 'w')
  arch.write(txtencyp)
  arch.close()
  
  print("El archivo ha sido encriptado...")
  
  
def desencriptararchivo(lugarArchivo, desplazo):
  # encrytar
  arch = open(lugarArchivo, 'r')
  txt = arch.read()
  arch.close()
  txtdesencyp = desencriptar(txt, desplazo)
  
  arch = open(lugarArchivo, 'w')
  arch.write(txtdesencyp)
  arch.close()
  
  print("El archivo ha sido desencriptado...")



desicion = input("Desea Encriptar (E) o Desencriptar (D) un archivo: ").upper()
lugarArchivo = input("Escribe la ubicación del archivo con el nombre del mismo: ")
desplazo = int(input("cuantas numeros de desplazo: "))

if desicion == 'E': 
  encriptararchivo(lugarArchivo, desplazo)
else:
  desencriptararchivo(lugarArchivo, desplazo)