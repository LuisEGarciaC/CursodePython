class Persona:
    # el metodo dunder sirve opametodos o funciones exoeciales de python

    def __init__(self, nombre, apellidos, edad, cedula, sexo):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.cedula = cedula
        self.sexo = sexo

    def desplegar(self):
        print(f'Nombre: {self.nombre}, Apellidos: {self.apellidos} Edad: {self.edad}, Cedula: {self.cedula}, Sexo: {self.sexo}')


persona1 = Persona('luis', 'garcia', 35, 172060666, 'masculino')
persona1.desplegar()
persona2 = Persona('luiss', 'garcias', 45, 172060666, 'masculino')
persona2.desplegar()
