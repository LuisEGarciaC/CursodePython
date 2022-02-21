
# *Tarea: Función con argumentos variables para sumar todos los valores recibidos
# *Crear una función para sumar los valores recibidos de tipo numérico, utilizando argumentos variables
# *args como parámetro de la función y regresar como resultado la suma de todos los valores pasados como argumentos.

# Crear una función para sumar los valores recibidos de tipo numérico, utilizando argumentos variables *args como parámetro de la función y regresar como resultado la suma de todos los valores pasados como argumentos.

# Preguntas de esta tarea
# ¿Cuál es el código de la función?
def sumar(*args):
    Suma = 0
    for valores in args:
      Suma += valores
    return Suma

resultado = sumar(1,2,3,4,5,6,7,8,9)
print(resultado)
