class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self.apellido = apellido
        self._edad = edad

    @property
    def nombre(self):
        print('Llamando método get nombre')
        return self._nombre

    @property
    def edad(self):
        print('Llamando método get edad')
        return self._edad

    @nombre.setter
    def nombre(self, nombre):
        print('Llamando método set nombre')
        self._nombre = nombre

    @edad.setter
    def edad(self, edad):
        print('Llamando método set edad')
        self._edad = edad

    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self.apellido} {self._edad}')

persona1 = Persona('Juan', 'Perez', 28)
persona1.nombre = 'Juan Carlos'
print(persona1.nombre)
persona1.edad = 35
print(persona1.edad)
# persona1._nombre = 'Cambio'
# print(persona1._nore)
