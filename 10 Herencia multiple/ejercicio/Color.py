class Color:
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def ancho(self, color):
        self._color = color

    def __str__(self):
      print(f'El color de la figura es {self._color}')
