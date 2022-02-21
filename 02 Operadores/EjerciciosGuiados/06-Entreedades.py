# edad = int(input('Introduce tu edad: '))

# #veintes = edad >= 20 and edad < 30
# #print(veintes)
# #treintas = edad >= 30 and edad <40
# #print(treintas)

# if (edad >= 20 and edad < 30) or (edad >= 30 and edad <40):
#   print('Dentro de rango (20\'s) o (30\'s)')
# #    if veintes:
# #        print('Dentro de los 20\'s')
# #    elif treintas:
# #        print('Dentro de los 30\'s')
# #    else:
# #        print('Fuera de rango')
# else:
#   print("No está dentro de los 20's ni 30's")
    
    

# tarea
# Solicitar al usuario dos valores:

# numero1 (int)

# numero2 (int)

# Se debe imprimir el mayor de los dos números (la salida debe ser identica a la que sigue):

# Proporciona el numero1:
# Proporciona el numero2:
# El numero mayor es:<numeroMayor>
# Nota: Recordar que las tareas no cambian de estado y no afectan en el avance de tu curso ni en la generación de tu certificado de finalización del curso en Udemy.

# Preguntas de esta tarea
# ¿Cuál es el código del requerimiento solicitado?

numero1 = int(input('Proporciona el numero1: '))
numero2 = int(input('Proporciona el numero2: '))

if( numero1 > numero2):
	print(f"El número mayor es: {numero1}")
else:
  print(f"El número mayor es: {numero2}")