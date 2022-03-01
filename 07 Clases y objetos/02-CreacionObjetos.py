class Persona:
    def __init__(self, nombre, apellido, edad):
        # en este caso se esta escribiendo en duro la informacion a mostrar
        self.nombre = 'Juan'
        self.apellido = 'Perez'
        self.edad = 28

persona1 = Persona()
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)
