# Proporciona tu edad:

# 0-10: La infancia es increíble...
# 10-20: Muchos cambios y mucho estudio...
# 20-30: Amor y comienza el trabajo...

# Cualquier otro valor: Etapa de vida no reconocida

edad= int(input("Proporciona tu edad:"))
etapa = None

# if ( edad >= 0) and (edad <= 10):
# 	print("La infancia es increíble...")
# elif ( edad >= 10) and (edad <= 20):
#   print("Muchos cambios y mucho estudio...")
# elif ( edad >= 20) and (edad <= 30):
#   print("Amor y comienza el trabajo...")
# else:
# 	print("Etapa de vida no reconocida")

if (  0 <= edad < 10):
	print("La infancia es increíble...")
elif ( 10 <= edad < 20):
  print("Muchos cambios y mucho estudio...")
elif ( 20 <= edad < 30):
  print("Amor y comienza el trabajo...")
else:
	print("Etapa de vida no reconocida")
