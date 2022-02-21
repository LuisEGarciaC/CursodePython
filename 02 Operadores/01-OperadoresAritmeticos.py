# operador aritmetico de suma
operandoA = 3
operandoB = 2
suma = operandoA + operandoB
#print('Resultado suma:', suma)
print(f'Resultado suma: {suma} ')

# operador aritmetico de resta
resta = operandoA - operandoB
print(f'Resultado resta: {resta}')

# operador aritmetico de multiplicación
multiplicacion = operandoA * operandoB
print(f'Resultado multiplicación: {multiplicacion}')

# operador aritmetico de división
division = operandoA / operandoB
print(f'Resultado división: {division}')

# operador aritmetico de división entera
divisionEntera = operandoA // operandoB
print(f'Resultado división en número entero: {divisionEntera}')

# operador aritmetico de modulo
modulo = operandoA % operandoB
print(f'Resultado residuo division (módulo): {modulo}')

# operador aritmetico de exponente
exponente = operandoA ** operandoB
print(f'Resultado del exponente: {exponente}')


# TAREA

# En el siguiente ejercicio se solicita calcular el área y el perímetro de un Rectángulo, para ello deberemos crear las siguientes variables:

# alto (int)

# ancho (int)

# El usuario debe proporcionar los valores de largo y ancho, y después se debe imprimir el resultado en el siguiente formato(no usar acentos y respetar los espacios, mayúsculas, minúsculas y saltos de línea):

# Proporciona el alto:
# Proporciona el ancho:
# Area: <area>
# Perímetro: <perimetro>
# Las fórmulas para calcular el área y el perímetro de un Rectángulo son:

# Área: alto * ancho

# Perímetro: (alto + ancho) * 2

# Nota: Recordar que las tareas no cambian de estado y no afectan en el avance de tu curso ni en la generación de tu certificado de finalización del curso en Udemy.

# Preguntas de esta tarea
# ¿Cuál es el código del requerimiento solicitado?

# alto = 50
# ancho = 20

alto = int(input('Proporciona el alto: '))
ancho = int(input('Proporciona el ancho: '))
Area = alto * ancho
Perímetro = (alto + ancho) * 2
print(f'El Área del Rectángulo es: {Area}')
print(f'El Perímetro del Rectángulo es: {Perímetro}')
