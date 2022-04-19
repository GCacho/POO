#Realizar un programa en el cual se declaren dos valores enteros 
#por teclado utilizando el método __init__. Calcular después la 
#suma, resta, multiplicación y división. Utilizar un método para
#cada una e imprimir los resultados obtenidos. Llamar a la clase 
#Calculadora.

class Calculadora():
    def __init__(self):
        self._n1 = int(input("Ingrese el primer Valor\n--->"))
        self._n2 = int(input("Ingrese el segundo Valor\n--->"))
    
    def suma(self):
        print(f"La suma de {self.n1} + {self.n2} = {self.n1 + self.n2}")
    
    def resta(self):
        print(f"La resta de {self.n1} - {self.n2} = {self.n1 - self.n2}")
    
    def multiplicacion(self):
        print(f"La multiplicación de {self.n1} x {self.n2} = {self.n1 * self.n2}")
    
    def division(self):
        print(f"La división de {self.n1} ÷ {self.n2} = {self.n1 / self.n2}")
    
    @property
    def n1(self):
        return(self._n1)
    
    @n1.setter
    def n1(self, n1):
        self._n1 = n1

    @property
    def n2(self):
        return(self._n2)
    
    @n2.setter
    def n2(self, n2):
        self._n2 = n2


if __name__ == "__main__":
    calculo1 = Calculadora()
    calculo1.suma()
    calculo1.resta()
    calculo1.multiplicacion()
    calculo1.division()