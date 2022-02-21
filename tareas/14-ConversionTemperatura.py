#Conversión de Temperatura

# Realizar dos funciones para convertir de grados celsius a fahrenheit y viceversa.

# Función 1. Recibir un parámetro llamado celcius y regresar el valor equivalente a fahrenheit

# La función se llama: celsius_fahrenheit(celsius) 

# La fórmula para convertir de celsius a fahrenheit es: celsius * 9/5 + 32 

# Función 2. Recibir un parámetro llamado fahrenheit y regresar el valor equivalente a celsius:

# fahrenheit_celsius(fahrenheit)         

# La fórmula para convertir de fahrenheit a celsius es:  (fahrenheit-32) * 5/9

# Los valores los debe proporcionar el usuario, utilizando la función input y convirtiendolo a tipo float.

# Deben hacer al menos dos pruebas, una donde conviertan de grados celcius a grados fahrenheit, y otra donde conviertan de grados fahrenheit a grados celsius y mandar a imprimir los resultados.

# Preguntas de esta tarea
# Cuál es el código del ejercicio solicitado?

def celsius_fahrenheit(celsius) :
  resultado = celsius * 9/5 + 32 
  return float(resultado)

def fahrenheit_celsius(fahrenheit):
  resultado = (fahrenheit-32) * 5/9
  return float(resultado)

fahrenheit = int(input("Valor a comvertir en fahrenheit: "))
grados = int(input("Valor a comvertir en grados: "))

print(f" el valor de celcius {fahrenheit}° convertido en fahrenheit es: {celsius_fahrenheit(fahrenheit)} ")
print(f" el valor de fahrenheit {grados}F convertido en fahrenheit es: {fahrenheit_celsius(grados)} ")