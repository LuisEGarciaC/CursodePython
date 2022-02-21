#Tarea: Función con argumentos variables para multiplicar los valores

# Crear una función para multiplicar los valores recibidos de tipo numérico, utilizando argumentos variables *args como parámetro de la función y regresar como resultado la multiplicación de todos los valores pasados como argumentos.


def multiplicar(*args):
    Resultado = 1
    for valor in args:
      Resultado *= valor
    return Resultado

resultado = multiplicar(5, 5)
print(resultado)
