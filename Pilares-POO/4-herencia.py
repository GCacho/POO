class Animales():
    def habla(self):
        print("Yo soy un Animal")

    def descripcion(self):
        print(f"Yo soy una {self.animal}") 

class Perro(Animales): #Hereda los atributos de la clase Animales.
    pass

class Abeja(Animales): #Hereda los atributos de la clase Animales.
    def __init__(self, animal):
        self.animal = animal

animal = Animales()
animal.habla()


perro = Perro()
perro.habla()


abeja = Abeja("Abeja")
abeja.descripcion()