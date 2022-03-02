# Definir una clase padre llamada Vehiculo y dos clases hijas llamadas Coche y Bicicleta, las cuales heredan de la clase Padre Vehiculo
# clace Vehiculo
class Vehiculo:
	def __init__(self,color, ruedas):
				self.color = color
				self.ruedas = ruedas

# llamado a imprimir
	def __str__(self):
		return f'Vehiculo[color: {self.color}, Ruedas: {self.ruedas}]'

# clace coche
class Coche(Vehiculo):
	def __init__(self,color, ruedas, velocidad):
			super().__init__(color, ruedas)
			self.velocidad = velocidad
# llamado a imrimir de la clace coche y vehiculo
	def __str__(self):
		return f'Velocidad[velocidad: {self.velocidad} (km/hr)] {super().__str__()} '

# clace Bicicleta y vehiculo
class Bicicleta(Vehiculo):
	def __init__(self,color, ruedas, tipo):
			super().__init__(color, ruedas)
			self.tipo  = tipo

	def __str__(self):
		return f'Tipo de bicicleta [tipo : {self.tipo }] {super().__str__()} '


respuesta1 = Vehiculo('negro', 28)
print(respuesta1)

respuesta2 = Coche('negro', 28, 50)
print(respuesta2)

respuesta3 = Bicicleta('negro', 28, 'montañera')
print(respuesta3)

