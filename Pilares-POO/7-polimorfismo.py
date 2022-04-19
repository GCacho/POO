#Es la modificación de métodos cuando se heredan de otras clases
#Crear objetos que usen el mismo método 

class Animales():
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def hablar(self):
        print(self.mensaje) 

class Perro(Animales):
    def hablar(self):
        print("Yo hago Guau!")

class Pez(Animales):
    def hablar(self):
        print("Yo no hablo")

perro = Perro("Guau!")
perro.hablar()

animal = Animales("Miau!")
animal.hablar()

pez = Pez("Nada")
pez.hablar()