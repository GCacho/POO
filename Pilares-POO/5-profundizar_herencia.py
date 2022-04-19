#Para evitar errores de herencia debido al constructor hay que utilizar super()
class Animales():
    def __init__(self, nombre):
        self.nombre = nombre

class Perro(Animales):
    def __init__(self, nombre, sonido):
        super().__init__(nombre) #Es para heredar el metodo nombre de la clase Animales()
        self.sonido = sonido

perro = Perro("Firulais", "Guauuu!")
print(perro.nombre)
print(perro.sonido)