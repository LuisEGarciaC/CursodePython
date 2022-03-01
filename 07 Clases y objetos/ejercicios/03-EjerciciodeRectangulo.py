class Reactangulo:
	def __init__(self, base, altura):
		self.base = base
		self.altura = altura

	def CalcularArea(self):
		Area = self.base * self.altura
		return Area

base = int(input('Introduce la base:'))
altura = int(input('Introduce la altura:'))

Calculo = Reactangulo(base, altura)
print(f'El calculo del area es: {Calculo.CalcularArea()}')

