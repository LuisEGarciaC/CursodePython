# from 10-01-NomenclaturaAtributosMetodos-parte1 import *
class MiClase:
	def __init__(self):
		self.mi_variable_publica=10
		self._mi_variable_protegida=11

#Creamos la prueba de la clase

if __name__ == '__main__':
	objeto=MiClase()
	print(objeto.mi_variable_publica)
	#No deberiamos accederaatributosometodos con un guion bay
	print(objeto._mi_variable_protegida)
	#Accedemosa
