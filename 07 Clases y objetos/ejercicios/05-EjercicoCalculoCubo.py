class Cubo:
    def __init__(self, ancho, profundidad, altura):
        self.ancho = ancho
        self.profundidad = profundidad
        self.altura = altura

    def CacularVolumen(self):
        return self.ancho * self.profundidad * self.altura

Ancho = int(input('Proporciona la ancho: '))
Profundo = int(input('Proporciona la profundidad: '))
Altura = int(input('Proporciona la altura: '))


resultado = Cubo(Ancho, Profundo, Altura).CacularVolumen()
print(f'El volumen del cubo es de: {resultado}')
