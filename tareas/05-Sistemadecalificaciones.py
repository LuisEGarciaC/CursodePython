# El objetivo del ejercicio es crear un sistema de calificaciones, como sigue:

# El usuario proporcionará un valor entre 0 y 10.

# Si está entre 9 y 10: imprimir una A

# Si está entre 8 y menor a 9: imprimir una B

# Si está entre 7 y menor a 8: imprimir una C

# Si está entre 6 y menor a 7: imprimir una D

# Si está entre 0 y menor a 6: imprimir una F

# cualquier otro valor debe imprimir: Valor desconocido

# Por ejemplo:

# Proporciona un valor entre 0 y 10:
# A
# Puedes utilizar el IDE de tu preferencia para codificar la solución y después pegar tu solución en esta herramienta.

calificacion = float(input("Ingrese la calificación: "))

if ( 9 < calificacion <= 10):
  print(f"La calificación {calificacion}: es A")
if ( 8 < calificacion <= 9):
  print(f"La calificación {calificacion}: es B")
elif ( 7 < calificacion <= 8):
  print(f"La calificación {calificacion}: es C")
elif ( 6 < calificacion <= 7):
  print(f"La calificación {calificacion}: es D")
elif ( 0 <= calificacion <= 6):
  print(f"La calificación {calificacion}: es F")
else:
	print("Valor desconocido")
