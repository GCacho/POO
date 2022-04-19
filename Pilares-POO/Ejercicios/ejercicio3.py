#Crear una clase Fabrica que tenga los atributos de Llantas, 
#Color y Precio; luego crear dos clases mas que hereden de Fabrica,
#las cuales son Moto y Carro. Crear metodos que muestren la 
#cantidad de llantas, color y precio de ambos transportes. 
#Por ultimo, crear objetos para cada clase y mostrar por pantalla 
#los atributos de cada uno

class Fabrica():
    # def __init__(self):
    #     self._llantas = 0
    #     self._color = ""
    #     self._precio = 0

    def descripcion(self):
        print(f"Llantas: {self.llantas}\nColor: {self.color}\nCosto: {self.precio}")

    # @property
    # def llantas(self):
    #     return(self._llantas)
    
    # @llantas.setter
    # def llantas(self, llantas):
    #     self._llantas = llantas
    
    # @property
    # def color(self):
    #     return(self._color)
    
    # @color.setter
    # def color(self, color):
    #     self._color = color
    
    # @property
    # def precio(self):
    #     return(self._precio)
    
    # @precio.setter
    # def precio(self, precio):
    #     self._precio = precio
    
class Moto(Fabrica):
    def __init__(self):
        self.llantas = 2
        self.color = input("De que color quieres la motocicleta?\n--->")
        self.precio = 10000


class Carro(Fabrica):
    def __init__(self):
        self.llantas = 4
        self.color = input("De que color quieres el coche?\n--->")
        self.precio = 50000

if __name__ == "__main__":
    moto1 = Moto()
    moto1.descripcion()
