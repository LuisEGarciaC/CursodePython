
# EJERCICIO
# ingresar un  numero cualquier si en un condicional if verificar si esta o no dentro de los valores 0 y 8

numero  = int(input('Ingresa un numero: '))
valorMinimo = 0
valorMaximo = 5
comparacion = ( numero >= valorMinimo) and ( valorMaximo <= 5)

if comparacion:
	print(f'El número {numero} esta dentro del rango de 0 y 5')
else:
  print(f'El número {numero} no esta dentro del rango de 0 y 5')


