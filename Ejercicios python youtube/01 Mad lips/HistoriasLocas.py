""" 
  Concatenar cadenas de caracteres
  Supongamos que queramos crear una cadena de caracteres que diga:
  
  Aprende a programar con ________.
    
  
"""

# PalabraAgregar = input("Apalabra a agregar: ")

# print('Aprende a programar con ' + PalabraAgregar)
# print('Aprende a programar con {}'.format(PalabraAgregar))
# print(f'Aprende a programar con {PalabraAgregar}')

# Mad Lips (Historias locas)

adj = input("Adjetivo: ")
Verbo1 = input("Un vervo: ")
Verbo2 = input("Un vervo: ")
Sustantivo_plural = input("Sustantivo (plural): ")

madlib = (f'!Programar es tan {adj}! Siempre me emociona por que me encanta {Verbo1} problemas.¡ Aprende a {Verbo2} con freeCodeCamp Español y alcansa tus {Sustantivo_plural}!' )

print(madlib)